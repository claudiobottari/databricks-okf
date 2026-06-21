---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af8909d2f2608631ff9fe617280dc0eb0a21042833956e181c5bd5b1e729a070
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-window-aggregation-in-data-profiling
    - TWAIDP
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Time Window Aggregation in Data Profiling
description: The mechanism by which Databricks profiling computes metrics over specified time intervals (windows), with Snapshot analysis using single points and TimeSeries/InferenceLog using granularity-based windows.
tags:
  - data-profiling
  - time-series
  - aggregation
timestamp: "2026-06-18T11:32:04.006Z"
---

# Time Window Aggregation in Data Profiling

**Time Window Aggregation** is a core concept in [Databricks Data Profiling](/concepts/databricks-data-profiling.md) that defines how summary statistics and metrics are computed over specific time intervals. Each statistic and metric in the [Profile Metrics Table](/concepts/profile-metrics-table.md) and [Drift Metrics Table](/concepts/drift-metrics-table.md) is computed for a specified time interval (called a "window"), with the aggregation method dependent on the analysis type. ^[data-profiling-metric-tables-databricks-on-aws.md]

## How Time Windows Are Determined

The method for determining time windows varies by analysis type:

- **Snapshot analysis**: The time window is a single point in time corresponding to when the metric was refreshed. No granularity-based windowing is applied. ^[data-profiling-metric-tables-databricks-on-aws.md]
- **TimeSeries and InferenceLog analysis**: The time window is based on the granularities specified in `create_monitor` and the values in the `timestamp_col` specified in the `profile_type` argument. These windows divide the data into discrete intervals for aggregation. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Granularity and Window Calculation

For `TimeSeries` and `InferenceLog` analysis, the profile looks back **30 days** from the time the profile is created. Due to this cutoff, the first analysis window may be **partial** — for example, the 30-day limit might fall in the middle of a week or month, meaning only part of that period is included in the calculation. This issue affects only the first window. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Grouping Columns

The profile metrics table contains one row for each combination of grouping columns per column in the primary table. The column associated with each row is shown in the `column_name` field. For profile metrics, the following grouping columns are used:

- **time window** — The specific time interval for which metrics are computed
- **granularity** — Applies to `TimeSeries` and `InferenceLog` analysis only
- **log type** — Indicates whether the metrics are from the input table or baseline table
- **slice key and value** — Identifies specific data slices (see [Data Slicing in Data Profiling](/concepts/data-slicing-in-databricks-profiling.md))
- **model id** — Applies to `InferenceLog` analysis only

For drift metrics, the following additional grouping columns are used:

- **comparison time window** — The window being compared against
- **drift type** — Indicates whether the comparison is to a previous window or a baseline table

## Drift Metrics and Time Windows

Drift metrics track changes in distribution for a metric. Two types of drift are computed, both of which depend on time windows:

### Consecutive Drift

Compares a window to the **previous time window**. Consecutive drift is only calculated if a consecutive time window exists after aggregation according to the specified granularities. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Baseline Drift

Compares a window to the baseline distribution determined by the **baseline table**. Baseline drift is only calculated if a baseline table is provided. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Slices Across Time Windows

Metrics are computed for all possible groups defined by the time windows and slice keys/values. For `InferenceLog` analysis, metrics are also computed for each model ID. The entire table (no slice) is represented by `slice_key = NULL` and `slice_value = NULL`. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Practical Example

The following query demonstrates how to filter by specific time windows and slices:

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
ORDER BY window.start
```

^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Profile Metrics Table](/concepts/profile-metrics-table.md) — Contains summary statistics organized by time window
- [Drift Metrics Table](/concepts/drift-metrics-table.md) — Tracks distribution changes across time windows
- [Data Slicing in Data Profiling](/concepts/data-slicing-in-databricks-profiling.md) — Divides data into subsets for granular analysis
- [Population Stability Index](/concepts/population-stability-index-psi.md) — A numeric metric representing distribution differences
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md) — Analysis type that uses model IDs and time windows
- TimeSeries Analysis — Analysis type that uses granularity-based windows
- Snapshot Analysis — Analysis type without time-based windowing

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
