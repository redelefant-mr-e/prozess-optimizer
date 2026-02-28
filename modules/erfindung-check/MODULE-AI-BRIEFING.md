# Erfindung-Check Module: AI Reuse Briefing

Use this briefing when building another module that should follow the same logic and structure as Erfindung-Check.

---

## Module Goal

**Erfindung-Check:** Invention novelty assessment → status (Neu/Unklar/Bekannt) + concrete next action.

---

## Scaffold Pattern

Every process step uses this structure:

| Element | Purpose |
|--------|---------|
| **Titel** | `# Schritt N: [Name]` – orientation, progress |
| **Ziel** | One-line success criterion (optional for intro steps) |
| **So gehst du vor** | Numbered sub-steps, concrete actions |
| **Tipp** | Typical pitfalls + solution (optional) |
| **Fazit** | Output checklist, bridge to next step |
| **Nächster Schritt** | Link to next step (or "So geht's weiter" at end) |

---

## Persona

**Target user:** Unsichere Erfinder:in mit konkreter Idee
- Limited time
- No patent/search expertise
- Needs structure and clear boundaries
- Wants pragmatic first assessment, not legal certainty

---

## Optimization Loop

1. **Source** → Write process steps (00–N) in `process/`
2. **Grade** → Run `grade_process.py` → `PROCESS-QUALITY-GRADE.md`
3. **Optimize** → Run `optimize_process.py` (Phase 1 + Phase 2) → `optimized/refined/`
4. **Evaluate** → (Optional) Run evaluation scripts, generate examples

---

## Design Template

**Shared:** `shared/design-templates/step-wizard/`
- `step-wizard.css` – reusable styles
- `step-wizard.js` – step navigation
- `template.html` – minimal example

Use for interactive step-by-step UIs. One step at a time, progress bar, Lucide icons.

---

## How to Replicate

1. Create `modules/[your-module]/` with:
   - `process/` – source steps
   - `process-docs/` – scaffold, persona, quality grade
   - `optimized/` – steps + ui
   - `scripts/` – analyze, optimize, grade (adapt paths)
   - `assets/` – reference materials

2. Define your own PROCESS-SCAFFOLD.md and USER-PERSONA.md.

3. Adapt `optimize_process.py` to use your module paths (BASE_DIR = module root).

4. Use `shared/design-templates/step-wizard/` for UI; link CSS/JS with correct relative paths.

5. Add MODULE-DESCRIPTION.md and MODULE-AI-BRIEFING.md for documentation.

---

## Key Concepts (Erfindung-Check Specific)

- **Erfindung:** New, concrete solution others could replicate
- **Kernprinzip:** Mechanism/structure that defines the invention
- **Prior Art:** Existing products, patents, publications
- **Kernidee:** Sentence pattern: *"Neu ist, dass [Mechanismus] so ausgeführt ist, dass [Wirkung] unter [Bedingung] entsteht."*
