#!/usr/bin/env python3
"""
Generates a coherent example that shows how the Erfindungsbeschreibung process evolves.
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

    prompt = """Create a coherent, realistic example for the Erfindungsbeschreibung process (Invention Documentation Guide). The example must show how the process EVOLVES step by step – each step builds on the previous.

**Example inventor:** Choose ONE concrete scenario (e.g., "Postdoc with software algorithm for image segmentation" or "Chemist with new catalyst" or "Engineer with sensor system" – something plausible for the academic/research context).

**Output as JSON** with these exact keys. Use German for all content. Be specific and realistic:

```json
{
  "erfindung_kurz": "One-sentence description of the example invention",
  "kern_der_neuerung": "1-2 sentences: What is truly new? (Das wesentliche Neue ist, dass ...)",
  "stand_der_technik": [
    {"loesung": "Known solution A", "nachteil": "Its disadvantage"},
    {"loesung": "Known solution B", "nachteil": "Its disadvantage"}
  ],
  "luecke": "What gap does the invention fill?",
  "technische_loesung": "What must one do to make it work? (components, steps)",
  "gliederung": [
    "Technische Aufgabe und Gebiet",
    "Stand der Technik",
    "Behebung der Nachteile",
    "Technische Lösung",
    "Vorteile",
    "Literaturverzeichnis"
  ],
  "checkliste_vor_abgabe": [
    "Kern formuliert",
    "Stand der Technik mit Nachteilen",
    "Lösung beschreibt was tun"
  ],
  "naechste_aktion": "Concrete next action (e.g., Beschreibung nach Gliederung ausformulieren bis Freitag)"
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
        lines = text.split("\n")
        text = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    data = json.loads(text)

    BASE.mkdir(parents=True, exist_ok=True)
    out_path = BASE / "PROZESS-BEISPIEL.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Example saved to: {out_path}")
    return data


if __name__ == "__main__":
    generate_example()
