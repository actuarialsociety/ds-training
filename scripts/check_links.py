#!/usr/bin/env python3
"""Check every link in the lesson markdown files.

- YouTube videos are checked with the public oEmbed endpoint (no API key). A
  video that is private, deleted or region-blocked fails.
- Relative links must point at a file in this repo.
- Other http(s) links must answer with a status below 400.

Usage:
    python3 scripts/check_links.py               # all *.md in the repo root
    python3 scripts/check_links.py "Kedro.md"    # specific files
    python3 scripts/check_links.py --json        # machine-readable report

Exit code 1 if any link is broken. Stdlib only, so it runs anywhere.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\]\((<[^>]+>|[^)\s]+)\)")
YT_ID_RE = re.compile(
    r"(?:youtube\.com/(?:watch\?(?:.*&)?v=|shorts/|embed/|live/)|youtu\.be/)([A-Za-z0-9_-]{11})"
)
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
# Thumbnails are derived from the video ID, so the video check covers them.
SKIP_RE = re.compile(r"^(mailto:|#)|img\.youtube\.com/vi/")
# Sites that refuse automated requests; a 403 from them is not a dead link.
BOT_BLOCKERS = ("giphy.com", "linkedin.com", "medium.com", "openai.com", "kaggle.com")
UA = "Mozilla/5.0 (ds-training link checker)"


def lesson_files(args: list[str]) -> list[Path]:
    if args:
        return [ROOT / a if not Path(a).is_absolute() else Path(a) for a in args]
    return sorted(p for p in ROOT.glob("*.md"))


def extract_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    # Links inside code are examples, not links.
    text = CODE_RE.sub("", text)
    links = []
    for m in LINK_RE.finditer(text):
        link = m.group(1).strip("<>")
        if not SKIP_RE.search(link):
            links.append(link)
    return links


def fetch(url: str, method: str = "HEAD") -> tuple[int, str]:
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace") if method == "GET" else ""
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # noqa: BLE001 - network errors of any kind
        return 0, str(e)


def check(source: Path, link: str) -> dict:
    result = {"file": source.name, "link": link, "ok": False, "detail": ""}
    yt = YT_ID_RE.search(link)
    if yt:
        vid = yt.group(1)
        oembed = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(
            f"https://www.youtube.com/watch?v={vid}", safe=""
        )
        status, body = fetch(oembed, "GET")
        if status == 200:
            data = json.loads(body)
            result.update(ok=True, detail=f"{data.get('title')} | {data.get('author_name')}")
        else:
            result["detail"] = f"YouTube oEmbed {status} (private/deleted/unavailable)"
        return result
    if not link.startswith(("http://", "https://")):
        target = (source.parent / urllib.parse.unquote(link.split("#")[0])).resolve()
        result.update(ok=target.exists(), detail="" if target.exists() else "missing local file")
        return result
    status, err = fetch(link)
    if status >= 400 or status == 0:  # some sites (e.g. Kaggle) reject HEAD
        status, err = fetch(link, "GET")
    host = urllib.parse.urlparse(link).netloc
    if status == 403 and any(b in host for b in BOT_BLOCKERS):
        result.update(ok=True, detail="403 (site blocks bots; check manually)")
    elif status == 429:
        result.update(ok=True, detail="429 rate-limited (assumed alive; check manually)")
    else:
        result.update(ok=0 < status < 400, detail=f"HTTP {status} {err}".strip())
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--verbose", "-v", action="store_true", help="also list working links")
    a = ap.parse_args()

    jobs = [(f, link) for f in lesson_files(a.files) for link in extract_links(f)]
    with ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(lambda j: check(*j), jobs))

    broken = [r for r in results if not r["ok"]]
    if a.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results if a.verbose else broken:
            mark = "OK  " if r["ok"] else "FAIL"
            print(f"{mark} {r['file']}: {r['link']}  -> {r['detail']}")
        print(f"\n{len(results)} links checked, {len(broken)} broken.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
