#!/usr/bin/env python3
"""
Generates a detailed improvement plan for the Erfindung-Check using GPT-5.1.
Uses USER-PERSONA.md and all evaluations as input.
"""

import os
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

MODEL = "gpt-5.1"
FALLBACK = "gpt-4o"
BASE = Path(__file__).parent / "Erfindung-Check-Prozess"
REFINED = BASE / "optimized" / "refined"


def load_all():
    """Load persona, evaluations, process summary."""
    parts = {}

    for name, path in [
        ("persona", BASE / "USER-PERSONA.md"),
        ("gesamt_evaluation", REFINED / "GESAMT-EVALUATION.md"),
        ("beispiel_evaluation", REFINED / "BEISPIEL-EVALUATION.md"),
        ("quality_grade", BASE / "PROCESS-QUALITY-GRADE.md"),
        ("rationale", REFINED / "RATIONALE.md"),
    ]:
        if path.exists():
            parts[name] = path.read_text(encoding="utf-8")

    # Process steps (concise)
    step_files = ["00-Einleitung.md", "01-Kategorie-wählen.md", "02-Markt-scannen.md",
                  "03-Prior-Art-suchen.md", "04-Treffer-bewerten.md", "05-Kern-schärfen.md", "06-Ergebnis-ableiten.md"]
    process_parts = []
    for f in step_files:
        fp = REFINED / f
        if fp.exists():
            process_parts.append(f"=== {f} ===\n{fp.read_text(encoding='utf-8')}\n")
    parts["process"] = "\n".join(process_parts)

    return parts


def generate_plan(client, data):
    prompt = """Du erstellst einen **detaillierten Verbesserungsplan** für das Erfindung-Check-Projekt.

## Kontext

Das Projekt umfasst:
- Einen optimierten 7-Schritte-Prozess (Markdown)
- Eine HTML-Präsentation (erfindung-check.html)
- Ein durchgängiges Beispiel (Einhand-Schnellspannzwinge)
- Mehrere AI-Evaluationen (Gesamtbewertung, Beispiel-Evaluation, Quality Grade)

## Perspektive: USER PERSONA

Die Zielgruppe ist die **unsichere Erfinder:in mit konkreter Idee**:
- Keine Patent-Expertise, begrenzte Zeit
- Braucht Struktur, klare Schritte, Entscheidungsregeln
- Schmerzpunkte: zu spät klären, Unsicherheit wo anfangen, vage Formulierungen

## Deine Aufgabe

Erstelle einen **konkreten, umsetzbaren Verbesserungsplan**. Jede Maßnahme soll:
- Einer spezifischen Schwäche aus den Evaluationen adressieren
- Die Persona-Perspektive berücksichtigen
- Konkret genug sein, um umgesetzt zu werden (nicht nur "verbessern", sondern "was genau")

---

## Output-Format (auf Deutsch)

# Detaillierter Verbesserungsplan: Erfindung-Check

## Übersicht
[2-3 Sätze: Ziel des Plans, Priorisierung]

---

## Phase 1: Quick Wins (1-2 Tage)
*Schnelle Verbesserungen mit hoher Wirkung*

### 1.1 [Titel der Maßnahme]
- **Problem:** [Welche Schwäche wird adressiert]
- **Lösung:** [Konkrete Änderung]
- **Datei/Stelle:** [Wo umsetzen]
- **Erwarteter Effekt:** [Für die Persona]

### 1.2 [Titel]
...

---

## Phase 2: Prozess & Inhalt (3-5 Tage)
*Strukturelle und inhaltliche Verbesserungen*

### 2.1 Input-Output-Handoffs klären
- **Problem:** Übergänge zwischen Schritten unklar
- **Lösung:** [Konkrete Vorschläge pro Schritt]
- **Beispiel-Formulierung:** [Wie könnte "Du bringst aus Schritt X mit..." aussehen]

### 2.2 [Weitere Maßnahmen]
...

---

## Phase 3: Beispiel & Pädagogik (2-3 Tage)
*Beispiel verbessern, Anleitungen vertiefen*

### 3.1 [Maßnahme]
...

---

## Phase 4: HTML & UX (1-2 Tage)
*Darstellung und Nutzerführung*

### 4.1 [Maßnahme]
...

---

## Priorisierte To-Do-Liste (Top 10)
1. [Konkretes To-Do]
2. ...
10. ...

---

## Erfolgskriterien
- [Woran messen wir, ob die Verbesserungen wirken]
"""

    content = f"""{prompt}

---
## USER PERSONA
{data.get('persona', '')}

---
## GESAMT-EVALUATION
{data.get('gesamt_evaluation', '')}

---
## BEISPIEL-EVALUATION
{data.get('beispiel_evaluation', '')}

---
## QUALITY GRADE (Original)
{data.get('quality_grade', '')}

---
## RATIONALE (Optimierung)
{data.get('rationale', '')}

---
## PROZESS (Auszug)
{data.get('process', '')[:8000]}
"""

    messages = [
        {"role": "system", "content": "Du bist ein erfahrener Produkt- und UX-Berater. Erstelle konkrete, umsetzbare Pläne. Keine Floskeln – jede Maßnahme muss spezifisch sein. Antworte auf Deutsch. Output strukturiertes Markdown."},
        {"role": "user", "content": content}
    ]

    try:
        return client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.3,
        ).choices[0].message.content
    except Exception as e:
        if "gpt-5" in str(e).lower() or "model" in str(e).lower():
            print(f"{MODEL} nicht verfügbar, nutze {FALLBACK}...")
            return client.chat.completions.create(
                model=FALLBACK,
                messages=messages,
                temperature=0.3,
            ).choices[0].message.content
        raise


def main():
    print("Lade Inhalte...")
    data = load_all()

    client = OpenAI()
    print(f"Generiere Verbesserungsplan mit {MODEL}...")
    result = generate_plan(client, data)

    out_path = REFINED / "VERBESSERUNGSPLAN.md"
    out_path.write_text(result, encoding="utf-8")
    print(f"Gespeichert: {out_path}")
    return result


if __name__ == "__main__":
    main()
