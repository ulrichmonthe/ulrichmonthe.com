"""Generate per-foundation pages — SPEC.md §4.1.

One static page per publishable foundation at /foundations/[slug]/, plus an
index. These are the pages search traffic lands on, and the thing you link to
when you want to point at a single funder.

Copy rule (SPEC §0.2): decision-relevant facts with the context needed to read
them. No imperative about a named real foundation, ever.

Run: python3 standing/build_pages.py
"""

from __future__ import annotations

import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(HERE, "data")
OUT = os.path.join(ROOT, "foundations")
BASE = "https://ulrichmonthe.com"

BAND_CLASS = {
    "Adds new grantees regularly": "reg",
    "Adds new grantees occasionally": "occ",
    "Rarely funds new grantees": "rare",
}


def e(x):
    return html.escape(str(x if x is not None else ""), quote=True)


def money(n):
    return "$" + format(int(round(n)), ",") if n else "—"


def pct(n):
    return "—" if n is None else f"{n * 100:.1f}%"


def meta_description(d, m):
    """Assemble and MEASURE — SPEC §4.1 requires 120-160 chars."""
    name = d["name"]
    yr = d["window"]["latest_eligible_year"]
    full = (f"{name} funded {m['total_grantee_count_latest']} organizations in FY{yr}; "
            f"{m['new_grantee_count_latest']} were new. Grant sizes, recipients and "
            f"application status from IRS filings.")
    if len(full) <= 160:
        if len(full) >= 120:
            return full
        return full + " Free, no login."
    short = (f"{name} funded {m['total_grantee_count_latest']} organizations in FY{yr}; "
             f"{m['new_grantee_count_latest']} were new. From IRS Form 990-PF filings.")
    if len(short) <= 160:
        return short
    return short[:157].rsplit(" ", 1)[0] + "…"


def title_for(name):
    t = f"{name} — Grant History"
    if len(t) <= 60:
        return t
    return (name[:57] + "…") if len(name) > 60 else name


HEAD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{base}/og-image.png">
  <script type="application/ld+json">{jsonld}</script>
  <script defer src="https://cloud.umami.is/script.js" data-website-id="86c99d21-f829-492f-b06e-4428c6a72181"></script>
  <script defer src="/scripts/track.js"></script>
  <script defer src="/scripts/notify.js"></script>
  <style>
    :root {{
      --ink:#1c1a17; --ink-soft:#5b554c; --paper:#f5f1e8; --paper-raised:#fbf9f3;
      --paper-deep:#ede7d9; --accent:#a8763e; --accent-deep:#8a5f30;
      --accent-soft:#efe6d6; --rule:#e2dbcb; --green:#3d6b48; --red:#9a4a32;
      --serif:"Newsreader","Iowan Old Style",Georgia,serif;
      --sans:"Instrument Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
      --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
    }}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:var(--sans);background:var(--paper);color:var(--ink);line-height:1.65;font-size:16px;-webkit-font-smoothing:antialiased}}
    .wrap{{max-width:820px;margin:0 auto;padding:0 24px}}
    nav{{font-size:14px;display:flex;justify-content:space-between;align-items:center;padding:26px 0}}
    nav .mark{{display:inline-flex;align-items:center;gap:11px;text-decoration:none;color:var(--ink)}}
    .mark-mono{{font-family:var(--serif);font-size:17px;font-weight:600;color:var(--paper);background:var(--accent);width:31px;height:31px;border-radius:7px;display:inline-flex;align-items:center;justify-content:center}}
    .mark-name{{font-family:var(--serif);font-size:20px;font-weight:500}}
    nav ul{{display:flex;gap:24px;list-style:none}}
    nav ul a{{color:var(--ink-soft);text-decoration:none}}
    .crumb{{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-soft);padding-top:22px}}
    .crumb a{{color:var(--accent-deep);text-decoration:none}}
    h1{{font-family:var(--serif);font-size:clamp(28px,4.4vw,40px);font-weight:600;line-height:1.15;letter-spacing:-.015em;margin:12px 0 10px}}
    .sub{{font-family:var(--mono);font-size:12.5px;color:var(--ink-soft);letter-spacing:.03em}}
    .band{{display:inline-block;font-size:11.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;padding:5px 12px;border-radius:100px;margin-top:16px}}
    .band.reg{{background:#e3ecdd;color:var(--green)}}
    .band.occ{{background:var(--accent-soft);color:var(--accent-deep)}}
    .band.rare{{background:#f2e0da;color:var(--red)}}
    .band.none{{background:var(--paper-deep);color:var(--ink-soft)}}
    .lead{{font-family:var(--serif);font-size:21px;line-height:1.5;margin:20px 0 8px;max-width:60ch}}
    .peer{{font-size:15px;color:var(--ink-soft);max-width:62ch}}
    section{{padding:34px 0 0}}
    h2{{font-family:var(--serif);font-size:22px;font-weight:600;margin-bottom:12px}}
    p{{color:var(--ink-soft);max-width:64ch}}
    p+p{{margin-top:11px}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:18px 24px;margin:6px 0 4px}}
    .m-l{{font-size:11.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-soft)}}
    .m-v{{font-family:var(--mono);font-size:19px;margin-top:3px;font-variant-numeric:tabular-nums}}
    .m-n{{font-size:13px;color:var(--ink-soft);margin-top:2px}}
    .tablewrap{{overflow-x:auto}}
    table{{width:100%;border-collapse:collapse;font-size:14.5px;margin-top:8px}}
    th{{text-align:left;font-size:11.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-soft);border-bottom:1px solid var(--rule);padding:8px 10px 8px 0}}
    td{{border-bottom:1px solid var(--rule);padding:9px 10px 9px 0;color:var(--ink-soft)}}
    td.n{{font-family:var(--mono);text-align:right;color:var(--ink);font-variant-numeric:tabular-nums}}
    td.name{{color:var(--ink)}}
    .newtag{{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-deep);background:var(--accent-soft);padding:2px 8px;border-radius:100px;margin-left:8px}}
    .prov{{font-family:var(--mono);font-size:12px;color:#9a927f;line-height:1.75;border-top:1px solid var(--rule);padding-top:14px;margin-top:26px}}
    .prov b{{color:var(--ink-soft)}}
    .notice{{background:var(--paper-deep);border-radius:10px;padding:18px 22px;margin-top:16px;font-size:15px;color:var(--ink-soft);max-width:66ch}}
    .notice b{{color:var(--ink)}}
    .cta{{margin:38px 0 8px;background:linear-gradient(155deg,#2a2218 0%,#1c1a17 100%);border-radius:12px;padding:30px 34px;color:var(--paper)}}
    .cta h3{{font-family:var(--serif);font-size:21px;font-weight:600;margin-bottom:10px;color:var(--paper)}}
    .cta p{{color:#d8d0c2;max-width:60ch;font-size:15.5px}}
    .cta a{{color:var(--accent-soft)}}
    ul.dir{{list-style:none;columns:2;column-gap:32px}}
    ul.dir li{{break-inside:avoid;padding:5px 0;border-bottom:1px solid var(--rule);display:flex;justify-content:space-between;gap:12px;align-items:baseline}}
    ul.dir a{{color:var(--accent-deep);text-decoration:none;font-size:15px}}
    ul.dir a:hover{{text-decoration:underline}}
    .dir-meta{{font-family:var(--mono);font-size:12px;color:#9a927f;white-space:nowrap}}
    @media(max-width:620px){{ul.dir{{columns:1}}}}
    .links{{display:flex;flex-wrap:wrap;gap:9px;margin-top:16px}}
    .links a{{font-size:14px;text-decoration:none;border:1px solid var(--rule);border-radius:100px;padding:7px 15px;background:var(--paper-raised);color:var(--accent-deep)}}
    footer{{margin-top:54px;border-top:1px solid var(--rule);padding:24px 0 46px;font-size:13.5px;color:var(--ink-soft);display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px}}
    footer a{{color:var(--accent-deep);text-decoration:none}}
    @media(max-width:620px){{.cta{{padding:24px 20px}}}}
  </style>
</head>
<body>
  <div class="wrap">
    <nav>
      <a class="mark" href="/" aria-label="Ulrich Monthe — home">
        <span class="mark-mono">UM</span><span class="mark-name">Ulrich Monthe</span>
      </a>
      <ul><li><a href="/live-projects/">Live Projects</a></li><li><a href="/#contact">Contact</a></li></ul>
    </nav>
    <div class="crumb"><a href="/live-projects/funder-standing/">Funder Standing</a> / {crumb}</div>
"""

FOOT = """    <footer>
      <span>© 2026 Ulrich Monthe</span>
      <span><a href="/live-projects/funder-standing/">Screen a set of funders</a> · <a href="/#contact">Get in touch</a></span>
    </footer>
  </div>
</body>
</html>
"""


def render_page(d, idx_row, total_pub):
    m = d.get("metrics")
    q = d["quality"]
    w = d["window"]
    name, slug = d["name"], d["slug"]
    canonical = f"{BASE}/foundations/{slug}/"
    publishable = q.get("publishable")

    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": f"{name} — grant history from IRS Form 990-PF",
        "description": f"New-grantee rate and grant history for {name}, computed from Form 990-PF filings.",
        "url": canonical,
        "creator": {"@type": "Person", "name": "Ulrich Monthe", "url": BASE},
        "isBasedOn": "https://www.irs.gov/charities-non-profits/form-990-series-downloads",
        "dateModified": d["provenance"]["computed_at"],
        "temporalCoverage": f"{w['years_present'][0]}/{w['years_present'][-1]}" if w.get("years_present") else "",
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
    }, separators=(",", ":"))

    desc = meta_description(d, m) if publishable and m else (
        f"{name}: IRS Form 990-PF grant history. Not enough matched filing data to compare "
        f"new-grantee activity, and this page says which condition failed rather than estimating.")
    if len(desc) > 160:
        desc = desc[:157].rsplit(" ", 1)[0] + "…"

    out = [HEAD.format(title=e(title_for(name)), desc=e(desc), canonical=canonical,
                       base=BASE, jsonld=jsonld, crumb=e(name))]

    out.append(f'    <h1>{e(name)}</h1>')
    bits = [b for b in [d.get("state"), f"EIN {d['ein']}", d.get("asset_band", "").replace("-", "–")] if b]
    out.append(f'    <div class="sub">{e(" · ".join(bits))} · data as of FY{w.get("latest_eligible_year") or max(w.get("years_present") or [0])}</div>')

    band = d.get("status_band", "Not enough data to compare")
    out.append(f'    <div class="band {BAND_CLASS.get(band, "none")}">{e(band)}</div>')

    if publishable and m:
        look = m.get("lookback_years_used") or 3
        out.append(f'''    <p class="lead">{m['new_grantee_count_latest']} of {m['total_grantee_count_latest']} organizations
      {e(name)} funded in FY{w['latest_eligible_year']} had not been funded in the prior {look} years.</p>''')
        peer = m.get("peer_median_new_grantee_rate")
        peer_txt = (f"Across all compared years the rate is {pct(m['new_grantee_rate_pooled'])}. "
                    f"Foundations of a similar size sit at {pct(peer)}.") if peer is not None else \
                   f"Across all compared years the rate is {pct(m['new_grantee_rate_pooled'])}."
        out.append(f'    <p class="peer">{e(peer_txt)}</p>')

        gs = m.get("grant_sizes") or {}
        out.append('    <section><h2>The numbers</h2><div class="grid">')
        cells = [
            ("New-grantee rate", pct(m["new_grantee_rate_pooled"]), "Pooled across compared years"),
            ("Median grant", money(gs.get("median")), f"Range {money(gs.get('min'))} – {money(gs.get('max'))}"),
            ("Repeat-dollar share", pct(m.get("repeat_dollar_concentration")), "Dollars to prior-year grantees"),
            ("Accepts unsolicited", "Yes" if d["self_reported"]["accepts_unsolicited"] else "No",
             "Inferred from the filing — see below"),
            ("Match rate", pct(q["match_rate"]), "Grant lines resolved to an organization"),
            ("Filing years used", str(len(w.get("years_present") or [])), "Consecutive returns on file"),
        ]
        for lab, val, note in cells:
            out.append(f'      <div><div class="m-l">{e(lab)}</div><div class="m-v">{e(val)}</div><div class="m-n">{e(note)}</div></div>')
        out.append('    </div></section>')

        recips = d.get("recipients_latest_year") or []
        if recips:
            shown = sorted(recips, key=lambda r: -(r.get("amount") or 0))[:25]
            out.append(f'    <section><h2>Who they funded in FY{w["latest_eligible_year"]}</h2>')
            out.append('    <div class="tablewrap"><table><thead><tr><th>Recipient</th><th style="text-align:right">Amount</th></tr></thead><tbody>')
            for r in shown:
                tag = '<span class="newtag">new</span>' if r.get("is_new") else ""
                out.append(f'      <tr><td class="name">{e(r.get("name"))}{tag}</td><td class="n">{money(r.get("amount"))}</td></tr>')
            out.append('    </tbody></table></div>')
            if len(recips) > len(shown):
                out.append(f'    <p style="margin-top:10px;font-size:14px">Showing the {len(shown)} largest of {len(recips)} grants.</p>')
            out.append('    </section>')
    else:
        reasons = {
            "match_rate": "grantee names in these filings could not be matched reliably enough",
            "eligible_year_count": "there are too few consecutive filing years to compare against",
            "total_grantee_count_pooled": "there are too few grantees to compute a stable figure",
            "recency": "the most recent usable filing is too old",
        }
        why = "; ".join(reasons.get(g, g) for g in q.get("gate_failures", []))
        out.append(f'''    <p class="lead">No comparison is shown for {e(name)}, because {e(why)}.</p>
    <p class="peer">Publishing a figure on that basis could read as open when it is not, so none is given.
      The application status below comes straight from the filing and is unaffected.</p>
    <section><h2>What the filing does say</h2><div class="grid">
      <div><div class="m-l">Accepts unsolicited</div><div class="m-v">{"Yes" if d['self_reported']['accepts_unsolicited'] else "No"}</div><div class="m-n">Inferred from the filing</div></div>
      <div><div class="m-l">Match rate</div><div class="m-v">{pct(q['match_rate'])}</div><div class="m-n">85% needed before a figure is published</div></div>
      <div><div class="m-l">Filing years on file</div><div class="m-v">{len(w.get('years_present') or [])}</div><div class="m-n">Consecutive returns</div></div>
    </div></section>''')

    out.append(f'''    <section><h2>How to read this</h2>
    <p>Every US private foundation files Form 990-PF, and Part XV of that return itemises each
      grant it paid, with the recipient's name. Lining those lists up across filing years shows
      which organizations were funded for the first time.</p>
    <p>That does work the application checkbox cannot. Whether a foundation says it accepts
      unsolicited proposals is self-reported and never audited. The grant ledger is behaviour.</p>
    <div class="notice"><b>What this page does not tell you.</b> Whether your work fits what
      {e(name)} funds — no tax return contains that. Whether anyone on your board already knows a
      trustee, which is how a great deal of foundation money actually moves. Or anything that has
      changed since the last filing, which runs twelve to twenty-four months behind.</div>
    </section>''')

    if q.get("drift_review_flag"):
        out.append('''    <div class="notice" style="margin-top:16px"><b>Flagged for review.</b>
      A high share of this funder's recipients appear in only one year. That is what genuine
      turnover looks like, and also what a renamed grantee looks like, so the figure above may be
      overstated. Match rate cannot distinguish the two.</div>''')

    out.append(f'''    <div class="prov">
      <b>Source.</b> IRS Form 990-PF, Part XV line 3a (grants paid during the year), tax years
      {e(", ".join(str(y) for y in (w.get("years_present") or [])))}<br>
      <b>Excludes.</b> Grants approved for future payment, which the return lists separately<br>
      <b>Computed.</b> {e(d["provenance"]["computed_at"])} · <b>Next recompute.</b> {e(d["provenance"]["next_recompute_expected"])}<br>
      <b>Distribution.</b> {e(d["provenance"].get("distribution", "IRS e-file corpus"))}
    </div>

    <div class="cta">
      <h3>If this is your foundation.</h3>
      <p>Every figure here comes from your own filings. If one looks wrong I would rather hear it
        than keep publishing it — <a href="mailto:umonthe1@gmail.com?subject=Correction%3A%20{e(slug)}">write to me</a>
        and I will show you the filings and the arithmetic behind it, and correct it if it is off.</p>
    </div>

    <div class="links">
      <a href="/live-projects/funder-standing/?s={e(d["ein"])}">Add to a screen</a>
      <a href="/foundations/">All {total_pub} foundations</a>
      <a href="/live-projects/funder-standing/">How this is computed</a>
    </div>
''')
    out.append(FOOT)
    return "\n".join(out)


def render_index(rows):
    """A directory, not a second browsing surface.

    Screening happens in the tool at /live-projects/funder-standing/. This page
    exists because that tool renders its list in JavaScript, which search
    engines largely cannot follow into the detail pages. So it is a plain,
    crawlable A-Z of links, deliberately thin, pointing into the tool for
    anything interactive.
    """
    canonical = BASE + "/foundations/"
    desc = ("An A-Z directory of %d US private foundations with grant histories computed "
            "from Form 990-PF filings. One page each, free and with no login." % len(rows))
    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": "Foundation grant histories - directory", "url": canonical,
        "creator": {"@type": "Person", "name": "Ulrich Monthe", "url": BASE},
    }, separators=(",", ":"))

    out = [HEAD.format(title="Foundation Grant Histories \u2014 A\u2013Z", desc=e(desc),
                       canonical=canonical, base=BASE, jsonld=jsonld, crumb="Directory")]

    out.append("    <h1>Foundation grant histories</h1>")
    out.append('    <p class="lead">One page for each of these %d foundations, showing how often '
               'it funds an organization it has not funded before \u2014 computed from its own '
               'Form 990-PF filings.</p>' % len(rows))
    out.append('    <div class="notice"><b>Comparing several at once?</b> The '
               '<a href="/live-projects/funder-standing/">screening tool</a> filters this list, '
               'shows the evidence behind each figure, and builds a set you can export or share '
               'as a link. This page is just the directory.</div>')

    groups = {}
    for r in rows:
        nm = r["name"]
        if nm.lower().startswith("the "):
            nm = nm[4:]
        letter = (nm.strip() or "?")[0].upper()
        if not letter.isalpha():
            letter = "#"
        groups.setdefault(letter, []).append(r)

    out.append("    <section>")
    for letter in sorted(groups):
        out.append('    <h2 style="margin-top:26px">%s</h2>' % letter)
        out.append('    <ul class="dir">')
        for r in sorted(groups[letter], key=lambda x: x["name"]):
            rate = pct(r["rate_pooled"]) if r["publishable"] else "no comparison"
            st = (" \u00b7 " + e(r["state"])) if r.get("state") else ""
            out.append('      <li><a href="/foundations/%s/">%s</a>'
                       '<span class="dir-meta">%s%s</span></li>'
                       % (e(r["slug"]), e(r["name"]), rate, st))
        out.append("    </ul>")
    out.append("    </section>")
    out.append('    <div class="links">'
               '<a href="/live-projects/funder-standing/">Screen a set of funders</a>'
               '<a href="/live-projects/funder-standing/#how">How this is computed</a></div>')
    out.append(FOOT)
    return "\n".join(out)


def main() -> int:
    with open(os.path.join(DATA, "index.json")) as fh:
        idx = json.load(fh)
    rows = idx["foundations"]
    total_pub = len(rows)

    os.makedirs(OUT, exist_ok=True)
    written = []
    for r in rows:
        with open(os.path.join(DATA, "foundations", f"{r['ein']}.json")) as fh:
            d = json.load(fh)
        d.setdefault("slug", r["slug"])
        path = os.path.join(OUT, r["slug"])
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(render_page(d, r, total_pub))
        written.append(r["slug"])

    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(render_index(rows))

    print(f"wrote {len(written)} foundation pages + index -> /foundations/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
