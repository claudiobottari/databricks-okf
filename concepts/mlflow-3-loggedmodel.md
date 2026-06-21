---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 514b620e5a5998c65112e8c07e835cdbd11e3c9dc55384468a2fdda0ac71ca60
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
    - log-load-and-register-mlflow-models-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-3-loggedmodel
    - M3L
    - MLflow 3 Logged Model
    - MLflow 3 LoggedModels
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
    - file: log-load-and-register-mlflow-models-databricks-on-aws.md
title: MLflow 3 LoggedModel
description: A new first-class object in MLflow 3 that elevates models from run artifacts to dedicated tracked entities, capturing metrics, parameters, and traces across multiple development phases and environments.
tags:
  - mlflow
  - machine-learning
  - model-management
timestamp: "2026-06-19T19:00:12.439Z"
---

## MLflow 3 LoggedModel

**MLflow 3 LoggedModel** is a new, dedicated first-class object introduced in MLflow 3 for deep learning and traditional machine learning models. It elevates the concept of a model produced by a training run, establishing it as a persistent entity that tracks the model lifecycle across different training and evaluation phases as well as across environments (development, staging, and production). ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Key Features

- **Dedicated metadata** – Each `LoggedModel` carries its own metrics, parameters, and traces, separate from the run that created it. This enables performance data to be carried forward when the model is promoted. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md, log-load-and-register-mlflow-models-databricks-on-aws.md]
- **Cross‑environment visibility** – When a `LoggedModel` is promoted to a Model Version in [Unity Catalog](/concepts/unity-catalog.md), all performance data from the original `LoggedModel` (metrics, parameters, traces) becomes visible on the Unity Catalog Model Version page, across all workspaces and experiments. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Model artifact isolation** – In MLflow 3, model artifacts are stored under the model’s own artifact path (`experiments/<experiment_id>/models/<model_id>/artifacts/`) rather than under the run’s artifact path. This change reinforces the model as an independent entity. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Using LoggedModel

#### Logging a model

In MLflow 3, you can log a model without an active run. The `artifact_path` parameter is deprecated in favor of `name`, which allows the model to be searched by name later. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="my_model",
    python_model=python_model,
    ...
)
```

The returned model URI is `models:/<model_id>` (instead of `runs:/<run_id>/<artifact_path>` as in MLflow 2.x). It is recommended to load models using this URI. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

#### Loading a model

Use `mlflow.<model-flavor>.load_model(model_uri)` with the model URI, a run-relative path, a Unity Catalog volumes path, or a registered model path. For Python function models, `mlflow.pyfunc.load_model()` is also available. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

#### Registering in Unity Catalog

When a `LoggedModel` is registered to the Unity Catalog model registry, all its metrics and parameters become visible in one central location across experiments and workspaces. Registration uses the three‑level Unity Catalog name (e.g., `my_catalog.my_schema.my_model`). ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

```python
mlflow.register_model("models:/{model_id}", "{catalog}.{schema}.{model_name}")
```

### Migration from MLflow 2.x

- Use `name` instead of `artifact_path` (the latter is deprecated).
- Model artifacts are now stored under the model’s path, not under the run’s path.
- Model URIs are `models:/<model_id>` rather than `runs:/<run_id>/<artifact_path>`.
- No requirement for an active run when logging a model.
- Models logged with MLflow 3 may not be fully compatible with MLflow 2.x clients, but the reverse is supported. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Limitations

- **Spark models** logged via `mlflow.spark.log_model` continue to use the MLflow 2.x run‑based artifact structure and do not produce a `LoggedModel`. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Related Concepts

- [MLflow 3 for Models](/concepts/mlflow-3-for-models.md) – broader platform changes including deployment jobs and unified metrics.
- [Unity Catalog](/concepts/unity-catalog.md) – the catalog system that stores registered models and their version histories.
- Model Version – a specific version of a registered model in Unity Catalog.
- [Model Registry](/concepts/mlflow-model-registry.md) – the component for managing model lifecycle (now defaults to `databricks-uc`).
- [MLflow runs](/concepts/mlflow-run.md) – the traditional unit of execution, still used but decoupled from model metadata in MLflow 3.
- [MLflow flavors](/concepts/mlflow-model-flavors.md) – standard packaging formats (pyfunc, sklearn, PyTorch) that remain unchanged.

### Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md
- log-load-and-register-mlflow-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
2. [log-load-and-register-mlflow-models-databricks-on-aws.md](/references/log-load-and-register-mlflow-models-databricks-on-aws-dc2ad486.md)
