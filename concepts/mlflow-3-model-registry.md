---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 870e372535509f7fe46549ec3b81d12601e4b4d4b2a72a0af8953dd10452dd7b
  pageDirectory: concepts
  sources:
    - model-registry-improvements-with-mlflow-3-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-model-registry
    - M3MR
  citations:
    - file: model-registry-improvements-with-mlflow-3-databricks-on-aws.md
title: MLflow 3 Model Registry
description: Enhanced model registry in MLflow 3 that exposes metrics and parameters for registered models, with unified cross-experiment and cross-workspace visibility.
tags:
  - machine-learning
  - mlflow
  - model-registry
timestamp: "2026-06-19T19:43:14.297Z"
---

# MLflow 3 Model Registry

The **MLflow 3 Model Registry** introduces significant enhancements to the [Unity Catalog](/concepts/unity-catalog.md) model registry, making it easier to discover model parameters, performance data, and associated traces across experiments and workspaces. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

## Key Improvements

### Unified Metrics and Parameters

When you register a `LoggedModel` to the Unity Catalog model registry, all of its metrics and parameters are automatically available in the model registry UI and through the API. This allows you to view model performance metrics across all [MLflow experiments](/concepts/mlflow-experiment.md) and workspaces on a single page, providing a centralized view of model performance. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### Traces Integration

The **Traces** panel on the model version page displays traces associated with the Model ID from multiple sources:

- Development and evaluation traces from `mlflow.evaluate()` runs
- Traces from online serving in endpoints

You can use the search box to filter traces and click on individual traces to view the full set of spans. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

## Related Concepts

- [MLflow LoggedModel](/concepts/mlflow-loggedmodel.md) — The model object that, when registered, makes metrics and parameters available in the registry
- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md) — Another new feature in MLflow 3
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system that hosts the enhanced model registry
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Where models are developed and evaluated before registration
- [Model Serving](/concepts/model-serving.md) — Online serving endpoints that generate traces visible in the registry

## Sources

- model-registry-improvements-with-mlflow-3-databricks-on-aws.md

# Citations

1. [model-registry-improvements-with-mlflow-3-databricks-on-aws.md](/references/model-registry-improvements-with-mlflow-3-databricks-on-aws-260d0089.md)
