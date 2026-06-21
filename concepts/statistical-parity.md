---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fad11c2ac1c64983c34da72a6f09def04e5f4ab73c3a4457cccf74d466c8871a
  pageDirectory: concepts
  sources:
    - monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - statistical-parity
  citations:
    - file: monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
title: Statistical Parity
description: A fairness metric that measures the difference in predicted outcomes (selection rates) between protected and unprotected groups
tags:
  - machine-learning
  - fairness
  - metrics
timestamp: "2026-06-19T19:46:11.116Z"
---

# Statistical Parity

**Statistical parity** is a fairness metric that measures the difference in predicted outcomes between a protected group and an unprotected group in a classification model. It is one of several fairness and bias metrics automatically computed by the [Data Profiling](/concepts/data-profiling.md) system when monitoring Classification Models with [Inference Log Analysis](/concepts/inferencelog-analysis.md).^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Definition and Purpose

Statistical parity quantifies whether a classifier assigns positive predictions at equal rates across groups. A value of zero indicates perfect parity (no difference in predicted outcomes), while non‑zero values signal disparity. The metric is computed as part of the fairness analysis that compares model behavior between a protected group (defined by a Boolean [slice expression](/concepts/data-slicing-expressions.md) evaluating to `True`) and an unprotected group (where the same slice evaluates to `False`).^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Applicability

Statistical parity is computed **only** when the profile analysis type is `InferenceLog` and the `problem_type` is `classification`. It does not apply to time‑series or snapshot analyses.^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## How It Is Computed

All fairness and bias metrics, including statistical parity, share the same data structure. Fairness scores are computed across all predicted classes in a **one-vs-all** manner, producing key‑value pairs. The values are stored in the [Profile Metrics Table](/concepts/profile-metrics-table.md) and can be used to trigger alerts when a threshold is exceeded.^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Metrics

In addition to statistical parity, the profiling system automatically computes these related fairness metrics:
- **Predictive parity** – compares precision between groups.
- **Predictive equality** – compares false positive rates.
- **Equal opportunity** – measures whether a label is predicted equally well for both groups.^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## References and Definitions

The implementation follows standard definitions from the fairness literature. For detailed explanations, see the Fairness (machine learning) Wikipedia article and the paper *Fairness Definitions Explained* by Verma and Rubin (2018).^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Concepts

- Fairness and Bias Monitoring
- Protected Group
- Unprotected Group
- [Slice Expression](/concepts/data-slicing-expressions.md)
- [Classification Problem Type](/concepts/data-classification.md)
- [Alert on Fairness Metrics](/concepts/alerting-on-fairness-metric-thresholds.md)

## Sources

- monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

# Citations

1. [monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md](/references/monitor-fairness-and-bias-for-classification-models-databricks-on-aws-14705c6d.md)
