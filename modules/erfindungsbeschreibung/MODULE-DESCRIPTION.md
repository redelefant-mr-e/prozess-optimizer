# Erfindungsbeschreibung Module: Detailed Description

## Purpose

The Erfindungsbeschreibung module guides inventors through the process of **documenting their invention** for typical TTO (Technology Transfer Office) invention disclosure forms at universities. It answers: What is the core novelty? Which details matter? How to keep it understandable without revealing too much? Output: **structured description** + **practical checklist** for filling out TTO forms.

---

## Process Flow

The process guides users through seven steps (0–6):

| Step | Name | Purpose | Output |
|------|------|---------|--------|
| 0 | Einleitung | Why good documentation matters; typical pitfalls | Readiness |
| 1 | Kern der Neuerung identifizieren | What is truly new? Delineation from prior work | Core in 1–2 sentences |
| 2 | Stand der Technik skizzieren | What exists? What are the disadvantages? | Short bullet points |
| 3 | Technische Lösung beschreiben | What must one do to make it work? | Clear solution sketch |
| 4 | Struktur und Form | Technical task → Prior art → Solution; 4 pages; sketches | Structured outline |
| 5 | Typische Fehler vermeiden | Too much/too little; equations; why vs. what | Checklist |
| 6 | Ergebnis | Summary, next steps, TTO form | Ready template + next action |

---

## Optimization Pipeline

Same as patent-next-steps:

1. **Grade** – `grade_process.py` → `PROCESS-QUALITY-GRADE.md`
2. **Optimize** – `optimize_process.py` (Phase 1 + Phase 2) → `optimized/refined/`, `optimized/draft/`
3. **Analyze** – `analyze_process.py` → `AI-PROCESS-GUIDE.md`
4. **Generate examples** – `generate_examples.py` → `PROZESS-BEISPIEL.json`
5. **Evaluate** – `evaluate_v4.py` → Test–Validate–Improve loop with GPT-5.1

---

## Scripts and Roles

| Script | Role | Output |
|--------|------|--------|
| `analyze_process.py` | Create AI-executable guide | `process-docs/AI-PROCESS-GUIDE.md` |
| `optimize_process.py` | Phase 1 + Phase 2 optimization | `optimized/refined/`, `optimized/draft/` |
| `grade_process.py` | Grade process quality | `process-docs/PROCESS-QUALITY-GRADE.md` |
| `generate_examples.py` | Generate coherent example | `optimized/steps/PROZESS-BEISPIEL.json` |
| `evaluate_v4.py` | Test–Validate–Improve loop | `process-docs/V4-EVALUATION.md` |

---

## UI

- **Design template:** `shared/design-templates/step-wizard/`
- **HTML:** `optimized/ui/erfindungsbeschreibung.html`
- **Steps:** 7 (0–6)

---

## Key Artifacts

| Artifact | Location | Purpose |
|----------|----------|---------|
| PROCESS-SCAFFOLD | process-docs/ | Step structure |
| USER-PERSONA | process-docs/ | Inventor persona |
| MODULE-AI-BRIEFING | process-docs/ | Concise AI briefing |
| AI-PROCESS-GUIDE | process-docs/ | Detailed AI-executable guide |
| Examples | examples/ | Extracts from TUM, HM, JMU, THI forms |

---

## Relationship to Other Modules

- **erfindung-check:** Assesses novelty before documentation
- **patent-next-steps:** Guides what to do after the invention; Erfindungsbeschreibung prepares the documentation for the TTO form
