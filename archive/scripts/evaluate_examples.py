#!/usr/bin/env python3
"""
Uses AI to evaluate the quality of the process examples.
Checks: coherence, realism, pedagogical value, evolution across steps.
"""

import os
import json
from pathlib import Path

env_path = Path(__file__).parent / ".env"
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

BASE = Path(__file__).parent / "Erfindung-Check-Prozess" / "optimized" / "refined"


def load_example():
    p = BASE / "PROZESS-BEISPIEL.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def evaluate(client, example):
    prompt = """Evaluate the quality of this process example for the "Erfindung-Check" (German invention novelty check). The example runs through all 7 steps with one invention: "Einhand-Schnellspannzwinge für Fahrradlenker".

## Evaluation Criteria

1. **Coherence across steps:** Does each step logically build on the previous? Do the market hits, prior art, and evaluations reference each other consistently?

2. **Realism:** Are the market products, patent titles, and categorizations plausible? Would a real user find this believable?

3. **Pedagogical value:** Does the example clearly show HOW to fill in each table? Is it instructive for someone with no patent experience?

4. **Evolution:** Does the example show progression – e.g., keywords from step 2 used in step 3, treffer from 2+3 evaluated in step 4, kernidee derived from the "Anders" differences?

5. **Internal consistency:** Is the final "Einordnung" (Neu wirkt plausibel) consistent with the treffer_bewertung? (Note: BikeGear + Schnellspannmechanismus-Patent are "Gleiche Funktion und Mechanismus" – that might suggest "Unklar" rather than "Neu wirkt plausibel")

## Output Format

Provide a structured evaluation in German:

# Beispiel-Evaluation

## Gesamtnote: [1-5] / 5
**Kurzurteil:** [1 Satz]

## 1. Kohärenz
[Was funktioniert, was nicht]

## 2. Realismus
[Stärken, Schwächen]

## 3. Pädagogischer Wert
[Für wen geeignet, was fehlt]

## 4. Evolution über Schritte
[Wird der Aufbau klar?]

## 5. Interne Konsistenz
[Widersprüche? Einordnung vs. Treffer?]

## Konkrete Verbesserungsvorschläge (Priorisiert)
1. [Wichtigster]
2. ...
3. [Optional]

## Empfehlung
[Beibehalten / Überarbeiten / Neu generieren – mit Begründung]
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du bist ein Experte für Prozessdokumentation und pädagogische Beispiele. Sei kritisch und konstruktiv. Antworte auf Deutsch."},
            {"role": "user", "content": f"{prompt}\n\n---\n\n## Beispiel-Daten (JSON)\n\n```json\n{json.dumps(example, ensure_ascii=False, indent=2)}\n```"}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


def main():
    example = load_example()
    if not example:
        print("No PROZESS-BEISPIEL.json found.")
        return

    client = OpenAI()
    print("Evaluating examples with AI...")
    result = evaluate(client, example)

    out_path = BASE / "BEISPIEL-EVALUATION.md"
    out_path.write_text(result, encoding="utf-8")
    print(f"Saved to {out_path}")
    return result


if __name__ == "__main__":
    main()
