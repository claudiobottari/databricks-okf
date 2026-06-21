---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58090b9e02270455118de8112ca9ade4ab9b05fbbcfc1b7f08d7f7320dd76cbb
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-apps-mlflow-experiment-resource
    - DAMER
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Databricks Apps MLflow Experiment Resource
description: An MLflow experiment added as a first-class resource in a Databricks App, enabling experiment tracking, agent debugging, prompt management, and model training logging directly from the app.
tags:
  - databricks-apps
  - mlflow
  - resource-management
timestamp: "2026-06-19T17:26:55.919Z"
---

# Databricks Apps MLflow Experiment Resource

A **Databricks Apps MLflow Experiment Resource** is a declared resource within a Databricks App that grants the app access to a specific [MLflow Experiment](/concepts/mlflow-experiment.md). This integration enables experiment tracking for AI applications, agents, LLMs, and ML models. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Overview

When you add an MLflow experiment as a resource, your app can perform several key operations. It can debug agents and LLM applications with execution traces, evaluate agent and LLM application quality with scorers, manage and version prompt templates for LLM applications, log ML model training runs with parameters, metrics, and artifacts, and retrieve experiment data, metadata, and run history. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

MLflow experiments provide a structured way to organize and log runs, track parameters, metrics, and artifacts throughout the AI application development lifecycle. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Adding an MLflow Experiment Resource

Before adding an MLflow experiment as a resource, review the [app resource prerequisites](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/resources#resources-prereqs). ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

To add the resource:

1. In the **App resources** section when creating or editing an app, click **+ Add resource** > **MLflow experiment**.
2. Choose an MLflow experiment from the list of available experiments in your workspace.
3. Select the appropriate permission level for your app:
   - **Can read:** Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results.
   - **Can edit:** Grants the app permission to modify experiment settings and metadata.
   - **Can manage:** Grants the app full administrative access to the experiment.
4. (Optional) Specify a custom resource key, which is how you reference the experiment in your app configuration. The default key is `experiment`.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

When you add an MLflow experiment resource, Databricks grants your app's service principal the specified permissions on the selected experiment. The app can log training runs and access experiment data through the MLflow Tracking API. Access is scoped to the selected experiment only — your app cannot access other experiments unless you add them as separate resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variables

When you deploy an app with an MLflow experiment resource, Databricks exposes the experiment ID through environment variables that you can reference using the `valueFrom` field in your `app.yaml` configuration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example configuration:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment # Use your custom resource key if different
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

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

For more information, see Databricks Apps Environment Variables and how to access environment variables from resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removing an MLflow Experiment Resource

When you remove an MLflow Experiment resource from an app, the app's service principal loses access to the experiment. The experiment itself remains unchanged and continues to be available for other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

Follow these best practices when working with MLflow experiment resources:

- Organize experiments logically by project or model type to improve discoverability.
- Use consistent naming conventions for runs and parameters across your organization.
- Consider experiment retention policies and storage management for long-running projects.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The underlying organizational unit for runs and tracking
- Databricks Apps service principal — The identity that receives permissions on the experiment resource
- Databricks Apps Environment Variables — How to access resource values in app configuration
- [MLflow Tracking API](/concepts/mlflow-tracking.md) — The API used to log runs and access experiment data
- 403 PERMISSION_DENIED Serverless Budget Policy Error — An error that can occur when MLflow workloads interact with experiments

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
