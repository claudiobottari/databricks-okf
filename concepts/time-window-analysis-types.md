---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aef509f915c4ee5c762f5cd7cd718453ac92be7ce58e8710d0e254785945cf02
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-window-analysis-types
    - TWAT
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Time Window Analysis Types
description: Three analysis modes (Snapshot, TimeSeries, InferenceLog) that determine how time intervals and granularities structure metric computation in data profiling.
tags:
  - data-profiling
  - time-series
  - databricks
timestamp: "2026-06-18T15:01:24.364Z"
---

# Time Window Analysis Types

**Time Window Analysis Types** refer to the three modes of time-based analysis available in [data profiling metric tables](/concepts/profile-metrics-table.md): `Snapshot`, `TimeSeries`, and `InferenceLog`. Each type defines how the analysis partitions the data into time intervals (windows) and how statistics are computed for those intervals.

## Overview

When a data profiling job runs on a Databricks table, it computes summary statistics for each column over a specified time interval called a *window*. The behavior of the window differs depending on the analysis type set in the `profile_type` argument of `create_monitor`. The analysis type also determines whether additional metrics such as model accuracy or fairness statistics are computed. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Snapshot Analysis

In `Snapshot` analysis, the time window is a single point in time corresponding to the moment the metrics are refreshed. There is no concept of granularity or consecutive windows; each refresh produces a complete snapshot of the current data. ^[data-profiling-metric-tables-databricks-on-aws.md]

Characteristics:

- No granularity parameter.
- No drift metrics based on consecutive windows (only baseline drift is possible if a baseline table is provided).
- Statistics reflect the entire table at the time of refresh.

## TimeSeries Analysis

In `TimeSeries` analysis, the time window is based on a granularity (e.g., hour, day, week, month) and the values in the `timestamp_col` specified in the profile definition. The data is aggregated into consecutive, non-overlapping windows according to the granularity. Statistics are computed for each window, and the profile looks back 30 days from the time it is created. ^[data-profiling-metric-tables-databricks-on-aws.md]

Key points:

- **Granularity**: Defines the size of each window (e.g., `1 day`, `1 week`).
- **Consecutive drift**: When two consecutive windows exist, the drift metrics table contains a row comparing each window to the previous one.
- **Baseline drift**: If a baseline table is provided, each window is compared to the baseline distribution.
- **Partial first window**: Because the profile looks back only 30 days, the first (oldest) window may be incomplete if the 30‑day cutoff falls in the middle of that granularity period. ^[data-profiling-metric-tables-databricks-on-aws.md]

## InferenceLog Analysis

`InferenceLog` analysis extends `TimeSeries` analysis with additional capabilities designed for monitoring deployed models. It uses the same time‑window concept (granularity and timestamp column) but also computes model accuracy metrics when both `label_col` and `prediction_col` are provided. ^[data-profiling-metric-tables-databricks-on-aws.md]

Key features:

- All the time‑window behavior of `TimeSeries` (granularity, consecutive drift, baseline drift, 30‑day lookback, partial first window).
- **Model accuracy metrics**: Metrics such as confusion matrix, precision, recall, F1 score, ROC AUC are calculated per window and per model version. These appear in a separate analysis table alongside the profile metrics table. ^[data-profiling-metric-tables-databricks-on-aws.md]
- **Model ID grouping**: Metrics are computed for each distinct `model_id` value (specified via `model_id_col`). This allows comparing performance across model versions over time. ^[data-profiling-metric-tables-databricks-on-aws.md]
- **Fairness and bias statistics**: For classification models, fairness and bias statistics are computed for slices that have a Boolean value. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Drift Computation Across Windows

Drift metrics describe how the distribution of a statistic changes over time. Two types of drift depend on time windows:

- **Consecutive drift**: Compares a window to the immediately preceding window. Only calculated if a consecutive window exists after aggregation according to the specified granularities. ^[data-profiling-metric-tables-databricks-on-aws.md]
- **Baseline drift**: Compares a window to the baseline distribution defined by an external baseline table. Only calculated if a baseline table is provided. ^[data-profiling-metric-tables-databricks-on-aws.md]

Both drift types are available for `TimeSeries` and `InferenceLog` analyses. `Snapshot` analysis supports only baseline drift.

## Related Concepts

- Data Profiling Metric Tables – The output tables containing window‑based statistics and drift metrics.
- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) – A visualization built from the metric tables.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Broader context for profiling and drift monitoring.
- [InferenceLog Profile](/concepts/inferencelog-profile.md) – Profile type for monitoring model inference performance.
- Granularity – Parameter controlling window size in time‑based analysis.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
