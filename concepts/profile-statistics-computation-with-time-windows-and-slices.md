---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d03b1d354e6c6b9f455a21dacefca1b1caed177a4f8c2c253dbd11c7242b369
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-statistics-computation-with-time-windows-and-slices
    - Slices and Profile Statistics Computation with Time Windows
    - PSCWTWAS
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Profile Statistics Computation with Time Windows and Slices
description: Statistics are computed for specified time intervals (windows) and optionally for data slices defined by slicing expressions, with metrics aggregated across all combinations of time windows, slices, and grouping columns.
tags:
  - data-profiling
  - computation-model
  - aggregation
timestamp: "2026-06-19T18:07:21.711Z"
---

# Profile Statistics Computation with Time Windows and Slices

**Profile statistics computation with time windows and slices** refers to the mechanism by which [Data Profiling](/concepts/data-profiling.md) on Databricks calculates summary statistics and drift metrics for each column of a monitored table. The computation groups data by time intervals (windows) and optionally by data subsets (slices), producing one row per combination of window, slice, and column in the resulting metric tables. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Time Windows

How the time window is defined depends on the profile type: ^[data-profiling-metric-tables-databricks-on-aws.md]

- **Snapshot** – The time window is a single point in time corresponding to the moment the profile was refreshed.
- **TimeSeries** – The time window is determined by the granularities specified in `create_monitor` and the `timestamp_col` provided in the `profile_type` argument.
- **InferenceLog** – Same as TimeSeries; windows are formed from the timestamp column and the specified granularities.

For TimeSeries and InferenceLog profiles, the system always looks back **30 days** from the time the profile is created when computing metrics (see [30-Day Lookback Window](/concepts/30-day-lookback-window.md)). This lookback may cause the **first analysis window** to be a partial window—for example, if the granularity is weekly, the 30‑day cutoff could fall in the middle of a week, omitting the remainder of that week. Subsequent refreshes produce complete windows because the lookback boundary moves forward. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Data Slicing

In addition to computing metrics for the entire table, you can provide slicing expressions to compute metrics for subsets of data called **slices**. Slicing expressions are defined in the `slicing_exprs` parameter of `create_monitor`. ^[data-profiling-metric-tables-databricks-on-aws.md]

For example, `slicing_exprs=["col_1", "col_2 > 10"]` generates: ^[data-profiling-metric-tables-databricks-on-aws.md]

- One slice for `col_2 > 10` (values: `true`, `false`).
- One slice for each unique value in `col_1`.

Slices are identified in the metric tables by two columns: `slice_key` (the expression string) and `slice_value` (the evaluated value). The entire table is represented by `slice_key = NULL` and `slice_value = NULL`. Each slice is defined by a **single** slice key—only one expression per slice. ^[data-profiling-metric-tables-databricks-on-aws.md]

Metrics are computed for all possible groups defined by the combination of time windows, slice keys, and slice values. For InferenceLog profiles, metrics are additionally computed per model id. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Additional Statistics for InferenceLog Analysis

For [InferenceLog Analysis](/concepts/inferencelog-analysis.md), additional statistics are computed beyond column-level summaries: ^[data-profiling-metric-tables-databricks-on-aws.md]

- **Model quality** – calculated when both `label_col` and `prediction_col` are provided.
- **Model‑specific slices** – automatically created based on distinct values of `model_id_col`.
- **Fairness and bias statistics** – computed for slices that have a Boolean value when the problem type is classification.

These quality metrics (e.g., confusion matrix, precision, recall, F1, ROC AUC) appear in the profile metrics table with `column_name` set to `:table` because they involve multiple columns. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Querying Metric Tables

The profile metrics table and drift metrics table can be queried directly using SQL. The following example shows filtering by model id, slice, and column: ^[data-profiling-metric-tables-databricks-on-aws.md]

```sql
SELECT window.start, column_name, count, num_nulls, distinct_count, frequent_items
FROM catalog.schema.table_profile_metrics
WHERE model_id = 1
  AND slice_key IS NULL
  AND column_name = "income_predicted"
ORDER BY window.start
```

Each row corresponds to a single column for one combination of grouping columns (time window, granularity, slice, and optionally model id). ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of automated statistics generation on Databricks.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics per column, window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores consecutive and baseline drift statistics.
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) – Default time boundary affecting first analysis windows.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – Profile type for model monitoring with quality metrics.
- [Fairness and Bias Statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) – Specialized metrics for classification slices.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
