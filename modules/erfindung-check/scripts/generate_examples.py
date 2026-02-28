#!/usr/bin/env python3
"""
Generates a coherent example that shows how the Erfindung-Check process evolves over time.
Uses OpenAI to create realistic, consistent examples for each step.
Output: PROZESS-BEISPIEL.json in Erfindung-Check-Prozess/optimized/refined/

The examples are also embedded in the markdown files (00–06) and erfindung-check.html.
To regenerate: run this script, then manually update the markdown/HTML with the new JSON data,
or extend this script to auto-update those files.
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
    
    prompt = """Create a coherent, realistic example for the Erfindung-Check process. The example must show how the process EVOLVES step by step – each step builds on the previous.

**Example invention:** Choose ONE concrete, plausible invention (e.g., "one-handed quick-release clamp for bicycle handlebars" or "magnetic cable organizer for desk" – something mechanical/product-focused that's easy to follow).

**Output as JSON** with these exact keys. Use German for all content. Be specific and realistic (invent plausible but fictional patent titles, years, product names):

```json
{
  "erfindung_kurz": "One-sentence description of the example invention",
  "kategorie": "Produkt, Gerät oder Mechanik",
  "markt_treffer": [
    {"name": "Product/Company", "ähnlichkeit": "ähnlich|sehr ähnlich|anders", "beschreibung": "1 Satz"},
    ... 5-7 entries
  ],
  "keywords": ["keyword1", "keyword2", ...],
  "prior_art": [
    {"titel": "Patent/Paper title", "jahr": "2021", "quelle": "Patent/Google Scholar/...", "relevanz": "1 Satz"},
    ... 4-6 entries
  ],
  "treffer_bewertung": [
    {"treffer": "Name/Title", "quelle": "Markt|Patent|Paper", "kategorie": "Gleiche Funktion, anderer Mechanismus|Ähnlicher Mechanismus, anderer Zweck|Gleiche Funktion und gleicher Mechanismus", "gleich": "1 Satz", "anders": "1 Satz", "relevanz": "1 Satz"},
    ... 4-6 entries
  ],
  "kernidee": "Neu ist, dass [Mechanismus] so ausgeführt ist, dass [Wirkung] unter [Bedingung] entsteht.",
  "varianten": ["Variante 1", "Variante 2"],
  "kernidee_keywords": {"mechanismus": ["..."], "wirkung": ["..."], "kontext": ["..."]},
  "offene_fragen": ["Frage 1"],
  "einordnung": "Neu wirkt plausibel|Unklar|Eher bekannt",
  "naechste_aktion": "Concrete next action based on Einordnung"
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
    # Remove markdown code blocks if present
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()
    
    return json.loads(text)


def main():
    print("Generating example with AI...")
    ex = generate_example()
    
    out_path = BASE / "PROZESS-BEISPIEL.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(ex, f, ensure_ascii=False, indent=2)
    
    print(f"Saved to {out_path}")
    return ex

if __name__ == "__main__":
    main()
