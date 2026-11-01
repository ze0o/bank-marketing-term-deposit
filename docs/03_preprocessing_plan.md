# 03 · Preprocessing Plan

Every method below is taught in the course (lesson numbers in the last column).
Three numeric features need taming (`balance`, `campaign`, `previous`), `pdays` needs binning because of
its `-1` code, and every categorical column needs encoding.

| Feature | Treatment | Why | Lesson |
| --- | --- | --- | --- |
| balance | `PowerTransformer` (Yeo-Johnson) | Skew 8.36 with negative values; a log fails on negatives, Yeo-Johnson handles them | 06 |
| campaign | `log1p` with `FunctionTransformer`, or bin with `pd.cut` into 1 / 2–3 / 4–5 / 6–10 / 11+ | Skew 4.90; the yes rate falls steadily across these bins | 05, 06 |
| previous | Bin with `pd.cut` into 0 / 1 / 2–3 / 4+ | Skew 41.85, max 275; the rate jumps at 1 then flattens (9.2%, 21.0%, 23.1%, 25.6%) | 06 |
| pdays | Bin with `pd.cut` into never / 1–90 / 91–180 / 181–365 / 365+ days | `-1` is a code, not a number; contacted clients convert at 35.0%, 27.4%, 17.8% and 29.2% | 06 |
| age | `StandardScaler`; optionally bin into 18–25 / 26–30 / 31–40 / 41–50 / 51–60 / 60+ | The U-shaped effect is missed by linear models unless binned | 06 |
| day | `StandardScaler` | No skew (0.09), no outliers | 06 |
| default, housing, loan, y | Map yes / no to 1 / 0, before the split | A fixed rule that learns nothing from the data | 11 lab |
| job, marital, education, contact, month, poutcome | `OneHotEncoder(drop='first', handle_unknown='ignore')`, keeping "unknown" as a level | Nominal categories; education has an order, but its "unknown" level has no place in it | 06 |
| duration | Drop | Leakage (see 02_target_and_features.md) | 07, 11 lab |

## Scaling

`StandardScaler` is needed for Logistic Regression, KNN and SVM, which depend on distances or
coefficient size; `RobustScaler` is the fallback if outliers remain. Decision Tree, Random Forest and
Gradient Boosting do not need scaling. All transformers go in one `ColumnTransformer` inside a `Pipeline`,
so each is fit on the training folds only (lesson 13).

## Imbalance and splitting

- **Stratified** 80/20 train/test split so both sets keep the 11.7% yes rate; tune with `GridSearchCV`
  over `StratifiedKFold`.
- Compare the course's options on the training data only: `class_weight='balanced'`,
  `RandomOverSampler` and `SMOTENC` (before one-hot), wrapped in imblearn's `make_pipeline`.
- Move the decision threshold with `predict_proba` and `precision_recall_curve` instead of the default 0.5.
- Start from a `DummyClassifier` baseline, so every model is compared with "no model".

## Order of operations

1. Map binary yes/no columns to 1/0 and drop `duration`.
2. Stratified train/test split.
3. Build the `ColumnTransformer` (transforms, bins, scaling, one-hot) and put it in a `Pipeline` with the model.
4. Resample (if used) inside the pipeline, so it only touches training folds.
5. Tune with cross-validation on the training set; evaluate once on the untouched test set.
