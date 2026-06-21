---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca4400bdafb163142c907e08450bc4cb1e496b18e2f2460c342f2aed8aaa9413
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-registration-methods
    - MRM
    - Model|registered models
  citations:
    - file: manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
title: Model Registration Methods
description: "Multiple approaches to register models in the Workspace Model Registry: via the UI from MLflow runs, programmatically via mlflow.log_model() during experiments, via mlflow.register_model() post-experiment, and via the MLflow Client API create_registered_model()."
tags:
  - model-registration
  - mlflow
  - api
  - databricks
timestamp: "2026-06-19T19:25:21.892Z"
---

# Model Registration Methods

**Model Registration Methods** refer to the techniques for creating and registering machine learning models in the [Workspace Model Registry](/concepts/workspace-model-registry.md) (legacy) on Databricks. These methods allow data scientists and ML engineers to add models to a central registry, enabling versioning, stage transitions, and lifecycle management.

## Overview

You can register a model either during an MLflow experiment run or after the run completes. The registration copies the model artifacts into a secure location managed by the Workspace Model Registry and creates a new model version. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

If your workspace uses Unity Catalog as the default catalog and you are on Databricks Runtime 13.3 LTS or above (or using [MLflow 3](/concepts/mlflow-3.md)), models are automatically created in and loaded from the workspace default catalog, with no configuration required. To explicitly target the Workspace Model Registry in that case, call `mlflow.set_registry_uri("databricks")`. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## UI Registration Methods

### Register an Existing Logged Model from a Notebook

1. Open the [MLflow Run](/concepts/mlflow-run.md) containing the model from the notebook’s Experiment Runs sidebar.
2. In the **Artifacts** section, click the model directory (e.g., `xxx-model`).
3. Click the **Register Model** button.
4. In the dialog, either select **Create New Model** and provide a name, or select an existing model.
5. Click **Register**. A new model version is created and a link to the registered model version appears. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

### Create a New Empty Model and Assign a Logged Model

1. On the registered models page, click **Create Model**, enter a name, and click **Create**.
2. Follow the same steps as above to register a logged model, selecting the newly created model name from the drop-down menu.
3. This creates a new registered model with a first version. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## API Registration Methods

### Register a Model During an Experiment Run

Use `mlflow.<model-flavor>.log_model(...)` with the `registered_model_name` parameter. If a registered model with that name does not exist, it creates a new model and version 1; otherwise, it creates a new version. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

```python
with mlflow.start_run(run_name=<run-name>) as run:
    ...
    mlflow.<model-flavor>.log_model(
        <model-flavor>=<model>,
        artifact_path="<model-path>",
        registered_model_name="<model-name>"
    )
```

### Register a Model After Runs Complete

Use `mlflow.register_model()` with the run ID and model path (the `mlruns:URI`). This also creates a new model or version. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

```python
result = mlflow.register_model("runs:<model-path>", "<model-name>")
```

### Create a New Registered Model (No Version)

Use the MLflow Client API `create_registered_model()` to create an empty registered model. Throws `MLflowException` if the model name already exists. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

```python
client = MlflowClient()
result = client.create_registered_model("<model-name>")
```

### Terraform

You can also register a model using the Databricks Terraform provider and the `databricks_mlflow_model` resource. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Quota Limits

The Workspace Model Registry imposes quota limits on the total number of registered models and model versions per workspace. If you exceed these limits, Databricks recommends deleting unused models or adjusting your registration and retention strategy. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry](/concepts/workspace-model-registry.md)
- [Unity Catalog Models](/concepts/unity-catalog-for-ml-models.md)
- Model Versioning
- [Stage Transitions](/concepts/model-versioning-and-stage-transitions.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- Databricks Terraform provider

## Sources

- manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md](/references/manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws-666e92b6.md)
