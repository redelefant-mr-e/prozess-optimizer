#!/usr/bin/env python3
"""
Evaluates the ENTIRE Erfindung-Check result using GPT-5.
Uses USER-PERSONA.md as the evaluation lens.

Evaluates: optimized process, HTML, examples, rationale – the complete package.
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

MODEL = "gpt-5"
FALLBACK = "gpt-4o"
BASE = Path(__file__).parent / "Erfindung-Check-Prozess"
REFINED = BASE / "optimized" / "refined"


def load_all():
    """Load persona, refined process, HTML (structure only), examples, rationale, example evaluation."""
    parts = {}

    # Persona
    p = BASE / "USER-PERSONA.md"
    parts["persona"] = p.read_text(encoding="utf-8") if p.exists() else ""

    # Refined process (all markdown steps)
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

    # HTML - structure and key elements (strip long style blocks for brevity)
    html_path = REFINED / "erfindung-check.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        # Keep structure: header, nav, sections, blocks - truncate if very long
        parts["html"] = html[:15000] + "\n...[truncated]..." if len(html) > 15000 else html

    # Example data
    ex_path = REFINED / "PROZESS-BEISPIEL.json"
    parts["example"] = ex_path.read_text(encoding="utf-8") if ex_path.exists() else ""

    # Rationale (optimization)
    rat_path = REFINED / "RATIONALE.md"
    parts["rationale"] = rat_path.read_text(encoding="utf-8") if rat_path.exists() else ""

    # Example evaluation (previous AI assessment)
    ev_path = REFINED / "BEISPIEL-EVALUATION.md"
    parts["example_evaluation"] = ev_path.read_text(encoding="utf-8") if ev_path.exists() else ""

    return parts


def evaluate(client, data):
    prompt = """Du bewertest das **gesamte Ergebnis** des Erfindung-Check-Projekts. Das umfasst:

1. **Optimierter Prozess** (7 Schritte, Markdown)
2. **HTML-Präsentation** (erfindung-check.html)
3. **Durchgängiges Beispiel** (Einhand-Schnellspannzwinge)
4. **Rationale** der Optimierung

## Deine Perspektive: USER PERSONA

Die Persona ist die **unsichere Erfinder:in mit konkreter Idee**:
- Konkrete Lösung, weiß nicht ob neu, will selbst prüfen
- Keine Patent-Expertise, begrenzte Zeit
- Braucht Struktur, klare Schritte, Entscheidungsregeln
- Will erste Einordnung (neu/unklar/bekannt) + konkrete Next Action
- Tendenz zu vagen Formulierungen; braucht Konkretisierungsdruck

## Deine Aufgabe

Bewerte das **Gesamtergebnis** aus dieser Perspektive. Stell dir vor: Würde diese Person den Prozess durchlaufen können? Würde sie verstehen, was zu tun ist? Würde sie am Ende wissen, was der nächste Schritt ist?

## Bewertungsdimensionen

### 1. Persona-Fit (Kernfrage)
- Erreicht der Prozess die Persona? Wo überfordert er? Wo unterfordert er?
- Adressiert er die Schmerzpunkte (zu spät klären, Unsicherheit wo anfangen, vage Formulierungen)?
- Sind die Beispiele für jemanden ohne Patent-Erfahrung nachvollziehbar?

### 2. Prozess-Qualität
- Ist der 7-Schritte-Prozess (nach Optimierung) kohärent?
- Sind die Übergänge klar? Input-Output-Handoffs?
- Sind die Tipps konkret genug?

### 3. HTML & UX
- Ist die Darstellung für die Persona geeignet?
- Unterstützt das Design die Nutzung (Lesbarkeit, Orientierung, Fortschritt)?
- Funktioniert die Navigation?

### 4. Beispiel-Qualität
- Zeigt das Beispiel die Evolution über die Schritte?
- Ist es konsistent (nach der Korrektur)?
- Hilft es, die Tabellen zu verstehen?

### 5. Gesamteindruck
- Würde die Persona den Prozess zu Ende bringen?
- Wo droht Abbruch? Was fehlt?
- Was ist der größte Stärke, was der größte Schwachpunkt?

---

## Output-Format (auf Deutsch)

# Gesamtbewertung: Erfindung-Check Ergebnis

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

## Empfehlung
[Konkrete nächste Schritte für die Autoren]
"""

    content = f"""{prompt}

---
## USER PERSONA
{data.get('persona', '')}

---
## OPTIMIERTER PROZESS (Schritte)
{data.get('process', '')}

---
## RATIONALE (Optimierung)
{data.get('rationale', '')}

---
## BEISPIEL (JSON)
{data.get('example', '')}

---
## BEISPIEL-EVALUATION (Vorherige AI-Bewertung)
{data.get('example_evaluation', '')}

---
## HTML (Struktur & Inhalt)
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
    print("Lade alle Inhalte...")
    data = load_all()

    client = OpenAI()
    print(f"Evaluierung mit {MODEL} (Persona-Perspektive)...")
    result = evaluate(client, data)

    out_path = REFINED / "GESAMT-EVALUATION.md"
    out_path.write_text(result, encoding="utf-8")
    print(f"Gespeichert: {out_path}")
    return result


if __name__ == "__main__":
    main()
