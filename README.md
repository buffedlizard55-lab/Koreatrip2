# Korea, considered.

A static, mobile-friendly evidence-led itinerary for two travelers, Seoul → Busan, working dates November 1–16, 2026 (Seoul → Busan → Seoul). Open [the published site](https://buffedlizard55-lab.github.io/Koreatrip2/) or serve this directory over HTTP (ES modules do not run from `file://`).

## Structure

- `index.html`: trip overview
- `pages/days.html`: 16-day plan (Tuesday palace visit moved to Wednesday)
- `pages/places.html`: filterable line-by-line directory; one official link per row
- `pages/*-guide.html`: food, cafés, markets, shopping, sights and stays by category
- `pages/transport.html`: hotel-to-destination routes and official operator links
- `pages/review.html`: flagged uncertainties, including all unverified rows
- `data/itinerary.js`: single source for site data; empty location/hour values mean not officially confirmed
- `research/AUDIT.md`: verification notes and key corrections
- `verification/days-1-3.md`, `verification/days-4-6.md`, `verification/days-7-9-transit.md`, `verification/days-10-16.md`: verification reports; Days 10–16 covers the supplied Busan itinerary and return to Seoul
- `data/verified-itinerary.json`, `data/days-1-3-session-9bfbcc9b.json`, `data/days-4-6.json`, `data/days-7-9-transit.json`: structured verification datasets (`session-9bfbcc9b`)
- `COORDINATION.md`: task board and handoff record

Days 13 and 15 remain open because no activities were supplied. Date-specific rail services and reservations are not inferred. Exact transit times/fares remain blank where an official source does not confirm them; specific unknown businesses are flagged.

Source status is deliberately conservative. An “official context · not evidence” link points to a government/tourism area page, **not** a confirmation of a specific shop. No booking information was provided. All regular hours should be reconfirmed for the day of travel.

## Local validation

```sh
node scripts/validate.mjs
python3 -m http.server 8000 --bind 0.0.0.0
```

GitHub Pages is configured for **legacy deployment from `main`**. The validation workflow checks and packages the canonical audited pages via `node scripts/build.mjs`, but GitHub Pages publishes the repository root automatically on a main push. Prior-session static data, builder, styling and original pages remain in Git history for provenance. Original generated HTML and the earlier verification worksheet are also preserved as text under `research/legacy-pages/`. Its former page URLs now redirect to the audited equivalents so the published site does not expose obsolete or unsupported table values. Do not rerun `build_site.py` over the integrated pages. The earlier session’s `app.js` and `styles.css` are retained from PR #1 for provenance; the new pages use `assets/app.js` and `assets/style.css`.
