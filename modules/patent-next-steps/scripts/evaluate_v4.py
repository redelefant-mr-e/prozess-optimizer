#!/usr/bin/env python3
"""
Evaluates Patent Next Steps V4 using GPT-5.1.
Perspective: academic inventor persona. Honest, critical, UI-focused.
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


def load_v4_content():
    """Load V4 markdown, HTML, persona."""
    parts = {}
    parts["persona"] = (MODULE_DIR / "process-docs" / "USER-PERSONA.md").read_text(encoding="utf-8")
    parts["improvement_plan"] = (MODULE_DIR / "optimized" / "refined-V4" / "V4-IMPROVEMENT-PLAN.md").read_text(encoding="utf-8") if (MODULE_DIR / "optimized" / "refined-V4" / "V4-IMPROVEMENT-PLAN.md").exists() else ""

    step_files = [
        "00-Einleitung.md", "01-Standort-und-Ansprechpartner.md",
        "02-Zeitfenster-beachten.md", "03-Schutzstrategie-waehlen.md",
        "04-Prioritaeten-setzen.md", "05-Ergebnis.md"
    ]
    md_dir = MODULE_DIR / "optimized" / "refined-V4"
    md_parts = []
    for f in step_files:
        fp = md_dir / f
        if fp.exists():
            md_parts.append(f"=== {f} ===\n{fp.read_text(encoding='utf-8')}\n")
    parts["markdown"] = "\n".join(md_parts)

    html_path = MODULE_DIR / "optimized" / "ui" / "patent-next-steps-V4.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        parts["html"] = html[:18000] + "\n...[truncated]..." if len(html) > 18000 else html
    else:
        parts["html"] = "(V4 HTML not found)"

    return parts


def evaluate(client, data):
    prompt = """Du bewertest **Patent Next Steps V4** – die streamlined Version mit "Aktion oben, Kontext unten", reduzierter Redundanz und Stepper-UI. Deine Bewertung soll **ehrlich, kritisch und konstruktiv** sein.

## Deine Rolle

Du bewertest aus der Perspektive der **Persona** (akademische Erfinder:in):
- Forscher:in, Doktorand:in oder Postdoc mit Erfindung/Prototyp
- Wenig Überblick über Patentprozess, Meldepflichten, Ansprechpartner:innen
- Erwartet: kompakt, praxisnah, nicht überfordernd

## Bewertungsdimensionen

### 1. V4-Verbesserungen: Erreicht?
- "Heute tun" oben: Funktioniert das? Ist es konkret genug?
- Redundanz reduziert? Noch Wiederholungen?
- Maria-Timeline durchgängig mit konkreten Daten?
- Stepper-UI: Hilfreich? "Du bist hier" klar?

### 2. Inhalt & Klarheit
- Sind Fachbegriffe erklärt? (z.B. TTO, Erfindungsberater:in, Publication trap)
- Wo fehlt noch Konkretheit?
- Ist die Länge angemessen – zu knapp oder gut?

### 3. UI & Nutzererfahrung
- Wizard-Navigation, Blöcke, Informationsdichte
- Stepper verständlich?
- Gibt es Lücken oder Verwirrung?

### 4. Lücken & Schwachstellen
- Was fehlt? Unerklärte Begriffe? Stolpersteine?

### 5. Top 5 Verbesserungsvorschläge (priorisiert)

---

## Output-Format

# Patent Next Steps V4: Evaluation

## Executive Summary (4–5 Sätze)

## 1. V4-Verbesserungen: Erreicht?

## 2. Inhalt & Klarheit

## 3. UI & Nutzererfahrung

## 4. Lücken & Schwachstellen

## 5. Top 5 Verbesserungsvorschläge

## 6. Was bereits gut funktioniert

## 7. Quick Wins

---

Sei **ehrlich und kritisch**. Konkrete Verweise. Output auf Deutsch."""

    messages = [
        {"role": "system", "content": "Du bist ein kritischer UX- und Content-Experte. Bewertest Guides für akademische Erfinder:innen. Ehrlich, konkret, konstruktiv. Output auf Deutsch."},
        {"role": "user", "content": f"""{prompt}

---

## USER PERSONA

{data['persona']}

---

## V4 IMPROVEMENT PLAN (Referenz)

{data.get('improvement_plan', 'N/A')}

---

## V4 MARKDOWN

{data['markdown']}

---

## V4 HTML

{data['html']}

---

Bewerte jetzt. Sei ehrlich und kritisch."""}
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        if "gpt-5" in str(e).lower() or "model" in str(e).lower():
            print(f"{MODEL} not available, falling back to {FALLBACK}...")
            response = client.chat.completions.create(
                model=FALLBACK,
                messages=messages,
                temperature=0.3,
            )
            return response.choices[0].message.content
        raise


def main():
    print("Loading V4 content (markdown + HTML)...")
    data = load_v4_content()

    print(f"Evaluating with {MODEL} (persona, honest, critical)...")
    client = OpenAI()
    result = evaluate(client, data)

    output_path = MODULE_DIR / "process-docs" / "V4-EVALUATION.md"
    output_path.write_text(result, encoding="utf-8")
    print(f"Evaluation saved to: {output_path}")
    print("\n--- Preview ---\n")
    print(result[:3500])
    if len(result) > 3500:
        print("\n... (see full file for rest)")
    return result


if __name__ == "__main__":
    main()
