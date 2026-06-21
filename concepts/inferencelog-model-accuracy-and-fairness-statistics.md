---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f00215910c6287b2c073655ca9dabb265d30195f408d80df3ebe28d6554898a
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inferencelog-model-accuracy-and-fairness-statistics
    - Fairness Statistics and InferenceLog Model Accuracy
    - IMAAFS
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
    - file: "data-profiling-metric-tables-databricks-on-aws.md: lines matching \"confusion_matrix"
    - file: precision
    - file: recall
    - file: f1_score
    - file: and roc_auc_score" in the schema table
title: InferenceLog Model Accuracy and Fairness Statistics
description: Additional statistics computed for InferenceLog analysis including model quality metrics (when label_col and prediction_col are provided), automatic slicing by model_id, and fairness/bias statistics for classification models with Boolean slices.
tags:
  - machine-learning
  - model-monitoring
  - fairness
  - classification
timestamp: "2026-06-19T18:07:54.090Z"
---

# InferenceLog Model Accuracy and Fairness Statistics

**InferenceLog Model Accuracy and Fairness Statistics** are specialized metrics computed during [Data Profiling](/concepts/data-profiling.md) on Databricks when the analysis type is set to `InferenceLog`. These statistics evaluate both the predictive performance of machine learning models and potential biases in their predictions, enabling data teams to monitor model quality over time.

## Overview

When a profile runs with `InferenceLog` analysis type, the system creates a [Profile Metrics Table](/concepts/profile-metrics-table.md) that includes standard column statistics plus additional model accuracy and fairness metrics. Model quality statistics are only calculated if both `label_col` and `prediction_col` are provided in the profile configuration. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Model Accuracy Statistics

Model accuracy metrics are stored in the profile metrics table under the `:table` value in the `column_name` field (since these metrics are based on more than one column). The following accuracy statistics are computed when `label_col` and `prediction_col` are provided:

- **Confusion matrix** – A struct showing counts of true positives, true negatives, false positives, and false negatives.
- **Precision** – The proportion of positive predictions that are correct.
- **Recall** – The proportion of actual positives correctly identified.
- **F1 score** – The harmonic mean of precision and recall.
- **ROC AUC score** – The area under the receiver operating characteristic curve.

^[data-profiling-metric-tables-databricks-on-aws.md: lines matching "confusion_matrix, precision, recall, f1_score, and roc_auc_score" in the schema table]

These statistics are only displayed if the profile has `InferenceLog` analysis type and both `label_col` and `prediction_col` are provided. For classification problems, the ROC AUC score is additionally only shown when `problem_type` is `classification`. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Model Fairness and Bias Statistics

For [InferenceLog Analysis](/concepts/inferencelog-analysis.md), fairness and bias statistics are automatically calculated for classification models. Slices are created based on the distinct values of the `model_id_col`, and fairness statistics are computed for slices that have a Boolean value. ^[data-profiling-metric-tables-databricks-on-aws.md]

These fairness statistics evaluate whether model predictions are biased across different demographic or categorical groups, enabling detection of disparities in prediction outcomes. The specific fairness metrics calculated include:

- [Fairness and bias statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) – Computed for classification model slices with Boolean values, as documented in the Databricks fairness and bias statistics reference. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Data Slicing

For `InferenceLog` analysis, additional slices are automatically created based on the distinct values of `model_id_col`. These slices appear in the metrics tables with `slice_key` and `slice_value` columns, enabling per-model comparisons. ^[data-profiling-metric-tables-databricks-on-aws.md]

Slices are defined with a single slice key. The entire table is represented by `slice_key` = NULL and `slice_value` = NULL in the metrics tables. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Retrieving Statistics

To query model accuracy statistics, you can directly query the profile metrics table. For example, to retrieve accuracy metrics for a specific model version:

```sql
SELECT window.start, column_name, count, num_nulls, distinct_count, frequent_items
FROM census_monitor_db.adult_census_profile_metrics
WHERE model_id = 1
  AND slice_key IS NULL
  AND column_name = "income_predicted"
ORDER BY window.start
```

^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overall framework for computing table statistics on Databricks.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, time window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Tracks changes in distribution over time.
- [Fairness and bias statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) – Detailed reference for fairness metrics on Databricks.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – Profile type for monitoring model predictions and accuracy.
- [Baseline Table](/concepts/baseline-table.md) – Optional reference used to compute baseline drift.
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) – Default time boundary that may cause partial windows in first analysis.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
2. data-profiling-metric-tables-databricks-on-aws.md: lines matching "confusion_matrix
3. precision
4. recall
5. f1_score
6. and roc_auc_score" in the schema table
