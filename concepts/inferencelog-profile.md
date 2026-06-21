---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73ff041d629559584f0944bbe3072f544dec2a2af93d99ad96bde64e1f4e033e
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inferencelog-profile
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: InferenceLog Profile
description: A data profile type for ML model monitoring that includes model quality metrics alongside time-series distribution analysis
tags:
  - databricks
  - machine-learning
  - inference-monitoring
timestamp: "2026-06-19T17:55:01.497Z"
---

---
title: InferenceLog Profile
summary: A data profile type that extends TimeSeries with model quality metrics (classification or regression), using prediction, label, and model_id columns.
sources:
  - create-a-data-profile-using-the-api-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:12:56.172Z"
updatedAt: "2026-06-19T14:29:09.111Z"
tags:
  - data-quality
  - monitoring
  - machine-learning
aliases:
  - inferencelog-profile
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# InferenceLog Profile

An **InferenceLog Profile** is a type of data profile in Databricks that monitors the quality of model inference data over time. It extends the [TimeSeries Profile](/concepts/timeseries-profile.md) by additionally computing model quality metrics, making it suitable for tracking the performance of deployed machine learning models. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Overview

InferenceLog profiles analyze data distributions across time windows while also evaluating prediction accuracy against ground-truth labels. They are designed for monitoring production model inference tables and can handle both classification and regression problem types. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

The profile is defined on any managed or external Delta table registered in [Unity Catalog](/concepts/unity-catalog.md). Only a single profile can exist per table in a Unity Catalog [Metastore](/concepts/metastore.md). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

When first created, an InferenceLog profile analyzes only data from the 30 days prior to its creation. After the profile is created, all new incoming data is processed incrementally. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Parameters

When creating an InferenceLog profile via the API, you configure an `InferenceLogConfig` with the following parameters:

| Parameter | Description |
|-----------|-------------|
| `problem_type` | The type of inference problem (e.g., `INFERENCE_PROBLEM_TYPE_CLASSIFICATION` for classification, or regression problem types). |
| `prediction_column` | The column containing model predictions. |
| `model_id_column` | The column identifying distinct model versions or IDs. |
| `label_column` | *(Optional)* The column containing ground-truth labels, used to compute quality metrics. |
| `timestamp_column` | The timestamp column (data type must be `TIMESTAMP` or convertible via `to_timestamp`). Used to define time windows for metric aggregation. |
| `granularities` | The time granularities over which to aggregate metrics (e.g., `AGGREGATION_GRANULARITY_1_DAY`). |

Slices are automatically created based on distinct values of the `model_id_column`, enabling per-model-version analysis. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Best Practices

- **Enable Change Data Feed (CDF)** on the table. When CDF is enabled, only newly appended data is processed on each refresh, rather than re-scanning the entire table. This improves efficiency and reduces cost as the number of tables grows.
- Profiles defined on materialized views do not support incremental processing; they will re-process all data at each refresh.

^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Data Profiling in Unity Catalog](/concepts/data-profiling-in-databricks.md) — The broader framework for monitoring data quality.
- [TimeSeries Profile](/concepts/timeseries-profile.md) — A similar profile type without model quality metrics.
- [Snapshot Profile](/concepts/snapshot-profile.md) — A profile type that captures the full table state at each refresh.
- InferenceLogConfig — The API configuration object for InferenceLog profiles.
- Model Monitoring — Continuous monitoring of model performance in production.
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) — The initial analysis constraint applied to time series and inference profiles.

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
