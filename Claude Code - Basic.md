# Claude Code - Basic
> *Claude Code is an AI coding agent that runs in your terminal and VS Code. It reads your project, plans changes, edits files and runs commands, and asks your permission along the way.*

# Prerequisites
- [Python - Basic](./Python%20-%20Basic.md)
- [Git in VS Code](./Git%20in%20VSCode.md)
- A Claude Pro/Max/Team/Enterprise plan or an Anthropic API key

# Objectives
- Install Claude Code, log in and start a session inside a project folder
- Generate a `CLAUDE.md` with `/init` and know what belongs in it
- Switch permission modes with **Shift + Tab** (default, auto-accept edits, plan) and know when to use each
- Use the **Explore → Plan → Code → Commit** loop to have Claude explain, then change, code
- Use Claude Code from inside VS Code

# Content
* [Claude Code overview](https://code.claude.com/docs/en/overview) and [Quickstart](https://code.claude.com/docs/en/quickstart)
* [CLAUDE.md & memory](https://code.claude.com/docs/en/memory)
* [Permission modes](https://code.claude.com/docs/en/permission-modes)
* [Claude Code in VS Code](https://code.claude.com/docs/en/vs-code)
* [Best practices](https://code.claude.com/docs/en/best-practices)
* Free course: [Claude Code in Action (Anthropic Academy)](https://anthropic.skilljar.com/claude-code-in-action)

### What is Claude Code?
[![What is Claude Code?](https://img.youtube.com/vi/fl1DSmwQKKY/0.jpg)](https://www.youtube.com/watch?v=fl1DSmwQKKY)
> *Claude · Official 3-minute overview of what Claude Code is*

---
### Installing Claude Code
[![Installing Claude Code](https://img.youtube.com/vi/0kILa02vKuI/0.jpg)](https://www.youtube.com/watch?v=0kILa02vKuI)
> *Claude · Official install walkthrough*

---
### Your first Claude Code prompt
[![Your first Claude Code prompt](https://img.youtube.com/vi/gbetp6D7J_Q/0.jpg)](https://www.youtube.com/watch?v=gbetp6D7J_Q)
> *Claude · Your first session and how to prompt*

---
### The CLAUDE.md file
[![The CLAUDE.md file](https://img.youtube.com/vi/O0FGCxkHM-U/0.jpg)](https://www.youtube.com/watch?v=O0FGCxkHM-U)
> *Claude · `/init` and project memory*

---
### The Explore → Plan → Code → Commit workflow in Claude Code
[![The Explore → Plan → Code → Commit workflow in Claude Code](https://img.youtube.com/vi/xJQuF02NAK8/0.jpg)](https://www.youtube.com/watch?v=xJQuF02NAK8)
> *Claude · Plan mode and the core workflow you will use every day*

---
### Claude Code for Data Scientists in 9 minutes
[![Claude Code for Data Scientists in 9 minutes](https://img.youtube.com/vi/5PBmvx0eKL4/0.jpg)](https://www.youtube.com/watch?v=5PBmvx0eKL4)
> *The Almost Astrophysicist · Data-science-flavoured tour, close to how actuaries will use it*

---

# Follow-along
**Repo:** [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks): Python notebooks, and it already has a `CLAUDE.md` to compare against yours

1. Install and launch:
   ```bash
   curl -fsSL https://claude.ai/install.sh | bash      # macOS / Linux / WSL
   git clone https://github.com/anthropics/claude-cookbooks && cd claude-cookbooks
   claude
   ```
2. Ask: *"Explain how this repo is organised and how notebooks are tested."* Then ask it to walk you through one notebook in `tool_use/`, cell by cell.
3. Rename `CLAUDE.md` to `CLAUDE.md.orig`, run `/init`, and compare the file Claude writes with the original.
4. Press **Shift + Tab** until you reach **plan mode**. Ask for a plan to add a small helper under `misc/`, e.g. one that summarises token usage. Review the plan, then approve it.
5. Open the folder in VS Code with the Claude Code extension, select a function and ask for docstrings. Review the diff before you accept it.
6. Ask Claude to create a branch, write a commit message and commit the change.

---
_Last reviewed: 2026-11-06_
