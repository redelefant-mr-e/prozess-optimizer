#!/usr/bin/env python3
"""
Generates a V3 improvement plan using GPT-5.1 to reach 5/5.
Based on V2 evaluation feedback and USER-PERSONA.
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
REFINED_V2 = BASE / "optimized" / "refined-V2"


def load_all():
    """Load persona, V2 evaluation, V2 process summary."""
    parts = {}

    parts["persona"] = (BASE / "USER-PERSONA.md").read_text(encoding="utf-8") if (BASE / "USER-PERSONA.md").exists() else ""

    ev_path = REFINED_V2 / "GESAMT-EVALUATION-V2.md"
    parts["v2_evaluation"] = ev_path.read_text(encoding="utf-8") if ev_path.exists() else ""

    step_files = [
        "00-Einleitung.md", "01-Kategorie-wählen.md", "02-Markt-scannen.md",
        "03-Prior-Art-suchen.md", "04-Treffer-bewerten.md", "05-Kern-schärfen.md", "06-Ergebnis-ableiten.md"
    ]
    process_parts = []
    for f in step_files:
        fp = REFINED_V2 / f
        if fp.exists():
            process_parts.append(f"=== {f} ===\n{fp.read_text(encoding='utf-8')}\n")
    parts["process"] = "\n".join(process_parts)[:12000]

    return parts


def generate_plan(client, data):
    prompt = """Du erstellst einen **detaillierten V3-Verbesserungsplan**, um den Erfindung-Check von **4/5 auf 5/5** zu bringen.

## Ausgangslage

- **V2** wurde mit 4/5 bewertet (Persona-Perspektive).
- V2 hat bereits: Limitations-Box, Handoffs, Minimal-Varianten, Entscheidungsmatrix, „So formulierst du konkret", Stepper, Tooltips.
- Die V2-Evaluation nennt konkrete Lücken, die für 5/5 geschlossen werden müssen.

## Ziel: 5/5

Eine 5/5 bedeutet aus Persona-Sicht:
- Die unsichere Erfinder:in kann den Prozess **ohne externe Hilfe** durchlaufen.
- Keine kognitiven Überforderungspunkte mehr (v.a. Schritt 3 und 4).
- Beispiel und Kernidee sind **mechanikfokussiert** und vermeiden falsche Sicherheit.
- UX ist vollständig (Stepper reagiert auf Scroll, Orientierung jederzeit klar).

## Deine Aufgabe

Erstelle einen **priorisierten, umsetzbaren V3-Plan**. Jede Maßnahme muss:
- Eine **spezifische Lücke** aus der V2-Evaluation adressieren
- **Konkret** sein (keine Floskeln – was genau ändern, wo, wie)
- Die **Persona** im Fokus haben (unsichere Erfinder:in, keine Patent-Expertise)

---

## Output-Format (auf Deutsch)

# V3-Verbesserungsplan: Auf dem Weg zu 5/5

## Übersicht
[2–3 Sätze: Ziel, Priorisierung, erwarteter Effekt]

---

## Priorität 1: Kognitive Entlastung (Schritt 3 & 4)
*Die größten Abbruchrisiken – Mikro-Walkthroughs und konkrete Beispiele*

### 1.1 Mikro-Walkthrough Schritt 3 (Prior Art)
- **Problem (aus V2-Eval):** Kombination aus Datenbankwahl, Keywords, 3 Ebenen, Relevanz-Checkliste ist „viel auf einmal"; fehlt durchgehendes Mikro-Beispiel.
- **Lösung:** [Konkrete Beschreibung – z.B. 3–5 Sätze Mini-Walkthrough mit Einhand-Schnellspannzwinge: „Du gibst X ein, siehst Bild Y, entscheidest so …"]
- **Datei/Stelle:** `03-Prior-Art-suchen.md`
- **Beispiel-Formulierung:** [Wörtlicher Vorschlag für 2–3 Sätze]

### 1.2 Mikro-Walkthrough Schritt 4 (Treffer bewerten)
- **Problem:** Entscheidungsmatrix ist abstrakt; Persona muss sie mehrfach lesen; fehlt Mini-Beispiel direkt in der Matrix.
- **Lösung:** [Konkret: Wie ein Treffer von „wirkt ähnlich" zu einer Matrix-Kategorie durchdekliniert wird]
- **Datei/Stelle:** `04-Treffer-bewerten.md`
- **Beispiel-Formulierung:** [Wörtlicher Vorschlag, evtl. als zusätzliche Zeile/Spalte in der Matrix]

---

## Priorität 2: Beispiel-Qualität (Kernidee & Konsistenz)
*Mechanikfokus, keine falsche Sicherheit*

### 2.1 Kernidee-Beispiel überarbeiten
- **Problem:** „Unter allen Wetterbedingungen" wirkt marketing- statt funktionsorientiert; Persona könnte falsche Sicherheit bekommen („rausdefinieren").
- **Lösung:** [Konkrete mechanikfokussierte Alternative – z.B. Hebelgeometrie, Rastposition, Kraftübertragung]
- **Datei/Stelle:** `05-Kern-schärfen.md`, `06-Ergebnis-ableiten.md`, Beispiel-Tabellen
- **Neue Kernidee (Beispiel):** [Wörtlicher Vorschlag]

### 2.2 Varianten-Kommentar ergänzen
- **Problem:** Varianten (Sicherheitsverschluss, verstellbare Spannkraft) – es wird nicht gezeigt, wie sie sich zu bestehenden Patenten verhalten.
- **Lösung:** [Kurzer Kommentar pro Variante: „könnte vom Patent X erfasst sein / eher nicht" – warum]
- **Datei/Stelle:** `05-Kern-schärfen.md` oder `06-Ergebnis-ableiten.md`

---

## Priorität 3: UX-Feinschliff
*Stepper, Navigation, Orientierung*

### 3.1 Stepper-Dynamik prüfen/verbessern
- **Problem:** Stepper soll beim Scrollen den aktiven Schritt aktualisieren + „Du bist bei Schritt X von 7".
- **Lösung:** [Falls JS fehlt: Beschreibung. Falls vorhanden: Prüfen ob scroll-basiert oder Intersection Observer besser]
- **Datei/Stelle:** `erfindung-check.html`

### 3.2 „Zurück nach oben / zum Stepper"-Link
- **Problem:** Steps sind lang; Persona braucht schnelle Rücknavigation.
- **Lösung:** Am Ende jedes Schritts einen Link „↑ Zurück zum Überblick" oder „↑ Nach oben"
- **Datei/Stelle:** `erfindung-check.html`, evtl. Markdown

---

## Priorität 4: Glossar & Verständlichkeit
*Begriffe für Laien klären*

### 4.1 Tooltips für weitere Begriffe
- **Problem:** „Funktionsprinzip", „Mechanismus", „Kontext", „Kernprinzip" könnten für Laien verschwimmen.
- **Lösung:** [Welche Begriffe wo mit Tooltip versehen – Priorität]
- **Datei/Stelle:** `erfindung-check.html`

### 4.2 Optional: Kurzes Glossar
- **Lösung:** [Kompakte 5–8 Zeilen Box am Ende der Einleitung oder als Collapsible]

---

## Priorität 5: Optional (Nice-to-have für 5/5)
*Wenn Zeit bleibt*

### 5.1 Cheat-Sheet / Kurzansicht
- 1–2 Seiten PDF oder HTML-Abschnitt: Nur Schritte, Minimal-Variante, Kern-Tabellenstruktur.
- **Erwarteter Effekt:** Persona kann ausdrucken oder nebenher offen haben.

### 5.2 Suchlauf-Beispiel Schritt 3
- „So sah meine erste Suche aus, so habe ich angepasst" – konkretes Beispiel bei zu vielen/zu wenigen Treffern.

---

## Umsetzungsreihenfolge (Top 10)
1. [Konkretes To-Do]
2. ...
10. ...

---

## Erfolgskriterien für 5/5
- [Woran messen wir, dass 5/5 erreicht ist – aus Persona-Sicht]
"""

    content = f"""{prompt}

---
## USER PERSONA
{data.get('persona', '')}

---
## V2 EVALUATION (4/5 – Lücken identifiziert)
{data.get('v2_evaluation', '')}

---
## V2 PROZESS (Auszug – aktuelle Inhalte)
{data.get('process', '')}
"""

    messages = [
        {"role": "system", "content": "Du bist ein erfahrener Produkt- und UX-Berater. Erstelle konkrete, umsetzbare Pläne. Jede Maßnahme muss spezifisch und wörtlich formulierbar sein. Antworte auf Deutsch. Output strukturiertes Markdown."},
        {"role": "user", "content": content}
    ]

    try:
        return client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.25,
        ).choices[0].message.content
    except Exception as e:
        if "gpt-5" in str(e).lower() or "model" in str(e).lower():
            print(f"{MODEL} nicht verfügbar, nutze {FALLBACK}...")
            return client.chat.completions.create(
                model=FALLBACK,
                messages=messages,
                temperature=0.25,
            ).choices[0].message.content
        raise


def main():
    print("Lade Inhalte...")
    data = load_all()

    client = OpenAI()
    print(f"Generiere V3-Verbesserungsplan mit {MODEL} (Ziel: 5/5)...")
    result = generate_plan(client, data)

    out_path = REFINED_V2 / "V3-VERBESSERUNGSPLAN.md"
    out_path.write_text(result, encoding="utf-8")
    print(f"Gespeichert: {out_path}")
    return result


if __name__ == "__main__":
    main()
