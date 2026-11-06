# Hugging Face - Advanced
> *Train big models cheaply with **LoRA** and **4-bit quantisation**, call open LLMs through **Inference Providers**, ship a demo to **Spaces**, and build **agents** that write and run Python to analyse claims data. Every video is a code-along. Most of the code runs on a free Colab T4.*

# Prerequisites
- [Hugging Face - Intermediate](./Hugging%20Face%20-%20Intermediate.md)
- [GPUs & Acceleration](./GPUs%20%26%20Acceleration.md) and a Colab T4 or better
- For Inference Providers: purchased credits or a PRO plan (free accounts get no monthly credit any more)

# Objectives
- Fine-tune the insurance classifier with a **LoRA** adapter and compare trainable parameters and macro-F1 with full fine-tuning
- Load a model in **4-bit** with `BitsAndBytesConfig` and measure the memory saved
- Call open models with `InferenceClient`, and know when to use dedicated **Inference Endpoints** instead
- Deploy a Gradio app for your classifier to a **Space**
- Build an agent, first from scratch and then with **smolagents**, that analyses the freMTPL2 claims-frequency data

# Key concepts
- **LoRA / PEFT**: freeze the base model and learn small low-rank update matrices (rank `r`, scale `lora_alpha`). Usually under 1% of the parameters train, and the adapter is a few MB you can share, swap, or merge with `merge_and_unload()`.
- **Quantisation**: store weights in 8-bit or 4-bit (NF4) to cut memory 2–4×, at a small cost in accuracy. **QLoRA** trains LoRA adapters on a 4-bit base, so billion-parameter models fit on one GPU. The T4 has no bf16, so compute in float16.
- **Inference Providers vs Endpoints**: *Providers* is one OpenAI-compatible API, billed per call, that routes to serverless partners. *Endpoints* are dedicated, autoscaling deployments where you choose the instance, region and private networking. Endpoints are usually the right choice for production or data-residency needs.
- **Spaces**: git repos that run a Gradio, Docker or static app. Free accounts can host up to 2 **ZeroGPU** Gradio Spaces (verified email, account older than 30 days). CPU Gradio and Docker Spaces need a paid plan.
- **Agents**: an LLM loops through *think → call a tool or write code → observe*. A smolagents `CodeAgent` writes Python rather than JSON tool calls. Restrict `additional_authorized_imports`, and treat its output as a draft that needs actuarial review.
- **CLI**: the CLI is now `hf ...`, e.g. `hf auth login`, `hf repos create`, `hf upload`.

# Content
* [PEFT quicktour](https://huggingface.co/docs/peft/quicktour) · [bitsandbytes quantisation](https://huggingface.co/docs/transformers/quantization/bitsandbytes) · [LLM course ch. 11: fine-tuning LLMs](https://huggingface.co/learn/llm-course/chapter11/1)
* [Inference Providers](https://huggingface.co/docs/inference-providers/index) · [pricing](https://huggingface.co/docs/inference-providers/pricing) · [Inference Endpoints](https://huggingface.co/docs/inference-endpoints/index)
* [Gradio Spaces](https://huggingface.co/docs/hub/spaces-sdks-gradio) · [ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu) · [Gradio quickstart](https://www.gradio.app/guides/quickstart)
* [smolagents guided tour](https://huggingface.co/docs/smolagents/guided_tour) · [Agents course (free)](https://huggingface.co/learn/agents-course/unit0/introduction) · [Enterprise Hub (SSO, audit logs, regions)](https://huggingface.co/docs/hub/enterprise-hub)
* **Background (optional, not code):** [LoRA explained by its inventor](https://www.youtube.com/watch?v=DhRoTONcyZE) · [Inference Providers overview](https://www.youtube.com/watch?v=oxwsizy1Spw) · [The Hub for Enterprise](https://www.youtube.com/watch?v=wUzfRBi9wZ0)

### How to Implement LoRA with Hugging Face PEFT: Step-by-Step Tutorial
[![How to Implement LoRA with Hugging Face PEFT: Step-by-Step Tutorial](https://img.youtube.com/vi/F29Y_y7g6IY/0.jpg)](https://www.youtube.com/watch?v=F29Y_y7g6IY)
> *SH AI Academy · Code along: LoRA with the PEFT library, step by step*

---
### BitsAndBytesConfig & QLoRA Explained - Hugging Face Lecture 23
[![BitsAndBytesConfig & QLoRA Explained - Hugging Face Lecture 23](https://img.youtube.com/vi/75pPfUUFhl4/0.jpg)](https://www.youtube.com/watch?v=75pPfUUFhl4)
> *Quantum Logics · Code along: 4-bit loading with BitsAndBytesConfig and QLoRA*

---
### Intro to Agents - Create an Agent from Scratch (No Frameworks)
[![Intro to Agents - Create an Agent from Scratch (No Frameworks)](https://img.youtube.com/vi/vHDwpoSFdQY/0.jpg)](https://www.youtube.com/watch?v=vHDwpoSFdQY)
> *Alejandro AO · Code along: build an agent from scratch on Inference Providers ([official notebook](https://github.com/huggingface/hub-tutorials/blob/main/notebooks/01-agents-from-scratch.ipynb))*

---
### Building Agents with Smolagents
[![Building Agents with Smolagents](https://img.youtube.com/vi/dSGS6-iGhyo/0.jpg)](https://www.youtube.com/watch?v=dSGS6-iGhyo)
> *Hugging Face · Code along: the same idea with smolagents ([official notebook](https://github.com/huggingface/hub-tutorials/blob/main/notebooks/02-intro-to-smolagents.ipynb))*

---
### Build AI Apps with Hugging Face Spaces
[![Build AI Apps with Hugging Face Spaces](https://img.youtube.com/vi/54zXAlLmIQE/0.jpg)](https://www.youtube.com/watch?v=54zXAlLmIQE)
> *Joe Maddalone · Code along: build and deploy an app on Spaces*

---
### End-to-End (small) LLM Fine-tuning Tutorial (from data to model to live demo) | On DGX Spark
[![End-to-End (small) LLM Fine-tuning Tutorial (from data to model to live demo) | On DGX Spark](https://img.youtube.com/vi/2hoNAr-id-E/0.jpg)](https://www.youtube.com/watch?v=2hoNAr-id-E)
> *Daniel Bourke · Optional, 59 minutes: end-to-end fine-tuning from data to model to live demo (Colab in the description)*

---

# Follow-along
**Notebooks:** [PEFT `LoRA.ipynb`](https://colab.research.google.com/github/huggingface/peft/blob/main/examples/sequence_classification/LoRA.ipynb) · [hub-tutorials 01: agents from scratch](https://colab.research.google.com/github/huggingface/hub-tutorials/blob/main/notebooks/01-agents-from-scratch.ipynb) · [hub-tutorials 02: smolagents](https://colab.research.google.com/github/huggingface/hub-tutorials/blob/main/notebooks/02-intro-to-smolagents.ipynb) · **Data:** [freMTPL2 claims frequency](https://huggingface.co/datasets/mabilton/fremtpl2) (GPL-2.0)

1. **LoRA (video 1):** open `LoRA.ipynb`, change `model_name_or_path` to `"roberta-base"` so it fits on a T4, and run it. Note what `print_trainable_parameters()` reports. Then apply LoRA to your Intermediate classifier and re-use its `Trainer` code:
   ```python
   from peft import LoraConfig, get_peft_model
   model = get_peft_model(AutoModelForSequenceClassification.from_pretrained(
       ckpt, num_labels=len(names), id2label=dict(enumerate(names)), label2id={n: i for i, n in enumerate(names)}),
       LoraConfig(task_type="SEQ_CLS", r=8, lora_alpha=16, lora_dropout=0.1))
   model.print_trainable_parameters()
   ```
   Compare macro-F1 and the size of the saved adapter with full fine-tuning.
2. **4-bit (video 2):**
   ```python
   import torch
   from transformers import AutoModelForCausalLM, BitsAndBytesConfig
   mid = "HuggingFaceTB/SmolLM3-3B"
   fp16 = AutoModelForCausalLM.from_pretrained(mid, dtype=torch.float16, device_map="auto")
   print(fp16.get_memory_footprint() / 1e9); del fp16; torch.cuda.empty_cache()
   q4 = AutoModelForCausalLM.from_pretrained(mid, device_map="auto", quantization_config=BitsAndBytesConfig(
       load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.float16))
   print(q4.get_memory_footprint() / 1e9)
   ```
3. **Agent from scratch (video 3):** code along with notebook 01. If its default model isn't available, pick a live one from [the providers list](https://huggingface.co/models?inference_provider=all), e.g. `openai/gpt-oss-20b`. Then ask it: *"List 3 rating factors for motor third-party liability and why each matters."*
4. **smolagents on claims data (video 4):** code along with notebook 02, then point an agent at freMTPL2:
   ```python
   from huggingface_hub import hf_hub_download
   from smolagents import CodeAgent, InferenceClientModel
   path = hf_hub_download("mabilton/fremtpl2", "freMTPL2freq.csv", repo_type="dataset")
   agent = CodeAgent(tools=[], model=InferenceClientModel(model_id="openai/gpt-oss-20b"),
                     additional_authorized_imports=["pandas", "numpy"], max_steps=10)
   agent.run("Load the CSV at source_file. Compute claim frequency = sum(ClaimNb)/sum(Exposure) "
             "by DrivAge band (18-25, 26-40, 41-60, 61+) and by Area. Report a table and two insights.",
             additional_args={"source_file": path})
   ```
   Check every number yourself in pandas. Use `max_steps`; the old `max_iterations` argument raises a `TypeError`.
5. **Ship it to a Space (video 5):** create `app.py`:
   ```python
   import gradio as gr
   from transformers import pipeline
   clf = pipeline("text-classification", model="<user>/insurance-intent-distilbert")
   gr.Interface(fn=lambda t: {d["label"]: d["score"] for d in clf(t, top_k=5)},
                inputs=gr.Textbox(label="Customer message"), outputs=gr.Label()).launch()
   ```
   Add a `requirements.txt` with `transformers` and `torch`, then run:
   ```bash
   hf repos create insurance-intent-demo --type space --sdk gradio --flavor zero-a10g
   hf upload <user>/insurance-intent-demo . . --repo-type space
   ```
   Your model repo is private, so add a read token as a Space **secret** called `HF_TOKEN`.
6. **Now try:** merge your LoRA adapter with `merge_and_unload()` and serve the merged model from the Space. Or swap the agent's model for a local `TransformersModel` and compare the quality of its answers.

---
_Last reviewed: 2026-11-06_
