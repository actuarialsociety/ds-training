#!/usr/bin/env python3
"""Turn YouTube IDs or URLs into lesson-ready Markdown blocks.

Each video is checked with YouTube's oEmbed endpoint and the exact title is
used, so a lesson never shows a made-up title or a dead video.

    python3 scripts/yt_block.py dQw4w9WgXcQ https://youtu.be/<id> ...

Prints one block per video. Exits 1 if any video cannot be found.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request

ID_RE = re.compile(r"(?:v=|youtu\.be/|shorts/|embed/|live/)?([A-Za-z0-9_-]{11})(?:[&?#].*)?$")


def video_id(arg: str) -> str | None:
    m = ID_RE.search(arg.strip())
    return m.group(1) if m else None


def oembed(vid: str) -> dict | None:
    url = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(
        f"https://www.youtube.com/watch?v={vid}", safe=""
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (ds-training)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except Exception:  # noqa: BLE001
        return None


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    failed = False
    for arg in argv:
        vid = video_id(arg)
        data = oembed(vid) if vid else None
        if not data:
            print(f"<!-- FAILED: {arg} is not an available YouTube video -->", file=sys.stderr)
            failed = True
            continue
        title = data["title"].replace("[", "(").replace("]", ")")
        print(f"### {title}")
        print(f"[![{title}](https://img.youtube.com/vi/{vid}/0.jpg)](https://www.youtube.com/watch?v={vid})")
        print(f"> *{data['author_name']} · TODO: why this video*")
        print("\n---")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
