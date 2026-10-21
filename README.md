# Korea Trip Dashboard

A mobile-friendly, static GitHub Pages dashboard for a two-person South Korea trip. The itinerary retains user-provided items but separates verified official information from unconfirmed claims. Unknown values are left blank and surfaced on **Flagged for review**.

## Preview locally

Open `index.html` in a browser, or run `python3 -m http.server 8000` from the repository root.

## Publish on GitHub Pages

The workflow in `.github/workflows/pages.yml` deploys the repository root when pushed to `main`. In repository Settings → Pages, select **GitHub Actions** as the build and deployment source. The current working branch is not `main`; merge to main is required for this workflow to publish.

## Editorial note

Sources are official operator, government, or Korea Tourism Organization pages where available. Hours and schedules can change; confirm for the actual travel date. The travel year is unresolved and the supplied weekday/date sequence conflicts with 2006. Nothing labeled unverified should be treated as a confirmed reservation, route, price, or business schedule.
