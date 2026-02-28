#!/usr/bin/env python3
"""Export Erfindungsbeschreibung from HTML to Markdown, Notion, and Word."""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.export_process import export_process

MODULE_DIR = Path(__file__).resolve().parent.parent
HTML_PATH = MODULE_DIR / "optimized" / "ui" / "erfindungsbeschreibung.html"
EXPORT_DIR = MODULE_DIR / "Export"

STEP_FILES = [
    "00-Einleitung.md",
    "01-Kern-der-Neuerung.md",
    "02-Stand-der-Technik.md",
    "03-Technische-Loesung.md",
    "04-Struktur-und-Form.md",
    "05-Fehler-vermeiden.md",
    "06-Ergebnis.md",
]

if __name__ == "__main__":
    export_process(
        html_path=HTML_PATH,
        export_dir=EXPORT_DIR,
        step_files=STEP_FILES,
        process_title="Erfindungsbeschreibung",
        output_base="Erfindungsbeschreibung",
    )
