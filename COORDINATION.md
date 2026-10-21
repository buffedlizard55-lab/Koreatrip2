# COORDINATION.md — Shared Task Board & Verification Log

**Repository:** `buffedlizard55-lab/Koreatrip2`  
**Active Session Branch:** `arena/9bfbcc9b-koreatrip2` (Session ID: `session-9bfbcc9b`)  
**Last Updated:** 2026-10-21 UTC  

---

## 1. Task Board

| Task ID | Task Description | Status | Owning Session ID | Branch | File Scope |
|---|---|---|---|---|---|
| `T1-days-1-3` | Verify Days 1–3 line-by-line (ICN Airport transit, AREX, Limousine Bus, Stanford Hotel Myeongdong, N Seoul Tower & Cable Car, Myeongdong Shopping/Dept Stores/Olive Young/Street Food, Gwangjang & Mangwon Markets, Pig Restaurant 2, Myeongdong Kyoja, Crystal Jade, Hongojib, Sookhee, Gyeongbokgung Palace, Bukchon Hanok Village, Cafe Onion Anguk, Tea House) | `done` | `session-9bfbcc9b` | `arena/9bfbcc9b-koreatrip2` | `data/days-1-3.json`, `verification/days-1-3.md` |
| `T2-days-4-6` | Verify Days 4–6 line-by-line (Seongsu-dong, Solsot, DDP, Hanjungsun, Caricature, Eternalog, Blue Elephant, Cafe Far Ben, Cafe Onion Seongsu, Rain Report, Jayeondo Sogeumppang, Musinsa Standard, Marge Sherwood, Ader Error, Brandy Melville, Break Silence, Chuncheongol Dakgalbi, Uri Wang Galbitang, Starfield COEX Mall, Soul Market, Gangnam Style Statue, Ikseon-dong & Insadong, Chwihyang / Favorite of Ikseon) | `done` | `session-9bfbcc9b` | `arena/9bfbcc9b-koreatrip2` | `data/days-4-6.json`, `verification/days-4-6.md` |
| `T3-days-7-9-transit` | Verify Days 7–9 & Public Transit Routing (Itaewon Day 7, Day 8 gap analysis, Day 9 Seoul–Busan KTX, L7 Haeundae by LOTTE, Haeundae Beach & Market, hotel-to-destination transit routes) | `done` | `session-9bfbcc9b` | `arena/9bfbcc9b-koreatrip2` | `data/days-7-9-transit.json`, `verification/days-7-9-transit.md` |
| `T4-site-integration` | Final integration, combined dataset (`data/verified-itinerary.json`), GitHub Pages dashboard site (`index.html`, category subpages, `flagged.html`), link/build check, PR & merge to `main`, GitHub Pages deployment verification | `in progress` | `session-9bfbcc9b` | `arena/9bfbcc9b-koreatrip2` | `index.html`, `itinerary.html`, `transit.html`, `dining.html`, `shopping-cafes.html`, `attractions-hotels.html`, `flagged.html`, `assets/*`, `data/verified-itinerary.json`, `.nojekyll` |

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
- **2026-10-21 (Session `session-9bfbcc9b`)**: Completed `T2-days-4-6` (`data/days-4-6.json`, `verification/days-4-6.md`). Claimed `T3-days-7-9-transit`.
  - **Sources Verified**: CatchTable (`catchtable.net`), Dongdaemun Design Plaza (`ddp.or.kr`), Hanjungsun (`hanjungsun.co.kr`), Acorn Caricature (`acorncaricature.imweb.me`), Eternalog (`eternalog-fotobooth.com`), Blue Elephant (`en.blueelephant.co`), Musinsa Standard (`locations.musinsa.com`), Marge Sherwood (`global.margesherwood.com`), ADER ERROR (`adererror.com`), Brandy Melville (`brandymelville.com`), Break Silence (`breaksilence-world.com`), NOL World (`world.nol.com`), Starfield COEX Mall (`starfield.co.kr`), VisitKorea (`english.visitkorea.or.kr`), VisitSeoul (`english.visitseoul.net`).
  - **Major Irregularities Flagged (Days 4–6)**:
    1. **Day 4 DDP vs. Seongsu Mix-Up**: Item 2 labels "Industrial warehouses converted into flagship fashion pop-ups & artisan bakeries" as **Dongdaemun Design Plaza (DDP)**, whereas that describes **Seongsu-dong** (Daelim Changgo / Seongsu Yeonbang); DDP is Zaha Hadid's futuristic cultural plaza in Jung-gu.
    2. **Day 4 & Day 6 Duplicate Restaurant (`Chwihyang` = `Favorite of Ikseon`)**: `Chwihyang` (`익선취향`) and `Favorite of Ikseon` (`@favorite_ikseon`) on Day 6 (plus the stray note at the bottom of Day 4) are the **exact same restaurant** (`17-32 Supyo-ro 28-gil, Jongno-gu`).
    3. **Day 4 & Day 6 Duplicate Cafe/Bakery Chains**: **Cafe Onion** (Day 3 Anguk & Day 4 Seongsu), **Rain Report** (Day 4 Seongsu & Day 6 Ikseon-dong), and **Jayeondo Salt Bread** (Day 4 Seongsu & Day 6 Ikseon-dong) are all scheduled twice across different days.
    4. **Day 4 Brandy Melville Early Closing**: Closes at **19:00 (7:00 PM)** daily.
    5. **Day 4 Solsot Seongsu Price & Break Time**: Dishes cost 14,000–25,900 KRW (~$10.20–$18.80 USD, not $7–$14) and it closes for weekday break time **15:00–17:00**.
    6. **Day 4 Uri Wang Galbitang Geographic Detour**: Located in Gangdong-gu (`119-9 Seongan-ro`), ~32 min east across the Han River from Seongsu.
    7. **Day 5 Subway to Starfield COEX Mall**: Direct Subway Line 2 from `Euljiro 1(il)-ga Station` (2-min walk from Stanford Hotel) to `Samseong Station` takes **30 minutes with zero transfers** (not 47 minutes).
- **2026-10-21 (Session `session-9bfbcc9b`)**: Completed `T3-days-7-9-transit` (`data/days-7-9-transit.json`, `verification/days-7-9-transit.md`). Claimed `T4-site-integration`.
  - **Sources Verified**: VisitKorea (`english.visitkorea.or.kr`), VisitSeoul (`english.visitseoul.net`), VisitBusan (`visitbusan.net`), KORAIL (`letskorail.com`), Lotte Hotels (`lottehotel.com/haeundae-l7/en.html`), Stanford Hotel Myeongdong (`stanford.webhelper.co.kr`).
  - **Major Irregularities Flagged (Days 7–9)**:
    1. **Day 7 Incomplete Itaewon Plan**: Day 7 lists only *"Itaewon (Nov 7)"* with no sub-items, while **Pig Restaurant 2 (Itaewon)** is listed on Day 2 (Myeongdong day).
    2. **Day 8 Completely Blank**: Sunday, Nov 8, 2026 has zero planned items in the source document (left blank in verified fields per strict no-hallucination rules; flagged for review).
    3. **Day 9 KTX Boarding Rule Discrepancy**: Prompt advises boarding KTX 45 minutes early, whereas Seoul Station KTX platform tracks are announced ~20 minutes before departure and train doors open ~15–20 minutes before departure.
    4. **Day 9 L7 Haeundae Check-in / Check-out Times**: Official check-in is **15:00** and check-out is **11:00 AM** (1 hour earlier than Stanford Hotel Myeongdong).
    5. **Day 9 Numbering Irregularities**: Duplicate `1.` and missing `3.` in original Day 9 list (`1, 1, 2, 4, 5, 6, 7, 8`).



