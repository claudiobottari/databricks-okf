---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0d263cb6a9efd10d39b7288a1b4e06d374478b130f170a6821e9a280a131ab4
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-model-artifact-storage
    - M3MAS
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
title: MLflow 3 Model Artifact Storage
description: Change in storage location for model artifacts from run-based paths to model-based paths under experiments.
tags:
  - mlflow
  - storage
  - databricks
timestamp: "2026-06-19T10:45:34.487Z"
---

# MLflow 3 Model Artifact Storage

**MLflow 3 Model Artifact Storage** refers to the new storage location for model artifacts introduced in MLflow 3. In MLflow 3, model artifacts are no longer stored under a run’s artifact path; instead they are placed under a dedicated model artifact path that is tied to the model itself rather than to any individual run. This change supports the concept of a `LoggedModel` — a first-class object that tracks a model’s lifecycle across multiple training and evaluation runs. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Storage Location Comparison

The following directory structures illustrate the difference between MLflow 2.x and MLflow 3:

```text
# MLflow 2.x
experiments/
  └── <experiment_id>/
    └── <run_id>/
      └── artifacts/
        └── ... # model artifacts are stored here

# MLflow 3
experiments/
  └── <experiment_id>/
    └── models/
      └── <model_id>/
        └── artifacts/
          └── ... # model artifacts are stored here
```

^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

In MLflow 2.x, model artifacts were nested under the run’s artifact directory. In MLflow 3, they are located under `experiments/<experiment_id>/models/<model_id>/artifacts/`, which decouples the artifacts from any single run and enables a model-centric view of the development lifecycle. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Model URI Format

Because artifacts are now stored under the model path, the URI used to reference a model has also changed:

- **MLflow 2.x**: `runs:/<run_id>/<artifact_path>`
- **MLflow 3**: `models:/<model_id>`

The new URI format is returned by `mlflow.<model-flavor>.log_model` and can also be constructed manually if only the model ID is known. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Recommended Loading Practice

To avoid compatibility issues, Databricks recommends loading models using `mlflow.<model-flavor>.load_model` with the model URI of the form `models:/<model_id>`. This URI is the standard identifier for a logged model in MLflow 3 and ensures that the correct artifact path is resolved. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Relation to LoggedModel

The shift in artifact storage is one of the key enablers of the `LoggedModel` concept introduced in MLflow 3. A `LoggedModel` is a dedicated object that captures metrics, parameters, and traces across different phases of development (training, evaluation) and across environments (development, staging, production). When a `LoggedModel` is promoted to Unity Catalog as a Model Version, all performance data from the original `LoggedModel` becomes visible on the UC Model Version page. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 for Models](/concepts/mlflow-3-for-models.md) — Overview of all new features in MLflow 3 for traditional ML and deep learning.
- [LoggedModel](/concepts/loggedmodel.md) — The new first-class model object that tracks lifecycle and performance across runs.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — How models are registered and managed, now defaulting to Unity Catalog.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where registered model versions reside.

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
