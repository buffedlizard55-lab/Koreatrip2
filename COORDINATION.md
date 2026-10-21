# Coordination — Koreatrip2

Shared task board for all agent sessions working on this repo.

## Session rules
- Claim a task by writing your session ID and file scope, then commit and push the claim immediately.
- Never start a task another session has claimed.
- Keep scopes non-overlapping: each session works on its own branch/worktree named `session-<id>/<task>` and edits only files in its claimed scope.
- If a task requires changing a file owned by another session, log the request here instead of editing it.
- Make small, frequent commits; run `git pull --rebase` before every push.
- On merge conflict: stop, resolve without discarding the other session's work, log what happened.
- When a task is finished, record sources, verification performed, and irregularities here, and mark it done.
- Never mark anything verified without checking an official source; link that source.
- Shared outputs (table data, site index/navigation) are changed only by the final integration session once all other tasks are done.
- Flagged items and unverified values do NOT block merge; publish them on the "Flagged for Review" page.

## Session: arena/d20d7578-koreatrip2 (single session, doing all tasks)

| Task | Status | Scope (files) | Session ID | Sources verified | Notes |
|------|--------|---------------|------------|------------------|-------|
| 1. Repo setup + COORDINATION.md | done | COORDINATION.md | arena/d20d7578-koreatrip2 | n/a | Initial commit exists on branch `arena/d20d7578-koreatrip2` |
| 2. Parse itinerary into structured data | done | `data/itinerary.json` | arena/d20d7578-koreatrip2 | — | Line-by-line parse of user-provided itinerary (9 days, 45 entries) |
| 3. Verify each fact against official sources | done | `data/verification.md` | arena/d20d7578-koreatrip2 | AREX, airportlimousine.co.kr, nseoultower.co.kr, VISITKOREA (Gyeongbokgung, Lotte, Olive Young, Gwangjang, COEX, Haeundae Market), Korail/letskorail, starfield.co.kr, lottehotel.com | Key results: Gyeongbokgung/Lotte/VISITKOREA items verified; N Seoul Tower +$31 matches official cable car+observatory but written hours wrong; Olive Young hours conflict; AREX $7 fare wrong; Gwangjang 2am claim unverified |
| 4. Site: landing page + category subpages | done | `index.html`, `pages/*.html`, `assets/style.css`, `tools/generate_site.py` | arena/d20d7578-koreatrip2 | — | Dashboard UI, mobile-friendly, every row has source link + status badge |
| 5. Flagged for Review page | done | `pages/flagged.html` | arena/d20d7578-koreatrip2 | — | 10 flagged items incl. Gyeongbokgung Tuesday conflict |
| 6. Integration: build check, broken-link check | in progress | all site files | arena/d20d7578-koreatrip2 | — | Internal link check pending; external links spot-checked via web search this session |
| 7. GitHub Pages publish | unclaimed | repo Pages settings | arena/d20d7578-koreatrip2 | — | Enable after merge to main; confirm deploy via GitHub API |
| 8. PR to main + merge | unclaimed | n/a | arena/d20d7578-koreatrip2 | — | PR from arena/d20d7578-koreatrip2 to main; merge without waiting |

## Irregularities / unverified items (published on Flagged for Review page)
1. Day 3 (Tue Nov 3, 2026) schedules Gyeongbokgung Palace — closed Tuesdays. Must reschedule.
2. Day 2 date says "Nov 2, 2006" — should be 2026.
3. Day 1 calls Oct 31 a Sunday — Oct 31, 2026 is Saturday (Nov 1 is Sunday).
4. N Seoul Tower hours in itinerary (10:00–10:30) conflict with official (weekdays 10:00–22:30, weekends 10:00–23:00).
5. Olive Young hours (8:00–midnight) conflict with official (10:00–22:30).
6. AREX fare "$7" matches neither official Express (₩13,000 ≈ $9.30) nor all-stop (₩4,750 ≈ $3.40).
7. Limousine bus "$13" vs official ₩17,000 (~$12.10) / ₩18,000 (~$12.80).
8. Gwangjang "stalls until 2:00am" — official food street closes 23:00.
9. Many small venues have no official English source; left blank/unverified (verify via Kakao/Naver Map before visiting).
10. Days 7–8 empty (Itaewon / free day).
