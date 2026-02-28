#!/usr/bin/env python3
"""
Convert Erfindungsbeschreibung PDFs to well-structured Markdown files.
Supports both text-based PDFs (direct extraction) and scanned PDFs (OCR via PyMuPDF + Tesseract).
"""

import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

# PDF directory (relative to project root)
PDF_DIR = Path(__file__).resolve().parent.parent / "Beispiele für Erfindungsmeldungen Formulare"

# Page marker pattern to strip
PAGE_MARKER_RE = re.compile(r"^--\s*\d+\s+of\s+\d+\s+--\s*$", re.MULTILINE)


def is_text_empty_or_only_markers(text: str) -> bool:
    """Check if extracted text is effectively empty (only page markers, whitespace)."""
    cleaned = PAGE_MARKER_RE.sub("", text).strip()
    return len(cleaned) < 50


def extract_text_direct(doc: fitz.Document) -> str:
    """Extract text directly from PDF (for text-based PDFs)."""
    parts = []
    for page in doc:
        parts.append(page.get_text())
    return "\n".join(parts)


def extract_text_ocr(doc: fitz.Document, pdf_path: Path) -> str:
    """OCR via pdf2image + pytesseract (reliable for scanned PDFs)."""
    try:
        from pdf2image import convert_from_path
        import pytesseract
    except ImportError:
        return "[OCR requires: pip install pdf2image pytesseract Pillow. Then: brew install tesseract tesseract-lang poppler]"
    parts = []
    images = convert_from_path(str(pdf_path), dpi=200)
    for i, img in enumerate(images):
        try:
            text = pytesseract.image_to_string(img, lang="deu+eng")
            parts.append(text or "")
        except pytesseract.TesseractError:
            text = pytesseract.image_to_string(img)
            parts.append(text or "")
        except Exception as e:
            parts.append(f"[OCR error on page {i + 1}: {e}]")
    return "\n".join(parts)


# Common German OCR substitutions (é/è often misread as ö, etc.)
OCR_CORRECTIONS = [
    (r"kénnen", "können"),
    (r"Kérper", "Körper"),
    (r"Korper", "Körper"),
    (r"médglich", "möglich"),
    (r"méglich", "möglich"),
    (r"Méglichkeiten", "Möglichkeiten"),
    (r"méglichkeiten", "Möglichkeiten"),
    (r"Méddglichkeiten", "Möglichkeiten"),
    (r"Uberflhren", "Überführen"),
    (r"eréffnet", "eröffnet"),
    (r"erhdhter", "erhöhter"),
    (r"erhdhte", "erhöhte"),
    (r"erhéhte", "erhöhte"),
    (r"erhéhtes", "erhöhtes"),
    (r"ausgeléste", "ausgelöste"),
    (r"ausgeldéste", "ausgelöste"),
    (r"Borinséurefunktion", "Borinsäurefunktion"),
    (r"RinggréBen", "Ringgrößen"),
    (r"Léslichkeiten", "Löslichkeiten"),
    (r"Léslichkeit", "Löslichkeit"),
    (r"weiterflhrenden", "weiterführenden"),
    (r"verknipfen", "verknüpfen"),
    (r"Mégliche", "Mögliche"),
    (r"Veréffentlichungen", "Veröffentlichungen"),
    (r"persénliche", "persönliche"),
    (r"gelést", "gelöst"),
    (r"veréffentlicht", "veröffentlicht"),
    (r"Verdéffentlichungen", "Veröffentlichungen"),
    (r"Vorveréffentlichung", "Vorveröffentlichung"),
    (r"Anwendungsméglichkeiten", "Anwendungsmöglichkeiten"),
    (r"bestméglich", "bestmöglich"),
    (r"erméglicht", "ermöglicht"),
    (r"erméglichen", "ermöglichen"),
    (r"Fur ", "Für "),
    (r" flr ", " für "),
    (r"fiir ", "für "),
    (r"Molekiil", "Molekül"),
    (r"Molekile", "Moleküle"),
    (r"Molekil", "Molekül"),
    (r"Molektile", "Moleküle"),
    (r"Makromolekiil", "Makromolekül"),
    (r"Makromolekile", "Makromoleküle"),
    (r"Antikérper", "Antikörper"),
    (r"Dariiber", "Darüber"),
    (r"nétig", "nötig"),
    (r"ungentgenden", "ungenügenden"),
    (r"Léslichkeiten", "Löslichkeiten"),
    (r"Héhe", "Höhe"),
    (r"zuruickzufordern", "zurückzufordern"),
    (r"weiterfiihrende", "weiterführende"),
    (r"weiterfiihrenden", "weiterführenden"),
    (r"Bioverfiigbarkeit", "Bioverfügbarkeit"),
    (r"Vorlaufermolekiil", "Vorläufermolekül"),
    (r"Vorlaufermolekills", "Vorläufermoleküls"),
    (r"K6rper", "Körper"),
    (r"mUssen", "müssen"),
    (r"Markermolekille", "Markermoleküle"),
    (r"Wirkstoffmolektile", "Wirkstoffmoleküle"),
    (r"auBerdem", "außerdem"),
    (r"unabhangigen", "unabhängigen"),
    (r"eingeschrankt", "eingeschränkt"),
    (r"beschranken", "beschränken"),
    (r" tiber ", " über "),
    (r"zusatzlichen", "zusätzlichen"),
]


def post_process(text: str) -> str:
    """Clean and normalize extracted text."""
    # Remove page markers
    text = PAGE_MARKER_RE.sub("", text)
    # Merge single-word lines that are PDF layout artifacts (e.g. "Grundsätzlich\nist\ndas\nSystem")
    lines = text.split("\n")
    merged = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Collect consecutive short lines (single word/token) and merge with space
        # Single-word lines from PDF column layout - merge if 3+ consecutive
        stripped = line.strip()
        if stripped and not re.match(r"^#{1,6}\s", line) and " " not in stripped and stripped not in ("-", "•", "–"):
            chunk = [stripped]
            j = i + 1
            while j < len(lines):
                s = lines[j].strip()
                if not s or " " in s or re.match(r"^#{1,6}\s", lines[j]) or s in ("-", "•", "–"):
                    break
                chunk.append(s)
                j += 1
            if len(chunk) >= 3:  # Only merge if 3+ short lines
                merged.append(" ".join(chunk))
                i = j
                continue
        merged.append(line)
        i += 1
    text = "\n".join(merged)
    # Apply German OCR corrections
    for wrong, right in OCR_CORRECTIONS:
        text = text.replace(wrong, right)
    # Normalize excessive line breaks (more than 2 consecutive newlines -> 2)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def detect_headings(text: str) -> str:
    """
    Promote known section titles to markdown headings.
    Common Erfindungsbeschreibung sections.
    """
    section_patterns = [
        (r"^Technische Aufgabe und Gebiet\s*$", "## Technische Aufgabe und Gebiet"),
        (r"^Stand der Technik\s*$", "## Stand der Technik"),
        (r"^Behebung bisheriger technischer Probleme / Nachteile\s*$", "## Behebung bisheriger technischer Probleme / Nachteile"),
        (r"^Technische Lösung\s*$", "## Technische Lösung"),
        (r"^Literaturverzeichnis\s*$", "## Literaturverzeichnis"),
        (r"^Probleme/Nachteile:\s*$", "### Probleme/Nachteile"),
        (r"^Vorteile gegenüber dem aktuellen Stand der Technik\s*", "### Vorteile gegenüber dem aktuellen Stand der Technik"),
    ]
    lines = text.split("\n")
    result = []
    for line in lines:
        matched = False
        for pattern, replacement in section_patterns:
            if re.match(pattern, line.strip()):
                result.append(replacement)
                matched = True
                break
        if not matched:
            result.append(line)
    return "\n".join(result)


def pdf_to_markdown(
    pdf_path: Path,
    output_path: Path,
    source_abbrev: str,
    use_ocr: bool | None = None,
) -> tuple[str, int, bool]:
    """
    Convert a PDF to Markdown.
    Returns (summary_placeholder, page_count, used_ocr).
    """
    doc = fitz.open(pdf_path)
    page_count = len(doc)

    # Try direct extraction first (unless OCR forced)
    if use_ocr is False:
        raw = extract_text_direct(doc)
        used_ocr = False
    elif use_ocr is True:
        raw = extract_text_ocr(doc, pdf_path)
        used_ocr = True
    else:
        raw = extract_text_direct(doc)
        if is_text_empty_or_only_markers(raw):
            raw = extract_text_ocr(doc, pdf_path)
            used_ocr = True
        else:
            used_ocr = False

    doc.close()

    body = post_process(raw)
    body = detect_headings(body)

    # Build frontmatter (summary to be filled in later)
    summary_placeholder = (
        f"Erfindungsmeldung (Anlage 1) der {source_abbrev}. "
        f"Beispiel für eine strukturierte Erfindungsbeschreibung im deutschen Patentformat."
    )

    frontmatter = f"""---
summary: |
  {summary_placeholder}
source: {source_abbrev}
pages: {page_count}
extraction: {"OCR" if used_ocr else "text"}
---

# Erfindungsbeschreibung

"""

    full_content = frontmatter + body
    output_path.write_text(full_content, encoding="utf-8")

    return summary_placeholder, page_count, used_ocr


def main():
    pdfs = [
        ("Erfindungsbeschreibung_HM.pdf", "HM"),
        ("Erfindungsbeschreibung_TUM.pdf", "TUM"),
        ("Erfindungsbeschreibung_THI.pdf", "THI"),
        ("Erfindungsbeschreibung JMU.pdf", "JMU"),
    ]

    if not PDF_DIR.exists():
        print(f"Error: PDF directory not found: {PDF_DIR}")
        sys.exit(1)

    for pdf_name, source in pdfs:
        pdf_path = PDF_DIR / pdf_name
        if not pdf_path.exists():
            print(f"Skipping (not found): {pdf_name}")
            continue

        # Output: Erfindungsbeschreibung_JMU.md (normalize space in JMU filename)
        md_name = pdf_name.replace(" ", "_").replace(".pdf", ".md")
        output_path = PDF_DIR / md_name

        print(f"Converting {pdf_name} -> {md_name} ...")
        try:
            summary, pages, used_ocr = pdf_to_markdown(pdf_path, output_path, source)
            mode = "OCR" if used_ocr else "text"
            print(f"  Done: {pages} pages, extraction={mode}")
        except Exception as e:
            print(f"  Error: {e}")
            raise

    print("Conversion complete.")


if __name__ == "__main__":
    main()
