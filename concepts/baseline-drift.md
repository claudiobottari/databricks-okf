---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df89fcc2c920b2e51161647258f1ca7359d8c51b8ecb11d13c5ffb7647794311
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - baseline-drift
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Baseline Drift
description: A drift comparison method that compares a data window to a baseline distribution defined by a separate baseline table, used when a static reference distribution exists.
tags:
  - drift-detection
  - baseline
  - data-monitoring
timestamp: "2026-06-18T11:31:38.952Z"
---

# Baseline Drift

**Baseline drift** is a type of drift metric computed by the [Data Profiling](/concepts/data-profiling.md) feature in Unity Catalog. It measures the change in the distribution of a data metric between a current time window and a predefined baseline distribution. This allows data practitioners to detect when the characteristics of their data have shifted away from an established reference, such as a training dataset or an approved historical snapshot. ^[data-profiling-metric-tables-databricks-on-aws.md]

## How Baseline Drift Is Calculated

During a profiling run, metrics are aggregated over time windows (for `TimeSeries` or `InferenceLog` analyses) or at a single point in time (for `Snapshot` analysis). For each metric, the profiling engine computes a baseline drift value by comparing the distribution observed in the current window to the distribution stored in the baseline table. This comparison uses statistical measures such as the [Population Stability Index](/concepts/population-stability-index-psi.md) (PSI). ^[data-profiling-metric-tables-databricks-on-aws.md]

Baseline drift is only calculated **if a baseline table was provided** when the monitor was created. Without a baseline table, only [Consecutive Drift](/concepts/consecutive-drift.md) (which compares a window to the immediately preceding window) is available. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Where Baseline Drift Is Stored

Baseline drift values are written to the **drift metrics table** (`{output_schema}.{table_name}_drift_metrics`). Each row in this table corresponds to a specific combination of time window, column, slice, and model ID (for `InferenceLog` analyses). The `drift_type` column distinguishes between `baseline` and `consecutive` drift. ^[data-profiling-metric-tables-databricks-on-aws.md]

The drift metrics table is generated only if either a baseline table is provided (enabling baseline drift) or a consecutive time window exists after aggregation according to the specified granularities (enabling consecutive drift). ^[data-profiling-metric-tables-databricks-on-aws.md]

## Use Cases

- **Model monitoring in production**: Compare feature distributions in the latest inference batch against the training set distribution to detect feature drift before model accuracy degrades.
- **Data quality pipelines**: Validate that incoming data conforms to an agreed-upon baseline distribution before it is used in reporting or downstream systems.
- **Regulatory compliance**: Demonstrate that data distributions have not shifted outside acceptable bounds since a baseline was established.

## Related Concepts

- [Consecutive Drift](/concepts/consecutive-drift.md) — drift between consecutive time windows, calculated even without a baseline table
- [Drift Metrics Table](/concepts/drift-metrics-table.md) — the system table that stores baseline and consecutive drift values
- [Data Profiling](/concepts/data-profiling.md) — the automated process that computes baseline drift
- [Baseline Table](/concepts/baseline-table.md) — the reference dataset or distribution used for baseline drift comparison
- [Population Stability Index](/concepts/population-stability-index-psi.md) — a common metric used to quantify distributional differences
- [Profile Metrics Table](/concepts/profile-metrics-table.md) — the companion table that stores per-window summary statistics

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
