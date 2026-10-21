# Korea, in two stops

A mobile-friendly, source-checked GitHub Pages itinerary for two adult travelers visiting Seoul and Busan. The site keeps user-supplied plans separate from verified travel facts, links official sources beside every table row, and leaves unsupported values blank on a clearly labeled **Flagged for Review** page.

## Browse the site

- `index.html` — clean landing page and trip overview
- `itinerary.html` — every supplied stop, including the empty day and incomplete suggestions
- `seoul.html` — Seoul sights, neighborhoods, hours, closures and station references
- `food-shopping.html` — official business / market checks and unresolved venue details
- `busan.html` — L7 Haeundae, beach, market and walking notes
- `getting-around.html` — SFO / ICN, AREX, airport bus, KTX and local transit links
- `flagged-for-review.html` — date conflicts, source discrepancies and unverified values

The supplied date strings are preserved as written. No travel year, day assignment, flight schedule or KTX detail is inferred. Research snapshot: 21 October 2026; confirm current schedules, fares, hours and holiday notices before travel.

## Run locally

The site is static and has no package installation step.

```sh
python3 scripts/check_site.py
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 0.0.0.0
```

Open `http://localhost:8000/` for local review. `scripts/check_site.py` validates required metadata, local page / fragment / asset links, filter targets, and an official-source link for every table row. `scripts/build_site.py` stages only the public website files in the ignored `site-build/` directory; it does not include coordination notes or repository scripts in the Pages artifact.

## Publishing

`.github/workflows/deploy-pages.yml` validates and deploys the site to GitHub Pages on pushes to `main` and on manual workflow dispatch. Pages is configured to use the Actions workflow. The public project-site URL is expected to be:

<https://buffedlizard55-lab.github.io/Koreatrip2/>
