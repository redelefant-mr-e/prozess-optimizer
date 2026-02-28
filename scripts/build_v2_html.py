#!/usr/bin/env python3
"""
Build V2 HTML apps from V2-Export markdown files.
Outputs wizard-style HTML in V1 format (wizard-block-action, wizard-block-info, etc.).
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
V2_EXPORT = PROJECT_ROOT / "V2-Export"
V2_HTML = PROJECT_ROOT / "V2-HTML"
SHARED_CSS = "../shared/design-templates/step-wizard/step-wizard.css"
INDEX_PATH = "../index.html"

# Block type mapping: (pattern, block_class, block_label)
BLOCK_RULES = [
    (r"Wichtige Grenze", "wizard-block limitations", None),
    (r"^Deine Aufgabe$", "wizard-block wizard-block-action", "Deine Aufgabe"),
    (r"^So gehst du vor", "wizard-block wizard-block-action", "Deine Aufgabe"),
    (r"^Beispiele? für", "wizard-block wizard-block-example", "Beispiel"),
    (r"^Beispiel", "wizard-block wizard-block-example", "Beispiel"),
    (r"^Tipp", "wizard-block wizard-block-tip", "Tipp"),
    (r"^Du bringst in den nächsten Schritt mit", "wizard-block handoff", None),
    (r"^Wenn du hier festhängst", "wizard-block handoff", None),
    (r"^Kurzüberblick", "wizard-block wizard-block-info", None),
    (r"^Was dieser Guide macht", "wizard-block wizard-block-info", None),
    (r"^Typische Stolpersteine", "wizard-block wizard-block-info", None),
    (r"^Saubere Erfindungsbeschreibung", "wizard-block wizard-block-info", None),
    (r"^Kernbegriffe", "wizard-block wizard-block-info", None),
    (r"^Standard-Gliederung", "wizard-block wizard-block-info", None),
    (r"^Wichtige Regel", "wizard-block wizard-block-info", None),
    (r"^Komponenten und Ablauf", "wizard-block wizard-block-info", None),
    (r"^Inhaltliche Checkliste", "wizard-block wizard-block-info", None),
    (r"^Was vermeiden", "wizard-block wizard-block-info", None),
    (r"^Selbsttest", "wizard-block wizard-block-info", None),
    (r"^Zusammenfassung", "wizard-block wizard-block-info", None),
    (r"^Deine Rohfassung", "wizard-block wizard-block-info", None),
    (r"^TTO-Formular finden", "wizard-block wizard-block-info", None),
    (r"^Nächste Aktion", "wizard-block wizard-block-info", None),
    (r"^Zeitfenster beachten", "wizard-block wizard-block-info", None),
    (r"^Deine Mitwirkung", "wizard-block wizard-block-info", None),
    (r"^Wichtige Meilensteine", "wizard-block wizard-block-info", None),
    (r"^Prioritätsjahr", "wizard-block wizard-block-info", None),
    (r"^Nachanmeldung", "wizard-block wizard-block-info", None),
    (r"^Was ist die PCT", "wizard-block wizard-block-info", None),
    (r"^Unser Ansatz", "wizard-block wizard-block-info", None),
    (r"^Warum dieser Check", "wizard-block wizard-block-info", None),
    (r"^Was ist eine Erfindung\?", "wizard-block wizard-block-info", None),
    (r"^Erfindung der Universität melden", "wizard-block wizard-block-info", None),
    (r"^Was passiert dann", "wizard-block wizard-block-info", None),
    (r"^Patentanmeldung und Publikation", "wizard-block wizard-block-info", None),
    (r"^Typische Situationen", "wizard-block wizard-block-info", None),
    (r"^Umfang", "wizard-block wizard-block-info", None),
    (r"^Formel", "wizard-block wizard-block-action", None),
    (r"^So geht's weiter", "wizard-block handoff", None),
]


def _inline(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    def link_repl(m):
        url = m.group(2)
        if url.endswith(".md"):
            url = url.replace(".md", ".html").replace("Erfindungsbeschreibung-V2", "erfindungsbeschreibung-v2").replace("Patentierungsprozess-V2", "patentierungsprozess-v2")
        return f'<a href="{url}">{m.group(1)}</a>'
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, s)
    return s


def _md_to_html(chunk: str) -> str:
    """Convert markdown chunk to HTML (tables, lists, paragraphs)."""
    lines = chunk.strip().split("\n")
    out = []
    in_table = False
    in_list = False
    list_type = "ul"
    table_row_count = 0

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            if in_table:
                out.append("</tbody></table></div>")
                in_table = False
            if in_list:
                out.append(f"</{list_type}>")
                in_list = False
            i += 1
            continue

        # Blockquote (Wichtige Grenze)
        if stripped.startswith(">") or (stripped == ">"):
            block_lines = []
            while i < len(lines):
                ln = lines[i].strip()
                if ln.startswith(">"):
                    block_lines.append(ln[1:].strip() if len(ln) > 1 else "")
                    i += 1
                else:
                    break
            parts = [b for b in block_lines if b]
            if parts:
                p_parts = []
                ul_parts = []
                for p in parts:
                    if p.startswith("- "):
                        ul_parts.append(f"<li>{_inline(p[2:])}</li>")
                    else:
                        p_parts.append(f"<p>{_inline(p)}</p>")
                body = "".join(p_parts)
                if ul_parts:
                    body += f"<ul>{''.join(ul_parts)}</ul>"
                out.append(body)
            continue

        # Table
        if stripped.startswith("|") and "|" in stripped:
            if re.match(r"^\|[\s\-:|]+\|$", stripped):
                i += 1
                continue
            if not in_table:
                out.append('<div class="wizard-table-wrap"><table class="wizard-table"><tbody>')
                in_table = True
                table_row_count = 0
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if any(c for c in cells):
                table_row_count += 1
                tag = "th" if table_row_count == 1 else "td"
                out.append("<tr>" + "".join(f"<{tag}>{_inline(c)}</{tag}>" for c in cells) + "</tr>")
            i += 1
            continue

        if in_table:
            out.append("</tbody></table></div>")
            in_table = False

        # List
        if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            lt = "ol" if re.match(r"^\d+\.\s+", stripped) else "ul"
            if not in_list or list_type != lt:
                if in_list:
                    out.append(f"</{list_type}>")
                out.append(f"<{lt}>")
                in_list = True
                list_type = lt
            text = re.sub(r"^[-*]\s+", "", stripped) or re.sub(r"^\d+\.\s+", "", stripped)
            out.append(f"<li>{_inline(text)}</li>")
            i += 1
            continue

        if stripped.startswith("- [ ]"):
            if not in_list or list_type != "ul":
                if in_list:
                    out.append(f"</{list_type}>")
                out.append("<ul>")
                in_list = True
                list_type = "ul"
            out.append(f"<li>{_inline(stripped[5:].strip())}</li>")
            i += 1
            continue

        if in_list:
            out.append(f"</{list_type}>")
            in_list = False

        # Horizontal rule
        if stripped in ("---", "***", "___"):
            i += 1
            continue
        # H3 / H4
        if stripped.startswith("### "):
            out.append(f"<h3>{_inline(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            out.append(f"<h3>{_inline(stripped[3:])}</h3>")
        elif stripped.startswith("# "):
            out.append(f"<h3>{_inline(stripped[2:])}</h3>")
        # Paragraph
        else:
            out.append(f"<p>{_inline(stripped)}</p>")
        i += 1

    if in_table:
        out.append("</tbody></table></div>")
    if in_list:
        out.append(f"</{list_type}>")

    return "\n".join(out)


def _parse_step_sections(content: str) -> list[tuple[str, str, str]]:
    """Parse step content into (block_type, block_label, html_content) tuples."""
    sections = []
    current_type = "wizard-block wizard-block-info"
    current_label = None
    current_lines = []

    def flush():
        nonlocal current_lines, current_label, current_type
        if not current_lines:
            return
        text = "\n".join(current_lines).strip()
        if not text:
            return
        html = _md_to_html(text)
        if html.strip():
            sections.append((current_type, current_label, html))
        current_lines = []
        current_label = None
        current_type = "wizard-block wizard-block-info"

    for line in content.split("\n"):
        stripped = line.strip()
        # Strip ## or ### for pattern matching
        check_line = re.sub(r"^#+\s*", "", stripped).strip()
        matched = False
        for pattern, block_type, label in BLOCK_RULES:
            if re.search(pattern, check_line, re.IGNORECASE):
                flush()
                current_type = block_type
                current_label = label
                if label:
                    current_lines = []
                else:
                    current_lines = [stripped]
                matched = True
                break
        if not matched and stripped:
            current_lines.append(line)

    flush()
    return sections


def _extract_steps(md: str) -> tuple[str, list[tuple[str, str]]]:
    """Extract (entry_text, [(step_title, step_content), ...]) from markdown."""
    # Split by # Schritt N: - re.split with capture returns [before, cap1, between, cap2, between, ...]
    parts = re.split(r"\n# Schritt (\d+): ", md)
    if len(parts) < 2:
        return "", [("Einleitung", md)]

    entry = parts[0].strip()
    if "---" in entry:
        entry = entry.split("---")[0].strip()

    step_list = []
    i = 1
    while i + 1 < len(parts):
        num, block = parts[i], parts[i + 1]
        lines = block.strip().split("\n")
        title = lines[0].strip() if lines else ""
        content = "\n".join(lines[1:]).strip() if len(lines) > 1 else ""
        # Remove "---" at end of content (separator before next step)
        content = re.sub(r"\n---\s*$", "", content)
        step_list.append((f"Schritt {num}: {title}", content))
        i += 2

    return entry, step_list


def _build_step_html(step_title: str, step_content: str) -> str:
    """Build HTML for one step."""
    sections = _parse_step_sections(step_content)
    blocks = []
    for block_type, label, html in sections:
        label_html = f'<span class="block-label">{label}</span>\n' if label else ""
        blocks.append(f'<div class="{block_type}">\n{label_html}{html}\n</div>')
    return "\n\n".join(blocks)


def build_single_html(
    md_path: Path,
    output_path: Path,
    title: str,
    subtitle: str,
    css_path: str = SHARED_CSS,
    index_path: str = INDEX_PATH,
) -> None:
    """Build one HTML file from markdown."""
    md = md_path.read_text(encoding="utf-8")
    entry, steps = _extract_steps(md)

    # Stepper labels
    stepper_labels = []
    for i, (stitle, _) in enumerate(steps):
        short = stitle.split(": ")[-1][:18] + ("…" if len(stitle.split(": ")[-1]) > 18 else "")
        stepper_labels.append(short)

    step_html_parts = []
    for i, (step_title, step_content) in enumerate(steps):
        is_last = i == len(steps) - 1
        blocks_html = _build_step_html(step_title, step_content)

        nav_html = ""
        if i == 0:
            nav_html = '<button type="button" class="wizard-btn wizard-btn-primary" data-wizard-next>Weiter</button>'
        else:
            nav_html = '<button type="button" class="wizard-btn wizard-btn-secondary" data-wizard-prev>Zurück</button>'
            if not is_last:
                nav_html += '\n        <button type="button" class="wizard-btn wizard-btn-primary" data-wizard-next>Weiter</button>'

        step_label = f"Schritt {i}" if i > 0 else "Schritt 0"
        display_title = step_title.replace("Schritt 0: ", "").replace("Schritt 1: ", "").replace("Schritt 2: ", "").replace("Schritt 3: ", "").replace("Schritt 4: ", "").replace("Schritt 5: ", "").replace("Schritt 6: ", "")

        step_html_parts.append(f'''
    <div class="wizard-step {"active" if i == 0 else ""}" data-step="{i}">
      <p class="wizard-step-label">{step_label}</p>
      <h2 class="wizard-step-title">{display_title}</h2>
      {blocks_html}
      <div class="wizard-nav">
        {nav_html}
      </div>
    </div>''')

    total_steps = len(steps)
    stepper_html = "\n      ".join(f'<span data-stepper="{i}">{stepper_labels[i]}</span>' for i in range(total_steps))

    html = f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_path}">
</head>
<body>

<div class="wizard-app" id="wizard">
  <div class="wizard-container">
    <header style="margin-bottom: 1rem;">
      <p style="margin: 0 0 0.5rem;"><a href="{index_path}" class="wizard-back-link">← Zurück zur Übersicht</a></p>
      <h1 style="margin: 0 0 0.25rem;">{title}</h1>
      <p class="wizard-subtitle" style="margin: 0;">{subtitle}</p>
    </header>

    <div class="wizard-stepper" id="stepper">
      {stepper_html}
    </div>

    <div class="wizard-progress">
      <div class="wizard-progress-bar">
        <div class="wizard-progress-fill" style="width: {100/total_steps if total_steps else 14}%;"></div>
      </div>
      <span class="wizard-progress-text" id="progressText">Schritt 1 von {total_steps}</span>
    </div>

{"".join(step_html_parts)}
  </div>
</div>

<script src="../shared/design-templates/step-wizard/step-wizard.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', function() {{
    var wizard = document.getElementById('wizard');
    var stepper = document.getElementById('stepper');
    if (typeof initStepWizard === 'function') {{
      function updateStepper(step) {{
        if (!stepper) return;
        var spans = stepper.querySelectorAll('[data-stepper]');
        spans.forEach(function(s, idx) {{
          s.classList.remove('active', 'done');
          if (idx === step) s.classList.add('active');
          else if (idx < step) s.classList.add('done');
        }});
      }}
      initStepWizard(wizard, {{
        startAt: 0,
        onStepChange: function(index) {{
          updateStepper(index);
          var pt = document.getElementById('progressText');
          if (pt) pt.textContent = 'Schritt ' + (index + 1) + ' von {total_steps}';
        }}
      }});
    }}
  }});
</script>
</body>
</html>'''

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"Wrote {output_path}")


def main():
    V2_HTML.mkdir(parents=True, exist_ok=True)

    configs = [
        (
            V2_EXPORT / "Was-ist-eine-Erfindung-V2.md",
            V2_HTML / "was-ist-eine-erfindung-v2.html",
            "Was ist eine Erfindung?",
            "Orientierung: Habe ich eine Erfindung? Was jetzt? Wann publizieren?",
        ),
        (
            V2_EXPORT / "Erfindungsbeschreibung-V2.md",
            V2_HTML / "erfindungsbeschreibung-v2.html",
            "Erfindungsbeschreibung",
            "Deine Erfindung korrekt dokumentieren – für TTO-Formulare",
        ),
        (
            V2_EXPORT / "Patentierungsprozess-V2.md",
            V2_HTML / "patentierungsprozess-v2.html",
            "Patentierungsprozess",
            "Was passiert nach der Erfindungsmeldung? Ausarbeitung, Prioritätsjahr, PCT",
        ),
    ]

    for md_path, out_path, title, subtitle in configs:
        if md_path.exists():
            build_single_html(md_path, out_path, title, subtitle, css_path="../shared/design-templates/step-wizard/step-wizard.css", index_path="../index.html")
        else:
            print(f"Skip (not found): {md_path}")

    # V2 index page
    index_html = f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>V2 Guides – Kundenüberarbeitete Prozesse</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../shared/design-templates/step-wizard/step-wizard.css">
</head>
<body>
  <div class="wizard-app">
    <div class="wizard-container">
      <header style="margin-bottom: 1rem;">
        <p style="margin: 0 0 0.5rem;"><a href="../index.html" class="wizard-back-link">← Zurück zur Übersicht</a></p>
        <h1 style="margin: 0 0 0.25rem;">V2 Guides</h1>
        <p class="wizard-subtitle" style="margin: 0;">Kundenüberarbeitete Prozess-Guides</p>
      </header>

      <div class="wizard-block wizard-block-action">
        <h3>Was ist eine Erfindung?</h3>
        <p>Orientierung: Habe ich eine Erfindung? Was jetzt? Warum schnell? Wann publizieren?</p>
        <p style="margin-top: 1rem;"><a href="was-ist-eine-erfindung-v2.html" class="wizard-btn wizard-btn-primary">Guide starten</a></p>
      </div>

      <div class="wizard-block wizard-block-action">
        <h3>Erfindungsbeschreibung</h3>
        <p>6 Schritte: Kern, Stand der Technik, Technische Lösung, Struktur, Fehler vermeiden, Ergebnis.</p>
        <p style="margin-top: 1rem;"><a href="erfindungsbeschreibung-v2.html" class="wizard-btn wizard-btn-primary">Guide starten</a></p>
      </div>

      <div class="wizard-block wizard-block-action">
        <h3>Patentierungsprozess</h3>
        <p>Ausarbeitung der Anmeldung, Nach der Einreichung (Prioritätsjahr, PCT).</p>
        <p style="margin-top: 1rem;"><a href="patentierungsprozess-v2.html" class="wizard-btn wizard-btn-primary">Guide starten</a></p>
      </div>
    </div>
  </div>
</body>
</html>'''
    (V2_HTML / "index.html").write_text(index_html, encoding="utf-8")
    print(f"Wrote {V2_HTML / 'index.html'}")


if __name__ == "__main__":
    main()
