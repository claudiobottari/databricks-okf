---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0cb681ec1239eedcbdc5d0d2c990447b4a7c49b280dc985d72d47bd8a7278bc3
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-resource-in-databricks-apps
    - MERIDA
    - MLflow Resources in Databricks Apps
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Resource in Databricks Apps
description: A configuration pattern that allows Databricks Apps to reference and interact with MLflow experiments as first-class resources, enabling experiment tracking capabilities within applications.
tags:
  - databricks
  - mlflow
  - app-development
timestamp: "2026-06-19T21:57:58.600Z"
---

# MLflow Experiment Resource in Databricks Apps

An **MLflow Experiment Resource** is a Databricks Apps resource that integrates [MLflow experiments](/concepts/mlflow-experiment.md) directly into your Databricks application. When added as a resource, the experiment becomes available for tracking runs, logging parameters and metrics, managing prompt templates, and evaluating AI applications from within the app. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Overview

Adding an MLflow experiment as a resource enables experiment tracking for AI applications, agents, LLMs, and ML models. MLflow experiments provide a structured way to organize and log runs, track parameters, metrics, and artifacts throughout the AI application development lifecycle. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

When you add an MLflow experiment as a resource, your app can:
- Debug agents and LLM applications with execution traces
- Evaluate agent and LLM application quality with scorers
- Manage and version prompt templates for LLM applications
- Log ML model training runs with parameters, metrics, and artifacts
- Retrieve experiment data, metadata, and run history

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Adding an MLflow Experiment Resource

Before adding an MLflow experiment as a resource, review the [app resource prerequisites](/concepts/app-resource-permission-levels.md) in the Databricks documentation. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

To add an MLflow experiment resource:

1. In the **App resources** section when creating or editing an app, click **+ Add resource** > **MLflow experiment**.
2. Choose an MLflow experiment from the list of available experiments in your workspace.
3. Select the appropriate permission level for your app:
   - **Can read:** Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results.
   - **Can edit:** Grants the app permission to modify experiment settings and metadata.
   - **Can manage:** Grants the app full administrative access to the experiment.
4. (Optional) Specify a custom resource key, which is how you reference the experiment in your app configuration. The default key is `experiment`.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

When you add an MLflow experiment resource:
- Databricks grants your app's service principal the specified permissions on the selected experiment.
- The app can log training runs and access experiment data through the [MLflow Tracking API](/concepts/mlflow-tracking.md).
- Access is scoped to the selected experiment only. Your app cannot access other experiments unless you add them as separate resources.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variables

When you deploy an app with an MLflow experiment resource, Databricks exposes the experiment ID through environment variables that you can reference using the `valueFrom` field in your `app.yaml` configuration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example configuration:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment # Use your custom resource key if different
```

**Using the experiment ID in your application:**

```python
import os
import mlflow

# Access the experiment using the injected environment variable
experiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")

# Set the experiment for tracking
mlflow.set_experiment(experiment_id=experiment_id)

# Log parameters and metrics
with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

For more information, see [Access environment variables from resources](/concepts/environment-variable-injection-for-app-resources.md).

## Removing an MLflow Experiment Resource

When you remove an MLflow experiment resource from an app, the app's service principal loses access to the experiment. The experiment itself remains unchanged and continues to be available for other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

Follow these best practices when working with MLflow experiment resources:
- Organize experiments logically by project or model type to improve discoverability.
- Use consistent naming conventions for runs and parameters across your organization.
- Consider experiment retention policies and storage management for long-running projects.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- [MLflow Tracking API](/concepts/mlflow-tracking.md)
- Databricks Apps
- Service principal
- App resource prerequisites
- 403 PERMISSION_DENIED Serverless Budget Policy Error – Potential error when running serverless workloads associated with experiment resources

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
