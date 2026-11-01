"""Shared data loading, preprocessing and evaluation helpers for the notebooks.

Every notebook imports from here so the train/test split and the
preprocessing are identical across all models.
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, f1_score,
                             precision_score, recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import (FunctionTransformer, OneHotEncoder,
                                   PowerTransformer, StandardScaler)

RANDOM_STATE = 42
BINARY_COLS = ['default', 'housing', 'loan']
NOMINAL_COLS = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']


def load_data(path='../data/bank-full.csv'):
    """Load the data and apply the fixed-rule steps that learn nothing from it.

    - map yes/no columns (and the target) to 1/0
    - drop `duration` (only known after the call -> leakage)
    - add bins chosen from the EDA (fixed cut points, so safe before the split)
    """
    df = pd.read_csv(path)
    for col in BINARY_COLS + ['y']:
        df[col] = df[col].map({'no': 0, 'yes': 1})
    df = df.drop(columns='duration')

    df['age_bin'] = pd.cut(df['age'], [17, 25, 30, 40, 50, 60, 100],
                           labels=['18-25', '26-30', '31-40', '41-50', '51-60', '60+']).astype(str)
    df['previous_bin'] = pd.cut(df['previous'], [-1, 0, 1, 3, 1000],
                                labels=['0', '1', '2-3', '4+']).astype(str)
    df['pdays_bin'] = pd.cut(df['pdays'], [-2, 0, 90, 180, 365, 1000],
                             labels=['never', '1-90', '91-180', '181-365', '365+']).astype(str)
    return df


def split(df, test_size=0.2):
    """Stratified 80/20 split so both sets keep the 11.7% yes rate."""
    X = df.drop(columns='y')
    y = df['y']
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=RANDOM_STATE)


def linear_preprocessor():
    """For Logistic Regression / KNN / SVM: transform, bin, scale and one-hot."""
    return ColumnTransformer([
        ('balance', PowerTransformer(method='yeo-johnson'), ['balance']),
        ('campaign', make_pipeline(FunctionTransformer(np.log1p, feature_names_out='one-to-one'),
                                   StandardScaler()), ['campaign']),
        ('day', StandardScaler(), ['day']),
        ('binary', 'passthrough', BINARY_COLS),
        ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False),
         NOMINAL_COLS + ['age_bin', 'previous_bin', 'pdays_bin']),
    ], verbose_feature_names_out=False)


def tree_preprocessor():
    """For Decision Tree / Random Forest / Gradient Boosting: raw numbers + one-hot.

    Trees split on thresholds, so they need no scaling, transforms or bins.
    """
    return ColumnTransformer([
        ('numeric', 'passthrough', ['age', 'balance', 'day', 'campaign', 'pdays', 'previous']),
        ('binary', 'passthrough', BINARY_COLS),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False), NOMINAL_COLS),
    ], verbose_feature_names_out=False)


def evaluate(name, y_true, y_proba, threshold=0.5):
    """Return the project's metrics for one model as a dict."""
    y_pred = (y_proba >= threshold).astype(int)
    return {
        'model': name,
        'threshold': threshold,
        'accuracy': accuracy_score(y_true, y_pred),
        'balanced_accuracy': balanced_accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, zero_division=0),
        'recall': recall_score(y_true, y_pred),
        'f1': f1_score(y_true, y_pred),
        'roc_auc': roc_auc_score(y_true, y_proba),
    }


def save_result(row, path='../results/metrics.csv'):
    """Append (or replace) one model's metrics in the shared results table."""
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = pd.DataFrame([row])
    if os.path.exists(path):
        old = pd.read_csv(path)
        old = old[old['model'] != row['model']]
        new = pd.concat([old, new], ignore_index=True)
    new.round(4).to_csv(path, index=False)
    return new.round(4)
