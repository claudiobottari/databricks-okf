---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9f906f85b97771933835ff9aa281dcaac60bc485ae341d73e06b62f3aea0852
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-model-registry-with-unity-catalog
    - M3MRWUC
    - Model Registry with Unity Catalog
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
title: MLflow 3 Model Registry with Unity Catalog
description: Default registry URI in MLflow 3 is now databricks-uc, using Unity Catalog for model lifecycle management with three-level naming.
tags:
  - mlflow
  - unity-catalog
  - model-registry
timestamp: "2026-06-19T10:45:38.122Z"
---

# MLflow 3 Model Registry with Unity Catalog

**MLflow 3 Model Registry with Unity Catalog** is the default model registry backend in MLflow 3 on Databricks. It replaces the legacy Workspace Model Registry by storing registered models, versions, stage transitions, and deployment metadata within [Unity Catalog](/concepts/unity-catalog.md), enabling cross-workspace visibility and governance through the Unity Catalog data and AI management layer.^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Key Changes from MLflow 2.x

In MLflow 3, the default registry URI is `databricks-uc`, which means all model registry operations target Unity Catalog by default. This is a change from MLflow 2.x where the workspace-level registry was the default.^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Model Naming Convention

Registered model names in Unity Catalog follow the three-level naming format: `<catalog>.<schema>.<model>`. When calling APIs that require a registered model name — such as `mlflow.register_model` — you must use this fully qualified name.^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

If your workspace has Unity Catalog enabled **and** its [default catalog](https://docs.databricks.com/aws/en/catalogs/default) is set to a Unity Catalog catalog, you can omit the [Catalog and Schema](/concepts/catalog-and-schema.md) parts and use only `<model>`. The default [Catalog and Schema](/concepts/catalog-and-schema.md) will be inferred automatically (this matches the MLflow 2.x behavior).^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

However, if the workspace has Unity Catalog enabled but the default catalog is **not** configured to be in Unity Catalog, you must specify the full three-level catalog.schema.model name.^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Using the Unity Catalog Registry

Databricks recommends using the [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) for managing the lifecycle of your models. The Unity Catalog registry provides:

- A consolidated model version page showing metrics, parameters, and traces from multiple runs across different experiments and workspaces.^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- Governance and lineage through Unity Catalog’s RBAC and audit capabilities.
- Integration with [MLflow 3 LoggedModels](/concepts/mlflow-3-loggedmodel.md) and [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md).

## Falling Back to the Legacy Workspace Model Registry

If you need to continue using the [Workspace Model Registry (legacy)](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry), you must explicitly set the registry URI to `databricks`. You can do this by:^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

- Using `mlflow.set_registry_uri("databricks")` in your code.
- Setting the environment variable `MLFLOW_REGISTRY_URI` to `"databricks"`.
- For cluster-level configuration, set the environment variable using [init scripts](https://docs.databricks.com/aws/en/init-scripts/).

## Benefits

The Unity Catalog-backed Model Registry enables centralized tracking of model performance from development through production. Model version pages display evaluation metrics from all training and evaluation runs, even across different workspaces and experiments, making it easier to compare and promote the best model versions.^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Related Concepts

- [MLflow 3](/concepts/mlflow-3.md) — Overview of MLflow 3 features for traditional ML and GenAI.
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance layer for data and AI assets.
- [LoggedModel](/concepts/loggedmodel.md) — The new MLflow 3 object that captures metrics across training and evaluation.
- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md) — Lakeflow-based workflows for model promotion and deployment.
- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The legacy, workspace-scoped registry that can be used as a fallback.
- Model version — A specific iteration of a registered model, with metadata and stage.

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
