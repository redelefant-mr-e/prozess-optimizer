# Patent Next Steps Module: Detailed Description

## Purpose

The Patent Next Steps module guides inventors (especially with academic background) through the essential steps of the patenting process after they have an invention or prototype. It answers: What to do next? Whom to involve when? What to clarify early? Output: **clear next action** + **decision checklist** tailored to context (Uni, Firma, Startup).

---

## Process Flow

The process guides users through six steps (optimized from seven; steps 1 and 2 were combined):

| Step | Name | Purpose | Output |
|------|------|---------|--------|
| 0 | Einleitung | Overview; three scenarios (Uni, Firma, Startup); no legal advice | User ready |
| 1 | Standort und Ansprechpartner:innen | Context, Meldepflicht, first contacts | Kontext + Meldepflicht + Kontaktliste |
| 2 | Zeitfenster beachten | Publication trap; deadlines; checklist | Checklist before publication |
| 3 | Schutzstrategie wählen | Patent vs. publication vs. trade secret | Rough strategy |
| 4 | Prioritäten setzen | What first? Sequence of steps | Prioritized to-do list |
| 5 | Ergebnis | Next action; when to involve patent attorney | Next action + decision |

---

## Optimization Pipeline

Same as erfindung-check:

1. **Grade** – `grade_process.py` → `PROCESS-QUALITY-GRADE.md`
2. **Optimize** – `optimize_process.py` (Phase 1 + Phase 2) → `optimized/refined/`, `optimized/draft/`
3. **Analyze** – `analyze_process.py` → `AI-PROCESS-GUIDE.md`
4. **Generate examples** – `generate_examples.py` → `PROZESS-BEISPIEL.json`

---

## Scripts and Roles

| Script | Role | Output |
|--------|------|--------|
| `analyze_process.py` | Create AI-executable guide | `process-docs/AI-PROCESS-GUIDE.md` |
| `optimize_process.py` | Phase 1 + Phase 2 optimization | `optimized/refined/`, `optimized/draft/` |
| `grade_process.py` | Grade process quality | `process-docs/PROCESS-QUALITY-GRADE.md` |
| `generate_examples.py` | Generate coherent example | `optimized/steps/PROZESS-BEISPIEL.json` |

---

## UI

- **Design template:** `shared/design-templates/step-wizard/`
- **HTML:** `optimized/ui/patent-next-steps.html`
- **Steps:** 6 (0–5)

---

## Key Artifacts

| Artifact | Location | Purpose |
|----------|----------|---------|
| PROCESS-SCAFFOLD | process-docs/ | Step structure |
| USER-PERSONA | process-docs/ | Academic inventor persona |
| AI-BRIEFING | process-docs/ | Concise AI briefing |
| AI-PROCESS-GUIDE | process-docs/ | Detailed AI-executable guide |

---

## Relationship to erfindung-check

The erfindung-check step 6 "So geht's weiter" links to this module as a natural follow-up: after assessing novelty, inventors need guidance on the patenting process.
