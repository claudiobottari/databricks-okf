---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab82566521ce05ae41948d6e11c1ee62a569c8ae43a319a6f378c596fc6cbbb5
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-drift-monitoring
    - DDM
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Data Drift Monitoring
description: The practice of tracking changes in data distributions over time against a baseline, detecting when data integrity, statistical distributions, or model performance shifts from expected norms.
tags:
  - data-quality
  - mlops
  - monitoring
timestamp: "2026-06-18T11:30:41.517Z"
---

# Data Drift Monitoring

**Data drift monitoring** is the practice of tracking changes in the statistical distribution of data over time to detect when production data deviates from expected patterns. In [Unity Catalog](/concepts/unity-catalog.md), data drift monitoring is a core capability of [Data Profiling](/concepts/data-profiling.md), which computes summary statistics and drift metrics for tables and machine learning model inference data. ^[data-profiling-databricks-on-aws.md]

## Overview

Data drift occurs when the statistical properties of a dataset change over time, potentially degrading the performance of machine learning models or data pipelines that were built on assumptions about the original data distribution. Data profiling in Databricks provides automated drift detection by comparing current data against a known baseline or against successive time windows. ^[data-profiling-databricks-on-aws.md]

Data drift monitoring helps answer questions such as: ^[data-profiling-databricks-on-aws.md]

- Is there drift between the current data and a known baseline?
- Is there drift between successive time windows of the data?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time across different model versions?

## How Data Drift Monitoring Works

### Primary Table and Baseline Table

Data profiling monitors a **primary table** (the table to be profiled) and can optionally use a **baseline table** as a reference for measuring drift. The baseline table should contain a dataset that reflects the expected quality of the input data in terms of statistical distributions, individual column distributions, and missing values. ^[data-profiling-databricks-on-aws.md]

For different profile types, the baseline table serves different purposes: ^[data-profiling-databricks-on-aws.md]

- **Snapshot profiles**: The baseline should contain a snapshot where the distribution represents an acceptable quality standard.
- **Time series profiles**: The baseline should contain data representing time windows where distributions represent an acceptable quality standard.
- **Inference profiles**: A good choice for a baseline is the data used to train or validate the model being profiled. This allows alerts when data has drifted relative to what the model was trained on.

### Drift Metrics Table

Data profiling creates a **drift metrics table** that contains statistics related to the data's drift over time. If a baseline table is provided, drift is also profiled relative to the baseline values. The drift metrics table is a Delta table stored in a Unity Catalog schema that you specify. ^[data-profiling-databricks-on-aws.md]

### Dashboard and Alerts

For each profile, Databricks automatically creates a customizable dashboard to help visualize and present profile results, including drift trends. You can also set up alerts based on the drift metrics to notify teams when drift exceeds acceptable thresholds. ^[data-profiling-databricks-on-aws.md]

## Types of Analysis

Data profiling provides three types of analysis that support drift monitoring: ^[data-profiling-databricks-on-aws.md]

| Analysis Type | Description |
|---------------|-------------|
| **Time series** | Computes metrics over successive time windows to detect drift over time |
| **Inference** | Monitors ML model inputs and predictions for drift, computing metrics per model ID |
| **Snapshot** | Compares a single snapshot of data against a baseline |

## Use Cases

### ML Model Monitoring

Data drift monitoring is critical for production machine learning systems. By profiling inference tables that contain model inputs and predictions, teams can detect when the data distribution has shifted away from the training distribution, potentially indicating model degradation. ^[data-profiling-databricks-on-aws.md]

### Data Pipeline Quality

Data drift monitoring helps track data integrity over time, answering questions such as: ^[data-profiling-databricks-on-aws.md]

- What is the fraction of null or zero values, and has it increased?
- What is the 90th percentile of a numerical column?
- What is the distribution of values in a categorical column, and how does it differ from yesterday?

### Subset and Slice Analysis

Data profiling allows monitoring drift on subsets or slices of data, enabling more granular detection of issues that may affect specific segments of the data population. ^[data-profiling-databricks-on-aws.md]

## Requirements

- Your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) and you must have access to Databricks SQL. ^[data-profiling-databricks-on-aws.md]
- To enable data profiling, you must have `USE CATALOG` on the catalog, `USE SCHEMA` on the schema containing the table, `SELECT` on the table, and `MANAGE` on the catalog, schema, or table. ^[data-profiling-databricks-on-aws.md]
- Only Delta tables are supported for profiling, including managed tables, external tables, views, materialized views, and streaming tables. ^[data-profiling-databricks-on-aws.md]

## Limitations

- Profiles created using time series or inference analysis modes only compute metrics over the last 30 days. ^[data-profiling-databricks-on-aws.md]
- The maximum table size for a snapshot profile is 4TB. For larger tables, use time series profiles instead. ^[data-profiling-databricks-on-aws.md]
- Profiles created over materialized views do not support incremental processing. ^[data-profiling-databricks-on-aws.md]
- Not all regions are supported. ^[data-profiling-databricks-on-aws.md]

## Best Practices

- **Establish a representative baseline** that reflects expected data quality and distributions. For ML models, use the training or validation dataset as the baseline. ^[data-profiling-databricks-on-aws.md]
- **Set up alerts** on drift metrics to proactively detect when data distributions shift beyond acceptable thresholds.
- **Monitor at appropriate granularity** by specifying time windows and data slices that match your use case.
- **Use custom metrics** to track domain-specific drift indicators beyond the default statistics. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The broader capability that provides drift monitoring
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — Monitoring data quality metrics alongside drift
- [MLflow Model Monitoring](/concepts/mlflow-production-monitoring.md) — Monitoring production ML models for performance degradation
- [Inference Tables](/concepts/inference-tables.md) — Tables that store model inputs and predictions for monitoring
- Custom Metrics — User-defined metrics for data profiling
- [Profile Alerts](/concepts/profile-alerts.md) — Automated notifications based on profile metrics

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
