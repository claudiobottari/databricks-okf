---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4e57bc7319181f965d7566739a4d90024c8ae849dd911c0ae666c038c48744a
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-vs-snapshot-profiling
    - TSVSP
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Time Series vs Snapshot Profiling
description: "Two analysis modes in data profiling: time series profiles compute metrics over rolling time windows (max 30 days) and support incremental processing, while snapshot profiles analyze a single point-in-state of a table (max 4TB)."
tags:
  - data-quality
  - monitoring
  - analysis-modes
timestamp: "2026-06-19T09:44:53.076Z"
---

# Time Series vs Snapshot Profiling

**Time Series Profiling** and **Snapshot Profiling** are two of the three analysis modes offered by [Data Profiling](/concepts/data-profiling.md) in Databricks Unity Catalog (the third being [Inference Profiling](/concepts/inference-profile.md)). They differ in how they compute metrics over time, which baseline table they expect, and the types of questions they answer about a table's data quality and distribution.

## Overview

Data profiling computes summary statistics and drift metrics for a primary table. The profile type determines whether metrics are calculated over sliding time windows (time series) or as a single point-in-time comparison against a static baseline (snapshot). Both modes produce the same two metric tables — the profile metrics table and the drift metrics table — but the interpretation and temporal granularity of the metrics differ. ^[data-profiling-databricks-on-aws.md]

## Time Series Profiling

Time series profiling monitors a table over a sequence of time windows. Metrics are computed for each window, enabling you to track changes in data distribution, null rates, percentiles, and other statistics across successive periods. This mode is ideal for tables that are continuously updated, such as event streams, logs, or inference tables. ^[data-profiling-databricks-on-aws.md]

**Baseline table requirements**: When using a time series profile, the baseline table should contain data that represents time windows where data distributions represent an acceptable quality standard. For example, on weather data, you might set the baseline to a week, month, or year where the temperature was close to expected normal temperatures. ^[data-profiling-databricks-on-aws.md]

**Limitations**: Time series profiles only compute metrics over the last 30 days. If you need a different lookback period, contact your Databricks account team. ^[data-profiling-databricks-on-aws.md]

## Snapshot Profiling

Snapshot profiling evaluates the current state of a table against a single static baseline. Instead of computing metrics over time windows, it compares the entire table's distribution to the baseline distribution. This mode is best suited for tables that are updated infrequently or whose quality you want to verify at a particular point in time. ^[data-profiling-databricks-on-aws.md]

**Baseline table requirements**: The baseline table for a snapshot profile should contain a snapshot of data where the distribution represents an acceptable quality standard. For example, on grade distribution data, one might set the baseline to a previous class where grades were distributed evenly. ^[data-profiling-databricks-on-aws.md]

**Limitations**: Snapshot profiles have a maximum table size of 4 TB. For larger tables, use time series profiles instead. ^[data-profiling-databricks-on-aws.md]

## Key Differences

| Aspect | Time Series Profiling | Snapshot Profiling |
|--------|-----------------------|-------------------|
| Temporal granularity | Metrics per time window | Single comparison |
| Baseline table purpose | Defines expected distributions over time windows | Defines a single acceptable snapshot distribution |
| Table size limit | None (recommended for >4 TB) | 4 TB maximum |
| Metrics calculation frequency | Recurring windows (e.g., daily) | One-shot or on-demand |
| Best for | Streaming data, continuously updated tables | Static or infrequently updated tables |
| Lookback period | Last 30 days (default) | Entire table |

## When to Use Each

- **Time Series Profiling**: Use when your table is continually updated and you need to detect drift, anomalies, or gradual degradation over time (e.g., production monitoring of an ML model's input features). ^[data-profiling-databricks-on-aws.md]
- **Snapshot Profiling**: Use when you have a static or slowly changing table and want to verify it matches a known good state (e.g., a data warehouse load that should match a training set). ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Inference Profiling](/concepts/inference-profile.md) – The third profile type, designed specifically for ML model inference tables.
- Data Profiling Metric Tables – The two Delta tables (profile metrics and drift metrics) produced by both modes.
- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) – The auto-generated visualization for any profile type.
- Custom Metrics – How to add user-defined metrics to a profile.

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
