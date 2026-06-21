---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad3277ffbb1ce66288c1953dc59c7120532cca55c9238cd2df3d69d2706ddafc
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-window-granularity-in-profiling
    - TWGIP
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Time Window Granularity in Profiling
description: How profiling metrics are computed over configurable time intervals (windows) based on granularities specified in create_monitor, with Snapshot, TimeSeries, and InferenceLog analysis types.
tags:
  - databricks
  - time-series
  - data-profiling
timestamp: "2026-06-19T14:44:04.250Z"
---

## Time Window Granularity in Profiling

**Time Window Granularity in Profiling** refers to the time interval over which [Data Profiling](/concepts/data-profiling.md) metrics and statistics are computed for TimeSeries and InferenceLog analysis types in Databricks monitoring. The granularity determines the temporal aggregation of data before summary statistics, drift metrics, and model accuracy metrics are calculated.^[data-profiling-metric-tables-databricks-on-aws.md]

### Overview

For Snapshot analysis, the time window is a single point in time corresponding to when the metric was refreshed. For TimeSeries and InferenceLog analysis, the time window is based on the granularities specified in `create_monitor` and the values in the `timestamp_col` argument.^[data-profiling-metric-tables-databricks-on-aws.md]

Each statistic and metric in the metric tables is computed for a specified time interval (called a "window"). Metrics are always computed for the entire table. In addition, if a slicing expression is provided, metrics are computed for each data slice defined by a value of the expression.^[data-profiling-metric-tables-databricks-on-aws.md]

### Granularity in Grouping Columns

For profile metrics tables, the time window is one of the grouping columns used. For drift metrics tables, additional grouping columns include the comparison time window and drift type (comparison to previous window or comparison to baseline table).^[data-profiling-metric-tables-databricks-on-aws.md]

The granularity grouping column appears only for TimeSeries and InferenceLog analysis. For drift metrics, the following additional grouping columns are used:

- comparison time window
- drift type (comparison to previous window or comparison to baseline table)

### Interaction with 30-Day Lookback

For time series or [inference profiles](/concepts/inference-profile.md), the profile looks back 30 days from the time the profile is created. Due to this cutoff, the first analysis might include a partial window. For example, the 30-day limit might fall in the middle of a week or month, in which case the full week or month is not included in the calculation. This issue affects only the first window.^[data-profiling-metric-tables-databricks-on-aws.md]

### Drift Types Based on Granularity

The drift metrics table contains statistics that track changes in distribution for a metric based on time windows:

- **Consecutive drift** compares a window to the previous time window. Consecutive drift is only calculated if a consecutive time window exists after aggregation according to the specified granularities.
- **Baseline drift** compares a window to the baseline distribution determined by the baseline table. Baseline drift is only calculated if a baseline table is provided.^[data-profiling-metric-tables-databricks-on-aws.md]

### Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [Drift Metrics](/concepts/drift-metrics.md)
- [Profile metrics](/concepts/profile-metrics-table.md)
- Time series analysis
- [Inference log analysis](/concepts/inferencelog-analysis.md)
- Snapshot analysis
- [Baseline Table](/concepts/baseline-table.md)
- [Slicing expressions](/concepts/data-slicing-expressions.md)

### Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
