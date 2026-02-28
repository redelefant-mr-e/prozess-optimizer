#!/usr/bin/env python3
"""
Grades the Patent Next Steps process quality using OpenAI.
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
        "00-Einleitung.md", "01-Standort-klaeren.md",
        "02-Ansprechpartner.md", "03-Zeitfenster-beachten.md",
        "04-Schutzstrategie-waehlen.md", "05-Prioritaeten-setzen.md",
        "06-Ergebnis.md",
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
    
    model = "gpt-5"
    
    prompt = """You are a harsh, critical quality assessor. Your job is to GRADE the "Patent Next Steps" process (Erfindung – Nächste Schritte, a German guide for inventors on the patenting process) using the USER PERSONA as your lens. Be genuinely critical – do not sugarcoat. If something is weak, say so. If the process fails the persona in some way, call it out.

## Your Task

Evaluate the process from EACH of these angles, using the persona as the reference:

### 1. Persona Fit
- Does the process actually serve the "Erfinder:in mit akademischem Hintergrund"?
- Where does it assume skills or knowledge the persona likely lacks?
- Where does it over-deliver (too detailed, boring) or under-deliver (missing support the persona needs)?
- Is it "nicht zu detailliert, nicht langweilig" as intended?

### 2. Completeness
- Are there gaps in the process? Steps missing? Transitions unclear?
- Does it cover all three contexts (Uni, Firma, Startup) equally well?
- What could a user get stuck on with no guidance?

### 3. Clarity & Actionability
- Are the instructions concrete enough for someone with little patent process experience?
- Where is the language vague or ambiguous?
- Do the "Tipp" sections actually help, or are they generic?

### 4. Risk & Liability
- Does the process adequately warn about its limitations (no legal advice)?
- Could a user be misled into thinking they've received legal advice when they haven't?
- Is the publication trap clearly explained?

### 5. Usability for the Target User
- Time: Is the process realistic for someone with limited time?
- Motivation: Does it give enough reason to act now?
- Drop-off: Where might users abandon the process? Why?

### 6. Structural & Scaffold Quality
- Is the flow logical? Any redundant or missing steps?
- Does the "So gehst du vor" structure work consistently?
- Are the outputs of each step clearly usable as inputs for the next?

---

## Output Format

Provide your assessment in this structure:

# Patent Next Steps: Quality Grade

## Overall Grade: [A / B / C / D / F]
**One-sentence verdict:** [Your blunt summary]

---

## 1. Persona Fit
[Critical assessment – what works, what doesn't, specific gaps]

## 2. Completeness
[Gaps, missing pieces, context bias]

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
