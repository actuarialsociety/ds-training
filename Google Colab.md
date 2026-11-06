# Google Colab
> *Colab runs Jupyter notebooks in your browser on Google's machines. There is nothing to install, it includes a free GPU, and it opens any notebook on GitHub. This is where you first meet a GPU.*

# Prerequisites
- [Python - Basic](./Python%20-%20Basic.md) (Jupyter notebooks)
- A Google account

# Objectives
- Create, run and share a notebook, and understand that the runtime VM is temporary
- Switch the runtime to a free **T4 GPU** and check it with `!nvidia-smi`
- Mount Google Drive so files persist between sessions
- Open any GitHub notebook with `colab.research.google.com/github/<owner>/<repo>/blob/<branch>/<path>.ipynb`
- Use Gemini in Colab to generate and explain code, and check its output before trusting it

# Content
* [Welcome to Colab notebook](https://colab.research.google.com/notebooks/intro.ipynb)
* [Colab FAQ: usage limits & GPUs](https://research.google.com/colaboratory/faq.html)
* [External data: Drive, Sheets & files](https://colab.research.google.com/notebooks/io.ipynb)
* [Data Science Agent in Colab](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/)

### Get started with Google Colaboratory (Coding TensorFlow)
[![Get started with Google Colaboratory (Coding TensorFlow)](https://img.youtube.com/vi/inN8seMm7UI/0.jpg)](https://www.youtube.com/watch?v=inN8seMm7UI)
> *TensorFlow · Official intro; older, but the basics have not changed*

---
### Google Colab for Data Science (2025): Setup, Drive Mount, GPU, Secrets, Gemini & Quick Dashboard
[![Google Colab for Data Science (2025): Setup, Drive Mount, GPU, Secrets, Gemini & Quick Dashboard](https://img.youtube.com/vi/-UTH9F9LqwU/0.jpg)](https://www.youtube.com/watch?v=-UTH9F9LqwU)
> *KSR Datavizon  · Recent, covers almost every objective: Drive, GPU, secrets, Gemini*

---
### Making the most of Colab (TF Dev Summit '20)
[![Making the most of Colab (TF Dev Summit '20)](https://img.youtube.com/vi/pnClcwTCyc0/0.jpg)](https://www.youtube.com/watch?v=pnClcwTCyc0)
> *TensorFlow · Tips from the Colab team: runtimes, GPUs, forms*

---
### Just in from the news desk 📰: Gemini-powered coding tools are now live in Google Colab!
[![Just in from the news desk 📰: Gemini-powered coding tools are now live in Google Colab!](https://img.youtube.com/vi/fviyXkQX2a8/0.jpg)](https://www.youtube.com/watch?v=fviyXkQX2a8)
> *Google for Developers · Official short on Gemini coding tools in Colab*

---
### Free Data Science Agent Powered By Gemini
[![Free Data Science Agent Powered By Gemini](https://img.youtube.com/vi/nHxXKyKYXqw/0.jpg)](https://www.youtube.com/watch?v=nHxXKyKYXqw)
> *Data Science Basics | AI · The Gemini Data Science Agent, end to end*

---

# Follow-along
**Repo:** [googlecolab/colabtools `notebooks/`](https://github.com/googlecolab/colabtools/tree/main/notebooks) · [Open the GitHub demo in Colab](https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb)

1. Open the demo link above. Then build a Colab URL yourself for this lesson's next notebook: `https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cudf_pandas_colab_demo.ipynb`.
2. Go to **Runtime → Change runtime type → T4 GPU** and run `!nvidia-smi`. Note the GPU name and memory. You will need this in [GPUs & Acceleration](./GPUs%20%26%20Acceleration.md).
3. Mount Drive and check that a file survives a runtime restart:
   ```python
   from google.colab import drive; drive.mount('/content/drive')
   import pandas as pd
   pd.DataFrame({"age_band": ["18-25", "26-40"], "claims": [12, 7]}).to_csv("/content/drive/MyDrive/claims.csv", index=False)
   ```
   Restart the runtime and read the CSV back.
4. Ask Gemini: *"load claims.csv and plot claims by age band"*. Read the code before you run it.
5. **File → Save a copy in GitHub** (or Drive), and share a view-only link.

---
_Last reviewed: 2026-11-06_
