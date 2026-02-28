#!/usr/bin/env python3
"""
Analyzes the Erfindungsbeschreibung process using OpenAI to create an AI-understandable process description.
"""

import os
from pathlib import Path

# Load .env from project root
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
    print("Installing openai package...")
    import subprocess
    subprocess.check_call(["pip", "install", "openai", "-q"])
    from openai import OpenAI


def load_process_content():
    """Load all process files into a single string."""
    base = MODULE_DIR / "process"
    files = [
        "00-Einleitung.md", "01-Kern-der-Neuerung.md",
        "02-Stand-der-Technik.md", "03-Technische-Loesung.md",
        "04-Struktur-und-Form.md", "05-Typische-Fehler-vermeiden.md",
        "06-Ergebnis.md",
    ]
    parts = []
    for f in files:
        p = base / f
        if p.exists():
            parts.append(f"=== {f} ===\n{p.read_text(encoding='utf-8')}\n")
    return "\n".join(parts)


def main():
    content = load_process_content()

    client = OpenAI()

    prompt = """You are analyzing a German-language process document called "Erfindungsbeschreibung" (Invention Documentation Guide).
Your task is to create a comprehensive, structured document that enables an AI assistant to FULLY UNDERSTAND and EXECUTE this process when helping a user document their invention for TTO forms.

The output must be in English and structured so that:
1. An AI can guide a user through each step
2. An AI knows exactly what to ask, what to collect, and what to produce at each step
3. An AI understands the key concepts (Technische Aufgabe, Stand der Technik, Technische Lösung, TUM rule)
4. An AI can reference the examples (TUM, HM, JMU, THI) appropriately

Create a document with these sections:

## PROCESS OVERVIEW
- Purpose and goal (help inventors document for TTO forms)
- Target user (inventor who can explain but not document)
- Key concepts (Technische Aufgabe, Stand der Technik, Technische Lösung, TUM rule: "what one must do so that it works")

## STEP-BY-STEP EXECUTION GUIDE
For each step (0-6), provide:
- Step name and purpose
- Inputs required (from user or previous steps)
- Actions to perform (concrete, actionable)
- Outputs to produce
- Example references (HM TI-RSS, JMU Prodrugs, TUM Protein LSC, THI Cu metallization)

## STRUCTURE TEMPLATE
- Technische Aufgabe und Gebiet
- Stand der Technik
- Behebung der Nachteile
- Technische Lösung
- Vorteile
- Literaturverzeichnis

## TUM RULE
- "Do not describe why something works, but rather what one must do so that it works"
- Target: "average person skilled in the art"
- Avoid: pages of equations; lengthy pre-trials as main content

## CHECKLIST FRAMEWORK
- Content checklist before submission
- Form checklist (length, sketches)
- What to avoid (equations, "why" instead of "what", too vague)

Be thorough and precise. An AI reading this document should be able to run the entire process without referring back to the original German files."""

    print("Sending process content to OpenAI for analysis...")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert at analyzing process documentation and creating AI-executable guides. Output clear, structured markdown."},
            {"role": "user", "content": f"{prompt}\n\n---\n\nORIGINAL PROCESS CONTENT:\n\n{content}"}
        ],
        temperature=0.3,
    )

    result = response.choices[0].message.content

    output_path = MODULE_DIR / "process-docs" / "AI-PROCESS-GUIDE.md"
    output_path.write_text(result, encoding="utf-8")

    print(f"Analysis complete. Saved to: {output_path}")
    return result


if __name__ == "__main__":
    main()
