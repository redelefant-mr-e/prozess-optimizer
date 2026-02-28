# Erfindung-Check – Arbeitsdokumente

Dieser Ordner enthält die exportierten Arbeitsdokumente des Erfindung-Checks, erzeugt aus der Webversion.

## Dateien

- **00-Einleitung.md** bis **06-Ergebnis-ableiten.md** – Ein Markdown-Dokument pro Prozessschritt
- **Erfindung-Check-Vollstaendig.md** – Alle Schritte in einer Datei zusammengeführt
- **Erfindung-Check-Notion.md** – Notion-optimierte Version (ohne interne Links), zum direkten Einfügen in Notion
- **Erfindung-Check.docx** – Vollständiges Word-Dokument für die Bearbeitung

## Aktualisierung

Nach Änderungen an der Webversion (`optimized/ui/erfindung-check.html`) die Arbeitsdokumente neu erzeugen:

```bash
# Von Projektroot aus:
python3 modules/erfindung-check/scripts/html_to_markdown.py

# Oder aus dem Modulordner:
cd modules/erfindung-check
python3 scripts/html_to_markdown.py
```

Das Script erzeugt alle Markdown-Dateien und das Word-Dokument neu und überschreibt die bestehenden Dateien.

## Abhängigkeiten

- `beautifulsoup4` – HTML-Parsing
- `python-docx` – Word-Export

Installation: `pip install beautifulsoup4 python-docx`
