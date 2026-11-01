# 01 · Problem Statement

## Business problem

A Portuguese bank sells **term deposits** through phone campaigns. It calls tens of thousands of clients,
but only about **1 in 9 (11.7%)** subscribes. Every wasted call costs agent time, and repeated calls annoy
clients: some were called up to 63 times in one campaign, and the yes rate falls as calls pile up
(14.6% after 1 call, 3.9% after 11+).

## Problem statement

> **Predict, before a call is made, whether a client will subscribe to a term deposit, so the bank can rank
> its call list and reach most subscribers with far fewer calls.**

Business problem → why it matters → what ML will do:
the bank wastes most of its calls → agent time and client goodwill are lost → a classifier scores each
client so the team calls the likeliest subscribers first and stops early on the rest.

## Type of problem

**Supervised binary classification.** Target: `y` (yes = 1, no = 0).

## Audience

- **Marketing / campaign managers**: decide whom to call and when to stop.
- **Call-centre team leads**: plan agent capacity around a ranked list.
- **Bank management**: lower cost per new deposit.

## Objectives

1. Build a classifier that predicts `y` from the client's profile, past campaign history and contact
   timing, using **only information available before the call**.
2. Beat the naive baseline. Predicting "no" for everyone is already **88.3% accurate but finds zero
   subscribers**, so accuracy alone is misleading.
3. Show business value: what share of all subscribers is reached by calling only the top-scored
   10%, 20% or 30% of clients.
4. Explain the drivers (coefficients / feature importance) and turn them into targeting recommendations,
   such as which segments to prioritise and when to stop calling a client.

## Success metrics

| Metric | Why |
| --- | --- |
| Balanced accuracy | Treats both classes equally despite the 11.7% / 88.3% split |
| Recall (yes class) | Share of real subscribers the model finds |
| Precision (yes class) | Share of called clients who actually subscribe |
| F1 (yes class) | Balance between recall and precision |
| ROC-AUC | How well the model ranks clients, independent of the threshold |
| Confusion matrix | Shows wasted calls (false positives) and missed subscribers (false negatives) |

Every model is compared against a `DummyClassifier` baseline. A concrete success threshold (for example
a minimum recall) will be set after the first baseline model.
