---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f209d4ffaaa8f7a7bb3fab6a88c2e2d9b23ba07fb971c1c4e0a1f5a585013231
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-drift-detection
    - DDD
    - Drift Detection
    - Drift detection
    - drift detection
    - Data drift
    - data drift
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Data Drift Detection
description: The practice of measuring changes in data distributions over time using Databricks profiling, with optional baseline tables and drift metrics for comparison.
tags:
  - data-quality
  - drift-detection
  - monitoring
timestamp: "2026-06-19T18:07:09.778Z"
---

# Data Drift Detection

**Data Drift Detection** is a [Data Profiling](/concepts/data-profiling.md) capability that analyzes changes in the statistical distribution of data over time. It helps data practitioners identify when production data has shifted from a known baseline or between successive time windows, enabling proactive monitoring of data quality and machine learning model performance.

## Overview

Data drift detection is provided through the data profiling feature in Unity Catalog's data quality monitoring system. It captures historical metrics of a table's data distribution, which can be used to identify and track changes in data characteristics over time. ^[data-profiling-databricks-on-aws.md]

## How It Works

Data profiling enables drift detection by comparing current data distributions against either a known baseline (such as training data) or against successive time windows of the production data itself. The drift metrics table contains statistics related to the data's drift over time. If a baseline table is provided, drift is also profiled relative to the baseline values. ^[data-profiling-databricks-on-aws.md]

## Questions Data Drift Detection Answers

Data drift detection helps answer practical questions about data consistency and quality: ^[data-profiling-databricks-on-aws.md]

- Is there drift between the current data and a known baseline?
- Is there drift between successive time windows of the data?
- What does the statistical distribution or drift of a subset or slice of the data look like?

## Related Monitoring Capabilities

Data drift detection works alongside other data quality monitoring features: ^[data-profiling-databricks-on-aws.md]

- **Anomaly detection** — Monitors tables for freshness (recent updates) and completeness (expected row counts)
- **Data profiling** — Provides summary statistics and captures historical metrics of data distribution
- **Custom metrics** — Allows users to define additional drift metrics beyond the built-in capabilities
- **Model monitoring** — Tracks how ML model inputs and predictions are shifting over time, and how model performance is trending

## Baseline Tables

A key component of drift detection is the optional **baseline table**, which serves as a reference for measuring drift. The baseline table should contain a dataset that reflects the expected quality of the input data, in terms of statistical distributions, individual column distributions, and missing values. ^[data-profiling-databricks-on-aws.md]

- For **time series profiles**, the baseline table should represent time windows where data distributions represent an acceptable quality standard. ^[data-profiling-databricks-on-aws.md]
- For **inference profiles**, a good choice for a baseline is the data that was used to train or validate the model being profiled. This enables users to be alerted when the data has drifted relative to what the model was trained on. ^[data-profiling-databricks-on-aws.md]
- For **snapshot profiles**, the baseline table should contain a snapshot of the data where the distribution represents an acceptable quality standard. ^[data-profiling-databricks-on-aws.md]

## Practical Applications

Data drift detection is commonly used in the following scenarios: ^[data-profiling-databricks-on-aws.md]

- Tracking how ML model inputs and predictions are shifting over time for model serving endpoints
- Monitoring inference tables that contain model inputs and predictions
- Comparing model version performance (e.g., determining whether model version A is performing better than version B)
- Detecting changes in data integrity, such as increases in null or zero values

## Metric Tables

Data profiling creates two metric tables: ^[data-profiling-databricks-on-aws.md]

- The **profile metrics table** contains summary statistics for each column, time window, and slice
- The **drift metrics table** contains statistics related to the data's drift over time, including drift relative to baseline values if a baseline table is provided

## Limitations

- Time series and inference analysis modes only compute metrics over the last 30 days ^[data-profiling-databricks-on-aws.md]
- Profiles created over materialized views do not support incremental processing ^[data-profiling-databricks-on-aws.md]
- Only Delta tables are supported for profiling ^[data-profiling-databricks-on-aws.md]

## Important Note

Data quality monitoring, including data drift detection, **does not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Data Profiling](/concepts/data-profiling.md)
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Drift Metrics Table](/concepts/drift-metrics-table.md)
- Model Monitoring
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md)
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
