# Coordination Board

Session ID: arena/6c06fb0a-koreatrip2
Branch: arena/6c06fb0a-koreatrip2

## Tasks

| ID | Task | Status | Owner | Files | Notes |
|----|------|--------|-------|-------|-------|
| T1 | Create COORDINATION.md | done | arena/6c06fb0a-koreatrip2 | COORDINATION.md | initial |
| T2 | Verify Week1 Seoul itinerary entries (hotels, transport, attractions, restaurants, stores) | done | arena/6c06fb0a-koreatrip2 | data/itinerary.json, pages/*, assets/* | 59 entries; official sources linked per row |
| T3 | Verify Week1 Day8-9 & Busan entries | done | arena/6c06fb0a-koreatrip2 | data/itinerary.json | Day 8/9 + Busan entries included; unverified flagged |
| T4 | Build GitHub Pages site (index + subpages) | done | arena/6c06fb0a-koreatrip2 | index.html, pages/*, assets/*, build_site.py | 12 HTML pages; responsive tables |
| T5 | Final integration: merge, re-verify, build check, publish | done | arena/6c06fb0a-koreatrip2 | all | link check passed; ready to PR/merge |

## Verification summary
- Official sources used: VisitKorea/VisitSeoul, Seoul Metropolitan Government, Incheon Airport, Korail, N Seoul Tower, Stanford Hotel, Lotte Hotels, Starfield COEX, DDP, Gyeongbokgung (royal.khs.go.kr via VisitKorea), Bukchon (hanok.seoul.go.kr), Olive Young, Cafe Onion (onionkr.com), Rain Report, Jayeondo, Musinsa Standard, Marge Sherwood, Blue Elephant, Ader Error, Myeongdong Kyoja, Gwangjang/Mangwon markets.
- Verified rows: 25+; unverified rows left blank and flagged.

## Irregularities flagged
1. Gyeongbokgung Palace (and guard ceremony) closed on Tuesdays; itinerary schedules them on Tue Nov 3, 2026.
2. N Seoul Tower itinerary hours (10:00-10:30) corrected to official 10:00-22:30 (weekday) / 10:00-23:00 (weekend).
3. Olive Young itinerary hours (08:00-24:00) not confirmed; official Myeongdong Town 10:00-22:30.
4. Day 7 and Day 8 have no detailed plan in the itinerary.
5. Many small businesses (Pig Restaurant 2, Hongojib, Myeongdong Sookhee, Break Silence, Chuncheongol Dakgalbi, Uri Wang Galbitang, Hanjungsun, Eternalog, caricature, Chwihyang, Favorite of Ikseon, Soul Market, Haeundae Market, street food, night markets, tea house) have no official source; hours/addresses left blank and flagged.
6. AREX itinerary "45 min, $7" approximates the All-Stop service (59-66 min, ₩4,750-₩5,350); Express is 43-51 min, ₩13,000.
7. Airport bus itinerary "$13" approximates KAL Limousine (₩18,000); standard airport bus ₩17,000.
8. Myeongdong Kyoja main branch moved to 129 Toegye-ro in 2026; older listings show 29 Myeongdong 10-gil.
9. Haeundae Market, Haeundae Beach hours unverified.

## Log
- 2026-10-21: Session started. Claimed T2-T5.
- 2026-10-21: Data verified and site built; link check passed.
