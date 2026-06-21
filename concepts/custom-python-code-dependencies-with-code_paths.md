---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6aecf10aa3c9908ef519127ea6cf4334e608765f90bc2be6d3e926df9ff55168
  pageDirectory: concepts
  sources:
    - log-model-dependencies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-python-code-dependencies-with-code_paths
    - CPCDWC
  citations:
    - file: log-model-dependencies-databricks-on-aws.md
title: Custom Python Code Dependencies with code_paths
description: Including custom .py files or Python wheel files as model artifacts using the code_paths parameter so they are added to the Python path when the model is loaded.
tags:
  - mlflow
  - python
  - custom-code
timestamp: "2026-06-19T19:16:39.259Z"
---

# Custom Python Code Dependencies with code_paths

**Custom Python Code Dependencies with `code_paths`** refers to the ability, when logging an MLflow model with `mlflow.pyfunc.log_model`, to include custom Python files or directories as part of the model artifact. These dependencies cannot be installed via `%pip install` (e.g., `.py` files) and are stored alongside the model so they are available during inference.

## Overview

When a model depends on local Python code — such as one or more `.py` files, custom [Python Wheel Files](/concepts/python-wheel-files.md), or entire directories — MLflow provides the `code_paths` parameter (in MLflow 3) or the `code_path` parameter (in MLflow 2.x) inside `mlflow.pyfunc.log_model`. Any files or directories passed using these parameters are stored as artifacts in a code directory within the model. When the model is later loaded, MLflow adds these files or directories to the Python path, making them importable at prediction time. ^[log-model-dependencies-databricks-on-aws.md]

## Usage

The following example shows the syntax for MLflow 3:

```python
mlflow.pyfunc.log_model(
   name=name,
   code_paths=[filename.py],
   data_path=data_path,
   conda_env=conda_env,
)
```

For MLflow 2.x, use `code_path` instead of `code_paths`. The parameter accepts a list of file paths or directory paths. Custom [Python Wheel Files](/concepts/python-wheel-files.md) can also be included using `code_paths` or `code_path`, exactly like `.py` files. ^[log-model-dependencies-databricks-on-aws.md]

## How It Works

- **Logging**: MLflow copies the specified files or directories into the model’s code directory as part of the artifact store.
- **Loading**: When the model is loaded (e.g., via `mlflow.pyfunc.load_model` or during serving), MLflow automatically adds the code directory to `sys.path`, so that any imports in the model’s `predict()` function can resolve the custom code.
- **Deployment**: For [Model Serving](/concepts/model-serving.md) and [Lakeflow Jobs](/concepts/lakeflow-jobs.md), if the model was logged with `code_paths` (or `code_path`), MLflow loads those dependencies automatically. In batch or streaming jobs, you can also manually extract and install dependencies using `mlflow.pyfunc.spark_udf` with `env_manager` or by extracting the requirements. ^[log-model-dependencies-databricks-on-aws.md]

## Important Notes

- The `code_paths` parameter is the recommended way to include Python code that is not installable as a regular package.
- For scenarios requiring more extensive customization (e.g., subclassing `PythonModel` or writing a custom flavor), see Custom Python Models and Custom Flavors.
- When deploying models via Model Serving, if you use a Databricks Runtime ML environment that includes `mlflow-skinny` instead of the full `mlflow`, ensure you specify `mlflow==<version>` in `pip_requirements` to avoid container build failures. ^[log-model-dependencies-databricks-on-aws.md]

## Related Concepts

- [MLflow PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md)
- Model Dependencies
- Model Serving Deployment
- Custom Python Models
- [Python Wheel File Dependencies](/concepts/python-wheel-files.md)
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)

## Sources

- log-model-dependencies-databricks-on-aws.md

# Citations

1. [log-model-dependencies-databricks-on-aws.md](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
