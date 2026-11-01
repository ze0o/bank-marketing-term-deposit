# Bank Marketing: Predicting Term-Deposit Subscription

Capstone project (General Assembly Data Science, Bahrain). A Portuguese bank's phone campaigns reach thousands of clients, but only **11.7%** subscribe to a term deposit. This project builds a model that scores clients **before** they are called, so the bank can call the likeliest subscribers first.

**Status:** stage 11 of 14 complete (Imbalance comparison).

## Problem statement

> Predict, before a call is made, whether a client will subscribe to a term deposit, so the bank can rank its call list and reach most subscribers with far fewer calls.

- **Type:** supervised binary classification
- **Target:** `y` (yes = 1, no = 0)
- **Metrics:** ROC-AUC, balanced accuracy, recall, precision, F1 (accuracy alone is misleading: always predicting "no" scores 88.3%)

Full details: [docs/01_problem_statement.md](docs/01_problem_statement.md)

## Dataset

45,211 rows × 17 columns (7 numeric, 10 categorical), no nulls, no duplicates. Missing information is hidden as `unknown` and `pdays = -1`. Source: [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing). `duration` is dropped because it is only known after the call (leakage).

## Key EDA findings

| Finding | Number |
| --- | --- |
| Clients who subscribed | 11.7% |
| Previous campaign succeeded → subscribe | 64.7% |
| Age 18–25 / 60+ subscribe | 24.0% / 42.3% (vs 9–10% in between) |
| 1 call vs 11+ calls this campaign | 14.6% vs 3.9% |
| May: share of calls / yes rate | 30.4% / 6.7% |
| Never contacted before | 81.7% of clients |
| Yes rate, oldest → newest tenth of the file | 3.0% → 47.1% |

Details: [notebooks/02_eda.ipynb](notebooks/02_eda.ipynb)

## Model results (test set)

| model | threshold | roc auc | balanced accuracy | recall | precision | f1 | accuracy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline (always no) | 0.50 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 | 0.883 |
| Logistic Regression | 0.50 | 0.779 | 0.713 | 0.634 | 0.288 | 0.396 | 0.773 |
| Decision Tree | 0.50 | 0.778 | 0.721 | 0.599 | 0.336 | 0.430 | 0.814 |
| Random Forest | 0.50 | 0.804 | 0.742 | 0.632 | 0.360 | 0.459 | 0.825 |
| Gradient Boosting | 0.50 | 0.806 | 0.618 | 0.253 | 0.660 | 0.366 | 0.897 |

ROC-AUC measures ranking quality and is the main comparison metric; the others depend on the threshold.

## Repository structure

```text
bank-marketing-term-deposit/
├── data/
│   ├── bank-full.csv
│   └── README.md
├── docs/
│   ├── 01_problem_statement.md
│   ├── 02_target_and_features.md
│   ├── 03_preprocessing_plan.md
│   └── 04_course_fit_and_limitations.md
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing_and_baseline.ipynb
│   ├── 04_logistic_regression.ipynb
│   ├── 05_random_forest_gradient_boosting.ipynb
│   └── 06_imbalance_comparison.ipynb
├── results/
│   ├── metrics.csv
│   ├── test_probas.csv
│   ├── lr_odds_ratios.csv
│   ├── best_params.json
│   └── imbalance_cv.csv
├── src/
│   └── prep.py
├── requirements.txt
└── README.md
```

## Current updates

| Stage | Date | What was added |
| --- | --- | --- |
| 11. Imbalance comparison | 2026-11-01 | `notebooks/06_imbalance_comparison.ipynb`: no handling vs class weights vs RandomOverSampler vs SMOTENC |
| 10. Tree models | 2026-11-01 | `notebooks/05_random_forest_gradient_boosting.ipynb`: Decision Tree, Random Forest, Gradient Boosting with tuned hyper-parameters |
| 9. Logistic Regression | 2026-11-01 | `notebooks/04_logistic_regression.ipynb`: class weights, GridSearchCV on C, odds ratios |
| 8. Preprocessing pipeline & baseline | 2026-11-01 | `src/prep.py` (shared split, preprocessors, metrics) and `notebooks/03_preprocessing_and_baseline.ipynb`: DummyClassifier baseline |
| 7. Course fit & limitations | 2026-11-01 | `docs/04_course_fit_and_limitations.md`: scope vs the course, limitations, open questions |
| 6. Preprocessing plan | 2026-11-01 | `docs/03_preprocessing_plan.md`: scaling, transforms, binning, encoding, imbalance handling |
| 5. Target & features | 2026-11-01 | `docs/02_target_and_features.md`: target choice, feature decisions, `duration` leakage |
| 4. EDA | 2026-11-01 | `notebooks/02_eda.ipynb`: target balance, distributions, rates by feature, time order, correlations, leakage check |
| 3. Data overview | 2026-11-01 | `notebooks/01_data_overview.ipynb`: data dictionary, types, hidden missing values, duplicates |
| 2. Problem statement | 2026-11-01 | `docs/01_problem_statement.md`: business problem, audience, objectives, success metrics |
| 1. Project setup | 2026-11-01 | Dataset (`data/bank-full.csv`), README, `requirements.txt`, `.gitignore` |

**Next:** Threshold & business value

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

Run the notebooks in order: 03–08 share the split and preprocessing in `src/prep.py` and write their results to `results/`.

