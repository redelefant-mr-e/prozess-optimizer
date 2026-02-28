#!/usr/bin/env python3
"""
Build Erfinderguide V2 app – outputs V1 (Erfindung-Check) content.
Copies the original Erfindung-Check wizard and adjusts paths for the Erfinderguide-V2 folder.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "Erfinderguide-V2"
ERFINDUNG_CHECK_HTML = PROJECT_ROOT / "modules/erfindung-check/optimized/ui/erfindung-check.html"


def build_html():
    """Copy Erfindung-Check HTML and adjust paths for Erfinderguide-V2."""
    html = ERFINDUNG_CHECK_HTML.read_text(encoding="utf-8")

    # Adjust paths: from modules/erfindung-check/optimized/ui/ (4 levels up) to Erfinderguide-V2/ (1 level up)
    html = html.replace("../../../../shared/", "../shared/")
    html = html.replace("../../../../index.html", "../index.html")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "erfinderguide-v2.html").write_text(html, encoding="utf-8")
    print(f"Wrote {OUTPUT_DIR / 'erfinderguide-v2.html'}")


if __name__ == "__main__":
    build_html()
