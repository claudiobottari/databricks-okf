---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f035e31e128f5a9f65d24cf9b98f3974c56966cf158b77001e33b8cc46ad9b5
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-table-monitoring
    - ITM
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Inference Table Monitoring
description: A use case of data profiling that tracks performance of GenAI apps, ML models, and model-serving endpoints by monitoring inference tables containing model inputs and predictions.
tags:
  - machine-learning
  - monitoring
  - genai
  - model-serving
timestamp: "2026-06-19T09:45:39.915Z"
---

# Inference Table Monitoring

**Inference Table Monitoring** refers to the practice of applying [Data Quality Monitoring](/concepts/data-quality-monitoring.md) capabilities to inference tables — tables that contain model inputs, predictions, and outputs from [MLflow](/concepts/mlflow.md) model serving endpoints or [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications. By monitoring inference tables, teams can track model performance, detect data drift, and ensure the quality of predictions over time.

## Overview

Inference tables are automatically populated by model serving endpoints and contain structured records of model inputs and predictions. Monitoring these tables provides visibility into how model behavior evolves as the data distribution shifts, which is critical for maintaining trust in production machine learning systems. ^[data-quality-monitoring-databricks-on-aws.md]

## Capabilities

Inference table monitoring builds on the two core capabilities of [Unity Catalog](/concepts/unity-catalog.md) data quality monitoring:

### Data Profiling

Data profiling provides summary statistics of the data in an inference table, which can be used to track the performance of GenAI apps, machine learning models, and model-serving endpoints by monitoring inference tables that contain model inputs and predictions. ^[data-quality-monitoring-databricks-on-aws.md]

Data profiling captures historical metrics of a table's data distribution or corresponding model's performance, which can be used for quick summary statistics to monitor a table and send alerts for changes. ^[data-quality-monitoring-databricks-on-aws.md]

Data profiling helps answer questions such as:

- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B?
- What does the statistical distribution or drift of a slice of the data look like?

^[data-quality-monitoring-databricks-on-aws.md]

### Anomaly Detection

Anomaly detection monitors enabled tables for freshness and completeness. While primarily designed for general data tables, these same checks can be applied to inference tables to detect when model serving stops producing predictions (freshness) or when prediction volumes drop unexpectedly (completeness). ^[data-quality-monitoring-databricks-on-aws.md]

## Key Monitoring Metrics

When monitoring inference tables, teams typically track:

- **Input drift**: How the distribution of model inputs changes over time compared to a baseline.
- **Prediction drift**: How the distribution of model outputs shifts over time.
- **Performance drift**: How model accuracy or other quality metrics change over time, which can be tracked by comparing predictions against ground truth data.
- **Freshness**: Whether the serving endpoint is producing predictions as expected.
- **Completeness**: Whether the expected number of predictions are being generated.

Data profiling in particular lets you control the time granularity of observations and set up custom metrics. ^[data-quality-monitoring-databricks-on-aws.md]

## Use Cases

- **Model monitoring in production**: Track how model behavior changes as new data arrives, enabling early detection of concept drift or data quality issues.
- **A/B comparison**: Compare the performance of model version A versus version B by monitoring their respective inference tables.
- **Alerting**: Set up alerts when prediction volumes drop or when input data distributions deviate significantly from training data.

## Limitations

Data quality monitoring **does not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — Captures historical metrics of data distribution and model performance
- [Anomaly Detection](/concepts/anomaly-detection.md) — Monitors freshness and completeness of tables
- [Model Serving](/concepts/model-serving.md) — Endpoints that produce inference tables
- [MLflow](/concepts/mlflow.md) — Framework for managing the ML lifecycle, including model deployment
- [GenAI Application Monitoring](/concepts/mlflow-genai-production-monitoring.md) — Specialized monitoring for generative AI applications
- Data Drift — Changes in data distribution over time

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
