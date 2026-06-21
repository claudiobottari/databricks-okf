---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9881c989be86b251472dbad9cc0932f137377aa7d78be8031a4362bd63e21c86
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-table-profiling
    - ITP
    - ITPM
    - inference-table-profiling-for-ml-models
    - ITPFMM
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Inference Table Profiling
description: A data profiling mode for tracking ML model performance over time by profiling inference tables that contain model inputs and predictions, supporting model version comparison.
tags:
  - machine-learning
  - model-monitoring
  - inference
  - databricks
timestamp: "2026-06-19T09:45:05.545Z"
---

# Inference Table Profiling

**Inference Table Profiling** is a mode of [Data Profiling](/concepts/data-profiling.md) in Databricks Unity Catalog that monitors machine learning model inputs, predictions, and performance over time. By profiling an inference table containing model inputs and corresponding predictions, you can track model quality trends, detect shifts in data distributions, and compare performance across model versions.^[data-profiling-databricks-on-aws.md]

## Overview

Inference table profiling extends data profiling to machine learning workloads. Instead of profiling raw data tables, you attach a profile to an **inference table** – a table that holds the model's input features and the model's predictions. Profiling then computes metrics for the entire table and, for inference analysis, for each **model ID** separately.^[data-profiling-databricks-on-aws.md]

## What Inference Table Profiling Tracks

Inference table profiling helps answer questions such as:

- How are ML model inputs and predictions shifting over time?^[data-profiling-databricks-on-aws.md]
- How is model performance trending over time? Is model version A performing better than version B?^[data-profiling-databricks-on-aws.md]
- Is there drift between the current data and a known baseline, or between successive time windows of the data?^[data-profiling-databricks-on-aws.md]

## Baseline Table for Inference Profiles

For inference profiles, a good baseline table is the data that was used to **train or validate** the model being profiled. This way, users can be alerted when the input data has drifted relative to what the model was trained on. The baseline table should:

- Contain the same **feature columns** as the primary table.^[data-profiling-databricks-on-aws.md]
- Include the same `model_id_col` specified for the primary table's `InferenceLog` so that data is aggregated consistently.^[data-profiling-databricks-on-aws.md]
- Ideally, use the test or validation set used to evaluate the model to ensure comparable model quality metrics.^[data-profiling-databricks-on-aws.md]

## Key Capabilities

- **Per‑model‑ID metrics**: Metrics are computed for each model version (identified by `model_id_col`), enabling per‑version quality tracking.^[data-profiling-databricks-on-aws.md]
- **Time‑series analysis**: Inference profiles only compute metrics over the last **30 days** by default.^[data-profiling-databricks-on-aws.md] (For longer windows, contact your Databricks account team.)^[data-profiling-databricks-on-aws.md]
- **Drift detection**: If a baseline table is provided, drift is profiled relative to baseline values.^[data-profiling-databricks-on-aws.md]
- **Custom metrics**: You can add custom metrics beyond the built-in summary statistics.^[data-profiling-databricks-on-aws.md]

## Requirements

- Your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) and you must have access to Databricks SQL.^[data-profiling-databricks-on-aws.md]
- To enable profiling, you need `USE CATALOG` on the catalog, `USE SCHEMA` on the schema containing the table, `SELECT` on the table, and `MANAGE` on the catalog, schema, or table.^[data-profiling-databricks-on-aws.md]
- Only **Delta tables** are supported for profiling (managed, external, views, materialized views, or streaming tables).^[data-profiling-databricks-on-aws.md]

## Output

Profiling creates two metric tables (stored as Delta tables in a Unity Catalog schema) and an auto‑generated dashboard:

- **Profile metrics table** – contains summary statistics.
- **Drift metrics table** – contains drift statistics (relative to baseline if provided).

Both tables can be queried via Databricks SQL, used for dashboards, and used for alerts.^[data-profiling-databricks-on-aws.md]

## Related Use Cases

- Monitor served models using Unity AI Gateway‑enabled inference tables – using inference tables with AI Gateway for real‑time monitoring.
- [Monitor fairness and bias for classification models](/concepts/fairness-and-bias-monitoring-for-classification-models.md) – fairness and bias tracking for classification models.
- Data profiling custom metrics – extending profiling with custom metrics.
- [Model Serving](/concepts/model-serving.md) – the endpoint that feeds inference tables.

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
