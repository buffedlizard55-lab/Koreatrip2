# Korea, considered.

A static, mobile-friendly evidence-led itinerary for two travelers, Seoul → Busan, working dates November 1–9, 2026. Open [the published site](https://buffedlizard55-lab.github.io/Koreatrip2/) or serve this directory over HTTP (ES modules do not run from `file://`).

## Structure

- `index.html`: trip overview
- `pages/days.html`: nine-day plan (Tuesday palace visit moved to Wednesday)
- `pages/places.html`: filterable line-by-line directory; one official link per row
- `pages/*-guide.html`: food, cafés, markets, shopping, sights and stays by category
- `pages/transport.html`: hotel-to-destination routes and official operator links
- `pages/review.html`: flagged uncertainties, including all unverified rows
- `data/itinerary.js`: single source for site data; empty location/hour values mean not officially confirmed
- `research/AUDIT.md`: verification notes and key corrections
- `COORDINATION.md`: task board and handoff record

Source status is deliberately conservative. An “official context · not evidence” link points to a government/tourism area page, **not** a confirmation of a specific shop. No booking information was provided. All regular hours should be reconfirmed for the day of travel.

## Local validation

```sh
node scripts/validate.mjs
python3 -m http.server 8000 --bind 0.0.0.0
```

The Pages workflow validates and packages only the canonical audited pages via `node scripts/build.mjs`. Prior-session static pages and their data remain in Git for provenance but are deliberately excluded from the published artifact because some older rows have conflicting or unsupported values. The earlier session’s `app.js` and `styles.css` are retained from PR #1 for provenance; the new pages use `assets/app.js` and `assets/style.css`.
