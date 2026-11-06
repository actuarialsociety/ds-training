# Hugging Face - Intermediate
> *Go beneath `pipeline()`: tokenise text yourself, run models by hand, **fine-tune** a classifier on your own labelled data, share it on the Hub, and use **embeddings** for semantic search. The running example classifies insurance customer messages into 17 categories, so you can compare it with zero-shot from the Basic lesson. Every video is a code-along.*

# Prerequisites
- [Hugging Face - Basic](./Hugging%20Face%20-%20Basic.md)
- [Python - Intermediate](./Python%20-%20Intermediate.md) (train/test split, metrics)
- A Colab **T4 GPU** runtime ([GPUs & Acceleration](./GPUs%20%26%20Acceleration.md))

# Objectives
- Tokenise text with `AutoTokenizer` and run `AutoModelForSequenceClassification` by hand (logits → softmax → labels)
- Prepare data with `map`, `filter`, `class_encode_column` and a stratified `train_test_split`
- Fine-tune DistilBERT with `Trainer` on insurance messages and report accuracy and **macro-F1**
- Push the model and the prepared dataset to the Hub as **private** repos
- Build semantic search over messages with `sentence-transformers`

# Key concepts
- **Tokenizer**: splits text into sub-word IDs and adds an *attention mask*. Padding and truncation make every row in a batch the same length. The tokenizer must match its model checkpoint.
- **Auto classes**: `AutoModel` returns hidden states. `AutoModelFor…` adds a task head. For a custom head, set `num_labels`, `id2label` and `label2id`.
- **Fine-tuning with `Trainer`**: a training loop with evaluation, checkpointing, mixed precision and Hub upload built in. In transformers v5, use `eval_strategy` (not `evaluation_strategy`) and `processing_class=tokenizer`.
- **Evaluation**: insurance classes are imbalanced, so report macro-F1 and a confusion matrix, not just accuracy, as you would for any classification model.
- **Sharing**: `trainer.push_to_hub()` uploads the weights plus an auto-generated model card. `Dataset.push_to_hub(..., private=True)` versions your data. Keep company data in private repos.
- **Embeddings**: a `SentenceTransformer` maps text to vectors, and cosine similarity finds the nearest neighbours. Uses include similar-claim lookup, matching complaints to policy wording and de-duplication.

# Content
* [LLM course ch. 2: Using transformers](https://huggingface.co/learn/llm-course/chapter2/1) · [ch. 3: Fine-tuning with Trainer](https://huggingface.co/learn/llm-course/chapter3/3) · [ch. 4: Sharing models](https://huggingface.co/learn/llm-course/chapter4/3)
* [Text classification task guide](https://huggingface.co/docs/transformers/tasks/sequence_classification) · [Process datasets](https://huggingface.co/docs/datasets/process) · [Evaluate](https://huggingface.co/docs/evaluate/index)
* [Sentence Transformers quickstart](https://sbert.net/docs/quickstart.html) · [Semantic search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)
* **Longer code-along (optional, 5 hours):** [Build a Text Classification Model with Hugging Face from Scratch](https://www.youtube.com/watch?v=XNDY7jtihok) · [code](https://github.com/mrdbourke/learn-huggingface)

### Using Fine-Tuned Models | Language Models with Hugging Face Ep. 3
[![Using Fine-Tuned Models | Language Models with Hugging Face Ep. 3](https://img.youtube.com/vi/yWYmenZo4JQ/0.jpg)](https://www.youtube.com/watch?v=yWYmenZo4JQ)
> *Kody Simpson · Code along: AutoTokenizer and AutoModel by hand, instead of a pipeline ([notebook](https://github.com/KodySimpson/huggingface-language-models/blob/master/using_fine_tuned.ipynb))*

---
### Tokenizers | Language Models with Hugging Face Ep. 4
[![Tokenizers | Language Models with Hugging Face Ep. 4](https://img.youtube.com/vi/xBta2Z2-tY0/0.jpg)](https://www.youtube.com/watch?v=xBta2Z2-tY0)
> *Kody Simpson · Code along: how tokenizers work ([notebook](https://github.com/KodySimpson/huggingface-language-models/blob/master/tokenizers.ipynb))*

---
### Batch Inference & Padding | Language Models with Hugging Face Ep. 5
[![Batch Inference & Padding | Language Models with Hugging Face Ep. 5](https://img.youtube.com/vi/hJPpj9Eg-eA/0.jpg)](https://www.youtube.com/watch?v=hJPpj9Eg-eA)
> *Kody Simpson · Code along: batching and padding ([notebook](https://github.com/KodySimpson/huggingface-language-models/blob/master/batch_inference.ipynb))*

---
### Fine Tuning a DistilBERT Model for Text Classification | Language Models with Hugging Face Ep. 7
[![Fine Tuning a DistilBERT Model for Text Classification | Language Models with Hugging Face Ep. 7](https://img.youtube.com/vi/nxBHvP043Nw/0.jpg)](https://www.youtube.com/watch?v=nxBHvP043Nw)
> *Kody Simpson · Code along: fine-tune DistilBERT for text classification with Trainer ([notebook](https://github.com/KodySimpson/huggingface-language-models/blob/master/fine_tune_emotion.ipynb))*

---
### Fine-Tune BERT for ANY Text Classification Task| Explained With Code
[![Fine-Tune BERT for ANY Text Classification Task| Explained With Code](https://img.youtube.com/vi/EAIil0wD-1A/0.jpg)](https://www.youtube.com/watch?v=EAIil0wD-1A)
> *Nachiketa Hebbar · Code along: fine-tune BERT for any classification task ([code](https://github.com/nachi-hebbar/LLM-Prompting))*

---
### From Text to Meaning: Semantic Search with Sentence Embeddings Explained
[![From Text to Meaning: Semantic Search with Sentence Embeddings Explained](https://img.youtube.com/vi/Cu7Yp2_GAZk/0.jpg)](https://www.youtube.com/watch?v=Cu7Yp2_GAZk)
> *GeoDev · Code along: semantic search with sentence embeddings (Colab linked in the description)*

---

# Follow-along
**Repo:** [KodySimpson/huggingface-language-models](https://github.com/KodySimpson/huggingface-language-models). Open each notebook in Colab, e.g. [`fine_tune_emotion.ipynb`](https://colab.research.google.com/github/KodySimpson/huggingface-language-models/blob/master/fine_tune_emotion.ipynb), on a **T4 GPU** runtime.

1. **By hand (videos 1–3):** code along with `using_fine_tuned.ipynb`, `tokenizers.ipynb` and `batch_inference.ipynb`. Then tokenise `"My windscreen cracked, am I covered?"` and inspect `input_ids` and `attention_mask`.
2. **Fine-tune (video 4):** code along with `fine_tune_emotion.ipynb`. If a cell fails on transformers v5, change `evaluation_strategy` to `eval_strategy`.
3. **Swap in insurance data:**
   ```python
   from datasets import load_dataset
   from transformers import AutoTokenizer, AutoModelForSequenceClassification, DataCollatorWithPadding
   ds = load_dataset("bitext/Bitext-insurance-llm-chatbot-training-dataset", split="train")
   ds = ds.select_columns(["instruction", "category"]).rename_columns({"instruction": "text", "category": "label"})
   ds = ds.class_encode_column("label").train_test_split(test_size=0.2, stratify_by_column="label", seed=42)
   ds["train"] = ds["train"].shuffle(seed=42).select(range(5000))   # keep it fast
   ds["test"] = ds["test"].shuffle(seed=42).select(range(1000))
   names = ds["train"].features["label"].names
   ckpt = "distilbert/distilbert-base-uncased"
   tok = AutoTokenizer.from_pretrained(ckpt)
   tokd = ds.map(lambda b: tok(b["text"], truncation=True), batched=True)
   model = AutoModelForSequenceClassification.from_pretrained(
       ckpt, num_labels=len(names), id2label=dict(enumerate(names)), label2id={n: i for i, n in enumerate(names)})
   ```
4. **Train and evaluate:**
   ```python
   import numpy as np, evaluate
   from transformers import TrainingArguments, Trainer
   acc, f1 = evaluate.load("accuracy"), evaluate.load("f1")
   def compute_metrics(p):
       preds = np.argmax(p.predictions, axis=-1)
       return {**acc.compute(predictions=preds, references=p.label_ids),
               **f1.compute(predictions=preds, references=p.label_ids, average="macro")}
   args = TrainingArguments("insurance-intent-distilbert", eval_strategy="epoch", num_train_epochs=2,
                            per_device_train_batch_size=32, report_to="none",
                            hub_private_repo=True)  # used when you push in step 5
   trainer = Trainer(model, args, train_dataset=tokd["train"], eval_dataset=tokd["test"],
                     data_collator=DataCollatorWithPadding(tok), processing_class=tok, compute_metrics=compute_metrics)
   trainer.train()
   ```
   Compare macro-F1 with the zero-shot result from the Basic lesson.
5. **Share privately:** log in with a **write** token (`from huggingface_hub import login; login()`), then run:
   ```python
   trainer.push_to_hub()
   ds.push_to_hub("<your-username>/insurance-intents-split", private=True)
   ```
   Reload it with `pipeline("text-classification", model="<your-username>/insurance-intent-distilbert")`. Compare `model_sharing.ipynb` in the repo.
6. **Semantic search (video 6):**
   ```python
   from sentence_transformers import SentenceTransformer
   st = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
   corpus = ds["test"]["text"]
   emb = st.encode(corpus, convert_to_tensor=True)
   scores = st.similarity(st.encode(["hail damaged my roof, how do I claim?"], convert_to_tensor=True), emb)[0]
   for i in scores.topk(5).indices.tolist(): print(round(float(scores[i]), 3), corpus[i])
   ```
7. **Now try:** train on `intent` (39 classes) instead of `category`, and compare macro-F1.

---
_Last reviewed: 2026-11-06_
