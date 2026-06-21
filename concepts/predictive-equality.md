---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a0c25e933929bacef2a4bc660924fa7f77b61126b99101c6728e41743ca4344
  pageDirectory: concepts
  sources:
    - monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predictive-equality
  citations:
    - file: monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
title: Predictive Equality
description: A fairness metric that compares false positive rates between protected and unprotected groups
tags:
  - machine-learning
  - fairness
  - metrics
timestamp: "2026-06-19T19:46:02.846Z"
---

# Predictive Equality

**Predictive Equality** is a fairness metric used to evaluate whether a classification model performs similarly across different demographic groups by comparing the False Positive Rate between a protected group and an unprotected group. It is one of several fairness metrics automatically computed by [Data Profiling](/concepts/data-profiling.md) when monitoring classification models for bias.

## Definition

Predictive equality is satisfied when the false positive rate (FPR) is approximately equal across groups. A model has predictive equality if the probability of a false positive prediction is the same for both the protected group and the unprotected group. Disparities in this metric may indicate that the model is unfairly flagging one group more often than another. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Computation in Databricks

In Databricks' data profiling, predictive equality is computed automatically when monitoring [Inference Log Analysis](/concepts/inferencelog-analysis.md) with a Classification Model. To enable this metric, you define a Boolean [Slice Expression](/concepts/data-slicing-expressions.md) that identifies the protected group. The slice where the expression evaluates to `True` is the protected group, and the slice where it evaluates to `False` is the unprotected group. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

For example, if you create `slicing_exprs=["age < 25"]`, the profile compares false positive rates between applicants under 25 (the protected group) and applicants 25 or older (the unprotected group). ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Usage Notes

Predictive equality metrics are computed only when the Analysis Type is `InferenceLog` and the Problem Type is `classification`. The fairness scores are reported as key-value pairs in a one-vs-all manner across all predicted classes. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Concepts

- Fairness Metrics — The broader set of fairness measures, including predictive parity, equal opportunity, and statistical parity
- [Predictive Parity](/concepts/predictive-parity.md) — Compares precision between groups
- [Equal Opportunity](/concepts/equal-opportunity.md) — Measures whether a label is predicted equally well for both groups
- [Statistical Parity](/concepts/statistical-parity.md) — Measures the difference in predicted outcomes between groups
- False Positive Rate — The underlying statistic that predictive equality compares
- Classification Model Monitoring — Context for applying fairness metrics in production

## Sources

- monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

# Citations

1. [monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md](/references/monitor-fairness-and-bias-for-classification-models-databricks-on-aws-14705c6d.md)
