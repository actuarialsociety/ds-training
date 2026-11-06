# Agent Guidelines

`ds-training` is a set of short, **video-driven** lessons that help actuaries
(or anyone) learn data science. Each lesson is one Markdown file in the repo
root, listed in [README.md](./README.md). Coding agents (Claude Code, Copilot,
Cursor) maintain the lessons: they find good new material, check that links
still work and keep each lesson short.

## Project rules (read first)

### 1. A lesson = videos + a repo to code along in

- Videos carry the teaching. Prose stays short: a one-paragraph intro at most,
  plus Prerequisites, Objectives and Follow-along steps.
- Every new lesson has a **Follow-along** section that points at a real GitHub
  repo or notebook (Colab link where possible). It gives 3 to 6 concrete steps
  the learner types and runs.
- 3 to 6 videos per lesson. Choose official channels first (Anthropic, Hugging
  Face, Google, NVIDIA, Microsoft/VS Code, the library's own maintainers),
  then trusted educators (StatQuest and similar). Pick recent, short videos over
  long or old ones.
- Follow [`.claude/skills/build-lesson/template.md`](.claude/skills/build-lesson/template.md)
  for the layout and the video block format. The existing lessons use the same
  format, so keep new and edited lessons consistent with them.

### 2. Never invent a link

- Find material with Exa (the `exa-search` and `exa-contents` skills, which
  need `EXA_API_KEY`), or with web search if Exa is not available.
- Check **every** YouTube ID with oEmbed before you write it into a lesson, and
  use the exact title that oEmbed returns:
  `curl -s "https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v=<ID>"`
- Check every GitHub repo with `gh repo view <owner/name> --json isArchived,pushedAt`.
  Do not use an archived repo, or one with no pushes in the last 2 years,
  unless it is the canonical source.
- Run `python3 scripts/check_links.py <files>` before you finish. It must
  report **0 broken**.

### 3. Repo conventions

- File names are `Topic - Level.md` with spaces, e.g. `Claude Code - Basic.md`.
  In README links, encode spaces as `%20` and `&` as `%26`.
- Every new lesson gets a line in the matching README section:
  `- [Name](./File%20Name.md): one-line description`. Mark optional lessons
  `(Optional)`.
- Each new or refreshed lesson ends with `_Last reviewed: YYYY-MM-DD_`. The
  refresh skill uses that date to look for newer material.
- Do not delete a learner-facing lesson without asking. Move superseded videos
  to an `## Older content` section at the end of the lesson, as
  `Devcontainers in VS Code.md` does.

### 4. Workflows

| Task | How |
| --- | --- |
| Add a lesson | `/build-lesson <topic> [level]` ([skill](.claude/skills/build-lesson/SKILL.md)) |
| Refresh lessons | `/refresh-lessons [file]` ([skill](.claude/skills/refresh-lessons/SKILL.md)) |
| Check links | `python3 scripts/check_links.py` (CI runs it weekly and on every PR) |
| Update Exa skills | `scripts/update_exa_skills.sh` |

### 5. Secrets

- `EXA_API_KEY` lives in your shell or in `.env`, which git ignores. See
  `.env.example`. Never write a key into a lesson, skill or commit.
- CI needs the `ANTHROPIC_API_KEY` and `EXA_API_KEY` repo secrets only for the
  scheduled refresh workflow.
