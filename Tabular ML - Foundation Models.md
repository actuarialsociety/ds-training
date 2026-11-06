# Tabular ML - Foundation Models
> *Tabular foundation models are pre-trained on millions of synthetic datasets. You give them your training rows "in context", and they predict new rows in one forward pass, with no task-specific training. Use them for zero-shot predictions and fast prototyping without a training pipeline. On small-to-medium datasets they often match or beat a tuned GBDT with zero tuning. Each video below shows the code being written and run. Code along in the linked notebook.*

> ⚠️ **Licences matter for actuarial work.** The weights for TabPFN 2.5+, Google TabFM and LimiX-2 are **non-commercial** (the code is Apache 2.0, but the weights are licensed separately). Check the licence before you use any of them for production pricing or reserving. Do not send policyholder data to a cloud API without approval.

# Prerequisites
- [Tabular ML - Gradient Boosting](./Tabular%20ML%20-%20Gradient%20Boosting.md): your baseline to beat
- [Google Colab](./Google%20Colab.md) / [GPUs & Acceleration](./GPUs%20%26%20Acceleration.md): local TabPFN and TabFM want a GPU
- A free [Hugging Face](https://huggingface.co/join) account. Hugging Face is the **model repository** where these models' weights are published, much as code lives on GitHub. Some weights are gated, so you accept their licence there before downloading

# Objectives
- Explain in-context learning for tables, and why one pre-trained model can handle any schema
- Run **TabPFN** (TabPFN-3, now 3.5) locally on a GPU (`tabpfn`) and through the cloud API (`tabpfn-client`), and benchmark it against your tuned XGBoost
- Run Google **TabFM** zero-shot and know its default limits
- Know where **LimiX-2** fits (classification, regression *and* imputation in one model)
- Use **TableGPT2**, a text-to-table LLM that writes and runs Python for BI-style questions. It is not a predictive model
- Assess fitness for actuarial use: row and feature limits, licences, data privacy and interpretability

# Key concepts
- **Prior-fitted networks (PFNs)**: instead of training on *your* data, the model is pre-trained on millions of synthetic tables generated from structural causal models. At prediction time your training rows are the "prompt", so `fit()` only stores them, and `predict()` is a single forward pass.
- **Row and column attention**: the transformer attends across rows (which other policies look like this one?) and across columns (which features interact?). Columns are not tied to fixed positions, so the same weights work for any set of columns, and the model copes when columns are added or dropped between datasets (schema shift).
- **Size limits**: TabPFN-3/3.5 handles up to 5,000 rows on CPU, and far more on a GPU or via the client. TabFM's defaults are 500 features and **100 context rows**, which you raise with `max_num_rows`. Large books still favour GBDTs. Foundation models shine on small, new or sparse portfolios.
- **Text-to-table LLMs (TableGPT2)**: a table encoder plus an LLM that answers natural-language questions by *generating and executing Python*. It is for analysis and BI, not for producing a risk score.
- **Governance**: zero training doesn't mean zero validation. Back-test, check calibration, and use SHAP or partial dependence (TabPFN has [extensions](https://github.com/PriorLabs/tabpfn-extensions)) before relying on the predictions.

# Content
* **TabPFN** (Prior Labs): [docs](https://docs.priorlabs.ai/) · [models & licences](https://docs.priorlabs.ai/models) · [weights on Hugging Face](https://huggingface.co/Prior-Labs/tabpfn_3_5) · [Nature paper (v2)](https://www.nature.com/articles/s41586-024-08328-6) · [TabPFN-3.5 report](https://arxiv.org/abs/2609.17895)
* **TabFM** (Google Research): [announcement](https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/) · [repo](https://github.com/google-research/tabfm)
* **LimiX**: [LimiX-2 paper](https://arxiv.org/abs/2609.17488) · [weights on Hugging Face](https://huggingface.co/stable-ai/LimiX-2) · [repo](https://github.com/limix-ldm-ai/LimiX). Install from the repo; the PyPI package `limix` is an unrelated genetics library. No code-along video exists yet
* **TableGPT2**: [tablegpt-agent repo](https://github.com/tablegpt/tablegpt-agent) · [paper](https://arxiv.org/abs/2411.02059) · [weights on Hugging Face](https://huggingface.co/tablegpt/TableGPT2-7B) · [agent docs](https://tablegpt.github.io/tablegpt-agent/)
* **Background (optional, not code):** [Frank Hutter explains TabPFN](https://www.youtube.com/watch?v=MKu09syGgEk) · [Introducing TabPFN-3.5](https://www.youtube.com/watch?v=HncTGFqSas8)

### Tabular Foundation Models (TabPFN)
[![Tabular Foundation Models (TabPFN)](https://img.youtube.com/vi/ZRwnY3eG7bE/0.jpg)](https://www.youtube.com/watch?v=ZRwnY3eG7bE)
> *Rajistics - data science, AI, and machine learning · 90-second warm-up on the idea before you code*

---
### 🟣 How We Make Tabular Predictions in 2026 with TabPFN
[![🟣 How We Make Tabular Predictions in 2026 with TabPFN](https://img.youtube.com/vi/qEQkOA3ogLk/0.jpg)](https://www.youtube.com/watch?v=qEQkOA3ogLk)
> *SAP Developers · Code along: TabPFN predictions end to end in Colab (notebook linked in the video description)*

---
### TabPFN vs XGBoost: can a foundation model beat a tuned XGBoost with zero tuning?
[![TabPFN vs XGBoost: can a foundation model beat a tuned XGBoost with zero tuning?](https://img.youtube.com/vi/A7_rBOljbzk/0.jpg)](https://www.youtube.com/watch?v=A7_rBOljbzk)
> *Prior Labs · Demo: TabPFN with zero tuning against a tuned XGBoost; picks up where the previous lesson ends*

---
### TabPFN in Action: a Practical Workshop
[![TabPFN in Action: a Practical Workshop](https://img.youtube.com/vi/3hTm1I1vig0/0.jpg)](https://www.youtube.com/watch?v=3hTm1I1vig0)
> *Prior Labs · Optional, 61 minutes: Prior Labs' hands-on workshop ([Kaggle notebook](https://www.kaggle.com/code/carlmcbrideellis/prior-labs-binary-classification-with-tabpfn))*

---
### Google TabFM vs XGBoost: Zero-Shot Tabular, Tested Honestly
[![Google TabFM vs XGBoost: Zero-Shot Tabular, Tested Honestly](https://img.youtube.com/vi/FQ_NRPsNqsM/0.jpg)](https://www.youtube.com/watch?v=FQ_NRPsNqsM)
> *ML Engineer · Code along: Google TabFM against XGBoost ([notebook](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/tabfm))*

---
### TableGPT2 7B - AI Model for Structured Data - Install Locally
[![TableGPT2 7B - AI Model for Structured Data - Install Locally](https://img.youtube.com/vi/Y4dnCCD0p8A/0.jpg)](https://www.youtube.com/watch?v=Y4dnCCD0p8A)
> *Fahd Mirza · Hands-on: installing TableGPT2 and asking it questions about a table*

---

# Follow-along
**Notebooks:** [TabPFN hands-on demo (Colab)](https://colab.research.google.com/github/PriorLabs/TabPFN/blob/main/examples/notebooks/TabPFN_Demo_Local.ipynb) · [TabFM vs XGBoost (Colab)](https://colab.research.google.com/github/SaschaHeyer/gen-ai-livestream/blob/main/tabfm/notebook.ipynb) · [PriorLabs/TabPFN `examples/`](https://github.com/PriorLabs/TabPFN/tree/main/examples)

1. **TabPFN demo:** open the TabPFN hands-on demo on a T4 runtime and run the install cell. Restart the runtime when it tells you to. At *Backend Selection*, choose **local** (GPU) or **client** (no GPU; sends data to Prior Labs, so use public data only). Log in and accept the licence.
2. Code along through *Classification* and *Comparing TabPFN with Other Classifiers*. The notebook benchmarks TabPFN against XGBoost and CatBoost for you. Note the accuracy and time of each.
3. **Your data:** swap in the insurance claims data from [Gradient Boosting](./Tabular%20ML%20-%20Gradient%20Boosting.md) step 1 (`is_claim` target; subsample to 5,000 rows or fewer on CPU). Compare `TabPFNClassifier()` with **zero tuning** against your tuned XGBoost on AUC, calibration and wall-clock time.
4. **TabFM:** open the TabFM notebook. It needs Python 3.11+ (current Colab is fine), and the 6.6 GB weights download on first load. Run it, complete its *YOUR TURN* cells, then run TabFM on your claims split, raising `max_num_rows` above the default 100.
5. **Schema shift:** drop one column at prediction time, and add a new one. Note what TabPFN and TabFM do, and what XGBoost does.
6. **Text-to-table:** following the [tablegpt-agent quick start](https://tablegpt.github.io/tablegpt-agent/), ask TableGPT2 *"average claim value by vehicle type, as a bar chart"* about the claims CSV. Read the Python it writes and check the answer with pandas.
7. **Pricing committee note:** write half a page covering, for each model, its accuracy against XGBoost, its licence, data-privacy questions, and how you would explain its predictions.

---
_Last reviewed: 2026-11-06_
