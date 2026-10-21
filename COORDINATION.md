# Korea itinerary task board

Coordination board created by the integration session because no `COORDINATION.md` existed at task start.

| Task | Status | Owner/session | Files in scope |
|---|---|---|---|
| Official-source verification, itinerary data, responsive GitHub Pages site, integration/build/deploy | in progress | `arena/e8d8cef5-koreatrip2` (current Arena session/branch) | `COORDINATION.md`, `README.md`, `.gitignore`, `.github/workflows/deploy-pages.yml`, `assets/`, `scripts/`, and all root site pages |

## Coordination / ownership

- The repository initially contained only `README.md`; no other task claims or site files were present.
- This session is the final integration session and owns the shared site, navigation, itinerary data, publication workflow and integration. No parallel-session handoff was in progress at claim time.
- Work stays on the fixed Arena branch `arena/e8d8cef5-koreatrip2`. Before each push, run `git pull --rebase` for this branch; do not push a different branch.
- Initial claim commit `1f7a23d chore: claim Korea itinerary integration task` was pushed before research / implementation continued.

## Sources checked (2026-10-21)

Every itinerary table row has a linked official reference and is locally checked for a `data-source="official"` link.

- **Air / rail / hotels:** [SFO flights](https://www.flysfo.com/passengers/flight-info), [Incheon Airport](https://www.airport.kr/ap_en/index.do), AREX [Express](https://www.airportrailroad.com/train/express/introduce), [All-Stop](https://www.airportrailroad.com/train/normal/introduce), [fares](https://www.airportrailroad.com/train/normal/fare), [Airport Limousine 6015](https://airportlimousine.co.kr/en/sub/sub01.php?cat_no=21), Stanford Hotel [FAQ](https://stanford.webhelper.co.kr/myeongdong/en/contents/list/faq), [Korail](https://www.korail.com/global/eng/main).
- **Seoul transit / sights:** [Seoul Metro](https://www.seoulmetro.co.kr/en/cyberStation.do); Visit Seoul pages for [Myeongdong](https://english.visitseoul.net/shopping/Myeong-dong/ENP000067), [Gyeongbokgung](https://english.visitseoul.net/attractions/Gyeongbokgung-Palace_/73?curPage=4), [Bukchon](https://english.visitseoul.net/attractions/Bukchon-Hanok-Village/ENP000261), [Yeonmujang-gil](https://english.visitseoul.net/area/Yeonmujang-gil/ENP7u7jrk), [Seoul Forest](https://english.visitseoul.net/nature/Seoul-Forest/ENP001838), [DDP](https://english.visitseoul.net/attractions/Dongdaemun-Design-Plaza-en/ENP024679), [Ikseon-dong](https://english.visitseoul.net/area/Ikseon-dong/ENP037008), [Insadong](https://english.visitseoul.net/shopping/Insa-dong/ENP000080), [Itaewon](https://english.visitseoul.net/shopping/Itaewon/ENP002077), [Gwangjang](https://english.visitseoul.net/shopping/Gwangjang-Market/ENP000286), [Mangwon](https://english.visitseoul.net/shopping/Mangwon-Market/ENP037950), [Cafe Onion](https://english.visitseoul.net/restaurants/Cafe-Onion/ENP020587), [Hanjungsun](https://english.visitseoul.net/area/hanjungsun/ENPp1q4s4), [Myeongdong Kyoja](https://english.visitseoul.net/area/Myeongdong-Kyoja-EN/ENP008570), [Rain Report Rainbow](https://english.visitseoul.net/restaurants/rainreport/ENP933ykf), [MUSINSA @ Daelim Changgo](https://english.visitseoul.net/shopping/2024-musinsa-daelim/ENPnh3bjr); [Royal Guard ceremony](https://english.visitseoul.net/events/Changing-of-the-Royal-Guard-at-Gyeongbokgung-Palace-en/ENP008256); [Seoul Hanok visitor tips](https://hanok.seoul.go.kr/front/eng/exp/expTip.do); [Seoul Bukchon restrictions](https://english.seoul.go.kr/notice-on-restrictions-for-tourist-visits-to-bukchon-special-management-area-effective-from-november-2024/); N Seoul Tower [hours](https://www.nseoultower.co.kr/eng/visit/use.asp), [admission](https://www.nseoultower.co.kr/eng/visit/use2.asp), [shuttle buses](https://www.nseoultower.co.kr/eng/visit/traffic.asp), [cable car](https://www.nseoultower.co.kr/eng/visit/traffic2.asp); Starfield [Library](https://m.starfield.co.kr/coexmall/library/intro?lang=en), [COEX metro directions](https://www.starfield.co.kr/coexmall/about/directions.do?type=metro), [Visit Gangnam MICE](https://visitgangnam.net/en/about/mice).
- **Business operators / brands:** [Cafe Onion](https://m.onionkr.com/artfinger/offline.html?cate_no=26), [Crystal Jade Sogong](https://www.crystaljade.co.kr/menu/menuInfo.do?shSq=20&shGb=A), [MUSINSA STANDARD](https://locations.musinsa.com/en/stndss), [MARGESHERWOOD](https://global.margesherwood.com/pages/stockist-official), [Eternalog](http://eternalog-fotobooth.com/), [Blue Elephant](https://en.blueelephant.co/product/space-seongsu/4552/), [ADERERROR](https://m.en.adererror.com/10th_anniversary.html), [Brandy Melville locator](https://locations.brandymelville.com/), [VisitKorea Myeongdong Kyoja record](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=99925), [company locator](http://www.mdkj.co.kr/en/restaurant/location.php). First-party social accounts for FAR BEN, Solsot and Hanjungsun are linked on the food page.
- **Busan:** [Busan Metro planner](https://www2.humetro.busan.kr/homepage/cyberstation/mapeng.do), [Busan City Haeundae Beach](https://www.busan.go.kr/eng/beaches/1325815), Visit Busan [beach](https://www.visitbusan.net/en/index.do?lang_cd=en&menuCd=DOM_000000303011001000&uc_seq=373), [market](https://www.visitbusan.net/en/index.do?lang_cd=en&menuCd=DOM_000000303011001000&uc_seq=294), [food stalls](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000302003001000&uc_seq=316), [L7 Haeundae](https://www.lottehotel.com/haeundae-l7/en).
- **Calendar reference:** [VisitKorea 2026 holidays](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140038) is a manual year-specific source only; it is not used to infer the trip year.

## Findings / irregularities

- Preserve date strings exactly: “Oct. 31/Nov. 1,” “Nov. 2–9 Monday–Monday,” “Nov 2, 2006.” No year or day mapping inferred; the empty itinerary day is retained.
- “Day 3 · Tuesday” conflicts with Gyeongbokgung’s normal Tuesday closure; a holiday substitution depends on the actual year. Guard Ceremony is listed 10:00 / 14:00 except Tuesdays and may be cancelled for weather.
- Stanford Hotel Myeongdong: 84 Namdaemun-ro; check-in after 15:00 / check-out before 12:00; official FAQ lists 6015 at about 80 minutes and ₩17,000 adult fare, plus airport stop / schedule information. Recheck operator timetable. L7 Haeundae: 55 Haeun-daero 570beon-gil; check-in 15:00 / check-out 11:00.
- AREX Express: 43 / 51 minutes T1 / T2 and ₩13,000 adult fare. All-Stop: 59 / 66 minutes (some trains +2–6 minutes); fares are in the current official fare table. These are snapshots, not promised trip-day totals.
- N Seoul Tower adult observatory admission: ₩29,000; cable car separate. Shuttle 01A / 01B listed at ₩1,500 transit-card only. Supplied USD “$31” is not an official ticket value or verified conversion.
- Gyeongbokgung Nov–Dec: 09:00–17:00, last entry 1 hour before close; adult foreign visitor admission listed ₩3,000. Bukchon current guide: 10:00–17:00 with 17:00–10:00 restricted hours in the designated zone. DDP: daily 10:00–20:00, closed Jan. 1 / Lunar New Year / Chuseok, space hours vary. Starfield Library: 10:30–22:00.
- Gwangjang: main market 09:00–18:00 (closed Sunday), food alley 09:00–23:00 year-round, Guje shopping street 10:00–19:00 (closed Sunday). Mangwon: daily 10:00–21:00, varies by store.
- Myeongdong Kyoja English / Korean addresses differ in VisitKorea. Cafe Onion weekend opening conflicts (brand 10:00; Visit Seoul 09:00). Exact values remain blank and flagged.
- Haeundae Beach: Busan City says about 5 minutes from Line 2 Exit 3 / 5; Visit Busan says 15 minutes from Exit 5. Walk time intentionally blank. Visit Busan lists daily 09:00–18:00 / free admission; Busan City page does not list hours. Food-stall hours / fees vary.
- Exact flight / KTX details, hotel-to-station walks, route-specific Busan Metro fare / duration, and some brand / restaurant branch details are unverified. Rain Report Rainbow is in Ikseon-dong / Jongno (not Seongsu). MUSINSA STANDARD and MUSINSA STORE @ Daelim Changgo are separate. Blue Elephant, ADERERROR retail and Brandy Melville Korea details remain unverified.

## Checks, handoffs and publication

- `python3 scripts/check_site.py` — passed at last run: 7 HTML pages, 82 sourced table rows; local links / fragments / assets validated. Re-run after edits.
- `python3 scripts/build_site.py` — passed; stages only public HTML and `assets/` into ignored `site-build/` for Pages.
- `git diff --check` — passed at last run; re-run before commit.
- The local check validates source-link presence, not future availability of external pages. Links are for manual review.
- Handoffs: none. Final integration / publication owned by `arena/e8d8cef5-koreatrip2`.
- Pull request / merge / Pages deployment: pending. After merge, verify Actions and Pages status / URL, then record PR number, merge SHA, workflow run and deployed URL here.
