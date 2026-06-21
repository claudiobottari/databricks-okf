---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4cc4a5acfe858a9a1139bdbf6e40dc9f688b6720a0a4c6dc42f4c639f8c89723
  pageDirectory: concepts
  sources:
    - log-load-and-register-mlflow-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-dependency-management-in-mlflow
    - MDMIM
  citations:
    - file: log-load-and-register-mlflow-models-databricks-on-aws.md
title: Model Dependency Management in MLflow
description: Techniques for capturing and restoring model dependencies using requirements.txt, conda.yaml, virtualenv, and PySpark UDF environment managers to ensure reproducible model loading and scoring.
tags:
  - mlflow
  - dependency-management
  - reproducibility
timestamp: "2026-06-19T19:16:11.012Z"
---

# Model Dependency Management in MLflow

**Model Dependency Management in MLflow** refers to the processes, tools, and best practices for capturing, packaging, and restoring the software dependencies required to run an MLflow model. Proper dependency management ensures that models can be loaded and served in environments different from where they were trained, enabling reproducible inference.

## Automatic Dependency Logging

When you log a model using `mlflow.<model-type>.log_model()`, MLflow automatically generates and saves `requirements.txt` and `conda.yaml` files alongside the model artifacts. These files capture the Python packages and versions present in the training environment, allowing the model's runtime dependencies to be reconstructed later. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Dependency Restoration

### Using `requirements.txt` or `conda.yaml`

To recreate the model development environment, you can use the logged dependency files to reinstall dependencies. MLflow recommends using `virtualenv` for this purpose, though `conda` is also supported. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Automatic Dependency Detection

In Databricks Runtime 10.5 ML and above, MLflow warns you if a mismatch is detected between the current notebook environment and the model's logged dependencies. This helps catch environment inconsistencies early. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### The `get_model_dependencies` Function

Starting in Databricks Runtime 11.0 ML, for `pyfunc` flavor models, you can call `mlflow.pyfunc.get_model_dependencies()` to retrieve and download the model's dependency file. The function returns a file path that you can then install using `%pip install <file-path>`. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Restoring Dependencies in PySpark UDFs

When loading a model as a PySpark UDF for batch or streaming inference, you can restore dependencies within the UDF context by specifying `env_manager="virtualenv"` in the `mlflow.pyfunc.spark_udf()` call. This approach isolates the model's dependencies and does not affect the outside environment. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Anaconda Channel Considerations

### License Change Impact

Anaconda Inc. updated its terms of service for anaconda.org channels, potentially requiring a commercial license if your use relies on Anaconda's packaging and distribution. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Default Channel Change

MLflow models logged before version 1.18 (Databricks Runtime 8.3 ML or earlier) used the `defaults` channel (`https://repo.anaconda.com/pkgs/`) as a dependency by default. Starting with MLflow v1.18, the default channel was changed to `conda-forge` (community-managed at `https://conda-forge.org/`). Databricks stopped using the `defaults` channel for newly logged models due to the license change. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Checking and Changing the Channel

To verify whether a model has a dependency on the `defaults` channel, examine the `channels` value in the `conda.yaml` file packaged with the model. If you need to change the channel for an existing model, you can re-register the model to the [Model Registry](/concepts/mlflow-model-registry.md) with a new `conda.yaml` by specifying the channel in the `conda_env` parameter of `log_model()`. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Compatibility with Older Models

Databricks does not force customers to change their use of Anaconda repositories. If your use of the Anaconda.com repo through Databricks is permitted under Anaconda's terms, no action is required. However, models logged before MLflow v1.18 without excluding the `defaults` channel may have an unintended dependency on that channel. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Deploying Models with Dependencies

For production serving, proper dependency management is critical when deploying models to [Model Serving](/concepts/model-serving.md) endpoints. Additional resources include:

- Deploy models with dependencies — Using logged dependencies to serve models.
- [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) — Handling private or custom libraries.
- Package custom artifacts for Model Serving — Including non-Python artifacts with models.

^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Related Concepts

- MLflow Models — The standard packaging format for MLflow.
- [Model Registry](/concepts/mlflow-model-registry.md) — Centralized store for managing model lifecycle.
- Pyfunc Flavor — The generic Python function model flavor.
- [Model Serving](/concepts/model-serving.md) — Hosting models as REST endpoints.
- Conda Environment Management — Managing environments with conda.
- Unity Catalog Volumes — Storage location for model artifacts.

## Sources

- log-load-and-register-mlflow-models-databricks-on-aws.md

# Citations

1. [log-load-and-register-mlflow-models-databricks-on-aws.md](/references/log-load-and-register-mlflow-models-databricks-on-aws-dc2ad486.md)
