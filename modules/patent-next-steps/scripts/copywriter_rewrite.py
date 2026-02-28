#!/usr/bin/env python3
"""
Copywriter rewrite: Uses GPT-5.1 to make the patent-next-steps text flow more naturally.
Reduces the "bullet-point forced" feel – more prose, warmer tone, less choppy.
Keeps structure, tables, and essential info. Output: refined-V3/
"""

import os
import re
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
INPUT_DIR = MODULE_DIR / "optimized" / "refined-V2"
OUTPUT_DIR = MODULE_DIR / "optimized" / "refined-V3"


def load_file(path):
    return path.read_text(encoding="utf-8")


def copywriter_rewrite(client, content, filename):
    """Rewrite content with a more natural, flowing style."""
    prompt = """Du bist ein erfahrener Copywriter. Deine Aufgabe: Den folgenden Text so umschreiben, dass er weniger "bullet-point forced" wirkt – sondern natürlicher, fließender, wie von einem erfahrenen Kollegen erzählt.

## Was du ändern sollst

- **Weniger Listen, wo Prosa besser passt:** Statt starrer Bullet-Listen lieber fließende Absätze – aber ohne Information zu verlieren
- **Wärmerer, kollegialer Ton:** Wie ein:e Mentor:in, der/die einem erklärt, nicht wie eine Checkliste
- **Übergänge schaffen:** Zwischen Abschnitten sanft verbinden, nicht abrupt von Punkt zu Punkt springen
- **Kurze Sätze lockern:** Wo es sinnvoll ist, Sätze verbinden oder variieren – aber nicht zu lang

## Was du NICHT ändern sollst

- **Tabellen:** Behalten – sie sind für Referenz wichtig
- **Struktur:** Überschriften (# ## ###), Schritt-Nummerierung, "Nächster Schritt"-Links
- **E-Mail-Vorlage / Code-Blöcke:** Unverändert lassen
- **Fachbegriffe:** Erfindungsberater:in, TTO, Meldepflicht, etc. – alle bleiben
- **Maria-Beispiel:** Das durchgängige Beispiel bleibt, kann aber flüssiger formuliert werden

## Format

- Output auf Deutsch
- Markdown beibehalten
- Gleiche Dateistruktur (Überschriften, Abschnitte)
- Keine zusätzlichen Abschnitte oder weggelassene Informationen

## Stil-Vorgabe

Statt: "Du solltest jetzt haben: Eine Checkliste. Das verhindert Fehler."
Besser: "Am Ende dieses Schritts hast du eine klare Checkliste – und damit eine gute Absicherung gegen den häufigsten Fehler."

Statt: "1. Schau in Arbeitsvertrag. 2. Suche im Intranet. 3. Frag Vorgesetzte."
Besser: "Zuerst wirfst du einen Blick in deinen Arbeitsvertrag oder die Promotionsordnung – nach Stichworten wie Erfindung oder Meldepflicht. Wenn du dort nichts findest, hilft eine Suche im Intranet. Und falls auch das nicht weiterführt: Ein kurzer Anruf bei deiner:m Vorgesetzten oder der Verwaltung klärt meist schnell, an wen du dich wenden solltest."

Schreibe den Text jetzt um."""

    messages = [
        {"role": "system", "content": "Du bist ein Copywriter mit Gespür für natürlichen, einladenden Ton. Du behältst alle Informationen bei, machst den Text aber fließender und weniger listenlastig. Output: Markdown."},
        {"role": "user", "content": f"{prompt}\n\n---\n\n## Zu bearbeitender Text\n\n{content}"}
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.5,
        )
        return response.choices[0].message.content
    except Exception as e:
        if "gpt-5" in str(e).lower() or "model" in str(e).lower():
            print(f"{MODEL} not available, falling back to {FALLBACK}...")
            response = client.chat.completions.create(
                model=FALLBACK,
                messages=messages,
                temperature=0.5,
            )
            return response.choices[0].message.content
        raise


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    client = OpenAI()

    step_files = [
        "00-Einleitung.md", "01-Standort-und-Ansprechpartner.md",
        "02-Zeitfenster-beachten.md", "03-Schutzstrategie-waehlen.md",
        "04-Prioritaeten-setzen.md", "05-Ergebnis.md"
    ]

    for step_file in step_files:
        fp = INPUT_DIR / step_file
        if not fp.exists():
            print(f"Skipping {step_file} (not found)")
            continue

        print(f"Rewriting {step_file}...")
        content = load_file(fp)
        rewritten = copywriter_rewrite(client, content, step_file)

        out_path = OUTPUT_DIR / step_file
        out_path.write_text(rewritten, encoding="utf-8")
        print(f"  -> {out_path}")

    print(f"\nDone. Output in {OUTPUT_DIR}")
    return OUTPUT_DIR


if __name__ == "__main__":
    main()
