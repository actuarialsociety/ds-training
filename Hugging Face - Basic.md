# Hugging Face - Basic
> *Hugging Face is the "GitHub of machine learning". The **Hub** hosts 2M+ open models, datasets and demo apps (**Spaces**), and the `transformers` and `datasets` libraries let you use them in a few lines of Python. In this lesson you run pre-trained models on insurance text and load Hub datasets into pandas. Every video is a code-along, so type the code as you watch.*

# Prerequisites
- [Python - Basic](./Python%20-%20Basic.md) and [PyData Stack](./PyData%20Stack.md) (pandas)
- [Google Colab](./Google%20Colab.md): every notebook below opens there
- A free [Hugging Face account](https://huggingface.co/join)

# Objectives
- Find a model or dataset on the Hub and read its **card** (intended use, limitations, **licence**) before using it
- Create a read **access token** and log in from Colab (Secrets) or with `hf auth login`
- Run `pipeline()` for sentiment and zero-shot classification on claims and complaints text
- Summarise a claim note with a small chat model through the `text-generation` pipeline
- Load a Hub dataset with `load_dataset` and analyse it in pandas

# Key concepts
- **The Hub**: every model, dataset and Space is a versioned git repo. You can pin a `revision` so results are reproducible, which matters for model governance.
- **Cards and licences**: a repo's README is its card. Licences vary (MIT, Apache-2.0, CC, GPL, non-commercial), and *gated* models need you to accept terms first. Check before any commercial or regulated use.
- **`pipeline()`**: one call bundles the tokenizer, the model and post-processing. Always pass `model=` explicitly so results don't change when the default model changes.
- **Zero-shot classification**: you supply the labels at run time ("motor claim", "home claim", "complaint"), so you can triage text with **no training data**.
- **transformers v5 changes**: the `summarization`, `translation` and `question-answering` pipelines were removed. Use `text-generation` with a chat model instead. If an older notebook fails, this is usually why. As a fallback, run `pip install "transformers<5"`.
- **Tokens**: use a *read* token to download and a *write* token to push. Keep tokens in Colab Secrets or `hf auth login`, never in a notebook.

# Content
* [Hub documentation](https://huggingface.co/docs/hub/index) · [Model cards](https://huggingface.co/docs/hub/model-cards) · [Licences](https://huggingface.co/docs/hub/repositories-licenses) · [Access tokens](https://huggingface.co/docs/hub/security-tokens)
* [Pipelines tutorial](https://huggingface.co/docs/transformers/pipeline_tutorial) · [Datasets quickstart](https://huggingface.co/docs/datasets/quickstart) · [Datasets with pandas](https://huggingface.co/docs/datasets/use_with_pandas)
* [Hugging Face LLM course (free)](https://huggingface.co/learn/llm-course/chapter1/1)
* **Background (optional, not code):** [What is Hugging Face? (official tour)](https://www.youtube.com/watch?v=qP9mbY3wuWk) · [Navigating the Model Hub](https://www.youtube.com/watch?v=XvSGPZFEjDY)

### Pipelines | Language Models with Hugging Face Ep. 2
[![Pipelines | Language Models with Hugging Face Ep. 2](https://img.youtube.com/vi/T8_4IcWs9xA/0.jpg)](https://www.youtube.com/watch?v=T8_4IcWs9xA)
> *Kody Simpson · Code along: pipelines for sentiment, zero-shot, NER and generation ([notebook](https://github.com/KodySimpson/huggingface-language-models/blob/master/pipelines.ipynb))*

---
### Hugging Face Pipeline() Explained - Install & Run Your First Model - Lecture 2
[![Hugging Face Pipeline() Explained - Install & Run Your First Model - Lecture 2](https://img.youtube.com/vi/UyRzFsegCEM/0.jpg)](https://www.youtube.com/watch?v=UyRzFsegCEM)
> *Quantum Logics · Code along: install `transformers` and run your first model in 7 minutes*

---
### HuggingFace + Langchain | Run 1,000s of FREE AI Models Locally
[![HuggingFace + Langchain | Run 1,000s of FREE AI Models Locally](https://img.youtube.com/vi/1h6lfzJ0wZw/0.jpg)](https://www.youtube.com/watch?v=1h6lfzJ0wZw)
> *Tech With Tim · Code along: download and run Hub models locally on your own machine ([code](https://github.com/techwithtim/Langchain-Transformers-Python))*

---
### How To Download & Process Hugging Face Dataset - Train LLM, AI, Process Data
[![How To Download & Process Hugging Face Dataset - Train LLM, AI, Process Data](https://img.youtube.com/vi/1viiT0OlOYo/0.jpg)](https://www.youtube.com/watch?v=1viiT0OlOYo)
> *Vuk Rosić · Code along: download and process a Hub dataset in Colab*

---
### Inspecting & Slicing Hugging Face Datasets - Lecture 10
[![Inspecting & Slicing Hugging Face Datasets - Lecture 10](https://img.youtube.com/vi/8wRl7XPJVus/0.jpg)](https://www.youtube.com/watch?v=8wRl7XPJVus)
> *Quantum Logics · Code along: inspect, slice and shuffle a dataset*

---

# Follow-along
**Repos:** [KodySimpson/huggingface-language-models](https://github.com/KodySimpson/huggingface-language-models) (the notebooks from video 1 and the Intermediate lesson) · [huggingface/notebooks](https://github.com/huggingface/notebooks) · **Data:** [Bitext insurance customer messages](https://huggingface.co/datasets/bitext/Bitext-insurance-llm-chatbot-training-dataset) (39k rows, 17 categories; some rows deliberately contain rude language)

1. **Token:** create a **Read** token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens). In Colab, click the key icon, add a secret called `HF_TOKEN` and turn on *Notebook access*. Locally, run `hf auth login`.
2. **Pipelines (video 1):** open [`pipelines.ipynb` in Colab](https://colab.research.google.com/github/KodySimpson/huggingface-language-models/blob/master/pipelines.ipynb) and code along. Then point it at insurance text:
   ```python
   from transformers import pipeline
   sentiment = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
   sentiment(["The adjuster settled my claim quickly and fairly.", "Three months and still no response on my claim."])

   triage = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
   triage("Hail damaged the roof and water came into the bedroom.",
          candidate_labels=["motor claim", "home claim", "life claim", "complaint"])
   ```
3. **Summarise a claim note** (the v5 way):
   ```python
   gen = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M-Instruct")
   note = ("Insured reports rear-end collision at a traffic light on 3 Oct; third party admitted liability; "
           "bumper and boot damaged; no injuries; car towed to approved repairer.")
   out = gen([{"role": "user", "content": f"Summarise this claim note in one sentence: {note}"}], max_new_tokens=60)
   print(out[0]["generated_text"][-1]["content"])
   ```
4. **Datasets into pandas (videos 4–5):**
   ```python
   from datasets import load_dataset
   ds = load_dataset("bitext/Bitext-insurance-llm-chatbot-training-dataset", split="train")
   df = ds.to_pandas()
   df["category"].value_counts()
   ds.filter(lambda r: r["category"] == "CLAIMS").shuffle(seed=0).select(range(5))["instruction"]
   ```
5. **Now try:** run zero-shot on 20 rows of `df["instruction"]`, using the 17 category names as labels, and compare the predictions with `df["category"]`. How accurate is it with no training? You will beat it in [Hugging Face - Intermediate](./Hugging%20Face%20-%20Intermediate.md).
6. **Read the cards:** open the cards for `facebook/bart-large-mnli` and the Bitext dataset. Note each licence and intended use, and whether you could use them at work.

---
_Last reviewed: 2026-11-06_
