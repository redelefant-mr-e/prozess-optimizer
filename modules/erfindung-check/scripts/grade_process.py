#!/usr/bin/env python3
"""
Grades the Erfindung-Check process quality using OpenAI GPT-5.
Uses USER-PERSONA.md to evaluate from multiple critical angles.
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
    import subprocess
    subprocess.check_call(["pip", "install", "openai", "-q"])
    from openai import OpenAI


def load_content():
    """Load process files and user persona."""
    process_dir = MODULE_DIR / "process"
    docs_dir = MODULE_DIR / "process-docs"
    
    process_files = [
        "00-Einleitung.md", "01-Kategorie-waehlen.md",
        "02-Markt-scannen.md", "03-Patente-pruefen.md", "04-Publikationen-pruefen.md",
        "05-Treffer-bewerten.md", "06-Kern-schaerfen.md", "07-Ergebnis-ableiten.md",
    ]
    
    process_parts = []
    for f in process_files:
        p = process_dir / f
        if p.exists():
            process_parts.append(f"=== {f} ===\n{p.read_text(encoding='utf-8')}\n")
    
    persona_path = docs_dir / "USER-PERSONA.md"
    persona = persona_path.read_text(encoding="utf-8") if persona_path.exists() else ""
    
    return "\n".join(process_parts), persona


def main():
    process_content, persona_content = load_content()
    
    client = OpenAI()
    
    # Try gpt-5 first, fallback to gpt-4o
    model = "gpt-5"
    
    prompt = """You are a harsh, critical quality assessor. Your job is to GRADE the "Erfindung-Check" process (a German invention novelty check) using the USER PERSONA as your lens. Be genuinely critical – do not sugarcoat. If something is weak, say so. If the process fails the persona in some way, call it out.

## Your Task

Evaluate the process from EACH of these angles, using the persona as the reference:

### 1. Persona Fit
- Does the process actually serve the "unsichere Erfinder:in mit konkreter Idee"?
- Where does it assume skills or knowledge the persona likely lacks?
- Where does it over-deliver (complexity the persona doesn't need) or under-deliver (missing support the persona needs)?

### 2. Completeness
- Are there gaps in the process? Steps missing? Transitions unclear?
- Does it cover all four categories (Mechanik, Verfahren, Software, Medizin) equally well, or does it favor some?
- What could a user get stuck on with no guidance?

### 3. Clarity & Actionability
- Are the instructions concrete enough for someone with no patent/search experience?
- Where is the language vague or ambiguous?
- Do the "Tipp" sections actually help, or are they generic?

### 4. Risk & Liability
- Does the process adequately warn about its limitations (e.g., "nicht absolute Sicherheit")?
- Could a user be misled into thinking they've done a proper patent search when they haven't?
- Any legal or practical risks?

### 5. Usability for the Target User
- Time: Is the process realistic for someone "mit begrenzter Zeit"?
- Motivation: Does it address the "zu spät klären" problem – i.e., does it give enough reason to start now?
- Drop-off: Where might users abandon the process? Why?

### 6. Structural & Scaffold Quality
- Is the flow logical? Any redundant or missing steps?
- Does the "So gehst du vor" structure work consistently?
- Are the outputs of each step clearly usable as inputs for the next?

---

## Output Format

Provide your assessment in this structure:

# Erfindung-Check: Quality Grade

## Overall Grade: [A / B / C / D / F]
**One-sentence verdict:** [Your blunt summary]

---

## 1. Persona Fit
[Critical assessment – what works, what doesn't, specific gaps]

## 2. Completeness
[Gaps, missing pieces, category bias]

## 3. Clarity & Actionability
[Vague spots, unclear instructions, weak tips]

## 4. Risk & Liability
[Warnings, potential misuse, legal/practical concerns]

## 5. Usability for Target User
[Time realism, motivation, drop-off points]

## 6. Structural Quality
[Flow, consistency, input-output handoffs]

---

## Top 5 Critical Issues (Prioritized)
1. [Most serious]
2. ...
5. [Least serious of the five]

## Top 3 Strengths
1. ...
2. ...
3. ...

## Recommendation
[One paragraph: What should the process authors do first?]
"""

    print(f"Grading process with {model} (critical assessment from persona perspective)...")
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a rigorous quality assessor. Be critical and honest. Do not praise unnecessarily. Identify real weaknesses. Output structured markdown."},
                {"role": "user", "content": f"{prompt}\n\n---\n\n## USER PERSONA (Reference)\n\n{persona_content}\n\n---\n\n## PROCESS CONTENT (To Grade)\n\n{process_content}"}
            ],
            temperature=0.4,
        )
    except Exception as e:
        if "gpt-5" in str(e).lower() or "model" in str(e).lower():
            print("GPT-5 not available, falling back to gpt-4o...")
            model = "gpt-4o"
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a rigorous quality assessor. Be critical and honest. Do not praise unnecessarily. Identify real weaknesses. Output structured markdown."},
                    {"role": "user", "content": f"{prompt}\n\n---\n\n## USER PERSONA (Reference)\n\n{persona_content}\n\n---\n\n## PROCESS CONTENT (To Grade)\n\n{process_content}"}
                ],
                temperature=0.4,
            )
        else:
            raise
    
    result = response.choices[0].message.content
    
    output_path = MODULE_DIR / "process-docs" / "PROCESS-QUALITY-GRADE.md"
    output_path.write_text(result, encoding="utf-8")
    
    print(f"Grade complete. Saved to: {output_path}")
    return result


if __name__ == "__main__":
    main()
