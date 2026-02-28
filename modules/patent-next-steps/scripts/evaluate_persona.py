#!/usr/bin/env python3
"""
Evaluates the Patent Next Steps module using GPT-5.1 from the persona's perspective.
Simulates a typical academic inventor walking through the process and identifies
where content feels thin or could be improved.
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

try:
    from openai import OpenAI
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "openai", "-q"])
    from openai import OpenAI

MODEL = "gpt-5.1"
FALLBACK = "gpt-4o"


def load_all():
    """Load persona, process steps, HTML, example."""
    parts = {}
    parts["persona"] = (MODULE_DIR / "process-docs" / "USER-PERSONA.md").read_text(encoding="utf-8")
    parts["quality_grade"] = (MODULE_DIR / "process-docs" / "PROCESS-QUALITY-GRADE.md").read_text(encoding="utf-8") if (MODULE_DIR / "process-docs" / "PROCESS-QUALITY-GRADE.md").exists() else ""

    step_files = [
        "00-Einleitung.md", "01-Standort-und-Ansprechpartnerin.md",
        "02-Zeitfenster-beachten.md", "03-Schutzstrategie-wählen.md",
        "04-Prioritäten-setzen.md", "05-Ergebnis.md"
    ]
    steps_dir = MODULE_DIR / "optimized" / "steps"
    process_parts = []
    for f in step_files:
        fp = steps_dir / f
        if fp.exists():
            process_parts.append(f"=== {f} ===\n{fp.read_text(encoding='utf-8')}\n")
    parts["process"] = "\n".join(process_parts)

    html_path = MODULE_DIR / "optimized" / "ui" / "patent-next-steps.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        parts["html"] = html[:15000] + "\n...[truncated]..." if len(html) > 15000 else html

    ex_path = MODULE_DIR / "optimized" / "steps" / "PROZESS-BEISPIEL.json"
    parts["example"] = ex_path.read_text(encoding="utf-8") if ex_path.exists() else ""

    return parts


def evaluate(client, data):
    prompt = """Du bewertest das **Patent Next Steps** Modul aus der Perspektive der **typischen Nutzer:in** (Persona). Der Nutzer hat den Prozess so durchlaufen, wie er/sie es tun würde – und meldet zurück: An manchen Stellen fühlt es sich "dünn" an.

## Deine Rolle

Du bist die **Erfinder:in mit akademischem Hintergrund**:
- Forscher:in, Doktorand:in oder Postdoc
- Hat Erfindung oder Prototyp
- Wenig Überblick über Patentprozess, Meldepflichten, Ansprechpartner:innen
- Sucht Orientierung: Welche Schritte? Wen wann einbeziehen? Was früh klären?
- Erwartet: kompakt, praxisnah – nicht zu detailliert, nicht langweilig

## Deine Aufgabe

**Simuliere**, dass du den Prozess (Markdown + HTML) durchgearbeitet hast. Bewerte aus deiner Sicht:

1. **Wo fühlt sich der Inhalt "dünn" an?** – Wo hättest du dir mehr Konkretes gewünscht? Wo bleiben Fragen offen?
2. **Wo fehlen Beispiele oder Konkretisierungen?** – Tabellen sind gut, aber reicht das? Brauchst du z.B. ein durchgängiges Beispiel (wie bei Erfindung-Check)?
3. **Wo bist du unsicher, was genau du tun sollst?** – Sind die "So gehst du vor"-Schritte konkret genug?
4. **Wo fehlt Kontext für deinen Kontext?** – Uni vs. Firma vs. Startup: Wird das Unterschiedliche genug herausgearbeitet?
5. **HTML vs. Markdown:** – Ist die HTML-Version genauso informativ oder fehlt dort etwas?

## Bewertungsdimensionen

### 1. Dünnstellen (priorisiert)
- Liste 3–5 Stellen, wo der Inhalt zu knapp ist
- Pro Stelle: Was fehlt? Was würde die Persona brauchen?

### 2. Fehlende Konkretisierung
- Gibt es Schritte ohne Beispiel oder Mikro-Walkthrough?
- Würde ein durchgängiges Beispiel (z.B. "Postdoc an Uni mit Software-Erfindung") helfen?

### 3. Handlungsunsicherheit
- Wo weiß die Persona nach dem Schritt nicht genau, was sie tun soll?
- Sind die Outputs (Checkliste, Kontaktliste, To-do) klar genug definiert?

### 4. Kontextspezifität
- Werden Uni / Firma / Startup ausreichend unterschieden?
- Fehlen typische Szenarien oder Stolpersteine pro Kontext?

### 5. Gesamteindruck
- Würde die Persona den Prozess als hilfreich empfinden?
- Was sind die 3 wichtigsten Verbesserungen, um "dünn" zu beheben?

---

## Output-Format

Erstelle ein strukturiertes Markdown-Dokument:

# Patent Next Steps: Persona-Evaluation

## Zusammenfassung (3–4 Sätze)
[Gesamteindruck aus Persona-Sicht]

## 1. Dünnstellen (priorisiert)
[Nummerierte Liste mit: Schritt, Problem, was fehlt]

## 2. Fehlende Konkretisierung
[Was würde helfen: Beispiele, Mikro-Walkthroughs, etc.]

## 3. Handlungsunsicherheit
[Wo bleibt unklar, was genau zu tun ist]

## 4. Kontextspezifität
[Uni/Firma/Startup – was fehlt?]

## 5. Top 3 Verbesserungen
1. [Konkrete Empfehlung]
2. [Konkrete Empfehlung]
3. [Konkrete Empfehlung]

## 6. Stärken (was schon gut funktioniert)
[2–3 Punkte]

Sei konkret und konstruktiv. Verweise auf einzelne Schritte oder Abschnitte."""

    messages = [
        {"role": "system", "content": "Du bist ein:e erfahrene:r Erfinder:in mit akademischem Hintergrund. Du bewertest Prozess-Guides aus Nutzer:innensicht. Sei konkret, kritisch und konstruktiv. Output auf Deutsch."},
        {"role": "user", "content": f"""{prompt}

---

## USER PERSONA (Referenz)

{data['persona']}

---

## OPTIMIERTER PROZESS (Markdown)

{data['process']}

---

## HTML (Auszug)

{data['html']}

---

## BEISPIEL (falls vorhanden)

{data['example']}

---

## QUALITY GRADE (falls vorhanden, als Kontext)

{data['quality_grade'][:2000] if data.get('quality_grade') else 'Nicht vorhanden'}

---

Bewerte jetzt aus Persona-Sicht. Wo fühlt es sich dünn an? Was würde helfen?"""}
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.4,
        )
        return response.choices[0].message.content
    except Exception as e:
        if "gpt-5" in str(e).lower() or "model" in str(e).lower():
            print(f"{MODEL} not available, falling back to {FALLBACK}...")
            response = client.chat.completions.create(
                model=FALLBACK,
                messages=messages,
                temperature=0.4,
            )
            return response.choices[0].message.content
        raise


def main():
    print("Loading patent-next-steps content...")
    data = load_all()

    print(f"Evaluating with {MODEL} (persona perspective)...")
    client = OpenAI()
    result = evaluate(client, data)

    output_path = MODULE_DIR / "process-docs" / "PERSONA-EVALUATION.md"
    output_path.write_text(result, encoding="utf-8")
    print(f"Evaluation saved to: {output_path}")
    print("\n--- Preview ---\n")
    print(result[:2500])
    if len(result) > 2500:
        print("\n... (see full file for rest)")
    return result


if __name__ == "__main__":
    main()
