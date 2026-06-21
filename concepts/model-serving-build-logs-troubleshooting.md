---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 476d238fb905e02e5861f1eaca3dbc8db4b4665bd289119f248732067c48bc75
  pageDirectory: concepts
  sources:
    - use-custom-python-libraries-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-build-logs-troubleshooting
    - MSBLT
    - Model Serving Troubleshooting
    - Model Serving Build Logs
  citations:
    - file: use-custom-python-libraries-with-model-serving-databricks-on-aws.md
title: Model Serving Build Logs Troubleshooting
description: Process of diagnosing package installation failures during Model Serving deployment by inspecting build logs in the Databricks Serving UI
tags:
  - databricks
  - troubleshooting
  - model-serving
timestamp: "2026-06-19T23:21:10.263Z"
---

# [Model Serving](/concepts/model-serving.md) Build Logs Troubleshooting

**Model Serving Build Logs Troubleshooting** refers to the process of diagnosing and resolving package installation failures that occur during the build phase of a [Model Serving](/concepts/model-serving.md) endpoint deployment. When a model deployment fails during the build phase, reviewing the build logs helps identify issues with custom Python libraries, private package repositories, or dependency conflicts. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Accessing Build Logs

To review build logs for a failed model deployment:

1. Navigate to the **Serving** page in your Databricks workspace.
2. Click the endpoint name to open the endpoint details.
3. Click the **Logs** tab.
4. Select the failed version from the drop-down menu.
5. Click **Build logs**.

Review the error messages in the build logs to identify the specific issue. After resolving the problem, create a new deployment or update your endpoint to trigger a new build. ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

## Common Package Installation Issues

### Private Package Repository Problems

If you are using a private package repository (such as Nexus or Artifactory), common issues include:

- **Missing packages**: The required package is not available in your configured repository. Add the required package to your private repository.
- **Connection issues**: [Model Serving](/concepts/model-serving.md) cannot reach your package repository. Verify network connectivity and firewall rules.
- **Authentication failures**: The credentials configured for your repository are not valid or have expired. Update the secrets in your workspace configuration.

^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

### Custom Library Issues

When using custom Python libraries packaged as wheel files, common problems include:

- Incorrect file paths specified in `extra_pip_requirements`
- Missing dependencies that the custom library requires
- Incompatible library versions

## Testing Package Installation Before Deployment

Serverless notebooks use the same default package repository configured for your workspace. You can test connectivity, authentication, and package availability by installing the requirements from your model's `requirements.txt` file before deploying to [Model Serving](/concepts/model-serving.md): ^[use-custom-python-libraries-with-model-serving-databricks-on-aws.md]

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

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The deployment platform for serving ML models
- [Custom Python Libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) — How to include custom libraries in model deployments
- Private Package Repository — Enterprise PyPI mirrors for secure package management
- MLflow Model Logging — How to log models with dependencies
- [Model Serving Endpoint Management](/concepts/model-serving-endpoint.md) — Creating and managing serving endpoints
- Serverless Network Security — Network policies that affect [Model Serving](/concepts/model-serving.md) connectivity

## Sources

- use-custom-python-libraries-with-model-serving-databricks-on-aws.md

# Citations

1. [use-custom-python-libraries-with-model-serving-databricks-on-aws.md](/references/use-custom-python-libraries-with-model-serving-databricks-on-aws-58bc4dbc.md)
