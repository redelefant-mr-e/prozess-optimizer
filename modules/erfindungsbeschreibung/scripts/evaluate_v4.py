#!/usr/bin/env python3
"""
Evaluates Erfindungsbeschreibung module using GPT-5.1 (or gpt-4o).
Perspective: inventor who can explain but not document. Honest, critical, UI-focused.
Test–Validate–Improve loop for the module.
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

STEP_FILES = [
    "00-Einleitung.md", "01-Kern-der-Neuerung.md",
    "02-Stand-der-Technik.md", "03-Technische-Loesung.md",
    "04-Struktur-und-Form.md", "05-Typische-Fehler-vermeiden.md",
    "06-Ergebnis.md",
]


def load_content():
    """Load markdown, HTML (if exists), persona, examples."""
    parts = {}
    parts["persona"] = (MODULE_DIR / "process-docs" / "USER-PERSONA.md").read_text(encoding="utf-8")

    # Try refined-V1 first, then process
    md_dir = MODULE_DIR / "optimized" / "refined-V1"
    if not md_dir.exists():
        md_dir = MODULE_DIR / "process"
    md_parts = []
    for f in STEP_FILES:
        fp = md_dir / f
        if fp.exists():
            md_parts.append(f"=== {f} ===\n{fp.read_text(encoding='utf-8')}\n")
    parts["markdown"] = "\n".join(md_parts) if md_parts else "(No markdown found)"

    html_path = MODULE_DIR / "optimized" / "ui" / "erfindungsbeschreibung.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        parts["html"] = html[:18000] + "\n...[truncated]..." if len(html) > 18000 else html
    else:
        parts["html"] = "(HTML not found)"

    # Load example extracts
    examples_dir = MODULE_DIR / "examples"
    if examples_dir.exists():
        ex_parts = []
        for f in ["hm_ti_rss.md", "jmu_prodrugs.md", "tum_protein_lsc.md"]:
            fp = examples_dir / f
            if fp.exists():
                ex_parts.append(f"=== {f} ===\n{fp.read_text(encoding='utf-8')}\n")
        parts["examples"] = "\n".join(ex_parts) if ex_parts else "(No examples)"
    else:
        parts["examples"] = "(No examples)"

    return parts


def evaluate(client, data):
    prompt = """Du bewertest **Erfindungsbeschreibung** – die Anleitung zur Dokumentation von Erfindungen für TTO-Formulare. Deine Bewertung soll **ehrlich, kritisch und konstruktiv** sein.

## Deine Rolle

Du bewertest aus der Perspektive der **Persona** (Erfinder:in, die erklären kann, aber nicht dokumentieren):
- Hat Erfindung; kann sie mündlich erklären
- Schwierigkeiten bei Dokumentation für TTO-Formulare
- Unsicher: Kern der Neuerung? Welche Details? Verständlich ohne zu viel preiszugeben?

## Bewertungsdimensionen

### 1. V4-Verbesserungen: Erreicht?
- Sind die Beispiele (TUM, HM, JMU, THI) effektiv eingebunden?
- Ist die TUM-Regel ("what one must do so that it works") klar?
- Struktur: Kern → Stand der Technik → Lösung → Form → Fehler → Ergebnis – logisch?

### 2. Inhalt & Klarheit
- Sind Fachbegriffe erklärt? (Technische Aufgabe, Stand der Technik, Technische Lösung)
- **Verständlichkeit der Beispiele für Fachfremde:** Kann jemand, der die spezifischen Erfindungen (TI-RSS, BNN-Heterozyklen, etc.) nicht kennt, die Beispiele verstehen? Haben die Beispiele genug Kontext („Worum geht es?", „Was ist das Neue?")?
- Wo fehlt noch Konkretheit?
- Ist die Länge angemessen?

### 3. UI & Nutzererfahrung (falls HTML vorhanden)
- Wizard-Navigation, Blöcke, Informationsdichte
- Stepper verständlich?

### 4. Lücken & Schwachstellen
- Was fehlt? Unerklärte Begriffe? Stolpersteine?
- Werden die Beispiel-Extrakte sinnvoll genutzt?

### 5. Top 5 Verbesserungsvorschläge (priorisiert)

---

## Output-Format

# Erfindungsbeschreibung: Evaluation

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
        {"role": "system", "content": "Du bist ein kritischer UX- und Content-Experte. Bewertest Guides für Erfinder:innen. Ehrlich, konkret, konstruktiv. Output auf Deutsch."},
        {"role": "user", "content": f"""{prompt}

---

## USER PERSONA

{data['persona']}

---

## MARKDOWN

{data['markdown']}

---

## HTML

{data['html']}

---

## EXAMPLES (TUM, HM, JMU)

{data.get('examples', 'N/A')}

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
    print("Loading content (markdown + HTML + examples)...")
    data = load_content()

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
