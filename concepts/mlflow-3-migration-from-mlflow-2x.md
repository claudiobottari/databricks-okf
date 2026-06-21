---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 76b0a3c2c084a9f9465f754809417eb02b12408a0bc3b1aab54b5ede08e90778
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-migration-from-mlflow-2x
    - M3MFM2
    - Migration from MLflow 2.x
    - migration guide from MLflow 2 Agent Evaluation
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
title: MLflow 3 Migration from MLflow 2.x
description: Key changes when migrating from MLflow 2.x to 3.0 including new log_model API, artifact storage location changes, default Unity Catalog registry, and deprecated APIs.
tags:
  - mlflow
  - migration
  - machine-learning
timestamp: "2026-06-19T19:01:25.725Z"
---

# MLflow 3 Migration from MLflow 2.x

**MLflow 3 Migration from MLflow 2.x** refers to the process of upgrading machine learning workflows from MLflow 2.x to MLflow 3 on Databricks. MLflow 3 introduces significant new capabilities while preserving core tracking concepts, making migration straightforward with minimal code changes in most cases. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Overview

MLflow 3 for models on Databricks delivers state-of-the-art experiment tracking, performance evaluation, and production management for machine learning models. The core concepts of experiments and runs, along with their metadata such as parameters, tags, and metrics, all remain the same between MLflow 2.x and 3.0. Migration should require minimal code changes in most cases. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

MLflow 3 introduces a new concept called `LoggedModel`, which elevates the model produced by a training run into a dedicated object that tracks the model lifecycle across different training and evaluation runs. `LoggedModels` capture metrics, parameters, and traces across phases of development (training and evaluation) and across environments (development, staging, and production). When a `LoggedModel` is promoted to Unity Catalog as a Model Version, all performance data becomes visible on the UC Model Version page. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

MLflow 3 also introduces deployment jobs, which use [Lakeflow Jobs](/concepts/lakeflow-jobs.md) to manage the model lifecycle including steps like evaluation, approval, and deployment. These model workflows are governed by Unity Catalog, and all events are saved to an activity log available on the model version page. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Key Differences and Migration Steps

### Logging Models

In MLflow 2.x, the `artifact_path` parameter is used when logging models, and a run must be active:

```python
with mlflow.start_run():
    mlflow.pyfunc.log_model(
        artifact_path="model",
        python_model=python_model,
        ...
    )
```

In MLflow 3, use `name` instead, which allows the model to later be searched by name. The `artifact_path` parameter is still supported but has been deprecated. Additionally, MLflow no longer requires a run to be active when logging a model — you can directly log a model without first starting a run. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=python_model,
    ...
)
```

### Model Artifacts

In MLflow 2.x, model artifacts are stored as run artifacts under the run's artifact path. In MLflow 3, model artifacts are stored in a different location, under the model's artifact path instead.

It is recommended to load models with `mlflow.<model-flavor>.load_model` using the model URI returned by `mlflow.<model-flavor>.log_model` to avoid any issues. This model URI is of the format `models:/<model_id>` (rather than `runs:/<run_id>/<artifact_path>` as in MLflow 2.x) and can also be constructed manually if only the model ID is available. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Model Registry

In MLflow 3, the default registry URI is now `databricks-uc`, meaning the [MLflow Model Registry](/concepts/mlflow-model-registry.md) in Unity Catalog will be used by default. The names of models registered in Unity Catalog are of the form `<catalog>.<schema>.<model>`. When calling APIs that require a registered model name, such as `mlflow.register_model`, this full three-level name is used. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

For workspaces with Unity Catalog enabled and a default catalog in Unity Catalog, you can use `<model>` as the name and the default [Catalog and Schema](/concepts/catalog-and-schema.md) will be inferred, matching MLflow 2.x behavior. Databricks recommends using the MLflow Model Registry in Unity Catalog for managing model lifecycle. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

If you want to continue using the [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md), use one of the following methods to set the registry URI to `databricks`:

- Use `mlflow.set_registry_uri("databricks")`
- Set the environment variable `MLFLOW_REGISTRY_URI`
- Use init scripts to set the environment variable at scale (requires all-purpose compute)

^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Other Important Changes

- **Backward compatibility**: MLflow 3 clients can load all runs, models, and traces logged with MLflow 2.x clients. However, models and traces logged with MLflow 3 clients may not be loadable with older 2.x client versions. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Deprecated APIs**: The `mlflow.evaluate` API has been deprecated. For traditional ML or deep learning models, use `mlflow.models.evaluate` which maintains full compatibility. For LLMs or GenAI applications, use `mlflow.genai.evaluate` instead. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Removed attributes**: The `run_uuid` attribute has been removed from the `RunInfo` object. Use `run_id` instead. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Installation

To use MLflow 3, update the package to version 3.0 or higher. The following lines must be executed each time a notebook is run: ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

```python
%pip install mlflow>=3.0 --upgrade
dbutils.library.restartPython()
```

## Limitation

Spark model logging (`mlflow.spark.log_model`) continues to work in MLflow 3 but does not use the new `LoggedModel` concept. Models logged using Spark model logging continue to use MLflow 2.x runs and run artifacts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Related Concepts

- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) — The new first-class model object in MLflow 3
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Unity Catalog-based model lifecycle management
- [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md) — [Lakeflow Jobs](/concepts/lakeflow-jobs.md) for model lifecycle orchestration
- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) — MLflow 3 features for GenAI application development
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and management layer for ML assets

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
