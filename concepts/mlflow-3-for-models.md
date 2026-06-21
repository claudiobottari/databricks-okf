---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ab9c8b37be277a19f345f0bd1f42b20c06186c6f249e353a0a15378b0c052fa
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-for-models
    - M3FM
    - MLflow Models
    - MLflow models
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
title: MLflow 3 for Models
description: State-of-the-art experiment tracking, performance evaluation, and production management for traditional machine learning and deep learning models on Databricks.
tags:
  - machine-learning
  - mlflow
  - databricks
timestamp: "2026-06-19T10:45:15.112Z"
---

# MLflow 3 for Models

**MLflow 3 for Models** is the latest generation of MLflow on Databricks, delivering state-of-the-art experiment tracking, performance evaluation, and production management for traditional machine learning and deep learning models. It introduces significant new capabilities while preserving core tracking concepts, making migration from MLflow 2.x straightforward. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## What is MLflow 3 for Models?

MLflow 3 for Models builds on the foundation of MLflow 2.x and adds:

- **Centralized model tracking** across all environments, from interactive notebook queries to production batch or real-time serving deployments. A dedicated model tracking UI is available. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Unified metrics and parameters** visible on the model version page in [Unity Catalog](/concepts/unity-catalog.md) and accessible via the REST API, consolidating data from all workspaces and experiments. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Orchestrated evaluation and deployment workflows** using Unity Catalog, with comprehensive status logs for each model version. Deployment jobs can include staged rollout and metrics collection. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

These capabilities simplify and streamline model development, evaluation, and production deployment. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Logged Models

A key new concept in MLflow 3 is the **[LoggedModel](/concepts/loggedmodel.md)**. For deep learning and traditional ML models, a `LoggedModel` elevates the model produced by a training run to a dedicated object that tracks the model lifecycle across different training and evaluation runs. `LoggedModels` capture metrics, parameters, and traces across phases of development (training and evaluation) and across environments (development, staging, production). When a `LoggedModel` is promoted to Unity Catalog as a Model Version, all performance data from the original `LoggedModel` becomes visible on the Unity Catalog Model Version page, providing cross-workspace and cross-experiment visibility. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Deployment Jobs

MLflow 3 introduces **deployment jobs**, which use [Lakeflow Jobs](/concepts/lakeflow-jobs.md) to manage the model lifecycle, including steps such as evaluation, approval, and deployment. These model workflows are governed by Unity Catalog, and all events are saved to an activity log on the model version page in Unity Catalog. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## How MLflow 3 for Models Differs from MLflow 2

### Logging Models

In MLflow 2.x, the `artifact_path` parameter was used when logging models, and a run had to be active. In MLflow 3, use the `name` parameter instead (which allows searching the model by name); `artifact_path` is deprecated but still supported. Additionally, MLflow 3 no longer requires an active run — you can log a model directly. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Model Artifacts

Model artifact storage changed. In MLflow 2.x, artifacts were stored under the run's artifact path (`experiments/<experiment_id>/<run_id>/artifacts/...`). In MLflow 3, they are stored under the model's artifact path (`experiments/<experiment_id>/models/<model_id>/artifacts/...`). Databricks recommends loading models with `mlflow.<model-flavor>.load_model` using the model URI returned by `log_model` (format `models:/<model_id>`) instead of the old `runs:/<run_id>/<artifact_path>` format. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Model Registry

In MLflow 3, the default registry URI is `databricks-uc`, which uses the [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md). Registered model names must follow the three-level format `<catalog>.<schema>.<model>`. For workspaces with Unity Catalog enabled and a configured default catalog, you can also use just `<model>` and the default catalog/schema will be inferred. If your default catalog is not in Unity Catalog, you must specify the full three-level name. Databricks recommends using the Unity Catalog Model Registry. To continue using the legacy Workspace Model Registry, set the registry URI to `databricks` via `mlflow.set_registry_uri("databricks")`, the `MLFLOW_REGISTRY_URI` environment variable, or init scripts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Other Important Changes

- MLflow 3 clients can load all runs, models, and traces logged with MLflow 2.x clients, but the reverse is not guaranteed — MLflow 3–logged items may not load in older 2.x clients. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- The `mlflow.evaluate` API has been deprecated. Use `mlflow.models.evaluate` for traditional ML/deep learning models (full compatibility), and `mlflow.genai.evaluate` for LLM/GenAI applications. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- The `run_uuid` attribute has been removed from `RunInfo` — use `run_id` instead. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Migrating from MLflow 2.x

Migration is straightforward with minimal code changes. Core concepts of experiments, runs, parameters, tags, and metrics remain unchanged. The main adjustments are:

- Replace `artifact_path` with `name` in `log_model` calls.
- Update model loading URIs from `runs:/` to `models:/`.
- Ensure the registry URI is set appropriately (defaults to `databricks-uc`).

See the [Migration from MLflow 2.x](/concepts/migrating-from-mlflow-2x-to-mlflow-3.md) guide for detailed steps.

## Installation

To use MLflow 3, install `mlflow>=3.0` in your notebook. Run the following code each time the notebook is started:

```python
%pip install mlflow>=3.0 --upgrade
dbutils.library.restartPython()
```

^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Limitations

Spark model logging (`mlflow.spark.log_model`) continues to work in MLflow 3 but does not use the new `LoggedModel` concept. Models logged with Spark model logging continue to use MLflow 2.x runs and run artifacts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Example Notebooks

The following pages include example notebooks:

- [MLflow 3 traditional ML workflow](/concepts/mlflow-3-traditional-ml-workflow.md)
- [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md)

## Next Steps

To learn more about MLflow 3 for Models, see:

- [Track and compare models using MLflow Logged Models](/concepts/mlflow-loggedmodel.md)
- Model Registry improvements with MLflow 3
- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md)

## Related Concepts

- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [LoggedModel](/concepts/loggedmodel.md)
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md)

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
