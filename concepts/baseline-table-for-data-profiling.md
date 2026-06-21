---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a19689f11ed65a617e0df285564d702ec6fb484a4ddd30e387ac6e9e43eea0d9
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - baseline-table-for-data-profiling
    - BTFDP
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Baseline Table for Data Profiling
description: An optional reference table used in data profiling to measure drift; it should reflect expected data quality, distributions, and match the primary table's schema.
tags:
  - data-quality
  - drift-monitoring
timestamp: "2026-06-18T11:30:24.383Z"
---

# Baseline Table for Data Profiling

A **baseline table** is an optional reference dataset used in [Data Profiling](/concepts/data-profiling.md) to measure drift — the change in values over time — relative to expected data distributions. When you attach a baseline table to a profile, drift metrics are computed by comparing the primary table’s current data to the baseline values, making it easier to detect statistically significant deviations from a known good state. ^[data-profiling-databricks-on-aws.md]

## Overview

The baseline table should contain a dataset that reflects the expected quality of the input data in terms of statistical distributions, individual column distributions, missing values, and other characteristics. It must match the schema of the primary (profiled) table, with one exception: for tables used with [Time Series Profile](/concepts/time-series-profile.md) or [Inference Profile](/concepts/inference-profile.md) analysis, the timestamp column is not required to be present in the baseline. If columns are missing in either the primary table or the baseline table, profiling uses best-effort heuristics to compute the output metrics. ^[data-profiling-databricks-on-aws.md]

## Requirements

- **Schema alignment**: The baseline table must have the same schema as the primary table, except for the timestamp column when using time series or inference profiles. ^[data-profiling-databricks-on-aws.md]
- **Availability**: The baseline table must be a Delta table registered in [Unity Catalog](/concepts/unity-catalog.md). ^[data-profiling-databricks-on-aws.md]
- **Optional**: A baseline is not required; profiling can compute drift metrics only from successive time windows without a reference table. ^[data-profiling-databricks-on-aws.md]

## Choosing a Baseline Table by Profile Type

The choice of baseline table depends on the profile type you are using:

### Snapshot Profiles

For a [Snapshot Profile](/concepts/snapshot-profile.md), the baseline table should contain a snapshot of data whose distribution represents an acceptable quality standard. For example, on grade distribution data, you might set the baseline to a previous class where grades were distributed evenly. ^[data-profiling-databricks-on-aws.md]

### Time Series Profiles

For a time series profile, the baseline table should contain data that represents time windows where data distributions represent an acceptable quality standard. For example, on weather data, you might set the baseline to a week, month, or year where the temperature was close to expected normal temperatures. ^[data-profiling-databricks-on-aws.md]

### Inference Profiles

For an [Inference Profile](/concepts/inference-profile.md) tracking machine learning model performance, a good baseline is the data that was used to train or validate the model. This allows alerts when production data drifts relative to what the model was trained on. The baseline table should contain the same feature columns as the primary table, and must also have the same `model_id_col` that was specified for the primary table’s `InferenceLog` so that data is aggregated consistently. Ideally, the test or validation set used to evaluate the model should be used to ensure comparable model quality metrics. ^[data-profiling-databricks-on-aws.md]

## How the Baseline Table Affects Drift Metrics

When a baseline table is provided, drift metrics in the [Drift Metrics Table](/concepts/drift-metrics-table.md) are computed relative to both the baseline values and successive time windows. Without a baseline, drift is only measured between time windows of the primary table. The inclusion of a baseline gives a fixed reference point that can help identify drift from an expected distribution, even when the time‑windowed comparison shows no self‑drift. ^[data-profiling-databricks-on-aws.md]

## Limitations

- The baseline table must be a Delta table in Unity Catalog. ^[data-profiling-databricks-on-aws.md]
- Schema mismatch beyond the timestamp column may lead to best-effort heuristics rather than exact metric computation. ^[data-profiling-databricks-on-aws.md]
- The baseline table itself is not automatically updated; it reflects the data distribution at the time it was created or last refreshed. ^[data-profiling-databricks-on-aws.md]

## Best Practices

- **Use training data as baseline for inference profiles** to detect data drift relative to the model’s training distribution. ^[data-profiling-databricks-on-aws.md]
- **Periodically evaluate whether the baseline still represents acceptable quality.** Data distributions may naturally evolve over time; refresh the baseline when the expected distribution changes. ^[data-profiling-databricks-on-aws.md]
- **Ensure the baseline is large enough** to provide statistically stable reference values for drift calculations. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The overall framework that includes baseline tables.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) — Stores summary statistics for the primary table.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) — Stores drift metrics computed with or without a baseline.
- [Snapshot Profile](/concepts/snapshot-profile.md) — One‑time or periodic snapshot analysis.
- [Time Series Profile](/concepts/time-series-profile.md) — Continuous monitoring over rolling time windows.
- [Inference Profile](/concepts/inference-profile.md) — Monitoring of ML model inputs, predictions, and performance.

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
