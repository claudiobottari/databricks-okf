---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b587f50096c9711f1303e47746d5edfca5a0a9f8ad0bb4b8b58b57350fb41d71
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-profile
    - TSP
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Time Series Profile
description: A data profiling analysis mode that computes metrics over time windows, limited to the last 30 days, useful for tracking data distribution changes across successive time periods.
tags:
  - data-quality
  - time-series
  - databricks
timestamp: "2026-06-18T15:00:52.485Z"
---

# Time Series Profile

**Time Series Profile** is an analysis mode within [Data Profiling](/concepts/data-profiling.md) that computes summary statistics and drift metrics over successive time windows of a table. It is designed for data that has a natural temporal ordering, allowing you to track how data distributions and quality metrics change over time.

## Overview

Time series profiling captures quantitative metrics for each time window you define, enabling you to detect and investigate changes in your data's distribution as they occur. This mode is particularly useful for monitoring data that arrives or changes over time — such as sensor readings, transaction logs, or daily aggregates.

When you detect a change in your table's data distribution, the metric tables created by data profiling can capture and alert you to the change and help you identify the cause. Time series profiling helps answer questions such as:

- What is the 90th percentile of a numerical column, and how has it changed over the last week?
- What is the distribution of values in a categorical column, and how does it differ from yesterday?
- Is there drift between successive time windows of the data?
- What does the statistical distribution of a subset or slice of the data look like over time? ^[data-profiling-databricks-on-aws.md]

## How Time Series Profiling Works

### Primary Table and Timestamp Column

To create a time series profile, you specify a primary table that contains a timestamp column. Data profiling uses this column to partition the data into time windows and compute metrics for each window. ^[data-profiling-databricks-on-aws.md]

### Baseline Table

You can optionally specify a baseline table to use as a reference for measuring drift. For time series profiles, the baseline table should contain data that represents time windows where data distributions represent an acceptable quality standard. For example, on weather data, you might set the baseline to a week, month, or year where the temperature was close to expected normal temperatures.

The baseline table should match the schema of the profiled table, except for the timestamp column. If columns are missing in either the primary table or the baseline table, profiling uses best-effort heuristics to compute the output metrics. ^[data-profiling-databricks-on-aws.md]

### Metric Tables

Time series profiling creates two metric tables:

- **Profile metric table**: Contains summary statistics for each time window, such as null counts, min/max values, percentiles, and distribution characteristics.
- **Drift metrics table**: Contains statistics related to the data's drift over time. If a baseline table is provided, drift is also profiled relative to the baseline values. If no baseline is provided, drift is computed between successive time windows.

Both metric tables are Delta tables stored in a Unity Catalog schema that you specify. ^[data-profiling-databricks-on-aws.md]

### Dashboard

For each profile, Databricks automatically creates a dashboard to visualize the profile results. The dashboard is fully customizable and helps you present time series trends and drift analysis. ^[data-profiling-databricks-on-aws.md]

## When to Use Time Series Profiling

Time series profiling is the recommended choice when:

- Your data has a natural time dimension (e.g., event logs, sensor data, daily aggregates).
- You want to track data quality metrics over time rather than analyzing a single snapshot.
- Your table is larger than 4TB (the maximum size for [Snapshot Profile](/concepts/snapshot-profile.md)).
- You need to detect gradual drift or sudden shifts in data distributions.

For tables where you only need a single-point-in-time analysis, consider using a [Snapshot Profile](/concepts/snapshot-profile.md) instead. ^[data-profiling-databricks-on-aws.md]

## Limitations

- Time series profiles only compute metrics over the last 30 days. If you need to adjust this, contact your Databricks account team. ^[data-profiling-databricks-on-aws.md]
- Profiles created over [Materialized Views](/concepts/materialized-views-in-databricks.md) do not support incremental processing. ^[data-profiling-databricks-on-aws.md]
- Only [Delta Tables](/concepts/delta-lake-table.md) are supported for profiling. Supported table types include managed tables, external tables, views, materialized views, and streaming tables. ^[data-profiling-databricks-on-aws.md]
- Not all regions support data profiling. For regional support, see the column **Data profiling** in the table AI and Machine Learning Features Availability. ^[data-profiling-databricks-on-aws.md]

## Requirements

- Your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) and you must have access to Databricks SQL.
- To enable data profiling, you must have the following privileges:
  - `USE CATALOG` on the catalog and `USE SCHEMA` on the schema containing the table.
  - `SELECT` on the table.
  - `MANAGE` on the catalog, schema, or table. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — Overview of the profiling system
- [Snapshot Profile](/concepts/snapshot-profile.md) — Single-point-in-time analysis mode
- [Inference Profile](/concepts/inference-profile.md) — Profile for ML model inputs and predictions
- Data Profiling Metric Tables — Schema details for profile and drift metrics
- Custom Metrics — Adding user-defined metrics to profiles
- [Profile Alerts](/concepts/profile-alerts.md) — Setting up alerts based on metric thresholds

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
