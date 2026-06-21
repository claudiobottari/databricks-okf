---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f9ce9b688963417cbf197b61165804ebd511839e4979714a76c5d648060279f1
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-resource
    - MER
    - Remove an MLflow Experiment resource
    - mlflow-experiment-resource-databricks-apps
    - MER(A
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Resource
description: A Databricks Apps resource type that connects an MLflow experiment to an app for tracking runs, parameters, metrics, and artifacts.
tags:
  - databricks-apps
  - mlflow
  - experiment-tracking
timestamp: "2026-06-18T14:18:35.100Z"
---

# MLflow Experiment Resource

A **MLflow Experiment Resource** is a Databricks Apps resource that allows an app to interact with a specific [MLflow Experiment](/concepts/mlflow-experiment.md) for tracking runs, parameters, metrics, artifacts, and other AI/ML lifecycle data. By adding an experiment as a resource, the app’s service principal is granted the specified permissions on that experiment, enabling programmatic access through the MLflow Tracking API. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Overview

MLflow experiments provide a structured way to organize and log runs, track parameters, metrics, and artifacts throughout the AI application development lifecycle. When you add an MLflow experiment as a resource, your Databricks App can: ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

- Debug agents and LLM applications with execution traces
- Evaluate agent and LLM application quality with scorers
- Manage and version prompt templates for LLM applications
- Log ML model training runs with parameters, metrics, and artifacts
- Retrieve experiment data, metadata, and run history

## Adding an MLflow Experiment Resource

Before adding an experiment resource, review the [app resource prerequisites](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/resources#resources-prereqs). Then follow these steps: ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

1. In the **App resources** section when creating or editing an app, click **+ Add resource** > **MLflow experiment**.
2. Choose an MLflow experiment from the list of available experiments in your workspace.
3. Select the appropriate permission level:
   - **Can read:** Grants the app permission to view experiment metadata, runs, parameters, and metrics.
   - **Can edit:** Grants the app permission to modify experiment settings and metadata.
   - **Can manage:** Grants the app full administrative access to the experiment.
4. (Optional) Specify a custom resource key (default: `experiment`).

When the resource is added, Databricks grants the app's service principal the selected permissions on the experiment. Access is scoped to that experiment only — other experiments are not accessible unless added as separate resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variables

On deployment, the experiment ID is exposed through environment variables that can be referenced using the `valueFrom` field in `app.yaml`. Example configuration: ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment # Use your custom resource key if different
```

In your application code, access the environment variable and set the experiment for tracking:

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

When you remove the resource from an app, the app’s service principal loses access to the experiment. The experiment itself remains unchanged and continues to be available for other users and applications with appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- Organize experiments logically by project or model type to improve discoverability.
- Use consistent naming conventions for runs and parameters across your organization.
- Consider experiment retention policies and storage management for long-running projects.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- Databricks Apps
- Service principal
- [MLflow Tracking API](/concepts/mlflow-tracking.md)
- Prompt templates
- Execution traces

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
