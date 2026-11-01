# 05 · Results and Recommendations

## Conclusion

A **Gradient Boosting** model, trained without `duration` (so it works *before* a call), ranks clients well enough that
**calling only the top-scored 30% reaches 72% of all subscribers**. Random calling would reach 30%.

## Final model

| Item | Choice |
| --- | --- |
| Model | `GradientBoostingClassifier` (300 trees, depth 4, learning rate 0.05, subsample 0.8) |
| Features | 15 inputs (`duration` dropped for leakage), one-hot for categories, raw numbers |
| Imbalance | No resampling; decision threshold tuned to **0.161** on training out-of-fold predictions |
| Validation | Stratified 80/20 split; hyper-parameters and threshold chosen on training data only; test set used once |

## Model comparison (test set, 9,043 clients)

| Model | Threshold | ROC-AUC | Balanced accuracy | Recall | Precision | F1 |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline (always "no") | 0.50 | 0.500 | 0.500 | 0.000 | 0.000 | 0.000 |
| Logistic Regression (class-weighted) | 0.50 | 0.779 | 0.713 | 0.634 | 0.288 | 0.396 |
| Decision Tree | 0.50 | 0.778 | 0.721 | 0.599 | 0.336 | 0.430 |
| Random Forest (class-weighted) | 0.50 | 0.804 | 0.742 | 0.632 | 0.360 | 0.459 |
| Gradient Boosting | 0.50 | 0.806 | 0.618 | 0.253 | 0.660 | 0.366 |
| **Gradient Boosting, tuned threshold** | **0.161** | **0.806** | **0.732** | **0.556** | **0.443** | **0.493** |

- Gradient Boosting has the best ranking (ROC-AUC 0.806), just ahead of Random Forest (0.804).
- With the tuned threshold it also has the best F1 (0.493): of every 100 clients it flags, about 44 subscribe, vs 12 with random calling.
- Accuracy is left out on purpose: the baseline scores 88.3% while finding no one.

## Business value

| Calls made (highest score first) | Share of all subscribers reached | Yes rate among called clients |
| --- | --- | --- |
| Top 10% | 45.1% | 52.8% |
| Top 20% | 62.4% | 36.5% |
| Top 30% | 71.6% | 27.9% |
| Top 50% | 83.4% | 19.5% |

The top 10% converts at **4.5× the 11.7% average**.

## Imbalance handling

Class weights and random oversampling did not change ROC-AUC; **SMOTENC lowered it** (Gradient Boosting 0.798 → 0.776 in cross-validation).
Balancing only shifts the recall/precision trade-off, which the threshold controls directly and without synthetic rows.

## What drives subscription

| Driver | Evidence |
| --- | --- |
| Previous campaign succeeded | 64.7% subscribe; Logistic Regression odds × 8.8; partial dependence 0.35 vs 0.11 |
| Month of contact | Busy May converts at 6.7%; March, September, October and December at 44–52% (low-volume months) |
| Number of calls | Yes rate falls from 14.6% (1 call) to 3.9% (11+); predicted probability flattens after 5–6 calls |
| Contact channel | "unknown" (an early recording gap) odds × 0.31; cellular scores highest |
| Housing loan | Odds × 0.65 |
| Balance | Predicted probability rises from 0.10 (≤ €0) to about 0.145 (above about €2,500) |
| Age | U-shaped: 18–25 and 60+ subscribe far more than 31–60 |

## Recommendations

1. **Call in model-score order.** Use the score to rank every campaign list; with a fixed budget, the top 30% of the list holds about 72% of the subscribers.
2. **Put past successes first.** Clients who said yes before are the single best group (64.7%).
3. **Cap calls at about 5 per client.** Each extra call lowers the odds, and the model sees almost no gain after 5–6.
4. **Prefer mobile numbers and keep contact details up to date.** Cellular contacts convert best; "unknown" contacts worst.
5. **Spread campaigns over the year.** May, the busiest month, converts worst. Smaller, targeted waves in other months did much better, though part of that effect is better targeting in later campaigns.
6. **Use Logistic Regression to explain, Gradient Boosting to rank.** The odds ratios give the marketing team a clear story; the boosted model gives the best list.

## Limitations

- **Time drift:** rows run from May 2008 to November 2010 (per the UCI description) and the yes rate climbs from 3.0% to 47.1% across the file; a random split may flatter the results for future campaigns.
- **No cost data:** the threshold is F1-optimal, not profit-optimal. With the cost of a call and the value of a deposit, it should be re-chosen in money terms.
- **Missing history:** 81.7% of clients have no previous campaign, so the strongest driver helps only a minority.
- **Old, single-bank data** without economic indicators or call content.

## Next steps

- Re-validate on a later campaign (or the last part of the file) to measure drift.
- Agree costs with the business and pick the threshold that maximises profit.
- Optionally train one model *with* `duration` to show on a slide how much leakage would inflate the scores.
- Build the presentation: problem, data, EDA, models, business value, recommendations, limitations.
