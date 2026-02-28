# Patent Next Steps V4: Improvement Plan

**Constraint:** Guide is interactive (wizard navigation), but users do **not** build to-dos or forms with it. No fillable fields, no user-generated checklists. Content is informational only.

---

## 1. Content & Structure

### 1.1 "Aktion oben, Kontext unten"
- Each step (1–5) starts with a **Heute tun** block: 1–3 concrete actions, max 2–3 lines
- Informational only – tells user what to do, does not collect input
- Example: "1. Ordne dich einem Kontext zu. 2. Prüfe Meldepflicht. 3. Finde Ansprechpartner:in."

### 1.2 Text streamlining (~30%)
- Cut redundancy: "Meldepflicht + Erfindungsberater:in" explained once (Step 1), then 1-line reminders
- "Erst Strategie, dann Veröffentlichung" – once in Step 2, brief reminder later
- "Uni: TTO koordiniert" – once, then kurz erinnern
- Shorten Step 0 intro to 2 paragraphs max
- Remove filler phrases, keep sentences short

### 1.3 Maria timeline (concrete dates)
- Step 1: "Tag 0–2: Maria schreibt E-Mail an TTO"
- Step 2: "Konferenz 15. Juni → Meldung bis 1. Juni"
- Step 3: "Vor dem Gespräch: 4 Leitfragen beantwortet"
- Step 4: "Maria: E-Mail heute, Termin nächste Woche, Strategie bis 6 Wo. vor Konferenz"
- Step 5: "Termin nächste Woche, Stichpunkte vorbereiten"

### 1.4 Concreteness (without forms)
- Step 1: Add hint: "Formular oft im Intranet unter ‚Erfindungsmeldung' oder ‚Invention Disclosure'"
- Step 2: "Konferenz 15. Mai → Meldung bis 1. Mai" as example (informational)
- Step 3: Leitfragen as clear bullet list (informational)
- Step 4: "Typische Reihenfolge" + Maria-Beispiel – no "erstelle deine Liste"
- Step 5: "Konkrete nächste Schritte für Startup" as example text (no form)

### 1.5 Reframe Step 4
- Remove "Erstelle deine To-do-Liste" / "Übertrage in deinen Kalender"
- Replace with: "Typische Reihenfolge" + "So geht Maria vor" (Beispiel-Timeline)
- User reads and applies mentally – no building required

### 1.6 Legal clarifications
- Konferenz-Submission: "Kann als Veröffentlichung gelten, je nach Prozess. Unbedingt vorher klären."
- Startup: "Meldepflicht: Nein – wenn keine anderen Verträge (Werkvertrag, Nebenbeschäftigung). Prüfe trotzdem."

---

## 2. UI & Interaction

### 2.1 Stepper ("Du bist hier")
- Add horizontal stepper above main content: Einleitung | Standort | Zeitfenster | Strategie | Prioritäten | Ergebnis
- Current step highlighted

### 2.2 Step numbering
- Display: "Schritt 1 von 6" (Einleitung) … "Schritt 6 von 6" (Ergebnis)
- No confusion between data-step 0 and "Schritt 1"

### 2.3 Block consolidation
- Reduce blocks per step where possible
- Merge related Info-blocks
- Keep: Ziel, Heute tun, Hauptinfo, Beispiel, Kontext, Tipp

### 2.4 Hierarchy
- "Heute tun" always first (after Ziel)
- "Mehr dazu" / optional details collapsible or visually secondary (optional)

---

## 3. Out of Scope (V4)

- No fillable forms
- No user-built to-do lists
- No user input collection
- No interactive checklists

---

## 4. File Structure

- `refined-V4/00-Einleitung.md` … `05-Ergebnis.md`
- `patent-next-steps-V4.html` with stepper UI
