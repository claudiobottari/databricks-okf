---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfdf989c2929af180be21b5b119254781aff9f84230e81b50802505956433584
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-accuracy-metrics-in-inferencelog-profiling
    - MAMIIP
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Model Accuracy Metrics in InferenceLog Profiling
description: For InferenceLog analysis, model quality metrics (confusion_matrix, precision, recall, f1_score, roc_auc_score) are computed when label_col and prediction_col are provided; fairness/bias stats for classification models.
tags:
  - model-evaluation
  - data-profiling
  - inference-log
  - fairness
timestamp: "2026-06-19T09:45:24.161Z"
---

# Model Accuracy Metrics in InferenceLog Profiling

**Model Accuracy Metrics in InferenceLog Profiling** refer to the set of quality and performance statistics automatically computed when a data profile uses the `InferenceLog` analysis type. These metrics evaluate how well a model’s predictions match the actual labels, providing a quantitative assessment of model performance over time and across different data slices.

## Overview

When a profile is created with `InferenceLog` analysis and both a label column (`label_col`) and a prediction column (`prediction_col`) are provided, the profiling system calculates additional model accuracy metrics beyond the standard column-level summary statistics. These metrics are stored in the profile metrics table and are automatically sliced by model ID, allowing performance tracking per model version or deployment. For classification models, fairness and bias statistics are also computed for slices that have a Boolean value. ^[data-profiling-metric-tables-databricks-on-aws.md]

Because model accuracy metrics involve more than one column, they are recorded in the profile metrics table with `column_name` set to `:table`. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Prerequisites

- The profile must be of type `InferenceLog`. ^[data-profiling-metric-tables-databricks-on-aws.md]
- Both `label_col` and `prediction_col` must be specified in the profile configuration. ^[data-profiling-metric-tables-databricks-on-aws.md]
- For classification-specific metrics (e.g. confusion matrix, ROC AUC), `problem_type` must be set to `classification`. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Metrics Computed

The profile metrics table includes the following model accuracy metrics:

| Metric | Description | Condition |
|--------|-------------|-----------|
| `confusion_matrix` | Contingency table of actual vs. predicted labels | Classification only |
| `precision` | Positive predictive value | Classification only |
| `recall` | Sensitivity or true positive rate | Classification only |
| `f1_score` | Harmonic mean of precision and recall | Classification only |
| `roc_auc_score` | Area under the ROC curve | Classification only |
| `log_loss` | Logarithmic loss (cross-entropy) | Classification only |
| `mean_absolute_error` | Mean absolute error | Regression |
| `mean_squared_error` | Mean squared error | Regression |
| `root_mean_squared_error` | Root mean squared error | Regression |
| `r2_score` | Coefficient of determination | Regression |

These metrics appear only when the corresponding conditions are met. For example, `precision`, `recall`, and `f1_score` exist only for classification problems. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Schema Details

In the profile metrics table, model accuracy metrics are stored in a `struct` column. For example, the `confusion_matrix` column is of type `struct` with nested arrays. The exact schema can be found in the [data profiling API reference documentation](https://api-docs.databricks.com/python/data-governance/unity-catalog/data-quality-monitoring/data-profiling/latest/index.html). ^[data-profiling-metric-tables-databricks-on-aws.md]

Each row in the profile metrics table represents a combination of time window, granularity, slice key/value, and model ID. The metrics are computed for the entire table as well as for any defined slices. The drift metrics table, if generated, can track changes in these accuracy metrics over consecutive time windows or against a baseline. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- InferenceLog Profiling – The analysis type that triggers model accuracy calculation.
- Data Profiling Metric Tables – General structure of profile and drift metrics tables.
- Classification Metrics (Precision, Recall, F1, ROC AUC) – Detailed definitions of the classification quality measures.
- Regression Metrics (MAE, MSE, RMSE, R²) – Definitions of the regression quality measures.
- Fairness and Bias Statistics for Classification Models – Additional metrics computed when slices have Boolean values.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
