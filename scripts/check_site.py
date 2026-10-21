#!/usr/bin/env python3
"""Validate local site pages, internal links, and official sources per table row."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.assets: list[str] = []
        self.title_text = ""
        self.title_depth = 0
        self.h1_count = 0
        self.has_language = False
        self.has_viewport = False
        self.filter_targets: list[str] = []
        self.errors: list[str] = []
        self.table_depth = 0
        self.row_depth = 0
        self.row_has_cells = False
        self.row_has_source = False
        self.data_rows = 0
        self.rows_without_source = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html" and attributes.get("lang"):
            self.has_language = True
        if attributes.get("id"):
            element_id = attributes["id"]
            assert element_id is not None
            if element_id in self.ids:
                self.errors.append(f"duplicate id #{element_id}")
            self.ids.add(element_id)
        if tag == "meta" and attributes.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.title_depth += 1
        if tag == "table":
            self.table_depth += 1
        if tag == "tr" and self.table_depth:
            self.row_depth += 1
            self.row_has_cells = False
            self.row_has_source = False
        if tag in {"td", "th"} and self.table_depth and self.row_depth:
            if tag == "td":
                self.row_has_cells = True
        if tag == "a":
            href = attributes.get("href")
            if href:
                self.links.append(href)
                if attributes.get("data-source") == "official" and self.table_depth and self.row_depth:
                    self.row_has_source = True
        if tag == "link" and attributes.get("rel", "").lower() in {"stylesheet", "icon"}:
            href = attributes.get("href")
            if href:
                self.assets.append(href)
        if tag == "script" and attributes.get("src"):
            self.assets.append(attributes["src"] or "")
        if attributes.get("data-filter-table"):
            self.filter_targets.append(attributes["data-filter-table"] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if tag == "tr" and self.row_depth:
            if self.row_has_cells:
                self.data_rows += 1
                if not self.row_has_source:
                    self.rows_without_source += 1
            self.row_depth -= 1
        if tag == "table" and self.table_depth:
            self.table_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text += data


def check_page(page: Path) -> list[str]:
    errors: list[str] = []
    rel = page.relative_to(ROOT)
    parser = PageParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - defensive error message
        return [f"{rel}: could not parse HTML: {exc}"]

    if not parser.title_text.strip():
        errors.append(f"{rel}: missing <title>")
    if parser.h1_count != 1:
        errors.append(f"{rel}: expected exactly one <h1>, found {parser.h1_count}")
    if not parser.has_language:
        errors.append(f"{rel}: missing html lang attribute")
    if not parser.has_viewport:
        errors.append(f"{rel}: missing viewport meta")
    if parser.rows_without_source:
        errors.append(f"{rel}: {parser.rows_without_source} table row(s) missing a data-source=\"official\" link")
    errors.extend(f"{rel}: {item}" for item in parser.errors)

    for target_id in parser.filter_targets:
        if target_id not in parser.ids:
            errors.append(f"{rel}: filter refers to missing table id #{target_id}")

    for href in parser.assets:
        parts = urlsplit(href)
        if parts.scheme or parts.netloc:
            continue
        if not parts.path:
            continue
        asset_path = (page.parent / unquote(parts.path)).resolve()
        if not asset_path.exists():
            errors.append(f"{rel}: missing local asset {href}")

    for href in parser.links:
        parts = urlsplit(href)
        if parts.scheme or parts.netloc or href.startswith("//"):
            continue
        path_part = unquote(parts.path)
        target = (page.parent / path_part).resolve() if path_part else page.resolve()
        if not target.exists():
            errors.append(f"{rel}: broken local link {href}")
            continue
        if parts.fragment:
            if target.is_dir():
                target = target / "index.html"
            if target.suffix.lower() == ".html" and target.exists():
                target_parser = PageParser()
                try:
                    target_parser.feed(target.read_text(encoding="utf-8"))
                except Exception as exc:  # pragma: no cover - defensive
                    errors.append(f"{rel}: could not parse fragment target {href}: {exc}")
                    continue
                fragment = unquote(parts.fragment)
                if fragment not in target_parser.ids:
                    errors.append(f"{rel}: missing fragment {href}")

    return errors


def main() -> int:
    pages = sorted(ROOT.glob("*.html"))
    if not pages:
        print("ERROR: no root HTML pages found", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    total_rows = 0
    for page in pages:
        all_errors.extend(check_page(page))
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        total_rows += parser.data_rows

    for required in (ROOT / "assets" / "styles.css", ROOT / "assets" / "site.js"):
        if not required.is_file():
            all_errors.append(f"missing required asset {required.relative_to(ROOT)}")

    if all_errors:
        print("Site validation failed:")
        for error in all_errors:
            print(f" - {error}")
        return 1

    print(f"Site validation passed: {len(pages)} page(s), {total_rows} sourced table row(s), local links and assets OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
