# Patent Next Steps Module: AI Reuse Briefing

Use this briefing when building another module that should follow the same logic and structure.

---

## Module Goal

**Patent Next Steps:** Guide inventors through essential patenting process steps → clear next action + decision checklist tailored to context (Uni, Firma, Startup).

---

## Scaffold Pattern

Same as erfindung-check:

| Element | Purpose |
|--------|---------|
| **Titel** | `# Schritt N: [Name]` |
| **Ziel** | One-line success criterion |
| **So gehst du vor** | Numbered sub-steps |
| **Tipp** | Typical pitfalls + solution |
| **Fazit** | Output checklist |
| **Nächster Schritt** | Link (or "So geht's weiter" at end) |

---

## Persona

**Target user:** Erfinder:in mit akademischem Hintergrund
- Has invention or prototype
- Little overview of patent process, Meldepflicht, contacts
- Wants orientation: what steps? whom when? what to clarify early?
- Expects: compact, practical – not too detailed, not boring

---

## Context-Specific Logic

| Context | Meldepflicht | First contact |
|---------|--------------|---------------|
| **Uni/Forschungsinstitut** | Yes (typically) | TTO, Erfindungsmeldestelle |
| **Firma mit F&E** | Often yes | Patentstelle, Vorgesetzte |
| **Startup/Solo** | No | Patentanwalt, IHK |

---

## Key Concepts

- **Meldepflicht:** Obligation to report inventions to employer
- **Publication trap:** Publishing before patent application destroys patent rights
- **TTO:** Technology Transfer Office
- **Schutzstrategie:** Patent vs. publication vs. trade secret vs. combination

---

## Design

Reuse `shared/design-templates/step-wizard/` – same CSS, JS, structure as erfindung-check.
