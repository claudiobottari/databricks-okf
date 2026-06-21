---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a23518d96c8f3de21ea12556be714a7bfadbf47bc49dc9ade5243bd1d9e5f2bf
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ml-model-performance-profiling
    - MMPP
  citations:
    - file: data-profiling-databricks-on-aws.md
title: ML Model Performance Profiling
description: Using Databricks data profiling on inference tables to track ML model inputs, predictions, performance trends, and drift over time.
tags:
  - machine-learning
  - databricks
  - mlops
  - monitoring
timestamp: "2026-06-19T18:07:07.421Z"
---

# ML Model Performance Profiling

**ML Model Performance Profiling** is a capability within [Data Profiling](/concepts/data-profiling.md) that tracks the performance of machine learning models over time by profiling inference tables. Inference tables capture model inputs and predictions, and profiling computes summary statistics and drift metrics to monitor how model quality and data distributions evolve. ^[data-profiling-databricks-on-aws.md]

## Overview

ML model performance profiling is a specialized application of data profiling that attaches to an [Inference Table](/concepts/inference-tables.md) — a Delta table that holds a model’s inputs, predictions, and optionally ground truth. By continuously computing metrics on this table, you can answer questions such as:

- How are model inputs and predictions shifting over time?
- How is model performance (e.g., accuracy, error rate) trending?
- Is model version A performing better than model version B? ^[data-profiling-databricks-on-aws.md]

## How It Works

When you create a profile on an inference table, the system generates two metric tables and an automated dashboard:

- **Profile Metrics Table** – Stores summary statistics (e.g., mean, null fraction, value distributions) for each column, time window, and data slice.
- **Drift Metrics Table** – Stores statistics that measure distributional change over time. If a [Baseline Table](/concepts/baseline-table.md) is supplied (typically the training or validation dataset), drift is also computed relative to that baseline. ^[data-profiling-databricks-on-aws.md]

The profile uses a **time series analysis** mode by default, meaning metrics are computed over rolling time windows. You can also use a **snapshot** analysis for point-in-time comparisons, but for ML monitoring the time series mode is standard. ^[data-profiling-databricks-on-aws.md]

### Baseline Table for ML

A best practice for ML model performance profiling is to provide a baseline table containing the data used for training or validation. This allows drift metrics to compare current inference data against a known expected distribution. The baseline should match the feature columns of the primary inference table and should include the same `model_id_col` to ensure consistent aggregation. Ideally, the test or validation set is used as the baseline to produce comparable quality metrics. ^[data-profiling-databricks-on-aws.md]

## Key Benefits

- **Automated monitoring** – Once configured, metrics are recalculated on a schedule without manual intervention.
- **Custom slicing** – You can define data slices (subsets defined by filtering expressions) and track metrics separately per slice.
- **Model version comparison** – By profiling inference tables that include a model ID column, you can compare performance across different model versions. ^[data-profiling-databricks-on-aws.md]

## Limitations

- Only Delta tables are supported (managed, external, views, materialized views, or streaming tables).
- The maximum table size for a snapshot profile is 4 TB; for larger tables, use time series profiles.
- Time series and inference profiles only compute metrics over the last 30 days by default (contact Databricks to adjust).
- Not all cloud regions support data profiling; check regional availability in the Databricks documentation. ^[data-profiling-databricks-on-aws.md]

## Getting Started

To start profiling a model’s performance:

1. Ensure your workspace has [Unity Catalog](/concepts/unity-catalog.md) enabled and you have the required privileges (`SELECT`, `MANAGE`, etc.).
2. Create a profile on an inference table using the Databricks UI or API.
3. Optionally specify a baseline table (training/validation data).
4. View the automatically generated dashboard, or query the metric tables directly via Databricks SQL.
5. Set up alerts on metric thresholds for proactive monitoring. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The general framework for computing summary statistics and drift over time.
- [Inference Table](/concepts/inference-tables.md) – The table type used to store model inputs, predictions, and ground truth.
- [Model Serving](/concepts/model-serving.md) – The production workload that generates inference data for profiling.
- [Drift Metrics](/concepts/drift-metrics.md) – Statistics that quantify distributional shift in data and predictions.
- [Baseline Table](/concepts/baseline-table.md) – An optional reference dataset used to compute drift relative to expected values.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages tables and permissions for profiling.

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
