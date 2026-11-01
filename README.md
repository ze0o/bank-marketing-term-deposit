# Bank Marketing: Predicting Term-Deposit Subscription

Capstone project (General Assembly Data Science, Bahrain). A Portuguese bank's phone campaigns reach thousands of clients, but only **11.7%** subscribe to a term deposit. This project builds a model that scores clients **before** they are called, so the bank can call the likeliest subscribers first.

**Status:** stage 3 of 7 of the study phase complete (Data overview). Modeling starts after the study phase.

## Problem statement

> Predict, before a call is made, whether a client will subscribe to a term deposit, so the bank can rank its call list and reach most subscribers with far fewer calls.

- **Type:** supervised binary classification
- **Target:** `y` (yes = 1, no = 0)
- **Metrics:** balanced accuracy, recall, precision, F1, ROC-AUC (accuracy alone is misleading: always predicting "no" scores 88.3%)

Full details: [docs/01_problem_statement.md](docs/01_problem_statement.md)

## Dataset

45,211 rows × 17 columns (7 numeric, 10 categorical), no nulls, no duplicates. Missing information is hidden as `unknown` and `pdays = -1`. Source: [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing).

## Repository structure

```text
bank-marketing-term-deposit/
├── data/
│   ├── bank-full.csv
│   └── README.md
├── docs/
│   └── 01_problem_statement.md
├── notebooks/
│   └── 01_data_overview.ipynb
├── requirements.txt
└── README.md
```

## Current updates

| Stage | Date | What was added |
| --- | --- | --- |
| 3. Data overview | 2026-11-01 | `notebooks/01_data_overview.ipynb`: data dictionary, types, hidden missing values, duplicates |
| 2. Problem statement | 2026-11-01 | `docs/01_problem_statement.md`: business problem, audience, objectives, success metrics |
| 1. Project setup | 2026-11-01 | Dataset (`data/bank-full.csv`), README, `requirements.txt`, `.gitignore` |

**Next:** EDA

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

