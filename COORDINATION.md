# Coordination Board

Shared task board for parallel agent sessions.

## Sessions

| Session ID | Branch | Scope | Status |
|---|---|---|---|
| e314c1fc | arena/e314c1fc-koreatrip2 | Single-page dashboard: `index.html`, `app.js`, `styles.css`, `README.md`, `.github/workflows/pages.yml`, `COORDINATION.md` | merged to main (PR #1) |
| 6c06fb0a | arena/6c06fb0a-koreatrip2 | Multi-page verified site: `data/itinerary.json`, `pages/*`, `assets/style.css`, `build_site.py`, `index.html`, `COORDINATION.md` | in progress |

## Tasks

| ID | Task | Status | Owner | Files | Notes |
|----|------|--------|-------|-------|-------|
| T1 | Create COORDINATION.md | done | arena/6c06fb0a-koreatrip2 | COORDINATION.md | initial |
| T2 | Verify Week1 Seoul itinerary entries (hotels, transport, attractions, restaurants, stores) | done | arena/6c06fb0a-koreatrip2 | data/itinerary.json, pages/*, assets/* | 59 entries; official sources linked per row |
| T3 | Verify Week1 Day8-9 & Busan entries | done | arena/6c06fb0a-koreatrip2 | data/itinerary.json | Day 8/9 + Busan entries included; unverified flagged |
| T4 | Build GitHub Pages site (index + subpages) | done | arena/6c06fb0a-koreatrip2 | index.html, pages/*, assets/*, build_site.py | 12 HTML pages; responsive tables |
| T5 | Final integration: merge, re-verify, build check, publish | done | arena/6c06fb0a-koreatrip2 | all | PR #2 merged to main; Pages workflow run 39564264196 succeeded; site built |
| S1 | Build verified itinerary dashboard and publish-ready GitHub Pages setup | done | e314c1fc | index.html, app.js, styles.css, README.md, .github/workflows/pages.yml, COORDINATION.md | merged to main (PR #1) |

## Verification summary (session 6c06fb0a)
- Official sources used: VisitKorea/VisitSeoul, Seoul Metropolitan Government, Incheon Airport, Korail, N Seoul Tower, Stanford Hotel, Lotte Hotels, Starfield COEX, DDP, Gyeongbokgung (royal.khs.go.kr via VisitKorea), Bukchon (hanok.seoul.go.kr), Olive Young, Cafe Onion (onionkr.com), Rain Report, Jayeondo, Musinsa Standard, Marge Sherwood, Blue Elephant, Ader Error, Myeongdong Kyoja, Gwangjang/Mangwon markets.
- Verified rows: 25+; unverified rows left blank and flagged.

## Irregularities flagged
1. Gyeongbokgung Palace (and guard ceremony) closed on Tuesdays; itinerary schedules them on Tue Nov 3, 2026.
2. N Seoul Tower itinerary hours (10:00-10:30) corrected to official 10:00-22:30 (weekday) / 10:00-23:00 (weekend).
3. Olive Young itinerary hours (08:00-24:00) not confirmed; official Myeongdong Town 10:00-22:30.
4. Day 7 and Day 8 have no detailed plan in the itinerary.
5. Many small businesses have no official source; hours/addresses left blank and flagged.
6. AREX itinerary "45 min, $7" approximates the All-Stop service (59-66 min, ₩4,750-₩5,350); Express is 43-51 min, ₩13,000.
7. Airport bus itinerary "$13" approximates KAL Limousine (₩18,000); standard airport bus ₩17,000.
8. Myeongdong Kyoja main branch moved to 129 Toegye-ro in 2026; older listings show 29 Myeongdong 10-gil.
9. Haeundae Market, Haeundae Beach hours unverified.
10. (from session e314c1fc) Supplied dates/weekday labels align with 2026 but text calls out 2006; travel year unresolved. Hotel supplied names remain labeled unverified pending reservation confirmation.

## Log
- 2026-10-21: Session e314c1fc merged PR #1 to main (single-page dashboard).
- 2026-10-21: Session 6c06fb0a started. Claimed T2-T5.
- 2026-10-21: Data verified and multi-page site built; link check passed.
- 2026-10-21: Merged origin/main into session branch; resolving integration. Keeping multi-page site plus Pages workflow from main.

## Publication
- PR: https://github.com/buffedlizard55-lab/Koreatrip2/pull/2
- Merge: merged to main (merge commit)
- Pages workflow run: 39564264196 (success)
- Site URL: https://buffedlizard55-lab.github.io/Koreatrip2/

## Session 96a67227 work board

# Coordination

Session ID: `96a67227` (Arena branch `arena/96a67227-koreatrip2`; branch name is fixed by the environment). This repository had no task board or other claims when work began. Only this session is active here; no parallel branches are being created.

| Task | Status | Owner | File scope | Sources / verification / irregularities |
|---|---|---|---|---|
| Research and itinerary data | Done | 96a67227 | `data/**`, `research/**` | 21 Oct: row-by-row source audit; methods/sources in `research/AUDIT.md`. Irregularities (Tuesday palace closure, year typo, timings, mismatched districts, unknown venues) published as unverified/partial entries. |
| Site design and implementation | In progress | 96a67227 | `index.html`, `pages/**`, `assets/**`, `scripts/**`, `.github/**`, `package.json`, `README.md` | — |
| Final integration, audit, publication | Unclaimed | — | All files after research and site tasks finish; `COORDINATION.md` | Recheck data, links, build, Pages, PR. |

## Requests / handoffs

None.

