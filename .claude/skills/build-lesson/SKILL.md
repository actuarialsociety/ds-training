---
name: build-lesson
description: Build a new video-driven lesson for this ds-training repo. Searches for the best recent videos and a follow-along repo with Exa, checks every link, writes `Topic - Level.md` from the template and adds it to README.md. Use when asked to add, create or draft a lesson or course module.
argument-hint: <topic> [Basic|Intermediate|Advanced]
---

# Build a lesson

Goal: a **short** lesson. A learner watches 3 to 6 videos and codes along in a
real repo. Read `AGENTS.md` first; its rules apply here.

## 1. Scope it (2 minutes, no tools)

- Pick the file name (`<Topic> - <Level>.md`, or `<Topic>.md` for a single
  lesson), the README section it belongs to, and its prerequisites, which are
  existing lessons in `README.md`.
- Write 3 to 5 objectives. Each one is something the learner can **do**. Every
  video and follow-along step must serve an objective.
- If the topic overlaps an existing lesson, extend that lesson instead and say so.

## 2. Find videos with Exa

Use the `exa-search` skill (needs `$EXA_API_KEY`). Run 2 or 3 queries, each
written as a description of the ideal video, restricted to YouTube and recent
uploads:

```bash
curl -sS -X POST "https://api.exa.ai/search" \
  -H "Content-Type: application/json" -H "x-api-key: $EXA_API_KEY" \
  -d '{
    "query": "short beginner tutorial video: <objective>, hands-on demo",
    "type": "auto",
    "numResults": 10,
    "includeDomains": ["youtube.com"],
    "startPublishedDate": "<today minus 18 months>",
    "contents": {"highlights": true}
  }' | jq -r '.results[] | "\(.publishedDate[:10])  \(.title)  \(.url)"'
```

- Add the vendor name to the query (e.g. "Anthropic official", "Hugging Face
  channel") to bias towards official channels; confirm via oEmbed `author_name`.
- If `EXA_API_KEY` is unset, use the WebSearch tool and say so in your summary.
- Phrase queries as *"code along / live coding / notebook walkthrough"*. The
  presenter must write and run code on screen. Theory explainers go in the
  *Background (optional)* line, never in the main video list.
- Shortlist candidates. Favour official channels, recent uploads, a linked
  notebook or repo, and insurance or finance examples. Drop clickbait, reaction
  videos and anything that only sells a course.
- Exa's page text for YouTube is just the site's footer. To read a candidate's
  description (repo links, length, channel), fetch the watch page and parse
  `ytInitialPlayerResponse.videoDetails`.

Then verify the shortlist and generate the blocks in one step:

```bash
python3 scripts/yt_block.py <id-or-url> <id-or-url> ...
```

Replace each `TODO: why this video` with a short reason. Never type a title
or ID by hand.

## 3. Find the follow-along repo

```bash
curl -sS -X POST "https://api.exa.ai/search" \
  -H "Content-Type: application/json" -H "x-api-key: $EXA_API_KEY" \
  -d '{"query": "official hands-on tutorial notebooks for <topic>", "type": "auto",
       "numResults": 8, "includeDomains": ["github.com"]}' | jq -r '.results[].url'
gh repo view <owner/name> --json description,pushedAt,isArchived,stargazerCount
```

Prefer, in this order: the vendor's official examples or course repo, a
notebook that opens in Colab
(`https://colab.research.google.com/github/<owner>/<repo>/blob/<branch>/<path>.ipynb`),
then a well-starred tutorial repo. Use the `exa-contents` skill, or
`gh api repos/<o>/<r>/contents/<path>`, to read the README or notebook. Then
write 3 to 6 follow-along steps that match the real files, including the exact
commands.

## 4. Write the lesson

- Copy `.claude/skills/build-lesson/template.md` to the new file and fill it in.
  Delete every placeholder.
- Order the videos from concept to hands-on to advanced. Put a `---` between
  video blocks, as the existing lessons do.
- Finish with `_Last reviewed: <today>_`.
- Add the lesson to `README.md` under the right section. Create a section only
  if no existing one fits.

## 5. Verify, then report

```bash
python3 scripts/check_links.py "<New Lesson>.md" README.md
```

It must report `0 broken`. Report the file, the videos (title and channel),
the repo, and anything you could not find. Do not commit unless asked.
