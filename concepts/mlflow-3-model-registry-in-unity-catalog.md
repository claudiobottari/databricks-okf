---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47dcaddaa6d312f1f75071525567525f17cf384bb4507d96a77caf1b104370d6
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-model-registry-in-unity-catalog
    - M3MRIUC
    - mlflow-3-model-registry-with-unity-catalog
    - M3MRWUC
    - Model Registry with Unity Catalog
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
title: MLflow 3 Model Registry in Unity Catalog
description: MLflow 3 defaults to the Unity Catalog-backed Model Registry (databricks-uc) with three-level model naming (<catalog>.<schema>.<model>) and inferred defaults for Unity Catalog workspaces.
tags:
  - mlflow
  - unity-catalog
  - model-registry
timestamp: "2026-06-19T19:00:34.814Z"
---

# MLflow 3 Model Registry in Unity Catalog

**MLflow 3 Model Registry in Unity Catalog** is the default model registry backend for MLflow 3 on Databricks, providing centralized model lifecycle management with Unity Catalog integration. It replaces the legacy Workspace Model Registry as the recommended approach for managing machine learning model versions, deployments, and governance.

## Default Registry URI

In MLflow 3, the default registry URI is now `databricks-uc`, which automatically routes all model registry operations to Unity Catalog. This means that when you call APIs such as `mlflow.register_model`, the system uses the MLflow Model Registry in Unity Catalog by default. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Model Naming Convention

Models registered in Unity Catalog follow a three-level naming convention: `<catalog>.<schema>.<model>`. When calling APIs that require a registered model name, such as `mlflow.register_model`, you must use this full three-level name unless your workspace has Unity Catalog enabled and its default catalog is configured within Unity Catalog. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

For workspaces where Unity Catalog is enabled and the default catalog is set to a Unity Catalog location, you can use the shorthand `<model>` name, and the default [Catalog and Schema](/concepts/catalog-and-schema.md) will be inferred automatically — this is consistent with MLflow 2.x behavior. However, if your workspace has Unity Catalog enabled but the default catalog is not configured to be in Unity Catalog, the full three-level name is required. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Key Capabilities

The Model Registry in Unity Catalog provides several enhanced capabilities in MLflow 3:

- **Cross-workspace visibility**: Model metrics, parameters, and traces are visible from the model version page in Unity Catalog across all workspaces and experiments. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Integration with LoggedModels**: When a [LoggedModel](/concepts/loggedmodel.md) is promoted to Unity Catalog as a model version, all performance data from the original LoggedModel becomes visible on the Unity Catalog model version page. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Deployment job orchestration**: [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md) use [Lakeflow Jobs](/concepts/lakeflow-jobs.md) to manage the model lifecycle, including evaluation, approval, and deployment steps, all governed by Unity Catalog. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Activity logging**: All deployment events are saved to an activity log available on the model version page in Unity Catalog, providing comprehensive audit trails. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Migration from MLflow 2.x

MLflow 3 preserves the core concepts of experiments and runs, but changes how model registry operations work:

- The registry URI is now `databricks-uc` by default, whereas MLflow 2.x used `databricks` for the Workspace Model Registry. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- Model names in API calls must use the three-level Unity Catalog naming convention when the default catalog is not in Unity Catalog. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Using the Legacy Workspace Model Registry

If you need to continue using the [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md) instead of Unity Catalog, you can revert to the old behavior using one of the following methods:

- Use `mlflow.set_registry_uri("databricks")` programmatically.
- Set the environment variable `MLFLOW_REGISTRY_URI` to `databricks`.
- To configure this at scale, use init scripts with all-purpose compute.

Databricks recommends using the MLflow Model Registry in Unity Catalog for managing model lifecycles. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Related Concepts

- [LoggedModel](/concepts/loggedmodel.md) — Core MLflow 3 concept for tracking model lifecycle across runs and environments.
- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md) — Orchestrated workflows for model evaluation, approval, and deployment.
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance and catalog system for model registry.
- [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md) — The older, non-Unity-Catalog model registry.
- [MLflow experiments](/concepts/mlflow-experiment.md) — Organizational units for MLflow runs.

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
