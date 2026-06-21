---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c43da9b2fc349e5c54f8a5758355726531cdcd95020815a01329d1dec5af39ed
  pageDirectory: concepts
  sources:
    - log-load-and-register-mlflow-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-flavors
    - MMF
    - MLflow Built-in Model Flavors
    - MLflow Flavors
    - MLflow LangChain Flavor
    - MLflow built-in flavors
    - MLflow flavor
    - MLflow flavors
    - Model Flavors
  citations:
    - file: log-load-and-register-mlflow-models-databricks-on-aws.md
title: MLflow Model Flavors
description: Built-in conventions that allow a single MLflow Model to be saved in multiple framework-specific formats (python-function, pytorch, sklearn, etc.) for compatibility with different serving and inference platforms.
tags:
  - mlflow
  - model-flavors
  - machine-learning
timestamp: "2026-06-19T19:16:03.823Z"
---

## MLflow Model Flavors

An MLflow Model is a standard format for packaging machine learning models for use across various downstream tools, including batch inference on Apache Spark and real-time serving through a REST API. The format defines a convention that allows a model to be saved in different **flavors**, each tailored to be understood by different model serving and inference platforms. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Built-in Model Flavors

MLflow provides several built-in model flavors, including `python-function`, `pytorch`, and `sklearn`. When a model is logged, MLflow automatically captures `requirements.txt` and `conda.yaml` files that can recreate the model's development environment. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### The `pyfunc` Flavor

The `python_function` (or `pyfunc`) flavor is a generic Python function interface supported for any Python MLflow model. Users can load a model as a Python function using `mlflow.pyfunc.load_model()` and then call `.predict()` on input data. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

For `pyfunc` flavor models, MLflow provides additional dependency management. In Databricks Runtime 11.0 ML and above, you can call `mlflow.pyfunc.get_model_dependencies` to retrieve and download the model's dependencies. When loading a model as a PySpark UDF, specifying `env_manager="virtualenv"` in the `mlflow.pyfunc.spark_udf` call restores model dependencies within the UDF context without affecting the outside environment. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Loading and Using Models by Flavor

To load a previously logged model for inference or further development, use `mlflow.<model-type>.load_model(modelpath)`, where `modelpath` can be a run-relative path, a Unity Catalog volumes path, or a registered model path. For Python models, an additional option is to use `mlflow.pyfunc.load_model()` to load the model as a generic Python function. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Related Concepts

- MLflow Model – The standard format that flavors extend.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The system used to log models and their flavors.
- [Model Serving](/concepts/model-serving.md) – Platforms that consume different model flavors.
- [MLflow Python Function (pyfunc)](/concepts/mlflow-pyfunc-python-function.md) – The generic Python flavor for serving.
- [Model Registry](/concepts/mlflow-model-registry.md) – Centralized model store for managing model versions.

### Sources

- log-load-and-register-mlflow-models-databricks-on-aws.md

# Citations

1. [log-load-and-register-mlflow-models-databricks-on-aws.md](/references/log-load-and-register-mlflow-models-databricks-on-aws-dc2ad486.md)
