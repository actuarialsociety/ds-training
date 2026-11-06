#!/usr/bin/env bash
# Re-vendor Exa's agent skills (MIT, https://github.com/exa-labs/agent-skills)
# into .claude/skills/. Equivalent to `npx skills add exa-labs/agent-skills --skill <name>`
# but pinned in git so every learner and CI run gets the same skill text.
# Review the diff before committing: skills are instructions your agent follows.
set -euo pipefail
cd "$(dirname "$0")/.."
base="https://raw.githubusercontent.com/exa-labs/agent-skills/main"
for skill in exa-search exa-contents; do
  mkdir -p ".claude/skills/$skill"
  curl -fsSL "$base/skills/$skill/SKILL.md" -o ".claude/skills/$skill/SKILL.md"
  curl -fsSL "$base/LICENSE" -o ".claude/skills/$skill/LICENSE"
done
git --no-pager diff --stat -- .claude/skills/exa-search .claude/skills/exa-contents
