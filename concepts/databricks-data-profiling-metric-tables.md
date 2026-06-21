---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e5112eeac29517a13f332e128d0f43ecda10a79683ee3a4d7fe7fbc908a06086
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profiling-metric-tables
    - DDPMT
    - Data Profiling Metrics Tables
    - Data profiling metric tables|metric tables
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Databricks Data Profiling Metric Tables
description: Two metric tables (profile metrics and drift metrics) created when a data profile runs on a Databricks table, containing summary statistics and distribution-change tracking data.
tags:
  - data-profiling
  - databricks
  - unity-catalog
  - monitoring
timestamp: "2026-06-19T18:08:02.920Z"
---

# Databricks Data Profiling Metric Tables

**Databricks Data Profiling Metric Tables** are system-generated tables that store summary statistics and drift metrics computed by the [Data Profiling](/concepts/data-profiling.md) feature in [Unity Catalog](/concepts/unity-catalog.md). When a profile runs on a Databricks table, it creates or updates two metric tables: a profile metrics table and a drift metrics table. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Overview

The profile metrics table contains summary statistics for each column and for each combination of time window, slice, and grouping columns. For `InferenceLog` analysis, the table also contains model accuracy metrics. ^[data-profiling-metric-tables-databricks-on-aws.md]

The drift metrics table contains statistics that track changes in distribution for a metric. Drift tables can be used to visualize or alert on changes in the data instead of specific values. Two types of drift are computed: ^[data-profiling-metric-tables-databricks-on-aws.md]

- **Consecutive drift** compares a window to the previous time window. Consecutive drift is only calculated if a consecutive time window exists after aggregation according to the specified granularities.
- **Baseline drift** compares a window to the baseline distribution determined by the baseline table. Baseline drift is only calculated if a baseline table is provided.

## Location

Metric tables are saved to the following paths: ^[data-profiling-metric-tables-databricks-on-aws.md]

- Profile metrics: `{output_schema}.{table_name}_profile_metrics`
- Drift metrics: `{output_schema}.{table_name}_drift_metrics`

Where `{output_schema}` is the [Catalog and Schema](/concepts/catalog-and-schema.md) specified by `output_schema_name`, and `{table_name}` is the name of the table being profiled.

## How Profile Statistics Are Computed

Each statistic and metric in the metric tables is computed for a specified time interval (called a "window"). The computation method depends on the analysis type: ^[data-profiling-metric-tables-databricks-on-aws.md]

- For `Snapshot` analysis, the time window is a single point in time corresponding to when the metric was refreshed.
- For `TimeSeries` and `InferenceLog` analysis, the time window is based on the granularities specified in `create_monitor` and the values in the `timestamp_col` specified in the `profile_type` argument.

Metrics are always computed for the entire table. If a slicing expression is provided, metrics are also computed for each data slice defined by a value of the expression. For example: ^[data-profiling-metric-tables-databricks-on-aws.md]

```python
slicing_exprs=["col_1", "col_2 > 10"]
```

This generates slices for `col_2 > 10`, `col_2 <= 10`, and one for each unique value in `col1`. Slices are identified in the metrics tables by the column names `slice_key` and `slice_value`. The entire table is equivalent to `slice_key` = NULL and `slice_value` = NULL. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Additional Statistics for Model Accuracy (InferenceLog Only)

For `InferenceLog` analysis, additional statistics are calculated: ^[data-profiling-metric-tables-databricks-on-aws.md]

- Model quality is calculated if both `label_col` and `prediction_col` are provided.
- Slices are automatically created based on the distinct values of `model_id_col`.
- For classification models, fairness and bias statistics are calculated for slices that have a Boolean value.

## Querying Metric Tables

You can query the metrics tables directly using SQL. The following example is based on `InferenceLog` analysis: ^[data-profiling-metric-tables-databricks-on-aws.md]

```sql
SELECT window.start, column_name, count, num_nulls, distinct_count, frequent_items
FROM census_monitor_db.adult_census_profile_metrics
WHERE model_id = 1
  AND slice_key IS NULL
  AND column_name = "income_predicted"
ORDER BY window.start
```

## Column Schemas

For each column in the primary table, the metrics tables contain one row for each combination of grouping columns. The column associated with each row is shown in the column `column_name`. For metrics based on more than one column (such as model accuracy metrics), `column_name` is set to `:table`. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Profile Metrics Table Grouping Columns

- Time window
- Granularity (`TimeSeries` and `InferenceLog` analysis only)
- Log type (input table or baseline table)
- Slice key and value
- Model ID (`InferenceLog` analysis only)

### Drift Metrics Table Additional Grouping Columns

- Comparison time window
- Drift type (comparison to previous window or comparison to baseline table)

### Profile Metrics Table Schema

The profile metrics table includes the following columns (where a metric is not applicable to a row, the corresponding cell is null): ^[data-profiling-metric-tables-databricks-on-aws.md]

| Column | Type | Description |
|--------|------|-------------|
| `window` | struct | Time window for the metric |
| `granularity` | string | Aggregation granularity |
| `log_type` | string | Input or baseline table |
| `slice_key` | string | Slice expression key |
| `slice_value` | string | Slice expression value |
| `model_id` | string | Model identifier (InferenceLog only) |
| `column_name` | string | Name of the column |
| `count` | long | Number of non-null values |
| `num_nulls` | long | Number of null values |
| `distinct_count` | long | Number of distinct values |
| `frequent_items` | array | Most frequent values |
| `quantiles` | array | Quantile values |
| `mean` | double | Mean value |
| `stddev` | double | Standard deviation |
| `min` | double | Minimum value |
| `max` | double | Maximum value |
| `version` | long | Profile version used for calculation |

**Notes:** ^[data-profiling-metric-tables-databricks-on-aws.md]

- For time series or inference profiles, the profile looks back 30 days from the time the profile is created. Due to this cutoff, the first analysis might include a partial window.
- The version shown is the version used to calculate the statistics and might not be the current version of the profile.
- Sample code to retrieve the 50th percentile: `SELECT element_at(quantiles, int((size(quantiles)+1)/2)) AS p50 ...` or `SELECT quantiles[500] ...`.

### Drift Metrics Table Schema

The drift table is only generated if a baseline table is provided, or if a consecutive time window exists after aggregation according to the specified granularities. ^[data-profiling-metric-tables-databricks-on-aws.md]

| Column | Type | Description |
|--------|------|-------------|
| `window` | struct | Current time window |
| `comparison_window` | struct | Comparison time window |
| `drift_type` | string | Consecutive or baseline drift |
| `granularity` | string | Aggregation granularity |
| `slice_key` | string | Slice expression key |
| `slice_value` | string | Slice expression value |
| `model_id` | string | Model identifier (InferenceLog only) |
| `column_name` | string | Name of the column |
| `psi` | double | Population Stability Index |
| `version` | long | Profile version used for calculation |

**Note:** The Population Stability Index (PSI) is a numeric value representing how different two distributions are. The range is [0, inf). PSI < 0.1 means no significant population change. PSI < 0.2 indicates moderate population change. PSI >= 0.2 indicates significant population change. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) – The visualization layer for profile metrics
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Broader framework for data quality management
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for Databricks data assets
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md) – Specialized profiling for ML model inference data
- [Fairness and Bias Statistics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) – Additional metrics for classification models
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) – Time boundary affecting first analysis windows

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
