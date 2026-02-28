#!/usr/bin/env python3
"""
Evaluates Patent Next Steps V3 (copywriter-refined) using GPT-5.1.
Perspective: academic inventor persona. Honest, critical, UI-focused.
Goal: Identify everything that increases chances to build the best version.
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


def load_v3_content():
    """Load V3 markdown, HTML, persona."""
    parts = {}
    parts["persona"] = (MODULE_DIR / "process-docs" / "USER-PERSONA.md").read_text(encoding="utf-8")

    step_files = [
        "00-Einleitung.md", "01-Standort-und-Ansprechpartner.md",
        "02-Zeitfenster-beachten.md", "03-Schutzstrategie-waehlen.md",
        "04-Prioritaeten-setzen.md", "05-Ergebnis.md"
    ]
    md_dir = MODULE_DIR / "optimized" / "refined-V3"
    md_parts = []
    for f in step_files:
        fp = md_dir / f
        if fp.exists():
            md_parts.append(f"=== {f} ===\n{fp.read_text(encoding='utf-8')}\n")
    parts["markdown"] = "\n".join(md_parts)

    html_path = MODULE_DIR / "optimized" / "ui" / "patent-next-steps-V3.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        parts["html"] = html[:18000] + "\n...[truncated]..." if len(html) > 18000 else html
    else:
        parts["html"] = "(V3 HTML not found)"

    return parts


def evaluate(client, data):
    prompt = """Du bewertest **Patent Next Steps V3** – die copywriter-überarbeitete Version des Guides für akademische Erfinder:innen. Deine Bewertung soll **ehrlich, kritisch und konstruktiv** sein. Ziel: Alles identifizieren, was die Chancen erhöht, die beste Version des Guides zu bauen.

## Deine Rolle

Du bewertest aus der Perspektive der **Persona** (akademische Erfinder:in):
- Forscher:in, Doktorand:in oder Postdoc mit Erfindung/Prototyp
- Wenig Überblick über Patentprozess, Meldepflichten, Ansprechpartner:innen
- Sucht Orientierung: Welche Schritte? Wen wann einbeziehen?
- Erwartet: kompakt, praxisnah, nicht überfordernd

## Bewertungsdimensionen

### 1. Inhalt & Ton (Copywriter-Pass)
- Liest sich der Text jetzt natürlicher und weniger „bullet-point forced“?
- Wo ist es zu lang geworden? Wo zu redundant?
- Wo fehlt trotzdem noch Konkretheit (Checklisten, Beispiele)?
- Gibt es Stellen, an denen die Prosa die Klarheit beeinträchtigt?

### 2. UI & Nutzererfahrung
- Wie gut funktioniert die Wizard-Navigation (6 Schritte)?
- Sind die Blöcke (Ziel, Info, Beispiel, Tipp, Kontext) visuell sinnvoll getrennt?
- Ist die Informationsdichte pro Schritt angemessen – überfordert oder zu dünn?
- Gibt es Scroll-Probleme, zu lange Schritte, unübersichtliche Tabellen?
- Fehlen visuelle Hinweise (z.B. Fortschritt, „Du bist hier“)?

### 3. Persona-Tauglichkeit
- Würde die Persona nach dem Durchlauf wissen, was sie als Nächstes tun soll?
- Sind die „Spezifisch für deinen Kontext“-Blöcke hilfreich oder zu generisch?
- Ist das Maria-Beispiel durchgängig und nachvollziehbar?
- Wo bleibt die Persona unsicher oder überfordert?

### 4. Lücken & Schwachstellen
- Was fehlt komplett? (z.B. Erfindungsberater:in-Rolle, konkrete Formulare, Links)
- Welche Stolpersteine werden nicht adressiert?
- Gibt es Widersprüche oder veraltete Infos?

### 5. Konkrete Verbesserungsvorschläge (priorisiert)
- Top 5 Änderungen, die den größten Impact hätten
- Pro Vorschlag: Was genau? Wo? Warum?

---

## Output-Format

Erstelle ein strukturiertes Markdown-Dokument:

# Patent Next Steps V3: Evaluation

## Executive Summary (4–5 Sätze)
[Gesamteindruck: Stärken, kritische Punkte, Empfehlung]

## 1. Inhalt & Ton
[Copywriter-Ergebnis: Was funktioniert, was nicht. Länge, Redundanz, Klarheit.]

## 2. UI & Nutzererfahrung
[Wizard, Blöcke, Informationsdichte, Scroll, visuelle Hinweise. Konkrete UX-Probleme.]

## 3. Persona-Tauglichkeit
[Handlungsfähigkeit nach Durchlauf, Kontext-Blöcke, Maria-Beispiel, Überforderung.]

## 4. Lücken & Schwachstellen
[Was fehlt, Stolpersteine, Widersprüche.]

## 5. Top 5 Verbesserungsvorschläge (priorisiert)
1. [Konkrete Änderung] – [Begründung]
2. ...
3. ...
4. ...
5. ...

## 6. Was bereits gut funktioniert
[3–4 Punkte, die beibehalten werden sollten]

## 7. Quick Wins (schnell umsetzbar)
[2–3 kleine Änderungen mit hohem Nutzen]

---

Sei **ehrlich und kritisch**. Keine Höflichkeitsfloskeln. Konkrete Verweise auf Schritte, Abschnitte oder Zeilen. Output auf Deutsch."""

    messages = [
        {"role": "system", "content": "Du bist ein kritischer UX- und Content-Experte. Du bewertest Guides für akademische Erfinder:innen. Sei ehrlich, konkret, konstruktiv. Keine Schmeichelei. Output auf Deutsch."},
        {"role": "user", "content": f"""{prompt}

---

## USER PERSONA (Referenz)

{data['persona']}

---

## V3 MARKDOWN (refined-V3/)

{data['markdown']}

---

## V3 HTML (patent-next-steps-V3.html)

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
    print("Loading V3 content (markdown + HTML)...")
    data = load_v3_content()

    print(f"Evaluating with {MODEL} (persona, honest, critical, UI-focused)...")
    client = OpenAI()
    result = evaluate(client, data)

    output_path = MODULE_DIR / "process-docs" / "V3-EVALUATION.md"
    output_path.write_text(result, encoding="utf-8")
    print(f"Evaluation saved to: {output_path}")
    print("\n--- Preview ---\n")
    print(result[:3500])
    if len(result) > 3500:
        print("\n... (see full file for rest)")
    return result


if __name__ == "__main__":
    main()
