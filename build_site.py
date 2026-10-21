import json, html, os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "itinerary.json")
PAGES = os.path.join(ROOT, "pages")

with open(DATA) as f:
    data = json.load(f)
entries = data["entries"]

NAV = [
    ("Home", "index.html"),
    ("Transportation", "pages/transportation.html"),
    ("Accommodation", "pages/accommodation.html"),
    ("Attractions", "pages/attractions.html"),
    ("Shopping", "pages/shopping.html"),
    ("Food", "pages/food.html"),
    ("Cafes & Bakeries", "pages/cafes.html"),
    ("Markets", "pages/markets.html"),
    ("Nightlife", "pages/nightlife.html"),
    ("Busan", "pages/busan.html"),
    ("Flagged for Review", "pages/flagged.html"),
    ("All Entries", "pages/all.html"),
]

def nav_html(active, depth=0):
    prefix = "" if depth == 0 else "../"
    out = "<nav>\n"
    for label, href in NAV:
        full = prefix + href
        cls = "active" if href == active else ""
        out += f'  <a href="{full}" class="{cls}">{html.escape(label)}</a>\n'
    out += "</nav>\n"
    return out

def header_html(title, depth=0):
    prefix = "" if depth == 0 else "../"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} - Korea Itinerary</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<header>
  <h1>Korea Itinerary (2 Adult Travelers)</h1>
  <p>Trip window: Oct 31 – Nov 9, 2026 · Seoul (Myeongdong) → Busan (Haeundae). Every row links to an official source where verified.</p>
</header>
{nav_html(title.lower().replace(' ','') , depth)}
"""

# map active by filename
ACTIVE_MAP = {
    "index.html": "index.html",
    "transportation.html": "pages/transportation.html",
    "accommodation.html": "pages/accommodation.html",
    "attractions.html": "pages/attractions.html",
    "shopping.html": "pages/shopping.html",
    "food.html": "pages/food.html",
    "cafes.html": "pages/cafes.html",
    "markets.html": "pages/markets.html",
    "nightlife.html": "pages/nightlife.html",
    "busan.html": "pages/busan.html",
    "flagged.html": "pages/flagged.html",
    "all.html": "pages/all.html",
}

def page_start(title, filename, depth):
    prefix = "" if depth == 0 else "../"
    active = ACTIVE_MAP[filename]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} - Korea Itinerary</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<header>
  <h1>Korea Itinerary (2 Adult Travelers)</h1>
  <p>Trip window: Oct 31 – Nov 9, 2026 · Seoul (Myeongdong) → Busan (Haeundae). Every row links to an official source where verified.</p>
</header>
{nav_html(active, depth)}
<div class="container">
"""

def page_end():
    return "</div>\n<footer>Korea Itinerary site · Data verified against official sources where available; unverified items listed on Flagged for Review.</footer>\n</body>\n</html>\n"

def table_html(rows, show_day=True):
    cols = []
    if show_day:
        cols.append(("Day", "day"))
    cols += [("Item", "item"), ("Area", "area"), ("Hours", "hours"), ("Price", "price"), ("Address", "address"), ("Notes", "notes"), ("Source", "source"), ("Verified", "verified")]
    out = '<div class="table-wrap"><table>\n<tr>'
    for label, _ in cols:
        out += f"<th>{html.escape(label)}</th>"
    out += "</tr>\n"
    for r in rows:
        out += "<tr>"
        if show_day:
            out += f"<td>{html.escape(r.get('day',''))}</td>"
        out += f"<td>{html.escape(r.get('item',''))}</td>"
        out += f"<td>{html.escape(r.get('area',''))}</td>"
        out += f"<td>{html.escape(r.get('hours','') or '')}</td>"
        out += f"<td>{html.escape(r.get('price','') or '')}</td>"
        out += f"<td>{html.escape(r.get('address','') or '')}</td>"
        out += f"<td>{html.escape(r.get('notes','') or '')}</td>"
        src = r.get("source","") or ""
        if src:
            out += f'<td><a class="src" href="{html.escape(src)}" target="_blank" rel="noopener">{html.escape(src)}</a></td>'
        else:
            out += "<td><span class=\"flag\">No official source</span></td>"
        v = r.get("verified", False)
        out += f'<td><span class="badge {"ok" if v else "warn"}">{"Yes" if v else "No"}</span></td>'
        out += "</tr>\n"
    out += "</table></div>\n"
    return out

CAT_PAGES = {
    "Transportation": ("transportation.html", "Transportation"),
    "Accommodation": ("accommodation.html", "Accommodation"),
    "Attractions": ("attractions.html", "Attractions & Sightseeing"),
    "Shopping": ("shopping.html", "Shopping"),
    "Food & Restaurants": ("food.html", "Food & Restaurants"),
    "Cafes & Bakeries": ("cafes.html", "Cafes & Bakeries"),
    "Markets": ("markets.html", "Markets"),
    "Nightlife": ("nightlife.html", "Nightlife & Bars"),
    "Busan": ("busan.html", "Busan (Day 9)"),
}

# Group entries
by_cat = {}
for e in entries:
    by_cat.setdefault(e["category"], []).append(e)

# index
def write_page(filename, title, body, depth):
    path = os.path.join(ROOT, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(page_start(title, filename.split('/')[-1], depth))
        f.write(body)
        f.write(page_end())

# Home
home_body = ""
home_body += '<div class="card"><h2>Overview</h2>'
home_body += '<p>This site organizes a Korea trip for two adult travelers: Seoul (Myeongdong base) Oct 31–Nov 8, 2026, then Busan (Haeundae) Nov 9. Use the navigation above to browse by category. Every table row includes a source link to an official site when the value could be verified; unverified values are left blank and listed on <a href="pages/flagged.html">Flagged for Review</a>.</p></div>\n'
# stats
total = len(entries)
verified = sum(1 for e in entries if e.get("verified"))
flagged = sum(1 for e in entries if e.get("flagged"))
cats = len(by_cat)
home_body += '<div class="stats">'
home_body += f'<div class="stat"><div class="num">{total}</div><div class="lbl">Total entries</div></div>'
home_body += f'<div class="stat"><div class="num">{verified}</div><div class="lbl">Verified rows</div></div>'
home_body += f'<div class="stat"><div class="num">{flagged}</div><div class="lbl">Flagged items</div></div>'
home_body += f'<div class="stat"><div class="num">{cats}</div><div class="lbl">Categories</div></div>'
home_body += '</div>\n'
# analysis
home_body += '<div class="card"><h2>Key analysis & findings</h2><ul>'
home_body += '<li><strong>Day 3 (Tue Nov 3) conflict:</strong> Gyeongbokgung Palace and its Changing of the Guard are CLOSED on Tuesdays. The itinerary schedules the palace on Tue Nov 3 — reschedule to Mon/Wed–Sun.</li>'
home_body += '<li><strong>N Seoul Tower hours corrected:</strong> itinerary said 10:00–10:30; official hours are Weekdays 10:00–22:30, Weekends/Holidays 10:00–23:00; cable car 10:00–23:00.</li>'
home_body += '<li><strong>AREX:</strong> Express train 43 min (T1)/51 min (T2), ₩13,000; All-Stop 59/66 min, ₩4,750/₩5,350. Itinerary’s “45 min, $7” approximates the All-Stop service.</li>'
home_body += '<li><strong>Airport bus:</strong> ₩17,000 standard / ₩18,000 KAL Limousine (itinerary “$13” approximates the KAL fare).</li>'
home_body += '<li><strong>Department stores:</strong> Lotte &amp; Shinsegae Myeongdong open 10:30–20:00 weekdays, 10:30–20:30 weekends (itinerary said 10:30–8:00/8:30, consistent).</li>'
home_body += '<li><strong>Olive Young Myeongdong Town:</strong> 10:00–22:30 daily (itinerary’s 8:00–24:00 not confirmed).</li>'
home_body += '<li><strong>Bukchon Hanok Village:</strong> tourist access restricted to 10:00–17:00 (Red Zone); ₩100,000 fine outside; closed to tourists 17:00–10:00.</li>'
home_body += '<li><strong>Day 7 and Day 8</strong> have no detailed plan in the itinerary; flagged for planning.</li>'
home_body += '<li><strong>Unverified items</strong> (no official source) are left blank and listed on Flagged for Review.</li>'
home_body += '</ul></div>\n'
# day by day summary table
home_body += '<div class="card"><h2>Itinerary by day</h2>'
home_body += '<div class="table-wrap"><table><tr><th>Day</th><th>Date</th><th>Plan</th></tr>'
dayplans = [
 ("Day 1","Sun Oct 31 / Sat Nov 1","SFO → ICN; ICN → Seoul (AREX/bus); check in Stanford Hotel Myeongdong; rest."),
 ("Day 2","Mon Nov 2","N Seoul Tower; Myeongdong shopping; night markets; dinner options."),
 ("Day 3","Tue Nov 3","Gyeongbokgung Palace (CLOSED Tue - conflict); Bukchon; tea house."),
 ("Day 4","Wed Nov 4","Seongsu (Brooklyn of Seoul): Solsot, DDP, shopping, cafes, dinner."),
 ("Day 5","Thu Nov 5","Starfield COEX Mall, Gangnam; Soul Market; Gangnam Style statue."),
 ("Day 6","Fri Nov 6","Ikseondong & Insadong: Chwihyang, Rain Report, Jayeondo salt bread."),
 ("Day 7","Sat Nov 7","Itaewon (no detailed plan provided)."),
 ("Day 8","Sun Nov 8","No plan provided in itinerary."),
 ("Day 9","Mon Nov 9","Seoul → Busan (KTX); check in L7 Haeundae; Haeundae Market street food."),
]
for d,p,plan in dayplans:
    home_body += f"<tr><td>{d}</td><td>{p}</td><td>{html.escape(plan)}</td></tr>\n"
home_body += '</table></div></div>\n'
write_page("index.html", "Home", home_body, 0)

# Category pages
for cat, (fname, title) in CAT_PAGES.items():
    rows = by_cat.get(cat, [])
    body = f'<div class="card"><h2>{html.escape(title)}</h2>'
    body += f'<p>{len(rows)} entries in this category.</p>'
    body += table_html(rows)
    body += '</div>\n'
    write_page("pages/"+fname, title, body, 1)

# All entries
all_body = '<div class="card"><h2>All entries</h2>'
all_body += f'<p>{len(entries)} total entries across all categories.</p>'
all_body += table_html(entries)
all_body += '</div>\n'
write_page("pages/all.html", "All Entries", all_body, 1)

# Flagged page
flagged_rows = [e for e in entries if e.get("flagged")]
flag_body = '<div class="card"><h2>Flagged for Review</h2>'
flag_body += '<p>Items that could not be verified against an official source, plus irregularities found during verification. Unverified values are left blank in the tables. Flagged items do not block the merge.</p>'
flag_body += '<div class="table-wrap"><table><tr><th>Day</th><th>Item</th><th>Category</th><th>Flag / Irregularity</th><th>Source checked</th></tr>\n'
for e in flagged_rows:
    src = e.get("source") or "—"
    flag_body += f"<tr><td>{html.escape(e['day'])}</td><td>{html.escape(e['item'])}</td><td>{html.escape(e['category'])}</td><td class='flag'>{html.escape(e['flagged'])}</td><td>{html.escape(src)}</td></tr>\n"
flag_body += '</table></div></div>\n'
write_page("pages/flagged.html", "Flagged for Review", flag_body, 1)

print("done")
