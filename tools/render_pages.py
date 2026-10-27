"""Render raw PDF scans to page images for vision reading.

Usage:
    py tools/render_pages.py raw/stochastics_1_2.pdf            # all pages
    py tools/render_pages.py raw/stochastics_1_2.pdf 1 40       # pages 1-40 (1-based)

Output: raw/pages/<pdf-stem>/page-001.png ...
Existing page images are skipped, so interrupted runs resume cheaply.
"""

import sys
from pathlib import Path

import pymupdf

DPI = 150


def render(pdf_path: Path, first: int | None, last: int | None) -> None:
    out_dir = Path("raw/pages") / pdf_path.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(pdf_path)
    start = (first or 1) - 1
    end = min(last or doc.page_count, doc.page_count)

    for i in range(start, end):
        out = out_dir / f"page-{i + 1:03d}.png"
        if out.exists():
            continue
        pix = doc[i].get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY)
        pix.save(out)
        print(out)

    doc.close()
    print(f"done: {pdf_path.name} pages {start + 1}-{end} -> {out_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    lo = int(sys.argv[2]) if len(sys.argv) > 2 else None
    hi = int(sys.argv[3]) if len(sys.argv) > 3 else None
    render(path, lo, hi)
