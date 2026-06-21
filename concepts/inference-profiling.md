---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04a3170e5f6fc238ddebc53ec42f8418772cf0711e3c01729e92854e920c3c55
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-profiling
    - InferenceLog Profiling
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Inference Profiling
description: A data profiling type for monitoring machine learning model predictions, requiring prediction column, model ID, and optionally label and problem type.
tags:
  - ml-monitoring
  - data-profiling
  - inference
timestamp: "2026-06-19T09:28:26.828Z"
---

```markdown
# Inference Profiling

**Inference Profiling** is a type of data profile in [[Lakehouse Monitoring|Databricks Lakehouse Monitoring]] that analyzes model inference data — predictions and associated metadata — to monitor the quality and behavior of machine learning models in production. It is designed for datasets that contain model outputs, such as predictions from a deployed model, along with optional ground-truth labels and model identifiers. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Overview

An inference profile runs on a schedule to compute statistics and metrics on model inference tables. It can be created through the Databricks UI (in Catalog Explorer) or via the API. The profile is often used together with [[TimeSeries Profiling]] because inference data is typically time-ordered; in fact, when you select the `Inference` profile type, you must also specify a timestamp column and granularities, just like a time series profile. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

When first created, an inference profile analyzes only the data from the 30 days prior to creation. After that initial run, it processes only newly appended data on each refresh. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Required Configuration

When setting up an inference profile, the following parameters must be specified:

- **Problem type**: Either `classification` or `regression`. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Prediction column**: The column that contains the model's predicted values. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Model ID column**: The column that contains the identifier of the model used for each prediction. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Timestamp column**: A column of type `TIMESTAMP` (or castable via `to_timestamp`) that marks when each prediction was made. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Metric granularities**: The time windows (e.g., hour, day) over which metrics are aggregated. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Additionally, you can optionally specify:

- **Label column**: The column containing ground-truth values for the predictions. When provided, the profile can compute accuracy, precision, recall, or other supervised metrics depending on the problem type. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Performance Considerations

To make inference profiling more efficient and cost-effective as you scale across many tables, it is a best practice to **enable change data feed (CDF)** on the source table. With CDF enabled, each refresh processes only newly appended data instead of re-scanning the entire table. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

> **Note:** Monitors defined on materialized views do not support incremental processing. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Advanced Options

The Databricks UI provides several advanced settings when creating or editing an inference profile:

| Option | Description |
|--------|-------------|
| **Schedule** | Choose between a recurring schedule (e.g., daily) or manual refresh. |
| **Notifications** | Send email alerts on profile completion or anomalies (up to 5 emails per event type). |
| **Metrics tables schema** | Specify a Unity Catalog schema for the output metric tables (defaults to the profiled table's schema). |
| **Assets directory** | An absolute workspace path where profiling assets are stored (defaults to `/Users/{user}/databricks_lakehouse_monitoring/{table_name}`). For shared profiles, use `/Shared/`. |
| **Baseline table** | A reference table or view for comparative analysis. |
| **Slicing expressions** | Define subsets of the data (e.g., `col_2 > 10`) to profile separately. Each expression generates slices for the predicate and its complement. |
| **Custom metrics** | User-defined SQL metrics of types `Aggregate`, `Derived`, or `Drift`. |

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Managing Profiles in the UI

After creation, you can:

- **View refresh history** and trigger manual refreshes from the **Quality** tab in Catalog Explorer. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Edit** profile settings (including schedule, notifications, slicing expressions, and custom metrics) by clicking **Configure** on the **Quality** tab. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Delete** the profile from the same configuration dialog. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

The metric tables produced by inference profiling are Unity Catalog tables and can be queried via notebooks, SQL query explorer, or viewed in Catalog Explorer. Access to these tables can be controlled using Unity Catalog privileges. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [[Data Profiling]] – The general concept of profiling data in Unity Catalog.
- [[TimeSeries Profile]] – A profile type for time-series data, sharing configuration with inference profiles.
- [[Anomaly Detection]] – A feature that can be enabled alongside profiling to detect metric anomalies.
- [[Data Quality Monitoring]] – The broader framework that includes profiling.
- Lakehouse Monitoring Output Tables – The structure of metric tables generated by profiling.

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md
```

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
