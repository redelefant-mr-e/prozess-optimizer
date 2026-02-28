#!/usr/bin/env python3
"""
Extract before/after versions from a Word document with track changes.
Before = original (deletions included, insertions excluded)
After = revised (insertions included, deletions excluded)
"""

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# Default paths
DEFAULT_DOCX = Path(
    "/Users/felixegidi/Library/CloudStorage/Dropbox/01- Red Elephant/05 - Projects/BayPAT/Erfinderguide/Erfinderguide von Red Elephant_KR00.docx"
)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = PROJECT_ROOT / "Erfinderguide-ClientReview"

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def get_style(elem):
    """Get paragraph style from w:pPr/w:pStyle."""
    pPr = elem.find("w:pPr", NS)
    if pPr is None:
        return None
    pStyle = pPr.find("w:pStyle", NS)
    if pStyle is None:
        return None
    return pStyle.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val")


def get_text_from_elem(elem, mode):
    """
    Extract text from element, respecting track changes.
    mode: "before" = include w:del, exclude w:ins
          "after"  = include w:ins, exclude w:del
    """
    parts = []

    def walk(e, in_ins=False, in_del=False):
        tag = e.tag.split("}")[-1] if "}" in e.tag else e.tag

        if tag == "ins":
            if mode == "after":
                if e.text:
                    parts.append(e.text)
                for c in e:
                    walk(c, in_ins=True, in_del=in_del)
            if e.tail:
                parts.append(e.tail)
            return

        if tag == "del":
            if mode == "before":
                if e.text:
                    parts.append(e.text)
                for c in e:
                    walk(c, in_ins=in_ins, in_del=True)
            if e.tail:
                parts.append(e.tail)
            return

        if tag == "t":
            should_include = (
                (not in_ins and not in_del)
                or (in_ins and mode == "after")
                or (in_del and mode == "before")
            )
            if should_include and e.text:
                parts.append(e.text)
            for c in e:
                walk(c, in_ins=in_ins, in_del=in_del)
            if should_include and e.tail:
                parts.append(e.tail)
            return

        if tag == "tab":
            should_include = (
                (not in_ins and not in_del)
                or (in_ins and mode == "after")
                or (in_del and mode == "before")
            )
            if should_include:
                parts.append("\t")
            if e.tail:
                parts.append(e.tail)
            return

        if tag == "br":
            should_include = (
                (not in_ins and not in_del)
                or (in_ins and mode == "after")
                or (in_del and mode == "before")
            )
            if should_include:
                parts.append("\n")
            if e.tail:
                parts.append(e.tail)
            return

        # Default: other elements (r, p, body, etc.)
        should_include = (
            (not in_ins and not in_del)
            or (in_ins and mode == "after")
            or (in_del and mode == "before")
        )
        if should_include and e.text:
            parts.append(e.text)
        for c in e:
            walk(c, in_ins=in_ins, in_del=in_del)
        if should_include and e.tail:
            parts.append(e.tail)

    walk(elem)
    return "".join(parts)


def get_paragraph_text(p_elem, mode):
    """Get text from a w:p element."""
    return get_text_from_elem(p_elem, mode).strip()


def get_cell_text(tc_elem, mode):
    """Get text from a table cell (w:tc)."""
    parts = []
    for p in tc_elem.findall(".//w:p", NS):
        t = get_paragraph_text(p, mode)
        if t:
            parts.append(t)
    return " | ".join(parts).replace("\n", " ")


def get_table_markdown(tbl_elem, mode):
    """Convert w:tbl to Markdown table."""
    rows = []
    for tr in tbl_elem.findall(".//w:tr", NS):
        cells = []
        for tc in tr.findall("w:tc", NS):
            cells.append(get_cell_text(tc, mode))
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    lines = ["| " + " | ".join(rows[0]) + " |"]
    lines.append("| " + " | ".join("---" for _ in rows[0]) + " |")
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n" + "\n".join(lines) + "\n"


def process_body(body, mode):
    """Process w:body and return list of (type, content) for Markdown."""
    result = []
    for child in body:
        tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
        if tag == "p":
            style = get_style(child)
            text = get_paragraph_text(child, mode)
            if not text and not style:
                continue
            if style and "Heading" in (style or ""):
                level = 1
                if "2" in (style or ""):
                    level = 2
                elif "3" in (style or ""):
                    level = 3
                result.append(("heading", level, text))
            elif text:
                result.append(("para", text))
        elif tag == "tbl":
            md = get_table_markdown(child, mode)
            if md.strip():
                result.append(("table", md))
    return result


def to_markdown(items):
    """Convert processed items to Markdown string."""
    lines = []
    for item in items:
        if item[0] == "heading":
            level, text = item[1], item[2]
            if text:
                lines.append("#" * level + " " + text)
                lines.append("")
        elif item[0] == "para":
            text = item[1]
            if text:
                lines.append(text)
                lines.append("")
        elif item[0] == "table":
            lines.append(item[1].strip())
            lines.append("")
    return "\n".join(lines).strip()


def main():
    parser = argparse.ArgumentParser(description="Extract before/after from Word docx with track changes")
    parser.add_argument("--input", "-i", type=Path, default=DEFAULT_DOCX, help="Path to docx file")
    parser.add_argument("--output", "-o", type=Path, default=DEFAULT_OUTPUT, help="Output directory")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        print("Ensure Dropbox is synced and the file is accessible.", file=sys.stderr)
        sys.exit(1)

    try:
        import zipfile

        with zipfile.ZipFile(args.input, "r") as z:
            xml_data = z.read("word/document.xml")
    except Exception as e:
        print(f"Error reading docx: {e}", file=sys.stderr)
        sys.exit(1)

    root = ET.fromstring(xml_data)
    body = root.find(".//w:body", NS)
    if body is None:
        print("Error: No body found in document", file=sys.stderr)
        sys.exit(1)

    before_items = process_body(body, "before")
    after_items = process_body(body, "after")

    args.output.mkdir(parents=True, exist_ok=True)

    before_md = to_markdown(before_items)
    after_md = to_markdown(after_items)

    (args.output / "Erfinderguide-BEFORE.md").write_text(before_md, encoding="utf-8")
    print(f"  Wrote {args.output / 'Erfinderguide-BEFORE.md'}")

    (args.output / "Erfinderguide-AFTER.md").write_text(after_md, encoding="utf-8")
    print(f"  Wrote {args.output / 'Erfinderguide-AFTER.md'}")

    readme = f"""# Erfinderguide – Client Review Before/After

Extracted from: `{args.input.name}`

## Files

- **Erfinderguide-BEFORE.md** – Original text (client deletions shown, insertions hidden)
- **Erfinderguide-AFTER.md** – Revised text (client insertions shown, deletions hidden)

## Source

Word document with track changes (KR00 = Korrektur/Revision). Run the extraction script to regenerate:

```bash
python3 scripts/extract_erfinderguide_review.py
```
"""
    (args.output / "README.md").write_text(readme, encoding="utf-8")
    print(f"  Wrote {args.output / 'README.md'}")

    print(f"\nExtraction complete. Output: {args.output}")


if __name__ == "__main__":
    main()
