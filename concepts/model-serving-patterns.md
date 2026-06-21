---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1cbcaa54fe00f5a42ce3f59b9f4e57b863106e923e3cd16a7cbd24b15eb608bd
  pageDirectory: concepts
  sources:
    - machine-learning-lifecycle-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-patterns
    - MSP
    - Model Serving Architecture
  citations:
    - file: machine-learning-lifecycle-databricks-on-aws.md
title: Model Serving Patterns
description: "Two primary deployment patterns on Databricks: real-time serving via low-latency REST endpoints (Model Serving) and batch inference via ai_query, Spark UDFs, or mlflow.pyfunc for periodic jobs."
tags:
  - machine-learning
  - deployment
  - mlops
timestamp: "2026-06-19T19:20:02.495Z"
---

## Model Serving Patterns

**Model serving patterns** describe the methods by which a trained machine learning model is deployed to generate predictions from input data in a production environment. Databricks supports two primary serving patterns: real-time (low-latency REST endpoints) and batch (periodic bulk inference). Both patterns can serve the same trained model artifact, using the same governance and lineage from a single registered version in Unity Catalog. ^[machine-learning-lifecycle-databricks-on-aws.md]

### Real-Time Serving

Real-time serving exposes the model as a low-latency REST endpoint using [Model Serving](/concepts/model-serving.md). This pattern is used for applications that require immediate decisions, such as fraud interception at transaction time, live personalization, or dynamic pricing. The model is deployed as a managed endpoint that scales to handle request traffic. ^[machine-learning-lifecycle-databricks-on-aws.md]

For logging and monitoring in real-time serving, [Inference Tables](/concepts/inference-tables.md) provide automatic logging of inputs and outputs from the endpoint without requiring changes to the model code. These logs feed into downstream monitoring systems for [Data Quality Monitoring](/concepts/data-quality-monitoring.md), [drift detection](/concepts/drift-detection-data-quality.md), and performance tracking. ^[machine-learning-lifecycle-databricks-on-aws.md]

### Batch Inference

Batch inference is used for periodic, bulk prediction jobs such as daily forecasts, nightly recommendation refreshes, or other scheduled processing. Databricks supports batch inference through several mechanisms:

- **[`ai_query`](https://docs.databricks.com/aws/en/large-language-models/ai-query#custom-model)** – provides efficient batch inference for custom models deployed as [Model Serving](/concepts/model-serving.md) endpoints.
- **Custom code with Apache Spark UDFs** – allows embedding model inference logic directly in Spark transformations.
- **[`mlflow.pyfunc`](https://docs.databricks.com/aws/en/mlflow/models#generated-code-snippets)** – a generic Python function wrapper that can run batch predictions within a Spark pipeline.

Batch inference pipelines write results to [Delta tables](/concepts/delta-lake-table.md) managed by [Unity Catalog](/concepts/unity-catalog.md), making the predictions available for downstream applications, dashboards, or automated workflows. ^[machine-learning-lifecycle-databricks-on-aws.md]

### Artifact Reuse

A key principle across these patterns is that **you train once and deploy from the same registered model version**. Whether the deployment target is a real-time endpoint or a batch pipeline, the same model artifact, metadata, and governance controls are used, eliminating training-serving skew. This is facilitated by the [MLflow Model Registry](/concepts/mlflow-model-registry.md) in Unity Catalog. ^[machine-learning-lifecycle-databricks-on-aws.md]

### Monitoring Considerations

For both serving patterns, production monitoring is critical. The [MLOps lifecycle](/concepts/ml-lifecycle.md) recommends logging model inputs and outputs continuously. Real-time serving uses [Inference Tables](/concepts/inference-tables.md) for automatic logging; batch pipelines inherently read from and write to Delta tables, providing a natural audit trail. These logs feed into [Data Quality Monitoring](/concepts/data-quality-monitoring.md) and [drift detection](/concepts/drift-detection-data-quality.md) to detect degradation over time. ^[machine-learning-lifecycle-databricks-on-aws.md]

### Related Concepts

- [Model Serving](/concepts/model-serving.md)
- Real-time serving
- [Batch inference](/concepts/batch-inference-pipelines.md)
- [Inference Tables](/concepts/inference-tables.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Drift detection](/concepts/data-drift-detection.md)
- MLOps workflows

### Sources

- machine-learning-lifecycle-databricks-on-aws.md

# Citations

1. [machine-learning-lifecycle-databricks-on-aws.md](/references/machine-learning-lifecycle-databricks-on-aws-d195211f.md)
