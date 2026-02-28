#!/usr/bin/env python3
"""
AI Process Optimization Machine for Patent Next Steps

Uses PROCESS-SCAFFOLD.md to generate optimized versions of the Patent Next Steps process.
- Phase 1: Generate optimized variant(s)
- Phase 2: Review and refine the output

Uses GPT-5 (falls back to gpt-4o if unavailable).
"""

import os
import re
from pathlib import Path
from datetime import datetime

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

MODEL = "gpt-5"
FALLBACK_MODEL = "gpt-4o"
BASE_DIR = MODULE_DIR
OUTPUT_DIR = BASE_DIR / "optimized"


def load_all_inputs():
    """Load scaffold, process, persona, quality grade."""
    docs_dir = BASE_DIR / "process-docs"
    files = {
        "scaffold": "PROCESS-SCAFFOLD.md",
        "persona": "USER-PERSONA.md",
        "quality_grade": "PROCESS-QUALITY-GRADE.md",
    }
    content = {}
    for key, fname in files.items():
        p = docs_dir / fname
        content[key] = p.read_text(encoding="utf-8") if p.exists() else ""
    
    process_dir = BASE_DIR / "process"
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
    content["process"] = "\n".join(process_parts)
    
    return content


def get_client():
    return OpenAI()


def call_ai(client, messages, model=MODEL):
    """Call OpenAI, fallback to gpt-4o if model unavailable."""
    try:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.4,
        ).choices[0].message.content
    except Exception as e:
        if "gpt-5" in str(e).lower() or "model" in str(e).lower():
            return client.chat.completions.create(
                model=FALLBACK_MODEL,
                messages=messages,
                temperature=0.4,
            ).choices[0].message.content
        raise


def phase1_generate(client, inputs):
    """Phase 1: Generate optimized process variant(s)."""
    prompt = """You are a process design expert. Your task is to create an OPTIMIZED version of the "Patent Next Steps" process (Erfindung – Nächste Schritte).

## Inputs
- PROCESS-SCAFFOLD: Defines the structure (Titel, Ziel, So gehst du vor, Tipp, Fazit, Nächster Schritt)
- USER-PERSONA: Target user = "Erfinder:in mit akademischem Hintergrund" – needs overview, not too detailed, not boring
- QUALITY-GRADE: Critical feedback (if present) – address any issues raised

## Your Task

Create ONE optimized process that improves the current version. You MAY:

1. **Combine steps** – if they share the same logic
2. **Add steps** – if the persona needs more guidance
3. **Split steps** – if clarity improves
4. **Reorder** – if the flow makes more sense differently
5. **Add elements** – e.g., clearer input-output handoffs; more concrete Tipps

## Constraints
- MUST follow the scaffold structure for each step
- MUST serve the persona: compact, practical, not too detailed, not boring
- MUST add a clear limitation/risk warning early (no legal advice)
- Output in German (same language as original)
- Each step as separate markdown block, clearly delimited

## Output Format (IMPORTANT – follow exactly)

First, output a RATIONALE section (markdown) explaining:
- What you changed and why
- Step mapping (old steps → new steps)
- How each change addresses quality or persona needs

Then output each step. Use this EXACT delimiter format for each file:

---
FILE: 00-Einleitung.md
---
[full markdown content of step 0]
---
FILE: 01-Standort-klaeren.md
---
[full markdown content of step 1]
---
... and so on for all steps (00 through 06).

Filenames: 00-Einleitung.md, 01-Standort-klaeren.md, 02-Ansprechpartner.md, 03-Zeitfenster-beachten.md, 04-Schutzstrategie-waehlen.md, 05-Prioritaeten-setzen.md, 06-Ergebnis.md
Also include README-optimized.md with overview table.

Generate the complete optimized process. Be systematic and thorough."""

    messages = [
        {"role": "system", "content": "You are a process design expert. Output structured markdown. Be systematic and address the quality feedback directly."},
        {"role": "user", "content": f"{prompt}\n\n---\n\n## SCAFFOLD\n\n{inputs['scaffold']}\n\n---\n\n## USER PERSONA\n\n{inputs['persona']}\n\n---\n\n## QUALITY GRADE (Critical Feedback)\n\n{inputs['quality_grade']}\n\n---\n\n## CURRENT PROCESS\n\n{inputs['process']}"}
    ]
    
    return call_ai(client, messages)


def phase2_review_and_refine(client, phase1_output, inputs):
    """Phase 2: Review Phase 1 output and produce refined version."""
    prompt = """You are a critical reviewer. The following is an AI-generated OPTIMIZED version of the Patent Next Steps process (from Phase 1).

Your task: REVIEW it critically, then REFINE it.

## Review Checklist
1. Does it follow the scaffold structure consistently?
2. Does it actually serve the persona (compact, practical, not too detailed, not boring)?
3. Are the step transitions clear? Input-output handoffs explicit?
4. Are there any logical gaps, redundancies, or new problems introduced?
5. Is the risk/limitation warning adequate?
6. Are the Tipps concrete and actionable (not generic)?

## Your Task
1. First output a REVIEW section: What's good? What's still weak? What would you change?
2. Then output the REFINED process: Apply your improvements. Fix any issues you found.
3. Use the same output format as Phase 1:
   - RATIONALE (updated)
   - Each step as --- FILE: XX-name.md --- [content] ---

If the Phase 1 output is already strong, your "refinement" may be minimal – but still apply at least 2-3 concrete improvements. Be critical."""

    messages = [
        {"role": "system", "content": "You are a critical process reviewer. Identify weaknesses and produce an improved version. Output structured markdown."},
        {"role": "user", "content": f"{prompt}\n\n---\n\n## PHASE 1 OUTPUT (To Review & Refine)\n\n{phase1_output}\n\n---\n\n## ORIGINAL SCAFFOLD (Reference)\n\n{inputs['scaffold'][:3000]}..."}
    ]
    
    return call_ai(client, messages)


def parse_and_save(output_text, output_dir):
    """Parse the AI output and save to files."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    file_pattern = r'---\s*FILE:\s*([^\n\-]+?)\s*---\s*\n([\s\S]*?)(?=\s*---\s*(?:FILE:|$))'
    matches = re.findall(file_pattern, output_text)
    
    if not matches:
        step_pattern = r'(# Schritt \d+:[^\n]+)\n([\s\S]*?)(?=# Schritt \d+:|## RATIONALE|## REVIEW|\Z)'
        step_matches = re.findall(step_pattern, output_text)
        for header, content in step_matches:
            num_match = re.search(r'Schritt (\d+):\s*(.+)', header)
            if num_match:
                num, title = num_match.groups()
                safe_name = re.sub(r'[^\w\s-]', '', title).strip()[:30].replace(' ', '-')
                filename = f"{int(num):02d}-{safe_name}.md"
                matches.append((filename, f"# Schritt {num}: {title.strip()}\n\n{content.strip()}"))
    
    rationale_match = re.search(r'^([\s\S]*?)(?=---\s*FILE:|# Schritt 0:)', output_text)
    rationale = rationale_match.group(1).strip() if rationale_match else ""
    if rationale and len(rationale) > 100:
        (output_dir / "RATIONALE.md").write_text(rationale, encoding="utf-8")
    
    for filename, content in matches:
        filename = filename.strip()
        if not filename.endswith(".md"):
            filename += ".md"
        content = re.sub(r'\s*---\s*FILE:[\s\S]*$', '', content.strip())
        filepath = output_dir / filename
        filepath.write_text(content, encoding="utf-8")
    
    return len(matches)


def run_pipeline():
    """Run the full optimization pipeline."""
    print("Loading inputs...")
    inputs = load_all_inputs()
    
    client = get_client()
    
    print("Phase 1: Generating optimized process...")
    phase1_output = phase1_generate(client, inputs)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "phase1_raw.md").write_text(phase1_output, encoding="utf-8")
    
    print("Phase 2: Reviewing and refining...")
    phase2_output = phase2_review_and_refine(client, phase1_output, inputs)
    
    (OUTPUT_DIR / "phase2_raw.md").write_text(phase2_output, encoding="utf-8")
    
    refined_dir = OUTPUT_DIR / "refined"
    file_count = parse_and_save(phase2_output, refined_dir)
    
    draft_dir = OUTPUT_DIR / "draft"
    parse_and_save(phase1_output, draft_dir)
    
    log = f"""# Optimization Log
Generated: {datetime.now().isoformat()}

## Pipeline
1. Phase 1: Generated optimized process
2. Phase 2: Reviewed and refined Phase 1 output

## Output
- `draft/` – Phase 1 output (parsed)
- `refined/` – Phase 2 output (final refined process)
- `phase1_raw.md` – Full Phase 1 response
- `phase2_raw.md` – Full Phase 2 response

## Files written to refined/: {file_count}
"""
    (OUTPUT_DIR / "OPTIMIZATION-LOG.md").write_text(log, encoding="utf-8")
    
    print(f"Done. Output in {OUTPUT_DIR}")
    return OUTPUT_DIR


if __name__ == "__main__":
    run_pipeline()
