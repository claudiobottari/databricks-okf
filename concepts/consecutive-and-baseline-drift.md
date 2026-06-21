---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b3d01b74a7cccc55e42240536efa8089c89fcc26ab5a8598545930ef423b7e82
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - consecutive-and-baseline-drift
    - Baseline Drift and Consecutive
    - CABD
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Consecutive and Baseline Drift
description: "Two drift comparison methods: consecutive drift compares a window to the previous time window, while baseline drift compares against a user-provided baseline table."
tags:
  - drift-detection
  - data-monitoring
  - databricks
timestamp: "2026-06-18T15:01:27.840Z"
---

# Consecutive and Baseline Drift

**Consecutive and Baseline Drift** are two types of distribution-change metrics computed by [Data Profiling](/concepts/data-profiling.md) in Unity Catalog. They track how data distributions evolve over time, enabling monitoring and alerting on data quality changes.

## Overview

When a profile runs on a Databricks table, it creates or updates two metric tables: a profile metrics table and a drift metrics table. The drift metrics table contains statistics that track changes in distribution for a metric. Drift tables can be used to visualize or alert on changes in the data instead of specific values. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Consecutive Drift

**Consecutive drift** compares a window to the previous time window. It measures how the distribution of a metric has changed from one consecutive time period to the next. Consecutive drift is only calculated if a consecutive time window exists after aggregation according to the specified granularities. ^[data-profiling-metric-tables-databricks-on-aws.md]

For example, if profiles are aggregated weekly, consecutive drift compares this week's distribution to last week's distribution. This type of drift is useful for detecting sudden shifts in data patterns.

## Baseline Drift

**Baseline drift** compares a window to the baseline distribution determined by the baseline table. Baseline drift is only calculated if a baseline table is provided. ^[data-profiling-metric-tables-databricks-on-aws.md]

Baseline drift is useful for detecting long-term drift away from a reference distribution, such as training data or a known good state.

## Drift Metrics Table

The drift metrics table is only generated if a baseline table is provided, or if a consecutive time window exists after aggregation according to the specified granularities. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Schema

The drift metrics table uses the following grouping columns:
- time window
- granularity (for `TimeSeries` and `InferenceLog` analysis only)
- comparison time window
- drift type (comparison to previous window or comparison to baseline table)
- log type - input table or baseline table
- slice key and value
- model id (for `InferenceLog` analysis only)

### Population Stability Index (PSI)

One key metric in the drift table is the [Population Stability Index (PSI)](/concepts/population-stability-index-psi.md), which quantifies how different two distributions are. The PSI output is a numeric value in the range [0, ∞):
- PSI < 0.1 means no significant population change
- PSI < 0.2 indicates moderate population change
- PSI >= 0.2 indicates significant population change

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The monitoring framework that generates drift metrics
- [Profile Metrics Table](/concepts/profile-metrics-table.md) — Contains summary statistics for each column
- [Drift Metrics Table](/concepts/drift-metrics-table.md) — Contains drift-specific statistics
- [Population Stability Index (PSI)](/concepts/population-stability-index-psi.md) — A key drift measurement metric
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md) — Analysis type that includes model accuracy and fairness metrics
- TimeSeries Analysis — Analysis type that uses time-based windows

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
