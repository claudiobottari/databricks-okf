---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36cd1c981854034c4e701b18e5fcb0093dd9dfb8c8e28b59ebfa7740ed534abb
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profiling-analysis-modes
    - PAM
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Profiling Analysis Modes
description: "The three types of data profiling analysis in Databricks: time series, inference (for ML models), and snapshot, each suited to different monitoring use cases."
tags:
  - databricks
  - monitoring
  - machine-learning
timestamp: "2026-06-19T18:06:55.155Z"
---

# Profiling Analysis Modes

**Profiling Analysis Modes** are the three modes of statistical analysis that [Data Profiling](/concepts/data-profiling.md) can perform on a table: time series, inference, and snapshot. The mode determines how metrics are computed, how drift is measured, and what kind of input and baseline tables are expected. The choice depends on whether the data has a temporal dimension, whether it contains machine-learning model inputs and predictions, or whether a single point-in-time snapshot is sufficient. ^[data-profiling-databricks-on-aws.md]

## Overview

When you create a profile, you select one of the three analysis modes. The mode influences how the profiling engine computes metrics over time windows and data slices, and what kind of baseline table (if any) is appropriate. All modes produce the same two metric tables — a profile metrics table and a drift metrics table — but the way drift distribution statistics are calculated differs. ^[data-profiling-databricks-on-aws.md]

## Time Series Mode

Time series mode is designed for tables that contain a timestamp column and where you want to track changes in data distributions over successive time windows. Metrics are computed per time window, and drift is measured between consecutive windows or between each window and a baseline. ^[data-profiling-databricks-on-aws.md]

For profiles that use a time series profile, the baseline table (if provided) should contain data that represents time windows where data distributions represent an acceptable quality standard. For example, on weather data, you might set the baseline to a week, month, or year where the temperature was close to expected normal temperatures. ^[data-profiling-databricks-on-aws.md]

## Inference Mode

Inference mode is used to profile the performance of machine learning models by analyzing an [inference table](/concepts/inference-tables.md) that contains the model’s inputs and corresponding predictions. Metrics are computed per model ID, enabling you to track model quality, drift in feature distributions, and performance differences between model versions. ^[data-profiling-databricks-on-aws.md]

For profiles that use an inference profile, a good choice for a baseline is the data that was used to train or validate the model being profiled. In this way, users can be alerted when the data has drifted relative to what the model was trained on. The baseline table should contain the same feature columns as the primary table and additionally should have the same `model_id_col` that was specified for the primary table's InferenceLog so that data is aggregated consistently. Ideally, the test or validation set used to evaluate the model should be used to ensure comparable model quality metrics. ^[data-profiling-databricks-on-aws.md]

## Snapshot Mode

Snapshot mode profiles the table as a single static snapshot — no time dimension is required. Metrics are computed on the entire table at the time of refresh, and drift is measured relative to a baseline table or the previous snapshot. ^[data-profiling-databricks-on-aws.md]

For profiles that use a snapshot profile, the baseline table should contain a snapshot of the data where the distribution represents an acceptable quality standard. For example, on grade distribution data, one might set the baseline to a previous class where grades were distributed evenly. ^[data-profiling-databricks-on-aws.md]

## Baseline Table Considerations by Mode

The choice of baseline table varies by analysis mode:

| Mode | Baseline Table Recommendation |
|------|-------------------------------|
| Time Series | Data representing time windows with acceptable distributions (e.g., a normal weather period) |
| Inference | Training or validation data for the model being profiled |
| Snapshot | A single snapshot that reflects an acceptable quality standard (e.g., a previous well-distributed class) |

The baseline table should match the schema of the profiled table, except for the timestamp column in time series or inference profiles. If columns are missing in either table, profiling uses best-effort heuristics to compute output metrics. ^[data-profiling-databricks-on-aws.md]

## Limitations

- Profiles created using the time series or inference analysis modes only compute metrics over the last 30 days. See [30-Day Lookback Window](/concepts/30-day-lookback-window.md) for details on how the initial analysis window may be partial. If you need to adjust this window, contact your Databricks account team. ^[data-profiling-databricks-on-aws.md]
- The maximum table size for a snapshot profile is 4 TB. For larger tables, use a time series profile instead. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The overarching feature that uses these analysis modes
- Metric tables — The output tables produced by all profiling modes
- [Baseline Table](/concepts/baseline-table.md) — An optional reference table used for drift measurement
- [Inference Tables](/concepts/inference-tables.md) — Tables containing model inputs and predictions for inference mode
- Time series analysis — Broader statistical concept underlying time series mode
- [Drift detection](/concepts/data-drift-detection.md) — How changes in data distributions are identified
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) — Default temporal boundary applied in time series and inference modes

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
