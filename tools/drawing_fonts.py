"""Find a Unicode TrueType font without depending on a particular OS."""
import os
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def register_drawing_font():
    candidates = [os.getenv("DRAWING_FONT", ""),
                  "C:/Windows/Fonts/arial.ttf",
                  "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                  "/Library/Fonts/Arial.ttf"]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            pdfmetrics.registerFont(TTFont("Arial", candidate))
            return
    raise FileNotFoundError("Set DRAWING_FONT to a Unicode TrueType font (.ttf).")
