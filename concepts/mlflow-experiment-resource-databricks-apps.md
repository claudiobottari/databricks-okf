---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1856bbd91667c04bb46ffaf8455ec24a8886db72b7276fc18cea1a0152b3969
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-resource-databricks-apps
    - MER(A
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Resource (Databricks Apps)
description: A Databricks Apps resource type that binds an MLflow experiment to an app, granting the app's service principal permissions to track runs, log parameters/metrics, and access experiment data via the MLflow Tracking API.
tags:
  - databricks-apps
  - mlflow
  - resource-management
timestamp: "2026-06-19T13:53:20.530Z"
---

# MLflow Experiment Resource (Databricks Apps)

**MLflow Experiment Resource (Databricks Apps)** is a Databricks Apps resource type that links a Databricks App to a specific [MLflow Experiment](/concepts/mlflow-experiment.md). Adding an experiment as a resource enables the app to log training runs, track parameters, metrics, and artifacts, as well as debug agents and evaluate LLM applications using execution traces and scorers. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Overview

When you add an MLflow experiment as a resource, your Databricks App can interact with that experiment through the [MLflow Tracking API](/concepts/mlflow-tracking.md). Capabilities include debugging agents and LLM applications with execution traces, evaluating agent and LLM application quality with scorers, managing and versioning prompt templates, logging ML model training runs with parameters/metrics/artifacts, and retrieving experiment data, metadata, and run history. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Adding an MLflow Experiment Resource

Before adding an MLflow experiment as a resource, review the [app resource prerequisites](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/resources#resources-prereqs). The process is performed in the **App resources** section when creating or editing an app:

1. Click **+ Add resource** and select **MLflow experiment**.
2. Choose an MLflow experiment from the list of available experiments in the workspace.
3. Select the appropriate permission level for the app:
   - **Can read:** View experiment metadata, runs, parameters, and metrics.
   - **Can edit:** Modify experiment settings and metadata.
   - **Can manage:** Full administrative access to the experiment.
4. Optionally specify a custom resource key (default is `experiment`). ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

When the resource is added, Databricks grants the app's service principal the specified permissions on the selected experiment. Access is scoped only to that experiment; other experiments require separate resource declarations. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variables

After deployment, the experiment ID is exposed through environment variables. The `app.yaml` configuration uses the `valueFrom` field referencing the resource key to inject the ID: ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment  # Use custom resource key if different
```

In the application code, the experiment ID can be read from the environment and used for MLflow tracking:

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

## Removing an MLflow Experiment Resource

When an MLflow Experiment resource is removed from an app, the app's service principal loses access to that experiment. The experiment itself remains unchanged and continues to be available to other users and applications with appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- Organize experiments logically by project or model type to improve discoverability.
- Use consistent naming conventions for runs and parameters across the organization.
- Consider experiment retention policies and storage management for long-running projects. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps – The application platform that hosts the app.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit for runs and tracking.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) – The API used to log parameters, metrics, and artifacts.
- Service Principal – The identity used by the Databricks App to access resources.
- Databricks Apps Resources – General resource types available to Databricks Apps.

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
