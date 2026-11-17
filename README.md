# Engineering Graphics · Variant 14

A visual study companion for Technical Drawing in Mechanical Engineering: twelve interactive models, twelve drawing sheets, and 66 assessment questions with study answers.

**[Open the study website](https://anjithu.github.io/Technical-Drawing-in-Mechanical-Eng/)** · **[Explore the 3D studio](https://anjithu.github.io/Technical-Drawing-in-Mechanical-Eng/viewer.html)** · **[Questions & answers](study/questions-and-answers.md)**

The studio supports orbit and zoom, camera presets, sections, orthographic projections, assembly animation, and dark/light themes. Drawings are supplied as A3 PDFs and editable SVGs.

## Start here

1. Read the original [exercise instructions](source/instructions/).
2. Explore the model in the [interactive studio](https://anjithu.github.io/Technical-Drawing-in-Mechanical-Eng/viewer.html).
3. Review the [drawing sheets](drawings/number-14/) and [calculation notes](drawings/number-14/Variant_14_Calculations_and_Assumptions.pdf).
4. Practise the [66 questions and answers](study/questions-and-answers.md).

## Review status

This is a study and review set. Unspecified dimensions, fits, roughness and tolerance annotations are proposals requiring instructor agreement. **Exercise 1a is a provisional reconstruction** of an ambiguous source. Add the required student name and initials before submitting drawings. The models illustrate the adopted geometry; they are not certified manufacturing CAD.

## Folder guide

| Folder | Contents |
| --- | --- |
| `source/instructions/` | Original course Word documents and PDF, unchanged |
| `drawings/number-14/` | 12 PDFs, 12 SVGs, combined sheets, calculations and validation |
| `content/questions.json` | 66 questions and authored study answers |
| `study/` | Readable study guide and assumptions |
| `src/` | Editable visualization and standalone export shell |
| `docs/` | GitHub Pages website and downloadable drawing set |
| `tools/` | Drawing generators and website build script |

## Run locally

Python 3.10 or later:

```sh
python tools/build_site.py
python -m http.server 8000 --directory docs
```

Open `http://localhost:8000`. The 3D viewer uses pinned Three.js and visualization runtime resources from CDNs, so it needs an internet connection. The study pages and drawing downloads are static.

To regenerate the drawing PDFs and SVGs:

```sh
python -m pip install -r requirements.txt
python tools/build_drawings.py
python tools/package_drawings.py
python tools/build_site.py
```

The generator uses Arial on Windows or DejaVu Sans on Linux. Set `DRAWING_FONT` to a Unicode TrueType font if needed. Print PDFs at **actual size / 100% on A3**; respect each labelled view scale.

GitHub Pages publishes `main` → `/docs`. Temporary previews, browser profiles, local output and credentials are excluded from version control.

## Attribution and use

Original exercise documents belong to their respective course authors and retain their original notices. Their inclusion does not grant redistribution rights. Study answers and draft drawings are learning aids, not an official answer key. No blanket license is applied to the course material. Three.js and the exported visualization runtime retain their upstream terms.
