"""Generate sitemap.xml from what is actually on disk.

The sitemap was hand-maintained, which is fine at 186 URLs and impossible at
several thousand. Worse, a hand-maintained sitemap fails silently: pages that
exist but are never listed simply do not get discovered, and nothing reports
it. Any agent expanding coverage would have shipped hundreds of unreachable
pages before anyone noticed.

So the source of truth is the filesystem. Every directory containing an
index.html is a URL; priority and change frequency come from the path. Adding
a page to the site adds it to the sitemap, with no second step to forget.

    python3 scripts/build_sitemap.py           # write sitemap.xml
    python3 scripts/build_sitemap.py --check   # exit 1 if stale, write nothing

--check is the form to run in a pull request: it answers "does the committed
sitemap match the committed pages" without touching the working tree.
"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://ulrichmonthe.com"
OUT = os.path.join(ROOT, "sitemap.xml")

SKIP_DIRS = {".git", ".github", "node_modules", "scripts", "standing",
             "styles", "research", "prototypes", "agents"}

def classify(url_path: str) -> tuple[str, str]:
    """changefreq and priority for one URL path."""
    if url_path == "/":
        return "monthly", "1.0"
    if url_path == "/live-projects/":
        return "weekly", "0.8"
    if url_path.startswith("/live-projects/"):
        return "weekly", "0.9"          # the three tools
    if url_path == "/foundations/":
        return "weekly", "0.8"          # the A–Z directory
    if url_path.startswith("/foundations/"):
        return "monthly", "0.7"
    if url_path.startswith("/notes/"):
        return "monthly", "0.8"
    return "monthly", "0.6"             # guides, verify, benchmarks


def discover() -> list[str]:
    """Every directory with an index.html, as a site-absolute URL path."""
    paths: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        parts = [] if rel == "." else rel.split(os.sep)
        if parts and parts[0] in SKIP_DIRS:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS
                       and not d.startswith(".")]
        if "index.html" in filenames:
            paths.append("/" if not parts else "/" + "/".join(parts) + "/")
    return sorted(set(paths))


def render(paths: list[str]) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in paths:
        cf, pr = classify(p)
        lines.append(f"  <url><loc>{BASE}{p}</loc>"
                     f"<changefreq>{cf}</changefreq>"
                     f"<priority>{pr}</priority></url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main() -> int:
    paths = discover()
    xml = render(paths)

    if "--check" in sys.argv:
        current = ""
        if os.path.exists(OUT):
            with open(OUT, encoding="utf-8") as fh:
                current = fh.read()
        have = set(re.findall(r"<loc>(.*?)</loc>", current))
        want = {f"{BASE}{p}" for p in paths}
        missing, extra = sorted(want - have), sorted(have - want)
        print(f"pages on disk {len(want)}, urls in sitemap {len(have)}")
        if missing:
            print(f"\nMISSING from sitemap ({len(missing)}) — these will not be crawled:")
            for u in missing[:20]:
                print(f"  {u}")
            if len(missing) > 20:
                print(f"  … and {len(missing) - 20} more")
        if extra:
            print(f"\nLISTED but not on disk ({len(extra)}) — these will 404:")
            for u in extra[:20]:
                print(f"  {u}")
        if missing or extra:
            print("\nFAIL  sitemap is stale — run: python3 scripts/build_sitemap.py")
            return 1
        print("sitemap OK — every page listed, every listing real.")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(xml)
    print(f"wrote sitemap.xml — {len(paths)} urls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
