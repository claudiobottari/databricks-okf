---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 977fdddbd732d665aeaee458f4e4e2746f407455c564ec8ed5c4bff98a07e8f0
  pageDirectory: concepts
  sources:
    - log-model-dependencies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowpyfunclog_model-for-dependency-management
    - MFDM
  citations:
    - file: log-model-dependencies-databricks-on-aws.md
title: mlflow.pyfunc.log_model for Dependency Management
description: Using mlflow.pyfunc.log_model to log models from libraries without built-in MLflow flavors, with automatic dependency inference and support for extra_pip_requirements and pip_requirements parameters.
tags:
  - mlflow
  - python
  - model-logging
timestamp: "2026-06-19T19:16:59.399Z"
---

# mlflow.pyfunc.log_model for Dependency Management

**mlflow.pyfunc.log_model for Dependency Management** is a method in the MLflow Python API that enables logging machine learning models along with their Python package dependencies. It provides a flexible approach for managing dependencies, particularly for libraries that do not have built-in MLflow model flavors.

## Overview

`mlflow.pyfunc.log_model` is designed to handle dependency management for Python ML libraries that can be installed with `pip install PACKAGE_NAME==VERSION`, but do not have built-in MLflow model flavors. When using this method, it is important to log requirements with exact library versions — for example, `f"nltk=={nltk.__version__}"` instead of just `nltk`. ^[log-model-dependencies-databricks-on-aws.md]

This method supports logging for:
- Public and custom libraries packaged as Python egg or [Python Wheel Files](/concepts/python-wheel-files.md)
- Public packages on PyPI and privately hosted packages on your own PyPI server

^[log-model-dependencies-databricks-on-aws.md]

## Automatic Dependency Inference

When `mlflow.pyfunc.log_model` is called, MLflow attempts to infer dependencies automatically using `mlflow.models.infer_pip_requirements`. The inferred dependencies are logged to a `requirements.txt` file as a model artifact. ^[log-model-dependencies-databricks-on-aws.md]

In older versions of MLflow, automatic identification may not capture all Python requirements, particularly for libraries that are not built-in model flavors. In such cases, additional dependencies can be specified using the `extra_pip_requirements` parameter. ^[log-model-dependencies-databricks-on-aws.md]

It is generally discouraged to overwrite the entire set of requirements with the `conda_env` and `pip_requirements` parameters, as this overrides the dependencies that MLflow picks up automatically. ^[log-model-dependencies-databricks-on-aws.md]

## Custom Python Code Dependencies

For Python code dependencies that cannot be installed using `%pip install` — such as one or more `.py` files — MLflow provides the `code_paths` parameter (or `code_path` in MLflow 2.x). When logging a model with this parameter, MLflow stores the specified files or directories as artifacts alongside the model in a code directory. When the model is loaded, MLflow adds these files or directories to the Python path. This approach also works with custom [Python Wheel Files](/concepts/python-wheel-files.md), which can be included in the model using `code_paths` or `code_path` just like `.py` files. ^[log-model-dependencies-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name=name,
    code_paths=[filename.py],
    data_path=data_path,
    conda_env=conda_env,
)
```

## Logging Direct and Transitive Dependencies

With MLflow 3, users can log both direct and transitive dependencies by setting the `MLFLOW_LOCK_MODEL_DEPENDENCIES` environment variable to `"true"`. ^[log-model-dependencies-databricks-on-aws.md]

```python
import os
os.environ["MLFLOW_LOCK_MODEL_DEPENDENCIES"] = "true"

# Now when you log your model, MLflow captures
# both direct and transitive dependencies
mlflow.sklearn.log_model(model, "my_model")
```

## Non-Python Package Dependencies

MLflow does not automatically detect non-Python dependencies such as Java packages, R packages, and native packages (such as Linux packages). For these, Databricks recommends logging an artifact with the model specifying these dependencies — this could be a simple `.txt` or `.json` file. The `artifacts` argument in `mlflow.pyfunc.log_model` allows specification of these additional artifacts. ^[log-model-dependencies-databricks-on-aws.md]

## Deployment Considerations

When deploying models from the MLflow Tracking Server or Model Registry, it is important to ensure that the deployment environment has the correct dependencies installed. For [Model Serving](/concepts/model-serving.md), Databricks handles public PyPI dependencies specified in the `requirements.txt` file, and MLflow automatically loads `.py` files or [Python Wheel Files](/concepts/python-wheel-files.md) included via `code_paths`. ^[log-model-dependencies-databricks-on-aws.md]

**Important:** Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. When logging a `pyfunc` model on these runtimes without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model's `conda.yaml`, and Model Serving cannot build the container image because it requires `mlflow`. Specify `mlflow==<version>` in `pip_requirements` when logging the model. ^[log-model-dependencies-databricks-on-aws.md]

For batch and streaming jobs, the Model Registry can generate a scoring notebook that contains code to install the Python dependencies from the model's `requirements.txt` file. ^[log-model-dependencies-databricks-on-aws.md]

## Customization Options

For scenarios requiring more customized model logging, users can either write a [custom Python model](/concepts/custom-mlflow-pythonmodel.md) by subclassing `mlflow.pyfunc.PythonModel`, or write a custom flavor for more advanced customization. The custom Python model approach works well for Python-only models, while custom flavors require more implementation work but offer greater flexibility. ^[log-model-dependencies-databricks-on-aws.md]

## Related Concepts

- [MLflow pyfunc PythonModel](/concepts/mlflow-pyfunc-custom-python-model.md) — The base class for custom Python models
- [MLflow Model Flavors](/concepts/mlflow-model-flavors.md) — Built-in model support for common ML libraries
- [Model Serving](/concepts/model-serving.md) — Deployment of MLflow models as REST API endpoints
- [Model Registry](/concepts/mlflow-model-registry.md) — Managing model lifecycle and generating scoring notebooks
- [MLflow Dependencies](/concepts/mlflow-model-dependency-logging.md) — Overview of dependency management in MLflow

## Sources

- log-model-dependencies-databricks-on-aws.md

# Citations

1. [log-model-dependencies-databricks-on-aws.md](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
