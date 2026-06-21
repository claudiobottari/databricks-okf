---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eafdb20d9ea13b42dc4f051508781083141d3a47a35c5ddeee18cbadf4955e27
  pageDirectory: concepts
  sources:
    - model-registry-improvements-with-mlflow-3-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-traces-in-unity-catalog
    - MTIUC
    - Store traces in Unity Catalog
    - Traces in Unity Catalog
    - traces in Unity Catalog
    - Log traces to Unity Catalog tables
    - Storing Traces in Unity Catalog
  citations:
    - file: model-registry-improvements-with-mlflow-3-databricks-on-aws.md
title: Model Traces in Unity Catalog
description: Traces panel on the model version page that consolidates inference traces from development, evaluation (mlflow.evaluate()), and online serving endpoints for full observability.
tags:
  - machine-learning
  - mlflow
  - observability
  - tracing
timestamp: "2026-06-19T19:43:42.380Z"
---

# Model Traces in Unity Catalog

**Model Traces in Unity Catalog** refers to the ability to view, search, and analyze [[MLflow Trace|MLflow Traces]] associated with a registered model directly from the Unity Catalog model registry interface and API. This feature is part of the [MLflow 3](/concepts/mlflow-3.md) improvements to the model registry.

## Overview

In MLflow 3, the Unity Catalog model registry has been enhanced to consolidate trace data from multiple sources. When you register a `LoggedModel` to the Unity Catalog model registry, all associated traces are made available in the model registry UI. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

The **Traces** panel on the model version page in Unity Catalog displays traces associated with the Model ID from:
- Development and evaluation runs (from `mlflow.evaluate()` runs)
- Online serving traces from model endpoints

^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

## Key Capabilities

### Unified Trace View

Model traces from all MLflow experiments and workspaces are accessible on a single page, providing a comprehensive view of model performance across the entire development and production lifecycle. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### Search and Filter

Users can search for specific traces using the search box in the **Traces** panel, making it easier to find relevant trace data among potentially large collections. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### Detailed Inspection

Clicking on a trace in the panel reveals the full set of Spans|span within that trace, allowing for detailed analysis of model behavior and performance. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### API Access

Beyond the UI, traces are also accessible programmatically through the Unity Catalog model registry API. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

## Accessing the Traces Panel

To view model traces in Unity Catalog:

1. Navigate to the registered model in Unity Catalog.
2. Select the desired model version.
3. Open the **Traces** tab on the model version page.

From this panel, you can search for traces and click on individual entries to view their complete span details. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) — The centralized model registry enhanced with MLflow 3 features.
- [MLflow LoggedModel](/concepts/mlflow-loggedmodel.md) — The object whose metrics and parameters are registered to the Unity Catalog registry.
- [[MLflow Trace|MLflow Traces]] — The trace data collected during development, evaluation, and serving.
- Spans — The individual components within a trace that can be inspected in detail.
- [MLflow Evaluate](/concepts/mlflow-genai-evaluate-api.md) — The evaluation function whose runs produce traces visible in the model registry.
- [Model Serving](/concepts/model-serving.md) — Online serving endpoints that generate production traces.

## Sources

- model-registry-improvements-with-mlflow-3-databricks-on-aws.md

# Citations

1. [model-registry-improvements-with-mlflow-3-databricks-on-aws.md](/references/model-registry-improvements-with-mlflow-3-databricks-on-aws-260d0089.md)
