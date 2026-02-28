#!/usr/bin/env python3
"""Export Patent Next Steps from HTML to Markdown, Notion, and Word."""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.export_process import export_process

MODULE_DIR = Path(__file__).resolve().parent.parent
HTML_PATH = MODULE_DIR / "optimized" / "ui" / "patent-next-steps-V4.html"
EXPORT_DIR = MODULE_DIR / "Export"

STEP_FILES = [
    "00-Einleitung.md",
    "01-Standort-und-Ansprechpartnerinnen.md",
    "02-Zeitfenster-beachten.md",
    "03-Schutzstrategie-waehlen.md",
    "04-Prioritaeten-setzen.md",
    "05-Ergebnis.md",
]

if __name__ == "__main__":
    export_process(
        html_path=HTML_PATH,
        export_dir=EXPORT_DIR,
        step_files=STEP_FILES,
        process_title="Patent Next Steps",
        output_base="Patent-Next-Steps",
    )
