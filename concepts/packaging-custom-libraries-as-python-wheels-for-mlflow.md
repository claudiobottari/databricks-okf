---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 13696dbb1849a135de1c76b6e36179d836a46464213b1c8637cc50154a3fd19e
  pageDirectory: concepts
  sources:
    - use-custom-python-libraries-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - packaging-custom-libraries-as-python-wheels-for-mlflow
    - PCLAPWFM
  citations:
    - file: use-custom-python-libraries-with-model-serving-databricks-on-aws.md
title: Packaging Custom Libraries as Python Wheels for MLflow
description: Method of packaging custom or unavailable libraries as Python wheel files and including them when logging MLflow models via extra_pip_requirements or conda_env
tags:
  - mlflow
  - python-packaging
  - model-deployment
timestamp: "2026-06-19T23:21:47.103Z"
---

Here is the wiki page for **Packaging Custom Libraries as Python Wheels for MLflow**, based strictly on the provided source material.

---

## Packaging Custom Libraries as Python Wheels for [MLflow](/concepts/mlflow.md)

**Packaging Custom Libraries as Python Wheels for MLflow** is a method for including custom or private Python libraries with models deployed to [Model Serving](/concepts/model-serving.md). This approach is recommended when a private PyPI mirror (such as Nexus or Artifactory) is not accessible, or when custom libraries are not available in any package repository. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Overview

Model development often requires custom Python libraries for pre- or post-processing, custom model definitions, and shared utilities. To make these libraries available during [Model Serving on Databricks](/concepts/model-serving-on-databricks.md), you can package them as [Python Wheel Files](/concepts/python-wheel-files.md) (`.whl`) and include them when logging your model with [MLflow](/concepts/mlflow.md). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Step 1: Upload the Dependency File

Databricks recommends uploading your wheel file to [Unity Catalog](/concepts/unity-catalog.md) [Volumes](/concepts/ucvolumedataset.md). Alternatively, you can upload it to the Databricks File System (DBFS) using the Databricks UI. After uploading, install the library in your notebook using `%pip` so that it is available to your training session. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Step 2: Log the Model with a Custom Library

After the library is installed and uploaded, specify the path to the wheel file using the `extra_pip_requirements` parameter in your `log_model` call. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

**Example using [Unity Catalog](/concepts/unity-catalog.md) volumes:**
```python
[[mlflow|MLflow]].sklearn.log_model(
    model,
    "sklearn-model",
    extra_pip_requirements=["/volumes/path/to/dependency.whl"]
)
```

**Example using DBFS:**
```python
[[mlflow|MLflow]].sklearn.log_model(
    model,
    "sklearn-model",
    extra_pip_requirements=["/dbfs/path/to/dependency.whl"]
)
```

If using DBFS, include a forward slash before the path (`/dbfs/path`). For `pyfunc` models, the same approach applies: ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
from [[mlflow|MLflow]].utils.environment import _mlflow_conda_env

[[mlflow|MLflow]].pyfunc.log_model(
    name="model",
    python_model=MyModel(),
    extra_pip_requirements=["/volumes/path/to/dependency.whl"],
)
```

If the custom library is stored outside volumes or DBFS, use the `code_paths` parameter and reference the wheel with a `code/` prefix: ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
[[mlflow|MLflow]].pyfunc.log_model(
    name="model",
    python_model=MyModel(),
    code_paths=["/path/to/dependency.whl"],
    extra_pip_requirements=["code/dependency.whl"],
)
```

### Step 3: Update an [MLflow](/concepts/mlflow.md) Model with Wheel Files

[MLflow](/concepts/mlflow.md) provides the `add_libraries_to_model()` utility to log a model with all its dependencies packaged as [Python Wheel Files](/concepts/python-wheel-files.md) — both custom libraries and all other dependencies specified in the model's environment. This ensures the libraries used during serving exactly match those in the training environment. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
import [[mlflow|MLflow]].models.utils

[[mlflow|MLflow]].models.utils.add_libraries_to_model(<model-uri>)
```

The `model_uri` references the [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) using the syntax `models:/<uc-model>/<model-version>`. For the legacy [Workspace Model Registry](/concepts/workspace-model-registry.md), use `models:/<model-name>/<model-version>`. This utility generates a new version under the existing registered model. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Requirements

- [MLflow](/concepts/mlflow.md) 1.29 or higher.
- Restrict outbound network access from [Model Serving](/concepts/model-serving.md) endpoints by configuring network policies (see network policies for model serving). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Troubleshooting

If a model deployment fails during the build phase, review the build logs:

1. Go to the **Serving** page in your Databricks workspace.
2. Click the endpoint name to open details.
3. Click the **Logs** tab.
4. Select the failed version from the drop-down menu.
5. Click **Build logs**.

After resolving the issue, create a new deployment or update the endpoint to trigger a new build. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

Common issues include missing packages in a private repository, connection failures to the repository, or expired authentication credentials. For private package repositories, update secrets in the workspace configuration as needed. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Alternative: Private Package Repository

If your organization uses a private PyPI mirror (such as Nexus or Artifactory), workspace admins can configure it as the default package repository. [Model Serving](/concepts/model-serving.md) automatically uses this workspace-level configuration, and the custom wheel packaging approach is not required. See [Configure default Python package repositories](https://docs.databricks.com/aws/en/admin/workspace-settings/default-python-packages) for setup instructions. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Related Concepts

- MLflow Model Serving
- Unity Catalog Volumes
- Databricks File System (DBFS)
- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md)
- Network policies for model serving

### Sources

- use-custom-python-libraries-with-model-serving-databricks-on-aws.md

# Citations

1. [use-custom-python-libraries-with-model-serving-databricks-on-aws.md](/references/use-custom-python-libraries-with-model-serving-databricks-on-aws-58bc4dbc.md)
