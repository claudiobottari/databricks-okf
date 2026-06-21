---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aaf03370704e015772606b74b9c217c8ff3e1fb49cd822cde27744768c138b3f
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-monitoring
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 9
      end: 12
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 24
      end: 28
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 20
      end: 24
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 30
      end: 30
title: Inference Monitoring
description: Tracking the performance of GenAI applications, machine learning models, and model-serving endpoints by monitoring inference tables that contain model inputs and predictions.
tags:
  - machine-learning
  - monitoring
  - inference
  - gen-ai
timestamp: "2026-06-18T11:32:41.858Z"
---

---
title: Inference Monitoring
summary: Inference monitoring tracks the performance of GenAI apps, machine learning models, and model-serving endpoints by monitoring inference tables that contain model inputs and predictions. It is a capability of data profiling within Unity Catalog data quality monitoring.
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - data-quality
  - monitoring
  - inference
  - mlflow
  - unity-catalog
aliases:
  - inference-monitoring
  - IM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Inference Monitoring

**Inference monitoring** is a feature of [Data Profiling](/concepts/data-profiling.md) (formerly Lakehouse Monitoring) in Unity Catalog that tracks the performance of [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications, machine learning models, and [model-serving endpoints](/concepts/model-serving-endpoint.md) by analyzing [Inference Tables](/concepts/inference-tables.md) containing model inputs and predictions. It is part of the broader [Data Quality Monitoring](/concepts/data-quality-monitoring.md) framework. ^[data-quality-monitoring-databricks-on-aws.md#L9-L12]

## How It Works

Inference monitoring uses data profiling to capture summary statistics and historical metrics from inference tables — tables in Unity Catalog that store the inputs sent to a model and the predictions or outputs returned. By monitoring these tables, teams can answer questions about:

- How model inputs and predictions are shifting over time.
- How model performance is trending across different model versions. ^[data-quality-monitoring-databricks-on-aws.md#L24-L28]

The statistics computed by inference monitoring include distributions of numerical columns, frequencies of categorical values, and drift between successive time windows. These metrics can be sliced by subsets of the data to investigate specific segments of inference traffic. ^[data-quality-monitoring-databricks-on-aws.md#L20-L24]

## Use Cases

- **Track input drift**: Detect when the statistical distribution of inputs to a deployed model changes, potentially degrading prediction quality.
- **Monitor prediction drift**: Observe whether model outputs shift over time, which may indicate concept drift or data pipeline issues.
- **Compare model versions**: Evaluate which version of a model delivers more stable or accurate predictions by analyzing inference data from A/B deployments.
- **Alert on anomalies**: Combined with [Anomaly Detection](/concepts/anomaly-detection.md) (freshness and completeness), inference monitoring can trigger alerts when inference tables become stale or incomplete.

## Non-Intrusive Monitoring

Data profiling — and therefore inference monitoring — does **not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables. It reads historical metadata and computes metrics separately. ^[data-quality-monitoring-databricks-on-aws.md#L30-L30]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The umbrella framework for anomaly detection and data profiling.
- [Data Profiling](/concepts/data-profiling.md) — The component that provides inference monitoring capabilities.
- [Anomaly Detection](/concepts/anomaly-detection.md) — A complementary feature that monitors freshness and completeness.
- [Inference Tables](/concepts/inference-tables.md) — Unity Catalog tables that capture model inputs and outputs.
- [Model-serving endpoints](/concepts/model-serving-endpoint.md) — The deployment targets whose inference data can be monitored.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores inference tables and enables monitoring.

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md:9-12](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
2. [data-quality-monitoring-databricks-on-aws.md:24-28](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
3. [data-quality-monitoring-databricks-on-aws.md:20-24](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
4. [data-quality-monitoring-databricks-on-aws.md:30-30](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
