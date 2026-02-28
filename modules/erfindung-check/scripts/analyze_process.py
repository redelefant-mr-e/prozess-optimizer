#!/usr/bin/env python3
"""
Analyzes the Erfindung-Check-Prozess using OpenAI to create an AI-understandable process description.
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
        "00-Einleitung.md",
        "01-Kategorie-waehlen.md",
        "02-Markt-scannen.md",
        "03-Patente-pruefen.md",
        "04-Publikationen-pruefen.md",
        "05-Treffer-bewerten.md",
        "06-Kern-schaerfen.md",
        "07-Ergebnis-ableiten.md",
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
    
    prompt = """You are analyzing a German-language process document called "Erfindung-Check" (Invention Check). 
Your task is to create a comprehensive, structured document that enables an AI assistant to FULLY UNDERSTAND and EXECUTE this process when helping a user.

The output must be in English and structured so that:
1. An AI can guide a user through each step
2. An AI knows exactly what to ask, what to collect, and what to produce at each step
3. An AI understands the decision logic and branching (e.g., when to recommend "neu", "unklar", or "bekannt")
4. An AI can suggest the right sources, keywords, and evaluation criteria per category

Create a document with these sections:

## PROCESS OVERVIEW
- Purpose and goal
- Target user
- Key concepts (Erfindung, Kernprinzip, Prior Art, etc.)

## STEP-BY-STEP EXECUTION GUIDE
For each step (0-7), provide:
- Step name and purpose
- Inputs required (from user or previous steps)
- Actions to perform (concrete, actionable)
- Outputs to produce
- Decision points and branching logic
- Category-specific variations (Mechanik, Verfahren, Software, Medizin)
- Suggested tools/sources
- Templates or table structures to use

## EVALUATION FRAMEWORK
- How to classify treffer (hits): gleiche Funktion/anderer Mechanismus, ähnlicher Mechanismus/anderer Zweck, gleiche Funktion und Mechanismus
- How to derive the final status: Neu wirkt plausibel / Unklar / Eher bekannt
- Next actions per status

## KEYWORD & SEARCH STRATEGY
- How to build keyword sets per category
- Search term structure (Funktion + Objekt + Kontext)
- Sources per category

## KERNIDEE (CORE IDEA) TEMPLATE
- The sentence structure pattern
- How to derive variants
- Quality criteria (avoid vague terms like "besser", "effizienter")

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
