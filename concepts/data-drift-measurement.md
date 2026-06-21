---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5c14739c4431fcb0e6ef03339eb88c7343e676065a669c87e72ddef195c6dd4
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-drift-measurement
    - DDM
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Data Drift Measurement
description: The process of measuring statistical changes in data distributions over time or relative to a baseline, including drift between successive time windows and between current data and expected values.
tags:
  - data-quality
  - drift-detection
  - databricks
timestamp: "2026-06-18T15:00:56.982Z"
---

# Data Drift Measurement

**Data Drift Measurement** refers to the quantitative assessment of how a dataset's statistical properties change over time relative to a known baseline or between successive time windows. It is a core capability of [Data Profiling](/concepts/data-profiling.md) in Unity Catalog, enabling data teams to detect, quantify, and alert on shifts in data distributions that may impact downstream analytics or machine learning model performance.

## Overview

Data drift measurement helps answer questions about the statistical distribution of data and how it evolves. For example, users can determine the 90th percentile of a numerical column, examine the distribution of values in a categorical column and how it differs from yesterday, or assess whether there is drift between current data and a known baseline. ^[data-profiling-databricks-on-aws.md]

Drift metrics are particularly valuable for monitoring machine learning model inputs and predictions over time, allowing teams to detect when production data has shifted away from the data used during model training or validation. ^[data-profiling-databricks-on-aws.md]

## How Drift Measurement Works

### Baseline Table

To measure drift, users can optionally specify a **baseline table** that serves as a reference for expected data values and distributions. The baseline table should contain a dataset that reflects the expected quality of the input data in terms of statistical distributions, individual column distributions, missing values, and other characteristics. It must match the schema of the profiled table, with the exception of the timestamp column for time series or inference profiles. ^[data-profiling-databricks-on-aws.md]

For different profile types, the baseline table serves distinct purposes:

- **Snapshot profiles**: The baseline should contain a snapshot where the distribution represents an acceptable quality standard. For example, on grade distribution data, one might set the baseline to a previous class where grades were distributed evenly. ^[data-profiling-databricks-on-aws.md]
- **Time series profiles**: The baseline should contain data representing time windows where data distributions represent an acceptable quality standard. For example, on weather data, one might set the baseline to a week, month, or year where the temperature was close to expected normal temperatures. ^[data-profiling-databricks-on-aws.md]
- **Inference profiles**: A good choice for a baseline is the data used to train or validate the model being profiled. This enables alerts when production data has drifted relative to what the model was trained on. The baseline should contain the same feature columns as the primary table and the same `model_id_col` for consistent aggregation. Ideally, the test or validation set should be used to ensure comparable model quality metrics. ^[data-profiling-databricks-on-aws.md]

### Drift Metrics Table

Data profiling creates a dedicated **drift metrics table** that contains statistics related to the data's drift over time. If a baseline table is provided, drift is also profiled relative to the baseline values. These metric tables are Delta tables stored in a Unity Catalog schema specified by the user. ^[data-profiling-databricks-on-aws.md]

Drift metrics are computed for:
- The entire table
- Time windows specified when creating the profile
- Data subsets (or "slices") defined by the user
- For inference analysis, each model ID ^[data-profiling-databricks-on-aws.md]

## Use Cases

Data drift measurement helps answer questions such as:

- Is there drift between the current data and a known baseline?
- Is there drift between successive time windows of the data?
- What does the statistical distribution or drift of a subset or slice of the data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B? ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The broader framework that includes drift measurement alongside summary statistics and custom metrics.
- [Baseline Table](/concepts/baseline-table.md) — The reference dataset used for computing drift.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) — The output table containing drift statistics.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) — The companion table containing summary statistics.
- [Inference Monitoring](/concepts/inference-monitoring.md) — Using drift measurement to track model input and prediction shifts.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The overarching practice of tracking data integrity over time.

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
