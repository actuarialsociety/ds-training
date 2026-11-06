# Tabular ML - Foundation Models
> *Tabular foundation models are pre-trained on millions of synthetic datasets. You give them your training rows "in context", and they predict new rows in one forward pass, with no task-specific training. Use them for zero-shot predictions and fast prototyping without a training pipeline. On small-to-medium datasets they often match or beat a tuned GBDT with zero tuning.*

> ⚠️ **Licences matter for actuarial work.** The weights for TabPFN 2.5+, Google TabFM and LimiX are **non-commercial**. Check the licence before you use any of them for production pricing or reserving. Do not send policyholder data to a cloud API without approval.

# Prerequisites
- [Tabular ML - Gradient Boosting](./Tabular%20ML%20-%20Gradient%20Boosting.md): your baseline to beat
- [Google Colab](./Google%20Colab.md) / [GPUs & Acceleration](./GPUs%20%26%20Acceleration.md): local TabPFN wants a GPU
- A free [Hugging Face](https://huggingface.co/join) account. Hugging Face is the **model repository** where these models' weights are published, much as code lives on GitHub. Some weights are gated, so you accept their licence there before downloading

# Objectives
- Explain in-context learning for tables: a prior built from structural causal models, one forward pass at prediction time, and transformer layers that alternate attention across rows and columns. Explain why this lets one model handle any schema, including when columns change
- Use **TabPFN** (TabPFN-3, now 3.5) locally (`tabpfn`, on a GPU) and through the cloud API (`tabpfn-client`), and benchmark it against your tuned XGBoost
- Compare the current models (TabPFN-3.5, Google **TabFM**, **LimiX-2**) with **TableGPT2**, a text-to-table LLM that pairs a table encoder with an LLM and writes executable Python or SQL for BI and conversational analysis. It is not a predictive model
- Assess fitness for actuarial use: row and feature limits, licences, data privacy and interpretability

# Content
* **TabPFN** (Prior Labs): [docs](https://docs.priorlabs.ai/) · [models & licences](https://docs.priorlabs.ai/models) · [weights on Hugging Face](https://huggingface.co/Prior-Labs/tabpfn_3_5) · [Nature paper (v2)](https://www.nature.com/articles/s41586-024-08328-6) · [TabPFN-3.5 report](https://arxiv.org/abs/2609.17895)
* **TabFM** (Google Research): [announcement](https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/) · [repo](https://github.com/google-research/tabfm)
* **LimiX**: [LimiX-2 paper](https://arxiv.org/abs/2609.17488) · [weights on Hugging Face](https://huggingface.co/stable-ai/LimiX-2) · [repo](https://github.com/limix-ldm/LimiX). Install from the repo; the PyPI package `limix` is an unrelated genetics library
* **TableGPT2**: [tablegpt-agent repo](https://github.com/tablegpt/tablegpt-agent) · [paper](https://arxiv.org/abs/2411.02059) · [weights on Hugging Face](https://huggingface.co/tablegpt/TableGPT2-7B) · [agent docs](https://tablegpt.github.io/tablegpt-agent/)

### Tabular Foundation Models (TabPFN)
[![Tabular Foundation Models (TabPFN)](https://img.youtube.com/vi/ZRwnY3eG7bE/0.jpg)](https://www.youtube.com/watch?v=ZRwnY3eG7bE)
> *Rajistics - data science, AI, and machine learning · 90-second intuition for tabular foundation models*

---
### TabPFN: Deep Learning for Tabular Data is Here! (Prof. Frank Hutter explains)
[![TabPFN: Deep Learning for Tabular Data is Here! (Prof. Frank Hutter explains)](https://img.youtube.com/vi/MKu09syGgEk/0.jpg)](https://www.youtube.com/watch?v=MKu09syGgEk)
> *Super Data Science: ML & AI Podcast with Jon Krohn · TabPFN's co-creator explains the prior and in-context learning*

---
### Introducing TabPFN-3.5!
[![Introducing TabPFN-3.5!](https://img.youtube.com/vi/HncTGFqSas8/0.jpg)](https://www.youtube.com/watch?v=HncTGFqSas8)
> *Prior Labs · Official announcement of the current version*

---
### TabPFN vs XGBoost: can a foundation model beat a tuned XGBoost with zero tuning?
[![TabPFN vs XGBoost: can a foundation model beat a tuned XGBoost with zero tuning?](https://img.youtube.com/vi/A7_rBOljbzk/0.jpg)](https://www.youtube.com/watch?v=A7_rBOljbzk)
> *Prior Labs · Head-to-head with XGBoost; picks up where the previous lesson ends*

---
### TabFM Explained: Google's New Foundation Model for Tabular Data
[![TabFM Explained: Google's New Foundation Model for Tabular Data](https://img.youtube.com/vi/8vW6gi5vRes/0.jpg)](https://www.youtube.com/watch?v=8vW6gi5vRes)
> *Dr. Data Science · Third-party explainer of Google TabFM (no official video exists)*

---
### TableGPT2 7B - AI Model for Structured Data - Install Locally
[![TableGPT2 7B - AI Model for Structured Data - Install Locally](https://img.youtube.com/vi/Y4dnCCD0p8A/0.jpg)](https://www.youtube.com/watch?v=Y4dnCCD0p8A)
> *Fahd Mirza · Running TableGPT2 locally (third-party; no official video exists)*

---

# Follow-along
**Repos:** [PriorLabs/TabPFN `examples/`](https://github.com/PriorLabs/TabPFN/tree/main/examples) · [PriorLabs/tabpfn-client](https://github.com/PriorLabs/tabpfn-client) (no GPU needed) · [google-research/tabfm](https://github.com/google-research/tabfm)

1. Install TabPFN: `pip install tabpfn` on a GPU (Colab T4 is fine), or `pip install tabpfn-client` on a CPU laptop. Log in when prompted and accept the licence.
2. Run `TabPFN/examples/tabpfn_for_binary_classification.py`, then `tabpfn_for_regression.py`.
3. Take your dataset from [Gradient Boosting](./Tabular%20ML%20-%20Gradient%20Boosting.md) step 4 (subsample to 10k rows or fewer on CPU or the client). Compare `TabPFNClassifier`/`TabPFNRegressor` with **zero tuning** against your tuned XGBoost on the metric and on wall-clock time.
4. Install TabFM (`pip install tabfm`), run its README quick start, then run it on the same split.
5. *(Stretch)* Try LimiX-2 for missing-value imputation on the same data. Then test schema shift: drop or add a column at prediction time and compare how TabPFN and XGBoost cope.
6. *(Text-to-table)* Following the [tablegpt-agent quick start](https://tablegpt.github.io/tablegpt-agent/), ask TableGPT2 in plain English, e.g. *"average claim size by region, as a bar chart"*, about your dataset. Read the Python it writes and check the answer with pandas.
7. Write a half page for a pricing committee: for each model, accuracy versus XGBoost, its licence, data-privacy questions and how you would explain its predictions.

---
_Last reviewed: 2026-11-06_
