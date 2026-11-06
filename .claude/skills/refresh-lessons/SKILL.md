---
name: refresh-lessons
description: Audit and update existing ds-training lessons. Fixes dead links, finds newer or better videos and repos with Exa, and keeps each lesson short. Use when asked to refresh, update, audit or check the lessons, or when the scheduled lesson-refresh workflow runs.
argument-hint: "[lesson file | all]"
---

# Refresh lessons

Read `AGENTS.md` first. The goal is to keep lessons **current and succinct**.
That means replacing material more often than adding it.

## 1. Find what's broken

```bash
python3 scripts/check_links.py            # or pass specific files; --json for a report
```

Fix every broken link. Search Exa for a replacement first, e.g. the same video
re-uploaded or the docs page at its new URL. If no replacement exists, delete
the link.

## 2. Pick lessons to refresh

- With an argument, refresh only that file. With `all`, or no argument,
  refresh the lessons whose `_Last reviewed:` date is oldest, or missing, up to
  **3 lessons per run**. Keeping each run small keeps the PR reviewable.
- Fast-moving topics (Claude Code, Copilot, Hugging Face, tabular foundation
  models) go stale in about 3 months. Stable ones (SQL, Regex, Terminal) last
  about 18 months.

## 3. Look for better material (per lesson)

Use the `exa-search` skill and restrict results to content published after the
lesson's `Last reviewed` date:

```bash
curl -sS -X POST "https://api.exa.ai/search" \
  -H "Content-Type: application/json" -H "x-api-key: $EXA_API_KEY" \
  -d '{"query": "<lesson objective> tutorial", "type": "auto", "numResults": 10,
       "includeDomains": ["youtube.com"], "startPublishedDate": "<last reviewed>",
       "contents": {"highlights": true}}' \
  | jq -r '.results[] | "\(.publishedDate[:10])  \(.title)  \(.url)"'
```

Also check for each lesson:
- Is there a new major version of the tool (e.g. a new TabPFN release, a
  renamed Kedro starter, a new Claude Code feature)? Use `exa-contents` on the
  official changelog or docs.
- Does the follow-along repo still exist, and do its steps still match it?
  Check with `gh repo view` and by reading the files.
- Main videos must be code-alongs, with the presenter writing and running
  code. Replace any concept-only video in the main list with a code-along and
  move the old one to the *Background (optional)* line.
- Swap a video only when the new one is clearly better: more current, official,
  shorter or more hands-on. Move what it replaces under `## Older content`.
  Keep 3 to 6 videos in the main section.

Generate every new video block with `python3 scripts/yt_block.py <ids...>`.

## 4. Update and verify

- Set `_Last reviewed: <today>_` on every lesson you reviewed, even when
  nothing changed.
- `python3 scripts/check_links.py` must report `0 broken`.
- Summarise per lesson what changed and why, which candidates you rejected, and
  what to look at next time. When running in CI, put this summary in the PR body.
