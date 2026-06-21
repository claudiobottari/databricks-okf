---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f51c83e1107b5d8a2dd557db7fa41320f4239f7d34fcee4dced70a4055768983
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - consecutive-vs-baseline-drift
    - CVBD
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Consecutive vs Baseline Drift
description: "Two types of drift computed in Databricks profiling: consecutive drift compares a window to the previous time window, while baseline drift compares to a baseline distribution from a baseline table."
tags:
  - databricks
  - drift-detection
  - data-quality
timestamp: "2026-06-19T14:43:12.001Z"
---

# Consecutive vs Baseline Drift

**Consecutive drift** and **baseline drift** are two types of distribution-change metrics computed by [Data Profiling](/concepts/data-profiling.md) on Databricks. Both are stored in the drift metrics table and help users detect and monitor shifts in data over time. The key difference lies in what each drift compares against: consecutive drift compares the current time window to the immediately preceding window, while baseline drift compares the current window to a fixed baseline distribution defined by a separate baseline table. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Consecutive Drift

Consecutive drift tracks changes by comparing a given time window to the previous time window. It is only calculated when a consecutive time window exists after aggregation according to the specified granularities (e.g., daily, weekly). If no prior window is available (for instance, after the first aggregation), consecutive drift is not computed for that row. This type of drift is useful for detecting gradual or abrupt changes relative to the most recent period. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Baseline Drift

Baseline drift compares a time window to the baseline distribution defined by a user-provided baseline table. It is only calculated if a baseline table is supplied when configuring the profile. This approach allows users to measure how current data deviates from a reference distribution (e.g., a training dataset or a historical standard), independent of the order of time windows. Baseline drift is particularly valuable for detecting concept drift or data quality degradation against a known good state. ^[data-profiling-metric-tables-databricks-on-aws.md]

## When Each Appears

The drift metrics table is generated only if either condition is met: a baseline table is provided (enabling baseline drift), or a consecutive time window exists after aggregation according to the specified granularities (enabling consecutive drift). If neither condition holds, no drift metrics are produced. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data profiling metric tables](/concepts/profile-metrics-table.md) – The parent tables that store profile and drift metrics.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – The table schema containing consecutive and baseline drift statistics.
- [Baseline Table](/concepts/baseline-table.md) – The user-defined reference distribution used for baseline drift computation.
- [Population stability index](/concepts/population-stability-index-psi.md) – A metric used in drift calculations to quantify distribution differences.
- Time series analysis – A profile type where consecutive drift relies on ordered time windows.
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md) – A profile type that supports both drift types for model monitoring.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
