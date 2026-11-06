# Claude Code - Intermediate
> *Turn Claude Code from a chat into a tool you configure: manage its context, teach it repeatable tasks with skills, connect it to other systems with MCP, and hand focused jobs to subagents.*

# Prerequisites
- [Claude Code - Basic](./Claude%20Code%20-%20Basic.md)
- Comfortable with git branches and pull requests; [GitHub CLI](https://cli.github.com/) installed and logged in (`gh auth login`)

# Objectives
- Manage context with `/context`, `/compact` and `/clear`
- Write a reusable skill (`.claude/skills/<name>/SKILL.md`) and invoke it as `/<name>`
- Connect an MCP server and use its tools in a session
- Create a custom subagent and delegate a focused task to it
- Have Claude drive a branch → commit → pull request workflow

# Content
* [Built-in commands](https://code.claude.com/docs/en/commands)
* [Skills](https://code.claude.com/docs/en/skills) (custom slash commands are now skills)
* [MCP](https://code.claude.com/docs/en/mcp)
* [Subagents](https://code.claude.com/docs/en/sub-agents)
* [Common workflows (git & PRs)](https://code.claude.com/docs/en/common-workflows)
* [Example skills: anthropics/skills](https://github.com/anthropics/skills)

### Context Management in Claude Code
[![Context Management in Claude Code](https://img.youtube.com/vi/eW3oTyfeWZ0/0.jpg)](https://www.youtube.com/watch?v=eW3oTyfeWZ0)
> *Claude · Why context fills up and what `/compact` and `/clear` do*

---
### What are skills?
[![What are skills?](https://img.youtube.com/vi/bjdBVZa66oU/0.jpg)](https://www.youtube.com/watch?v=bjdBVZa66oU)
> *Claude · What skills are and when to write one*

---
### Claude Code Tutorial #6 - Slash Commands
[![Claude Code Tutorial #6 - Slash Commands](https://img.youtube.com/vi/52KBhQqqHuc/0.jpg)](https://www.youtube.com/watch?v=52KBhQqqHuc)
> *Net Ninja · Built-in and custom slash commands, hands-on*

---
### MCP in Claude Code
[![MCP in Claude Code](https://img.youtube.com/vi/kkBFmwkDzdo/0.jpg)](https://www.youtube.com/watch?v=kkBFmwkDzdo)
> *Claude · Adding an MCP server*

---
### Claude Code Tutorial #8 - Subagents
[![Claude Code Tutorial #8 - Subagents](https://img.youtube.com/vi/Phr7vBx9yFQ/0.jpg)](https://www.youtube.com/watch?v=Phr7vBx9yFQ)
> *Net Ninja · Building and using a subagent*

---
### Beyond the basics with Claude Code
[![Beyond the basics with Claude Code](https://img.youtube.com/vi/tuY2ChJIx48/0.jpg)](https://www.youtube.com/watch?v=tuY2ChJIx48)
> *Claude · Optional 47-minute deep dive; watch later*

---

# Follow-along
**Repo:** this repo, [ds-training](./README.md). It uses the same features you are learning: see [`AGENTS.md`](./AGENTS.md) and [`.claude/skills/`](./.claude/skills/)

1. Fork and clone `ds-training`, then run `claude` in it. Ask: *"How do the build-lesson and refresh-lessons skills work?"*
2. Get an [Exa API key](https://dashboard.exa.ai/api-keys) and run `export EXA_API_KEY=...`. Then run `/build-lesson "Polars" Basic` and watch Claude search for material, verify every link with `scripts/yt_block.py` and `scripts/check_links.py`, and write the lesson.
3. Write your own skill. Copy [anthropics/skills `template/SKILL.md`](https://github.com/anthropics/skills/tree/main/template) to `.claude/skills/data-dictionary/SKILL.md` and have it produce a column-by-column data dictionary for any CSV. Test it with `/data-dictionary`.
4. Add the Exa MCP server with `claude mcp add --transport http exa https://mcp.exa.ai/mcp`, check it is connected with `/mcp`, then ask a question that needs a web search.
5. Use `/agents` to create a `link-fixer` subagent whose job is to run `scripts/check_links.py` and propose replacements. Ask Claude to delegate to it.
6. Run `/context`, then `/compact` with a focus instruction, and see how much context it frees. Finally, ask Claude to commit and open a PR on your fork with `gh pr create`, and review the description it writes.

---
_Last reviewed: 2026-11-06_
