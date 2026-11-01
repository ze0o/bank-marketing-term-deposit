# Bank Marketing: Predicting Term-Deposit Subscription

Capstone project (General Assembly Data Science, Bahrain). A Portuguese bank's phone campaigns reach thousands of clients, but only **11.7%** subscribe to a term deposit. This project builds a model that scores clients **before** they are called, so the bank can call the likeliest subscribers first.

**Status:** stage 4 of 7 of the study phase complete (EDA). Modeling starts after the study phase.

## Problem statement

> Predict, before a call is made, whether a client will subscribe to a term deposit, so the bank can rank its call list and reach most subscribers with far fewer calls.

- **Type:** supervised binary classification
- **Target:** `y` (yes = 1, no = 0)
- **Metrics:** balanced accuracy, recall, precision, F1, ROC-AUC (accuracy alone is misleading: always predicting "no" scores 88.3%)

Full details: [docs/01_problem_statement.md](docs/01_problem_statement.md)

## Dataset

45,211 rows × 17 columns (7 numeric, 10 categorical), no nulls, no duplicates. Missing information is hidden as `unknown` and `pdays = -1`. Source: [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing).

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
| `duration` correlation with target | 0.39, but only known after the call → dropped (leakage) |

Details: [notebooks/02_eda.ipynb](notebooks/02_eda.ipynb)

## Repository structure

```text
bank-marketing-term-deposit/
├── data/
│   ├── bank-full.csv
│   └── README.md
├── docs/
│   └── 01_problem_statement.md
├── notebooks/
│   ├── 01_data_overview.ipynb
│   └── 02_eda.ipynb
├── requirements.txt
└── README.md
```

## Current updates

| Stage | Date | What was added |
| --- | --- | --- |
| 4. EDA | 2026-11-01 | `notebooks/02_eda.ipynb`: target balance, distributions, rates by feature, time order, correlations, leakage check |
| 3. Data overview | 2026-11-01 | `notebooks/01_data_overview.ipynb`: data dictionary, types, hidden missing values, duplicates |
| 2. Problem statement | 2026-11-01 | `docs/01_problem_statement.md`: business problem, audience, objectives, success metrics |
| 1. Project setup | 2026-11-01 | Dataset (`data/bank-full.csv`), README, `requirements.txt`, `.gitignore` |

**Next:** Target & features

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

