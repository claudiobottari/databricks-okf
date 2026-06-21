---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55690f291abdbef01268478fbc5b16ce316f09468da45bb6cd69c788778e48b6
  pageDirectory: concepts
  sources:
    - use-custom-python-libraries-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - private-pypi-mirror-configuration-for-model-serving
    - PPMCFMS
    - Private PyPI Mirror Configuration
  citations:
    - file: use-custom-python-libraries-with-model-serving-databricks-on-aws.md
title: Private PyPI Mirror Configuration for Model Serving
description: Workspace-level configuration of private package repositories (Nexus, Artifactory) as default package source for Model Serving deployments
tags:
  - databricks
  - package-management
  - security
timestamp: "2026-06-19T23:20:47.710Z"
---

# Private PyPI Mirror Configuration for [Model Serving](/concepts/model-serving.md)

**Private PyPI Mirror Configuration for Model Serving** refers to the setup required to use private Python package repositories (such as Nexus or Artifactory) as the source for dependencies when deploying machine learning models to [Model Serving](/concepts/model-serving.md) endpoints on Databricks. This configuration allows enterprise teams to reduce the risk of supply-chain attacks by controlling which packages are available for model deployments. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Overview

Model development often requires custom Python libraries for pre-processing, post-processing, custom model definitions, and shared utilities. Many enterprise security teams encourage the use of private PyPI mirrors instead of public repositories. Databricks offers native support for installing custom libraries and libraries from a private mirror in the workspace. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

There are two primary approaches for making custom or private libraries available to [Model Serving](/concepts/model-serving.md) endpoints:

1. **Configure a private package repository** as the workspace default for automatic use by [Model Serving](/concepts/model-serving.md).
2. **Package custom libraries as wheel files** and include them when logging the model.

## Requirements

- [MLflow](/concepts/mlflow.md) 1.29 or higher^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]
- Restrict outbound network access from [Model Serving](/concepts/model-serving.md) endpoints by configuring network policies (see Network Policies for Model Serving). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Option 1: Private Package Repository

Use this option when your organization operates a private PyPI mirror such as Nexus or Artifactory. Workspace admins configure it as the default package repository for the workspace. [Model Serving](/concepts/model-serving.md) automatically uses this workspace-level configuration when building the model environment. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

To set up a private package repository, see Configure Default Python Package Repositories. Once configured, proceed to serving the model. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Option 2: Package Custom Libraries as Wheel Files

Use this option when a private PyPI mirror is not accessible, or for custom libraries that are not available in any package repository. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Step 1: Upload the Dependency File

Databricks recommends uploading the dependency file to Unity Catalog Volumes. Alternatively, upload it to Databricks File System (DBFS) using the Databricks UI. Install the library in the notebook using `%pip` to make it available to the cluster. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Step 2: Log the Model with the Custom Library

After installing the library and uploading the Python wheel file, specify the path in the `extra_pip_requirements` parameter when logging the model: ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
[[mlflow|MLflow]].sklearn.log_model(
    model,
    "sklearn-model",
    extra_pip_requirements=["/volumes/path/to/dependency.whl"]
)
```

For DBFS paths, include a forward slash before the path: ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
[[mlflow|MLflow]].sklearn.log_model(
    model,
    "sklearn-model",
    extra_pip_requirements=["/dbfs/path/to/dependency.whl"]
)
```

If the custom library is stored outside volumes or DBFS, use the `code_paths` parameter and reference the file within the `code/` directory: ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
[[mlflow|MLflow]].pyfunc.log_model(
    name="model",
    python_model=MyModel(),
    code_paths=["/path/to/dependency.whl"],
    extra_pip_requirements=["code/dependency.whl"]
)
```

### Step 3: Update the [MLflow](/concepts/mlflow.md) Model with [Python Wheel Files](/concepts/python-wheel-files.md)

[MLflow](/concepts/mlflow.md) provides the `add_libraries_to_model()` utility to log a model with all dependencies pre-packaged as [Python Wheel Files](/concepts/python-wheel-files.md). This guarantees that the libraries used by the model are exactly those accessible from the training environment. The model URI can reference the [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) (`models:/<uc-model>/<model-version>`) or the [Workspace Model Registry](/concepts/workspace-model-registry.md) (`models:/<model-name>/<model-version>`). This utility generates a new version under the existing registered model. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
import [[mlflow|MLflow]].models.utils
[[mlflow|MLflow]].models.utils.add_libraries_to_model(<model-uri>)
```

## Serving the Model

When a new model version with the included packages is available in the model registry, add that version to an endpoint with [Model Serving](/concepts/model-serving.md). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Troubleshooting

### Build Logs

If model deployment fails during the build phase, review build logs to identify package installation issues:

1. Go to the **Serving** page in the Databricks workspace.
2. Click the endpoint name to open details.
3. Click the **Logs** tab.
4. Select the failed version from the drop-down menu.
5. Click **Build logs**.

Review error messages, resolve the issue, then create a new deployment or update the endpoint to trigger a new build. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Private Package Repository Issues

Common issues with private package repositories include:

- **Missing packages**: The package is not available in the configured repository. Add the required package to the private repository. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]
- **Connection issues**: [Model Serving](/concepts/model-serving.md) cannot reach the package repository. Verify network connectivity and firewall rules. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]
- **Authentication failures**: Credentials configured for the repository are not valid or have expired. Update the secrets in the workspace configuration. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Testing with Serverless Notebooks

Serverless notebooks use the same default package repository configured for the workspace. Use a notebook to test connectivity, authentication, and package availability by installing the requirements from the model's `requirements.txt` file before deploying to [Model Serving](/concepts/model-serving.md): ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
import subprocess
import sys

# Step 1: Set model details
catalog = "<your_catalog>"
schema = "<your_schema>"
model_name = "<your_model>"
version = <your_version>

# Step 2: Download the model's requirements.txt
full_model_name = f"{catalog}.{schema}.{model_name}"
requirements_uri = f"models:/{full_model_name}/{version}/requirements.txt"
print(f"Downloading artifacts from: {requirements_uri}")
local_path = [[mlflow|MLflow]].artifacts.download_artifacts(requirements_uri)

# Step 3: Print the requirements
with open(local_path, "r") as f:
    print(f.read())

# Step 4: Install the requirements using the workspace's default package repository
print(f"Installing requirements from {local_path}...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", local_path])
print("Installation complete!")
```

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Deploying ML models as endpoints
- Configure Default Python Package Repositories — Workspace-level configuration for private mirrors
- Unity Catalog Volumes — Recommended storage location for dependency files
- Databricks File System (DBFS) — Alternative storage location for dependency files
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Registry for managing model versions
- Network Policies for Model Serving — Network access controls for serving endpoints
- Supply Chain Security — Security considerations for package dependencies

## Sources

- use-custom-python-libraries-with-model-serving-databricks-on-aws.md

# Citations

1. [use-custom-python-libraries-with-model-serving-databricks-on-aws.md](/references/use-custom-python-libraries-with-model-serving-databricks-on-aws-58bc4dbc.md)
