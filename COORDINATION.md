# COORDINATION.md — Shared Task Board & Verification Log

**Repository:** `buffedlizard55-lab/Koreatrip2`  
**Active Session Branch:** `arena/9bfbcc9b-koreatrip2` (Session ID: `session-9bfbcc9b`)  
**Last Updated:** 2026-10-21 UTC  

---

## 1. Task Board

| Task ID | Task Description | Status | Owning Session ID | Branch | File Scope |
|---|---|---|---|---|---|
| `T1-days-1-3` | Verify Days 1–3 line-by-line (ICN Airport transit, AREX, Limousine Bus, Stanford Hotel Myeongdong, N Seoul Tower & Cable Car, Myeongdong Shopping/Dept Stores/Olive Young/Street Food, Gwangjang & Mangwon Markets, Pig Restaurant 2, Myeongdong Kyoja, Crystal Jade, Hongojib, Sookhee, Gyeongbokgung Palace, Bukchon Hanok Village, Cafe Onion Anguk, Tea House) | `done` | `session-9bfbcc9b` | `arena/9bfbcc9b-koreatrip2` | `data/days-1-3.json`, `verification/days-1-3.md` |
| `T2-days-4-6` | Verify Days 4–6 line-by-line (Seongsu-dong, Solsot, DDP, Hanjungsun, Caricature, Eternalog, Blue Elephant, Cafe Far Ben, Cafe Onion Seongsu, Rain Report, Jayeondo Sogeumppang, Musinsa Standard, Marge Sherwood, Ader Error, Brandy Melville, Break Silence, Chuncheongol Dakgalbi, Uri Wang Galbitang, Starfield COEX Mall, Soul Market, Gangnam Style Statue, Ikseon-dong & Insadong, Chwihyang / Favorite of Ikseon) | `in progress` | `session-9bfbcc9b` | `arena/9bfbcc9b-koreatrip2` | `data/days-4-6.json`, `verification/days-4-6.md` |
| `T3-days-7-9-transit` | Verify Days 7–9 & Public Transit Routing (Itaewon Day 7, Day 8 gap analysis, Day 9 Seoul–Busan KTX, L7 Haeundae by LOTTE, Haeundae Beach & Market, hotel-to-destination transit routes) | `unclaimed` | — | — | `data/days-7-9-transit.json`, `verification/days-7-9-transit.md` |
| `T4-site-integration` | Final integration, combined dataset (`data/verified-itinerary.json`), GitHub Pages dashboard site (`index.html`, category subpages, `flagged.html`), link/build check, PR & merge to `main`, GitHub Pages deployment verification | `unclaimed` | — | — | `index.html`, `itinerary.html`, `transit.html`, `dining.html`, `shopping-cafes.html`, `attractions-hotels.html`, `flagged.html`, `assets/*`, `data/verified-itinerary.json`, `.nojekyll` |

---

## 2. Session Log

- **2026-10-21 (Session `session-9bfbcc9b`)**: Created `COORDINATION.md` and claimed `T1-days-1-3`.
- **2026-10-21 (Session `session-9bfbcc9b`)**: Completed `T1-days-1-3` (`data/days-1-3.json`, `verification/days-1-3.md`). Claimed `T2-days-4-6`.
  - **Sources Verified**: Incheon Airport (`airport.kr`), AREX (`arex.or.kr`), Airport Limousine (`airportlimousine.co.kr`), Stanford Hotel Myeongdong (`stanford.webhelper.co.kr`), N Seoul Tower (`nseoultower.co.kr`), VisitKorea (`english.visitkorea.or.kr`), VisitSeoul (`english.visitseoul.net`), Lotte Department Store (`global.lotteshopping.com`), Shinsegae (`shinsegaedf.com`), Olive Young (`oliveyoung.co.kr`), MICHELIN Guide (`guide.michelin.com`), Myeongdong Kyoja (`mdkj.co.kr`), Crystal Jade Korea (`crystaljade.co.kr`), Hongojib (`hongojib.com`), Korea Heritage Service (`royal.khs.go.kr`), Seoul Metropolitan Gov. (`english.seoul.go.kr`).
  - **Major Irregularities Flagged (Days 1–3)**:
    1. **Day 3 Critical Closure**: Gyeongbokgung Palace & Changing of the Guard are **CLOSED on Tuesdays** (Nov 3, 2026 is a non-holiday Tuesday).
    2. **Day 2 Critical Closure**: Cho Yonsoon's Netflix hand-cut noodle stall (**Gohyang Kalguksu**, Stall A70 at Gwangjang Market) is **CLOSED on Mondays** (Nov 2, 2026).
    3. **Day 3 Bukchon Curfew**: Bukchon Hanok Village Red Zone (`Bukchon-ro 11-gil`) enforces a strict **10:00–17:00** tourist visiting window (100,000 KRW fine after 17:00).
    4. **Day 2 Olive Young Hours**: Flagship operates **10:00–22:30**, not `8:00 AM–12:00 AM`.
    5. **Day 2 Namsan Tower / Cable Car**: Year typo (`Nov 2, 2006`), Namsan Shuttle Bus 01A/01B bypasses the Cable Car, Namsan Ormi outdoor elevator is closed Mondays 09:00–14:00, and Cable Car closes at 23:00 (not 10:30 PM).
    6. **Day 2 Crystal Jade Shinsegae B1F**: Closes at **20:00 (Last Order 19:30)** on Mondays.
    7. **Day 1 AREX Fare & Transfer**: Express Train is 13,000 KRW (~$9.50 USD) and terminates at Seoul Station, requiring a Line 4 transfer or taxi to reach Myeongdong.

