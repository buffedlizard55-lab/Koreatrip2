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

## Session: arena/d20d7578-koreatrip2 (this session, single agent)

| Task | Status | Scope (files) | Session ID | Sources verified | Notes |
|------|--------|---------------|------------|------------------|-------|
| 1. Repo setup + COORDINATION.md | done | COORDINATION.md | arena/d20d7578-koreatrip2 | n/a | Initial commit exists on branch `arena/d20d7578-koreatrip2` |
| 2. Parse itinerary into structured data | in progress | `data/itinerary.json` | arena/d20d7578-koreatrip2 | — | Line-by-line parse of user-provided itinerary |
| 3. Verify each fact against official sources | unclaimed | `data/verification.md` | arena/d20d7578-koreatrip2 | — | Official source link per row; blank + flag if unconfirmed |
| 4. Site: landing page + category subpages | unclaimed | `index.html`, `pages/*.html`, `assets/*` | arena/d20d7578-koreatrip2 | — | Dashboard UI, mobile-friendly, tables with sources |
| 5. Flagged for Review page | unclaimed | `pages/flagged.html` | arena/d20d7578-koreatrip2 | — | All unverified/irregular items with source links |
| 6. Integration: build check, broken-link check | unclaimed | all site files | arena/d20d7578-koreatrip2 | — | Confirm no broken links |
| 7. GitHub Pages publish | unclaimed | repo settings / gh-pages | arena/d20d7578-koreatrip2 | — | Confirm deploy succeeds |
| 8. PR to main + merge | unclaimed | n/a | arena/d20d7578-koreatrip2 | — | Merge without waiting; record PR link + result |

## Irregularities / unverified items (log here, publish on Flagged for Review page)
- None yet.
