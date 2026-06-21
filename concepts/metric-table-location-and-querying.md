---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 916d29721cc9a56ceee29c3ddf9f9646d0ac0e8a5e2f4fed9bf9dc571b0eae3f
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metric-table-location-and-querying
    - Querying and Metric Table Location
    - MTLAQ
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Metric Table Location and Querying
description: Convention for naming and locating profile and drift metric tables using output schema and table name, along with direct SQL querying patterns.
tags:
  - data-profiling
  - databricks
  - sql
timestamp: "2026-06-18T15:01:37.236Z"
---

# Metric Table Location and Querying

**Metric Table Location and Querying** describes where [Data Profiling](/concepts/data-profiling.md) metric tables are stored in [Unity Catalog](/concepts/unity-catalog.md) and how to query them directly using SQL. When a profile runs on a Databricks table, it creates or updates two metric tables: a profile metrics table and a drift metrics table. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Metric Table Location

Metric tables are saved to the following paths in Unity Catalog:

- **Profile metrics table:** `{output_schema}.{table_name}_profile_metrics`
- **Drift metrics table:** `{output_schema}.{table_name}_drift_metrics`

Where:
- `{output_schema}` is the [Catalog and Schema](/concepts/catalog-and-schema.md) specified by `output_schema_name` when creating the monitor.
- `{table_name}` is the name of the table being profiled. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Profile Metrics Table

The profile metrics table contains summary statistics for each column and for each combination of time window, slice, and grouping columns. For `InferenceLog` analysis, the analysis table also contains model accuracy metrics. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Grouping Columns

For profile metrics, the following grouping columns are used:
- Time window
- Granularity (for `TimeSeries` and `InferenceLog` analysis only)
- Log type (input table or baseline table)
- Slice key and value
- Model ID (for `InferenceLog` analysis only) ^[data-profiling-metric-tables-databricks-on-aws.md]

### Row Structure

For each column in the primary table, the metrics tables contain one row for each combination of grouping columns. The column associated with each row is shown in the `column_name` column. For metrics based on more than one column — such as model accuracy metrics — `column_name` is set to `:table`. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Drift Metrics Table

The drift metrics table contains statistics that track changes in distribution for a metric. Drift tables can be used to visualize or alert on changes in the data instead of specific values. The drift table is only generated if a baseline table is provided, or if a consecutive time window exists after aggregation according to the specified granularities. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Types of Drift

Two types of drift are computed:
- **Consecutive drift:** Compares a window to the previous time window. Only calculated if a consecutive time window exists after aggregation according to the specified granularities.
- **Baseline drift:** Compares a window to the baseline distribution determined by the baseline table. Only calculated if a baseline table is provided. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Additional Grouping Columns

For drift metrics, the following additional grouping columns are used:
- Comparison time window
- Drift type (comparison to previous window or comparison to baseline table) ^[data-profiling-metric-tables-databricks-on-aws.md]

## Querying Metric Tables

You can query the metrics tables directly using SQL. The following example queries the profile metrics table for an `InferenceLog` analysis:

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
  model_id = 1          -- Constrain to version 1
  AND slice_key IS NULL -- Look at aggregate metrics over the whole data
  AND column_name = "income_predicted"
ORDER BY window.start
```

^[data-profiling-metric-tables-databricks-on-aws.md]

## How Profile Statistics Are Computed

Each statistic and metric in the metric tables is computed for a specified time interval (called a "window"). The behavior depends on the analysis type:
- **Snapshot analysis:** The time window is a single point in time corresponding to when the metric was refreshed.
- **TimeSeries and InferenceLog analysis:** The time window is based on the granularities specified in `create_monitor` and the values in the `timestamp_col` specified in the `profile_type` argument. ^[data-profiling-metric-tables-databricks-on-aws.md]

Metrics are always computed for the entire table. If a slicing expression is provided, metrics are also computed for each data slice defined by a value of the expression. Slices are identified in the metrics tables by the column names `slice_key` and `slice_value`. The entire table is equivalent to `slice_key` = NULL and `slice_value` = NULL. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Additional Statistics for Model Accuracy (InferenceLog Only)

For `InferenceLog` analysis, additional statistics are calculated:
- Model quality is calculated if both `label_col` and `prediction_col` are provided.
- Slices are automatically created based on the distinct values of `model_id_col`.
- For classification models, fairness and bias statistics are calculated for slices that have a Boolean value. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) — The dashboard created by a profile
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — Broader framework for monitoring data quality
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) where metric tables are stored
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md) — Profile type that includes model accuracy metrics
- TimeSeries Analysis — Profile type for time-based data analysis
- Snapshot Analysis — Profile type for point-in-time analysis

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
