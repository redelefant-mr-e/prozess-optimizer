# Patent Next Steps V3: Evaluation

## Executive Summary (4–5 Sätze)

V3 liest sich deutlich flüssiger als eine Bullet-Point-Sammlung, ist aber an mehreren Stellen zu wortreich und wiederholt sich, sodass die Orientierung leidet. Inhaltlich deckt der Guide die Kernfragen der Persona gut ab (Meldepflicht, Publication trap, grobe Strategie), bleibt aber bei konkreten „Was klicke / schreibe / tue ich jetzt genau?“ noch zu abstrakt. Die Wizard-Struktur mit 6 Schritten ist grundsätzlich passend, wird aber durch lange Textblöcke, Tabellen und Wiederholungen ausgebremst. Für die Persona wäre eine stärkere Verdichtung in klaren Checklisten, Entscheidungsregeln und Mini-Formularen nötig. Empfehlung: Text radikal straffen, pro Schritt eine sichtbare „Aktion oben, Kontext unten“-Struktur einführen und das Maria-Beispiel gezielter als roter Faden nutzen.

---

## 1. Inhalt & Ton

**Was funktioniert:**

- Ton ist grundsätzlich passend: direkt, „du“, wenig Juristendeutsch, erklärt Begriffe (Publication trap, Trade Secret) ohne abzuschweifen.
- Die Struktur „Ziel → Info → Beispiel → Tipp/Kontext“ ist inhaltlich sinnvoll und entspricht den Bedürfnissen der Persona.
- Maria als Beispiel ist gut gewählt (Postdoc, Software-Algorithmus, Uni-Kontext) und spiegelt die Kernpersona.

**Kritische Punkte:**

1. **Zu viel Prosa, zu wenig „Handgriff“**

   - Viele Abschnitte sind unnötig ausgeschmückt und wiederholen die gleiche Aussage in anderen Worten.
     - Beispiel Schritt 0:  
       - Absatz 1 („Du hast eine Idee…“) + Absatz 2 („Dieser Guide nimmt dich Schritt für Schritt…“) + Absatz 3 („Auf dieser Basis schaust du dir…“) + Absatz 4 („Am Ende dieses Einstiegs…“) sagen im Kern: „Wir klären Kontext, Zeitfenster, Strategie, Prioritäten, du bekommst eine Checkliste.“ Das könnte in 2 kurzen Absätzen stehen.
   - Die Persona will: „Was mache ich heute Nachmittag konkret?“ – das geht in der Prosa teilweise unter.

2. **Redundanz über Schritte hinweg**

   - „Meldepflicht + Erfindungsberater:in/TTO“ wird in Schritt 0, 1, 2, 3, 4 und 5 jeweils wieder erklärt, oft mit sehr ähnlichen Formulierungen.
   - „Erst Strategie klären, dann veröffentlichen“ wird in Schritt 2, 3 und 4 mehrfach variiert.
   - „Du musst keinen Patentanwalt selbst suchen (Uni/Firma)“ steht in Schritt 1, 3, 4 und 5.
   → Das wirkt belehrend und verlängert den Text unnötig. Einmal klar, dann nur noch in 1 Zeile erinnern.

3. **Konkretheit fehlt an den entscheidenden Stellen**

   - Schritt 1:
     - Gute E-Mail-Vorlage, aber kein **konkreter Hinweis**, wo typischerweise das Formular liegt (z.B. „Suche im Intranet nach ‚Erfindungsmeldung PDF‘“ / „Oft heißt das Formular ‚Erfindungsmeldung‘ oder ‚Invention Disclosure‘“).
     - Kein Mini-Formular im Text, das die 3–5 wichtigsten Felder einer Erfindungsmeldung andeutet (Titel, Kurzbeschreibung, Beteiligte, Kontext).
   - Schritt 2:
     - Checkliste ist gut, aber sehr allgemein. Es fehlt ein **konkretes Beispiel mit Datum** („Konferenzdeadline 15. Mai → Erfindungsmeldung bis 1. Mai abschicken“).
   - Schritt 3:
     - Leitfragen sind textlich beschrieben, aber nicht als **klare Liste** zum Ausfüllen („Bewerte Marktpotenzial: niedrig/mittel/hoch“, „Publikation vs. Schutz: was ist dir wichtiger?“).
   - Schritt 4:
     - „Erstelle deine To-do-Liste“ bleibt abstrakt. Eine **ausfüllbare 3-Zeilen-Tabelle** wäre deutlich hilfreicher.
   - Schritt 5:
     - Kostenrahmen (3.000–8.000 €) ist gut, aber es fehlen **konkrete nächste Schritte** für Startup („2 Kanzleien anrufen, 1 Erstberatung buchen, Fragenliste vorbereiten“).

4. **Prosa beeinträchtigt Klarheit**

   - Viele Sätze sind unnötig lang und verschachtelt, z.B.:
     - „Gerade im Projekt- oder Forschungskontext kann das darüber entscheiden, ob aus deiner Idee später wirklich etwas wird – oder ob du Chancen verschenkst, ohne es zu merken.“
     - „In diesem Termin klärt ihr, ob eine Patentanmeldung geplant ist und, falls ja, wie ihr das zeitlich vor der Paper-Einreichung organisiert.“
   - Das erhöht die kognitive Last. Die Persona ist fachlich fit, aber nicht im Patentrecht – sie braucht **kurze, klare Sätze**.

5. **Maria-Beispiel: inkonsistent genutzt**

   - In Schritt 1 und 2 ist Maria konkret und hilfreich. In Schritt 3–5 wird sie eher summarisch erwähnt.
   - Es fehlen **Mini-Snippets**, die Maria parallel zur Persona durch den Wizard führen:
     - z.B. in Schritt 2: „Marias Konferenzdeadline: 15. Juni. Sie setzt sich die interne Deadline 1. Juni für die Erfindungsmeldung.“
     - in Schritt 4: „Ihre To-do-Liste im Kalender: heute 30 Min für E-Mail, nächste Woche Termin, bis Datum X Strategieentscheidung.“

---

## 2. UI & Nutzererfahrung

**Wizard-Navigation (6 Schritte):**

- Grundstruktur (Schritt 0–5) ist logisch.
- Fortschrittsanzeige („Schritt 1 von 6“) ist vorhanden – gut.
- Problem: In HTML ist Schritt 0 als `data-step="0"` markiert, aber die Progress-Textanzeige startet mit „Schritt 1 von 6“. Das kann verwirren:
  - Nutzer ist inhaltlich in der Einleitung (Schritt 0), UI sagt „Schritt 1 von 6“.

**Blöcke (Ziel, Info, Beispiel, Tipp, Kontext):**

- Visuelle Trennung (unterschiedliche Hintergründe, Block-Labels) ist sinnvoll.
- Aber: In vielen Schritten stehen **zu viele Blöcke hintereinander**, alle ähnlich gewichtet:
  - Schritt 1: Action (Ziel), Info (Kontext), Info (Meldepflicht), Info (Ansprechpartner), Info (E-Mail), Beispiel, Kontext, Tipp → 8 Blöcke.
  - Für die Persona wirkt das wie ein langer Scroll-Artikel, nicht wie ein „Wizard-Schritt“.

**Informationsdichte pro Schritt:**

- Schritt 0 und 1 sind sehr voll; Schritt 3–5 sind etwas schlanker, aber immer noch textlastig.
- Tabellen + Fließtext + Beispiel in einem Schritt erzeugen Scroll-Strecken, bei denen der „Call to Action“ (Was soll ich tun?) nach oben wegrutscht.
- Die Persona könnte nach der Hälfte des Schritts vergessen haben, was das Ziel war.

**Scroll-Probleme / Tabellen:**

- Tabellen sind sinnvoll, aber:
  - In Schritt 2 zwei Tabellen hintereinander (Publication trap + akademische Situationen) → Scroll + kognitive Last.
  - Auf kleinen Screens (Laptop, Tablet) wird das schnell unübersichtlich, trotz `overflow-x:auto`.
- Es fehlt eine **klare visuelle Hierarchie**: Was ist „Muss ich lesen“, was ist „Kann ich bei Bedarf lesen“?

**Visuelle Hinweise:**

- Fortschrittsbalken vorhanden, aber:
  - Kein „Du bist hier“-Marker in der Step-Navigation (z.B. Stepper mit allen Schritten, aktueller hervorgehoben).
  - Kein „Aktion zuerst“-Pattern (z.B. oben ein kurzer „Mach jetzt X“, darunter „Warum“).
- Block-Labels („Ziel“, „Beispiel“, „Tipp“) sind gut, aber nicht konsequent genutzt:
  - In manchen Blöcken fehlt das Label (z.B. viele Info-Blöcke ohne Label).
  - „Kontext“ und „Info“ verschwimmen.

---

## 3. Persona-Tauglichkeit

**Würde die Persona nach dem Durchlauf wissen, was sie als Nächstes tun soll?**

- Ja, grob. Sie versteht:
  - Meldepflicht prüfen → melden.
  - Publication trap vermeiden → vor Veröffentlichung klären.
  - Strategie grob überlegen → mit TTO/Patentstelle besprechen.
- Aber: Die **konkrete erste Aktion** ist oft in der Mitte des Textes versteckt, nicht oben:
  - Besser wäre: Jeder Schritt beginnt mit „Heute: Mach X (15–30 Minuten)“.

**„Spezifisch für deinen Kontext“-Blöcke:**

- Inhaltlich sinnvoll, aber:
  - Wiederholen oft bereits Gesagtes („Uni: TTO/Erfindungsberater:in koordiniert“, „Firma: nicht eigenmächtig Anwalt beauftragen“, „Startup: du organisierst selbst“).
  - Sie sind eher generische Hinweise als echte **Entscheidungsregeln**.
- Für die Persona wäre hilfreicher:
  - 1–2 **konkrete Unterschiede** pro Kontext („Uni: Formular A, Firma: Formular B, Startup: kein Formular, aber…“).
  - Evtl. ein Mini-Switch: „Ich bin an einer Uni / Firma / Startup → zeig mir nur die relevanten Punkte“.

**Maria-Beispiel:**

- Anfangs gut, später zu oberflächlich.
- Es fehlt eine **durchgehende Timeline**:
  - Wann genau meldet sie?
  - Welche E-Mail schreibt sie?
  - Welche 3 Punkte notiert sie für das Gespräch?
- Aktuell ist Maria eher „Illustration“ als „Guided Walkthrough“.

**Unsicherheit / Überforderung:**

- Mögliche Überforderungspunkte:
  - Schritt 2: Zwei Tabellen + viel Text → Gefahr, dass Nutzer:in die Unterschiede zwischen „öffentlich“, „kompliziert“, „meist nein“ nicht wirklich versteht, sondern nur „alles ist gefährlich“ mitnimmt.
  - Schritt 3: Patent vs. Publikation vs. Trade Secret – für jemanden ohne Vorwissen ist das viel auf einmal, ohne klare „Wenn A, dann B“-Regel.
  - Schritt 5: Kostenrahmen 3.000–8.000 € kann abschrecken, ohne dass klar ist, welche Fördermöglichkeiten oder Uni-Kostenübernahme existieren (für Startups: evtl. EXIST, WIPANO etc. – zumindest andeuten).

---

## 4. Lücken & Schwachstellen

**Was fehlt komplett / ist zu dünn:**

1. **Rolle der Erfindungsberater:in / TTO konkret**
   - Es wird gesagt, dass sie „koordinieren“ und „unterstützen“, aber:
     - Was machen sie konkret im Gespräch?
     - Welche Unterlagen sollte die Persona mitbringen?
     - Wie lange dauert typischerweise der Prozess von Meldung bis Entscheidung?

2. **Formulare / typische Felder**
   - Kein Beispiel einer Erfindungsmeldung (auch nur schematisch).
   - Kein Hinweis auf typische Pflichtangaben (Miterfinder:innen, Drittmittelprojekte, Fördergeber).

3. **Links / Ressourcen (auch generisch)**
   - Keine Links zu:
     - Informationsseiten zu Arbeitnehmererfindungsgesetz (DE).
     - Typischen TTO-Seiten (z.B. „Suche nach ‚Technologietransfer‘ + Name deiner Uni“).
   - Selbst wenn keine institutionenspezifischen Links möglich sind, könnte man generische Suchanweisungen geben.

4. **Stolpersteine, die nicht adressiert werden:**

   - **Miterfinder:innen**: Wer gehört auf die Meldung? Was, wenn man sich nicht einig ist?
   - **Drittmittel / Kooperationspartner**: Was, wenn Industriepartner oder andere Unis beteiligt sind?
   - **Software-spezifische Themen** (Maria ist Software-Use-Case):
     - Kurz: „Achtung: Reines Copyright vs. Patent auf Verfahren – was ist realistisch?“ (ohne tief zu gehen).
   - **Zeitliche Dauer**:
     - Wie lange dauert es typischerweise, bis eine Entscheidung zur Patentanmeldung fällt? (Wochen, Monate?)

5. **Widersprüche / Unklarheiten:**

   - Schritt 2: „Konferenz-Submission (noch nicht akzeptiert) – oft ja [öffentlich]“  
     → Das ist juristisch heikel und stark vom Konferenzprozess abhängig. Hier wäre eine vorsichtigere Formulierung sinnvoll („kann als Veröffentlichung gelten, je nach Prozess; unbedingt vorher klären“).
   - Schritt 1: „Startup / Solo – Meldepflicht: Nein“  
     → Das stimmt nur, wenn keine anderen Verträge bestehen (z.B. Werkverträge, Nebenbeschäftigungen). Ein kurzer Hinweis auf „prüfe trotzdem Verträge“ fehlt.

---

## 5. Top 5 Verbesserungsvorschläge (priorisiert)

1. **Pro Schritt eine klare „Aktion oben, Kontext unten“-Struktur einführen**

   - **Was genau?**  
     - Ganz oben im Schritt (direkt unter Titel) ein kurzer Block „Heute tun“ mit 1–3 Bulletpoints, maximal 2–3 Zeilen.
     - Darunter erst die erklärenden Info-, Kontext- und Beispielblöcke.
   - **Wo?**  
     - In allen Schritten 1–5, insbesondere 1 („Standort und Ansprechpartner:innen“) und 2 („Zeitfenster beachten“).
   - **Warum?**  
     - Die Persona will schnell wissen, was sie konkret tun soll. Aktuell muss sie sich das aus dem Fließtext herausziehen.

2. **Redundanz reduzieren und Text um ~30 % straffen**

   - **Was genau?**
     - Wiederholte Aussagen („Erst Strategie, dann Veröffentlichung“, „Uni: TTO/Erfindungsberater:in koordiniert“, „Firma: nicht eigenmächtig Anwalt beauftragen“) auf **einmal pro Guide** beschränken, danach nur noch in 1 Zeile erinnern.
     - Lange Sätze aufteilen, Füllphrasen streichen.
   - **Wo?**
     - Schritt 0 (Einleitung massiv kürzen), Schritt 1 (Kontext + Ansprechpartner zusammenfassen), Schritt 2 (Publication trap-Erklärung straffen), Schritt 3–5 (Kontextblöcke kürzen).
   - **Warum?**
     - Weniger Text = geringere kognitive Last. Die Persona liest eher alles, wenn es kompakt ist.

3. **Mehr konkrete, ausfüllbare Mini-Elemente einbauen (Checklisten, Felder, Tabellen)**

   - **Was genau?**
     - Schritt 1: Mini-Formular „Notiere: Kontext, Meldepflicht, Ansprechpartner:in“ als kleine Tabelle mit leeren Feldern.
     - Schritt 2: Checkliste mit Beispiel-Datum („Konferenz am __ → Erfindungsmeldung bis __“).
     - Schritt 3: Leitfragen als Bullet-Liste mit Skalen („Marktpotenzial: niedrig/mittel/hoch“).
     - Schritt 4: 3-Zeilen-Tabelle „To-do, Deadline, Status“.
   - **Wo?**
     - In den jeweiligen „So gehst du vor“-Abschnitten.
   - **Warum?**
     - Die Persona will etwas „mitnehmen“ – nicht nur Text, sondern konkrete Notizen/Entscheidungen.

4. **Maria-Beispiel als durchgehende Timeline strukturieren**

   - **Was genau?**
     - Pro Schritt ein kurzer, konsistenter Maria-Block mit Datum/Zeitrahmen:
       - Schritt 1: „Tag 0–2: Maria schreibt E-Mail an TTO.“
       - Schritt 2: „Konferenzdeadline 15. Juni → Meldung bis 1. Juni.“
       - Schritt 3: „Vor dem Gespräch beantwortet sie 4 Leitfragen.“
       - Schritt 4: „Ihre To-do-Liste mit konkreten Daten.“
       - Schritt 5: „Was sie im Gespräch mit der Erfindungsberaterin klärt.“
   - **Wo?**
     - In allen Schritten 1–5, jeweils ein kurzer, klar strukturierter Maria-Kasten.
   - **Warum?**
     - Erhöht Nachvollziehbarkeit und Identifikation. Die Persona kann ihren eigenen Fall direkt danebenlegen.

5. **Kontextspezifische Blöcke fokussieren und mit klaren Entscheidungsregeln anreichern**

   - **Was genau?**
     - Statt generischer Hinweise („Uni: TTO koordiniert“) pro Kontext 2–3 **klare Regeln**:
       - Uni: „Wenn du angestellt bist → Meldepflicht fast sicher. Wenn nur eingeschrieben ohne Vertrag → prüfen.“
       - Firma: „Immer zuerst Patentstelle/Vorgesetzte, nie direkt Anwalt.“
       - Startup: „Wenn du innerhalb der nächsten 3 Monate pitchen / veröffentlichen willst → spätestens 4 Wochen vorher Erstberatung.“
   - **Wo?**
     - In den „Spezifisch für deinen Kontext“-Blöcken in Schritt 1, 2, 3, 4, 5.
   - **Warum?**
     - Erhöht Entscheidungsfähigkeit, reduziert Unsicherheit. Weniger Wiederholung, mehr konkrete Handlungslogik.

---

## 6. Was bereits gut funktioniert

1. **Klarer, nicht-juristischer Ton**  
   Verständlich, direkt, ohne unnötigen Fachjargon. Das ist für die Persona genau richtig.

2. **Logische Schrittfolge (Kontext → Zeitfenster → Strategie → Prioritäten → Ergebnis)**  
   Entspricht der mentalen Reise der Nutzer:in und baut sinnvoll aufeinander auf.

3. **Publication trap als eigener Schritt mit Tabellen**  
   Das zentrale Risiko wird explizit adressiert und mit konkreten Situationen (Preprint, GitHub, Konferenz) verknüpft.

4. **E-Mail-Vorlage für erste Kontaktaufnahme**  
   Sehr praxisnah, senkt die Hemmschwelle, tatsächlich zu handeln.

---

## 7. Quick Wins (schnell umsetzbar)

1. **Einleitungsseite (Schritt 0) halbieren**

   - Kürze die Einleitung auf:
     - 1 Absatz „Du hast eine Erfindung – was jetzt?“
     - 1 Absatz „Was dieser Guide macht“ (max. 4 Sätze).
     - Tabelle mit 3 Szenarien beibehalten, restliche Prosa straffen.
   - Effekt: Schnellere Orientierung, weniger Scrollen, Einstieg wirkt weniger „textwandig“.

2. **In Schritt 1 ganz oben einen 3-Punkte-Aktionsblock einfügen**

   - Beispiel:
     - „Heute:  
       1. Ordne dich einem Kontext zu (Uni/Firma/Startup).  
       2. Prüfe, ob du eine Meldepflicht hast.  
       3. Finde deine erste Ansprechpartner:in und notiere Name/E-Mail.“
   - Effekt: Nutzer:in weiß sofort, was in diesem Schritt konkret zu tun ist.

3. **In Schritt 2 die zweite Tabelle („Typische akademische Situationen“) mit einem Warnhinweis ergänzen und sprachlich entschärfen**

   - Z.B. bei „Konferenz-Submission“: „Kann als Veröffentlichung gelten, je nach Prozess. Unbedingt vorher mit TTO/Patentstelle klären.“
   - Effekt: Reduziert das Risiko falscher Sicherheit oder unnötiger Panik, bleibt aber vorsichtig.

Diese Änderungen sind mit wenig Aufwand umsetzbar und verbessern sofort Lesbarkeit, Klarheit und Handlungsorientierung für die Persona.