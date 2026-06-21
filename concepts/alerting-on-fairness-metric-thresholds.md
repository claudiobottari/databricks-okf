---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eaecbbd1e473c957e7afa2fc2261cad41e1a9b41a9f01d7aa45670c49e6dc9e7
  pageDirectory: concepts
  sources:
    - monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alerting-on-fairness-metric-thresholds
    - AOFMT
    - Alert on Fairness Metrics
  citations:
    - file: monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
title: Alerting on Fairness Metric Thresholds
description: The practice of setting up automated alerts when fairness metrics exceed defined thresholds, enabling teams to investigate and remediate bias
tags:
  - machine-learning
  - fairness
  - monitoring
  - alerting
timestamp: "2026-06-19T19:46:14.817Z"
---

### Alerting on Fairness Metric Thresholds

**Alerting on Fairness Metric Thresholds** refers to the capability within Databricks data profiling to automatically notify model owners or on‑call teams when a fairness metric for a classification model crosses a user‑defined boundary. This enables proactive investigation of potential bias toward specific groups.

## Context: Fairness Metrics in Data Profiling

When monitoring a classification model through an [Inference Log Analysis](/concepts/inferencelog-analysis.md) profile with `problem_type = "classification"`, the system computes four fairness metrics for each [Slice Expression](/concepts/data-slicing-expressions.md) that defines a protected group. The slice expression is a Boolean condition (e.g., `age < 25`). The group where the expression evaluates to `True` is the protected group; the group where it evaluates to `False` is the unprotected group. The following metrics are reported in the [Profile Metrics Table](/concepts/profile-metrics-table.md):

- `predictive_parity` – compares precision between groups. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]
- `predictive_equality` – compares false positive rates between groups. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]
- `equal_opportunity` – measures whether a label is predicted equally well for both groups. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]
- `statistical_parity` – measures the difference in predicted outcomes between groups. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

All fairness metrics share the same data type, with scores computed across all predicted classes in a one‑vs‑all manner as key‑value pairs. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Creating Alerts

You can create an alert on any of these fairness metrics. For example, the owner of the model can set up an alert that fires when a fairness metric exceeds a specified threshold and then route that alert to an on‑call person or team for investigation. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

The threshold is user‑configurable; typical values depend on the domain and the acceptable level of disparity. The alert mechanism integrates with Databricks notification channels (email, webhook, etc.) but can be customized per the model owner’s preferences.

## Related Concepts

- Fairness (machine learning)
- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – Profile type used for classification model monitoring.
- [Slice Expression](/concepts/data-slicing-expressions.md) – Boolean expression used to define protected/unprotected groups.
- Protected Group – The group against which bias is assessed.
- [Predictive Parity](/concepts/predictive-parity.md), [Predictive Equality](/concepts/predictive-equality.md), [Equal Opportunity](/concepts/equal-opportunity.md), [Statistical Parity](/concepts/statistical-parity.md) – Individual fairness metrics.
- Classification Model Monitoring – Broader practice of monitoring model performance over time.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores computed metrics including fairness scores.

## Sources

- monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

# Citations

1. [monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md](/references/monitor-fairness-and-bias-for-classification-models-databricks-on-aws-14705c6d.md)
