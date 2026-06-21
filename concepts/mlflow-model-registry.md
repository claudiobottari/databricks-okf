---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea4cc33c92ad3526a0c186eb4aa3768a067419c972356aef38b961fe31f8cf59
  pageDirectory: concepts
  sources:
    - log-load-and-register-mlflow-models-databricks-on-aws.md
    - mlflow-api-reference-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-model-registry
    - MMR
    - MLflow Model Registration
    - MLflow model registration
    - MLflow Model Registry (Workspace)
    - Model Registry
    - Model registry
    - model registry
  citations:
    - file: log-load-and-register-mlflow-models-databricks-on-aws.md
    - file: mlflow-api-reference-databricks-on-aws.md
title: MLflow Model Registry
description: A centralized model store with UI and APIs for managing the full lifecycle of MLflow Models, including registration with Unity Catalog or Workspace Model Registry.
tags:
  - mlflow
  - model-registry
  - model-lifecycle
timestamp: "2026-06-19T19:16:08.179Z"
---

# MLflow Model Registry

The **MLflow Model Registry** is a centralized model store that provides a user interface (UI) and a set of APIs to manage the full lifecycle of MLflow Models. It allows teams to register, version, stage, and deploy machine learning models in a collaborative environment. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Capabilities

The Model Registry serves as a single source of truth for model artifacts. You can use it to track model versions, transition models between stages (such as Staging, Production, Archived), and manage model metadata alongside the experiment that produced them. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Registering a Model

To register a model using the MLflow API, call `mlflow.register_model()` with the model URI and the desired registered model name. For example: ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

```python
mlflow.register_model("models:/{model_id}", "{registered_model_name}")
```

The model URI can reference a model by its model ID (MLflow 3 only), a run-relative path, or a Unity Catalog volume path. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Integration with Unity Catalog

In Databricks, the Model Registry is available in two forms: **Unity Catalog model registry** and the **Workspace Model Registry (legacy)**. When you register models created with [MLflow 3](/concepts/mlflow-3.md) to the [Unity Catalog](/concepts/unity-catalog.md) model registry, you can view parameters and metrics in one central location, across all experiments and workspaces. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Legacy Workspace Model Registry

The Workspace Model Registry is a legacy option that operates within a single Databricks workspace. It provides the same core functionality of model versioning and staging, but does not offer the cross-workspace and governance features of Unity Catalog. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## MLflow 3 Enhancements

When models created with MLflow 3 are registered to the Unity Catalog model registry, additional metadata such as parameters and metrics are made available in a centralized view, enabling better model comparison and lifecycle management across experiments and workspaces. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## API Support

The Model Registry is also accessible through the open-source MLflow REST API. The Databricks Runtime for Machine Learning provides a managed version of the MLflow server that includes both experiment tracking and the Model Registry. ^[mlflow-api-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — The open-source platform for managing the machine learning lifecycle.
- MLflow Models — The packaging format used to store and load models.
- Managed MLflow Server
- [Model Serving](/concepts/model-serving.md) — Deploying registered models as REST endpoints.

## Sources

- log-load-and-register-mlflow-models-databricks-on-aws.md
- mlflow-api-reference-databricks-on-aws.md

# Citations

1. [log-load-and-register-mlflow-models-databricks-on-aws.md](/references/log-load-and-register-mlflow-models-databricks-on-aws-dc2ad486.md)
2. [mlflow-api-reference-databricks-on-aws.md](/references/mlflow-api-reference-databricks-on-aws-472f1a07.md)
