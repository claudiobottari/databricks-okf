---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b65b07face5b683b6b7c9de15fff34ed3d532e7d8813554880951cdc176de4ad
  pageDirectory: concepts
  sources:
    - use-custom-python-libraries-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-add_libraries_to_model-utility
    - MAU
  citations:
    - file: use-custom-python-libraries-with-model-serving-databricks-on-aws.md
title: MLflow add_libraries_to_model Utility
description: MLflow utility that prepackages all model dependencies as Python wheel files alongside the model, ensuring exact library versions from the training environment
tags:
  - mlflow
  - dependency-management
  - model-registry
timestamp: "2026-06-19T23:20:51.141Z"
---

# [MLflow](/concepts/mlflow.md) `add_libraries_to_model` Utility

The **`add_libraries_to_model`** utility is a function provided by [MLflow](/concepts/mlflow.md) that packages all dependencies of a logged model — including custom libraries shipped as Python wheels — directly into the model artifact. It ensures that the exact libraries used during training are available when the model is served, eliminating environment mismatches.

## Overview

When deploying a model with [Model Serving](/concepts/model-serving.md), it is critical that the serving environment contains all the Python packages that the model relies on. While `extra_pip_requirements` or `conda_env` parameters in `log_model()` can specify dependencies, they may not guarantee that the same library versions will be resolved at inference time. The `add_libraries_to_model` utility solves this by bundling the dependencies at model registration time. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Purpose

This utility is designed for scenarios where:

- Custom Python libraries (packaged as wheel files) are used for pre‑/post‑processing, custom model definitions, or other shared code.
- Dependencies are stored in Unity Catalog volumes or Databricks File System (DBFS) and need to be permanently linked to the model.
- You want to guarantee that the libraries used by the model are exactly the ones accessible from your training environment. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Usage

The function resides in the `mlflow.models.utils` module.

```python
import [[mlflow|MLflow]].models.utils

[[mlflow|MLflow]].models.utils.add_libraries_to_model(<model-uri>)
```

^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Model URI

The `model_uri` argument specifies the registered model version to update. It can reference either the [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) or the [Workspace Model Registry](/concepts/workspace-model-registry.md) (legacy):

- [Unity Catalog](/concepts/unity-catalog.md): `models:/<catalog>.<schema>.<model-name>/<model-version>`
- [Workspace Model Registry](/concepts/workspace-model-registry.md): `models:/<model-name>/<model-version>`

When a model registry URI is used, the utility automatically generates a new version under the existing registered model. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Effect

After calling `add_libraries_to_model`, the model artifact includes:

- All packages specified as dependencies in the model’s `conda.yaml` or `requirements.txt`.
- Any custom [Python Wheel Files](/concepts/python-wheel-files.md) that were provided via `extra_pip_requirements` or `code_paths` when the model was logged.

The new model version can then be deployed to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), and the serving environment will use the bundled libraries. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Requirements

- [MLflow](/concepts/mlflow.md) 1.29 or higher. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]
- The model must already be registered in a model registry ([Unity Catalog](/concepts/unity-catalog.md) or workspace).
- Custom wheel files must be accessible (e.g., in a [Unity Catalog](/concepts/unity-catalog.md) volume or DBFS) at the time `add_libraries_to_model` is called.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Deployment of ML models to endpoints that use the packaged libraries.
- extra_pip_requirements – Parameter used in `log_model()` to specify additional pip dependencies.
- [Unity Catalog](/concepts/unity-catalog.md) – Recommended storage location for dependency wheel files.
- [Model Registry](/concepts/mlflow-model-registry.md) – Central repository where models are versioned and from which the utility creates new versions.
- Python wheel – Standard format for packaging custom Python libraries.

## Sources

- use-custom-python-libraries-with-model-serving-databricks-on-aws.md

# Citations

1. [use-custom-python-libraries-with-model-serving-databricks-on-aws.md](/references/use-custom-python-libraries-with-model-serving-databricks-on-aws-58bc4dbc.md)
