#!/usr/bin/env python3
"""Stage only public website files for the GitHub Pages artifact."""
from __future__ import annotations

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site-build"
PAGES = (
    "index.html",
    "itinerary.html",
    "seoul.html",
    "food-shopping.html",
    "busan.html",
    "getting-around.html",
    "flagged-for-review.html",
)


def main() -> None:
    missing = [name for name in PAGES if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit("Missing required page(s): " + ", ".join(missing))
    if not (ROOT / "assets" / "styles.css").is_file() or not (ROOT / "assets" / "site.js").is_file():
        raise SystemExit("Missing required CSS or JavaScript asset")

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    for name in PAGES:
        shutil.copy2(ROOT / name, OUTPUT / name)
    shutil.copytree(ROOT / "assets", OUTPUT / "assets")
    (OUTPUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Staged {len(PAGES)} HTML pages and {len(list((OUTPUT / 'assets').iterdir()))} assets in {OUTPUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
