"""Build the static study hub from the repository's canonical content."""
from pathlib import Path
import html
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = json.loads((ROOT / "content/questions.json").read_text(encoding="utf-8"))
CHAPTERS = DATA["chapters"]
REPO = "https://github.com/anjithU/Technical-Drawing-in-Mechanical-Eng"
esc = html.escape


def page(title, body, active):
    nav = "".join(f'<a {"aria-current=page" if key == active else ""} href="{url}">{label}</a>'
                  for key, url, label in [("home", "index.html", "Overview"),
                  ("viewer", "viewer.html", "3D studio"),
                  ("questions", "questions.html", "Questions & answers"),
                  ("drawings", "drawings.html", "Drawings")])
    return f'''<!doctype html>
<html lang="en" data-theme="dark"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Variant 14 engineering graphics: interactive models, drawing sheets and 66 study questions with answers.">
<title>{esc(title)} · Engineering Graphics</title><link rel="stylesheet" href="assets/site.css">
<script src="assets/site.js" defer></script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header><a class="brand" href="index.html"><span class="monogram">14</span><span>Engineering Graphics<small>MECHANICAL DRAWING STUDY LAB</small></span></a>
<nav aria-label="Main navigation">{nav}</nav><button id="theme" type="button" aria-label="Switch to light theme">Light theme</button></header>
<main id="main">{body}</main>
<footer><span>Variant 14 · Technical Drawing in Mechanical Engineering</span><a href="{REPO}">Source on GitHub ↗</a><p>Study and review material. Proposed dimensions require instructor agreement; Exercise 1a is provisional.</p></footer>
</body></html>'''


def build():
    DOCS.mkdir(exist_ok=True)
    download = DOCS / "downloads"
    download.mkdir(exist_ok=True)
    drawing_root = ROOT / "drawings/number-14"
    for folder in ("pdf", "svg"):
        shutil.copytree(drawing_root / folder, download / folder, dirs_exist_ok=True)
    for name in ("Variant_14_All_12_Drawings.pdf", "Variant_14_Calculations_and_Assumptions.pdf"):
        shutil.copy2(drawing_root / name, download / name)
    with zipfile.ZipFile(download / "Variant_14_Study_Drawings.zip", "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(drawing_root.rglob("*")):
            if path.is_file() and "qa" not in path.parts:
                bundle.write(path, path.relative_to(drawing_root))

    cards = "".join(f'''<a class="exercise" href="questions.html#exercise-{c['exercise']}"><span class="exercise-number">{c['exercise'].upper()}</span><div><h3>{esc(c['title'])}</h3><p>{len(c['questions'])} study questions · PDF + SVG</p></div><span aria-hidden="true">↗</span></a>''' for c in CHAPTERS)
    home = f'''<section class="hero"><div><p class="eyebrow">VARIANT 14 / ENGINEERING GRAPHICS</p><h1>Understand the shape.<br><span>Read the drawing.</span></h1><p class="lead">Explore mechanical components in 3D, connect each view to its drawing, and prepare with focused questions and answers.</p><div class="actions"><a class="button primary" href="viewer.html">Launch 3D studio ↗</a><a class="button" href="questions.html">Study the questions</a></div><div class="stats"><span><b>12</b> exercises</span><span><b>66</b> questions & answers</span><span><b>A3</b> drawing sheets</span></div></div><div class="blueprint" aria-label="Stylized orthographic drawing of a stepped shaft" role="img"><div class="cross horizontal"></div><div class="cross vertical"></div><div class="shaft"><i></i><i></i><i></i><i></i><i></i></div><div class="dimension">VARIANT 14 · SECTION / PROJECTION / ASSEMBLY</div><span class="drawing-label">ENGINEERING GRAPHICS STUDIO</span></div></section>
<section class="intro"><p class="eyebrow">FROM GEOMETRY TO UNDERSTANDING</p><h2>One study space, three ways to learn.</h2><div class="features"><article><span>01 / EXPLORE</span><h3>Interactive models</h3><p>Orbit, zoom, switch camera views and inspect sections. Move through assembly stages in dark or light mode.</p><a href="viewer.html">Open the studio →</a></article><article><span>02 / EXPLAIN</span><h3>Questions & answers</h3><p>Work through the assessment topics, then reveal clear explanations to check your understanding.</p><a href="questions.html">Review 66 questions →</a></article><article><span>03 / REVIEW</span><h3>Drawing collection</h3><p>Inspect twelve A3 sheets, edit the SVGs, and follow the adopted dimensions in the calculation notes.</p><a href="drawings.html">Browse the drawings →</a></article></div></section>
<section><div class="section-heading"><div><p class="eyebrow">THE COMPLETE COLLECTION</p><h2>Choose an exercise.</h2></div><a href="drawings.html">Download drawing set →</a></div><div class="exercise-grid">{cards}</div></section>
<aside class="notice"><strong>Review draft</strong><p>Unspecified dimensions and annotations are proposed values. Exercise 1a is a provisional reconstruction. Confirm these with your instructor before submission.</p></aside>'''
    (DOCS / "index.html").write_text(page("Study hub", home, "home"), encoding="utf-8")

    sections = []
    markdown = ["# Questions & answers · Variant 14", "", "66 assessment questions paired with authored study explanations. These are not an official answer key. Original questions are attributed to the course instructions linked in each section.", ""]
    for c in CHAPTERS:
        ex = c["exercise"]
        items = "".join(f'<details class="question" id="q-{q["id"]}"><summary><span>{i:02}</span>{esc(q["question"])}</summary><div class="answer"><p>{esc(q["answer"])}</p></div></details>' for i, q in enumerate(c["questions"], 1))
        sections.append(f'<section class="chapter" id="exercise-{ex}" data-chapter="{ex}"><p class="eyebrow">EXERCISE {ex.upper()}</p><h2>{esc(c["title"])}</h2><p class="chapter-links"><a href="downloads/pdf/Exercise_{ex}_Variant_14.pdf">Drawing PDF ↗</a> · <a href="{REPO}/blob/main/source/instructions/{c["source"]}">Original instructions ↗</a></p>{items}</section>')
        markdown += [f'## Exercise {ex} — {c["title"]}', "", f'[Original instructions](../source/instructions/{c["source"]}) · [Drawing PDF](../drawings/number-14/pdf/Exercise_{ex}_Variant_14.pdf)', ""]
        for i, q in enumerate(c["questions"], 1):
            markdown += [f'### {i}. {q["question"]}', "", q["answer"], ""]
    options = "".join(f'<option value="{c["exercise"]}">{c["exercise"]} — {esc(c["title"])}</option>' for c in CHAPTERS)
    body = f'''<section class="page-heading"><p class="eyebrow">RECALL / REASON / EXPLAIN</p><h1>Questions & answers</h1><p class="lead">Try answering first. Open each question to compare your reasoning with the study explanation.</p></section><div class="filters"><label>Search questions and answers<input id="search" type="search" placeholder="e.g. section, tolerance, thread"></label><label>Exercise<select id="exercise"><option value="all">All 12 exercises</option>{options}</select></label><button id="expand" type="button">Expand visible answers</button></div><p id="results" role="status" aria-live="polite">66 questions</p><p class="empty" id="empty" hidden>No matching questions. Try another term or exercise.</p>{''.join(sections)}'''
    (DOCS / "questions.html").write_text(page("Questions & answers", body, "questions"), encoding="utf-8")
    (ROOT / "study/questions-and-answers.md").write_text("\n".join(markdown), encoding="utf-8")

    rows = "".join(f'<tr><td><b>{c["exercise"]}</b></td><td>{esc(c["title"])}</td><td><a href="downloads/pdf/Exercise_{c["exercise"]}_Variant_14.pdf">PDF ↗</a></td><td><a href="downloads/svg/Exercise_{c["exercise"]}_Variant_14.svg" download>SVG ↓</a></td><td><a href="questions.html#exercise-{c["exercise"]}">Study →</a></td></tr>' for c in CHAPTERS)
    body = f'''<section class="page-heading"><p class="eyebrow">PRINT / INSPECT / EDIT</p><h1>The drawing collection</h1><p class="lead">Twelve A3 sheets, editable vectors, and the calculations behind the proposed geometry.</p><div class="actions"><a class="button primary" href="downloads/Variant_14_All_12_Drawings.pdf">All 12 drawings · PDF ↗</a><a class="button" href="downloads/Variant_14_Study_Drawings.zip" download>Complete drawing bundle ↓</a><a class="button" href="downloads/Variant_14_Calculations_and_Assumptions.pdf">Calculations & assumptions ↗</a></div></section><aside class="notice"><strong>Before printing or submitting</strong><p>Print at actual size / 100% on A3. Exercise 4 uses a 2:1 main view; local detail scales are labelled. All dimensions indicate actual millimetres. Proposed values need instructor agreement, and Exercise 1a remains provisional.</p></aside><div class="table-wrap"><table><thead><tr><th>Exercise</th><th>Subject</th><th>Drawing</th><th>Editable</th><th>Questions</th></tr></thead><tbody>{rows}</tbody></table></div>'''
    (DOCS / "drawings.html").write_text(page("Drawing collection", body, "drawings"), encoding="utf-8")
    template = (ROOT / "src/viewer-shell.template.html").read_text(encoding="utf-8")
    fragment = (ROOT / "src/viewer.fragment.html").read_text(encoding="utf-8")
    (DOCS / "viewer.html").write_text(template.replace("__VIEWER_FRAGMENT_ESCAPED__", esc(fragment, quote=True)), encoding="utf-8")
    (DOCS / ".nojekyll").touch()
    print(f"Built study hub: {len(CHAPTERS)} exercises, {sum(len(c['questions']) for c in CHAPTERS)} questions, 12 PDF/SVG pairs.")


if __name__ == "__main__":
    build()
