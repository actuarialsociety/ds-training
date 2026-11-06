<img src="https://www.actuarialsociety.org.za/wp-content/uploads/2024/01/ASSA-LOGO-20224-e1704698493878.png" width="500" >

# `ds-training` 
> *A collection of open-source training material for actuaries (or anyone) to up-skill in data science*
> * *[VS Code](https://code.visualstudio.com/) is used to enhance developer experience; the correct extensions can make a world of difference!*
> * *AI code assistants and agents, such as [Claude Code](https://code.claude.com/docs/en/overview), [GitHub Copilot](https://github.com/features/copilot) or [Continue](https://www.continue.dev/), are essential tools for learning*
> * *Every lesson is **video-driven** with a **repo to code along in**. Lessons are kept current by Claude Code (see [Maintaining these lessons](#maintaining-these-lessons))*

![](https://media.giphy.com/media/zIOdLMZDcBDc2gk6vV/giphy.gif?cid=790b76115z20caqim0bzt56valpecg67mpo2wh0kazib6z0u&ep=v1_gifs_search&rid=giphy.gif&ct=g)

## Core Skills
- [Python - Basic](./Python%20-%20Basic.md): VS Code setup & Python basics
- [GitHub Copilot](./GitHub%20Copilot.md): Leading commercial AI code assistant
- [Continue](./Continue.md) (Optional): Leading open-source AI code assistant
- [Terminal in Windows](./Terminal%20in%20Windows.md): Command-line interface with Windows
- [Terminal in Mac](./Terminal%20in%20Mac.md): Command-line interface with MacOS
- [Windows Subsystem for Linux](./Windows%20Subsystem%20Linux.md) (Optional): Linux on Windows; Linux is developer standard ￫ what servers run!

## Claude Code
- [Claude Code - Basic](./Claude%20Code%20-%20Basic.md): Install, CLAUDE.md, permission modes, plan → code → commit
- [Claude Code - Intermediate](./Claude%20Code%20-%20Intermediate.md): Context management, skills, MCP, subagents, PR workflows
- [Claude Code - Advanced](./Claude%20Code%20-%20Advanced.md): Hooks, headless mode, GitHub Actions, Agent SDK, worktrees, plugins

## Python for Data Science
- [PyData Stack](./PyData%20Stack.md): Essential Python libraries for data analysis (NumPy, Pandas, Matplotlib, etc.)
- [Python - Advanced](./Python%20-%20Intermediate.md): Advanced Python concepts for data science

## Cloud Notebooks & GPUs
- [Google Colab](./Google%20Colab.md): Notebooks in the browser, free T4 GPU, Drive, Gemini; your first GPU
- [GPUs & Acceleration](./GPUs%20%26%20Acceleration.md): Why GPUs help; zero-code-change speed-ups for pandas, scikit-learn and XGBoost

## Hugging Face
- [Hugging Face - Basic](./Hugging%20Face%20-%20Basic.md): The Hub, model cards & licences, pipelines and datasets on insurance text
- [Hugging Face - Intermediate](./Hugging%20Face%20-%20Intermediate.md): Tokenizers, fine-tuning a claims-message classifier, pushing to the Hub, semantic search
- [Hugging Face - Advanced](./Hugging%20Face%20-%20Advanced.md): LoRA, 4-bit quantisation, Inference Providers, Spaces, agents on claims data

## Machine Learning on Tabular Data
- [Tabular ML - Gradient Boosting](./Tabular%20ML%20-%20Gradient%20Boosting.md): XGBoost, CatBoost & LightGBM, the gold standard for structured data
- [Tabular ML - Foundation Models](./Tabular%20ML%20-%20Foundation%20Models.md): TabPFN, TabFM, LimiX & TableGPT2: zero-shot prediction and text-to-table LLMs

## Data Pipelines with Kedro
- [Kedro - Basic](./Kedro%20-%20Basic.md): Nodes, pipelines, Data Catalog, Kedro-Viz; a claims-frequency pipeline
- [Kedro - Intermediate](./Kedro%20-%20Intermediate.md): Parameters, environments, namespaces (champion vs challenger), factories, versioning, testing
- [Kedro - Advanced](./Kedro%20-%20Advanced.md): Hooks, data validation, MLflow-tracked GLM, runners, Docker, Airflow, GenAI nodes

## Source Control
- [Git in VS Code](./Git%20in%20VSCode.md): Using Git version control within VS Code
- [Source control tips playlist](./Source%20control%20tips%20playlist.md) (Optional): Collection of best practices for source control

## Databases
- [SQL Basics](./SQL%20Basics.md): Fundamentals of Structured Query Language
- [SQLAlchemy & Copilot](./SQLAlchemy%20%26%20Copilot.md): Using SQLAlchemy ORM with GitHub Copilot assistance

## VS Code Skills
- [Debugging in VS Code](./Debugging%20in%20VS%20Code.md): Techniques for debugging code in VS Code
- [Regex in VS Code](./Regex%20in%20VS%20Code.md): Using regular expressions in VS Code
- [LiveShare in VS Code](./LiveShare%20in%20VS%20Code.md): Collaborative coding in real-time with VS Code
- [Remote Development in VS Code](./Remote%20Development%20in%20VS%20Code.md): Developing on remote machines or containers
- [Devcontainers in VS Code](./Devcontainers%20in%20VS%20Code.md): Using development containers for consistent environments

## Documentation
- [Markdown](./Markdown.md): Lightweight markup language for creating formatted text

## Maintaining these lessons
Browse the lessons as a [wiki](https://github.com/actuarialsociety/ds-training/wiki). It is regenerated from this repo on every merge to `main`.

This repo is set up for [Claude Code](./Claude%20Code%20-%20Basic.md) to find and maintain lessons, using [Exa](https://exa.ai/docs/get-started/agent-skills/overview) agent skills for search. Rules are in [AGENTS.md](./AGENTS.md).
1. `cp .env.example .env` and add an [Exa API key](https://dashboard.exa.ai/api-keys), or `export EXA_API_KEY=...`
2. In Claude Code:
   - `/build-lesson <topic> [level]`: find videos and a follow-along repo, verify every link, write the lesson and add it here
   - `/refresh-lessons [file|all]`: fix dead links and swap in newer or better material
3. `python3 scripts/check_links.py` checks every link. It runs in CI on each PR and weekly, and [`lesson-refresh.yml`](./.github/workflows/lesson-refresh.yml) opens a refresh PR monthly
