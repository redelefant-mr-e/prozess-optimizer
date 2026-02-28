#!/usr/bin/env python3
"""Export all process modules to Markdown, Notion, and Word."""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODULES = [
    ("erfindung-check", "html_to_markdown.py"),
    ("patent-next-steps", "export_to_markdown.py"),
    ("erfindungsbeschreibung", "export_to_markdown.py"),
]

if __name__ == "__main__":
    for module, script in MODULES:
        script_path = PROJECT_ROOT / "modules" / module / "scripts" / script
        if script_path.exists():
            print(f"\n=== {module} ===")
            subprocess.run([sys.executable, str(script_path)], check=True, cwd=str(PROJECT_ROOT))
        else:
            print(f"  Skip {module}: {script} not found")
