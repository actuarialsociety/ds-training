# GPUs & Acceleration
> *A CPU has a few fast, general-purpose cores. A GPU has thousands of simple cores that all work at once. Data science is mostly the same operation applied to millions of rows, which is exactly what a GPU is good at. You turned one on in [Google Colab](./Google%20Colab.md); here you learn why it helps and how to use it, usually with **zero code changes**.*

# Prerequisites
- [Google Colab](./Google%20Colab.md) (T4 GPU runtime)
- [PyData Stack](./PyData%20Stack.md) (pandas) and a little scikit-learn

# Objectives
- Explain CPU vs GPU and what CUDA is, in plain language
- Check for a GPU with `!nvidia-smi` and `torch.cuda.is_available()`
- Speed up existing pandas code with `%load_ext cudf.pandas` and existing scikit-learn code with `%load_ext cuml.accel`
- Train XGBoost on the GPU with `device="cuda"`
- Judge when a GPU helps (large, vectorised work) and when it does not (small data, row-by-row Python loops)

# Content
* [What's the difference between a CPU and a GPU? (NVIDIA)](https://blogs.nvidia.com/blog/whats-the-difference-between-a-cpu-and-a-gpu/)
* [cuDF pandas accelerator mode](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/)
* [cuML zero-code-change acceleration](https://docs.rapids.ai/api/cuml/stable/zero-code-change/)
* [XGBoost GPU support](https://xgboost.readthedocs.io/en/stable/gpu/index.html)

### Nvidia CUDA in 100 Seconds
[![Nvidia CUDA in 100 Seconds](https://img.youtube.com/vi/pPStdjuYzSI/0.jpg)](https://www.youtube.com/watch?v=pPStdjuYzSI)
> *Fireship · CUDA and parallelism in 100 seconds*

---
### CPU Vs GPU Explained With Real-World Analogies
[![CPU Vs GPU Explained With Real-World Analogies](https://img.youtube.com/vi/v21wuW_uYZ4/0.jpg)](https://www.youtube.com/watch?v=v21wuW_uYZ4)
> *BeSA Cloud Academy · CPU vs GPU through everyday analogies*

---
### Faster pandas on Colab
[![Faster pandas on Colab](https://img.youtube.com/vi/D6dCVNWLaFM/0.jpg)](https://www.youtube.com/watch?v=D6dCVNWLaFM)
> *NVIDIA Developer · Official short: faster pandas on Colab*

---
### Accelerate pandas 150x with NVIDIA cuDF and Zero Code Changes
[![Accelerate pandas 150x with NVIDIA cuDF and Zero Code Changes](https://img.youtube.com/vi/HXzveO9NEVA/0.jpg)](https://www.youtube.com/watch?v=HXzveO9NEVA)
> *NVIDIA Developer · Official cudf.pandas demo, zero code changes*

---
### Accelerate scikit-learn 50x on GPUs with cuML — Zero Code Change
[![Accelerate scikit-learn 50x on GPUs with cuML — Zero Code Change](https://img.youtube.com/vi/cIJsVq8CPys/0.jpg)](https://www.youtube.com/watch?v=cIJsVq8CPys)
> *NVIDIA Developer · The same trick for scikit-learn with cuML*

---
### Accelerated Machine Learning with XGBoost on NVIDIA GPUs | Accelerated Data Science Series
[![Accelerated Machine Learning with XGBoost on NVIDIA GPUs | Accelerated Data Science Series](https://img.youtube.com/vi/lhraJRaDkOA/0.jpg)](https://www.youtube.com/watch?v=lhraJRaDkOA)
> *NVIDIA Developer · GPU XGBoost on Colab; leads into Tabular ML*

---

# Follow-along
**Repo:** [rapidsai-community/showcase `getting_started_tutorials/`](https://github.com/rapidsai-community/showcase/tree/main/getting_started_tutorials) · [cudf.pandas notebook in Colab](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cudf_pandas_colab_demo.ipynb) · [cuML notebook in Colab](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cuml_sklearn_colab_demo.ipynb)

1. On a T4 runtime, run `!nvidia-smi`, then `import torch; torch.cuda.is_available()`. The second should print `True`.
2. Open the cudf.pandas notebook and run the groupby and merge cells on plain pandas, timing each one with `%%time`.
3. Restart the runtime and add `%load_ext cudf.pandas` as the first cell, **before** `import pandas`. Re-run the same cells unchanged and compare the timings. Use `%%cudf.pandas.profile` to see which operations ran on the GPU.
4. Open the cuML notebook and compare a scikit-learn model with and without `%load_ext cuml.accel`.
5. Time XGBoost on the CPU, then on the GPU:
   ```python
   from sklearn.datasets import make_classification
   import xgboost as xgb
   X, y = make_classification(n_samples=1_000_000, n_features=50, random_state=0)
   %time xgb.XGBClassifier(tree_method="hist", device="cpu").fit(X, y)
   %time xgb.XGBClassifier(tree_method="hist", device="cuda").fit(X, y)
   ```
6. Repeat step 5 with `n_samples=10_000`. Is the GPU still faster? Explain why or why not.

---
_Last reviewed: 2026-11-06_
