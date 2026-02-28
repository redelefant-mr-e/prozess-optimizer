#!/usr/bin/env python3
"""
Build patent-next-steps-V3.html from refined-V3 markdown.
Uses GPT to convert markdown content into the wizard HTML structure.
"""

import os
from pathlib import Path

MODULE_DIR = Path(__file__).parent.parent
PROJECT_ROOT = MODULE_DIR.parent.parent
env_path = PROJECT_ROOT / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ[key.strip()] = value.strip()

from openai import OpenAI

MD_DIR = MODULE_DIR / "optimized" / "refined-V3"
TEMPLATE_HTML = MODULE_DIR / "optimized" / "ui" / "patent-next-steps-V2.html"
OUTPUT_HTML = MODULE_DIR / "optimized" / "ui" / "patent-next-steps-V3.html"

STEP_FILES = [
    "00-Einleitung.md", "01-Standort-und-Ansprechpartner.md",
    "02-Zeitfenster-beachten.md", "03-Schutzstrategie-waehlen.md",
    "04-Prioritaeten-setzen.md", "05-Ergebnis.md"
]


def load_all_md():
    parts = []
    for f in STEP_FILES:
        p = MD_DIR / f
        if p.exists():
            parts.append(f"=== {f} ===\n{p.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


def main():
    template = TEMPLATE_HTML.read_text(encoding="utf-8")
    md_content = load_all_md()

    client = OpenAI()
    prompt = """Du bekommst:
1. Eine HTML-Datei (patent-next-steps-V2.html) mit der Wizard-Struktur
2. Die überarbeiteten Markdown-Inhalte (refined-V3) – fließender, weniger bullet-point-lastig

Deine Aufgabe: Erstelle eine neue patent-next-steps-V3.html, in der du den HTML-Rahmen (head, CSS, Scripts, wizard-container, wizard-progress, wizard-nav Buttons) UNVERÄNDERT lässt, aber den INHALT jedes wizard-step durch den entsprechenden V3-Markdown-Inhalt ersetzt.

Regeln:
- Jeder Schritt (00–05) hat ein <div class="wizard-step" data-step="N"> mit Inhalt
- Die V3-Texte sind länger und prosaartiger – konvertiere sie in die gleiche HTML-Struktur: wizard-block, wizard-block-info, wizard-block-action, wizard-block-example, wizard-block-context, wizard-block-tip, limitations
- Tabellen: <div class="wizard-table-wrap"><table class="wizard-table">...</table></div>
- Code/E-Mail-Vorlagen: <pre>...</pre>
- Überschriften: <h3>, <h4>
- Paragraphen: <p>
- Listen: <ol>, <ul>, <li>
- Beispiel-Blöcke: <div class="wizard-block wizard-block-example"><span class="block-label">Beispiel: Maria</span>...
- Ziel-Blöcke: <div class="wizard-block wizard-block-action"><span class="block-label">Ziel</span>...
- Spezifisch für Kontext: wizard-block-context
- Tipp: wizard-block-tip
- Wichtige Grenze: wizard-block limitations
- "Nächster Schritt" Links am Ende eines Schritts: WEGLASSEN (wir haben wizard-nav Buttons)
- WICHTIG: Am Ende der Datei MÜSSEN die Script-Tags stehen:
  <script src="../../../../shared/design-templates/step-wizard/step-wizard.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      if (typeof initStepWizard === 'function') {
        initStepWizard(document.getElementById('wizard'), { startAt: 0 });
      }
    });
  </script>
- Letzter Schritt (Schritt 5): NUR "Zurück"-Button, KEIN "Weiter"-Button
- Titel im Header: "Patent Next Steps V3" (statt V2)
- Gib NUR die vollständige HTML-Datei aus, keine Erklärung."""

    messages = [
        {"role": "system", "content": "Du konvertierst Markdown-Inhalte in die vorgegebene HTML-Wizard-Struktur. Output: vollständige HTML-Datei."},
        {"role": "user", "content": f"{prompt}\n\n---\n\n## Template HTML\n\n{template[:8000]}...\n\n---\n\n## V3 Markdown Content\n\n{md_content}"}
    ]

    # Content might be too long; split into two calls if needed
    full_content = f"{prompt}\n\n---\n\n## Template HTML (first 12000 chars)\n\n{template[:12000]}\n\n---\n\n## V3 Markdown Content\n\n{md_content}"
    if len(full_content) > 100000:
        # Truncate md if needed
        md_content = md_content[:60000] + "\n\n[... truncated for length ...]"
        full_content = f"{prompt}\n\n---\n\n## Template HTML\n\n{template[:10000]}\n\n---\n\n## V3 Markdown Content\n\n{md_content}"

    messages = [
        {"role": "system", "content": "Du konvertierst Markdown-Inhalte in die vorgegebene HTML-Wizard-Struktur. Output: vollständige HTML-Datei, keine Erklärung."},
        {"role": "user", "content": full_content}
    ]

    print("Calling API to build HTML...")
    try:
        r = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.2,
        )
    except Exception as e:
        print(f"Error: {e}")
        return

    html = r.choices[0].message.content
    # Strip markdown code block if present
    if html.startswith("```"):
        html = html.split("\n", 1)[1]
    if html.endswith("```"):
        html = html.rsplit("```", 1)[0]
    html = html.strip()

    # Ensure script tags are present (model sometimes drops them)
    wizard_script = '''<script src="../../../../shared/design-templates/step-wizard/step-wizard.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    if (typeof initStepWizard === 'function') {
      initStepWizard(document.getElementById('wizard'), { startAt: 0 });
    }
  });
</script>'''
    if 'step-wizard.js' not in html:
        html = html.replace('</body>', wizard_script + '\n</body>')

    OUTPUT_HTML.write_text(html, encoding="utf-8")
    print(f"Written: {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
