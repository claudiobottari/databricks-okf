---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 090477c250755f16b9a3beb36115679d20ada6d38a2ca0d9da013e63cd6e96ad
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - environment-variable-injection-from-databricks-app-resources
    - EVIFDAR
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Environment Variable Injection from Databricks App Resources
description: When a Databricks App is deployed with a resource like an MLflow experiment, the resource ID is exposed via environment variables for use in application code.
tags:
  - databricks
  - environment-variables
  - app-configuration
timestamp: "2026-06-19T08:52:02.411Z"
---

# Environment Variable Injection from Databricks App Resources

**Environment Variable Injection from Databricks App Resources** is a mechanism by which Databricks automatically injects environment variables into an app’s runtime container when the app declares a resource dependency. This pattern allows app code to securely access resource identifiers, connection strings, and other configuration values without hardcoding them or managing secrets manually. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## How It Works

When you add a resource to a Databricks App—for example, an [MLflow Experiment](/concepts/mlflow-experiment.md) resource—Databricks grants the app’s service principal the specified permissions on that resource and exposes a resource-specific environment variable inside the app container. The variable is made available through the `valueFrom` field in the `app.yaml` configuration file. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

The environment variable name is determined by the resource type and the custom resource key you assign when adding the resource. For an MLflow experiment resource, the default key is `experiment`, and the injected variable is `MLFLOW_EXPERIMENT_ID`. If you specify a custom resource key, you use that key in `valueFrom` instead. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Example: MLflow Experiment Resource

The following is a typical `app.yaml` fragment that maps the injected environment variable to a container environment variable:

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment   # resource key (default)
```

In your Python application code, you can then read the variable using `os.getenv`:

```python
import os
import mlflow

experiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")
mlflow.set_experiment(experiment_id=experiment_id)
```

This allows the app to log runs, parameters, and metrics to the correct experiment without embedding the experiment ID in source code. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Resource Types and Injected Variables

The source material only describes the MLflow experiment resource, where the injected environment variable is `MLFLOW_EXPERIMENT_ID`. Other resource types (e.g., models, secrets, databases) are expected to follow the same `valueFrom` pattern, but their specific variable names are not covered in the provided source. For full details, see the general documentation on [accessing environment variables from resources](/concepts/environment-variable-injection-from-app-resources.md) in Databricks Apps. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Permissions and Security

When a resource is added, Databricks automatically grants the app’s service principal the permission level selected during resource configuration (Can read, Can edit, or Can manage). The app can then access only that specific resource through the injected environment variable—other resources remain inaccessible unless added explicitly. This scoped access model ensures that environment variable injection does not inadvertently widen the app’s permission surface. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removal of Resources

If you remove a resource from the app, the associated environment variable is no longer injected, and the app’s service principal loses access to that resource. The resource itself is not affected and remains available to other users and applications. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps – The serverless application platform.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The resource type used in the example.
- [Service Principal Authorization for Databricks Apps](/concepts/service-principal-authorization-for-databricks-apps.md)
- app.yaml configuration – The file where `valueFrom` is defined.
- [Environment variables in Databricks Apps](/concepts/environment-variable-injection-for-databricks-app-resources.md) – General guidance on environment variable usage.

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
