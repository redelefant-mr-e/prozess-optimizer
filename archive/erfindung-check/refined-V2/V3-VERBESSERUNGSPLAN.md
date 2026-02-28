# V3-Verbesserungsplan: Auf dem Weg zu 5/5

## Übersicht

Ziel von V3 ist, die letzten Hürden für die unsichere Erfinder:in zu entfernen: kognitive Entlastung in Schritt 3/4, mechanikfokussierte Beispiele ohne falsche Sicherheit und ein UX-Flow, der die gefühlte „Wizard“-Logik technisch einlöst.  
Die Maßnahmen sind nach Impact auf Abbruchrisiko priorisiert und jeweils so formuliert, dass sie 1:1 in Text/Code übernommen werden können.

---

## Priorität 1: Kognitive Entlastung (Schritt 3 & 4)

*Die größten Abbruchrisiken – Mikro-Walkthroughs und konkrete Beispiele*

### 1.1 Mikro-Walkthrough Schritt 3 (Prior Art)

- **Problem (aus V2-Eval):**  
  Kombination aus Datenbankwahl, Keywords, 3 Ebenen (Bild/Abstract/Claims) und Relevanz-Checkliste ist „viel auf einmal“. Es fehlt ein durchgehendes, sehr kleines Beispiel, das zeigt: „So sieht ein konkreter Suchlauf aus, so entscheidest du.“

- **Lösung:**  
  Direkt nach „### 4. Arbeite in drei Ebenen, um schnell zu filtern“ einen kompakten Mikro-Walkthrough mit der Einhand-Schnellspannzwinge einfügen, der:
  - eine konkrete Suchanfrage nennt,
  - 2–3 Treffer beschreibt (nur verbal, keine echten Screenshots nötig),
  - pro Treffer explizit zeigt: Was sehe ich im Bild? Was steht im Abstract? Wie entscheide ich „relevant oder nicht“?

- **Datei/Stelle:**  
  `03-Prior-Art-suchen.md`  
  Einfügen **unterhalb** der Tabelle „3 Ebenen“ als eigenen Unterabschnitt `### Mini-Beispiel: So sieht ein Suchlauf konkret aus`.

- **Beispiel-Formulierung (wörtlich verwendbar):**

  ```markdown
  ### Mini-Beispiel: So sieht ein Suchlauf konkret aus

  Nehmen wir die Einhand-Schnellspannzwinge für Fahrradlenker aus dem Beispiel.

  1. **Suchanfrage in Espacenet:**  
     Gib ein: `quick release clamp handlebar one hand`.

  2. **Erster Treffer in der Liste:**  
     - **Bild/Skizze:** Du siehst eine Klemme, die um einen runden Lenker gelegt wird, mit einem seitlichen Hebel.  
       → Das sieht deinem Mechanismus sehr ähnlich.  
     - **Abstract (Kurzbeschreibung):** „Quick-release clamp for bicycle handlebars, operable with one hand …“  
       → Gleicher Anwendungsfall (Lenker) und gleiche Wirkung (Einhand-Schnellspannen).  
     - **Entscheidung:** **relevant** – du nimmst den Treffer in deine Tabelle auf.

  3. **Zweiter Treffer:**  
     - **Bild/Skizze:** Eine Zwinge für Werkbänke, die an einer Tischkante befestigt wird, mit einem Schnellspannhebel.  
       → Anderer Anwendungsfall (Werkbank statt Lenker), aber ähnlicher Hebelmechanismus.  
     - **Abstract:** „One-hand quick-release clamp for securing workpieces on a table …“  
       → Wirkung (Einhand-Schnellspannen) ist ähnlich, Objekt ist anders.  
     - **Entscheidung:** **relevant** – du nimmst den Treffer auf, weil der Mechanismus interessant ist.

  4. **Dritter Treffer:**  
     - **Bild/Skizze:** Eine klassische Schraubzwinge mit Drehgriff, kein Hebel.  
       → Mechanik sieht deutlich anders aus.  
     - **Abstract:** „Screw clamp for adjustable fixation …“ – keine Einhandbedienung, kein Schnellspann.  
       → Andere Wirkung, anderer Mechanismus.  
     - **Entscheidung:** **nicht relevant** – du nimmst den Treffer **nicht** in deine Tabelle auf.

  So arbeitest du dich nur durch die ersten 20 Treffer deiner Suchanfrage und speicherst nur die, bei denen Bild **und** Abstract wirklich nach deinem Prinzip aussehen.
  ```

---

### 1.2 Mikro-Walkthrough Schritt 4 (Treffer bewerten)

- **Problem:**  
  Die Entscheidungsmatrix ist inhaltlich gut, aber abstrakt. Die Persona muss sie mehrfach lesen. Es fehlt ein Mini-Beispiel direkt an der Matrix, das zeigt: „Treffer X wirkt ähnlich – so ordnest du ihn in eine Kategorie ein.“

- **Lösung:**  
  - Direkt **unterhalb** der Entscheidungsmatrix einen „Mini-Case“ ergänzen, der einen konkreten Treffer (z.B. „BikeGear Innovations“) von der ersten Wahrnehmung („wirkt sehr ähnlich“) bis zur finalen Kategorie („sehr ähnlich“ oder „praktisch gleich“) durchdekliniert.
  - Zusätzlich in der Bewertungstabelle eine **Beispielzeile** mit vollständig ausgefüllten Spalten ergänzen.

- **Datei/Stelle:**  
  `04-Treffer-bewerten.md`  
  1. Unter der Matrix einen Abschnitt `### Mini-Beispiel: Einen Treffer durch die Matrix führen` einfügen.  
  2. In der Tabelle, in der Markt- und Patenttreffer bewertet werden, eine erste Zeile als „Beispiel (Einhand-Schnellspannzwinge)“ einfügen.

- **Beispiel-Formulierung (Matrix-Walkthrough):**

  ```markdown
  ### Mini-Beispiel: Einen Treffer durch die Matrix führen

  Beispiel-Treffer: **BikeGear Innovations – Schnellspannklemme für Fahrradlenker**

  1. **Frage 1: Erreicht der Treffer dieselbe Wirkung?**  
     Deine Erfindung: „Einhand-Schnellspannen am Fahrradlenker“.  
     BikeGear: Beschreibt ebenfalls eine Klemme, die mit einem Hebel am Lenker mit einer Hand gespannt und gelöst werden kann.  
     → Antwort: **Ja** → du gehst zur nächsten Frage.

  2. **Frage 2: Nutzt er denselben Mechanismus?**  
     Du siehst in der Skizze: ein seitlicher Hebel, der über eine Exzenterbewegung zwei Klemmbacken zusammenzieht.  
     Deine Idee nutzt ebenfalls einen seitlichen Hebel mit Exzenter, nur mit leicht anderer Hebelgeometrie.  
     → Antwort: **Ja, im Kern derselbe Mechanismus**.  
     → Kategorie: **„praktisch gleich“**.

  3. **Was trägst du in die Tabelle ein?**  
     - Kategorie: „praktisch gleich“  
     - Kurzkommentar: „Gleiche Wirkung (Einhand-Schnellspannen am Lenker) und im Kern derselbe Hebel-Exzenter-Mechanismus. Unterschiede nur in Details der Hebelform.“

  So siehst du: Auch wenn dein Hebel etwas anders aussieht, kann der Treffer trotzdem in die Kategorie „praktisch gleich“ fallen.
  ```

- **Beispiel-Formulierung (zusätzliche Tabellenzeile):**

  Angenommen, du hast in `04-Treffer-bewerten.md` eine Tabelle wie:

  ```markdown
  | Quelle | Name/Titel | Kategorie (Matrix) | Kurzbegründung |
  |--------|------------|--------------------|----------------|
  ```

  Ergänze als **erste Zeile**:

  ```markdown
  | Beispiel (Einhand-Schnellspannzwinge) | BikeGear Innovations – Schnellspannklemme für Fahrradlenker | praktisch gleich | Gleiche Wirkung (Einhand-Schnellspannen am Lenker) und im Kern derselbe Hebel-Exzenter-Mechanismus; Unterschiede nur in der Hebelform. |
  ```

---

## Priorität 2: Beispiel-Qualität (Kernidee & Konsistenz)

*Mechanikfokus, keine falsche Sicherheit*

### 2.1 Kernidee-Beispiel überarbeiten

- **Problem:**  
  Die bisherige Kernidee-Formulierung mit „unter allen Wetterbedingungen sicher bedient werden kann“ ist eher marketing-/kontextorientiert. Sie kann der Persona suggerieren, man könne sich durch Kontext („Wetter“) aus einem bestehenden Patent „rausdefinieren“, statt das mechanische Prinzip zu adressieren.

- **Lösung:**  
  - Kernidee-Beispiel konsequent auf **mechanische Unterschiede** fokussieren (Hebelgeometrie, Rastmechanismus, Kraftübertragung, Position der Lagerpunkte).
  - Den Kontext (z.B. Wetter, Komfort) nur als **Nebenbedingung** erwähnen, nicht als Kern der Neuheit.
  - Explizit machen, dass trotz mechanischer Unterschiede unklar bleiben kann, ob das bestehende Patent den neuen Mechanismus mit abdeckt.

- **Datei/Stelle:**  
  `05-Kern-schärfen.md` – Abschnitt mit der Beispiel-Kernidee.  
  `06-Ergebnis-ableiten.md` – Beispiel-Tabellen/Begründung für „Unklar“.

- **Neue Kernidee (Beispiel – wörtlich verwendbar):**

  ```markdown
  **Beispiel: Kernidee der Einhand-Schnellspannzwinge (mechanikfokussiert)**

  *Neu ist, dass* der Schnellspannhebel der Lenkerklemme über einen **zweistufigen Rastmechanismus** mit definierter Zwischenposition geführt wird:

  - In einer **ersten Rastposition** liegen die Klemmbacken lose am Lenker an, sodass sich die Klemme mit einer Hand entlang des Lenkers verschieben lässt.
  - In der **zweiten Rastposition** wird über einen Exzenter und eine veränderte Hebelgeometrie eine höhere Klemmkraft erzeugt, ohne dass der Hebel den Lenker oder andere Anbauteile berührt.
  - Die Lagerpunkte des Hebels sind so angeordnet, dass sich der Hebelweg auf einen Winkel von maximal 60° beschränkt und mit einem Daumen bedient werden kann.

  Der Kern der Erfindung liegt damit im **spezifischen Zusammenspiel aus Hebelgeometrie, Exzenter und zweistufiger Rastung**, nicht nur darin, dass die Klemme „komfortabel“ oder „bei jedem Wetter“ bedient werden kann.
  ```

- **Ergänzende Klarstellung in `06-Ergebnis-ableiten.md` (um falsche Sicherheit zu vermeiden):**

  ```markdown
  **Wichtiger Hinweis zum Beispiel:**

  Auch wenn sich die Kernidee im Beispiel auf einen speziellen zweistufigen Rastmechanismus stützt, kann es sein, dass ein bestehendes Patent zu Schnellspannklemmen **auch solche Varianten mit abdeckt**. Deshalb ordnen wir das Beispiel im Ergebnis als **„unklar“** ein – nicht als „sicher neu“.
  ```

---

### 2.2 Varianten-Kommentar ergänzen

- **Problem:**  
  Die Varianten (z.B. zusätzlicher Sicherheitsverschluss, verstellbare Spannkraft) werden genannt, aber es wird nicht gezeigt, wie sie sich zu bestehenden Patenten verhalten. Die Persona lernt dadurch nicht, wie man Varianten im Lichte vorhandener Schutzrechte denkt.

- **Lösung:**  
  - Für jede Beispiel-Variante einen **kurzen Kommentar** ergänzen:
    - „könnte vom Patent X mit erfasst sein, weil …“ oder
    - „eher eigenständig, weil Mechanismus Y anders ist“.
  - Klarstellen, dass Varianten nicht automatisch „neu“ sind, nur weil sie anders aussehen.

- **Datei/Stelle:**  
  `05-Kern-schärfen.md` – direkt unter der Varianten-Liste.  
  Optional Verweis in `06-Ergebnis-ableiten.md` bei der Einordnung „Unklar“.

- **Beispiel-Formulierung (wörtlich verwendbar):**

  Angenommen, du hast in `05-Kern-schärfen.md` bereits eine Liste wie:

  ```markdown
  **Mögliche Varianten der Kernidee (Beispiel):**

  - Variante A: zusätzlicher Sicherheitsverschluss, der den Hebel in geschlossener Position verriegelt.
  - Variante B: verstellbare Spannkraft über eine Feineinstellschraube am Hebel.
  ```

  Ergänze darunter:

  ```markdown
  **Wie verhalten sich diese Varianten zu bestehenden Patenten? (Beispiel-Denkmuster)**

  - **Variante A – zusätzlicher Sicherheitsverschluss:**  
    Wenn ein bestehendes Patent bereits eine Schnellspannklemme mit Hebel beschreibt, kann ein zusätzlicher Verriegelungsmechanismus als **naheliegende Ergänzung** betrachtet werden. Er könnte vom bestehenden Patent mit erfasst sein, wenn dort allgemein „Sicherungsmechanismen“ beansprucht werden.  
    → Für dich heißt das: Diese Variante ist **nicht automatisch neu**, nur weil ein Riegel dazukommt.

  - **Variante B – verstellbare Spannkraft über Feineinstellschraube:**  
    Wenn das Patent nur einen festen Schnellspannmechanismus ohne Feineinstellung beschreibt, kann eine zusätzliche Feineinstellschraube eine **technische Variante** sein. Ob sie noch vom Patent erfasst ist, hängt davon ab, wie breit die Ansprüche formuliert sind (z.B. „any means for adjusting clamping force“).  
    → Für dich heißt das: Auch hier ist ohne genaue Anspruchsanalyse **unklar**, ob die Variante wirklich außerhalb des bestehenden Patents liegt.

  Diese Kommentare sollen dir zeigen: Varianten sind wichtig, aber sie ersetzen keine professionelle Prüfung, ob ein bestehendes Patent sie mit abdeckt.
  ```

---

## Priorität 3: UX-Feinschliff

*Stepper, Navigation, Orientierung*

### 3.1 Stepper-Dynamik prüfen/verbessern

- **Problem:**  
  - Im HTML ist beim Laden nur Schritt 0 als `.active` markiert.  
  - Es gibt kein JavaScript, das beim Scrollen den aktiven Schritt aktualisiert.  
  - Die Anzeige „Du bist bei Schritt X von 7“ bleibt statisch.  
  → Für die Persona entsteht ein Bruch: Der Stepper wirkt wie ein Wizard, verhält sich aber wie eine statische Liste.

- **Lösung:**  
  - Ein kleines JavaScript einbauen, das:
    - per `IntersectionObserver` oder Scroll-Listener erkennt, welcher Schritt gerade im Viewport ist,
    - im Stepper die entsprechende `.active`-Klasse setzt,
    - den Text „Du bist bei Schritt X von 7“ dynamisch aktualisiert.
  - Sicherstellen, dass die IDs der Schritt-Sektionen (`#step-0`, `#step-1`, …) mit den Stepper-Links übereinstimmen.

- **Datei/Stelle:**  
  `erfindung-check.html`  
  - Schritt-Sektionen: `<section id="step-0">`, `<section id="step-1">`, …  
  - Stepper: `<nav class="stepper">…</nav>`  
  - Neues `<script>`-Tag am Ende des `<body>`.

- **Konkretes JS-Snippet (wörtlich einfügbar, ggf. IDs/Klassen anpassen):**

  ```html
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      const sections = document.querySelectorAll('section[id^="step-"]');
      const stepperLinks = document.querySelectorAll('.stepper a[href^="#step-"]');
      const progressLabel = document.querySelector('.stepper-progress'); // z.B. <div class="stepper-progress">Du bist bei Schritt 0 von 7</div>

      // Map von section.id → Schritt-Nummer (0-basiert)
      const stepIndexById = {};
      sections.forEach((sec, index) => {
        stepIndexById[sec.id] = index;
      });

      function setActiveStep(id) {
        stepperLinks.forEach(link => {
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });

        if (progressLabel && typeof stepIndexById[id] !== 'undefined') {
          const current = stepIndexById[id];
          const total = sections.length;
          progressLabel.textContent = `Du bist bei Schritt ${current} von ${total - 1}`;
        }
      }

      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              setActiveStep(entry.target.id);
            }
          });
        },
        {
          root: null,
          threshold: 0.4 // Abschnitt ist „aktiv“, wenn ~40% sichtbar
        }
      );

      sections.forEach(sec => observer.observe(sec));
    });
  </script>
  ```

  > Hinweis: Falls du aktuell keine `.stepper-progress`-Box hast, füge im Stepper-Bereich z.B. ein:
  >
  > ```html
  > <div class="stepper-progress">Du bist bei Schritt 0 von 7</div>
  > ```

---

### 3.2 „Zurück nach oben / zum Stepper“-Link

- **Problem:**  
  Die einzelnen Schritte sind lang. Auf mobilen Geräten oder bei konzentriertem Lesen am Stück verliert die Persona leicht den Überblick und muss viel scrollen, um wieder zum Stepper zu kommen.

- **Lösung:**  
  - Am Ende **jedes** Schritts einen klar sichtbaren Link/Button einfügen:
    - „↑ Zurück zum Überblick“ oder „↑ Zurück zur Schrittübersicht“,
    - der zum Stepper-Bereich (z.B. `#stepper-top`) scrollt.
  - Optional: Den Link visuell als sekundären Button gestalten.

- **Datei/Stelle:**  
  `erfindung-check.html`  
  - Direkt vor dem Ende jeder `<section id="step-X">…</section>`.

- **Beispiel-Formulierung (HTML, wörtlich einfügbar):**

  ```html
  <p class="back-to-top">
    <a href="#stepper-top">↑ Zurück zur Schrittübersicht</a>
  </p>
  ```

  Und im Stepper-Bereich sicherstellen, dass ein Anker existiert:

  ```html
  <div id="stepper-top"></div>
  <nav class="stepper">
    <!-- Stepper-Inhalt -->
  </nav>
  ```

  Optionales CSS:

  ```css
  .back-to-top {
    margin-top: 2rem;
    text-align: right;
  }

  .back-to-top a {
    font-size: 0.9rem;
    text-decoration: none;
  }
  ```

---

## Priorität 4: Glossar & Verständlichkeit

*Begriffe für Laien klären*

### 4.1 Tooltips für weitere Begriffe

- **Problem:**  
  Begriffe wie „Funktionsprinzip“, „Mechanismus“, „Kontext“, „Kernprinzip“ tauchen mehrfach auf. Für Laien können diese Begriffe verschwimmen. Bisher gibt es nur vereinzelt Tooltips (z.B. für „Prior Art“).

- **Lösung:**  
  - Für die zentralen Fachbegriffe konsistente Tooltips einführen:
    - „Funktionsprinzip“
    - „Mechanismus“
    - „Kontext“
    - „Kernprinzip“ / „Kernidee“
  - Die Definitionen sollen **in einem Satz** und laienverständlich sein, z.B.:
    - Funktionsprinzip: „Was passiert technisch, damit die Wirkung entsteht?“
    - Mechanismus: „Die konkrete Anordnung von Teilen, die das Funktionsprinzip umsetzt.“

- **Datei/Stelle:**  
  `erfindung-check.html`  
  - Im Stepper-Content, wo die Begriffe das erste Mal auftauchen (z.B. in Schritt 4/5).
  - Tooltip-Implementierung analog zum bestehenden „Prior Art“-Tooltip.

- **Beispiel-Formulierungen (HTML, wörtlich einfügbar):**

  ```html
  Funktionsprinzip
  <span class="tooltip">
    ?
    <span class="tooltip-text">
      Funktionsprinzip = Was technisch passiert, damit die gewünschte Wirkung entsteht (z.B. „Hebel drückt Klemmbacken zusammen“).
    </span>
  </span>
  ```

  ```html
  Mechanismus
  <span class="tooltip">
    ?
    <span class="tooltip-text">
      Mechanismus = Die konkrete Anordnung und Bewegung von Teilen, die das Funktionsprinzip umsetzt (z.B. Hebel, Exzenter, Klemmbacken).
    </span>
  </span>
  ```

  ```html
  Kontext
  <span class="tooltip">
    ?
    <span class="tooltip-text">
      Kontext = Umgebung und Einsatzsituation deiner Lösung (z.B. Fahrradlenker im Außenbereich, Laborumgebung, Software-Backend).
    </span>
  </span>
  ```

  ```html
  Kernprinzip
  <span class="tooltip">
    ?
    <span class="tooltip-text">
      Kernprinzip = Der eine technische Grundgedanke, ohne den deine Lösung nicht funktionieren würde.
    </span>
  </span>
  ```

---

### 4.2 Optional: Kurzes Glossar

- **Problem:**  
  Auch mit Tooltips kann es hilfreich sein, alle wichtigen Begriffe an einer Stelle gesammelt zu sehen – besonders für Nutzer:innen, die lieber einmal „alles lesen“ und dann arbeiten.

- **Lösung:**  
  - Eine kompakte Glossar-Box mit 5–8 Begriffen am Ende der Einleitung oder direkt nach Schritt 0 einfügen.
  - Als aufklappbares Element („Glossar einblenden“) gestalten, damit es nicht stört, aber verfügbar ist.

- **Datei/Stelle:**  
  `erfindung-check.html` oder `00-Einleitung.md` (je nach Build-Prozess).  
  Position: Unterhalb von „Warum dieser Check?“ / „Warum jetzt und nicht später?“.

- **Beispiel-Formulierung (Markdown/HTML, wörtlich verwendbar):**

  ```markdown
  <details>
    <summary><strong>Kurzes Glossar (optional)</strong></summary>

  - **Prior Art:** Alles, was vor deiner Idee schon öffentlich beschrieben oder geschützt wurde (Produkte, Patente, Publikationen).
  - **Funktionsprinzip:** Was technisch passiert, damit die gewünschte Wirkung entsteht (z.B. „Hebel drückt Klemmbacken zusammen“).
  - **Mechanismus:** Die konkrete Anordnung und Bewegung von Teilen, die das Funktionsprinzip umsetzt.
  - **Kontext:** Umgebung und Einsatzsituation deiner Lösung (z.B. Fahrradlenker, Labor, Software-Backend).
  - **Kernprinzip / Kernidee:** Der eine technische Grundgedanke, ohne den deine Lösung nicht funktionieren würde.
  - **Patentanspruch (Claim):** Der Teil eines Patents, der beschreibt, was genau geschützt sein soll.
  - **Variante:** Eine technische Abwandlung deiner Kernidee (z.B. anderer Hebel, zusätzlicher Riegel), die das Grundprinzip beibehält.

  </details>
  ```

---

## Priorität 5: Optional (Nice-to-have für 5/5)

*Wenn Zeit bleibt*

### 5.1 Cheat-Sheet / Kurzansicht

- **Ziel:**  
  Der/die Nutzer:in kann den Prozess auf 1–2 Seiten überblicken, ausdrucken oder nebenher offen haben. Das reduziert die gefühlte Komplexität und unterstützt die „1–2 Abende“-Story.

- **Lösung (Inhalt):**  
  - Pro Schritt:
    - 1 Satz Ziel,
    - 3–5 Bulletpoints „So gehst du vor“,
    - 1 Bullet „Minimal-Variante“.
  - Keine Beispiele, nur Struktur.

- **Datei/Stelle:**  
  - Entweder als eigener Abschnitt in `erfindung-check.html` (z.B. `#cheat-sheet`)  
  - oder als separate Datei `erfindung-check-cheatsheet.html` / PDF.

- **Beispiel-Formulierung (Ausschnitt, Schritt 3 & 4):**

  ```markdown
  ## Cheat-Sheet: Schritt 3 – Prior Art suchen

  **Ziel:** Schnell erkennen, ob dein Kernprinzip bereits in Patenten oder Publikationen auftaucht.

  - Wähle 1 Patentdatenbank (Espacenet oder Google Patents).
  - Starte mit genau 3 Suchanfragen aus deinen Markt-Keywords (Deutsch/Englisch).
  - Scrolle pro Suchanfrage nur durch die ersten 20 Treffer.
  - Speichere nur Treffer, bei denen Bild **und** Abstract wirklich nach deinem Prinzip aussehen.
  - Notiere pro Treffer: Titel, Jahr, Quelle, Link, 1 Satz „warum relevant“.

  **Minimal-Variante:** 3–5 relevante Treffer in 1 Datenbank, 1 Satz Begründung pro Treffer.
  ```

---

### 5.2 Suchlauf-Beispiel Schritt 3 (zu viele/zu wenige Treffer)

- **Ziel:**  
  Die Persona bekommt ein klares Bild, wie man bei „zu vielen“ oder „zu wenigen“ Treffern konkret nachjustiert.

- **Lösung:**  
  - In Schritt 3 unter „Tipp – zu viele/zu wenige Treffer“ ein kurzes, konkretes Beispiel ergänzen:
    - Ausgangssuche → 500 Treffer → Anpassung → 30 Treffer.
    - Ausgangssuche → 0 Treffer → Anpassung → 10 Treffer.

- **Datei/Stelle:**  
  `03-Prior-Art-suchen.md` – unter „Tipp“.

- **Beispiel-Formulierung (wörtlich verwendbar):**

  ```markdown
  **Mini-Beispiele zum Nachjustieren:**

  - **Zu viele Treffer (z.B. 500+):**  
    Ausgangssuche: `clamp`  
    → Ergebnis: sehr viele allgemeine Klemmen.  
    Anpassung: `quick release clamp handlebar one hand`  
    → Ergebnis: ca. 30 Treffer, davon 5 wirklich relevant.

  - **Zu wenige Treffer (z.B. 0–2):**  
    Ausgangssuche: `one-hand quick release clamp for bicycle handlebar` (sehr spezifisch)  
    → Ergebnis: 0 Treffer.  
    Anpassung:  
    - erst breiter: `quick release clamp handlebar`  
    - dann noch breiter: `quick release clamp`  
    → Ergebnis: erst 10, dann 80 Treffer – du filterst wieder mit Bildern und Abstract.
  ```

---

## Umsetzungsreihenfolge (Top 10)

1. **Mikro-Walkthrough in Schritt 3 ergänzen** (`03-Prior-Art-suchen.md`, Abschnitt „Mini-Beispiel: So sieht ein Suchlauf konkret aus“).
2. **Mikro-Walkthrough in Schritt 4 ergänzen** (`04-Treffer-bewerten.md`, Abschnitt „Mini-Beispiel: Einen Treffer durch die Matrix führen“).
3. **Beispielzeile in der Bewertungstabelle von Schritt 4 ergänzen** (`04-Treffer-bewerten.md`).
4. **Kernidee-Beispiel mechanikfokussiert neu formulieren** (`05-Kern-schärfen.md`).
5. **Hinweis zur Unsicherheit trotz mechanischer Unterschiede in Schritt 6 ergänzen** (`06-Ergebnis-ableiten.md`).
6. **Varianten-Kommentare zur Patentnähe ergänzen** (`05-Kern-schärfen.md`).
7. **Stepper-Dynamik per JavaScript implementieren** (`erfindung-check.html` + Script).
8. **„Zurück zur Schrittübersicht“-Link am Ende jedes Schritts einfügen** (`erfindung-check.html`).
9. **Tooltips für Funktionsprinzip/Mechanismus/Kontext/Kernprinzip ergänzen** (`erfindung-check.html`).
10. **Optionales Glossar als `<details>`-Box nach der Einleitung einfügen** (`erfindung-check.html` oder `00-Einleitung.md`).

(Nice-to-have: Cheat-Sheet und zusätzliche Suchlauf-Beispiele danach.)

---

## Erfolgskriterien für 5/5

Aus Persona-Sicht ist 5/5 erreicht, wenn:

1. **Selbstständige Durchführbarkeit ohne externe Hilfe**
   - Test: 3–5 Nutzer:innen aus der Zielgruppe (keine Patent-Erfahrung) durchlaufen den Prozess ohne Live-Support.  
   - Kriterium: Mindestens 4/5 kommen bis Schritt 6 und können eine der drei Ergebnis-Kategorien („neu/unklar/bekannt“) selbst wählen.

2. **Keine kognitiven Überforderungspunkte in Schritt 3 & 4**
   - Test: Nach Schritt 3 und 4 wird abgefragt: „Wie sicher fühlst du dich auf einer Skala von 1–5, dass du weißt, was du tun sollst?“  
   - Kriterium: Durchschnitt ≥ 4/5; keine Kommentare wie „zu theoretisch“, „weiß nicht, wie ich entscheiden soll“.

3. **Mechanikfokus und realistische Erwartung**
   - Test: Nutzer:innen sollen in eigenen Worten beschreiben, was im Beispiel die „Kernidee“ ist und warum das Ergebnis „unklar“ ist.  
   - Kriterium: Sie nennen mechanische Aspekte (Hebel, Rastmechanismus, Kraftübertragung) und erwähnen, dass trotz Unterschied ein bestehendes Patent sie abdecken könnte.

4. **UX-Orientierung jederzeit klar**
   - Test: Beobachtung bei Nutzung (Desktop + mobil).  
   - Kriterium:
     - Nutzer:innen können jederzeit sagen, bei welchem Schritt sie sind, ohne nachzudenken.
     - Niemand verliert den Stepper „aus den Augen“ oder scrollt frustriert nach oben.

5. **Verständlichkeit zentraler Begriffe**
   - Test: Kurzer Begriffstest nach Abschluss („Was verstehst du unter Funktionsprinzip/Mechanismus/Kernidee?“).  
   - Kriterium: Mindestens 4/5 geben laiengerechte, inhaltlich passende Beschreibungen.

Wenn diese Kriterien erfüllt sind, ist der Erfindung-Check aus Sicht der unsicheren Erfinder:in auf 5/5-Niveau.