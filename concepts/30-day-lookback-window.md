---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd5f7d3d9672cf77b25565973ed026e648f545f0fae6cbe8e7b43a82cc08a992
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - 30-day-lookback-window
    - 3LW
    - 30‑Day Lookback Window
    - lookback_window
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: 30-Day Lookback Window
description: A profiling constraint where for time series or inference profiles, the analysis looks back 30 days from profile creation, potentially causing partial windows in the first analysis.
tags:
  - databricks
  - data-profiling
  - limitations
timestamp: "2026-06-19T14:43:57.264Z"
---

# 30-Day Lookback Window

The **30-Day Lookback Window** is a default time boundary applied during data profiling for Time Series Analysis and [Inference Log Analysis](/concepts/inferencelog-analysis.md) on Databricks. When a profile is created or refreshed, the system computes statistics only from data that falls within the 30 days immediately preceding the profile creation time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Effect on the First Analysis Window

Because the profile looks back exactly 30 days from the current time, the first analysis window may be a partial window. For example, if the profile is created on a Wednesday and the aggregation granularity is weekly, the 30‑day cutoff might fall in the middle of a previous week. In that case, only the portion of the week that lies within the 30‑day limit is included in the calculation; the full week is not used. ^[data-profiling-metric-tables-databricks-on-aws.md]

This partial‑window behavior applies only to the **first** analysis after the profile is created. Subsequent refreshes will have complete windows because the lookback boundary moves forward with the profile creation time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Context and Relevance

The 30‑day lookback window is built into the metric computation logic for both the [Profile Metrics Table](/concepts/profile-metrics-table.md) and the [Drift Metrics Table](/concepts/drift-metrics-table.md) when the profile type is `TimeSeries` or `InferenceLog`. It ensures that statistics are computed over a consistent, rolling historical period, but it introduces the partial‑window edge case for the initial analysis. ^[data-profiling-metric-tables-databricks-on-aws.md]

Users who query metric tables directly should be aware that the first window’s metrics may be based on a shorter time span than the requested granularity. For `Snapshot` analysis, the lookback window does not apply because the time window is a single point in time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, time window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics that track distribution changes over time.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – A profile type for monitoring model predictions and accuracy.
- Time Series Analysis – A profile type for monitoring data over continuous time windows.
- [Data Slicing](/concepts/data-slicing-expressions.md) – Metrics are computed for data slices defined by slicing expressions.
- [Baseline Table](/concepts/baseline-table.md) – An optional reference used to compute baseline drift.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
