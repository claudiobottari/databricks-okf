---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 298f1909994047b350fa4b093a8e6b3ec6f0d0566c61cbb189f8c0dfe25b8098
  pageDirectory: concepts
  sources:
    - monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - equal-opportunity
  citations:
    - file: monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
title: Equal Opportunity
description: A fairness metric that measures whether a label is predicted equally well for both protected and unprotected groups (true positive rate parity)
tags:
  - machine-learning
  - fairness
  - metrics
timestamp: "2026-06-19T19:46:06.498Z"
---

# Equal Opportunity

**Equal Opportunity** is a fairness metric computed automatically by Databricks data profiling when monitoring a classification model's predictions for bias across groups. It measures whether a label is predicted equally well for both the protected group and the unprotected group. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Context and Use

Equal opportunity is one of four fairness and bias metrics that the profile computes when the analysis type is `InferenceLog` and `problem_type` is `classification`. The metric is defined by the slicing expression used to designate the protected group: the group where the Boolean slice evaluates to `True`. The profile then compares model performance on that group against the group where the slice evaluates to `False`. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

The metric output is a key-value pair with fairness scores computed across all predicted classes in a one‑vs‑all manner. Users can create alerts on this metric — for example, when the equal opportunity score exceeds a threshold — and route the alert to an on‑call person or team for investigation. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Fairness Metrics

The profile automatically computes three additional fairness metrics alongside equal opportunity:

- [Predictive Parity](/concepts/predictive-parity.md) — compares the model’s precision between groups.
- [Predictive Equality](/concepts/predictive-equality.md) — compares false positive rates between groups.
- [Statistical Parity](/concepts/statistical-parity.md) — measures the difference in predicted outcomes between groups.

## References

The concept of equal opportunity in machine learning is drawn from the literature on fairness definitions; see the Wikipedia article on Fairness (machine learning) and the paper *Fairness Definitions Explained* (Verma and Rubin, 2018). ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Concepts

- Classification model
- Protected group
- [Data Profiling](/concepts/data-profiling.md)
- Bias detection
- [Inference log analysis](/concepts/inferencelog-analysis.md)

## Sources

- monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

# Citations

1. [monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md](/references/monitor-fairness-and-bias-for-classification-models-databricks-on-aws-14705c6d.md)
