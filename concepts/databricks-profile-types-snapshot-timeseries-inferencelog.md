---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d3c250eceac3dd05238fad4f30d34c7698e4a4d997cd8e1d76d4e3fcdd0f70c
  pageDirectory: concepts
  sources:
    - data-profiling-metric-tables-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-profile-types-snapshot-timeseries-inferencelog
    - DPTSTI
    - Profile Types (TimeSeries, Inference)
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
title: "Databricks Profile Types: Snapshot, TimeSeries, InferenceLog"
description: "Three analysis types exist: Snapshot (single point-in-time window), TimeSeries (windows based on timestamp granularities), and InferenceLog (adds model accuracy, fairness, and bias statistics)."
tags:
  - data-profiling
  - analysis-types
  - databricks
timestamp: "2026-06-19T09:45:25.600Z"
---

# Databricks Profile Types: Snapshot, TimeSeries, InferenceLog

**Databricks Profile Types** define how data profiling metrics are computed and aggregated over time. The three supported types — `Snapshot`, `TimeSeries`, and `InferenceLog` — determine the structure of time windows, the availability of drift metrics, and (for `InferenceLog`) the inclusion of model accuracy statistics. All profiles create two metric tables: a profile metrics table and a drift metrics table. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Snapshot

A **Snapshot** profile treats the entire table as a single point in time. The time window corresponds to the moment the metric was last refreshed. No aggregation across multiple time windows occurs, and drift metrics are not computed unless a baseline table is provided (baseline drift only). ^[data-profiling-metric-tables-databricks-on-aws.md]

Snapshot profiles are best suited for static or infrequently updated tables where the goal is to capture a one-time summary of the data distribution. The profile metrics table contains summary statistics for each column, each slice, and each grouping column, but the `granularity` grouping column is not present (it is only used for `TimeSeries` and `InferenceLog`). ^[data-profiling-metric-tables-databricks-on-aws.md]

## TimeSeries

A **TimeSeries** profile divides the data into consecutive time windows based on the granularities specified in `create_monitor` and the `timestamp_col` provided in the profile type configuration. Metrics are computed for each window, allowing trend analysis and change detection over time. ^[data-profiling-metric-tables-databricks-on-aws.md]

Because windows are consecutive, the profile can calculate **consecutive drift** — a comparison of a window to the previous time window — provided a consecutive time window exists after aggregation. **Baseline drift** (comparison to a baseline table) can also be computed if a baseline table is supplied. ^[data-profiling-metric-tables-databricks-on-aws.md]

The first analysis window may be partial: the profile looks back 30 days from creation time, so the first window might span only part of a week or month. This affects only the initial run. ^[data-profiling-metric-tables-databricks-on-aws.md]

TimeSeries profiles are ideal for monitoring data quality over time, detecting drift, and setting alerts on changes in distributions.

## InferenceLog

An **InferenceLog** profile extends the `TimeSeries` profile with additional metrics specific to machine learning inference pipelines. It requires a `timestamp_col` and uses the same windowed granularity as `TimeSeries`. In addition to standard column statistics, the profile metrics table contains model accuracy metrics such as `confusion_matrix`, `precision`, `recall`, `f1_score`, and `roc_auc_score`. ^[data-profiling-metric-tables-databricks-on-aws.md]

Model quality is calculated only if both `label_col` and `prediction_col` are provided. For classification models, fairness and bias statistics are computed for Boolean-valued slices. ^[data-profiling-metric-tables-databricks-on-aws.md]

InferenceLog profiles automatically create slices based on the distinct values of `model_id_col`, and metrics are computed for each model version separately. The `model_id` column appears as an additional grouping column in the profile metrics table. ^[data-profiling-metric-tables-databricks-on-aws.md]

This profile type is purpose-built for monitoring production model performance, drift, and fairness over time.

## Comparison

| Feature | Snapshot | TimeSeries | InferenceLog |
|---------|----------|------------|--------------|
| Time window | Single point (refresh time) | Granularity-based consecutive windows | Granularity-based consecutive windows |
| Granularity grouping | Not present | Present | Present |
| Drift (consecutive) | Not supported | Supported (if consecutive windows exist) | Supported |
| Drift (baseline) | Supported (if baseline table provided) | Supported | Supported |
| Model accuracy metrics | Not included | Not included | Included (if `label_col` and `prediction_col` given) |
| Fairness / bias stats | Not included | Not included | For classification with Boolean slices |
| Model ID grouping | Not present | Not present | Present |

All profile types support slicing expressions for per-segment analysis. Drift metrics tables are generated only when baseline drift or consecutive drift can be computed. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — Overview of monitoring and profiling in Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and metadata layer
- [Drift Detection](/concepts/data-drift-detection.md) — Change and baseline drift
- Model Monitoring — Inference pipeline monitoring
- [Fairness and Bias in ML](/concepts/fairness-and-bias-monitoring-for-classification-models.md) — Statistical fairness metrics

## Sources

- data-profiling-metric-tables-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
