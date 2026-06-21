---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03e14ea1d2743ae2ce207a2eb94e8243f4bfa6fa3d3371241f0329a9c0d76d64
  pageDirectory: concepts
  sources:
    - log-load-and-register-mlflow-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-integration-for-mlflow-models
    - UCIFMM
  citations:
    - file: log-load-and-register-mlflow-models-databricks-on-aws.md
title: Unity Catalog Integration for MLflow Models
description: Saving, registering, and managing MLflow models within Unity Catalog volumes and the Unity Catalog model registry, including viewing parameters and metrics across experiments and workspaces.
tags:
  - mlflow
  - unity-catalog
  - model-management
timestamp: "2026-06-19T19:16:35.549Z"
---

# Unity Catalog Integration for MLflow Models

**Unity Catalog Integration for MLflow Models** refers to the capability to register, manage, and serve MLflow models using Unity Catalog as the centralized governance and metadata layer. This integration enables organizations to manage the full lifecycle of MLflow Models within Unity Catalog, providing unified governance, lineage tracking, and access control across workspaces.

## Model Registration in Unity Catalog

MLflow models can be registered in the MLflow Model Registry, which when used with Unity Catalog becomes a centralized model store that provides a UI and set of APIs for managing the complete lifecycle of MLflow Models. When models created with MLflow 3 are registered to the Unity Catalog model registry, you can view data such as parameters and metrics in one central location, across all experiments and workspaces. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

To register a model using the API in MLflow 3, use the following command:

```python
mlflow.register_model("models:/{model_id}", "{registered_model_name}")
```

For MLflow 2.x, a different syntax is used. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Saving Models to Unity Catalog Volumes

Models can be saved to Unity Catalog volumes using `mlflow.<model-type>.save_model()`. The `modelpath` parameter must be a Unity Catalog volumes path. For example, to save a model to a volume location, use a path like `/dbfs/Volumes/catalog_name/schema_name/volume_name/my_project_models/`: ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

```python
modelpath = "/dbfs/Volumes/catalog_name/schema_name/volume_name/my_project_models/model-%f-%f" % (alpha, l1_ratio)
mlflow.sklearn.save_model(lr, modelpath)
```

## Loading Models from Unity Catalog

Models registered in Unity Catalog can be loaded for inference or further development using `mlflow.<model-type>.load_model()`. Supported model paths include Unity Catalog volumes paths (such as `dbfs:/Volumes/catalog_name/schema_name/volume_name/{path_to_artifact_root}/{model_path}`), as well as other standard MLflow model referencing formats. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

For Python MLflow models, you can also use `mlflow.pyfunc.load_model()` to load the model as a generic Python function: ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

```python
model = mlflow.pyfunc.load_model(model_path)
model.predict(model_input)
```

## Downloading Model Artifacts

Logged model artifacts — including model files, plots, and metrics — can be downloaded for registered models using various APIs. When using Unity Catalog, set the registry URI to `databricks-uc` before downloading: ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

```python
mlflow.set_registry_uri("databricks-uc")
mlflow.artifacts.download_artifacts(f"models:/{model_name}/{model_version}")
```

## Model Deployment and Serving

Models registered in the Unity Catalog model registry can be deployed using [Model Serving](/concepts/model-serving.md) to host them as REST endpoints. These endpoints are updated automatically based on the availability of model versions. Prior to deployment, it is recommended to validate that the model can be served using `mlflow.models.predict`. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Model Registry Improvements with MLflow 3

MLflow 3 introduces significant enhancements to MLflow models by providing a new, dedicated `LoggedModel` object with its own metadata such as metrics and parameters. When these models are registered to the Unity Catalog model registry, you can view this data in one central location, across all experiments and workspaces. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Related Concepts

- MLflow Model
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- [MLflow 3](/concepts/mlflow-3.md)
- Unity Catalog volumes
- [Workspace Model Registry](/concepts/workspace-model-registry.md)
- Model lifecycle management
- [Databricks Autologging](/concepts/databricks-autologging.md)

## Sources

- log-load-and-register-mlflow-models-databricks-on-aws.md

# Citations

1. [log-load-and-register-mlflow-models-databricks-on-aws.md](/references/log-load-and-register-mlflow-models-databricks-on-aws-dc2ad486.md)
