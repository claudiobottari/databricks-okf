---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1148b708458a95b07d530152c6226e02bce877c1675f4be573343101f3d591f6
  pageDirectory: concepts
  sources:
    - use-custom-python-libraries-with-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - testing-private-repository-connectivity-with-serverless-notebooks
    - TPRCWSN
  citations:
    - file: use-custom-python-libraries-with-model-serving-databricks-on-aws.md
title: Testing Private Repository Connectivity with Serverless Notebooks
description: Using serverless notebooks to validate connectivity, authentication, and package availability from private PyPI mirrors before deploying to Model Serving
tags:
  - databricks
  - testing
  - package-management
timestamp: "2026-06-19T23:21:11.374Z"
---

# Testing Private Repository Connectivity with Serverless Notebooks

**Testing Private Repository Connectivity with Serverless Notebooks** refers to using a Databricks serverless notebook to verify that the workspace's configured private PyPI mirror (or custom package repository) is accessible and that required packages can be installed before deploying a model to [Model Serving](/concepts/model-serving.md). This technique helps diagnose issues with package availability, network connectivity, and authentication before triggering a costly endpoint build. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Purpose

When using a private package repository (such as Nexus or Artifactory) for [Model Serving](/concepts/model-serving.md), deployment failures often stem from missing packages, connection timeouts, or expired credentials. Serverless notebooks share the same default package repository that is configured at the workspace level. Therefore, a notebook can serve as a low-cost, interactive testbed to confirm that the repository is properly reachable and that the model’s dependencies can be resolved without error. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## How to Test Connectivity

To test connectivity, the user downloads the model’s `requirements.txt` file from the [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Model Registry](/concepts/workspace-model-registry.md) and then attempts to install those requirements inside a serverless notebook. The installation step exercises the same pip configuration that [Model Serving](/concepts/model-serving.md) will use, revealing any authentication or repository‑access problems before a model version is deployed. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

The recommended workflow is:

1. Specify the model by its catalog, schema, name, and version.
2. Download the model’s `requirements.txt` artifact using `mlflow.artifacts.download_artifacts()`.
3. Print the requirements to inspect them.
4. Install the requirements with `pip install`. If the installation succeeds, the private repository is reachable and the packages are available.

## Example Code

The following script, taken directly from the Databricks documentation, demonstrates the full test: ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
import subprocess
import sys

# Step 1: Set your model details
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

If the installation fails, the error message provides clues about whether the private repository is unreachable, the credentials are invalid, or a required package is missing. After resolving the issue, the user can proceed to deploy the model with [Model Serving](/concepts/model-serving.md). ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Related Concepts

- Private Package Repository – The workspace-level configuration that serverless notebooks and [Model Serving](/concepts/model-serving.md) both use.
- [Model Serving](/concepts/model-serving.md) – The production endpoint that will ultimately use the same repository.
- [Serverless Notebooks](/concepts/serverless-notebook-environments.md) – The interactive notebook environment used for this connectivity test.
- [Custom Python Libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) – The broader guide that includes packaging wheels and configuring repositories.
- 101 403 PERMISSION_DENIED Serverless Budget Policy Error – Another common issue affecting serverless workloads.

## Sources

- use-custom-python-libraries-with-model-serving-databricks-on-aws.md

# Citations

1. [use-custom-python-libraries-with-model-serving-databricks-on-aws.md](/references/use-custom-python-libraries-with-model-serving-databricks-on-aws-58bc4dbc.md)
