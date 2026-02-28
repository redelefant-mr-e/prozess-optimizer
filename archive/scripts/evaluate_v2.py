#!/usr/bin/env python3
"""
Evaluates the refined-V2 Erfindung-Check result using GPT-5.1.
Uses USER-PERSONA.md as the evaluation lens.
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
REFINED = BASE / "optimized" / "refined-V2"


def load_all():
    """Load persona, refined-V2 process, HTML, examples."""
    parts = {}

    p = BASE / "USER-PERSONA.md"
    parts["persona"] = p.read_text(encoding="utf-8") if p.exists() else ""

    step_files = [
        "README-optimized.md", "00-Einleitung.md", "01-Kategorie-wählen.md", "02-Markt-scannen.md",
        "03-Prior-Art-suchen.md", "04-Treffer-bewerten.md", "05-Kern-schärfen.md", "06-Ergebnis-ableiten.md"
    ]
    process_parts = []
    for f in step_files:
        fp = REFINED / f
        if fp.exists():
            process_parts.append(f"=== {f} ===\n{fp.read_text(encoding='utf-8')}\n")
    parts["process"] = "\n".join(process_parts)

    html_path = REFINED / "erfindung-check.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        parts["html"] = html[:18000] + "\n...[truncated]..." if len(html) > 18000 else html

    ex_path = REFINED / "PROZESS-BEISPIEL.json"
    parts["example"] = ex_path.read_text(encoding="utf-8") if ex_path.exists() else ""

    # Previous evaluation for context (refined, not V2)
    ev_path = BASE / "optimized" / "refined" / "GESAMT-EVALUATION.md"
    parts["previous_evaluation"] = ev_path.read_text(encoding="utf-8") if ev_path.exists() else ""

    imp_path = BASE / "optimized" / "refined" / "VERBESSERUNGSPLAN.md"
    parts["improvement_plan"] = imp_path.read_text(encoding="utf-8")[:3000] if imp_path.exists() else ""

    return parts


def evaluate(client, data):
    prompt = """Du bewertest das **gesamte Ergebnis** des Erfindung-Check-Projekts in seiner **V2-Version** (refined-V2). Das umfasst:

1. **Optimierter Prozess V2** (7 Schritte, Markdown) – mit Verbesserungen aus dem Verbesserungsplan
2. **HTML-Präsentation V2** (erfindung-check.html) – mit Stepper, Tooltips, Limitations-Boxen
3. **Durchgängiges Beispiel** (Einhand-Schnellspannzwinge)

## Kontext

Die V2-Version wurde basierend auf einer vorherigen Evaluation (Note 3/5) und einem detaillierten Verbesserungsplan erstellt. Verbesserungen umfassen u.a.:
- Limitations-Box und „Warum jetzt und nicht später?“
- Input-Output-Handoffs pro Schritt
- „Wenn du wenig Zeit hast“-Minimal-Varianten
- Entscheidungsmatrix für Funktionsprinzip
- „So formulierst du konkret“ (gegen vage Formulierungen)
- Fortschrittsanzeige (Stepper) in der HTML-Version
- Tooltips für Fachbegriffe (Prior Art, Claims)

## Deine Perspektive: USER PERSONA

Die Persona ist die **unsichere Erfinder:in mit konkreter Idee**:
- Konkrete Lösung, weiß nicht ob neu, will selbst prüfen
- Keine Patent-Expertise, begrenzte Zeit
- Braucht Struktur, klare Schritte, Entscheidungsregeln
- Will erste Einordnung (neu/unklar/bekannt) + konkrete Next Action
- Tendenz zu vagen Formulierungen; braucht Konkretisierungsdruck

## Deine Aufgabe

Bewerte das **V2-Gesamtergebnis** aus dieser Perspektive. Berücksichtige die umgesetzten Verbesserungen. Würde diese Person den Prozess durchlaufen können? Würde sie verstehen, was zu tun ist? Würde sie am Ende wissen, was der nächste Schritt ist?

## Bewertungsdimensionen

### 1. Persona-Fit (Kernfrage)
- Erreicht der Prozess die Persona? Wo überfordert er? Wo unterfordert er?
- Adressiert er die Schmerzpunkte (zu spät klären, Unsicherheit wo anfangen, vage Formulierungen)?
- Sind die Beispiele für jemanden ohne Patent-Erfahrung nachvollziehbar?

### 2. Prozess-Qualität
- Ist der 7-Schritte-Prozess kohärent?
- Sind die Übergänge klar? Input-Output-Handoffs?
- Sind die Tipps und Minimal-Varianten konkret genug?

### 3. HTML & UX
- Ist die Darstellung für die Persona geeignet?
- Unterstützt das Design die Nutzung (Lesbarkeit, Orientierung, Fortschritt, Stepper)?
- Funktioniert die Navigation?

### 4. Beispiel-Qualität
- Zeigt das Beispiel die Evolution über die Schritte?
- Ist es konsistent?
- Hilft die Kommentar-Spalte, die Tabellen zu verstehen?

### 5. Gesamteindruck
- Würde die Persona den Prozess zu Ende bringen?
- Wo droht Abbruch? Was fehlt noch?
- Hat sich die Qualität gegenüber der vorherigen Version (Note 3/5) verbessert?

---

## Output-Format (auf Deutsch)

# Gesamtbewertung: Erfindung-Check V2

## Gesamtnote: [1-5] / 5
**Ein-Satz-Urteil:** [Klares Fazit]

---

## 1. Persona-Fit
[Assessment]

## 2. Prozess-Qualität
[Assessment]

## 3. HTML & UX
[Assessment]

## 4. Beispiel-Qualität
[Assessment]

## 5. Gesamteindruck
[Assessment]

---

## Top 3 Stärken
1. ...
2. ...
3. ...

## Top 3 Verbesserungspotenziale
1. ...
2. ...
3. ...

## Vergleich zur vorherigen Version
[Kurze Einschätzung: Hat sich die Qualität verbessert? Wo am meisten?]

## Empfehlung
[Konkrete nächste Schritte für die Autoren]
"""

    content = f"""{prompt}

---
## USER PERSONA
{data.get('persona', '')}

---
## V2 PROZESS (Schritte)
{data.get('process', '')}

---
## VORHERIGE EVALUATION (refined, Note 3/5)
{data.get('previous_evaluation', '')}

---
## VERBESSERUNGSPLAN (Auszug)
{data.get('improvement_plan', '')}

---
## BEISPIEL (JSON)
{data.get('example', '')}

---
## HTML V2 (Struktur & Inhalt)
{data.get('html', '')}
"""

    messages = [
        {"role": "system", "content": "Du bist ein erfahrener UX- und Prozess-Evaluator. Bewerte aus der Nutzerperspektive. Sei kritisch und konstruktiv. Antworte auf Deutsch. Output strukturiertes Markdown."},
        {"role": "user", "content": content}
    ]

    try:
        return client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.35,
        ).choices[0].message.content
    except Exception as e:
        if "gpt-5" in str(e).lower() or "model" in str(e).lower():
            print(f"{MODEL} nicht verfügbar, nutze {FALLBACK}...")
            return client.chat.completions.create(
                model=FALLBACK,
                messages=messages,
                temperature=0.35,
            ).choices[0].message.content
        raise


def main():
    print("Lade V2-Inhalte...")
    data = load_all()

    client = OpenAI()
    print(f"Evaluierung mit {MODEL} (Persona-Perspektive)...")
    result = evaluate(client, data)

    out_path = REFINED / "GESAMT-EVALUATION-V2.md"
    out_path.write_text(result, encoding="utf-8")
    print(f"Gespeichert: {out_path}")
    return result


if __name__ == "__main__":
    main()
