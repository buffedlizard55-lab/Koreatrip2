# Korea, considered.

A static, mobile-friendly evidence-led itinerary for two travelers, Seoul → Busan, working dates November 1–9, 2026. Open [the published site](https://buffedlizard55-lab.github.io/Koreatrip2/) or serve this directory over HTTP (ES modules do not run from `file://`).

## Structure

- `index.html`: trip overview
- `pages/days.html`: nine-day plan (Tuesday palace visit moved to Wednesday)
- `pages/places.html`: filterable line-by-line directory; one official link per row
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

The Pages workflow validates and publishes static files without a frontend build tool.
