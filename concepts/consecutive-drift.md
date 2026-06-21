---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b4ca8c8c02fa32e92dad5e5ccb063a2a3fa372fa6b518a30823516a95d1b598
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - consecutive-drift
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Consecutive Drift
description: A drift comparison method that compares a data window to the immediately previous time window to detect changes over sequential time periods.
tags:
  - drift-detection
  - time-series
  - data-monitoring
timestamp: "2026-06-18T11:31:22.711Z"
---

# Consecutive Drift

**Consecutive Drift** is a type of [data drift](/concepts/data-drift-detection.md) analysis that compares a current time window to the immediately preceding time window to detect changes in data distribution. It is one of two drift types computed by [Data Profiling](/concepts/data-profiling.md) in [Unity Catalog](/concepts/unity-catalog.md), the other being [Baseline Drift](/concepts/baseline-drift.md). ^[data-profiling-metric-tables-databricks-on-aws.md]

## Overview

Data profiling in Databricks automatically calculates consecutive drift when monitoring tables for changes in data characteristics over time. The drift metrics table stores these comparisons, which can be used to visualize or trigger alerts when data distributions shift between consecutive time periods. ^[data-profiling-metric-tables-databricks-on-aws.md]

## How Consecutive Drift Works

Consecutive drift measures the statistical difference between a window's distribution and the distribution from the immediately preceding time window. For example, if monitoring on a weekly basis, consecutive drift would compare this week's data distribution to last week's. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Computation Requirements

Consecutive drift is only calculated when a consecutive time window exists after aggregation according to the specified granularities. If there is no preceding window to compare against (such as at the start of monitoring), no consecutive drift is computed for that initial period. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Supported Analysis Types

Consecutive drift applies to TimeSeries and InferenceLog analysis types. For Snapshot analysis, the time window is a single point in time corresponding to when the metric was refreshed, so consecutive drift is not relevant. ^[data-profiling-metric-tables-databricks-on-aws.md]

### First Window Consideration

For time series or inference profiles, the profile looks back 30 days from the time the profile is created. Due to this cutoff, the first analysis might include a partial window. For example, the 30 day limit might fall in the middle of a week or month, in which case the full week or month is not included in the calculation. This issue affects only the first window. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Storage Location

Drift metrics tables are saved to `{output_schema}.{table_name}_drift_metrics`, where:
- `{output_schema}` is the [Catalog and Schema](/concepts/catalog-and-schema.md) specified by `output_schema_name`
- `{table_name}` is the name of the table being profiled

## Schema

The drift metrics table includes additional grouping columns beyond those in the [Profile Metrics Table](/concepts/profile-metrics-table.md):

- **comparison time window** — identifies which time windows are being compared
- **drift type** — indicates whether the comparison is to the previous window (consecutive) or to a baseline table (baseline)

Where a metric is not applicable to a row, the corresponding cell is null. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- Data Drift — broader concept of changes in data distribution over time
- [Baseline Drift](/concepts/baseline-drift.md) — drift type that compares to a baseline distribution
- [Data Profiling](/concepts/data-profiling.md) — the automated process that computes drift metrics
- [Unity Catalog](/concepts/unity-catalog.md) — the governance layer where data profiling operates
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md) — one of the analysis types that supports consecutive drift
- [Population Stability Index](/concepts/population-stability-index-psi.md) — a metric used to quantify drift magnitude

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
