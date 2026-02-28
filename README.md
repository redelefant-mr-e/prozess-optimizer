# Process Optimizer

A modular app for creating, optimizing, and running structured step-by-step processes. Each module follows a consistent pattern: source process, scaffold, persona, AI-driven optimization, and interactive UI.

---

## Structure

```
Process-Optimizer/
├── modules/           # Process modules
│   ├── erfindung-check/
│   └── patent-next-steps/
├── shared/            # Reusable assets
│   └── design-templates/
│       └── step-wizard/
├── archive/           # Older versions and scripts
└── .env               # API keys (OpenAI)
```

---

## Modules

### erfindung-check

Invention novelty assessment: 8-step process to check if an idea is new and how it differs from existing solutions.

- **UI:** [modules/erfindung-check/optimized/ui/erfindung-check.html](modules/erfindung-check/optimized/ui/erfindung-check.html) – open in browser
- **Docs:** [MODULE-DESCRIPTION.md](modules/erfindung-check/MODULE-DESCRIPTION.md), [MODULE-AI-BRIEFING.md](modules/erfindung-check/MODULE-AI-BRIEFING.md)
- **Scripts:** `analyze_process`, `optimize_process`, `grade_process`, `generate_examples` (in `modules/erfindung-check/scripts/`)

### patent-next-steps

Patent process guidance: 6-step process for inventors (especially academic) – what to do next, whom to involve when, what to clarify early. Natural follow-up to erfindung-check.

- **UI V1:** [modules/patent-next-steps/optimized/ui/patent-next-steps.html](modules/patent-next-steps/optimized/ui/patent-next-steps.html)
- **UI V2:** [modules/patent-next-steps/optimized/ui/patent-next-steps-V2.html](modules/patent-next-steps/optimized/ui/patent-next-steps-V2.html) – with Erfindungsberater:in, durchgängigem Beispiel (Maria), Mikro-Walkthroughs, E-Mail-Vorlage
- **Docs:** [MODULE-DESCRIPTION.md](modules/patent-next-steps/MODULE-DESCRIPTION.md), [MODULE-AI-BRIEFING.md](modules/patent-next-steps/MODULE-AI-BRIEFING.md)
- **Scripts:** `analyze_process`, `optimize_process`, `grade_process`, `generate_examples` (in `modules/patent-next-steps/scripts/`)

### erfindungsbeschreibung

Invention documentation guide: 7-step process for inventors – how to document an invention for TTO forms. Focus: What is the core novelty? Which details matter? How to keep it understandable without revealing too much? Uses real examples from TUM, HM, JMU, THI.

- **UI:** [modules/erfindungsbeschreibung/optimized/ui/erfindungsbeschreibung.html](modules/erfindungsbeschreibung/optimized/ui/erfindungsbeschreibung.html)
- **Docs:** [MODULE-DESCRIPTION.md](modules/erfindungsbeschreibung/MODULE-DESCRIPTION.md), [process-docs/MODULE-AI-BRIEFING.md](modules/erfindungsbeschreibung/process-docs/MODULE-AI-BRIEFING.md)
- **Scripts:** `analyze_process`, `optimize_process`, `grade_process`, `generate_examples`, `evaluate_v4` (in `modules/erfindungsbeschreibung/scripts/`)

---

## Shared Assets

- **step-wizard:** Reusable CSS/JS for step-by-step UIs. Used by erfindung-check, patent-next-steps, and available for new modules.

---

## Quick Start

1. Add `OPENAI_API_KEY` to `.env`
2. Run scripts from module directory, e.g.:
   ```bash
   python modules/erfindung-check/scripts/analyze_process.py
   python modules/erfindung-check/scripts/grade_process.py
   ```
3. Open a UI:
   - Erfindung-Check: `modules/erfindung-check/optimized/ui/erfindung-check.html`
   - Patent Next Steps: `modules/patent-next-steps/optimized/ui/patent-next-steps.html`
   - Erfindungsbeschreibung: `modules/erfindungsbeschreibung/optimized/ui/erfindungsbeschreibung.html`

---

## Adding a New Module

See [modules/erfindung-check/MODULE-AI-BRIEFING.md](modules/erfindung-check/MODULE-AI-BRIEFING.md) for the replication pattern.
