---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7b06559b185e466ef751c4ffeb4cc79b7009695810dcd595a096d3f56b6ed4b
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-api-changes-and-deprecations
    - Deprecations and MLflow 3 API Changes
    - M3ACAD
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
title: MLflow 3 API Changes and Deprecations
description: Notable API changes in MLflow 3 including the deprecation of artifact_path (replaced by name), removal of run_uuid (use run_id), and deprecation of mlflow.evaluate in favor of mlflow.models.evaluate.
tags:
  - mlflow
  - api
  - deprecation
timestamp: "2026-06-19T19:00:44.283Z"
---

# MLflow 3 API Changes and Deprecations

**MLflow 3 API Changes and Deprecations** summarizes the modifications, removed features, and deprecated interfaces introduced in Databricks’ MLflow 3 for models. These changes affect how users log models, evaluate performance, access run metadata, and interact with the model registry. Understanding them is essential for a smooth migration from MLflow 2.x.

## Key API Changes

### Model Logging: `artifact_path` → `name`

In MLflow 2.x, logging a model required the `artifact_path` parameter:

```python
with mlflow.start_run():
    mlflow.pyfunc.log_model(
        artifact_path="model",
        python_model=python_model,
    )
```

In MLflow 3, use the `name` parameter instead. The `artifact_path` parameter is still supported but **deprecated**. Additionally, MLflow 3 no longer requires an active run when logging a model — models are first-class citizens and can be logged directly without starting a run:

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=python_model,
)
```

^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Model Artifact Storage Location

Model artifacts are stored in a different location in MLflow 3. Instead of being placed under the run’s artifact path, they are stored under the model’s own artifact path:

- **MLflow 2.x:** `experiments/<experiment_id>/<run_id>/artifacts/...`
- **MLflow 3:** `experiments/<experiment_id>/models/<model_id>/artifacts/...`

Databricks recommends loading models using the model URI returned by `log_model` (`models:/<model_id>`) rather than the old `runs:/<run_id>/<artifact_path>` pattern. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Model Registry URI Default

The default registry URI in MLflow 3 is now `databricks-uc`, meaning the [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) is used automatically. Registered model names must be of the form `<catalog>.<schema>.<model>`. For workspaces with Unity Catalog enabled and a Unity Catalog default catalog, the short form `<model>` is still accepted (the default [Catalog and Schema](/concepts/catalog-and-schema.md) are inferred). If the default catalog is not in Unity Catalog, the full three-level name is required. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

To continue using the [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md), users must explicitly set the registry URI to `databricks` via `mlflow.set_registry_uri("databricks")`, the environment variable `MLFLOW_REGISTRY_URI`, or init scripts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### `RunInfo`: `run_uuid` Removed

The `run_uuid` attribute has been removed from the `RunInfo` object. Use `run_id` instead in all code that previously referenced `run_uuid`. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Deprecations

### `mlflow.evaluate` API

The `mlflow.evaluate` API is **deprecated**. For traditional machine learning or deep learning models, use `mlflow.models.evaluate`, which maintains full compatibility with the original API. For LLMs or GenAI applications, use `mlflow.genai.evaluate` instead. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Backward Compatibility Notes

- MLflow 3 clients can load all runs, models, and traces logged with MLflow 2.x clients. However, the reverse is **not** guaranteed — models and traces logged with MLflow 3 clients may not be loadable by older 2.x client versions. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- [Spark model logging](/concepts/mlflow-pyspark-ml-autologging.md) (`mlflow.spark.log_model`) continues to work in MLflow 3, but it does **not** use the new [LoggedModel](/concepts/loggedmodel.md) concept. Models logged via Spark continue to use MLflow 2.x runs and run artifacts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Related Concepts

- [LoggedModel](/concepts/loggedmodel.md) — The new first-class model object in MLflow 3
- [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md)
- [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md)
- mlflow.evaluate (deprecated)
- mlflow.models.evaluate
- [Track and compare models using MLflow Logged Models](/concepts/mlflow-loggedmodel.md)
- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md)

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
