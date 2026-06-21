---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44756d4a0ea2ec45d926093113808d718ac19bfd748f2decb047f3dea2902065
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-artifact-storage-architecture
    - M3ASA
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
title: MLflow 3 Artifact Storage Architecture
description: In MLflow 3, model artifacts are stored under a dedicated model artifact path (models/<model_id>/artifacts/) rather than under the run's artifact path, changing how models are loaded and referenced.
tags:
  - mlflow
  - architecture
  - storage
timestamp: "2026-06-19T19:00:31.807Z"
---

# MLflow 3 Artifact Storage Architecture

**MLflow 3 Artifact Storage Architecture** refers to the change in how model artifacts are stored and referenced in MLflow 3 compared to MLflow 2.x. In MLflow 2.x, model artifacts were stored under the run’s artifact path, making them subordinate to a specific run. In MLflow 3, models become first-class citizens through the [MLflow 3 Logged Model](/concepts/mlflow-3-loggedmodel.md) concept, and their artifacts are stored under a dedicated model‑level path. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Storage Hierarchy

In MLflow 2.x, the artifact directory for a model logged inside a run was:

```text
experiments/
  └── <experiment_id>/
    └── <run_id>/
      └── artifacts/
        └── ...   # model artifacts stored here
```

In MLflow 3, artifacts are stored under a separate path that is tied to the model identity rather than a specific run:

```text
experiments/
  └── <experiment_id>/
    └── models/
      └── <model_id>/
        └── artifacts/
          └── ...   # model artifacts stored here
```

^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

This change allows a model’s artifacts to persist independently of any single training run and to be updated or evaluated across multiple runs. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Model URI

Because artifacts live under a model‑specific path, the recommended way to load a model in MLflow 3 is to use the model URI returned by `mlflow.<flavor>.log_model`. This URI uses the format `models:/<model_id>` instead of the MLflow 2.x format `runs:/<run_id>/<artifact_path>`. If only the model ID is known, the `models:/` URI can be constructed manually. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## LoggedModel and Artifact Lifecycle

The artifact storage shift is enabled by the introduction of `LoggedModels`. A `LoggedModel` is a dedicated object that tracks the model lifecycle across development, evaluation, and production. Because the model is no longer a subordinate of a single run, its artifacts remain accessible even when the model is promoted to [Unity Catalog](/concepts/unity-catalog.md) as a Model Version. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Limitation: Spark Model Logging

Spark model logging (`mlflow.spark.log_model`) continues to work in MLflow 3 but **does not** use the new `LoggedModel` architecture. Artifacts for Spark‑logged models are still stored under the run’s artifact path (MLflow 2.x style). ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 Logged Model](/concepts/mlflow-3-loggedmodel.md)
- [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md)
- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md)
- Run Artifact Path (MLflow 2.x)

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
