---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fad9bbf492ef39d842936a43736b4bc7fce55b65b97937604b65758735893a46
  pageDirectory: concepts
  sources:
    - log-load-and-register-mlflow-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-format
    - MMF
  citations:
    - file: log-load-and-register-mlflow-models-databricks-on-aws.md
title: MLflow Model Format
description: A standard format for packaging machine learning models for use across downstream tools such as batch inference on Spark or real-time REST API serving.
tags:
  - mlflow
  - model-packaging
  - machine-learning
timestamp: "2026-06-19T19:15:55.851Z"
---

<!-- SOURCE: log-load-and-register-mlflow-models-databricks-on-aws.md -->

# MLflow Model Format

The **MLflow Model Format** is a standard convention for packaging machine learning models so they can be used across a variety of downstream tools, including batch inference on Apache Spark, real‑time serving through a REST API, and streaming inference. The format defines a directory structure and metadata files that allow a model to be saved in one or more *flavors* – each flavor represents a way the model can be interpreted by a specific serving or inference platform (for example, Python function, PyTorch, scikit‑learn). ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Format Structure

In addition to the serialized model artifact, every `log_model()` call automatically writes two environment specification files:

- **`requirements.txt`** – a pip‑compatible list of Python dependencies.
- **`conda.yaml`** – a Conda environment specification.

These files can be used to recreate the development environment when the model is loaded, using `virtualenv` (recommended) or `conda`. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

> **Note on Conda channels:** Models logged before MLflow v1.18 (Databricks Runtime 8.3 ML or earlier) used the `defaults` Anaconda channel by default. Starting with MLflow v1.18, the default channel changed to `conda‑forge`. Existing models that still reference the `defaults` channel may be affected by updated Anaconda licensing terms; you can inspect the `channels` key in the model’s `conda.yaml` to verify, and re‑register the model with a different channel if needed. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## MLflow 3 Enhancements

[MLflow 3](/concepts/mlflow-3.md) introduces a dedicated `LoggedModel` object with its own metadata such as metrics and parameters. This allows richer tracking and comparison of logged models across runs and workspaces, especially when registered in the [Unity Catalog](/concepts/unity-catalog.md) model registry. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Logging and Loading

### Logging a Model

Use `mlflow.<flavor>.log_model(model, ...)` to save a model to the [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) during a run.

### Loading a Model

Use `mlflow.<flavor>.load_model(model_path)` where `model_path` can be any of the following:

- A model ID path: `models:/{model_id}` (MLflow 3 only)
- A run‑relative path: `runs:/{run_id}/{model_path}`
- A Unity Catalog volumes path: `dbfs:/Volumes/...`
- An MLflow‑managed artifact storage path beginning with `dbfs:/databricks/mlflow-tracking/`
- A registered model path: `models:/{model_name}/{stage}`

For Python models, `mlflow.pyfunc.load_model()` loads the model as a generic Python function, making it suitable for scoring with `model.predict()`. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

Alternatively, you can export the model as a Spark UDF using `mlflow.pyfunc.spark_udf()` for batch or streaming inference on a Spark cluster. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Dependency Management

Starting with Databricks Runtime 10.5 ML, MLflow warns if there is a mismatch between the current environment and the model’s logged dependencies. In Databricks Runtime 11.0 ML and above, you can use `mlflow.pyfunc.get_model_dependencies()` to retrieve the dependency file and install it with `%pip install <file>`. When loading a model as a PySpark UDF, specify `env_manager="virtualenv"` to restore the model’s dependencies inside the UDF context without affecting the notebook environment. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Registration

Models can be registered in the [MLflow Model Registry](/concepts/mlflow-model-registry.md) (either workspace‑scoped or Unity Catalog‑scoped) to manage their lifecycle. The API call is:

- MLflow 3: `mlflow.register_model("models:/{model_id}", "{registered_model_name}")`
- MLflow 2.x: `mlflow.register_model("runs:/{run_id}/{model_path}", "{registered_model_name}")`

When models created with MLflow 3 are registered to Unity Catalog, parameters and metrics become visible across experiments and workspaces. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Saving to Unity Catalog Volumes

To save a model locally on Databricks, use `mlflow.<flavor>.save_model(model, model_path)` where `model_path` must be a Unity Catalog volumes path (e.g., `/dbfs/Volumes/catalog/schema/volume/...`). ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Downloading Model Artifacts

Logged model artifacts (model files, plots, metrics) can be downloaded for a registered model version using the Python API, Java API, or CLI. Example (Python):

```python
mlflow.set_registry_uri("databricks-uc")
mlflow.artifacts.download_artifacts(f"models:/{model_name}/{model_version}")
```

^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Deployment

Models registered in Unity Catalog can be deployed for online serving via [Model Serving](/concepts/model-serving.md), which automatically creates REST endpoints and updates them when new model versions become available. Before deployment, it is recommended to validate the model using `mlflow.models.predict()`. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- [Databricks Autologging](/concepts/databricks-autologging.md)
- [MLflow 3](/concepts/mlflow-3.md)

## Sources

- log-load-and-register-mlflow-models-databricks-on-aws.md

# Citations

1. [log-load-and-register-mlflow-models-databricks-on-aws.md](/references/log-load-and-register-mlflow-models-databricks-on-aws-dc2ad486.md)
