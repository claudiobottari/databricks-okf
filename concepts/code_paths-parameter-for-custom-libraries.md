---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 399e327ce8f2919a6e4a8f20aea24a52dc671c1f84071c77bedf43d4b5093ffc
  pageDirectory: concepts
  sources:
    - use-custom-python-libraries-with-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code_paths-parameter-for-custom-libraries
    - CPFCL
  citations:
    - file: use-custom-python-libraries-with-model-serving-databricks-on-aws.md
title: code_paths Parameter for Custom Libraries
description: MLflow log_model parameter that allows inclusion of custom libraries stored outside Unity Catalog volumes or DBFS by embedding them in the model artifact's code directory
tags:
  - mlflow
  - model-logging
  - python
timestamp: "2026-06-19T23:21:02.116Z"
---

## code_paths Parameter for Custom Libraries

The **`code_paths` parameter** is an [MLflow](/concepts/mlflow.md) argument used when logging a model with `mlflow.pyfunc.log_model()` to include custom Python libraries that are stored outside [Unity Catalog](/concepts/unity-catalog.md) volumes or DBFS. It allows you to specify the file system path to a dependency (such as a Python wheel file) so that it gets packaged alongside the model in the artifact directory under a `code/` subdirectory. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Purpose

When a custom library is not accessible through a private PyPI mirror and is not uploaded to a volume or DBFS, you cannot reference it directly via an absolute path in `extra_pip_requirements`. The `code_paths` parameter solves this by letting [MLflow](/concepts/mlflow.md) copy the file into the model artifact as `code/<filename>`. You can then reference that relative path in `extra_pip_requirements` to install the library at deployment time. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Usage

In `mlflow.pyfunc.log_model()`, pass a list of file paths to the `code_paths` parameter. Then, in `extra_pip_requirements`, specify the library using the relative path `code/<wheel-file-name>.whl`. The following example demonstrates the pattern:

```python
[[mlflow|MLflow]].pyfunc.log_model(
    name="model",
    python_model=MyModel(),
    code_paths=["/path/to/dependency.whl"],   # logged as code/dependency.whl
    extra_pip_requirements=["code/dependency.whl"],
)
```

^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Context

The `code_paths` parameter is part of **Option 2** (Package custom libraries as wheel files) for including custom libraries with [Model Serving](/concepts/model-serving.md) deployments. It is an alternative to the recommended approach of uploading dependencies to Unity Catalog volumes or Databricks File System (DBFS). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Related Concepts

- [MLflow](/concepts/mlflow.md) – The framework that provides the `log_model()` API and the `code_paths` parameter.
- extra_pip_requirements Parameter – Used alongside `code_paths` to specify installation paths for packaged dependencies.
- Private Libraries Model Serving – The broader guide on using custom libraries with [Model Serving](/concepts/model-serving.md).
- [Model Serving](/concepts/model-serving.md) – The serving infrastructure that consumes models logged with these dependencies.
- Custom Python Libraries – General concept of packaging and deploying custom code.

### Sources

- use-custom-python-libraries-with-model-serving-databricks-on-aws.md

# Citations

1. [use-custom-python-libraries-with-model-serving-databricks-on-aws.md](/references/use-custom-python-libraries-with-model-serving-databricks-on-aws-58bc4dbc.md)
