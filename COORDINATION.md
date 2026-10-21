# Coordination Board

Shared task board for parallel agent sessions.

## Sessions

| Session ID | Branch | Scope | Status |
|---|---|---|---|
| e314c1fc | arena/e314c1fc-koreatrip2 | Single-page dashboard: `index.html`, `app.js`, `styles.css`, `README.md`, `.github/workflows/pages.yml`, `COORDINATION.md` | merged to main (PR #1) |
| 6c06fb0a | arena/6c06fb0a-koreatrip2 | Multi-page verified site: `data/itinerary.json`, `pages/*`, `assets/style.css`, `build_site.py`, `index.html`, `COORDINATION.md` | merged to main (PR #2) |
| 96a67227 | arena/96a67227-koreatrip2 | Audited multi-page directory: `data/itinerary.js`, `research/AUDIT.md`, `pages/*`, `scripts/*` | merged to main (PR #5) |
| d20d7578 | arena/d20d7578-koreatrip2 | Verification markdown & generator: `data/verification.md`, `pages/day-by-day.html`, `pages/activities.html`, `tools/generate_site.py` | merged to main (PR #4) |
| 535004bc | arena/535004bc-koreatrip2 | Line-by-line official verification JSONs (`data/hotels-transport.json`, `data/days-1-3.json`, `data/days-4-9.json`, `data/flagged.json`) + cross-session integration & verification audit | in progress |

## Tasks

| ID | Task | Status | Owner | Files | Notes |
|----|------|--------|-------|-------|-------|
| T1 | Create COORDINATION.md | done | arena/6c06fb0a-koreatrip2 | COORDINATION.md | initial |
| T2 | Verify Week1 Seoul itinerary entries (hotels, transport, attractions, restaurants, stores) | done | arena/6c06fb0a-koreatrip2 | data/itinerary.json, pages/*, assets/* | 59 entries; official sources linked per row |
| T3 | Verify Week1 Day8-9 & Busan entries | done | arena/6c06fb0a-koreatrip2 | data/itinerary.json | Day 8/9 + Busan entries included; unverified flagged |
| T4 | Build GitHub Pages site (index + subpages) | done | arena/6c06fb0a-koreatrip2 | index.html, pages/*, assets/*, build_site.py | 12 HTML pages; responsive tables |
| T5 | Final integration: merge, re-verify, build check, publish | done | arena/6c06fb0a-koreatrip2 | all | PR #2 merged to main; Pages workflow run 39564264196 succeeded; site built |
| S1 | Build verified itinerary dashboard and publish-ready GitHub Pages setup | done | e314c1fc | index.html, app.js, styles.css, README.md, .github/workflows/pages.yml, COORDINATION.md | merged to main (PR #1) |
| S535004bc-1 | Verify Hotels, Transport, Days 1–9 & 18 Flagged Irregularities from official sources | done | 535004bc (arena/535004bc-koreatrip2) | `data/hotels-transport.json`, `data/days-1-3.json`, `data/days-4-9.json`, `data/flagged.json` | Every row linked to official source; unverified values left blank |
| S535004bc-2 | Final Cross-Session Integration, Line-by-Line Re-verification & Link Audit | in progress | 535004bc (arena/535004bc-koreatrip2) | `index.html`, `pages/*`, `data/*`, `scripts/validate.mjs`, `COORDINATION.md` | Preserve all prior session files & integrate new official sources found |

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

Session ID: `96a67227` (Arena branch `arena/96a67227-koreatrip2`; branch name is fixed by the environment). This checkout had no task board when work began. A separate Arena session later merged PR #1 into `main`; this branch remains the fixed Arena branch, not a newly named session branch.

| Task | Status | Owner | File scope | Sources / verification / irregularities |
|---|---|---|---|---|
| Research and itinerary data | Done | 96a67227 | `data/**`, `research/**` | 21 Oct: row-by-row source audit; methods/sources in `research/AUDIT.md`. Irregularities (Tuesday palace closure, year typo, timings, mismatched districts, unknown venues) published as unverified/partial entries. |
| Site design and implementation | Done | 96a67227 | `index.html`, `pages/**`, `assets/**`, `scripts/**`, `.github/**`, `README.md` | 21 Oct: 5 static pages, filterable directory and Pages workflow. Smoke-rendered all pages and checked local links; `node scripts/validate.mjs` passes. |
| Final integration, audit, publication | Done | 96a67227 | All files after research and site tasks finish; `COORDINATION.md` | Recheck data, links, build, Pages, PR. |

## Requests / handoffs

- 21 Oct: `main` advanced during this work when PR #1 from session `e314c1fc` merged. Rebased this branch onto that merge. Conflicts in `COORDINATION.md`, `index.html`, `README.md`, and the Pages workflow were resolved by retaining the earlier session’s log and `app.js`/`styles.css`, while integrating the new multi-page dashboard, audit and validation workflow. No earlier commits were discarded; the original dashboard remains in Git history.

- 21 Oct: During the next `git pull --rebase`, PR #2 from session `6c06fb0a` landed on `main`. Resolved second conflicts in `COORDINATION.md`, `index.html`, and `assets/style.css` without removing its category pages/data. Preserved its stylesheet as `assets/previous-style.css`, and pointed its 12 existing category pages there; this session’s dashboard uses `assets/style.css`. The legacy `build_site.py` is retained but must not be rerun over the integrated index.


## Final integration audit notes (96a67227)

- Rechecked the combined data after PR #2: its earlier Kyoja “moved branch” assertion conflicts with two addresses on a single official tourism page; the canonical directory now leaves the address blank and flags it. An additional Seongsu Rain Report outlet and official Musinsa Standard, Marge Sherwood and Blue Elephant listings were incorporated; source links are in `research/AUDIT.md`.
- The prior 12 generated category pages and `data/itinerary.json` are retained on this branch, but the deploy artifact intentionally excludes them because some entries contain third-party-only prices/locations and unresolved date errors. The live site publishes the 11 audited pages built from `data/itinerary.js`. The prior pages still render locally with preserved `assets/previous-style.css`. Do not rerun the older `build_site.py` over the integrated index.
- Conflict resolutions preserved both earlier session histories and logs. A force-with-lease push is required solely because this fixed branch was rebased onto the moving `main`; no other branch was created or modified.

- Publication configuration check: GitHub Pages API reports `build_type: legacy`, source `main:/`, and a built site. Attempting to switch to workflow mode returned API 403 (integration lacks Pages-write settings access). The prior action-based deploy had a failed run after PR #3 even though legacy `pages-build-deployment` succeeded. To prevent competing deploys, this branch makes the workflow validation-only; Pages auto-publishes root on merge. `build/` is a checked canonical preview, not the Pages artifact. The navigation exposes only the audited views; older merged pages remain available by direct URL for historical comparison and may contain unverified claims.

- Final root-publish safeguard: the previous static category URLs were converted to accessible redirects to their audited equivalents. Their original HTML is preserved under `research/legacy-pages/` and in PR #2 Git history; `data/itinerary.json`, `build_site.py`, and preserved styles remain in the repository. This prevents a Pages legacy root deployment from exposing third-party-only/contradictory table fields in the earlier generated HTML.

- PR #5: https://github.com/buffedlizard55-lab/Koreatrip2/pull/5 — integration candidate; check run [39564824249](https://github.com/buffedlizard55-lab/Koreatrip2/actions/runs/39564824249) passed validation/build. Merge result and Pages publication to be recorded after merge.

---

## Session `535004bc` (`arena/535004bc-koreatrip2`) Work Board & Conflict Resolution Log

- **Conflict Resolution Log (2026-10-21)**: When rebasing `arena/535004bc-koreatrip2` onto `origin/main` (`7f1d419`, following merges of PRs #1–#5), an add/add conflict occurred in `COORDINATION.md` because this session branched from `bf44c27` before `COORDINATION.md` existed on `main`. Resolved without discarding any work from sessions `e314c1fc`, `6c06fb0a`, `96a67227`, or `d20d7578`.
- **Additional Official Sources Verified by Session `535004bc`** (recorded in `data/hotels-transport.json`, `data/days-1-3.json`, `data/days-4-9.json`, `data/flagged.json`):
  - **Crystal Jade Korea Official (`crystaljade.co.kr`)**: Confirmed both Myeongdong-area branches—**Shinsegae Main Branch B1 (`https://www.crystaljade.co.kr/menu/menuInfo.do?shSq=49&shGb=H`)** (`63 Sogong-ro, Jung-gu, B1F`, Weekdays `10:30–20:00`, Weekends `10:30–20:30`) and **Sogong Branch (`https://www.crystaljade.co.kr/menu/menuInfo.do?shSq=20&shGb=A`)** (`16 Namdaemun-ro 7-gil, B1F`, `11:00–21:30`, break `15:00–17:00`).
  - **Myeongdong Kyoja Official (`http://www.mdkj.co.kr/en/menu/menu03.php`) & MICHELIN Guide (`https://guide.michelin.com/sg/en/seoul-capital-area/kr-seoul/restaurant/myeongdong-kyoja`)**: Confirmed `10:30–21:00` daily hours, Main Store (`29 Myeongdong 10-gil` / `129 Toegye-ro`) and Branch Store (`8 Myeongdong 10-gil`), plus official brand history noting automated mandu shaping since 1983.
  - **Airport Limousine Co. Official (`https://airportlimousine.co.kr/en/sub/sub01.php?cat_no=47`)**: Confirmed Route **#6015** (`17,000 KRW` Adult, `12,000 KRW` Child, `05:19–22:59`) stopping directly at `Lotte Hotel / IBIS Myeong-dong` (2-min walk from Stanford Hotel Myeongdong), and the March 5, 2026 mandatory ticket-office purchase rule.
  - **AREX Official (`https://www.arex.or.kr/content.do?url=&menuNo=MN201503300000000001&contentNo=&clientLocale=ko_KR&clientDevice=Normal`)**: Confirmed Express Train duration (`43 min` T1 / `51 min` T2) and updated `13,000 KRW` adult fare (`9,500 KRW` on older English pages).
  - **Stanford Hotel Myeongdong Official FAQ (`https://stanford.webhelper.co.kr/myeongdong/en/contents/list/faq`)**: Confirmed `84 Namdaemun-ro, Jung-gu` (9F Lobby), check-in after `15:00`, check-out before `12:00`, early/late fee `20,000 KRW/hr`.
  - **L7 HAEUNDAE by LOTTE Official (`https://www.lottehotel.com/prerendered/haeundae-l7/en/about/art-experience/l7/index.html` & `https://www.lottehotel.com/haeundae-l7/ko/hotel-offers/packages/2024-06/memories-in-perfume.html`)**: Confirmed `55 Haeun-daero 570beon-gil, Haeundae-gu, Busan`, check-in `15:00`, check-out `12:00` (Nov).
  - **N Seoul Tower (`https://www.nseoultower.co.kr/eng/visit/use.asp`) & Namsan Cable Car (`http://www.cablecar.co.kr/m/eng/guide/open.html`)**: Confirmed Observatory (`29,000 KRW`, Mon–Fri `10:00–22:30`, Sat–Sun `10:00–23:00`) and Cable Car (`15,000 KRW` round-trip / `12,000 KRW` one-way, `10:00–23:00` daily).
  - **Gyeongbokgung Palace (`https://www.royalpalace.go.kr:8443/html/eng_gbg/guide/guide01_tab01.jsp`) & Guard Ceremony (`https://www.kh.or.kr/cms/content/view/824`)**: Confirmed closed Tuesdays (critical conflict on Day 3 Tuesday Nov 3).
  - **Bukchon Hanok Village (`https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=215658`)**: Confirmed `10:00–17:00` tourist entry restriction and `100,000 KRW` fine in the Red Zone (`Bukchon-ro 11-gil`).
  - **Seongsu & Ikseon Official Brand Sources**: Blue Elephant (`https://blueelephant.co/product/space-seongsu/4552/`), Musinsa Standard Seongsu (`https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=216520`), MARGESHERWOOD Flagship (`https://global.margesherwood.com/pages/stockist-official`), Eternalog (`https://eternalog-fotobooth.com/21`), Acorn Caricature (`https://acorncaricature.imweb.me/Map?sort=UPDATE&category=1i08d61PE1`), Break Silence (`https://breaksilence-world.com/contact.html`), Jayeondo Salt Bread (`https://english.visitseoul.net/area/saltbread-in-seaside/ENPxtexu0`), Cafe Onion (`https://english.visitseoul.net/eat/cafe-onion/ENP020587`), Haeundae Beach (`https://www.visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000301001001000&uc_seq=373`), and Haeundae Traditional Market (`https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=459&vcontsId=84963`).
