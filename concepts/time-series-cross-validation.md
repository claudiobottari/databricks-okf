---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c2576bc76af9ec8203d2bc62b5e6d9e2930aef66c5dfa75f59b32bf2b136f87
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-cross-validation
    - TSC
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Time Series Cross-Validation
description: Chronological splitting method for forecasting data that incrementally extends the training set and validates on subsequent time points.
tags:
  - cross-validation
  - time-series
  - model-evaluation
  - forecasting
timestamp: "2026-06-19T18:05:52.543Z"
---

---
title: Time Series Cross-Validation
summary: A validation technique for forecasting that incrementally extends the training dataset chronologically and validates on subsequent time points to ensure robust evaluation over different time segments.
sources:
  - data-preparation-for-forecasting-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:29:19.929Z"
updatedAt: "2026-06-19T14:41:38.617Z"
tags:
  - forecasting
  - model-evaluation
  - time-series
  - machine-learning
aliases:
  - time-series-cross-validation
  - TSC
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Time Series Cross-Validation

**Time Series Cross-Validation** is a model evaluation technique used specifically for forecasting tasks. Unlike standard [Cross-Validation](/concepts/crossvalidator.md), which partitions data randomly, time series cross-validation respects the chronological order of observations by incrementally extending the training dataset forward in time and validating on subsequent time points. This approach provides a robust evaluation of a model's performance over different segments of time and ensures that the forecasting model is rigorously tested against unseen future data, maintaining the relevance and accuracy of predictions. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Application in AutoML

In AutoML forecasting experiments, time series cross-validation is the default splitting strategy for dividing data into training, validation, and test sets. The number of cross-validation folds depends on characteristics of the input table, including the number of time series present, the presence of covariates (additional features), and the length of the time series. ^[data-preparation-for-forecasting-databricks-on-aws.md]

This technique is used specifically for forecasting tasks; other AutoML problem types (classification, regression) use standard cross-validation methods that do not respect temporal order.

## Data Splits

AutoML splits the data into three sets: training, validation, and test. The time series cross-validation procedure defines how these splits are created and how many folds are used. ^[data-preparation-for-forecasting-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – The broader workflow that applies time series cross-validation.
- [Cross-Validation](/concepts/crossvalidator.md) – The general model evaluation family.
- Training, Validation, and Test Sets – The data splits produced by this method.
- Data Leakage – A pitfall avoided by respecting temporal ordering.
- [Time Series Aggregation](/concepts/time-series-aggregation.md) – How AutoML handles multiple values at the same timestamp.

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
