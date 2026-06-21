---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eab8837c63f2d2604bf688225232b027d5241238ea7b7f28546b62a87b05ac1d
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-on-databricks-batch-and-real-time
    - "Real-Time and Model Serving on Databricks: Batch"
    - MSODBAR
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: "Model Serving on Databricks: Batch and Real-Time"
description: "Two model deployment patterns: batch inference for efficient large-scale scoring and real-time serving via low-latency API endpoints, with governance through Unity Catalog inference tables."
tags:
  - model-deployment
  - inference
  - mlops
timestamp: "2026-06-18T15:05:41.795Z"
---

# Model Serving on Databricks: Batch and Real-Time

**Model Serving on Databricks** refers to the deployment and serving of machine learning models for inference, supporting both batch and real-time workloads within a unified platform. Databricks provides infrastructure and tooling to serve models efficiently, with governance and observability integrated through Unity Catalog and MLOps practices. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Batch Inference

Batch inference applies a trained model to a large dataset in a single, non-interactive job. It is optimized for high throughput and cost efficiency, processing many records at once rather than responding to individual requests. Batch inference is commonly used for offline scoring, nightly recommendations, or periodic data enrichment. Databricks supports batch inference through standard Spark-based or Python-based jobs, leveraging scalable compute resources. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Real-Time Serving

Real-time serving exposes models as low-latency API endpoints, enabling interactive inference for applications such as chatbots, fraud detection, or dynamic personalization. Databricks provides managed infrastructure for deploying these endpoints with autoscaling, load balancing, and monitoring. Real-time serving endpoints log inference requests and responses to inference tables governed in [Unity Catalog](/concepts/unity-catalog.md), enabling auditability and downstream analysis. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Model Deployment and Diagnostics with Genie Code

[Genie Code](/concepts/genie-code.md) — Databricks’ AI-assisted development tool — can generate code for deploying models to both batch and real-time serving endpoints. It also provides diagnostic capabilities, helping users identify performance issues and optimize model serving endpoints directly from the notebook interface. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Governance and MLOps

Models served on Databricks are fully governed by Unity Catalog, which tracks model versions, lineage, and access controls. The [AI Gateway](/concepts/ai-gateway.md) provides a central layer for managing, securing, and monitoring access to both external and internally served models. Databricks’ MLOps tooling (e.g., [MLOps Stacks](/concepts/mlops-stacks.md)) enables automated promotion of models from development through staging to production, with infrastructure-as-code templates. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Integration with the ML Lifecycle

Model serving is part of a unified DS/ML lifecycle. Models are tracked in the [Model Registry](/concepts/mlflow-model-registry.md) (backed by Unity Catalog), where each deployed version links to its training run, dataset, environment, and git commit, providing a complete audit trail. Real-time serving endpoints automatically log to inference tables, which can be used for [Data Quality Monitoring](/concepts/data-quality-monitoring.md) and drift detection. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- Batch Inference
- Real-Time Serving
- [Unity Catalog](/concepts/unity-catalog.md)
- [AI Gateway](/concepts/ai-gateway.md)
- [Model Registry](/concepts/mlflow-model-registry.md)
- [MLOps Stacks](/concepts/mlops-stacks.md)
- [Genie Code](/concepts/genie-code.md)
- [Inference Tables](/concepts/inference-tables.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
