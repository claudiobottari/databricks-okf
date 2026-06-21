---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ed447499cde006e2047b618d2f45adaa5431145868f903b0a0397e98caac4ce
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-table-profiling-for-ml-models
    - ITPFMM
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Inference Table Profiling for ML Models
description: Profiling inference tables that contain ML model inputs and predictions to track model performance over time, compare model versions, and detect data drift relative to training/validation data.
tags:
  - machine-learning
  - mlops
  - databricks
timestamp: "2026-06-18T11:33:07.337Z"
---

# Inference Table Profiling for ML Models

**Inference table profiling** is a feature of [Data Profiling](/concepts/data-profiling.md) in Databricks that tracks the performance of machine learning models over time by profiling inference tables containing model inputs and predictions. This enables monitoring of model quality, input drift, and prediction distribution changes across model versions. ^[data-profiling-databricks-on-aws.md]

## Overview

Inference table profiling allows you to continuously monitor how your deployed ML models are performing in production. By attaching a profile to an inference table — a [Delta table](/concepts/delta-lake-table.md) that stores model inputs and corresponding predictions — you can track metrics such as prediction distributions, model performance trends, and data drift relative to training or validation data. ^[data-profiling-databricks-on-aws.md]

This approach helps answer questions such as:

- How are ML model inputs and predictions shifting over time?
- How is model performance trending across time periods?
- Which model version (A vs B) is performing better?

## How It Works

To profile the performance of a machine learning model, you create a profile attached to an inference table that holds the model's inputs and corresponding predictions. This is known as an **inference profile** (also referred to as inference analysis mode). ^[data-profiling-databricks-on-aws.md]

### Primary Table and Baseline Table

The **primary table** is the inference table to be profiled. You can optionally specify a **baseline table** to use as a reference for measuring drift. A good choice for a baseline is the data used to train or validate the model being profiled. This way, you can be alerted when production data has drifted relative to what the model was trained on. ^[data-profiling-databricks-on-aws.md]

The baseline table should:
- Contain the same feature columns as the primary table
- Have the same `model_id_col` specified for the primary table's InferenceLog so that data is aggregated consistently
- Ideally use the test or validation set used to evaluate the model, ensuring comparable model quality metrics

When a baseline table is provided, drift is computed relative to expected data values and distributions from the baseline.

### What Gets Measured

For inference analysis, metrics are computed:

- **For the entire table** — overall statistics across all predictions
- **For specified time windows** — tracking changes over time
- **For data subsets (slices)** — analyzing segments of the data
- **For each model ID** — comparing performance across different model versions

## Metric Tables

When you create an inference profile, Databricks generates two metric tables stored in a Unity Catalog schema you specify: ^[data-profiling-databricks-on-aws.md]

| Metric Table | Description |
|-------------|-------------|
| Profile metrics table | Contains summary statistics about the inference data |
| Drift metrics table | Contains statistics related to data drift over time (and relative to the baseline table, if provided) |

These metric tables are Delta tables that you can query using Databricks SQL, view in the UI, and use to create dashboards and alerts. Databricks also automatically creates a customizable dashboard for each profile to help visualize results.

## Requirements

- Your workspace must be enabled for Unity Catalog and have access to Databricks SQL. ^[data-profiling-databricks-on-aws.md]
- You must have `USE CATALOG` on the catalog, `USE SCHEMA` on the schema, `SELECT` on the table, and `MANAGE` on the catalog, schema, or table.
- Inference profiling uses serverless compute for jobs but does not require that your account be enabled for serverless compute.
- The inference table must be a [Delta table](/concepts/delta-lake-table.md) (managed, external, or a streaming table).

## Limitations

- Profiles created using inference analysis mode only compute metrics over the last 30 days. To adjust this, contact your Databricks account team. ^[data-profiling-databricks-on-aws.md]
- Only Delta tables are supported for profiling.
- Profiles created over materialized views do not support incremental processing.
- Not all regions are supported.

## Getting Started

To create an inference profile:

1. **Create or identify an inference table** that contains model inputs and predictions.
2. **Create a profile** attached to the inference table using the Databricks UI or API, selecting the inference analysis mode.
3. **Optionally specify a baseline table** (such as your training or validation data).
4. **View results** in the automatically created dashboard, or query the metric tables directly.

For additional guidance, see:
- Monitor served models using Unity AI Gateway-enabled inference tables
- [Data profiling dashboard](/concepts/data-profiling-dashboard.md)
- [Data profiling metric tables](/concepts/profile-metrics-table.md)
- [Profile Alerts](/concepts/profile-alerts.md)

## Use Cases

- **Monitoring model performance degradation** — detect when prediction accuracy changes over time
- **Detecting training-serving skew** — compare production data distributions to training data distributions
- **Comparing model versions** — evaluate whether a new model version (A) performs better than the previous version (B)
- **Alerting on data drift** — receive notifications when input data distributions shift significantly

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The broader feature that provides summary statistics for tables
- [Inference Table](/concepts/inference-tables.md) — The Delta table storing model inputs and predictions
- Data Drift — Changes in data distribution over time
- Model Performance Monitoring — Tracking ML model quality in production
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores metric tables
- [Delta Tables](/concepts/delta-lake-table.md) — The supported table format for profiling
- MLflow Models — Models that can be monitored via inference profiling

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
