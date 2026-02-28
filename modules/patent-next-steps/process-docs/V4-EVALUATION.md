# Patent Next Steps V4: Evaluation

## Executive Summary (4–5 Sätze)

Die V4-Version ist ein klarer Fortschritt: „Heute tun“ steht konsequent oben, die Maria-Timeline ist greifbarer, und der Stepper macht den Ablauf deutlich strukturierter. Für die Persona „akademische Erfinder:in ohne Überblick“ ist die Tonalität passend pragmatisch und entlastend. Gleichzeitig ist der Guide an einigen Stellen noch textlastig, wiederholt Kernbotschaften leicht variiert und könnte noch stärker in „Wenn du X bist, tu jetzt Y“-Entscheidungslogik denken. Fachbegriffe sind weitgehend erklärt, aber nicht immer dort, wo sie zum ersten Mal auftauchen, und ein paar kritische Stolpersteine (z.B. „Arbeitnehmererfindung“, „Dienst-/freie Erfindung“) fehlen komplett. Insgesamt: solide Basis, aber noch Luft nach oben bei Fokussierung, Entscheidungsführung und Reduktion.

---

## 1. V4-Verbesserungen: Erreicht?

**„Heute tun“ oben – funktioniert das?**

- Ja, strukturell ist das sauber umgesetzt: In den Schritten 1–5 steht der Aktionsblock ganz oben und ist visuell hervorgehoben (orange Box, „Heute tun“-Label).
- Inhaltlich sind die Aktionen meist konkret genug („Arbeitsvertrag prüfen“, „E-Mail abschicken“, „Leitfragen beantworten“).
- Kritik:  
  - In Schritt 3 („Schutzstrategie wählen“) sind die „Heute tun“-Punkte eher kognitiv („Optionen vergleichen“) als handlungsnah. Für die Persona wäre noch klarer: „Schreibe 3 Stichpunkte zu …“ / „Notiere deine Präferenz A/B“.  
  - In Schritt 5 („Ergebnis“) ist „Leite deine nächste Aktion ab“ relativ abstrakt – hier könnte man stärker in konkrete Fälle („Wenn du Meldepflicht hast und noch nicht gemeldet hast → …“) direkt im Aktionsblock gehen, nicht erst in der Tabelle darunter.

**Redundanz reduziert?**

- Deutlich besser als typische V1/V2-Guides:  
  - „Erst Strategie, dann Veröffentlichung“ taucht zwar mehrfach auf, aber in sinnvoller Dosis (als zentrale Leitregel).
  - „Meldepflicht“ wird im Detail in Schritt 1 erklärt, später eher kurz erinnert.
- Trotzdem noch spürbare Wiederholungen:
  - Die Warnung vor Veröffentlichung (Publication trap) wird in Schritt 2 sehr ausführlich behandelt und dann in Schritt 3 und 5 nochmals sinngemäß wiederholt („erst Strategie klären, dann handeln“). Das ist inhaltlich richtig, aber textlich redundant.
  - „Uni: TTO/Erfindungsberater:in koordiniert, du musst keinen Anwalt suchen“ kommt in Schritt 1, 4 und 5 in sehr ähnlicher Form vor.
- Aus Persona-Sicht: Einmal klar, dann nur noch sehr kurze Reminder („Erinnerung: …“) würden reichen.

**Maria-Timeline mit konkreten Daten?**

- Positiv:
  - Schritt 1: „Tag 0–2“ – sehr konkret, gut.
  - Schritt 2: „Konferenz 15. Juni – Meldung bis 1. Juni“ – klare, greifbare Daten.
  - Schritt 4: „Heute / diese Woche / vor Konferenz (6 Wo.)“ – gute zeitliche Staffelung.
  - Schritt 5: „Termin nächste Woche, Stichpunkte vorbereiten“ – schließt den Bogen.
- Kritik:
  - Die Timeline ist zwar über die Schritte verteilt, aber nicht explizit als „Timeline“ erkennbar. Man muss sich die Stationen selbst zusammensuchen.
  - Es fehlt eine abschließende, kompakte Zusammenfassung von Marias Zeitstrahl im Ergebnis-Schritt (z.B. Mini-Tabelle „Tag 0–2 / Woche 1 / 6 Wochen vor Konferenz“).

**Stepper-UI: Hilfreich? „Du bist hier“ klar?**

- Der horizontale Stepper mit Labels („Einleitung | Standort | Zeitfenster | …“) ist gut lesbar und semantisch klar.
- Die Progress-Anzeige „Schritt X von 6“ plus Stepper ist redundant, aber nicht schädlich – allerdings könnte man sich auf eines fokussieren, um visuelles Rauschen zu reduzieren.
- Potenzielles Problem:
  - In der HTML-Struktur ist „Schritt 0“ die Einleitung, aber im UI steht „Schritt 1 von 6“ – das ist konsistent, aber für Entwickler:innen eine Fehlerquelle. Für Nutzer:innen ist es okay.
  - Der Stepper zeigt „Einleitung“ als ersten Punkt, aber im Content steht „Schritt 0: Einleitung“ (Markdown) vs. „Schritt 1 von 6“ (HTML). Diese Doppelzählung kann verwirren, wenn jemand beide Versionen sieht.

---

## 2. Inhalt & Klarheit

**Fachbegriffe – ausreichend erklärt?**

- Gut:
  - TTO wird direkt in der Einleitung erklärt („Technology Transfer Office – Technologietransferstelle“).
  - „Publication trap“ wird in Schritt 2 verständlich beschrieben, inklusive Beispielen (Preprint, GitHub, Investorengespräch).
  - „Trade Secret“ wird kurz, aber korrekt erklärt.
- Lücken:
  - „Erfindungsberater:in“ wird zwar verwendet, aber nicht explizit erklärt (Rolle, typischer Auftrag, wo sie organisatorisch hängt).
  - Zentrale juristische Begriffe fehlen komplett: „Arbeitnehmererfindung“, „Diensterfindung“ vs. „freie Erfindung“. Für akademische Erfinder:innen in Deutschland ist das ein Kernkonzept.
  - „Prioritätsanmeldung“ wird im Startup-Kontext erwähnt, aber nicht erklärt (was bedeutet Priorität, warum wichtig?).
  - „NDA“ (Non-Disclosure Agreement) wird nur als Abkürzung erwähnt, ohne Erklärung.
- Für die Persona wäre eine Mini-Glossar-Box oder Inline-Erklärung bei erster Nennung hilfreich.

**Wo fehlt Konkretheit?**

- Schritt 1:
  - „Prüfe die Meldepflicht – Arbeitsvertrag, Promotionsordnung oder Intranet“ ist gut, aber es fehlt ein Hinweis, was typische Formulierungen sind („Arbeitnehmererfindungsgesetz“, „Diensterfindung“, „Inanspruchnahme“).
- Schritt 2:
  - Die Empfehlung „Meldung spätestens 2 Wochen vor geplanter Einreichung“ ist praxisnah, aber nicht begründet. Ein Satz „damit TTO/Patentstelle noch reagieren kann“ würde das verankern.
- Schritt 3:
  - „Marktpotenzial niedrig/mittel/hoch“ ist sehr vage. Ein Beispiel („niedrig = nur Nischenanwendung im eigenen Labor; hoch = potenziell viele Kliniken/Unternehmen als Nutzer“) würde helfen.
  - „Erfindung-Check hilft“ – hier fehlt ein Link oder zumindest ein klarer Verweis, was das ist (anderer Guide? internes Tool?).
- Schritt 5:
  - Kostenrahmen 3.000–8.000 € ist gut, aber ohne Kontext („für eine erste nationale Anmeldung, ohne internationale Phase“) kann das missverstanden werden.

**Länge – zu knapp oder gut?**

- Für eine Persona, die „kompakt, praxisnah, nicht überfordernd“ erwartet, ist der Guide an der oberen Grenze der akzeptablen Länge.
- Positiv:
  - Jeder Schritt ist klar strukturiert (Action, Info, Beispiel, Kontext, Tipp).
  - Sätze sind überwiegend kurz und verständlich.
- Kritik:
  - Die Summe aller Blöcke pro Schritt ist hoch – besonders Schritt 1 und 2 wirken textschwer.
  - Manche Tabellen sind sehr dicht; für mobile Nutzung könnte das anstrengend werden.
  - Es gibt kaum explizite „Optional lesen“-Signale; alles wirkt gleich wichtig.

---

## 3. UI & Nutzererfahrung

**Wizard-Navigation, Blöcke, Informationsdichte**

- Navigation:
  - Vor/Zurück-Buttons sind klar, Stepper zeigt Position – das reduziert Unsicherheit („Wo bin ich?“).
- Blockstruktur:
  - Die Blocktypen (Action, Info, Example, Context, Tipp) sind visuell differenziert – gut für Scannen.
  - „Heute tun“ ist als Action-Block klar hervorgehoben.
- Informationsdichte:
  - Für eine akademische Zielgruppe ist die Dichte grundsätzlich okay, aber:
    - Es fehlen „Fokus-Hinweise“: Was ist absolut kritisch, was nice-to-know?
    - Die E-Mail-Vorlage in Schritt 1 ist hilfreich, aber nimmt viel Platz ein – könnte als „aufklappbar“ oder sekundär markiert werden.

**Stepper verständlich?**

- Ja, die Labels sind selbsterklärend („Zeitfenster“, „Strategie“, „Prioritäten“, „Ergebnis“).
- Potenziell irritierend:
  - Die Einleitung wird im Markdown als „Schritt 0“ bezeichnet, im UI als „Schritt 1 von 6“. Das ist inkonsistent, wenn jemand beide Versionen sieht.
  - Der Stepper selbst zeigt keine „done/active“-Zustände im HTML-Snippet (nur CSS-Klassen vorbereitet). Wenn das im finalen Produkt nicht dynamisch gesetzt wird, verliert der Stepper seine „Du bist hier“-Funktion.

**Gibt es Lücken oder Verwirrung?**

- Übergänge:
  - Die Übergänge zwischen den Schritten sind logisch, aber nicht immer explizit:  
    - Beispiel: Am Ende von Schritt 2 könnte klarer stehen: „Wenn du eine Deadline < 4 Wochen hast, ist Schritt 2 dein wichtigster Schritt – geh jetzt direkt zu Schritt 1 (Meldung) zurück, falls noch nicht geschehen.“
- Persona-spezifische Verwirrung:
  - Doktorand:innen mit Stipendium (nicht angestellt) sind ein typischer Sonderfall – sie tauchen nicht explizit auf. Viele wissen nicht, ob sie Meldepflicht haben.
  - Internationale Kontexte (nicht-deutsche Unis) werden nicht adressiert – das ist okay, aber dann sollte das explizit als „deutschlandzentriert“ markiert werden.

---

## 4. Lücken & Schwachstellen

1. **Rechtlicher Rahmen zu Arbeitnehmererfindungen fehlt komplett**  
   Für akademische Erfinder:innen in Deutschland ist das zentral. Ohne wenigstens eine grobe Erklärung („Diensterfindung vs. freie Erfindung“) bleibt ein blinder Fleck.

2. **Keine klare Entscheidungslogik („Wenn … dann …“) über alle Schritte hinweg**  
   Der Guide gibt viel Kontext, aber wenig explizite Pfade:  
   - „Wenn du in einer Uni mit Meldepflicht bist UND eine Konferenzdeadline in 3 Wochen hast, dann …“  
   - Das wäre für die Persona enorm entlastend.

3. **Erfindung-Check wird erwähnt, aber nicht verankert**  
   Es ist unklar, ob der Nutzer den schon gemacht hat, ob er jetzt dahin springen soll, oder ob das nur „nice to know“ ist.

4. **Startup-Kontext bleibt oberflächlich**  
   - Es wird zwar gesagt „du organisierst selbst, Kostenrahmen X“, aber typische Stolpersteine fehlen:  
     - Vertraulichkeit mit potenziellen Kunden/Investoren  
     - Umgang mit Open-Source-Komponenten im Patentkontext (gerade bei Software relevant).

5. **Keine explizite „Don’t do“-Liste**  
   - Es gibt verstreut Warnungen (Publication trap, nicht eigenmächtig Anwalt beauftragen), aber keine kompakte Übersicht „3 Dinge, die du auf keinen Fall tun solltest“.

---

## 5. Top 5 Verbesserungsvorschläge

1. **Entscheidungslogik explizit machen (höchste Priorität)**  
   - Ergänze in Schritt 5 (Ergebnis) eine klare „Wenn … dann …“-Matrix, z.B.:
     - „Wenn du an einer Uni mit Meldepflicht bist UND noch nicht gemeldet hast → Nächste Aktion: E-Mail an Erfindungsberater:in heute.“
     - „Wenn du in 2–4 Wochen eine Konferenzdeadline hast → Nächste Aktion: Meldung innerhalb von 1–3 Tagen, Erstgespräch innerhalb von 1 Woche.“
   - Teile diese Logik ggf. schon in Schritt 1/2 an, damit Nutzer:innen nicht bis zum Ende warten müssen.

2. **Rechtliche Grundbegriffe ergänzen (kompakt, nicht juristisch)**  
   - Füge eine kleine Box (z.B. in Schritt 1) ein:
     - „Diensterfindung vs. freie Erfindung (Deutschland) – was heißt das grob?“
     - „Arbeitnehmererfindungsgesetz – warum du melden musst.“
   - Erkläre kurz „Prioritätsanmeldung“ im Startup-Kontext.

3. **Redundanz weiter reduzieren und „Must read“ vs. „Optional“ markieren**  
   - Markiere z.B.:
     - „Kritisch“ (muss gelesen werden): Publication trap, Meldepflicht, Reihenfolge Meldung → Beratung → Strategie → Anmeldung.
     - „Optional“: detaillierte Tabellen, E-Mail-Vorlage, Kontextblöcke.
   - Kürze Wiederholungen von „Uni: TTO koordiniert, du musst keinen Anwalt suchen“ auf 1–2 Stellen + kurze Reminder.

4. **Maria-Timeline als durchgängige, sichtbare Storyline aufbereiten**  
   - Am Ende (Schritt 5) eine kompakte Timeline-Box:
     - Tag 0–2: E-Mail an TTO  
     - Woche 1: Erstgespräch  
     - 6 Wochen vor Konferenz: Strategie fix  
     - Vor Konferenz: ggf. Anmeldung abgeschlossen  
   - Verlinke aus den früheren Maria-Abschnitten auf diese Übersicht („siehe Timeline im Ergebnis“).

5. **Startup-/Solo-Sektion leicht vertiefen**  
   - Ergänze in Schritt 2/3:
     - Hinweis zu NDAs („Vor Gesprächen mit Unternehmen/Investoren ohne NDA kann eine Veröffentlichung vorliegen – kurz mit Anwalt/TTO klären“).
   - In Schritt 5:
     - Ein Mini-Entscheidungsbaum: „Budget < X → Prioritätsanmeldung + spätere Entscheidung; Budget > X → direkt mit Anwalt über internationale Strategie sprechen.“

---

## 6. Was bereits gut funktioniert

- **„Aktion oben, Kontext unten“ ist konsequent und hilfreich**  
  Die Nutzer:in sieht sofort, was heute zu tun ist, ohne sich erst durch Theorie zu kämpfen.
- **Tonalität ist pragmatisch, nicht einschüchternd**  
  Direkte „du“-Ansprache, klare Sprache, wenig Juristendeutsch – das passt sehr gut zur Persona.
- **Beispiele und Tabellen machen abstrakte Risiken greifbar**  
  Besonders die Publication-trap-Tabelle und Marias Konferenzbeispiel sind didaktisch stark.
- **Rollenklärung Uni/Firma/Startup ist verständlich**  
  Die Tabelle in Schritt 1 gibt schnell Orientierung, wer typischerweise zuständig ist.
- **UI-Grundstruktur (Stepper, Blöcke, Buttons) ist klar und konsistent**  
  Man weiß, wo man ist und wie man weiterkommt; die Blocktypen unterstützen das Scannen.

---

## 7. Quick Wins

1. **Begriffsklärungen direkt an erster Stelle einfügen**  
   - Bei erster Nennung von „Erfindungsberater:in“, „NDA“, „Prioritätsanmeldung“ jeweils 1 erklärender Halbsatz ergänzen.

2. **Ein Satz zu „Erfindung-Check“ ergänzen**  
   - In Schritt 3: „Erfindung-Check = separater Guide/Tool, mit dem du grob prüfst, ob es schon ähnliche Patente gibt (Link).“

3. **Doppelte Hinweise zu TTO/Patentanwalt straffen**  
   - In Schritt 4/5 jeweils nur noch 1 Satz als Reminder („Erinnerung: An der Uni organisiert das TTO den Patentanwalt“).

4. **„Heute tun“ in Schritt 3 und 5 schärfen**  
   - Schritt 3: „Schreibe 3 Stichpunkte zu Marktpotenzial / Publikation vs. Schutz / Nachbaubarkeit auf.“  
   - Schritt 5: „Wähle in der Tabelle deine Situation aus und schreibe dir genau 1 nächste Aktion mit Datum auf.“

5. **Maria-Timeline im Ergebnis-Schritt kurz zusammenfassen**  
   - Eine kleine Box „Marias Weg in 4 Schritten“ – das verankert die Story und hilft Nutzer:innen, sich selbst einzuordnen.

Diese Anpassungen sind mit wenig Aufwand umsetzbar, erhöhen aber die Klarheit und Handlungsorientierung für die akademische Persona deutlich.