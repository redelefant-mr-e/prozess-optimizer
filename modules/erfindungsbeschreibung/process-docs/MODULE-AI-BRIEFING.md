# Erfindungsbeschreibung Module: AI Reuse Briefing

Use this briefing when building or optimizing the Erfindungsbeschreibung module.

---

## Module Goal

**Erfindungsbeschreibung:** Guide inventors through documenting their invention for TTO forms → structured description + practical checklist. Focus: *Du kannst es erklären, aber nicht sauber dokumentieren. Was ist der Kern der Neuerung, welche Details zählen und wie bleibt es verständlich, ohne zu viel preiszugeben?*

---

## Scaffold Pattern

Same as patent-next-steps and erfindung-check:

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

**Target user:** Erfinder:in, die erklären kann, aber nicht dokumentieren
- Has invention; can explain it orally
- Struggles to document for TTO forms
- Unsure: core novelty? which details? understandable without over-disclosure?
- Wants: clear structure, best practices, real examples (TUM, HM, JMU, THI)

---

## Key Concepts (from TUM Guideline + HM/JMU)

- **Technische Aufgabe:** What is the problem? Which field?
- **Stand der Technik:** What exists? What are the disadvantages?
- **Technische Lösung:** What must one do to make it work? (not *why* it works)
- **TUM-Regel:** "Do not describe why something works, but rather what one must do so that it works." Target: "average person skilled in the art"
- **Umfang:** ca. 4 DIN A4 pages; sketches helpful

---

## Example Sources

| Source | Invention | Use Case |
|--------|-----------|----------|
| **HM** | TI-RSS (ADAS testing) | Structure: Technische Aufgabe → Stand der Technik → Behebung → Lösung → Vorteile |
| **JMU** | BNN-Heterozyklen (Prodrugs) | Gebiet der Erfindung, Stand der Technik, technische Lösung |
| **TUM** | Protein LSC | Titel, Erfinder, Entwicklung, Disclosure-Anforderungen |
| **THI** | Cu metallization | Formularfelder, Erfinderdetails |

---

## Design

Reuse `shared/design-templates/step-wizard/` – same CSS, JS, structure as patent-next-steps.
