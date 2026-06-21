---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 39f247201a7cdd00116968d7ad0585f5aa733b817a19114927fecac7ebed8911
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inferencelog-analysis-metrics
    - IAM
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: InferenceLog Analysis Metrics
description: Additional statistics for model monitoring including model quality metrics (when label_col and prediction_col are provided), fairness and bias statistics for classification models, and automatic slicing by model_id.
tags:
  - databricks
  - model-monitoring
  - mlops
timestamp: "2026-06-19T14:44:14.599Z"
---

# InferenceLog Analysis Metrics

**InferenceLog Analysis Metrics** are statistical measures computed by [Data Profiling](/concepts/data-profiling.md) in [Unity Catalog](/concepts/unity-catalog.md) when monitoring the input and output logs of machine learning models. This analysis type tracks model accuracy, data drift, and distribution statistics over time, organized by model version, time windows, and data slices.^[data-profiling-metric-tables-databricks-on-aws.md]

## Overview

When a profile runs on a table that contains model inference logs, Unity Catalog creates two metric tables: a **profile metrics table** and a **drift metrics table**. For `InferenceLog` analysis specifically, the profile metrics table also includes model accuracy metrics in addition to the standard column-level summary statistics.^[data-profiling-metric-tables-databricks-on-aws.md]

The analysis is time-series based: metrics are computed for time windows defined by the granularity specified in `create_monitor` and the values in the `timestamp_col`. The profile looks back 30 days from creation time, which may cause the first window to be partial.^[data-profiling-metric-tables-databricks-on-aws.md]

## Metric Table Locations

Metric tables are saved to:

- Profile metrics: `{output_schema}.{table_name}_profile_metrics`
- Drift metrics: `{output_schema}.{table_name}_drift_metrics`

Where `{output_schema}` is the [Catalog and Schema](/concepts/catalog-and-schema.md) specified by `output_schema_name` and `{table_name}` is the name of the table being profiled.^[data-profiling-metric-tables-databricks-on-aws.md]

## Grouping Columns for InferenceLog Analysis

For `InferenceLog` analysis, the profile metrics table contains one row per combination of the following grouping columns:

- **Time window** – the interval being summarized.
- **Granularity** – the time granularity (e.g., day, week).
- **Log type** – whether the row describes the input table or the baseline table.
- **Slice key and value** – slices defined by `slicing_exprs`; `slice_key = NULL` and `slice_value = NULL` represent the entire table.
- **Model ID** – the distinct values from `model_id_col`; slices are automatically created for each unique model ID.^[data-profiling-metric-tables-databricks-on-aws.md]

The drift metrics table uses the same grouping columns, plus:

- **Comparison time window** – the window being compared.
- **Drift type** – either consecutive drift (compared to previous window) or baseline drift (compared to a baseline table).^[data-profiling-metric-tables-databricks-on-aws.md]

## Model Accuracy Metrics

Model accuracy metrics are included only when both `label_col` and `prediction_col` are provided in the profile configuration. These metrics appear in the profile metrics table with `column_name` set to `:table` (indicating they are derived from multiple columns).^[data-profiling-metric-tables-databricks-on-aws.md]

### Classification Metrics

If the `problem_type` is `classification`, the following metrics are added:

| Metric | Description |
|--------|-------------|
| `confusion_matrix` | Struct containing TP, TN, FP, FN |
| `precision` | Precision score |
| `recall` | Recall score |
| `f1_score` | F1 score |
| `roc_auc_score` | Area under the ROC curve |

These metrics are calculated for each slice and each model ID.^[data-profiling-metric-tables-databricks-on-aws.md]

### Fairness and Bias Statistics

For classification models, fairness and bias statistics are calculated for slices that have a Boolean value (e.g., demographic groups). These statistics help evaluate whether model performance is consistent across subgroups. See [Fairness and Bias Statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) for details.^[data-profiling-metric-tables-databricks-on-aws.md]

## Drift Metrics

The drift metrics table tracks changes in distribution for any metric. Two types of drift are computed:

- **Consecutive drift** – compares a window to the previous time window. Only calculated if a consecutive time window exists after aggregation.
- **Baseline drift** – compares a window to a baseline distribution provided by a baseline table. Only calculated if a baseline table is provided.^[data-profiling-metric-tables-databricks-on-aws.md]

Drift metrics include the [Population Stability Index (PSI)](/concepts/population-stability-index-psi.md) as a numeric value indicating how different two distributions are:

- PSI < 0.1: no significant population change.
- PSI < 0.2: moderate population change.
- PSI >= 0.2: significant population change.^[data-profiling-metric-tables-databricks-on-aws.md]

## Querying Metrics

You can query the metric tables directly using SQL. The following example retrieves profile metrics for a specific model version and slice:

```sql
SELECT
  window.start,
  column_name,
  count,
  num_nulls,
  distinct_count,
  frequent_items
FROM census_monitor_db.adult_census_profile_metrics
WHERE
  model_id = 1
  AND slice_key IS NULL
  AND column_name = "income_predicted"
ORDER BY window.start;
```

^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The broader feature that generates these metrics.
- Model Monitoring – Continuous tracking of model performance using these metrics.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer providing profiling capabilities.
- [Fairness and Bias Statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) – Additional metrics for classification models with Boolean slices.
- [Drift Metrics](/concepts/drift-metrics.md) – Metrics tracking distribution changes over time.
- [Population Stability Index (PSI)](/concepts/population-stability-index-psi.md) – Measure used in drift metrics.
- [Metric Tables](/concepts/profile-metric-tables.md) – The output tables (`profile_metrics` and `drift_metrics`) generated by profiling.
- [Baseline Table](/concepts/baseline-table.md) – Reference table used for baseline drift calculations.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
