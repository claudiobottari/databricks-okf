---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 13cc87a5295fcb937606f0c96df538dc8cbfd7d38b550678d88414cb2a33a19c
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-analysis-types
    - DPAT
    - Data Profile Types
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Data Profiling Analysis Types
description: "The three modes of analysis in Databricks data profiling: time series (temporal metrics over windows), inference (ML model performance tracking), and snapshot (single-point-in-time profiling)."
tags:
  - data-quality
  - databricks
  - monitoring
  - machine-learning
timestamp: "2026-06-19T14:43:41.174Z"
---

# Data Profiling Analysis Types

Data profiling provides summary statistics for tables, computing profiling metrics over time so you can easily view historical trends. It is useful for in-depth monitoring of all key metrics for select tables, and for tracking the performance of machine learning models and model-serving endpoints. ^[data-profiling-databricks-on-aws.md]

Data profiling on Databricks offers three distinct types of analysis: time series analysis, inference analysis, and snapshot analysis. Each analysis type is designed for different use cases and data characteristics.

## Time Series Analysis

**Time Series Analysis** tracks how data distributions and characteristics change over successive time windows. This is the primary analysis type for monitoring data quality over time. ^[data-profiling-databricks-on-aws.md]

### Key Characteristics

- Computes metrics over the last 30 days for profiled tables ^[data-profiling-databricks-on-aws.md]
- Requires a timestamp column to define time windows for aggregation ^[data-profiling-databricks-on-aws.md]
- Provides drift metrics relative to baseline data or between successive windows ^[data-profiling-databricks-on-aws.md]
- Supports data slicing for subset analysis within each time window ^[data-profiling-databricks-on-aws.md]

### Use Cases

- Tracking changes in data distributions over time ^[data-profiling-databricks-on-aws.md]
- Detecting drift between current data and a known baseline ^[data-profiling-databricks-on-aws.md]
- Monitoring the fraction of null or zero values and how it changes ^[data-profiling-databricks-on-aws.md]
- Comparing 90th percentile values or other distribution metrics across time periods ^[data-profiling-databricks-on-aws.md]

### Baseline Requirements

For time series profiles, the baseline table should contain data representing time windows where data distributions represent an acceptable quality standard. For example, on weather data, you might set the baseline to a week, month, or year where temperature was close to expected normal temperatures. ^[data-profiling-databricks-on-aws.md]

## Inference Analysis

**Inference Analysis** profiles machine learning model inputs and predictions to track model performance over time. This type is used when profiling [Inference Tables](/concepts/inference-tables.md) that contain model inputs and corresponding predictions. ^[data-profiling-databricks-on-aws.md]

### Key Characteristics

- Computes metrics for each model ID in the inference table ^[data-profiling-databricks-on-aws.md]
- Tracks how model inputs and predictions shift over time ^[data-profiling-databricks-on-aws.md]
- Monitors model performance trends across different model versions ^[data-profiling-databricks-on-aws.md]
- Validates whether model version A is performing better than version B ^[data-profiling-databricks-on-aws.md]

### Use Cases

- Monitoring model drift in production deployments ^[data-profiling-databricks-on-aws.md]
- Comparing performance across model versions ^[data-profiling-databricks-on-aws.md]
- Tracking changes in feature distributions that may affect model quality ^[data-profiling-databricks-on-aws.md]
- Detecting data drift relative to training or validation data ^[data-profiling-databricks-on-aws.md]

### Baseline Requirements

For inference profiles, a good baseline choice is the data used to train or validate the model being profiled. This baseline table should contain the same feature columns as the primary table, and ideally the same test or validation set used to evaluate the model. ^[data-profiling-databricks-on-aws.md]

## Snapshot Analysis

**Snapshot Analysis** provides a point-in-time statistical summary of a table's contents. This is the simplest profiling type, computing metrics for the entire table at a single point in time. ^[data-profiling-databricks-on-aws.md]

### Key Characteristics

- Computes summary statistics for the entire table ^[data-profiling-databricks-on-aws.md]
- Does not track changes over time windows ^[data-profiling-databricks-on-aws.md]
- Suitable for smaller tables (maximum 4TB) ^[data-profiling-databricks-on-aws.md]
- Provides a baseline reference for understanding current data quality ^[data-profiling-databricks-on-aws.md]

### Use Cases

- One-time data quality assessment ^[data-profiling-databricks-on-aws.md]
- Establishing a baseline for future time series comparisons ^[data-profiling-databricks-on-aws.md]
- Validating data integrity before downstream processing ^[data-profiling-databricks-on-aws.md]
- Tables that exceed 4TB should use time series profiles instead ^[data-profiling-databricks-on-aws.md]

### Baseline Requirements

For snapshot profiles, the baseline table should contain a snapshot where the distribution represents an acceptable quality standard. For example, on grade distribution data, one might set the baseline to a previous class where grades were distributed evenly. ^[data-profiling-databricks-on-aws.md]

## Comparison of Analysis Types

| Feature | Time Series | Inference | Snapshot |
|---------|-------------|-----------|----------|
| Temporal tracking | Yes | Yes | No |
| Model performance monitoring | No | Yes | No |
| Table size limit | None | None | 4TB |
| Baseline requirement | Time windows | Training/validation data | Quality reference |
| Time range | Last 30 days | Last 30 days | Single point |
| Drift metrics | Yes | Yes | No |

## Selecting an Analysis Type

Choose the analysis type based on your monitoring goals:

- **Time Series**: For general [Data Quality Monitoring](/concepts/data-quality-monitoring.md) over time
- **Inference**: For ML model monitoring in production
- **Snapshot**: For one-time data quality assessment or establishing baselines

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Inference Tables](/concepts/inference-tables.md)
- Model Drift
- Data Drift
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Drift Metrics Table](/concepts/drift-metrics-table.md)

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
