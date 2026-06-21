---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e339a6ff259a8e779d88c33c2983f508fd97bc9c30008b09bfe6f2a9bb054ec1
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inferencelog-analysis
    - Inference Log Analysis
    - Inference log analysis
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: InferenceLog Analysis
description: A profile analysis type for ML model monitoring that computes model accuracy, fairness, bias statistics, and per-model-id metrics using label and prediction columns.
tags:
  - machine-learning
  - model-monitoring
  - databricks
timestamp: "2026-06-18T15:01:30.749Z"
---

# InferenceLog Analysis

**InferenceLog Analysis** is a type of data profiling in Unity Catalog designed for monitoring machine learning models in production. It analyzes inference logs—records of model predictions over time—to track model quality, data drift, and performance metrics across different model versions and data segments.

## Overview

InferenceLog analysis computes summary statistics and model accuracy metrics for each time window, slice, and model version. When a profile runs on a table configured for InferenceLog analysis, it creates or updates two metric tables: a profile metrics table and a drift metrics table. The profile metrics table contains both standard column statistics and model-specific accuracy metrics. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Time Windows

For InferenceLog analysis, the time window is based on the granularities specified in `create_monitor` and the values in the `timestamp_col` specified in the `profile_type` argument. For time series or inference profiles, the profile looks back 30 days from the time the profile is created. Due to this cutoff, the first analysis might include a partial window (for example, the 30-day limit might fall in the middle of a week or month, in which case the full week or month is not included in the calculation). ^[data-profiling-metric-tables-databricks-on-aws.md]

## Model Quality Metrics

Additional statistics are calculated specifically for InferenceLog analysis:

- **Model quality** is calculated if both `label_col` and `prediction_col` are provided. This includes metrics such as confusion matrices, precision, recall, F1 score, and ROC AUC score.
- **Slices** are automatically created based on the distinct values of `model_id_col`.
- For classification models, fairness and bias statistics are calculated for slices that have a Boolean value. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Grouping Columns

For profile metrics in InferenceLog analysis, the following grouping columns are used:

- Time window
- Granularity
- Log type (input table or baseline table)
- Slice key and value
- Model ID

For drift metrics, the following additional grouping columns are used:

- Comparison time window
- Drift type (comparison to previous window or comparison to baseline table)

^[data-profiling-metric-tables-databricks-on-aws.md]

## Metric Table Location

Metric tables are saved to `{output_schema}.{table_name}_profile_metrics` and `{output_schema}.{table_name}_drift_metrics`, where:

- `{output_schema}` is the [Catalog and Schema](/concepts/catalog-and-schema.md) specified by `output_schema_name`
- `{table_name}` is the name of the table being profiled

^[data-profiling-metric-tables-databricks-on-aws.md]

## Drift Analysis

InferenceLog analysis supports two types of drift computation:

- **Consecutive drift** compares a window to the previous time window. Consecutive drift is only calculated if a consecutive time window exists after aggregation according to the specified granularities.
- **Baseline drift** compares a window to the baseline distribution determined by the baseline table. Baseline drift is only calculated if a baseline table is provided.

Drift tables can be used to visualize or alert on changes in the data distribution instead of specific values. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Example Query

The following example queries the profile metrics table for an InferenceLog analysis:

```sql
SELECT window.start, column_name, count, num_nulls, distinct_count, frequent_items
FROM census_monitor_db.adult_census_profile_metrics
WHERE model_id = 1        -- Constrain to version 1
  AND slice_key IS NULL   -- Look at aggregate metrics over the whole data
  AND column_name = "income_predicted"
ORDER BY window.start
```

^[data-profiling-metric-tables-databricks-on-aws.md]

## Column-Level Details

For each column in the primary table, the metrics tables contain one row for each combination of grouping columns. The column associated with each row is shown in the column `column_name`. For metrics based on more than one column (such as model accuracy metrics), `column_name` is set to `:table`. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Additional Schema Information

The profile metrics table for InferenceLog analysis includes fields for confusion matrix, precision, recall, F1 score, and ROC AUC score (formatted as structs) when both `label_col` and `prediction_col` are provided. The drift metrics table uses the Population Stability Index (PSI) as a numeric value representing how different two distributions are, where PSI < 0.1 means no significant population change, PSI < 0.2 indicates moderate change, and PSI >= 0.2 indicates significant change. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The overall framework for monitoring table statistics
- [Drift Metrics](/concepts/drift-metrics.md) — Tracking distribution changes over time
- Model Monitoring — Production monitoring of model performance
- [Fairness and Bias Statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) — Evaluating model fairness across segments
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores metric tables

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
