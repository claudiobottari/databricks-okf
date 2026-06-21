---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d5f22abfcf091c6fa6184dc417828139314ff4ccfee2ab9122e4428c67030dd
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-environment-variable-injection
    - MEEVI
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Environment Variable Injection
description: Databricks automatically exposes the experiment ID via environment variables when an MLflow experiment is added as an app resource, accessible through the valueFrom field in app.yaml.
tags:
  - environment-variables
  - mlflow
  - databricks-apps
timestamp: "2026-06-19T17:26:50.225Z"
---

## MLflow Experiment Environment Variable Injection

**MLflow Experiment Environment Variable Injection** is a mechanism in Databricks Apps that automatically exposes the ID of an [MLflow Experiment](/concepts/mlflow-experiment.md) resource as an environment variable inside the application runtime. This allows app code to retrieve the active experiment ID without hardcoding it or manually fetching it from the workspace API. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### How It Works

When you add an MLflow experiment as a resource to a Databricks app, the deployment infrastructure injects the experiment ID into the app’s environment. The injection is configured declaratively in the `app.yaml` file using the `valueFrom` field. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

The resource key (by default `experiment`) is referenced in `valueFrom`. Databricks then maps that resource to an environment variable that the app can consume.

**Example `app.yaml` snippet:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment # Use your custom resource key if different
```

### Using the Injected Variable in Application Code

Inside the application (typically a Python script or a notebook), the injected environment variable is accessed via standard methods such as `os.getenv()`. The retrieved experiment ID can be passed directly to the MLflow tracking API. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example usage (Python):**

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

The app code does not need to know the experiment ID at development time; it is supplied at deployment time by the injected environment variable.

### Custom Resource Keys

If a custom resource key is specified when adding the experiment resource (instead of the default `experiment`), the `valueFrom` entry must match that custom key. The environment variable name (the `name` field in the `env` list) can be chosen arbitrarily; it does not have to be `MLFLOW_EXPERIMENT_ID`. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Related Concepts

- Databricks Apps environment variables – General mechanism for injecting resource credentials, secrets, and configuration values.
- [Databricks Apps resources](/concepts/databricks-app-resource-permissions.md) – The framework for attaching MLflow experiments, models, secrets, and other workspace objects to an app.
- [MLflow Experiment Resource](/concepts/mlflow-experiment-resource.md) – The resource type that triggers the injection.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) – The client API that uses the environment variable for experiment identification.

### Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
