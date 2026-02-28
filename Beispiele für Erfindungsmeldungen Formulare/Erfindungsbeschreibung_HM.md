---
summary: |
  **Context:** Erfindungsmeldung (Anlage 1) der Hochschule München (HM) – Beispiel für eine vollständige
  technische Erfindungsbeschreibung im deutschen Patentformat.

  **Purpose:** Dient als Vorlage/Template für Erfinder:innen, die eine Erfindung bei einer Hochschule melden.
  Zeigt die typische Struktur: Technische Aufgabe, Stand der Technik, Behebung von Nachteilen, Technische Lösung,
  Literaturverzeichnis.

  **Important notes:** Thema: TI-RSS (Technical Inspection Road Side System) – Prüfsystem für Fahrzeugumfeldsensorik
  (ADAS) mittels C2X-Kommunikation. Enthält 4 Skizzen (im Original-PDF). Textbasiertes PDF, vollständig extrahierbar.
source: HM
pages: 6
extraction: text
---

# Erfindungsbeschreibung

Erfindungsmeldung: Anlage 1 
5 Seiten Beschreibung der Erfindung inkl. 4 Skizzen/Zeichnungen 
## Technische Aufgabe und Gebiet
Das erfundene System ist dem Gebiet einer technischen Untersuchung von Kraftfahrzeugen zuzuordnen. Die Aufgabe 
des Systems ist es, die Funktionalität der fahrzeugeigenen Umfeldsensorik (z.B. Kamera, Radar, LiDAR) und der 
nachfolgenden Datenverarbeitung zu testen. In anderen Worten testet das System bei einem Kraftfahrzeug, ob die 
Objekte in der Umgebung des Kraftfahrzeugs vom Kraftfahrzeug korrekt wahrgenommen werden. Dabei wird das 
gesamte Fahrzeugsystem getestet, ohne in das Fahrzeug selbst einzugreifen. Das System kann eine Ergänzung der 
bestehenden periodischen technischen Hauptuntersuchung (HU, englisch: periodical technical inspection (PTI)) sein 
und ist daher mit diesem Gebiet verwandt. Das System ist unabhängig von Fahrzeugherstellern bzw. 
Prüforganisationen. Grundsätzlich ist das System modular aufgebaut und kann an bestehenden Verkehrsüberwachungssysteme (z.B. Toll Collect, fest installierten Geschwindigkeits-, Abstands- oder
Rotlichtüberwachungsanlagen, Verkehrsdichtemessgeräten usw.) positioniert werden. 
## Stand der Technik
Fahrzeugumfeldsensoren sind von entscheidender Bedeutung für das automatisierte Fahren.
Fahrzeugumfeldsensoren, wie Radare, Lidar und Kameras, sind verantwortlich für die Erfassung und Interpretation der 
Umgebung, wodurch das Fahrzeug in der Lage ist, präzise Entscheidungen in Echtzeit zu treffen. Die 
Fahrzeugumfeldsensorik ist also ein Grundbestandteil für das automatisierte Fahrerassistenzfunktionen (ADAS, 
advances driver assistance system). Dazu ist es unabdingbar, dass die Funktion der Fahrzeugumfeldsensorik 
sichergestellt ist, um potenzielle Risiken zu minimieren und Unfälle zu verhindern. Je höher die Automatisierungsstufe 
[1], desto zuverlässiger muss die Fahrzeugumfeldsensorik sein. 
Die Homologation (Typgenehmigung) [2] neuer Kraftfahrzeuge ist der letzte Schritt der Fahrzeugentwicklung. Bei 
erfolgreicher Homologation wird das Fahrzeug zugelassen, ab dann ist das Fahrzeug in Betrieb. Im Rahmen der 
Homologation werden Fahrzeuge und deren Funktionsweise grundlegend geprüft, was auch automatisierte 
Fahrfunktionen und die Fahrzeugumfeldsensorik miteinschließt. 
Im Betrieb selbst wird ein Kraftfahrzeug im Rahmen von Service Terminen, durch die Fahrzeugeigendiagnose und bei 
der Hauptuntersuchung überprüft. Die Service Termine sind lediglich Herstellerempfehlungen und rechtlich nicht 
verpflichtend. In der Regel sind Service Termine von Fahrzeugherstellern alle ein bis zwei Jahre bzw. nach 15.000 bis 
30.000 km empfohlen [3]. In Kombination mit der Anzahl von 1,05 Wartungen pro Pkw in Deutschland im Jahr 2020 
[4], kann abgeschätzt werden, dass Kraftfahrzeuge nicht häufiger als jährlich eine Werkstatt aufsuchen. Dabei muss die 
Fahrzeugumfeldsensorik nicht zwangsweise untersucht werden. 
Die Vorstellung eines Kraftfahrzeugs zur HU ist gesetzlich vorgeschrieben und in der StVZO § 29 mit jeweiligen Anlagen 
geregelt [5]. Neuwagen müssen drei Jahre nach Zulassung zur HU vorgestellt werden, danach alle zwei Jahre (Anlage 
VIII (§ 29 Absatz 1 bis 4, 7, 9, 11 und 13) Untersuchung der Fahrzeuge [5]. In der Anlage VIIIa (§ 29 Absatz 1 und 3, 
Anlage VIII Nummer 1.2) Durchführung der Hauptuntersuchung [5] sind im Absatz 6 Untersuchung die 
vorgeschriebenen Untersuchungspunkte aufgelistet. Dabei ist die Fahrzeugumfeldsensorik nicht aufgeführt und 
demnach kein Prüfpunkt bei einer HU. 
Die Eigendiagnose eines Kraftfahrzeugs überwacht das Fahrzeug kontinuierlich in Echtzeit. Die Überwachung beruht in 
der Regel auf den Daten verschiedenster Sensordaten (z.B. der Lambda Sensor zur Überwachung der 
Abgaszusammensetzung) und im Fahrzeug verbauter Steuergeräte. Andere Forschungsarbeiten [6, 7] haben gezeigt, 
dass die Eigendiagnose nicht immer in der Lage ist einen Fehler der Fahrzeugumfeldsensorik zu erkennen, sodass es 
keine fahrzeugseitige Fehlermeldung gibt und die Fahrzeugumfeldsensorik mit hohen Leistungseinschränkungen 
weiter aktiv bleibt. Hier besteht bei hohen Automatisierungsstufen ein enormes Potential zu schweren Unfällen. 
Aus diesem Grund arbeiten die Überwachungsorganisationen (DEKRA, TÜV, KÜS, …) und die FSD Fahrzeugsystemdaten 
GmbH (Zentrale Stelle nach StVG) an neuen unabhängigen Prüfmöglichkeiten für die Fahrzeugumfeldsensorik und 
automatisierter Fahrfunktionen modernen Fahrzeuge. 
Die FSD erarbeitete hier bereits in dem Projekt ErVast [7] einen Fahrzeug-Demonstrator mit dem die 
Fahrzeugumfeldsensorik getestet werden kann [7]. Dies wird mit dem Demonstrator ermöglicht, der das zu testende 
Fahrzeug (vehicle under test, VUT) automatisiert umkreist und dabei alle Fahrzeugumfeldsensoren des VUT anregt. 

Die vom VUT erkannte Position des Demonstrators wird anschließend mit einer Referenz verglichen. Die Auswertung 
gelingt hier nur aufgrund des vollständigen Zugriffs auf die Sensordaten, da das VUT in diesem Fall ein 
Forschungsfahrzeug und kein Serienfahrzeug ist. 
Die KÜS stellte dieses Jahr einen ADAS-Rollenprüfstand vor, welcher das Überprüfen der Fahrzeugumfeldsensoren und 
ADAS-Funktionen übernehmen soll [8]. Prinzipiell soll hier der Radar über ein Radar Targetsimulator und die Kamera 
über verschiedene Videos auf Bildschirmen angeregt werden. Dieser Testvorgang ist stark limitiert da sich das VUT in 
einem Prüfstandsumgebung befindet und der Test somit nicht unter realen Bedingungen stattfindet. Auch der 
Unterschied zwischen realer Sensorstimulation und simulierter Sensorstimulation kann deutliche Einschränkungen in 
der Aussagekraft der Tests mit sich bringen. 
Die Virtual Vehicle Research GmbH entwickelte den SPIDER (Smart Physical Demonstration and Evaluation Robot) um 
ADAS Funktionen und die Fahrzeugumfeldsensorik zu testen [9]. Der SPIDER ist dabei eine mobile Hardwareplattform, 
die ein zu detektierendes Objekt nachbilden soll. Es besteht lediglich aus einem Gerüst, auf welches wesentliche 
Fahrzeugumfeldsensorik und Steuergeräte montiert sind. Damit sollen Test an neuen Fahrzeugtypen nach dem HiL 
(Hardware in the loop) Prinzip durchgeführt werden, ohne, dass ein gesamter Prototyp aufgebaut werden muss. 
## Behebung bisheriger technischer Probleme / Nachteile
### Probleme/Nachteile
- 
Kraftfahrzeuge werden gesetzlich vorgeschrieben erst nach 3 Jahren (Neufahrzeuge) und dann alle 2 Jahre 
überprüft. Eine Überprüfung der Fahrzeugumfeldsensorik ist dabei nicht verpflichtend. 
- 
Die Eigendiagnose moderner Fahrzeuge ist nicht ausreichend, um die Fahrzeugumfeldsensorik zu testen [6, 
7]. 
- 
Aktuelle Prüfung der Fahrzeugumfeldsensorik nach der FSD [7] erfordert einen Sensordatenzugriff am VUT, 
was die Überprüfung von Serienfahrzeugen ausschließt. 
- 
Aktuelle Prüfung der Fahrzeugumfeldsensorik nach der KÜS [8] testet das VUT in einem Prüfstandsmodus, 
weshalb reale Reaktionen des VUT von den Prüfstandsreaktionen abweichen können. Signale der Sensoren 
müssten getilgt und künstlich erzeugt und an den Sensor zurückgeschickt werden, was selbst zu Fehlern und 
damit falschen Rückschlüssen führen kann. Da für die Fahrzeughersteller keine Sensorhardware 
vorgeschrieben ist, wird die ADAS-Funktionalität bzw. die Umgebungserkennung oft unterschiedlich realisiert. 
Ohne eine definierte Schnittstelle (welche gesetzlich vorzuschreiben wären, was erfahrungsgemäß sehr lange 
dauert) zur IT-Infrastruktur des VUT ist oftmals eine Stimulation der Sensorik nicht möglich. 
- 
Aktuelle Prüfung der Fahrzeugumfeldsensorik nach der Virtual Vehicle Research GmbH [9] benötigt eine 
gesonderte Teststrecke abseits des öffentlichen Straßenverkehrs 
 Aufgrund der stark variierenden Umfeldsensorhardware kann mit den aktuellen Prüfverfahren nicht 
jedes Fahrzeug getestet werden. Die Ergebnisse der Prüfung der Fahrzeuge deren 
Fahrzeugumfeldsensoren mit den aktuellen Prüfverfahren testbar sind, können im Realbetrieb 
abweichen, da zu starke Limitierungen der aktuellen Prüfverfahren vorliegen (Prüfstandsbetrieb, 
Simulation, usw.). Aktuell sind demnach nur ungenaue Aussagen zur Funktionalität der 
Fahrzeugumfeldsensorik möglich. Eindeutige und reale Prüfergebnisse der Fahrzeugumfeldsensorik 
können aktuell nur mit realen Testfahrten abgebildet werden, die enorm zeitaufwändig und mit 
hohen Kosten verbunden sind. Eine genaue Reproduzierbarkeit ist je nach Fahrszenario kaum 
möglich. 
 
 

## Technische Lösung
Abbildung 1 zeigt schematisch den Prüfablauf der Fahrzeugumfeldsensorik unter Einsatz des erfundenen Systems am 
Beispiel einer Kreuzung. Wie zu erkennen ist besteht das Technical Inspection – Road Side System (TI-RSS) aus drei 
Komponenten: Einer Technical Inspection-Road-Side-Unit (TI-RSU), einem Referenzobjekt (RO) und einer Cloud 
Anbindung zur Speicherung und zum Austausch von Daten. 
 
 
Abbildung 1: Schematische Skizze der Erfindung (TI-RSS) in einem Beispielhaften Einsatz an einer Kreuzung 
Die TI-RSU ist hierbei das Herzstück der TI-RSS, da es mit dem zu prüfenden Fahrzeug (VUT) mittels Car-2-X 
Kommunikation (C2X) kommuniziert, das Referenzobjekt steuert und mit der Cloud verbunden ist, um die gewonnen 
Daten zu speichern und zu übertragen. Die TI-RSU baut hierbei auf gewöhnlichen Road-Side-Units (RSU) zur C2X 
Kommunikation auf (z.B. Commsignia [10], Cohda [11]). Für die TI-RSU wird die gewöhnliche RSU jedoch um eine 
eigene Sensorik und einem Steuerungscomputer mit Ethernetschnittstelle erweitert, was nachfolgend detailliert 
erklärt wird. Über die Ethernetschnittstelle wird vom Steuerungscomputer der TI-RSU das Referenzobjekt gesteuert, 
welches vom VUT im Prüfszenario durch dessen Fahrzeugumfeldsensoren detektiert wird. Das Referenzobjekt wird 
ebenfalls nachfolgend detaillierter beschrieben. 
Die Überprüfung der Sensoren der VUT funktioniert mit Hilfe der TI-RSS folgendermaßen: 
Voraussetzung für die Überprüfung der Fahrzeugumfeldsensorik ist, dass das VUT mit der Car-2-X Kommunikation 
ausgestattet ist und die Nachricht Collective Perception Message (CPM) versendet [12]. Die CPM enthält Informationen 
über den Zustand detektierter Objekte in der Umgebung, welche durch dessen Sensorinformationen gewonnen 
wurden. Diese Informationen innerhalb der Nachricht sollen durch das TI-RSS ausgenutzt werden, um die 
Funktionalität der Sensoren des VUT zu überprüfen. Grundprinzip ist somit die Gegenüberstellung zwischen der 
Verkehrssituation, wie sie das VUT über die eigene Sensorik erfasst und der tatsächlichen Verkehrssitiuation (ground 
truth). Somit können auch Sensordekalibration und -degradation detektiert werden, die der Eigendiagnose des VUT 
verborgen bleiben. 
Die prinzipielle Idee ist hierbei, dass das Referenzobjekt durch die Fahrzeugumfeldsensorik des VUT detektiert wird 
und der Zustand des RO durch die CPM des VUT an die TI-RSU geschickt wird. Da die TI-RSU das Referenzobjekt selbst 
steuert und somit dessen Zustand kennt (Ground-Truth) kann die Information vom VUT innerhalb der CPM mit dem 
tatsächlichen Zustand des RO durch die TI-RSU ermittelt werden. Da das VUT den Zustand des Fahrzeugs jedoch aus 
dessen lokalen Koordinatensystems beschreibt, ist für die Überprüfung der Genauigkeit der übermittelten Daten die 
Position und Richtung des VUT notwendig. Dies soll von der TI-RSU durch dessen Sensorik sowie unter Zuhilfenahme 
der Cooperative Awareness Message (CAM) [13] des VUT erfolgen. Durch die Erfindung und unter Ausnutzung der C2X 

Kommunikationsdaten kann somit eine Überprüfung der Fahrzeugumfeldsensorik auf der Straße unter realen 
Bedingungen durchgeführt werden, was einen wesentlichen Unterschied zu den bisherigen Methoden darstellt. Das 
Ergebnis der Prüfung sowie eine Empfehlung für einen Werkstattbesuch oder ein azyklische Hauptuntersuchung für 
eine weiterführende Untersuchung zur Problemlösung soll anschließend an das VUT mittels einer neuen C2X Nachricht 
gesendet werden. Sollte das VUT zu einer Untersuchung der Fahrzeugumfeldsensorik aufgefordert werden, werden die 
Daten ebenfalls an die zuständige Stelle per Cloud weitergeleitet. 
Abbildung 2 zeigt noch einmal detailliert in einem Kontextdiagramm den Informationsaustausch zwischen den 
Entitäten innerhalb des TI-RSS und externen Akteuren (VUT, Stakeholder). 
 
Abbildung 2: Kontextdiagramm der Erfindung. Darstellung der Datenflüsse zwischen den Einzelkomponenten der Erfindung sowie externen 
Akteuren. 
Abbildung 3 illustriert ein mögliches Design des Referenzobjektes. So besteht das Referenzobjekt aus dem Objekt 
selbst, welches mit einer Antriebseinheit auf einer Führungsschiene fährt. In diesem Beispiel ist die Führungsschiene 
als Kreis ausgeführt, um eine zweidimensionale Zustandsänderung der Dynamik und Position zu realisieren. 
 
 
Abbildung 3: Schematische Darstellung des Referenzobjektes. Das Objekt selbst besitzt Eigenschaften, damit es gut und realitätsnah von der 
Fahrzeugumfeldsensorik erkannt wird. Für die Prüfung der Fahrzeugumfeldsensorik bewegt sich das Referenzobjekt mit einer vorgegebenen 
Dynamik, gesteuert von der TI-RSU, auf einer Führungsschiene, welche in diesem Beispiel als Kreis ausgeführt ist. 
Das Objekt kann sich somit mit unterschiedlichen Geschwindigkeiten und Beschleunigungen vom VUT entfernen oder 
annähern sowie nach links oder rechts fahren. Das konkrete Aussehen des Objektes ist aktuell noch nicht im Detail 
spezifiziert. Klar ist jedoch, dass es gewisse Eigenschaften erfüllen muss. So wird das Aussehen derart gestaltet sein, 
dass es für die drei Hauptarten von Fahrzeugumfeldsensoren (Kamera, Radar, Lidar) gut und realitätsnah zu detektieren 
ist. Beispielsweise sollte der Reflexionsgrad des Referenzobjektes, dem eines Autos entsprechen, falls das 
Referenzobjekt ein Auto darstellen soll. Analog gilt dies für die Darstellung anderer Verkehrsteilnehmer (LKW, 
Fußgänger). Des Weiteren kann das Objekt selbst die Form und das Aussehen eines Fahrzeuges haben oder dies wird 

durch Bildschirme auf dem Objekt impliziert. Insgesamt ist es das Ziel eine gute Sichtbarkeit durch die 
Fahrzeugumfeldsensorik zu gewährleisten sowie möglichst alle Parameter der CPM anzusprechen, um möglichst viele 
Daten für die Beurteilung der Funktionalität der Sensoren verwenden zu können. 
Abbildung 4 zeigt abschließend die Komponenten der Technical Inspection-Road-Side-Unit. Diese besteht aus einer 
klassischen C2X-Road-Side-Unit zur Realisierung der C2X Kommunikation, einem Steuerungscomputer für das 
Referenzobjekt sowie eigener Sensorik zur Positionsbestimmung des VUT. Da lediglich die Position und Fahrtrichtung 
des VUT bekannt sein muss zum Zeitpunkt des Tests, ist die Verwendung von Radar und/oder LiDAR Sensoren 
ausreichend. 
 
Abbildung 4: Schematische Darstellung der Komponenten der TI-RSU 
### Vorteile gegenüber dem aktuellen Stand der Technik
- 
Aperiodisches Überprüfen möglich 
- 
Reale Prüfumgebung, kein Prüfstandsmodus 
- 
Prüfung im Staßenverkehr (z.B. an Ampelanlage) oder auf separater Prüfstrecke möglich 
- 
Überprüfung von Serienfahrzeugen möglich ohne Eingriff ins VUT 
- 
Aufbauend auf bestehender Technologie (C2X Kommunikation) 
- 
Informationen in der C2X Nachricht lassen direkt Rückschluss über Grad der Funktionalität zu (keine, leichte 
oder große Abweichungen von Ground Truth) 
- 
Modularer Aufbau, der in Verbindung mit bestehenden Verkehrsüberwachungssystemen der
Straßenverkehrsinfrastruktur(z.B. Toll Collect, fest installierten Enforcement-Anlagen: Geschwindigkeits-, 
Abstands- oder Rotlichtüberwachungsanlagen, sowie Verkehrsdichtemessgeräten usw.) eingesetzt werden, 
um diese mit der C2X-Technologie zu vernetzen. In diesem Zusammenhang können, je nach Qualität der Daten 
und Einsatzzweck, die Messdaten der bestehenden Verkehrsüberwachungssysteme als Ground Truth 
verwendet bzw. vize versa Daten validiert und verifiziert werden. 
- 
Bei entsprechender Sensorikausstattung der Verkehrsinfrastruktur kann im modularen Ansatz auch auf das 
Referenzobjekt verzichtet werden. Grundsätzlich können bei ausreichender Marktdurchdringung der 
Fahrzeuge mit C2X in diesem Setting auch teuere Enforcement-Anlagen („Blitzer“) teilweise durch den viel 
günstigeren TI-RSU-Ansatz ersetzt werden. 
Das wesentliche Neue an der Erfindung ist, dass die Prüfung der Funktionalität der Fahrzeugumfeldsensorik nicht unter 
Laborbedingungen und simulierten Signalen, sondern direkt auf der Straße durch Ausnutzung der C2X Kommunikation 
funktioniert. Hierfür wird ein neuartiges System vorgestellt, welches den Input über das Design und die Dynamik des 
Referenzobjektes steuert und den Output des Fahrzeugs über die CPM überprüft. Das allgemeine Verfahren und das 
konkrete System TI-RSS stellen einen komplett neuen Ansatz zur technischen Überprüfung der Funktionalität der 
Fahrzeugumfeldsensorik dar. Die Hauptkomponenten (TI-RSU und RO) des TI-RSS sind in dieser Form noch nicht auf 
dem Markt zu finden und stellen deshalb ebenfalls komplett neuartige Produkte dar.  
Das TI-RSS kann ebenfalls bei der HU eingesetzt werden. Die Integration dieses Systems in die gesetzlich 
vorgeschriebene HU würde einen enormen Markt erschließen (ca. 40mio HUs pro Jahr). Das System kann darüber 
hinaus bestehende, sehr teure Verkehrsüberwachungsanlagen (Blitzer, Verkehrszählungen, usw.) ersetzen. 
Informationen wie bspw. die Geschwindigkeit der vorbeifahrenden Fahrzeuge kann mit dem System direkt erfasst 
werden. Für diesen Anwendungsfall wären alle Kommunen potenzielle Abnehmer, was einen enormen Markt darstellt. 
Blitzgeräte allein gibt es in Deutschland mehr als 4.600 [14]. Blitzgeräte können zwischen 65.000 bis 250.000 € kosten 
[15], das System hingegen kann rein für die “Blitzerfunktion” mit 10.000 bis 20.000 € (geschätzt) aufgebaut werden.  

## Literaturverzeichnis
[1] SAE INTERNATIONAL: SAE J3016 LEVELS OF DRIVING AUTOMATION. URL 
https://www.sae.org/standards/content/j3016_202104/ Accessed: 2022-01-26  
[2] BUNDESAMT FÜR JUSTIZ: VERORDNUNG (EU) 2018/858 DES EUROPÄISCHEN PARLAMENTS UND DES RATES , 2018-
05-30. URL https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32018R0858 Accessed: 2023-11-23  
[3] AUDI AG: Audi Inspektion und Audi Wartungskonzept. URL https://www.audi-zentrum-
duisburg.audi/de/angebote/service/inspektion.html Accessed: 2023-11-24  
[4] DAT: Anzahl der Wartungsarbeiten an Personenkraftwagen in Deutschland von 2010 bis 2020 : (pro Pkw). URL 
https://de.statista.com/statistik/daten/studie/37145/umfrage/haeufigkeit-von-wartungsarbeit-bei-pkw/ 
Accessed: 2023-11-24  
[5] BUNDESAMT FÜR JUSTIZ: Straßenverkehrs-Zulassungs-Ordnung (StVZO) , 2012-04-26. URL https://www.gesetze-im-
internet.de/stvzo_2012/BJNR067910012.html Accessed: 2023-11-22  
[6] MANN, Clemens: Untersuchungen zur Prüfung von kamerabasierten Fahrerassistenzsystemen im Rahmen der 
Hauptuntersuchung. Zwickau, Hochschule Zwikau, Fakultät Kraftfahrzeugtechnik. Diplomarbeit. 01.2019 
Accessed: 2023-07-06. Supervisor: 
[7] STOLLER, André ; LOTZE, Martin ; BAHNERT, Christoph ; AUERSWALD, Rico ; ZÄPER, Andreas ; RICHTER, Robert ; 
ENGELBERT, André ; UNGER, Thomas ; BALZER, Paul: ErVast - Einsatz dynamischer Verkehrselemente für die Prüfung 
automatisierter Fahrfunktionen : Schlussbericht des Verbundes : AVF - automatisiertes und vernetztes Fahren 
(BMDV) : Laufzeit des Vorhabens: von: 01.01.2020 bis: 31.12.2021. In: ErVast - Einsatz dynamischer 
Verkehrselemente für die Prüfung automatisierter Fahrfunktionen , 2022  
[8] KÜS: Fahrerassistenzsysteme regelmäßig auf den Prüfstand : Regelmäßige Prüfungen als Schlüssel für 
dauerhafte Fahrzeugsicherheit. In: dSpace MAGAZIN, 2/2023, pp. 56–61  
[9] VIRTUAL VEHICLE RESEARCH GMBH: SPIDER : A MOBILE HIL PLATFORM FOR FAST, FLEXIBLE REPRODUCIBLE ADAS OR 
SENSOR TESTS. URL https://www.v2c2.at/spider/ Accessed: 2023-11-25  
[10] COMMSIGNIA LTD.: High performance V2X enabled roadside unit with edge computing. URL 
https://www.commsignia.com/products/rsu/ Accessed: 2023-11-25  
[11] COHDA WIRELESS: MK6 RSU. URL https://www.cohdawireless.com/solutions/hardware/mk6-rsu/ Accessed: 2023-
11-25  
[12] ETSI (Hrsg.): ETSI TR 103 562 : Intelligent Transport Systems (ITS); Vehicular Communications; Basic Set of 
Applications; Analysis of the Collective Perception Service (CPS); Release 2. V2.1.1. 2019  
[13] ETSI (Hrsg.): ETSI EN 302 637-2 : Intelligent Transport Systems (ITS); Vehicular Communications; Basic Set of 
Applications; Part 2: Specification of Cooperative Awareness Basic Service. Final Draft: V1.3.1. 2014. URL 
https://www.etsi.org/deliver/etsi_en/302600_302699/30263702/01.03.01_30/en_30263702v010301v.pdf  
[14] SCDB.INFO: Ranking der europäischen Staaten mit den meisten fest installierten Blitzgeräten im Straßenverkehr. 
URL https://de.statista.com/statistik/daten/studie/3514/umfrage/anzahl-der-fest-installierten-blitzer-in-
ausgewaehlten-laendern-europas/ Accessed: 2023-11-27  
[15] AHN, P.: Stationäre Blitzer zur Geschwindigkeitskontrolle und Unfallprävention. URL 
https://www.bussgeldkatalog.net/blitzer/stationaere-blitzer Accessed: 2023-11-27