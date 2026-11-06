# Claude Code - Advanced
> *Run Claude Code as automation: guard it with permissions and hooks, script it headless, run it in GitHub Actions, build your own agents with the Agent SDK, and run parallel sessions.*

# Prerequisites
- [Claude Code - Intermediate](./Claude%20Code%20-%20Intermediate.md)
- JSON/YAML, GitHub Actions basics, an Anthropic API key (needed for headless runs, CI and the SDK)

# Objectives
- Write `.claude/settings.json` allow and deny rules and a PreToolUse or PostToolUse hook
- Run Claude headless (`claude -p … --output-format json`) from scripts
- Set up [claude-code-action](https://github.com/anthropics/claude-code-action) so Claude answers `@claude` in PRs or runs on a schedule
- Build a small agent with the Claude Agent SDK (Python)
- Run parallel sessions with git worktrees, and package a plugin

# Content
* [Hooks guide](https://code.claude.com/docs/en/hooks-guide) · [Settings & permissions](https://code.claude.com/docs/en/settings)
* [Headless / programmatic use](https://code.claude.com/docs/en/headless) · [CLI reference](https://code.claude.com/docs/en/cli-reference)
* [GitHub Actions](https://code.claude.com/docs/en/github-actions)
* [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
* [Worktrees](https://code.claude.com/docs/en/worktrees) · [Plugins](https://code.claude.com/docs/en/plugins)

### Hooks in Claude Code
[![Hooks in Claude Code](https://img.youtube.com/vi/IkaPHiMDazM/0.jpg)](https://www.youtube.com/watch?v=IkaPHiMDazM)
> *Claude · Hooks: run your own scripts before or after Claude acts*

---
### Claude Code + GitHub Actions - Full Workflow Breakdown
[![Claude Code + GitHub Actions - Full Workflow Breakdown](https://img.youtube.com/vi/x0IQKEEOawQ/0.jpg)](https://www.youtube.com/watch?v=x0IQKEEOawQ)
> *Software Engineer Meets AI · Setting up Claude in GitHub Actions*

---
### Claude Agent SDK - complete walkthrough in 12 mins!
[![Claude Agent SDK - complete walkthrough in 12 mins!](https://img.youtube.com/vi/u1uyXXl_6N8/0.jpg)](https://www.youtube.com/watch?v=u1uyXXl_6N8)
> *AI Bites · Agent SDK walkthrough*

---
### Claude Code Worktrees in 7 Minutes
[![Claude Code Worktrees in 7 Minutes](https://img.youtube.com/vi/z_VI51k-tn0/0.jpg)](https://www.youtube.com/watch?v=z_VI51k-tn0)
> *Developers Digest · Parallel sessions with worktrees*

---
### Claude Code Plugins Explained In 7 Minutes
[![Claude Code Plugins Explained In 7 Minutes](https://img.youtube.com/vi/_lBG5h3AY50/0.jpg)](https://www.youtube.com/watch?v=_lBG5h3AY50)
> *Software Engineer Meets AI · Plugins and marketplaces*

---
### How the Claude Code team uses Claude Code
[![How the Claude Code team uses Claude Code](https://img.youtube.com/vi/S-sYlFiGFv8/0.jpg)](https://www.youtube.com/watch?v=S-sYlFiGFv8)
> *Claude · Advanced workflows from the team that builds Claude Code*

---

# Follow-along
**Repos:** [anthropics/claude-code `examples/`](https://github.com/anthropics/claude-code/tree/main/examples) · [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) · this repo's [`.github/workflows/lesson-refresh.yml`](./.github/workflows/lesson-refresh.yml)

1. **Permissions and hooks:** in your `ds-training` fork, write a `.claude/settings.json` that denies `Read(./.env)` and adds a PostToolUse hook on `Edit|Write` that runs `python3 scripts/check_links.py`. Use [`examples/settings/`](https://github.com/anthropics/claude-code/tree/main/examples/settings) as a starting point. Confirm the hook is active with `/hooks`.
2. **Headless:**
   ```bash
   claude -p "List lessons whose 'Last reviewed' date is over 3 months old" --output-format json | jq -r .result
   ```
3. **GitHub Actions:** read [`lesson-refresh.yml`](./.github/workflows/lesson-refresh.yml). It runs the `refresh-lessons` skill every month and opens a PR. Add the `ANTHROPIC_API_KEY` and `EXA_API_KEY` secrets to your fork, trigger it from the **Actions** tab, and review the PR it opens.
4. **Agent SDK:** `git clone https://github.com/anthropics/claude-agent-sdk-python && pip install claude-agent-sdk`, then run `examples/quick_start.py`. Next, change `examples/hooks.py` so it blocks any Bash command that contains `rm`.
5. **Worktrees:** run `claude --worktree` twice, giving the two sessions independent tasks (e.g. refresh two different lessons). Merge both branches when they finish.
6. **Plugins:** open `/plugin` and install a plugin from the official marketplace. Then package your Intermediate `data-dictionary` skill as a local plugin with a `.claude-plugin/plugin.json`.

---
_Last reviewed: 2026-11-06_
