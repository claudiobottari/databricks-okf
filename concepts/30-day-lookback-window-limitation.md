---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1f70b8a7840f58b787d099c443815d630fe150e3bb3f71736e72a2cfbc31b11
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - 30-day-lookback-window-limitation
    - 3LWL
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: 30-Day Lookback Window Limitation
description: For time series or inference profiles, the profile looks back 30 days from when it is created, which may cause the first analysis to include a partial window (e.g., cutting mid-week or mid-month).
tags:
  - data-profiling
  - limitations
  - time-series
timestamp: "2026-06-19T18:07:30.341Z"
---

# 30-Day Lookback Window Limitation

The **30-Day Lookback Window Limitation** is a property of the data profiling logic on Databricks that restricts the time window used for computing statistics in Time Series Analysis and [Inference Log Analysis](/concepts/inferencelog-analysis.md) profiles. When a profile is created or refreshed, the system computes metrics only from data that falls within the 30 days immediately preceding the profile creation time. This lookback is built into the metric computation for both the [Profile Metrics Table](/concepts/profile-metrics-table.md) and the [Drift Metrics Table](/concepts/drift-metrics-table.md). ^[data-profiling-metric-tables-databricks-on-aws.md]

## Effect on the First Analysis Window

Because the profile looks back exactly 30 days from the time of creation, the first analysis window may be a *partial window*. For example, if the aggregation granularity is weekly and the 30‑day cutoff falls in the middle of a previous week, only the portion of that week that lies within the 30‑day limit is included; the full week is not used. This partial‑window behavior affects **only the first analysis** after the profile is created. Subsequent refreshes will have complete windows because the lookback boundary moves forward with the profile creation time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Context and Applicability

The 30‑day lookback window is applied when the profile type is `TimeSeries` or `InferenceLog`. For `Snapshot` analysis, the lookback does not apply because the time window is a single point in time. Understanding this limitation is important when querying metric tables directly: the metrics for the first window may be based on a shorter time span than the requested granularity. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, time window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics tracking distribution changes over time.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – A profile type for monitoring model predictions.
- Time Series Analysis – A profile type for monitoring data over continuous time windows.
- Snapshot Analysis – A profile type with no lookback window.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
