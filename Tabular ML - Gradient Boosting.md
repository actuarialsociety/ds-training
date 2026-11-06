# Tabular ML - Gradient Boosting
> *For structured data (policies, claims, exposures), gradient-boosted decision trees are still the standard for production and for Kaggle. **XGBoost** is the industry workhorse. **CatBoost** handles categorical features natively. **LightGBM** is built for speed and low memory on very large data.*

# Prerequisites
- [Python - Intermediate](./Python%20-%20Intermediate.md) (scikit-learn: train/test split, fit/predict, cross-validation)
- [GPUs & Acceleration](./GPUs%20%26%20Acceleration.md) (Optional): for the GPU step
- GLM intuition (Poisson, Gamma, Tweedie) helps

# Objectives
- Explain how gradient boosting fits each new tree to the errors left by the previous trees, and how learning rate and number of trees trade off against overfitting
- Train **XGBoost** on mixed numeric and categorical features (`enable_categorical=True`) with early stopping, native missing-value handling, `scale_pos_weight` for imbalanced classes, and `device="cuda"`
- Use **CatBoost**'s native categorical handling for high-cardinality data, and explain how ordered boosting and symmetric trees resist overfitting
- Explain how **LightGBM** stays fast and light on massive data (histogram splits, leaf-wise growth, GOSS for many rows, EFB for many columns), and tune `num_leaves` and `min_data_in_leaf`
- Fit actuarial objectives (Gamma, Tweedie) and compare the three libraries on one dataset

# Content
* [XGBoost: Introduction to boosted trees](https://xgboost.readthedocs.io/en/stable/tutorials/model.html) · [Parameter tuning & imbalance](https://xgboost.readthedocs.io/en/stable/tutorials/param_tuning.html)
* [CatBoost Python quickstart](https://catboost.ai/docs/en/concepts/python-quickstart) · [How categoricals are encoded](https://catboost.ai/docs/en/concepts/algorithm-main-stages_cat-to-numberic)
* Optional, 57 minutes: [XGBoost in Python from Start to Finish (StatQuest)](https://www.youtube.com/watch?v=GrJP9FLV3FE)
* [XGBoost categorical data](https://xgboost.readthedocs.io/en/stable/tutorials/categorical.html)
* [LightGBM features](https://lightgbm.readthedocs.io/en/stable/Features.html) · [Parameter tuning](https://lightgbm.readthedocs.io/en/stable/Parameters-Tuning.html)

### Gradient Boost Part 1 (of 4): Regression Main Ideas
[![Gradient Boost Part 1 (of 4): Regression Main Ideas](https://img.youtube.com/vi/3CC4N4z3GJc/0.jpg)](https://www.youtube.com/watch?v=3CC4N4z3GJc)
> *StatQuest with Josh Starmer · The clearest explanation of how gradient boosting works*

---
### XGBoost Part 1 (of 4): Regression
[![XGBoost Part 1 (of 4): Regression](https://img.youtube.com/vi/OtD8wVaFm6E/0.jpg)](https://www.youtube.com/watch?v=OtD8wVaFm6E)
> *StatQuest with Josh Starmer · What XGBoost adds: regularisation, gain, pruning*

---
### CatBoost Part 1: Ordered Target Encoding
[![CatBoost Part 1: Ordered Target Encoding](https://img.youtube.com/vi/KXOTSkPL2X4/0.jpg)](https://www.youtube.com/watch?v=KXOTSkPL2X4)
> *StatQuest with Josh Starmer · How CatBoost encodes categories without target leakage*

---
### CatBoost Part 2: Building and Using Trees
[![CatBoost Part 2: Building and Using Trees](https://img.youtube.com/vi/3Bg2XRFOTzg/0.jpg)](https://www.youtube.com/watch?v=3Bg2XRFOTzg)
> *StatQuest with Josh Starmer · CatBoost's symmetric trees and why they resist overfitting*

---
### 196 - What is Light GBM and how does it compare against XGBoost?
[![196 - What is Light GBM and how does it compare against XGBoost?](https://img.youtube.com/vi/n_ZMQj09S6w/0.jpg)](https://www.youtube.com/watch?v=n_ZMQj09S6w)
> *DigitalSreeni · LightGBM concepts and a Python comparison with XGBoost*

---
### LightGBM Optimizations | Gradient Based One Side Sampling(GOSS) | Exclusive Feature Bundling( EFB)
[![LightGBM Optimizations | Gradient Based One Side Sampling(GOSS) | Exclusive Feature Bundling( EFB)](https://img.youtube.com/vi/OTDLjYxInp0/0.jpg)](https://www.youtube.com/watch?v=OTDLjYxInp0)
> *RoboSathi · LightGBM's GOSS and EFB tricks for huge row and column counts*

---
### Getting Started with Accelerated XGBoost
[![Getting Started with Accelerated XGBoost](https://img.youtube.com/vi/v0IFKPUzW_s/0.jpg)](https://www.youtube.com/watch?v=v0IFKPUzW_s)
> *NVIDIA Developer · Official 3-minute intro to GPU XGBoost*

---

# Follow-along
**Repos:** [dmlc/xgboost `demo/guide-python`](https://github.com/dmlc/xgboost/tree/master/demo/guide-python) · [catboost/tutorials](https://github.com/catboost/tutorials) · [microsoft/LightGBM `examples/python-guide`](https://github.com/microsoft/LightGBM/tree/master/examples/python-guide)

1. Run `pip install xgboost catboost lightgbm scikit-learn`, clone the three repos, and run `xgboost/demo/guide-python/basic_walkthrough.py`, `xgboost/demo/guide-python/categorical.py` (native categoricals) and `LightGBM/examples/python-guide/simple_example.py`.
2. Run `xgboost/demo/guide-python/gamma_regression.py`. It fits a Gamma objective, as you would for claim severity. Then switch to `objective="reg:tweedie", tweedie_variance_power=1.5` and compare.
3. Open `catboost/tutorials/categorical_features/categorical_features_parameters.ipynb`. Pass the categorical columns via `cat_features=` with no one-hot encoding, then compare against one-hot encoding.
4. On one dataset, fit all three libraries with early stopping on a validation set and record fit time and deviance/log-loss. Use a public insurance or claims CSV, e.g. `sklearn.datasets.fetch_openml("freMTPL2freq")`.
5. Blank out about 10% of one feature (set it to NaN) and refit XGBoost without imputing. For a binary target, set `scale_pos_weight = neg / pos` and compare PR-AUC.
6. *(GPU, optional)* Refit with `device="cuda"` (XGBoost), `task_type="GPU"` (CatBoost) and `device_type="gpu"` (LightGBM), and compare training times.

---
_Last reviewed: 2026-11-06_
