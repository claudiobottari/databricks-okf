---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00a1f89bc80e31c1936d3d6d52dd421fdd3da44e7059a274433f416a1f15e8bd
  pageDirectory: concepts
  sources:
    - use-custom-python-libraries-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-libraries-for-databricks-model-serving
    - CLFDMS
    - Custom Python Libraries for Model Serving
    - Custom Python Libraries with Model Serving
    - Private Libraries for Model Serving
    - Use Custom Python Libraries with Model Serving
    - Use custom Python libraries with Model Serving
    - using custom Python libraries with Model Serving
  citations:
    - file: use-custom-python-libraries-with-model-serving-databricks-on-aws.md
title: Custom Libraries for Databricks Model Serving
description: Pattern for including custom Python libraries or libraries from private mirrors when deploying ML models to Databricks Model Serving endpoints
tags:
  - databricks
  - model-serving
  - mlflow
timestamp: "2026-06-19T23:20:42.656Z"
---

# Custom Libraries for [Databricks Model Serving](/concepts/databricks-model-serving.md)

**Custom Libraries for Databricks Model Serving** refers to the methods and best practices for including private or proprietary Python libraries — such as pre/post-processing functions, custom model definitions, or shared utilities — in a model deployment served via [Databricks Model Serving](/concepts/databricks-model-serving.md). This also covers using private PyPI mirrors (e.g., Nexus, Artifactory) to reduce supply-chain risk. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Requirements

- [MLflow](/concepts/mlflow.md) 1.29 or higher.
- Restrict outbound network access from [Model Serving](/concepts/model-serving.md) endpoints by configuring network policies. See [Validate with model serving](/concepts/databricks-model-serving.md) in the Databricks network security documentation. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Option 1: Use a Private Package Repository

If your organization uses a private PyPI mirror (such as Nexus or Artifactory), workspace admins can configure it as the default package repository for the entire workspace. [Model Serving](/concepts/model-serving.md) automatically uses this workspace-level configuration when building the model environment. Once configured, proceed directly to serving the model. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

To set up a private package repository, see Configure default Python package repositories. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Option 2: Package Custom Libraries as Wheel Files

Use this option when a private PyPI mirror is not accessible, or when you have custom libraries that are not available in any package repository. You package them as [Python Wheel Files](/concepts/python-wheel-files.md) and include them when logging your model with [MLflow](/concepts/mlflow.md). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Step 1: Upload Your Dependency File

Databricks recommends uploading the wheel file to Unity Catalog volumes. Alternatively, upload it to Databricks File System (DBFS) using the Databricks UI. To make the library available to your notebook, install it using `%pip`, which downloads the dependency to the cluster. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Step 2: Log the Model with a Custom Library

After installing the library and uploading the wheel file, include the path in the `extra_pip_requirements` parameter of `log_model()`. For example:

```python
[[mlflow|MLflow]].sklearn.log_model(model, "sklearn-model",
    extra_pip_requirements=["/volumes/path/to/dependency.whl"])
```

For DBFS, prefix the path with `/dbfs/`:

```python
[[mlflow|MLflow]].sklearn.log_model(model, "sklearn-model",
    extra_pip_requirements=["/dbfs/path/to/dependency.whl"])
```

If your library is stored externally, you can use the `code_paths` parameter and reference it as `"code/<wheel-file-name>.whl"` in `extra_pip_requirements`:

```python
[[mlflow|MLflow]].pyfunc.log_model(
    name="model",
    python_model=MyModel(),
    code_paths=["/path/to/dependency.whl"],   # logged as code/dependency.whl
    extra_pip_requirements=["code/dependency.whl"],
)
```

All custom Python libraries associated with the model must be specified when logging, using either `extra_pip_requirements` or `conda_env`. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Step 3: Update [MLflow](/concepts/mlflow.md) Model with [Python Wheel Files](/concepts/python-wheel-files.md)

[MLflow](/concepts/mlflow.md) provides the `add_libraries_to_model()` utility to log the model together with **all** its dependencies pre-packaged as wheel files. This guarantees that the libraries used at serving time match those from the training environment exactly. The utility generates a new version in the model registry ([Unity Catalog](/concepts/unity-catalog.md) or workspace legacy). Example:

```python
import [[mlflow|MLflow]].models.utils
[[mlflow|MLflow]].models.utils.add_libraries_to_model(<model-uri>)
```

Use `models:/<catalog>.<schema>.<model>/<version>` for [Unity Catalog](/concepts/unity-catalog.md) or `models:/<model-name>/<model-version>` for the workspace registry. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Serve Your Model

Once the model version with the required packages is available in the model registry, add it to a [Model Serving](/concepts/model-serving.md) endpoint by following the standard endpoint creation or update workflow. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Troubleshoot Package Installation

If model deployment fails during the build phase, review the build logs:

1. Go to the **Serving** page in the Databricks workspace.
2. Click the endpoint name, then the **Logs** tab.
3. Select the failed version from the drop‑down and click **Build logs**.
4. Identify the error and resolve it, then create a new deployment or update the endpoint to trigger a new build. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Troubleshoot Private Package Repository

Common issues when using a private repository include:

- **Missing packages**: The package is not available in the configured repository. Add it manually.
- **Connection issues**: [Model Serving](/concepts/model-serving.md) cannot reach the repository. Verify network connectivity and firewall rules.
- **Authentication failures**: Credentials are invalid or expired. Update the secrets in the workspace configuration. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Testing with a Serverless Notebook

[Serverless notebooks](/concepts/serverless-notebook-environments.md) use the same default package repository as the workspace. You can test connectivity and package availability by installing the requirements from the model’s `requirements.txt` file before deploying:

```python
import [[mlflow|MLflow]]
import subprocess
import sys

catalog = "<your_catalog>"
schema = "<your_schema>"
model_name = "<your_model>"
version = <your_version>

full_model_name = f"{catalog}.{schema}.{model_name}"
requirements_uri = f"models:/{full_model_name}/{version}/requirements.txt"
local_path = [[mlflow|MLflow]].artifacts.download_artifacts(requirements_uri)

with open(local_path, "r") as f:
    print(f.read())

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", local_path])
print("Installation complete!")
```

^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The platform for deploying models as REST endpoints.
- Unity Catalog volumes – Recommended storage for wheel files.
- Databricks File System (DBFS) – Alternative storage for wheel files.
- [MLflow](/concepts/mlflow.md) – Framework used for model logging and registry operations.
- Private PyPi mirror – Enterprise package repository configuration.
- [Serverless notebooks](/concepts/serverless-notebook-environments.md) – Environment for pre‑deployment testing.

## Sources

- use-custom-python-libraries-with-model-serving-databricks-on-aws.md

# Citations

1. [use-custom-python-libraries-with-model-serving-databricks-on-aws.md](/references/use-custom-python-libraries-with-model-serving-databricks-on-aws-58bc4dbc.md)
