"""Render the last year of GitHub contributions as a lidar-style radar SVG.

Usage: GITHUB_TOKEN=... python3 scripts/activity.py [login] [out.svg]
Standard library only, so the workflow needs no install step.
"""

import datetime as dt
import json
import math
import os
import sys
import urllib.request

LOGIN = sys.argv[1] if len(sys.argv) > 1 else "yigitozc"
OUT = sys.argv[2] if len(sys.argv) > 2 else "assets/activity.svg"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
    repositories(ownerAffiliations: OWNER, privacy: PUBLIC) { totalCount }
  }
}
"""

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={
            "Authorization": f"bearer {os.environ['GITHUB_TOKEN']}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    if "errors" in body:
        raise SystemExit(body["errors"])
    return body["data"]["user"]


def level(count, cuts):
    if not count:
        return 0
    return 1 + sum(count > c for c in cuts)


def render(user):
    cal = user["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    active = sum(1 for d in days if d["contributionCount"])

    nonzero = sorted(d["contributionCount"] for d in days if d["contributionCount"])
    cuts = [nonzero[len(nonzero) * q // 4] for q in (1, 2, 3)] if nonzero else [0, 0, 0]

    by_weekday = [0] * 7
    for d in days:
        by_weekday[dt.date.fromisoformat(d["date"]).weekday()] += d["contributionCount"]
    busiest = WEEKDAYS[by_weekday.index(max(by_weekday))] if any(by_weekday) else "—"

    cx, cy, r0, r1 = 200, 180, 46, 150
    sizes = [1.4, 2.6, 3.4, 4.2, 5.2]
    alphas = [0.35, 0.45, 0.65, 0.85, 1]
    dots = []
    for wi, week in enumerate(weeks):
        ang = -math.pi / 2 + 2 * math.pi * wi / len(weeks)
        for d in week["contributionDays"]:
            ring = dt.date.fromisoformat(d["date"]).weekday()
            rad = r0 + (r1 - r0) * ring / 6
            lv = level(d["contributionCount"], cuts)
            color = "#2ee6c5" if lv else "#2a3a66"
            dots.append(
                f'<circle cx="{cx + rad * math.cos(ang):.1f}" cy="{cy + rad * math.sin(ang):.1f}" '
                f'r="{sizes[lv]}" fill="{color}" fill-opacity="{alphas[lv]}">'
                f"<title>{d['date']}: {d['contributionCount']}</title></circle>"
            )

    rings = "".join(
        f'<circle cx="{cx}" cy="{cy}" r="{r0 + (r1 - r0) * i / 6:.1f}" class="ring"/>' for i in range(7)
    )
    stats = [
        ("Contributions · last 12 months", f"{cal['totalContributions']:,}"),
        ("Active days", str(active)),
        ("Most active day", busiest),
        ("Public repositories", str(user["repositories"]["totalCount"])),
    ]
    rows = []
    for i, (label, value) in enumerate(stats):
        x, y = 430 + (i % 2) * 360, 96 + (i // 2) * 88
        rows.append(f'<text x="{x}" y="{y}" class="label">{label}</text>')
        rows.append(f'<text x="{x}" y="{y + 38}" class="value">{value}</text>')

    updated = dt.date.today().isoformat()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="1200" height="360" role="img" aria-label="GitHub activity of {LOGIN}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#070b16"/><stop offset="1" stop-color="#0f1b33"/>
    </linearGradient>
    <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#2ee6c5" stop-opacity="0"/><stop offset="1" stop-color="#2ee6c5" stop-opacity=".35"/>
    </linearGradient>
  </defs>
  <style>
    .ring {{ fill: none; stroke: #18254a; }}
    .label {{ font: 500 15px ui-monospace, 'JetBrains Mono', Consolas, monospace; fill: #8ea2c9; }}
    .value {{ font: 700 32px 'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif; fill: #f1f5ff; }}
    .title {{ font: 600 18px ui-monospace, 'JetBrains Mono', Consolas, monospace; fill: #2ee6c5; }}
    .foot {{ font: 400 13px ui-monospace, Consolas, monospace; fill: #5b6f99; }}
    .sweep {{ transform-origin: {cx}px {cy}px; animation: spin 6s linear infinite; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  </style>
  <rect width="1200" height="360" rx="18" fill="url(#bg)"/>
  {rings}
  <path class="sweep" d="M{cx} {cy} L{cx + r1 + 8} {cy} A{r1 + 8} {r1 + 8} 0 0 0 {cx + (r1 + 8) * math.cos(-0.6):.1f} {cy + (r1 + 8) * math.sin(-0.6):.1f} Z" fill="url(#sweep)"/>
  {''.join(dots)}
  <circle cx="{cx}" cy="{cy}" r="5" fill="#2ee6c5"/>
  <text x="430" y="48" class="title">&gt; activity scan</text>
  {''.join(rows)}
  <text x="790" y="272" class="foot">one ring per weekday · one spoke per week</text>
  <text x="790" y="294" class="foot">updated {updated}</text>
</svg>
"""


if __name__ == "__main__":
    svg = render(fetch())
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT}")
