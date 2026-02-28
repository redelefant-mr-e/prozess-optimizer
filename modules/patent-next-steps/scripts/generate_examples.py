#!/usr/bin/env python3
"""
Generates a coherent example that shows how the Patent Next Steps process evolves.
Uses OpenAI to create realistic, consistent examples for each step.
Output: PROZESS-BEISPIEL.json in optimized/steps/
"""

import os
import json
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

try:
    from openai import OpenAI
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "openai", "-q"])
    from openai import OpenAI

BASE = MODULE_DIR / "optimized" / "steps"


def generate_example():
    """Use AI to generate a coherent example through all process steps."""
    client = OpenAI()
    
    prompt = """Create a coherent, realistic example for the Patent Next Steps process (Erfindung – Nächste Schritte). The example must show how the process EVOLVES step by step – each step builds on the previous.

**Example inventor:** Choose ONE concrete scenario (e.g., "Postdoc at university with software invention" or "Engineer at Mittelstand company with mechanical prototype" – something plausible for the academic/research context).

**Output as JSON** with these exact keys. Use German for all content. Be specific and realistic:

```json
{
  "erfindung_kurz": "One-sentence description of the example invention",
  "kontext": "Uni|Firma|Startup",
  "meldepflicht": true,
  "erste_ansprechpartner": "TTO|Patentstelle|Vorgesetzte|IHK",
  "kontakt_liste": [
    {"prioritaet": 1, "rolle": "TTO", "wann": "Sofort"},
    {"prioritaet": 2, "rolle": "Patentanwalt", "wann": "Nach Strategie-Klärung"}
  ],
  "zeitfenster_checkliste": [
    "Meldung an TTO vor Veröffentlichung",
    "Kein Paper einreichen vor Patentstrategie"
  ],
  "schutzstrategie": "Patent|Publikation|Trade Secret|Kombination",
  "strategie_begruendung": "1-2 Sätze warum",
  "prioritaeten": [
    "Meldung an TTO",
    "Gespräch mit TTO zur Strategie",
    "Entscheidung: Patent ja/nein"
  ],
  "naechste_aktion": "Concrete next action (e.g., Meldung an TTO bis Ende der Woche)",
  "patentanwalt_wann": "Vor Anmeldung|Bei Konflikten|Bei Unsicherheit"
}
```

Return ONLY valid JSON, no other text."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You output only valid JSON. No markdown, no explanation. Use German for content."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )
    
    text = response.choices[0].message.content.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()
    
    return json.loads(text)


def main():
    print("Generating example with AI...")
    ex = generate_example()
    
    BASE.mkdir(parents=True, exist_ok=True)
    out_path = BASE / "PROZESS-BEISPIEL.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(ex, f, ensure_ascii=False, indent=2)
    
    print(f"Saved to {out_path}")
    return ex

if __name__ == "__main__":
    main()
