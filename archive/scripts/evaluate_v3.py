#!/usr/bin/env python3
"""
Evaluates the refined-V3 Erfindung-Check result using GPT-5.1.
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
REFINED = BASE / "optimized" / "refined-V3"


def load_all():
    """Load persona, refined-V3 process, HTML, examples."""
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
        parts["html"] = html[:20000] + "\n...[truncated]..." if len(html) > 20000 else html

    ex_path = REFINED / "PROZESS-BEISPIEL.json"
    parts["example"] = ex_path.read_text(encoding="utf-8") if ex_path.exists() else ""

    ev_v2 = BASE / "optimized" / "refined-V2" / "GESAMT-EVALUATION-V2.md"
    parts["v2_evaluation"] = ev_v2.read_text(encoding="utf-8") if ev_v2.exists() else ""

    imp_path = REFINED / "V3-VERBESSERUNGSPLAN.md"
    parts["v3_plan"] = imp_path.read_text(encoding="utf-8")[:4000] if imp_path.exists() else ""

    return parts


def evaluate(client, data):
    prompt = """Du bewertest das **gesamte Ergebnis** des Erfindung-Check-Projekts in seiner **V3-Version** (refined-V3). Das umfasst:

1. **Optimierter Prozess V3** (7 Schritte, Markdown) – mit Mikro-Walkthroughs, mechanikfokussierter Kernidee, Glossar
2. **HTML-Präsentation V3** (erfindung-check.html) – mit Stepper (IntersectionObserver), Tooltips, „Zurück zur Schrittübersicht"
3. **Durchgängiges Beispiel** (Einhand-Schnellspannzwinge)

## Kontext

V3 wurde erstellt, um von 4/5 (V2) auf 5/5 zu kommen. Verbesserungen umfassen u.a.:
- Mikro-Walkthrough Schritt 3 (Prior Art): „So sieht ein Suchlauf konkret aus"
- Mikro-Walkthrough Schritt 4: „Einen Treffer durch die Matrix führen"
- Kernidee-Beispiel mechanikfokussiert (zweistufiger Rastmechanismus statt „Wetterbedingungen")
- Varianten-Kommentare zur Patentnähe
- Glossar (aufklappbar)
- Stepper-Dynamik per IntersectionObserver
- „Zurück zur Schrittübersicht"-Link pro Schritt
- Tooltips für Funktionsprinzip, Mechanismus, Kontext, Kernprinzip

## Deine Perspektive: USER PERSONA

Die Persona ist die **unsichere Erfinder:in mit konkreter Idee**:
- Konkrete Lösung, weiß nicht ob neu, will selbst prüfen
- Keine Patent-Expertise, begrenzte Zeit
- Braucht Struktur, klare Schritte, Entscheidungsregeln
- Will erste Einordnung (neu/unklar/bekannt) + konkrete Next Action
- Tendenz zu vagen Formulierungen; braucht Konkretisierungsdruck

## Deine Aufgabe

Bewerte das **V3-Gesamtergebnis** aus dieser Perspektive. Würde diese Person den Prozess ohne externe Hilfe durchlaufen können? Sind die kognitiven Überforderungspunkte (Schritt 3 & 4) entschärft? Ist das Beispiel mechanikfokussiert und vermeidet es falsche Sicherheit?

## Bewertungsdimensionen

### 1. Persona-Fit (Kernfrage)
- Erreicht der Prozess die Persona? Wo überfordert er noch?
- Adressiert er die Schmerzpunkte?
- Sind die Mikro-Walkthroughs hilfreich?

### 2. Prozess-Qualität
- Sind die Übergänge klar? Sind Schritt 3 und 4 kognitiv entlastet?
- Ist die Kernidee mechanikfokussiert?

### 3. HTML & UX
- Funktioniert der Stepper dynamisch? Sind die „Zurück"-Links hilfreich?
- Sind die Tooltips und das Glossar nützlich?

### 4. Beispiel-Qualität
- Ist das Beispiel konsistent und mechanikfokussiert?
- Vermeidet es falsche Sicherheit („rausdefinieren")?

### 5. Gesamteindruck
- Würde die Persona den Prozess zu Ende bringen?
- Ist 5/5 aus Persona-Sicht erreicht?

---

## Output-Format (auf Deutsch)

# Gesamtbewertung: Erfindung-Check V3

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

## Top 3 Verbesserungspotenziale (falls noch vorhanden)
1. ...
2. ...
3. ...

## Vergleich zu V2 (4/5)
[Hat sich die Qualität verbessert? Wo am meisten?]

## Empfehlung
[Konkrete nächste Schritte – oder Bestätigung, dass 5/5 erreicht ist]
"""

    content = f"""{prompt}

---
## USER PERSONA
{data.get('persona', '')}

---
## V3 PROZESS (Schritte)
{data.get('process', '')}

---
## V2 EVALUATION (4/5)
{data.get('v2_evaluation', '')}

---
## V3 VERBESSERUNGSPLAN (Auszug)
{data.get('v3_plan', '')}

---
## BEISPIEL (JSON)
{data.get('example', '')}

---
## HTML V3 (Struktur & Inhalt)
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
    print("Lade V3-Inhalte...")
    data = load_all()

    client = OpenAI()
    print(f"Evaluierung mit {MODEL} (Persona-Perspektive)...")
    result = evaluate(client, data)

    out_path = REFINED / "GESAMT-EVALUATION-V3.md"
    out_path.write_text(result, encoding="utf-8")
    print(f"Gespeichert: {out_path}")
    return result


if __name__ == "__main__":
    main()
