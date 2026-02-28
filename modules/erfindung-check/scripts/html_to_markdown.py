#!/usr/bin/env python3
"""
Export Erfindung-Check Webversion to Markdown files.
Parses erfindung-check.html and creates one Markdown file per step in Export/.
"""

import os
import re
from pathlib import Path

from bs4 import BeautifulSoup

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_DIR = SCRIPT_DIR.parent
HTML_PATH = MODULE_DIR / "optimized" / "ui" / "erfindung-check.html"
EXPORT_DIR = MODULE_DIR / "Export"

# Step index to filename mapping
STEP_FILES = [
    "00-Einleitung.md",
    "01-Kategorie-waehlen.md",
    "02-Markt-scannen.md",
    "03-Prior-Art-suchen.md",
    "04-Treffer-bewerten.md",
    "05-Kern-schaerfen.md",
    "06-Ergebnis-ableiten.md",
]


def expand_tooltips(soup):
    """Replace tooltip-wrap with inline text (term (tooltip))."""
    for wrap in soup.find_all(class_="tooltip-wrap"):
        tooltip_span = wrap.find(class_="tooltip-text")
        if tooltip_span:
            tooltip_text = tooltip_span.get_text(strip=True)
            term = "".join(c.strip() for c in wrap.children if isinstance(c, str)).strip()
            if not term:
                term = wrap.get_text(strip=True).replace(tooltip_text, "").strip() or tooltip_text.split("=")[0].strip()
            replacement = f"{term} ({tooltip_text}) "
        else:
            replacement = wrap.get_text(strip=True)
        wrap.replace_with(replacement)
    return soup


def element_to_markdown(el, indent=0):
    """Convert a BeautifulSoup element to Markdown string."""
    if el is None:
        return ""
    if isinstance(el, str):
        return el

    text_parts = []

    for child in el.children:
        if isinstance(child, str):
            text_parts.append(child)
            continue

        if child.name == "a":
            href = child.get("href", "#")
            text_parts.append(f"[{child.get_text(strip=True)}]({href})")
        elif child.name == "strong":
            text_parts.append(f"**{child.get_text(strip=True)}**")
        elif child.name == "em":
            text_parts.append(f"*{child.get_text(strip=True)}*")
        elif child.name == "code":
            text_parts.append(f"`{child.get_text(strip=True)}`")
        elif child.name == "br":
            text_parts.append("\n")
        elif child.name in ("h1", "h2", "h3", "h4"):
            level = int(child.name[1])
            text_parts.append("\n" + "#" * level + " " + child.get_text(strip=True) + "\n")
        elif child.name == "p":
            text_parts.append("\n" + element_to_markdown(child) + "\n")
        elif child.name == "ul":
            items = []
            for li in child.find_all("li", recursive=False):
                items.append("- " + element_to_markdown(li).strip())
            text_parts.append("\n" + "\n".join(items) + "\n")
        elif child.name == "ol":
            items = []
            for i, li in enumerate(child.find_all("li", recursive=False), 1):
                items.append(f"{i}. " + element_to_markdown(li).strip())
            text_parts.append("\n" + "\n".join(items) + "\n")
        elif child.name == "blockquote":
            inner = element_to_markdown(child).strip()
            lines = inner.split("\n")
            text_parts.append("\n" + "\n".join("> " + line for line in lines) + "\n")
        elif child.name == "table":
            text_parts.append(table_to_markdown(child))
        elif child.name == "details":
            summary = child.find("summary")
            summary_text = summary.get_text(strip=True) if summary else "Details"
            inner = element_to_markdown(child).strip()
            text_parts.append(f"\n**{summary_text}**\n{inner}\n")
        elif child.name == "div" and "wizard-table-wrap" in child.get("class", []):
            table = child.find("table")
            if table:
                text_parts.append(table_to_markdown(table))
        elif child.name == "div" and "limitations" in child.get("class", []):
            parts = ["> **⚠️ Wichtige Grenze**"]
            for p in child.find_all("p"):
                parts.append("> " + element_to_markdown(p).replace("\n", "\n> "))
            for ul in child.find_all("ul"):
                for li in ul.find_all("li", recursive=False):
                    parts.append("> - " + element_to_markdown(li).replace("\n", " "))
            text_parts.append("\n" + "\n".join(parts) + "\n")
        else:
            text_parts.append(element_to_markdown(child))

    return "".join(text_parts).strip()


def table_to_markdown(table):
    """Convert HTML table to Markdown table."""
    rows = []
    for tr in table.find_all("tr"):
        cells = []
        for cell in tr.find_all(["th", "td"]):
            cells.append(element_to_markdown(cell).replace("\n", " ").strip())
        rows.append(cells)

    if not rows:
        return ""

    # Determine column count
    col_count = max(len(r) for r in rows)

    # Pad rows if needed
    for row in rows:
        while len(row) < col_count:
            row.append("")

    lines = []
    # Header
    lines.append("| " + " | ".join(rows[0]) + " |")
    lines.append("| " + " | ".join("---" for _ in rows[0]) + " |")
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")

    return "\n" + "\n".join(lines) + "\n"


def block_to_markdown(block):
    """Convert a wizard-block to Markdown."""
    parts = []

    # Block label (Deine Aufgabe, Beispiel, Tipp)
    label_el = block.find(class_="block-label")
    if label_el:
        label = label_el.get_text(strip=True)
        label_el.decompose()

    # Check block type
    classes = block.get("class", [])
    is_limitations = "limitations" in classes
    is_handoff = "handoff" in block.get("class", [])

    if is_limitations:
        parts.append("\n> **⚠️ Wichtige Grenze**\n")
        for p in block.find_all("p"):
            parts.append("> " + element_to_markdown(p) + "\n")
        for ul in block.find_all("ul"):
            for li in ul.find_all("li", recursive=False):
                parts.append("> - " + element_to_markdown(li) + "\n")
        return "\n".join(parts)

    # Regular block content
    for child in block.children:
        if isinstance(child, str) and not child.strip():
            continue
        if hasattr(child, "name") and child.name in ("div", "span") and "block-label" in child.get("class", []):
            continue

        content = element_to_markdown(child) if hasattr(child, "children") else str(child)
        if content.strip():
            parts.append(content)

    result = "\n".join(parts).strip()

    # Add section header based on block type
    if label_el and "block-label" in str(block):
        pass  # label already extracted

    if "wizard-block-action" in classes and label_el:
        result = "## Deine Aufgabe\n\n" + result
    elif "wizard-block-info" in classes:
        h3 = block.find("h3")
        if h3:
            h3_text = h3.get_text(strip=True)
            result = f"## {h3_text}\n\n" + result
            result = re.sub(r"^###\s*" + re.escape(h3_text) + r"\s*\n+", "", result, count=1)
    elif "wizard-block-example" in classes:
        h3 = block.find("h3")
        if h3:
            h3_text = h3.get_text(strip=True)
            result = f"## Beispiel: {h3_text}\n\n" + result
            result = re.sub(r"^###\s*" + re.escape(h3_text) + r"\s*\n+", "", result, count=1)
        else:
            result = "## Beispiel\n\n" + result
    elif "wizard-block-tip" in classes:
        h3 = block.find("h3")
        if h3:
            h3_text = h3.get_text(strip=True)
            result = f"## Tipp: {h3_text}\n\n" + result
            result = re.sub(r"^###\s*" + re.escape(h3_text) + r"\s*\n+", "", result, count=1)
        else:
            result = "## Tipp\n\n" + result
    elif is_handoff:
        result = re.sub(r"^#+\s*Du bringst in den nächsten Schritt mit\s*\n+", "", result, count=1)
        result = "## Du bringst in den nächsten Schritt mit\n\n" + result

    return result


def process_step(step_el, step_index, next_filename):
    """Process a wizard-step and return Markdown content."""
    title_el = step_el.find(class_="wizard-step-title")
    title = title_el.get_text(strip=True) if title_el else f"Schritt {step_index}"

    # Expand tooltips in title
    if title_el:
        expand_tooltips(title_el)
        title = title_el.get_text(strip=True)
        title = re.sub(r"\)([a-zA-ZäöüÄÖÜß])", r") \1", title)  # Ensure space after tooltip before word

    md_parts = [f"# Schritt {step_index}: {title}\n"]

    def is_block(classes):
        if not classes:
            return False
        c = classes if isinstance(classes, list) else [classes]
        return any("wizard-block" in str(x) or x in ("handoff", "limitations") for x in c)

    # Only process direct children to avoid nested blocks (e.g. limitations inside info)
    for block in step_el.find_all("div", class_=is_block, recursive=False):
        classes = block.get("class", [])
        if "wizard-table-wrap" in classes:
            continue

        expand_tooltips(block)
        content = block_to_markdown(block)
        if content.strip():
            md_parts.append(content)
            md_parts.append("")

    if next_filename:
        md_parts.append("\n---\n")
        md_parts.append(f"*Nächster Schritt: [{next_filename}]({next_filename})*")

    return "\n".join(md_parts).strip()


def main():
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    steps = soup.find_all("div", class_="wizard-step", attrs={"data-step": True})
    steps = sorted(steps, key=lambda s: int(s.get("data-step", 0)))

    for i, step_el in enumerate(steps):
        next_file = STEP_FILES[i + 1] if i + 1 < len(STEP_FILES) else None
        md_content = process_step(step_el, i, next_file)

        out_path = EXPORT_DIR / STEP_FILES[i]
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"  Wrote {out_path.name}")

    print(f"\nExported {len(steps)} Markdown files to {EXPORT_DIR}")

    # Phase 2: Concatenate and create Word document
    import subprocess
    import sys
    script_dir = Path(__file__).resolve().parent
    print("\n--- Phase 2: Word export ---")
    subprocess.run([sys.executable, str(script_dir / "markdown_to_docx.py")], check=True, cwd=str(script_dir))


if __name__ == "__main__":
    main()
