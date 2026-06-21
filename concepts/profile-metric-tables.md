---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf256d4e25711faf3f2bfa1abbc338defbaaf0039a7f18a6be2a9f6929db0acc
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-metric-tables
    - PMT
    - Profile Metrics
    - Profile Metrics Table Schema
    - Profile metrics
    - Metric Tables
    - Monitor Metric Tables|profile metric tables
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Profile Metric Tables
description: Delta tables automatically created by Databricks data profiling that store summary statistics and drift metrics, queryable via SQL and usable for dashboards and alerts.
tags:
  - databricks
  - data-quality
  - delta-lake
timestamp: "2026-06-19T18:06:52.970Z"
---

# Profile Metric Tables

**Profile metric tables** are the two Delta tables automatically created when you set up [Data Profiling](/concepts/data-profiling.md) on a Unity Catalog table. They store the aggregate summary statistics and drift metrics that profiling computes, enabling you to track data quality, model performance, and distribution changes over time. ^[data-profiling-databricks-on-aws.md]

## Overview

When you attach a profile to a primary table, Databricks generates two metric tables and stores them in a Unity Catalog schema specified during profile creation. Metric values are computed for the entire table, and for the time windows and data subsets (“slices”) you define. For inference profiles, metrics are also computed per model ID. The metric tables are Delta tables, so you can view them in the Databricks UI, query them with Databricks SQL, and use them as sources for dashboards and alerts. ^[data-profiling-databricks-on-aws.md]

## Types of Metric Tables

### Profile Metrics Table

The profile metrics table contains summary statistics for the profiled table, such as null fractions, percentiles, value distributions, and custom metrics. For the full schema, see the Databricks documentation on the [profile metrics table schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output#profile-metrics-table). ^[data-profiling-databricks-on-aws.md]

### Drift Metrics Table

The drift metrics table stores statistics that measure how the data changes over time. If you provide a [Baseline Table](/concepts/baseline-table.md), drift is also computed relative to the baseline values. See the [drift metrics table schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output#drift-metrics-table). ^[data-profiling-databricks-on-aws.md]

## Dashboard

For each profile, Databricks automatically creates a dashboard to help you visualize the results from the metric tables. The dashboard is fully customizable. ^[data-profiling-databricks-on-aws.md]

## Custom Metrics

You can control the time granularity of observations and add custom metrics to define business-specific quality checks. See [Use custom metrics with data profiling](/concepts/custom-metrics-in-data-profiling.md). ^[data-profiling-databricks-on-aws.md]

## Usage

- **Viewing:** Both metric tables appear in the Databricks UI under the Unity Catalog schema you specified. ^[data-profiling-databricks-on-aws.md]
- **Querying:** You can query the tables with Databricks SQL for ad‑hoc analysis or custom reports. ^[data-profiling-databricks-on-aws.md]
- **Alerts:** You can set up [Profile Alerts](/concepts/profile-alerts.md) that trigger when metrics cross defined thresholds. ^[data-profiling-databricks-on-aws.md]

## Limitations

- Only Delta tables that are managed tables, external tables, views, materialized views, or streaming tables are supported for profiling. ^[data-profiling-databricks-on-aws.md]
- Profiles created over materialized views do not support incremental processing; they compute metrics from scratch each time. ^[data-profiling-databricks-on-aws.md]
- Time series and inference profiles only compute metrics over the last 30 days. Contact your Databricks account team if you need a longer window. ^[data-profiling-databricks-on-aws.md]
- Snapshot profiles support a maximum table size of 4 TB. For larger tables, use time series profiles instead. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The monitoring feature that creates the metric tables
- [Profile Alerts](/concepts/profile-alerts.md) – Notifications based on metric table values
- [Baseline Table](/concepts/baseline-table.md) – Reference data used for drift calculations
- Custom metrics – User-defined metrics added to the profile metrics table
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer that stores the metric tables
- [Delta tables](/concepts/delta-lake-table.md) – Storage format for profile metric tables
- Databricks SQL – Query engine for exploring metric tables

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
