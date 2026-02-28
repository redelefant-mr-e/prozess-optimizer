# HM: TI-RSS (Technical Inspection Road Side System)

**Quelle:** Hochschule München, Erfindungsmeldung Anlage 1  
**Erfindung:** Prüfsystem für Fahrzeugumfeldsensorik (ADAS) mittels C2X-Kommunikation

---

## Gliederung (Best Practice)

1. **Technische Aufgabe und Gebiet**
2. **Stand der Technik**
3. **Behebung bisheriger technischer Probleme / Nachteile**
4. **Technische Lösung**
5. **Vorteile gegenüber dem aktuellen Stand der Technik**
6. **Literaturverzeichnis**

---

## Technische Aufgabe (Auszug)

> Das erfundene System ist dem Gebiet einer technischen Untersuchung von Kraftfahrzeugen zuzuordnen. Die Aufgabe des Systems ist es, die Funktionalität der fahrzeugeigenen Umfeldsensorik (z.B. Kamera, Radar, LiDAR) und der nachfolgenden Datenverarbeitung zu testen. [...] Das System kann eine Ergänzung der bestehenden periodischen technischen Hauptuntersuchung (HU) sein.

---

## Stand der Technik (Struktur)

- Kontext: Fahrzeugumfeldsensoren für automatisiertes Fahren
- Homologation, HU, Service – Fahrzeugumfeldsensorik nicht verpflichtend geprüft
- Eigendiagnose reicht nicht aus [6, 7]
- **FSD ErVast [7]:** Demonstrator umkreist VUT – aber: Sensordatenzugriff nötig, nur Forschungsfahrzeuge
- **KÜS [8]:** ADAS-Rollenprüfstand – Prüfstandsmodus, nicht real
- **Virtual Vehicle SPIDER [9]:** Mobile Plattform – braucht gesonderte Teststrecke

**Erläuterungen:** FSD = FSD Fahrzeugsystemdaten GmbH (Zentrale Stelle); ErVast = Projekt zur Prüfung automatisierter Fahrfunktionen. KÜS = Kraftfahrzeug-Überwachungsorganisation. ADAS = Advanced Driver Assistance Systems (Fahrerassistenzsysteme). SPIDER = Smart Physical Demonstration and Evaluation Robot. VUT = Vehicle Under Test (zu testendes Fahrzeug).

**Nachteile zusammengefasst:** Kein Verfahren testet Serienfahrzeuge unter realen Bedingungen ohne Eingriff ins Fahrzeug.

---

## Kern der Neuerung (Formulierung)

> Das wesentliche Neue an der Erfindung ist, dass die Prüfung der Funktionalität der Fahrzeugumfeldsensorik **nicht unter Laborbedingungen und simulierten Signalen, sondern direkt auf der Straße durch Ausnutzung der C2X Kommunikation** funktioniert.

---

## Technische Lösung (Auszug)

> Das TI-RSS besteht aus drei Komponenten: Einer TI-RSU, einem Referenzobjekt (RO) und einer Cloud-Anbindung. [...] Grundprinzip ist die Gegenüberstellung zwischen der Verkehrssituation, wie sie das VUT über die eigene Sensorik erfasst, und der tatsächlichen Verkehrssituation (ground truth).

---

## Vorteile (Stichpunkte)

- Aperiodisches Überprüfen möglich
- Reale Prüfumgebung, kein Prüfstandsmodus
- Überprüfung von Serienfahrzeugen möglich ohne Eingriff ins VUT
- Aufbauend auf bestehender Technologie (C2X)
- Modularer Aufbau, an bestehende Verkehrsüberwachung anbindbar
