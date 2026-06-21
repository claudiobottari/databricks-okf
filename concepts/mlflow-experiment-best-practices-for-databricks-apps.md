---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d440b37cb76e96d88bd6da7bd64a1cac8a7f9ddba21a7711a1c8b4d739fdd8f8
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-best-practices-for-databricks-apps
    - MEBPFDA
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Best Practices for Databricks Apps
description: Recommended practices for organizing, naming, and managing MLflow experiments used as resources in Databricks Apps.
tags:
  - databricks
  - mlflow
  - best-practices
timestamp: "2026-06-19T08:52:14.987Z"
---

# MLflow Experiment Best Practices for Databricks Apps

**MLflow Experiment Best Practices for Databricks Apps** provides guidance on how to effectively integrate [MLflow experiments](/concepts/mlflow-experiment.md) into Databricks Apps to enable experiment tracking for AI applications, agents, LLMs, and ML models. MLflow experiments provide a structured way to organize and log runs, track parameters, metrics, and artifacts throughout the AI application development lifecycle.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Overview

When you add an MLflow experiment as a resource in a Databricks App, the app gains several capabilities: debugging agents and LLM applications with execution traces, evaluating agent and LLM application quality with scorers, managing and versioning prompt templates for LLM applications, logging ML model training runs with parameters, metrics, and artifacts, and retrieving experiment data, metadata, and run history.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Adding an MLflow Experiment Resource

Before adding an MLflow experiment as a resource, review the [app resource prerequisites](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/resources#resources-prereqs). To add the resource, navigate to the **App resources** section when creating or editing an app, click **+ Add resource** > **MLflow experiment**, and select an experiment from the available list in your workspace.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Permission Level Best Practices

Choose the appropriate permission level based on the app's requirements:

- **Can read:** Grants permission to view experiment metadata, runs, parameters, and metrics. Use for apps that only display experiment results.
- **Can edit:** Grants permission to modify experiment settings and metadata. Use for apps that need to log new runs or update existing ones.
- **Can manage:** Grants full administrative access to the experiment. Reserve for app administration scenarios.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

When an MLflow experiment resource is added, Databricks grants the app's service principal the specified permissions on the selected experiment. The app can then log training runs and access experiment data through the MLflow Tracking API. Access is scoped to the selected experiment only — the app cannot access other experiments unless they are added as separate resources.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variable Configuration

When deploying an app with an MLflow experiment resource, Databricks exposes the experiment ID through environment variables. Reference these using the `valueFrom` field in your `app.yaml` configuration.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example app.yaml configuration:**
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

## Organizational Best Practices

### Logical Experiment Organization

Organize experiments logically by project or model type to improve discoverability. This makes it easier for team members to find relevant experiments and understand the context of runs.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Consistent Naming Conventions

Use consistent naming conventions for runs and parameters across your organization. This promotes clarity and enables straightforward comparison across different runs and projects.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Retention and Storage Management

Consider experiment retention policies and storage management for long-running projects. Establish guidelines for archiving or cleaning up old experiments to manage storage costs and maintain a clean workspace.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removing an MLflow Experiment Resource

When you remove an MLflow Experiment resource from an app, the app's service principal loses access to the experiment. The experiment itself remains unchanged and continues to be available for other users and applications that have appropriate permissions.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Custom Resource Keys

Optionally specify a custom resource key, which is how you reference the experiment in your app configuration. The default key is `experiment`. Custom keys help distinguish between multiple experiment resources in the same app.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps — The application platform where MLflow experiments are integrated as resources
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The core organizational unit for MLflow runs and tracking
- [MLflow Tracking API](/concepts/mlflow-tracking.md) — The API used to log parameters, metrics, and artifacts
- [Service Principal Authorization](/concepts/service-principal-authorization-for-databricks-apps.md) — How Databricks Apps authenticate and access resources
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controls for managing serverless workload costs in MLflow
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Using MLflow experiments for production monitoring

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
