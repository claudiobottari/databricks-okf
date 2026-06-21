---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea78d31f93019d1514169d5354d4ee523098e0fe6b992b51a43ba640828b292a
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-types-in-databricks-data-profiling
    - PTIDDP
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Profile Types in Databricks Data Profiling
description: Databricks data profiling supports three analysis modes — Snapshot, Timeseries, and InferenceLog — each producing different visualization widgets and selectors on the dashboard.
tags:
  - databricks
  - data-profiling
  - analysis-modes
timestamp: "2026-06-19T18:06:34.460Z"
---

# Profile Types in Databricks Data Profiling

**Profile Types** in Databricks Data Profiling define the kind of statistical analysis performed on a monitored table and determine which metrics are computed, how time windows are handled, and which visualizations appear on the automatically generated dashboard. The three supported profile types are `Snapshot`, `TimeSeries`, and `InferenceLog`. ^[data-profiling-dashboard-databricks-on-aws.md, data-profiling-metric-tables-databricks-on-aws.md]

## Snapshot

A `Snapshot` profile captures a point-in-time view of the table’s data. It computes summary statistics (e.g., null counts, distinct values, min/max) for each column at the moment the profile is created or refreshed. No rolling time window is applied. The dashboard for a `Snapshot` profile shows filters appropriate for a single time point. ^[data-profiling-dashboard-databricks-on-aws.md]

## TimeSeries

A `TimeSeries` profile computes statistics over consecutive, rolling time windows. It is designed for tracking data quality and distribution changes over time. Because it uses a time‑based window, a 30‑day lookback boundary is applied: only data within the 30 days preceding the profile creation time is included. This can cause a partial window for the first analysis if the lookback cutoff falls mid‑window. ^[data-profiling-metric-tables-databricks-on-aws.md]

The dashboard for a `TimeSeries` profile displays different selectors than those for `Snapshot`, allowing users to choose the time range and other time‑related parameters. ^[data-profiling-dashboard-databricks-on-aws.md]

## InferenceLog

An `InferenceLog` profile is used for monitoring model predictions and inference accuracy over time. Like `TimeSeries`, it uses a rolling time window and is subject to the same 30‑day lookback behavior. Metrics are computed for both the [Profile Metrics Table](/concepts/profile-metrics-table.md) and the [Drift Metrics Table](/concepts/drift-metrics-table.md) when the profile type is `InferenceLog`. The dashboard provides selectors tailored to inference monitoring (e.g., model names). ^[data-profiling-dashboard-databricks-on-aws.md, data-profiling-metric-tables-databricks-on-aws.md]

## Effect on the Dashboard

For each profile type, the automatically created dashboard includes a different set of visualizations and interactive filters. The left panel of the dashboard lists the metrics and statistics available. Users can customize the charts, date range, data slices, and model filters (for `InferenceLog`) using the editable widgets at the top of the dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of the profiling system on Databricks.
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) – Time boundary applied to `TimeSeries` and `InferenceLog` profiles.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores computed summary statistics.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics for tracking distribution changes.
- [Data Slicing](/concepts/data-slicing-expressions.md) – Metrics can be computed for subsets defined by slicing expressions.

## Sources

- data-profiling-dashboard-databricks-on-aws.md
- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
2. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
