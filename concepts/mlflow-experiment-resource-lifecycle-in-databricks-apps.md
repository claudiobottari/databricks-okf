---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 747e3f43e8a98ed4b860634f1e43a4dd7495f3dcd7e6b70006d329f2ff824fba
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-resource-lifecycle-in-databricks-apps
    - MERLIDA
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Resource Lifecycle in Databricks Apps
description: The process of adding an MLflow experiment resource to an app (granting service principal access) and removing it (revoking service principal access, with the experiment itself remaining unchanged).
tags:
  - lifecycle
  - resource-management
  - databricks-apps
timestamp: "2026-06-19T17:27:34.796Z"
---

# MLflow Experiment Resource Lifecycle in Databricks Apps

**MLflow Experiment Resource Lifecycle in Databricks Apps** refers to the complete lifecycle of adding, referencing, using, and removing an [MLflow Experiment](/concepts/mlflow-experiment.md) as a managed resource within a Databricks App. This integration enables applications to leverage MLflow's tracking capabilities for AI development, including agent traces, LLM evaluations, prompt templates, and model training runs.

## Overview

When an MLflow experiment is attached as an app resource, the app's service principal receives the specified permissions on that experiment. The app can then log runs, parameters, metrics, and artifacts, and retrieve experiment metadata and run history through the MLflow Tracking API. Access is scoped to the selected experiment only; other experiments are not accessible unless added as separate resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Adding an MLflow Experiment Resource

Before adding the resource, review the [app resource prerequisites](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/resources#resources-prereqs). ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

1. In the **App resources** section when creating or editing an app, click **+ Add resource** > **MLflow experiment**.
2. Choose an available experiment from the workspace.
3. Select a permission level for the app:
   - **Can read** – View experiment metadata, runs, parameters, and metrics. Suitable for apps that display experiment results.
   - **Can edit** – Modify experiment settings and metadata.
   - **Can manage** – Full administrative access to the experiment.
4. Optionally specify a custom resource key (default is `experiment`). This key is used to reference the resource in the app configuration.

After adding, Databricks grants the app's service principal the selected permissions on that experiment. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variable Injection

When the app is deployed, the experiment ID is exposed through an environment variable. The variable is referenced using the `valueFrom` field in `app.yaml`:

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment  # Use your custom resource key if different
```

Within the application code, the environment variable can be accessed and used to set the active experiment:

```python
import os
import mlflow

experiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")
mlflow.set_experiment(experiment_id=experiment_id)

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
```

For more details, see [Access environment variables from resources](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/environment-variables#access-resources). ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removing an MLflow Experiment Resource

When the MLflow experiment resource is removed from an app, the app's service principal loses access to the experiment. The experiment itself remains unchanged and continues to be available to other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- Organize experiments logically by project or model type to improve discoverability.
- Use consistent naming conventions for runs and parameters across your organization.
- Consider experiment retention policies and storage management for long-running projects. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for MLflow runs and evaluations.
- Databricks Apps Service Principal – The identity used by the app to access resources.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) – The API for logging parameters, metrics, and artifacts.
- App Resource Prerequisites – Requirements before adding any resource to a Databricks App.
- Environment Variables in Databricks Apps – How resources inject configuration into app code.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – Error that can occur when MLflow serverless workloads lack a configured budget policy.

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
