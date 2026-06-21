---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 005704df24c126333c664ddfef38a148f838927f52e68cb255663b69737a500c
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - drift-detection-data-quality
    - DD(Q
    - drift detection
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Drift detection (data quality)
description: A monitoring capability that identifies statistical drift between current data and a known baseline, between successive time windows, or in ML model inputs and predictions over time.
tags:
  - data-quality
  - machine-learning
  - monitoring
timestamp: "2026-06-19T18:08:01.018Z"
---

## Drift detection (data quality)

**Drift detection** is a capability within [Data Profiling](/concepts/data-profiling.md) that measures how the statistical properties of a dataset change over time. It helps data practitioners answer questions about distribution shifts, baseline deviations, and performance drift in machine learning models.

### Overview

Drift detection is one of the analytical functions offered by [Data Quality Monitoring](/concepts/data-quality-monitoring.md) on Databricks. It is exposed through the data profiling feature, which captures historical metrics of a table’s data distribution. These metrics can be used to compare the current data against a known baseline, between successive time windows, or across different slices (subsets) of data. ^[data-quality-monitoring-databricks-on-aws.md]

### Types of drift

Data profiling enables users to detect several forms of drift:

- **Distribution drift**: Changes in the statistical distribution of a column (e.g., a shift in the 90th percentile of a numerical column, or a change in the frequency of values in a categorical column).
- **Baseline drift**: Drift between the current data and a reference baseline table.
- **Temporal drift**: Drift between successive time windows of the same table.
- **Slice drift**: Drift within a specific subset or slice of the data, such as a particular geographic region or customer segment.
- **Model input/prediction drift**: For inference tables, drift in the distribution of model inputs and predictions over time.
- **Model performance drift**: Trends in model performance metrics (e.g., accuracy, precision) and comparisons between model versions.

^[data-quality-monitoring-databricks-on-aws.md]

### How drift detection works

Drift detection relies on the historical metrics stored by the data profiling system. When a profile is created or refreshed, the system computes summary statistics (e.g., mean, percentiles, null fraction, category frequencies) for each column in the monitored table. These statistics are stored in a [Profile Metrics Table](/concepts/profile-metrics-table.md) and a [Drift Metrics Table](/concepts/drift-metrics-table.md). By comparing the metrics of the current window against those of a baseline or previous window, the system quantifies the drift. ^[data-quality-monitoring-databricks-on-aws.md]

### Use cases

Data teams use drift detection to:

- Monitor data integrity over time (e.g., has the fraction of null or zero values increased?).
- Ensure that machine learning models continue to operate on data that matches the training distribution.
- Trigger alerts when significant distribution shifts occur, prompting investigation or retraining.
- Compare the performance of model version A vs. version B.

^[data-quality-monitoring-databricks-on-aws.md]

### Related concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The umbrella feature that includes anomaly detection and data profiling.
- [Anomaly detection (data quality)](/concepts/anomaly-detection-databricks.md) – A complementary feature that monitors table freshness and completeness.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, time window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics that track distribution changes over time.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – A profile type for monitoring model predictions and drift.
- Time Series Analysis – A profile type for monitoring data over continuous time windows.

### Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
