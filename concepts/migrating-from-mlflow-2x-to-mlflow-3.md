---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3018c7b5e7baf3774b1202473a7d6055badd15ef11800f7db6618ee1e831b656
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migrating-from-mlflow-2x-to-mlflow-3
    - MFM2TM3
    - Migration from MLflow 2.x
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
    - file: |-
        get-started-with-mlflow-3-for-models-databricks-on-aws.md

        ### Deployment Jobs

        MLflow 3 introduces deployment jobs
    - file: which use Lakeflow Jobs to manage the model lifecycle including evaluation
    - file: approval
    - file: and deployment steps. These model workflows are governed by Unity Catalog
    - file: |-
        and all events are saved to an activity log available on the model version page in Unity Catalog. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md

        ## Limitation

        Spark model logging (`mlflow.spark.log_model`) continues to work in MLflow 3 but does not use the new `LoggedModel` concept. Models logged using Spark model logging continue to use MLflow 2.x runs and run artifacts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md

        ## Related Concepts

        - [[MLflow 3 for Models
title: Migrating from MLflow 2.x to MLflow 3
description: Key differences and migration guide between MLflow 2.x and 3.0, including changes to model logging, artifact storage, and model registry.
tags:
  - mlflow
  - migration
  - databricks
timestamp: "2026-06-19T10:45:17.876Z"
---

# Migrating from MLflow 2.x to MLflow 3

**Migrating from MLflow 2.x to MLflow 3** is a straightforward process that requires minimal code changes in most cases. MLflow 3 preserves core tracking concepts from MLflow 2.x (experiments, runs, parameters, tags, and metrics) while introducing significant new capabilities for model lifecycle management. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Overview

MLflow 3 for models on Databricks delivers state-of-the-art experiment tracking, performance evaluation, and production management. The migration is designed to be seamless — core concepts from MLflow 2.x remain unchanged, making the transition quick and simple. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Key Changes to Be Aware Of

### Logging Models: `name` replaces `artifact_path`

In MLflow 2.x, the `artifact_path` parameter was required when logging models:

```python
with mlflow.start_run():
    mlflow.pyfunc.log_model(
        artifact_path="model",
        python_model=python_model,
        ...
    )
```

In MLflow 3, use the `name` parameter instead, which allows the model to later be searched by name. The `artifact_path` parameter is still supported but has been deprecated. Additionally, MLflow 3 no longer requires a run to be active when logging a model — models have become first-class citizens and can be logged directly without first starting a run. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=python_model,
    ...
)
```

### Model Artifacts Location

In MLflow 2.x, model artifacts were stored as run artifacts under the run's artifact path. In MLflow 3, model artifacts are stored under the model's own artifact path:

```
# MLflow 2.x
experiments/
  └── <experiment_id>/
    └── <run_id>/
      └── artifacts/
        └── ... 

# MLflow 3
experiments/
  └── <experiment_id>/
    └── models/
      └── <model_id>/
        └── artifacts/
          └── ...
```

Databricks recommends loading models with `mlflow.<model-flavor>.load_model` using the model URI returned by `mlflow.<model-flavor>.log_model`. This model URI uses the format `models:/<model_id>` rather than `runs:/<run_id>/<artifact_path>` as in MLflow 2.x. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Model Registry: Default URI Changes to Unity Catalog

In MLflow 3, the default registry URI is now `databricks-uc`, meaning the [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) will be used. The names of models registered in Unity Catalog take the form `<catalog>.<schema>.<model>`. When calling APIs that require a registered model name (such as `mlflow.register_model`), this full three-level name is used. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

For workspaces with Unity Catalog enabled and whose default catalog is in Unity Catalog, you can still use `<model>` as the name and the default [Catalog and Schema](/concepts/catalog-and-schema.md) will be inferred (no change from MLflow 2.x). If your workspace has Unity Catalog enabled but its default catalog is not configured to be in Unity Catalog, you must specify the full three-level name. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

Databricks recommends using the MLflow Model Registry in Unity Catalog for managing model lifecycles. To continue using the [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md), set the registry URI to `databricks` using `mlflow.set_registry_uri("databricks")`, the `MLFLOW_REGISTRY_URI` environment variable, or an init script for at-scale configuration. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Deprecated and Removed APIs

- **`mlflow.evaluate` API**: This has been deprecated. For traditional ML or deep learning models, use `mlflow.models.evaluate` which maintains full compatibility with the original API. For LLMs or GenAI applications, use the `mlflow.genai.evaluate` API instead. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **`run_uuid` attribute**: Removed from the `RunInfo` object. Use `run_id` instead in your code. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Backward Compatibility

MLflow 3 clients can load all runs, models, and traces logged with MLflow 2.x clients. However, the reverse is not necessarily true — models and traces logged with MLflow 3 clients may not be loadable with older 2.x client versions. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Installation

To use MLflow 3, update the package to version 3.0 or higher. The following code must be executed each time a notebook is run:

```python
%pip install mlflow>=3.0 --upgrade
dbutils.library.restartPython()
```

^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## New Features in MLflow 3

### Logged Models

MLflow 3 introduces the concept of a `LoggedModel`, which elevates the model produced by a training run to a dedicated object that tracks the model lifecycle across different training and evaluation runs. `LoggedModels` capture metrics, parameters, and traces across phases of development (training and evaluation) and across environments (development, staging, production). When promoted to Unity Catalog as a Model Version, all performance data from the original `LoggedModel` becomes visible on the UC Model Version page across all workspaces and experiments. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md

### Deployment Jobs

MLflow 3 introduces deployment jobs, which use Lakeflow Jobs to manage the model lifecycle including evaluation, approval, and deployment steps. These model workflows are governed by Unity Catalog, and all events are saved to an activity log available on the model version page in Unity Catalog. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md

## Limitation

Spark model logging (`mlflow.spark.log_model`) continues to work in MLflow 3 but does not use the new `LoggedModel` concept. Models logged using Spark model logging continue to use MLflow 2.x runs and run artifacts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md

## Related Concepts

- [MLflow 3 for Models](/concepts/mlflow-3-for-models.md) — The new model tracking and deployment system
- [Logged Models](/concepts/logged-models.md) — First-class model objects tracking lifecycle across environments
- [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) — The default registry for MLflow 3
- [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md) — Alternative registry for backward compatibility
- Deployment Jobs — Lakeflow-based model lifecycle management

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
2. get-started-with-mlflow-3-for-models-databricks-on-aws.md

### Deployment Jobs

MLflow 3 introduces deployment jobs
3. which use Lakeflow Jobs to manage the model lifecycle including evaluation
4. approval
5. and deployment steps. These model workflows are governed by Unity Catalog
6. and all events are saved to an activity log available on the model version page in Unity Catalog. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md

## Limitation

Spark model logging (`mlflow.spark.log_model`) continues to work in MLflow 3 but does not use the new `LoggedModel` concept. Models logged using Spark model logging continue to use MLflow 2.x runs and run artifacts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md

## Related Concepts

- [[MLflow 3 for Models
