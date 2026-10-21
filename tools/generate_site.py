#!/usr/bin/env python3
"""Generate Koreatrip2 static site from data/itinerary.json + data/verification.md."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "pages")
os.makedirs(PAGES, exist_ok=True)

with open(os.path.join(ROOT, "data/itinerary.json"), encoding="utf-8") as f:
    DATA = json.load(f)

TRIP = DATA["trip"]
DAYS = DATA["days"]

# Official source links per entry id (from verification session)
SOURCES = {
    "d1i2a": [("AREX official — ticketing & fares", "https://www.airportrailroad.com/ticket/rsv"),
              ("Seoul Metropolitan Government — airport transport", "https://english.seoul.go.kr/service/entry/getting-to-seoul-from-incheon-airport/")],
    "d1i2b": [("Airport Limousine official — route guide", "https://www.airportlimousine.co.kr/en/sub/sub01.php"),
              ("Incheon Airport — bus fares", "https://www.airport.kr/ap_en/6636/subview.do")],
    "d2i1b": [("N Seoul Tower official — hours", "https://www.nseoultower.co.kr/eng/visit/use.asp"),
              ("N Seoul Tower official — admission & ticketing", "https://www.nseoultower.co.kr/eng/visit/use2.asp"),
              ("N Seoul Tower official — cable car", "https://www.nseoultower.co.kr/eng/visit/traffic2.asp"),
              ("VISITKOREA — N Seoul Tower", "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=88026")],
    "d2i1": [("Seoul Off Script — getting to N Seoul Tower (bus/cable car)", "https://www.seouloffscript.com/article/namsan-tower-getting-there")],
    "d2i2a": [("LOTTE Department Store official — Myeongdong Main", "https://m.global.lotteshopping.com/eng/store/main"),
              ("VISITKOREA — Lotte Department Store Myeongdong Main", "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=106961")],
    "d2i2b": [("VISITKOREA — Olive Young Myeongdong Main Branch", "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=148763"),
              ("Olive Young Myeongdong Town", "https://myeongdongtown.oliveyoung.com/en/")],
    "d2i3": [("VISITKOREA — Gwangjang Market", "https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=106345"),
              ("Visit Seoul — Gwangjang Market", "https://english.visitseoul.net/shopping/gwangjang-market_/287")],
    "d3i1": [("VISITKOREA — Gyeongbokgung Palace", "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=87740")],
    "d3i1b": [("VISITKOREA — Gyeongbokgung Palace", "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=87740"),
              ("VISITKOREA — Royal Guard Changing Ceremony", "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=124533")],
    "d5i1": [("Seoul Metro — subway info", "https://www.seoulmetro.co.kr")],
    "d5": [("Starfield COEX Mall official", "https://www.starfield.co.kr/coexmall/main.do"),
           ("VISITKOREA — Starfield COEX Mall", "https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=73375")],
    "d9i3": [("Korail Let's Korail (official booking)", "https://www.letskorail.com"),
             ("Korea Go Now — KTX Seoul to Busan guide", "https://koreagonow.com/seoul-to-busan-ktx-guide/")],
    "d9i5": [("Lotte Hotels & Resorts — official", "https://www.lottehotel.com/")],
    "d9i6": [("L7 Haeundae location reviews (1-min walk to Haeundae Beach)", "https://www.tripadvisor.com/ShowUserReviews-g297884-d27938643-r976401526-L7_Haeundae-Busan.html")],
    "d9i7": [("VISITKOREA — Busan Haeundae Market", "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=84963"),
             ("Visit Busan — Haeundae Market", "https://www.visitbusan.net/index.do?menuCd=DOM_000000301003001000&uc_seq=294&lang_cd=en")],
}

# Verification status per entry id
STATUS = {
    "d1i1": "blank", "d1i2a": "partial", "d1i2b": "partial", "d1i3": "blank", "d1i3a": "unverified",
    "d2i1": "unverified", "d2i1b": "partial", "d2i2": "unverified", "d2i2a": "verified", "d2i2b": "unverified",
    "d2i2c": "unverified", "d2i3": "partial", "d2i3d1": "unverified", "d2i3d2": "unverified",
    "d2i3d3": "unverified", "d2i3d4": "unverified", "d2i3b": "unverified",
    "d3i1": "verified", "d3i1b": "verified", "d3i2": "unverified", "d3i3": "unverified",
    "d3i3a": "unverified", "d3i4": "unverified",
    "d4i1": "unverified", "d4i2": "unverified", "d4i3": "unverified", "d4i4": "unverified",
    "d4i5": "unverified", "d4i6": "unverified", "d4i6a": "unverified", "d4i6b": "unverified",
    "d4i6c": "unverified", "d4i6d": "unverified", "d4i7": "unverified", "d4i8": "unverified", "d4i9": "unverified",
    "d5i1": "unverified", "d5i2": "unverified", "d5i3": "unverified",
    "d6i1": "unverified", "d6i2": "unverified", "d6i3": "unverified", "d6i4": "unverified",
    "d7i1": "unverified", "d8i1": "unverified",
    "d9i1": "blank", "d9i2": "unverified", "d9i3": "partial", "d9i4": "unverified",
    "d9i5": "verified", "d9i6": "partial", "d9i7": "verified",
}

# Extra verification notes per entry (short)
NOTES = {
    "d1i2a": "Itinerary: 45 min / $7. Official: Express ~43 min (T1), adult ₩13,000 (~$9.30); all-stop ~59–66 min, ~₩4,750 (~$3.40). $7 matches neither.",
    "d1i2b": "Itinerary: $13. Official route 6015 to Myeongdong: ₩17,000 (~$12.10); premium ₩18,000 (~$12.80); ~60–80 min.",
    "d2i1b": "Itinerary hours '10:00–10:30' conflict with official: observatory weekdays 10:00–22:30, weekends 10:00–23:00; cable car 10:00–23:00. Combined cable car + observatory ≈ ₩44,000 ≈ $31.40, matching the ~$31 estimate.",
    "d2i2a": "Matches Lotte official hours (weekdays 10:30–20:00, weekends 10:30–20:30).",
    "d2i2b": "Itinerary 8:00–midnight conflicts with official 10:00–22:30.",
    "d2i3": "Official Gwangjang food street closes 23:00; 'until 2:00am' unverified.",
    "d3i1": "Matches official. BUT Day 3 is a Tuesday — palace closed Tuesdays (irregularity).",
    "d3i1b": "Matches official 10:00 & 14:00, closed Tuesdays (same conflict).",
    "d5": "Mall hours 10:30–22:00 daily (official). Subway time 47 min not from official source.",
    "d9i3": "Official KTX Seoul–Busan: ~2h15m fastest, ~2h30–2h45m typical; standard fare ~₩54,400–59,800. Itinerary time plausible.",
    "d9i5": "Hotel exists at 55 Haeun-daero 570beon-gil, Haeundae-gu, Busan; ~1-min walk to Haeundae Beach.",
    "d9i6": "Walking time not from official source.",
    "d9i7": "Official market hours 09:00–22:00, varies by store.",
}

BADGE_CSS = {
    "verified": "ok", "partial": "partial", "blank": "blank", "unverified": "unverified",
}

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def val(v):
    return esc(v) if v not in (None, "") else "—"

def sources_html(entry_id):
    links = SOURCES.get(entry_id, [])
    if not links:
        return '<span style="color:#6b7280;font-size:0.75rem">— no official source</span>'
    parts = []
    for label, url in links:
        parts.append(f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(label)}</a>')
    return "<br>".join(parts)

def row_html(entry, day_num):
    eid = entry["id"]
    status = STATUS.get(eid, "unverified")
    badge = BADGE_CSS.get(status, "unverified")
    irr = entry.get("irregularity")
    irr_html = ""
    if irr:
        irr_html = f'<br><span style="color:#991b1b;font-size:0.78rem;font-weight:700">⚠ {esc(irr)}</span>'
    note = NOTES.get(eid, "")
    note_html = f'<br><span style="color:#4b5563;font-size:0.78rem">Verification: {esc(note)}</span>' if note else ""
    return (f"<tr>"
            f"<td>{day_num}</td>"
            f"<td><strong>{esc(entry['item'])}</strong>{irr_html}{note_html}</td>"
            f"<td>{esc(entry['category'])}</td>"
            f"<td>{val(entry.get('details'))}</td>"
            f"<td>{val(entry.get('time'))}</td>"
            f"<td>{val(entry.get('cost'))}</td>"
            f"<td>{val(entry.get('hours'))}</td>"
            f"<td class='source'>{sources_html(eid)}</td>"
            f"<td class='status'><span class='badge {badge}'>{status}</span></td>"
            f"</tr>")

def page_shell(title, body, active):
    # href values are site-root paths; active is compared against them
    nav_items = [
        ("/", "Home"),
        ("/pages/day-by-day.html", "Day-by-Day"),
        ("/pages/transportation.html", "Transportation"),
        ("/pages/accommodation.html", "Accommodation"),
        ("/pages/food.html", "Food & Markets"),
        ("/pages/shopping.html", "Shopping & Cafes"),
        ("/pages/activities.html", "Activities"),
        ("/pages/flagged.html", "Flagged for Review"),
    ]
    nav = ""
    for href, label in nav_items:
        aclass = ' class="active"' if href == active else ""
        nav += f'<a{aclass} href="{href}">{label}</a>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} — Korea Trip Itinerary</title>
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <h1>Korea Trip Itinerary</h1>
    <p class="sub">Two adults &bull; Seoul (Myeongdong) &rarr; Busan (Haeundae) &bull; Oct 31 – Nov 9, 2026</p>
  </div>
</header>
<nav class="navbar">{nav}</nav>
<div class="container" id="content">
{body}
<div class="site-footer">
  <div class="wrap">
    <p><strong>Source data:</strong> itinerary supplied by the trip organizers; see <a href="/data/itinerary.json">data/itinerary.json</a> and <a href="/data/verification.md">data/verification.md</a>.</p>
    <p><strong>Disclaimer:</strong> Planning aid compiled from public sources and the user-provided itinerary. Hours, prices, and operating days change — confirm on the official venue/site before visiting. Unverified values were intentionally left blank; nothing was inferred or made up.</p>
    <p>GitHub: <a href="https://github.com/buffedlizard55-lab/Koreatrip2">buffedlizard55-lab/Koreatrip2</a></p>
  </div>
</div>
</div>
</body>
</html>"""

def table_wrap(caption, rows_html):
    head = ("<thead><tr>"
            "<th>Day</th><th>Item</th><th>Category</th><th>Details</th><th>Time</th><th>Cost</th><th>Hours</th>"
            "<th class='source'>Official source</th><th class='status'>Status</th>"
            "</tr></thead>")
    return (f"<p>{esc(caption)}</p>"
            f"<div class='table-wrap'><table>{head}<tbody>{rows_html}</tbody></table></div>")

def day_block(day):
    items = "".join(row_html(it, day["day"]) for it in day["items"])
    base = day.get("base", "")
    dates = day.get("dates", "")
    return (f"<div class='day-section'>"
            f"<div class='day-header'><strong>{esc(day['label'])}</strong><span class='dates'>{esc(dates)} &bull; {esc(base)}</span></div>"
            f"<table><thead><tr><th>Item</th><th>Category</th><th>Details</th><th>Time</th><th>Cost</th><th>Hours</th>"
            f"<th class='source'>Official source</th><th class='status'>Status</th></tr></thead><tbody>{items}</tbody></table>"
            f"</div>")

# ---------- Day-by-day ----------
body = "<h2 id='content'>Day-by-Day Plan</h2>"
body += "<p class='small'>All entries transcribed line-by-line from the itinerary. Every row shows its official source link (or '— no official source') and verification status. Unverified values were left blank.</p>"
for day in DAYS:
    body += day_block(day)
with open(os.path.join(PAGES, "day-by-day.html"), "w", encoding="utf-8") as f:
    f.write(page_shell("Day-by-Day Plan", body, "/pages/day-by-day.html"))

# ---------- Category pages ----------
CATEGORY_ORDER = ["Transportation", "Accommodation", "Food", "Restaurant", "Cafe", "Bar",
                  "Shopping", "Activity"]
CAT_LABELS = {
    "Transportation": "Transportation",
    "Accommodation": "Accommodation",
    "Food": "Food & Street Food",
    "Restaurant": "Restaurants",
    "Cafe": "Cafes",
    "Bar": "Bars & Nightlife",
    "Shopping": "Shopping",
    "Activity": "Activities & Sights",
}

def cat_pages():
    specs = [
        ("transportation", ["Transportation"], "Transportation", "transportation.html",
          "All transport entries: airport transfers, KTX, subway.", "transportation.html"),
        ("accommodation", ["Accommodation"], "Accommodation", "accommodation.html",
          "Hotels: Stanford Hotel Myeongdong and L7 Haeundae.", "accommodation.html"),
        ("food", ["Food", "Restaurant", "Bar"], "Food & Markets", "food.html",
          "Restaurants, cafes (incl. Insadong/Seongsu), markets, and street food.", "food.html"),
        ("shopping", ["Cafe", "Shopping"], "Shopping & Cafes", "shopping.html",
          "Coffee shops, dessert stops, shops, department stores, and markets.", "shopping.html"),
        ("activities", ["Activity"], "Activities & Sights", "activities.html",
          "Palaces, observation deck, markets, and experiences.", "activities.html"),
    ]
    pages = {fname: [] for _, _, _, _, _, fname in specs}
    for page_key, cats, title, active, caption, fname in specs:
        rows = []
        for day in DAYS:
            for it in day["items"]:
                if it["category"] in cats:
                    rows.append(row_html(it, day["day"]))
        pages[fname].append((title, caption, "".join(rows) if rows else
                             "<tr><td colspan='9' style='text-align:center;color:#6b7280;padding:2rem'>No entries in this category.</td></tr>"))
    for page_key, cats, title, active, caption, fname in specs:
        blocks = ""
        for t, c, r in pages[fname]:
            blocks += (f"<h2 id='content'>{t}</h2>"
                       f"<p class='small'>{c}</p>"
                       f"{table_wrap(t, r)}")
        with open(os.path.join(PAGES, fname), "w", encoding="utf-8") as f:
            f.write(page_shell(title, blocks, active))

cat_pages()

# ---------- Flagged page ----------
flag_items = [
    ("SCHEDULE CONFLICT — Gyeongbokgung closed on Day 3",
     "Day 3 (Tuesday, Nov 3, 2026) schedules Gyeongbokgung Palace and the changing-of-the-guard ceremony, but the palace is closed on Tuesdays (ceremony suspended too).",
     "VISITKOREA: https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=87740",
     "Move the palace visit to another day (e.g. Day 4, 5, 6, 8, or 9 in Seoul) or swap Day 3 with a non-Tuesday."),
    ("Typo — Day 2 date",
     "Itinerary says 'Nov 2, 2006'. The trip is Oct–Nov 2026; Nov 2, 2026 is a Monday, matching the 'Monday' label.",
     "Calendar check",
     "Should read Nov 2, 2026."),
    ("Date/day mismatch — Day 1",
     "Itinerary labels Day 1 as Sunday with 'Oct.31/Nov 1'. In 2026, Oct 31 is a Saturday and Nov 1 is a Sunday.",
     "Calendar check",
     "Travel date is likely Sunday, Nov 1, 2026 (flight SFO→ICN typically arrives Nov 1 due to date line)."),
    ("N Seoul Tower hours",
     "Itinerary lists observatory/cable car hours as '10:00–10:30', which looks truncated.",
     "Official: https://www.nseoultower.co.kr/eng/visit/use.asp",
     "Official: observatory weekdays 10:00–22:30, weekends/holidays 10:00–23:00, last entry 30 min before close. Cable car 10:00–23:00 (weather permitting)."),
    ("Olive Young hours",
     "Itinerary lists 8:00–12:00am (8am–midnight).",
     "Official: https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=148763",
     "Official Olive Young Myeongdong Main: 10:00–22:30 daily."),
    ("AREX fare",
     "Itinerary: 45 min, $7.",
     "Official: https://www.airportrailroad.com/ticket/rsv",
     "Official Express: ~43 min (T1) to Seoul Station, adult ₩13,000 (~$9.30). All-stop: ~59–66 min, ~₩4,750 (~$3.40). $7 matches neither."),
    ("Limousine bus fare",
     "Itinerary: $13.",
     "Official: https://www.airportlimousine.co.kr/en/sub/sub01.php",
     "Official route 6015 (airport→Myeongdong): ₩17,000 (~$12.10); premium ₩18,000 (~$12.80); ~60–80 min traffic-dependent."),
    ("Gwangjang Market late hours",
     "Itinerary: 'some food stalls open until 2:00 a.m.'",
     "Official: https://english.visitseoul.net/shopping/gwangjang-market_/287",
     "Official food street: 09:00–23:00 daily; general market 09:00–18:00 Mon–Sat, closed Sundays. 2am claim unverified."),
    ("Unverified small venues",
     "Dozens of restaurants, cafes, bars, and shops (e.g. Pig Restaurant 2, Myeongdong Kyoja, Crystal Jade, Hongojib, Myeongdong Sookhee, Chwihyang, Jayeondo, Break Silence, Chuncheongol Dakgalbi, Uri Wang Galbitang, Seongsu shopping list) have no official English source found in this session.",
     "—",
     "Verify via Kakao Map / Naver Map or the venue's Instagram before visiting. Left blank intentionally — nothing inferred."),
    ("KTX boarding tip",
     "Itinerary says 'board 45 minutes early to secure luggage space' and '45 miuntes' (typo).",
     "Official: https://www.letskorail.com",
     "KTX Seoul–Busan takes ~2h15m–2h45m depending on stops; standard fare ~₩54,400–59,800. Arriving early is sensible; confirm luggage policy on booking."),
    ("Empty days",
     "Day 7 (Itaewon, Sat Nov 7) and Day 8 (Sun Nov 8) have no planned entries.",
     "—",
     "Fill in or mark as free days."),
]

rows = ""
for title, desc, src, action in flag_items:
    rows += (f"<div class='flag-item'>"
             f"<h4>{esc(title)}</h4>"
             f"<p>{esc(desc)}</p>"
             f"<p><strong>Source:</strong> {esc(src)}</p>"
             f"<p><strong>Suggested action:</strong> {esc(action)}</p>"
             f"</div>")

body = ("<h2 id='content'>Flagged for Review</h2>"
        "<p>Irregularities, conflicts, and values that could not be confirmed from an official source. "
        "These do not block the trip plan but should be reviewed before traveling.</p>"
        + rows)
with open(os.path.join(PAGES, "flagged.html"), "w", encoding="utf-8") as f:
    f.write(page_shell("Flagged for Review", body, "/pages/flagged.html"))

print("Site generated.")
print("Pages:", sorted(os.listdir(PAGES)))
