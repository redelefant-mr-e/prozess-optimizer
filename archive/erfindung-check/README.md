# Optimierte Prozess-Varianten

Diese Varianten wurden von der **AI Process Optimization Machine** erzeugt.

## Pipeline

1. **Phase 1:** AI generiert optimierte Version – nutzt PROCESS-SCAFFOLD, USER-PERSONA, PROCESS-QUALITY-GRADE
2. **Phase 2:** AI prüft und verfeinert die Phase-1-Ausgabe

## Ordner

| Ordner | Inhalt |
|--------|--------|
| `draft/` | Phase-1-Output (erste Optimierung) |
| `refined/` | Phase-2-Output (geprüft und verfeinert) |
| `phase1_raw.md` | Vollständige Phase-1-Antwort |
| `phase2_raw.md` | Vollständige Phase-2-Antwort |

## Änderungen (refined)

- **8 → 7 Schritte:** Patente + Publikationen zu „Prior Art suchen“ zusammengeführt
- **Risikohinweis** in der Einleitung ergänzt
- **Input-Output-Handoffs** klarer formuliert
- **Tipps** konkreter und handlungsorientierter

## Erneut ausführen

```bash
cd /Users/felixegidi/Desktop/Cursor/Process-Optimizer
python3 optimize_process.py
```
