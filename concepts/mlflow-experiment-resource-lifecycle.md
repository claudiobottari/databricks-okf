---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40262aad288bc82821e3431e87265c7090c5ad52b95687cf528a73ffbb6662e8
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-resource-lifecycle
    - MERL
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Resource Lifecycle
description: The process of adding and removing MLflow experiment resources from Databricks apps, including how removal revokes service principal access while leaving the experiment itself intact.
tags:
  - databricks
  - mlflow
  - operations
timestamp: "2026-06-18T10:39:32.962Z"
---

# MLflow Experiment Resource Lifecycle

An **MLflow experiment resource** is a Databricks Apps resource that allows an application to connect to an [MLflow Experiment](/concepts/mlflow-experiment.md) for tracking runs, parameters, metrics, and artifacts. The lifecycle of an MLflow experiment resource encompasses adding it to an app, using it for experiment tracking, and removing it when no longer needed. Access is scoped to the selected experiment and managed through permissions granted to the app's service principal. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

---

## Adding an MLflow Experiment Resource

Adding an MLflow experiment resource requires an existing MLflow experiment in the workspace and compliance with general [app resource prerequisites](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/resources#resources-prereqs). ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

To add the resource:

1. In the **App resources** section when creating or editing an app, click **+ Add resource** > **MLflow experiment**.
2. Choose an experiment from the list of available experiments in your workspace.
3. Select the permission level for the app: **Can read**, **Can edit**, or **Can manage**.
4. Optionally, specify a custom resource key (default is `experiment`). This key is used to reference the experiment in your app configuration.

When the resource is added, Databricks automatically grants the app's service principal the specified permissions on the selected experiment. The app can then log runs and access experiment data through the [MLflow Tracking API](/concepts/mlflow-tracking.md), but only for that specific experiment. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Permission Levels

| Permission Level | Capabilities |
|---|---|
| **Can read** | View experiment metadata, runs, parameters, and metrics. Suitable for apps that display experiment results. |
| **Can edit** | Modify experiment settings and metadata. |
| **Can manage** | Full administrative access to the experiment. |

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

---

## Environment Variables

When an app with an MLflow experiment resource is deployed, Databricks exposes the experiment ID through environment variables. The variable name corresponds to the resource key defined in the app configuration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example `app.yaml` configuration:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment  # Uses the resource key
```

**Example usage in Python:**

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

The environment variable provides a secure, configuration-driven way to inject the experiment ID into the application without hard‑coding it. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

---

## Removing an MLflow Experiment Resource

When an MLflow experiment resource is removed from the app, the app’s service principal loses the permissions that were granted on that experiment. The experiment itself remains unchanged and continues to be accessible to other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

---

## Best Practices

- **Organize experiments logically** by project or model type to improve discoverability.
- **Use consistent naming conventions** for runs and parameters across your organization.
- **Consider experiment retention policies and storage management** for long-running projects, especially when experiments accumulate many runs and artifacts.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

---

## Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md)
- Databricks Apps
- Service Principal
- [MLflow Tracking API](/concepts/mlflow-tracking.md)
- Databricks Apps Resources
- Environment Variables in Databricks Apps

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
