# Erfindung-Check: AI Briefing (No Prior Context Required)

## What This Is
An 8-step process to check if an idea is novel and how it differs from existing solutions. Output: **Neu wirkt plausibel** | **Unklar** | **Eher bekannt** + concrete next action.

## Core Concepts
- **Erfindung:** New, concrete solution to a problem that others could replicate.
- **Kernprinzip:** The mechanism/structure that defines the invention.
- **Prior Art:** Existing products, patents, publications that may overlap.

---

## The 8 Steps

| Step | Do This | Output |
|------|---------|--------|
| **0** | Explain what an invention is and why this check matters | User ready to proceed |
| **1** | Ask user to pick category: **Produkt/Mechanik** \| **Material/Verfahren** \| **Software** \| **Medizin** | Category + search strategy |
| **2** | Broad search (DE+EN): function + object + context. Use *alternative*, *mechanism*, *device*, *prototype*. Sources: websites, YouTube, forums | 5–10 similar solutions + keyword list |
| **3** | Patent search (Espacenet, Google Patents) with 2–4 keyword combos. Filter: images → abstract → claims | Patent table (Titel, Jahr, Link, Relevanz) |
| **4** | Publication search (Google Scholar, PubMed, Lens, Semantic Scholar) with same keywords + *paper*, *method*, *prototype* | Publication table |
| **5** | Merge hits. Classify each: **Gleiche Funktion, anderer Mechanismus** \| **Ähnlicher Mechanismus, anderer Zweck** \| **Gleiche Funktion + Mechanismus** (critical) | Evaluation table (Gleich/Anders pro Treffer) |
| **6** | Formulate Kernidee: *"Neu ist, dass [Mechanismus] so ausgeführt ist, dass [Wirkung] unter [Bedingung] entsteht."* Add 2–3 variants. Derive 3–5 keywords each for Mechanismus, Wirkung, Kontext. Quick final search | Kernidee sentence + variants + keywords |
| **7** | Choose status → next action | Status + next step |

---

## Status → Next Action
- **Neu wirkt plausibel:** Dokumentieren, vertraulich halten, Schutzstrategie prüfen
- **Unklar:** Kernidee schärfen, zweite Suchrunde mit besseren Keywords
- **Eher bekannt:** Pivot prüfen (anderer Mechanismus, Use-Case, Kombination)

## Category-Specific Sources
- **Mechanik:** Produktseiten, Patentskizzen, "mechanism"
- **Verfahren:** Papers, "method", "process", "composition"
- **Software:** GitHub, Papers, "workflow", "pipeline"
- **Medizin:** PubMed, "diagnostic", "assay", "clinical"

## Kernidee Quality
Avoid vague terms ("besser", "effizienter"). Focus on: *what is concretely different in structure, arrangement, or execution?*
