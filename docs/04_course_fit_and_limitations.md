# 04 · Course Fit and Limitations

## Fit with the course

The course repo covers everything this project needs (supervised ML lessons 05–17). Its lesson 11 lab
already solves this problem on `bank.csv`, a 10% sample of this same file, so this project goes clearly
beyond that lab.

| Area | Lesson 11 lab | This project adds |
| --- | --- | --- |
| Data | bank.csv, about 4,500 rows | bank-full, all 45,211 rows |
| Models | Logistic Regression, KNN | Decision Tree, Random Forest, Gradient Boosting, SVM, Voting / Stacking (14, 15, 17) |
| Preprocessing | StandardScaler and one-hot, by hand | Transforms and bins from lesson 06, inside a Pipeline and ColumnTransformer (13) |
| Tuning | A loop over k for KNN | GridSearchCV or RandomizedSearchCV with cross-validation (13) |
| Imbalance | SMOTENC only | Class weights vs oversampling vs SMOTENC, plus threshold tuning (10, 11) |
| Explaining | Odds ratios | Feature importance, partial dependence and SHAP (16) |
| Business output | A model comparison | A ranked call list: share of subscribers reached by calling the top-scored clients |

Left out because the course does not teach them: Cramér's V and chi-square tests (replaced by
rate-per-category tables), percentile capping (replaced by Yeo-Johnson and binning) and time-based
validation splits (kept only as a limitation).

## Limitations

- **Missing history:** 81.7% of clients have no previous campaign, so the strongest feature (`poutcome`) helps only a minority.
- **Time drift:** the yes rate rises from 3.0% to 47.1% across the file and there is no year column, so results on a random split may look better than on future campaigns.
- **No costs:** without the cost of a call or the value of a deposit, the best threshold cannot be set in money terms; reach-at-top-X% is the stand-in.
- **Old data:** 2008–2010, from one Portuguese bank; patterns may not carry over today.
- **No call content or economic indicators** in this version of the dataset.

## Open questions

- [ ] Confirm the dataset is approved, given that the lesson 11 lab already uses its 10% sample.
- [ ] Keep a `duration` benchmark model to show the leakage effect, or leave it out entirely?
- [ ] Which models go in the final deck? Suggested: Logistic Regression as the readable baseline, Random Forest and Gradient Boosting.
