---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd35b7aba4c06ee86379f4c9ff927f6606758177248f6a7ef5a3599a1edc2f16
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-resource-best-practices
    - MERBP
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Resource Best Practices
description: Recommended practices for organizing experiments by project or model type, using consistent naming conventions for runs and parameters, and considering retention policies and storage management.
tags:
  - best-practices
  - mlflow
  - databricks-apps
timestamp: "2026-06-19T17:27:00.050Z"
---

# MLflow Experiment Resource Best Practices

**MLflow Experiment Resource Best Practices** provides guidance for effectively adding, configuring, and managing [MLflow experiments](/concepts/mlflow-experiment.md) as resources within Databricks Apps. Following these practices ensures reliable experiment tracking, proper access control, and maintainable configurations for AI applications, agents, LLMs, and ML models.

## Organize Experiments Logically

Organize experiments by project or model type to improve discoverability. A clear organizational structure makes it easier for team members to find relevant experiments and understand the purpose of each experiment resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Use Consistent Naming Conventions

Use consistent naming conventions for runs and parameters across your organization. Standardized naming improves readability, simplifies querying experiment data, and reduces confusion when multiple teams or applications share experiment resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Consider Experiment Retention Policies

Consider experiment retention policies and storage management for long-running projects. As experiments accumulate runs, parameters, metrics, and artifacts, storage costs and query performance can be affected. Plan for data lifecycle management to avoid unnecessary storage consumption. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Select Appropriate Permission Levels

When adding an MLflow experiment as a resource to a Databricks App, choose the permission level that matches the app's requirements:

- **Can read:** Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results.
- **Can edit:** Grants the app permission to modify experiment settings and metadata.
- **Can manage:** Grants the app full administrative access to the experiment.

Databricks grants the app's service principal the specified permissions on the selected experiment. Access is scoped to the selected experiment only — the app cannot access other experiments unless they are added as separate resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Use Custom Resource Keys

Specify a custom resource key when adding an experiment resource. The resource key is how you reference the experiment in your app configuration. The default key is `experiment`, but a custom key can improve clarity when an app uses multiple experiment resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Reference Experiment ID via Environment Variables

When deploying an app with an MLflow experiment resource, Databricks exposes the experiment ID through environment variables. Reference these variables using the `valueFrom` field in your `app.yaml` configuration rather than hardcoding the experiment ID. This approach keeps configuration portable and avoids embedding sensitive identifiers in code. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

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

experiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")
mlflow.set_experiment(experiment_id=experiment_id)

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Understand Resource Removal Behavior

When you remove an MLflow experiment resource from an app, the app's service principal loses access to the experiment. The experiment itself remains unchanged and continues to be available for other users and applications that have appropriate permissions. Plan for access changes when restructuring app resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations
- Databricks Apps — The application platform that hosts MLflow experiment resources
- Service principal — The identity used by Databricks Apps for authorization
- [MLflow Tracking API](/concepts/mlflow-tracking.md) — The API used to log runs and access experiment data
- [Environment variables in Databricks Apps](/concepts/environment-variable-injection-for-databricks-app-resources.md) — How to access resource metadata from application code

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
