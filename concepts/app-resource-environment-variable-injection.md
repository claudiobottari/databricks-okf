---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d4fbb13cecf222ad0f2e77f91c2a2672e8a021139b6b25783e1a936e1be30044
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - app-resource-environment-variable-injection
    - AREVI
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: App Resource Environment Variable Injection
description: Pattern in Databricks Apps where resource identifiers (e.g., MLflow experiment IDs) are automatically exposed as environment variables at deployment, referenced via the valueFrom field in app.yaml configuration.
tags:
  - databricks-apps
  - environment-variables
  - configuration
timestamp: "2026-06-19T13:53:29.751Z"
---

# App Resource Environment Variable Injection

**App Resource Environment Variable Injection** is the mechanism by which Databricks Apps expose resource identifiers — such as experiment IDs, secret scopes, or other managed entities — as environment variables to application code. When a resource is added to a Databricks app and deployed, the platform automatically injects the resource’s identifier into the app’s runtime environment, allowing the application to reference it via `valueFrom` in the `app.yaml` configuration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Overview

A Databricks App can declare app resource dependencies that grant the app’s service principal specific permissions on workspace resources. For each declared resource, the platform generates one or more environment variables during deployment. The app’s code can then read these variables to obtain the resource’s ID or connection information without hardcoding it. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variable Exposure

When you add an [MLflow Experiment](/concepts/mlflow-experiment.md) resource to a Databricks app, Databricks exposes the experiment ID through environment variables. You reference the variable using the `valueFrom` field in your `app.yaml` configuration, specifying the resource key (default is `experiment` for MLflow experiments). For example:

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment   # Use your custom resource key if different
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

The environment variable name is automatically derived from the resource type and key. For an MLflow experiment resource with the default key, the variable is `MLFLOW_EXPERIMENT_ID`. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Using the Injected Variable in Application Code

After injection, the application can read the environment variable using standard runtime APIs. The following Python example shows how to retrieve an MLflow experiment ID and use it for tracking:

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

The variable value is guaranteed to be available at runtime and reflects the resource ID at the time of deployment. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Permission Scoping

When an environment variable is injected from a resource, the app’s service principal is granted the permission level selected during resource setup (e.g., **Can read**, **Can edit**, or **Can manage**). Access is scoped to the selected resource only; the app cannot access other resources of the same type unless they are added as separate dependencies. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- **Use custom resource keys** to control environment variable names and avoid conflicts when multiple resources of the same type are added. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Organize resources logically** — for MLflow experiments, group them by project or model type to improve discoverability. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Never hardcode resource IDs** in application source code; always rely on injected environment variables to keep deployments portable. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Monitor environment variable changes** when resources are removed or replaced — the app’s service principal loses access to the removed resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps Resources
- App.yaml Configuration
- Environment Variables in Databricks Apps
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Service Principal Permissions for Apps](/concepts/service-principal-authorization-for-databricks-apps.md)
- Resource Dependency Management

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
