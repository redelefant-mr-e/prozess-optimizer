#!/usr/bin/env python3
"""
Build script for GitHub Pages deployment.
Creates deploy/ with flat structure and rewritten paths.
Run from project root: python scripts/build_deploy.py
"""

import os
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEPLOY_DIR = PROJECT_ROOT / "deploy"

# Path rewrites for index.html
INDEX_REWRITES = [
    ("href=\"modules/erfindung-check/optimized/ui/erfindung-check.html\"", "href=\"erfindung-check.html\""),
    ("href=\"modules/patent-next-steps/optimized/ui/patent-next-steps-V4.html\"", "href=\"patent-next-steps.html\""),
    ("href=\"modules/erfindungsbeschreibung/optimized/ui/erfindungsbeschreibung.html\"", "href=\"erfindungsbeschreibung.html\""),
    ("href=\"shared/design-templates/step-wizard/step-wizard.css\"", "href=\"step-wizard.css\""),
]

# Path rewrites for module HTML (guides)
MODULE_REWRITES = [
    ("href=\"../../../../shared/design-templates/step-wizard/step-wizard.css\"", "href=\"step-wizard.css\""),
    ("src=\"../../../../shared/design-templates/step-wizard/step-wizard.js\"", "src=\"step-wizard.js\""),
    ("href=\"../../../../index.html\"", "href=\"index.html\""),
]

# patent-next-steps specific: internal link to erfindung-check
PATENT_NEXT_STEPS_REWRITES = [
    ("href=\"../../../erfindung-check/optimized/ui/erfindung-check.html\"", "href=\"erfindung-check.html\""),
]

DEPLOY_README = """# Prozess-Optimizer Guides

Interactive guides for Erfindung-Check, Patentierungsprozess, and Erfindungsbeschreibung.

## Deploy to GitHub Pages

1. Create a new repository on GitHub (e.g. `prozess-optimizer` or `process-optimizer-guides`)
2. In this folder, run:
   ```
   git init
   git add .
   git commit -m "Initial: interactive guides"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
3. In the repo: Settings > Pages > Source: Deploy from a branch > main / root
4. Site will be at https://YOUR_USERNAME.github.io/YOUR_REPO/
"""


def rewrite(content: str, rewrites: list[tuple[str, str]]) -> str:
    for old, new in rewrites:
        content = content.replace(old, new)
    return content


def main():
    # Create or clear deploy dir
    if DEPLOY_DIR.exists():
        shutil.rmtree(DEPLOY_DIR)
    DEPLOY_DIR.mkdir(parents=True)

    # Copy CSS and JS
    shared = PROJECT_ROOT / "shared" / "design-templates" / "step-wizard"
    shutil.copy(shared / "step-wizard.css", DEPLOY_DIR / "step-wizard.css")
    shutil.copy(shared / "step-wizard.js", DEPLOY_DIR / "step-wizard.js")

    # Copy and rewrite index.html
    index_src = PROJECT_ROOT / "index.html"
    index_content = index_src.read_text(encoding="utf-8")
    index_content = rewrite(index_content, INDEX_REWRITES)
    (DEPLOY_DIR / "index.html").write_text(index_content, encoding="utf-8")

    # Copy and rewrite guide HTML files
    guides = [
        (PROJECT_ROOT / "modules" / "erfindung-check" / "optimized" / "ui" / "erfindung-check.html", "erfindung-check.html", []),
        (PROJECT_ROOT / "modules" / "patent-next-steps" / "optimized" / "ui" / "patent-next-steps-V4.html", "patent-next-steps.html", PATENT_NEXT_STEPS_REWRITES),
        (PROJECT_ROOT / "modules" / "erfindungsbeschreibung" / "optimized" / "ui" / "erfindungsbeschreibung.html", "erfindungsbeschreibung.html", []),
    ]

    for src_path, dest_name, extra_rewrites in guides:
        content = src_path.read_text(encoding="utf-8")
        content = rewrite(content, MODULE_REWRITES)
        content = rewrite(content, extra_rewrites)
        (DEPLOY_DIR / dest_name).write_text(content, encoding="utf-8")

    # Write deploy README
    (DEPLOY_DIR / "README.md").write_text(DEPLOY_README, encoding="utf-8")

    print("Deploy build complete. Output in deploy/")


if __name__ == "__main__":
    main()
