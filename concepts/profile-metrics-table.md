---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3dce03db3bcbfbb1e5e54aef4b55a74bc007bc787725ff66420b282ef7266b56
  pageDirectory: concepts
  sources:
    - profile-alerts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-metrics-table
    - PMT
    - Profiling Metrics Table
    - Data profiling metric tables
    - Profile metrics
    - data profiling metric tables
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Profile Metrics Table
description: A table storing data profiling statistics (e.g., fraction of missing values) that can be queried to trigger alerts on data quality changes.
tags:
  - databricks
  - data-quality
  - monitoring
  - unity-catalog
timestamp: "2026-06-19T19:58:16.671Z"
---

```markdown
---
title: Profile Metrics Table
summary: A Databricks metric table containing summary statistics for each column and combination of time window, slice, and grouping columns from data profiling runs.
sources:
  - data-profiling-metric-tables-databricks-on-aws.md
  - profile-alerts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:31:14.290Z"
updatedAt: "2026-06-19T14:43:44.497Z"
tags:
  - databricks
  - data-profiling
  - metrics
aliases:
  - profile-metrics-table
  - PMT
confidence: 0.9
provenanceState: merged
inferredParagraphs: 2
---

# Profile Metrics Table

A **profile metrics table** is a system-generated table created by [[Data Profiling]] in Unity Catalog that stores summary statistics for each column of a monitored table. The table is updated each time a profile run completes, providing a historical record of data quality and distribution metrics over time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Location

When a profile runs on a Databricks table, it creates two metric tables in the output schema specified at profile creation:

| Table | Suffix | Description |
|-------|--------|-------------|
| Profile metrics | `_profile_metrics` | Summary statistics for each column per time window, slice, and grouping combination. |
| Drift metrics | `_drift_metrics` | Statistics tracking changes in distribution between consecutive windows or against a baseline. |

The full path is `{output_schema}.{table_name}_profile_metrics` and `{output_schema}.{table_name}_drift_metrics`, where `{output_schema}` is the [[catalog-and-schema|Catalog and Schema]] provided in the `output_schema_name` parameter and `{table_name}` is the name of the monitored table. ^[data-profiling-metric-tables-databricks-on-aws.md]

## How Statistics Are Computed

Each metric is computed for a defined time interval (a "window"):

- **Snapshot analysis**: The window is a single point in time corresponding to the last refresh.
- **TimeSeries** and **InferenceLog** analysis: The window is determined by the granularities specified in `create_monitor` and the values in the `timestamp_col` argument. ^[data-profiling-metric-tables-databricks-on-aws.md]

Metrics are always calculated for the entire table. If `slicing_exprs` are provided, the same metrics are also computed for each slice (e.g., a slice for `col_1 > 10` and one for `col_1 <= 10`, plus one per unique value in a categorical column). Slices are identified in the tables by the columns `slice_key` and `slice_value`. The entire table is represented by `slice_key = NULL` and `slice_value = NULL`. ^[data-profiling-metric-tables-databricks-on-aws.md]

For **InferenceLog** analysis, additional model-accuracy metrics are calculated if both `label_col` and `prediction_col` are provided. Slices are automatically created for each distinct value of `model_id_col`. For classification models, fairness and bias statistics are computed for Boolean-valued slices. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Querying the Profile Metrics Table

You can query the profile metrics table directly using SQL. For example, to retrieve column statistics for a specific model version:

```sql
SELECT
  window.start,
  column_name,
  count,
  num_nulls,
  distinct_count,
  frequent_items
FROM census_monitor_db.adult_census_profile_metrics
WHERE model_id = 1
  AND slice_key IS NULL
  AND column_name = "income_predicted"
ORDER BY window.start;
```

^[data-profiling-metric-tables-databricks-on-aws.md]

## Schema of the Profile Metrics Table

The profile metrics table contains one row for each combination of:

- Time window (struct with `start` and `end` timestamps)
- Granularity (for TimeSeries/InferenceLog analysis)
- Log type (input table or baseline table)
- Slice key and slice value
- Model ID (InferenceLog analysis only)
- Column name

Where a metric is not applicable to a given row, the cell is null. ^[data-profiling-metric-tables-databricks-on-aws.md]

| Column | Type | Description |
|--------|------|-------------|
| `window` | `STRUCT<start: TIMESTAMP, end: TIMESTAMP>` | The time window for this metric row. |
| `version` | `INT` | Profile version used for this computation (may differ from the current profile version). |
| `column_name` | `STRING` | The column for which statistics are reported. For multi-column metrics (e.g., model accuracy), the value is `:table`. |
| `id` | `STRING` | Hash identifier of the row. |
| `granularity` | `STRING` | Aggregation granularity (e.g., `"1 day"`); only present for TimeSeries/InferenceLog. |
| `model_id` | `STRING` | Model version (InferenceLog only). |
| `slice_key` | `STRING` | Slice expression (e.g., `"col_1 > 10"`). `NULL` for the full table. |
| `slice_value` | `STRING` | Specific slice value, or `"true"`/`"false"` for Boolean expressions. |
| `log_type` | `STRING` | Either `"input"` or `"baseline"`. |
| `count` | `LONG` | Number of non-null values. |
| `num_nulls` | `LONG` | Number of null values. |
| `distinct_count` | `LONG` | Approximate distinct value count. |
| `min` | `DOUBLE` | Minimum value (numeric columns only). |
| `max` | `DOUBLE` | Maximum value (numeric columns only). |
| `mean` | `DOUBLE` | Mean value (numeric columns only). |
| `stddev` | `DOUBLE` | Standard deviation (numeric columns only). |
| `num_zeros` | `LONG` | Number of zero values. |
| `num_negative_vals` | `LONG` | Number of negative values. |
| `num_positive_vals` | `LONG` | Number of positive values. |
| `min_length` | `INT` | Minimum string length (string columns only). |
| `max_length` | `INT` | Maximum string length (string columns only). |
| `mean_length` | `DOUBLE` | Mean string length (string columns only). |
| `approx_percentiles` | `ARRAY<DOUBLE>` | Approximate percentiles (1000 bins). |
| `quantiles` | `ARRAY<DOUBLE>` | Quantiles for 0th, 1st, 5th, 25th, 50th, 75th, 95th, 99th, 100th percentiles. |
| `frequent_items` | `MAP<STRING, DOUBLE>` | Frequent values and their relative frequencies (top 100). |
| `histogram` | `ARRAY<STRUCT<...>>` | Histogram bins (numeric columns only). |

For InferenceLog analysis only, the following additional columns appear: ^[data-profiling-metric-tables-databricks-on-aws.md]

| Column | Type | Description |
|--------|------|-------------|
| `confusion_matrix` | `ARRAY<ARRAY<LONG>>` | Confusion matrix for classification. |
| `precision` | `DOUBLE` | Precision (classification). |
| `recall` | `DOUBLE` | Recall (classification). |
| `f1_score` | `DOUBLE` | F1 score (classification). |
|

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
