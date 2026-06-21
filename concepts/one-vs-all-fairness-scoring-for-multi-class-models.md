---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93ba3a6714e1d439bc9910683bdfa302b5f71ce37cccd7cd2606684bc5d77b97
  pageDirectory: concepts
  sources:
    - monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - one-vs-all-fairness-scoring-for-multi-class-models
    - OFSFMM
  citations:
    - file: monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
title: One-vs-All Fairness Scoring for Multi-Class Models
description: A technique for computing fairness metrics across all predicted classes in a multi-class classification model by treating each class in a one-vs-all manner
tags:
  - machine-learning
  - fairness
  - multi-class-classification
timestamp: "2026-06-19T19:46:10.524Z"
---

# One-vs-All Fairness Scoring for Multi-Class Models

**One-vs-All Fairness Scoring** is the mechanism used by [Data Profiling](/concepts/data-profiling.md) on Databricks to compute fairness and bias metrics for multi-class classification models. When a model predicts more than two classes, each fairness metric is calculated in a *one-vs-all* fashion: for each predicted class, the metric compares model performance between a protected group and an unprotected group, treating that class as the positive outcome against all others. The results are stored as key-value pairs where the key is the class label and the value is the fairness score. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## How Fairness Monitoring Works

To monitor fairness, you define a Boolean slicing expression that identifies a protected group. The group where the expression evaluates to `True` is the protected group (the group you are checking for bias against); the group where it evaluates to `False` is the unprotected group. For example, `slicing_exprs=["age < 25"]` creates a slice with `slice_key = "age < 25"` and compares all rows where `age < 25` is `True` against those where it is `False`. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

These metrics are computed only when the analysis type is `InferenceLog` and the `problem_type` is `classification`. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Fairness and Bias Metrics

The profile automatically computes four standard fairness metrics. Each is computed across all predicted classes using the one-vs-all approach, producing a key-value pair per class.

- **Predictive parity** – Compares the model’s precision (positive predictive value) between the protected and unprotected groups.
- **Predictive equality** – Compares the false positive rate between the groups.
- **Equal opportunity** – Measures whether a label is predicted equally well for both groups (true positive rate parity).
- **Statistical parity** – Measures the difference in predicted outcomes (positive prediction rate) between groups.

For formal definitions, see the Wikipedia article on Fairness (machine learning) and the paper *Fairness Definitions Explained* (Verma and Rubin, 2018). ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Output and Alerting

All fairness metrics share the same data type: fairness scores are stored as key-value pairs with the class label as the key. You can query these metrics from the [Profile Metrics Table](/concepts/profile-metrics-table.md) or set up alerts. For example, a model owner can create an alert that triggers when a fairness metric exceeds a threshold and route that alert to an on-call person or team for investigation. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [Inference Log Analysis](/concepts/inferencelog-analysis.md)
- Classification Models
- Protected Group
- [Slicing Expression](/concepts/data-slicing-expressions.md)
- Fairness (machine learning)

## Sources

- monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

# Citations

1. [monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md](/references/monitor-fairness-and-bias-for-classification-models-databricks-on-aws-14705c6d.md)
