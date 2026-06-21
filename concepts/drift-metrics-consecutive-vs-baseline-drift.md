---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73648c13a8b6483eeafd12d7c1d314fb971c9332a73b022c4f9dfc10ec07bd4a
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - drift-metrics-consecutive-vs-baseline-drift
    - DMCVBD
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: "Drift Metrics: Consecutive vs Baseline Drift"
description: "Two types of drift computed for monitoring data distribution changes: consecutive drift compares a window to the previous time window, while baseline drift compares a window to a baseline distribution from a baseline table."
tags:
  - data-profiling
  - drift-detection
  - monitoring
timestamp: "2026-06-19T18:07:32.995Z"
---

# Drift Metrics: Consecutive vs Baseline Drift

**Drift metrics** are statistics tracked by [Data Profiling](/concepts/data-profiling.md) that capture changes in the distribution of a metric over time. They are stored in a dedicated drift metrics table and enable visualization and alerting on shifts in data rather than on absolute values. ^[data-profiling-metric-tables-databricks-on-aws.md]

The drift metrics table contains two types of drift, distinguished by the `drift_type` column: **consecutive drift** and **baseline drift**. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Consecutive Drift

**Consecutive drift** compares a time window to the immediately preceding time window. It is computed only when a consecutive time window exists after the data has been aggregated according to the granularities specified in the profile configuration. ^[data-profiling-metric-tables-databricks-on-aws.md]

For example, if the granularity is set to "day", consecutive drift compares each day's metric value to the previous day's value. If the data does not have two consecutive windows (e.g., because the first window is partial or the profile has only just started), consecutive drift is not calculated for that window. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Baseline Drift

**Baseline drift** compares a time window to a baseline distribution defined by an external baseline table. It is computed only if a baseline table has been provided when creating or updating the profile. ^[data-profiling-metric-tables-databricks-on-aws.md]

The baseline table captures a reference distribution (e.g., training data or a historical "golden" dataset). Each profile window is then compared against that fixed baseline to detect significant distributional shifts. ^[data-profiling-metric-tables-databricks-on-aws.md]

## How Drift Metrics Are Stored

Drift metrics are written to a table named `{output_schema}.{table_name}_drift_metrics`, where `{output_schema}` is the [Catalog and Schema](/concepts/catalog-and-schema.md) specified by `output_schema_name` and `{table_name}` is the name of the table being profiled. ^[data-profiling-metric-tables-databricks-on-aws.md]

The drift metrics table includes additional grouping columns beyond those in the profile metrics table: a **comparison time window** and the **drift type** (either `comparison_to_previous_window` or `comparison_to_baseline_table`). ^[data-profiling-metric-tables-databricks-on-aws.md]

The table is generated only if at least one of the following conditions is met: a baseline table is provided, or a consecutive time window exists after aggregation. If neither condition holds, no drift table is produced. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Relation to Profile Metrics

Both types of drift are computed from the summary statistics stored in the [Profile Metrics Table](/concepts/profile-metrics-table.md). For each combination of column, time window, slice, and grouping columns, the drift table records a comparison metric (e.g., population stability index, Jensen-Shannon divergence) indicating how much the distribution has changed. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Common Use Cases

- **Consecutive drift** is useful for real-time or near-real-time monitoring where the most recent data should be compared to the most recent past (e.g., alerting on a sudden drop in feature values).
- **Baseline drift** is used when there is a known "good" reference dataset (e.g., training data) and any significant departure from that reference should trigger investigation.

## Related Concepts

- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores the summary statistics used to compute drift.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – The output table containing drift calculations.
- [Baseline Table](/concepts/baseline-table.md) – The external table that defines the reference distribution for baseline drift.
- [Data Profiling](/concepts/data-profiling.md) – The overall process that generates these metric tables.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Broader framework for monitoring data health.
- [Population Stability Index](/concepts/population-stability-index-psi.md) – A common drift metric used in these comparisons.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
