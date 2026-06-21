---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c9a4783aad5a46cdf5f8894a4ff1cab8d35ff8489bd78810919847720e9f194f
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - population-stability-index-psi
    - PSI(
    - Population Stability Index
    - Population stability index
    - population stability index
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: Population Stability Index (PSI)
description: "A numeric metric in [0, inf) measuring how different two distributions are: PSI < 0.1 indicates no significant change, < 0.2 moderate change, and >= 0.2 significant population change."
tags:
  - drift-detection
  - statistics
  - monitoring
timestamp: "2026-06-19T18:07:46.577Z"
---

# Population Stability Index (PSI)

The **Population Stability Index (PSI)** is a statistical measure used to quantify the degree of change between two distributions of a variable over time. In the context of [Data Profiling](/concepts/data-profiling.md) and [Drift Metrics](/concepts/drift-metrics.md), PSI helps detect when the underlying characteristics of a dataset have shifted significantly, enabling proactive monitoring of data quality and model performance.

## Overview

PSI measures how different two distributions are from each other, producing a numeric value that indicates the magnitude of distribution drift. The metric is computed for each column in the profiled table and for each combination of time window, slice, and grouping columns. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Interpretation

The PSI value is a non-negative numeric value that falls within the range **[0, ∞)**. Standard thresholds provide guidance for interpretation: ^[data-profiling-metric-tables-databricks-on-aws.md]

| PSI Value | Interpretation |
|-----------|----------------|
| PSI < 0.1 | **No significant population change.** The distributions are highly similar. |
| PSI < 0.2 | **Moderate population change.** A noticeable but potentially acceptable shift. |
| PSI ≥ 0.2 | **Significant population change.** The distributions have shifted substantially, warranting investigation. |

These thresholds help determine when data drift is meaningful enough to require action, such as retraining machine learning models, investigating data pipeline issues, or triggering alerts for [Data Quality Monitoring](/concepts/data-quality-monitoring.md).

## When PSI Is Calculated

PSI is stored in the drift metrics table, which is only generated under specific conditions: ^[data-profiling-metric-tables-databricks-on-aws.md]

- A **baseline table** is provided, enabling baseline drift comparisons.
- A **consecutive time window** exists after aggregation according to the specified granularities, enabling consecutive drift comparisons.

For TimeSeries analysis or InferenceLog analysis, the profile looks back 30 days from the time the profile is created. Due to this cutoff, the first analysis might include a partial window. For example, the 30‑day limit might fall in the middle of a week or month, in which case the full week or month is not included in the calculation. This issue affects only the first window. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Relationship to Drift Metrics

PSI is one of the statistics computed in the drift metrics table. The drift table tracks changes in distribution for a metric, enabling visualization or alerting on changes in the data. The drift metrics table supports two types of drift comparison: ^[data-profiling-metric-tables-databricks-on-aws.md]

- **Consecutive drift** — compares a window to the previous time window. Only calculated if a consecutive time window exists after aggregation according to the specified granularities.
- **Baseline drift** — compares a window to the baseline distribution determined by the baseline table. Only calculated if a baseline table is provided.

## Schema Location

The drift metrics table that contains PSI values is saved to `{output_schema}.{table_name}_drift_metrics`, where `{output_schema}` is the [Catalog and Schema](/concepts/catalog-and-schema.md) specified by `output_schema_name` and `{table_name}` is the name of the table being profiled. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- Data Profiling Metric Tables — The parent tables containing profile and drift metrics
- [Drift Metrics](/concepts/drift-metrics.md) — The category of metrics tracking distributional changes
- [30‑Day Lookback Window](/concepts/30-day-lookback-window.md) — The time constraint that can cause partial windows in the first analysis
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for monitoring data health
- [Baseline Table](/concepts/baseline-table.md) — An optional reference table used to compute baseline drift

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
