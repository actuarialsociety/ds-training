# Tabular ML - Gradient Boosting
> *For structured data (policies, claims, exposures), gradient-boosted decision trees are still the standard for production and for Kaggle. **XGBoost** is the industry workhorse. **CatBoost** handles categorical features natively. **LightGBM** is built for speed and low memory on very large data. In every video below, someone writes and runs the code. Pause, type it yourself, and keep the linked notebook open beside you.*

# Prerequisites
- [Python - Intermediate](./Python%20-%20Intermediate.md) (scikit-learn: train/test split, fit/predict, cross-validation)
- [Google Colab](./Google%20Colab.md) to run the notebooks; [GPUs & Acceleration](./GPUs%20%26%20Acceleration.md) (Optional) for the GPU step
- GLM intuition (Poisson, Gamma, Tweedie) helps

# Objectives
- Build an end-to-end claims model with XGBoost: cleaning, stratified split, pipeline, evaluation
- Train **XGBoost** on mixed numeric and categorical features (`enable_categorical=True`) with early stopping, native missing-value handling and `scale_pos_weight` for imbalanced classes
- Use **CatBoost** on high-cardinality categoricals via `cat_features=`, with no one-hot encoding
- Train **LightGBM** on a large dataset and tune `num_leaves` and `min_data_in_leaf`
- Fit actuarial objectives (Gamma, Tweedie) and compare the three libraries on one dataset

# Key concepts
- **Boosting**: each new tree is fitted to the errors left by the trees before it, and its contribution is shrunk by the *learning rate*. More trees with a smaller learning rate usually generalise better. Early stopping picks the number of trees for you.
- **XGBoost**: adds regularisation to every split. It learns a default direction for missing values, so you don't need to impute. `scale_pos_weight ≈ negatives/positives` rebalances rare events such as claims or fraud.
- **CatBoost**: encodes each category from the target values of *earlier* rows only ("ordered" target statistics), which avoids target leakage. Its symmetric trees use the same split across a whole level, which resists overfitting and predicts fast. Good for occupation, vehicle make, postcode and similar high-cardinality fields.
- **LightGBM**: buckets feature values into histograms and grows the leaf with the biggest gain first. It samples rows by gradient (GOSS) and bundles sparse columns (EFB), so it stays fast on millions of rows and thousands of columns.
- **Actuarial objectives**: all three support Poisson (frequency), Gamma (severity) and Tweedie (pure premium), so the GLM structure you know carries over.

# Content
* [XGBoost: Introduction to boosted trees](https://xgboost.readthedocs.io/en/stable/tutorials/model.html) · [Categorical data](https://xgboost.readthedocs.io/en/stable/tutorials/categorical.html) · [Parameter tuning & imbalance](https://xgboost.readthedocs.io/en/stable/tutorials/param_tuning.html)
* [CatBoost Python quickstart](https://catboost.ai/docs/en/concepts/python-quickstart)
* [LightGBM Python intro](https://lightgbm.readthedocs.io/en/stable/Python-Intro.html) · [Parameter tuning](https://lightgbm.readthedocs.io/en/stable/Parameters-Tuning.html)
* **Background theory (optional, watch any time):** StatQuest [Gradient Boost](https://www.youtube.com/watch?v=3CC4N4z3GJc) · [XGBoost](https://www.youtube.com/watch?v=OtD8wVaFm6E) · [CatBoost encoding](https://www.youtube.com/watch?v=KXOTSkPL2X4) · [CatBoost trees](https://www.youtube.com/watch?v=3Bg2XRFOTzg) · [LightGBM GOSS & EFB](https://www.youtube.com/watch?v=OTDLjYxInp0)

### End-to-End ML/Data Science Project (with XGBoost) | Car Insurance Claims Prediction
[![End-to-End ML/Data Science Project (with XGBoost) | Car Insurance Claims Prediction](https://img.youtube.com/vi/wFUMqh5JePA/0.jpg)](https://www.youtube.com/watch?v=wFUMqh5JePA)
> *Harry's Data Journey · Code along: an end-to-end car insurance claims model with XGBoost ([code](https://github.com/harryallum/Data-Science-Projects/tree/main/Car%20Insurance%20Claim%20Prediction))*

---
### XGBoost Model in Python | Tutorial | Machine Learning
[![XGBoost Model in Python | Tutorial | Machine Learning](https://img.youtube.com/vi/ap2SS0-XPcE/0.jpg)](https://www.youtube.com/watch?v=ap2SS0-XPcE)
> *Harsh Kumar · Code along: XGBoost step by step on an imbalanced Kaggle dataset ([notebook](https://github.com/harsh1kumar/learning/blob/master/machine_learning/santander_trxn_prediction/07_trxn_pred_xgboost.ipynb))*

---
### LightGBM Model in Python | Tutorial | Machine Learning
[![LightGBM Model in Python | Tutorial | Machine Learning](https://img.youtube.com/vi/SW3akc0ho7M/0.jpg)](https://www.youtube.com/watch?v=SW3akc0ho7M)
> *Harsh Kumar · Code along: LightGBM on the *same* dataset, for a direct comparison ([notebook](https://github.com/harsh1kumar/learning/blob/master/machine_learning/santander_trxn_prediction/06_trxn_pred_lightgbm.ipynb))*

---
### Catboost Tutorial on Google Colaboratory with free GPU
[![Catboost Tutorial on Google Colaboratory with free GPU](https://img.youtube.com/vi/mUGAA02fGuw/0.jpg)](https://www.youtube.com/watch?v=mUGAA02fGuw)
> *Bhavesh Bhatt · Code along: CatBoost with categorical features ([notebook](https://github.com/bhattbhavesh91/catboost-tutorial))*

---
### Time Series Forecasting with XGBoost - Use python and machine learning to predict energy consumption
[![Time Series Forecasting with XGBoost - Use python and machine learning to predict energy consumption](https://img.youtube.com/vi/vV12dGe_Fho/0.jpg)](https://www.youtube.com/watch?v=vV12dGe_Fho)
> *Rob Mulla · Code along: XGBoost for forecasting, e.g. claim volumes ([Kaggle notebook](https://www.kaggle.com/code/robikscube/time-series-forecasting-with-machine-learning-yt))*

---
### XGBoost in Python from Start to Finish
[![XGBoost in Python from Start to Finish](https://img.youtube.com/vi/GrJP9FLV3FE/0.jpg)](https://www.youtube.com/watch?v=GrJP9FLV3FE)
> *StatQuest with Josh Starmer · Optional, 56 minutes: XGBoost from start to finish, including missing data, imbalance and cross-validated tuning*

---

# Follow-along
**Repos:** [harryallum/Data-Science-Projects](https://github.com/harryallum/Data-Science-Projects/tree/main/Car%20Insurance%20Claim%20Prediction) · [harsh1kumar/learning](https://github.com/harsh1kumar/learning/tree/master/machine_learning/santander_trxn_prediction) · [bhattbhavesh91/catboost-tutorial](https://github.com/bhattbhavesh91/catboost-tutorial) · [dmlc/xgboost demos](https://github.com/dmlc/xgboost/tree/master/demo/guide-python)

1. **Insurance claims model (video 1):** in Colab, run
   ```python
   !git clone https://github.com/harryallum/Data-Science-Projects
   %cd "Data-Science-Projects/Car Insurance Claim Prediction"
   ```
   Open `main.ipynb` and code along with the video. Type the cells yourself rather than running them.
2. **Make it actuarial:** in the same notebook, set `scale_pos_weight = (y_train==0).sum() / (y_train==1).sum()`. Retrain and compare recall and PR-AUC. Then build a severity model on the claimants only, using `new_claim_value` as the target with `objective="reg:gamma"`, and try `reg:tweedie` (`tweedie_variance_power=1.5`) on all rows.
3. **XGBoost vs LightGBM (videos 2–3):** open [`07_trxn_pred_xgboost.ipynb`](https://colab.research.google.com/github/harsh1kumar/learning/blob/master/machine_learning/santander_trxn_prediction/07_trxn_pred_xgboost.ipynb) and [`06_trxn_pred_lightgbm.ipynb`](https://colab.research.google.com/github/harsh1kumar/learning/blob/master/machine_learning/santander_trxn_prediction/06_trxn_pred_lightgbm.ipynb) in Colab. The data is the [Santander Kaggle competition](https://www.kaggle.com/c/santander-customer-transaction-prediction/), which needs a free Kaggle login. Record fit time and AUC for each model.
4. **CatBoost (video 4):** open [`catboost-notebook.ipynb`](https://colab.research.google.com/github/bhattbhavesh91/catboost-tutorial/blob/master/catboost-notebook.ipynb). Then return to the insurance data from step 1 and pass `occupation`, `vehicle_type` and `highest_education` directly as `cat_features=`, without one-hot encoding. Is CatBoost better than XGBoost with one-hot columns?
5. **Missing values and native categoricals:** run [`categorical.py`](https://github.com/dmlc/xgboost/blob/master/demo/guide-python/categorical.py). Then blank out about 10% of one feature in the insurance data (set it to NaN) and refit XGBoost with `enable_categorical=True` and no imputation.
6. **GPU (optional):** refit with `device="cuda"` (XGBoost), `task_type="GPU"` (CatBoost) and `device_type="gpu"` (LightGBM) on a Colab T4, and compare training times.

---
_Last reviewed: 2026-11-06_
