---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b06680c19d2771177aa5effbaf0634cac16bac8628e29b33dcec8d0d97bf329f
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - environment-variable-injection-for-app-resources
    - EVIFAR
    - environment-variable-injection-for-databricks-app-resources
    - EVIFDAR
    - Environment variables in Databricks Apps
    - environment-variable-injection-from-app-resources
    - Environment variables from app resources
    - Access environment variables from resources
    - Environment Variables from Resources
    - accessing environment variables from resources
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Environment Variable Injection for App Resources
description: Databricks Apps automatically injects resource metadata (such as experiment ID) into the app runtime via environment variables, configured using the valueFrom field in app.yaml.
tags:
  - databricks-apps
  - configuration
  - environment-variables
timestamp: "2026-06-18T14:19:22.516Z"
---

# Environment Variable Injection for App Resources

**Environment Variable Injection for App Resources** is a mechanism in Databricks Apps that automatically exposes resource metadata—such as experiment IDs, connection strings, or secret references—as environment variables in the application runtime. This allows app code to securely access resource configurations without hardcoding them in the application source.

## Overview

When a Databricks App is deployed with declared resources—such as an [MLflow Experiment](/concepts/mlflow-experiment.md), a Databricks SQL Warehouse, or a [Secrets Scope](/concepts/databricks-secret-scopes.md)—the platform automatically injects the resource's identifying metadata into the application's environment. App code can then read these environment variables to reference the resource at runtime, rather than embedding resource identifiers directly in the code. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Injection Mechanism

### Resource Declaration

Resources are declared in the app's `app.yaml` configuration file. When you add a resource through the Databricks Apps UI or the declarative configuration, Databricks grants the app's service principal appropriate permissions on the selected resource and prepares environment variable injection for that resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Custom Resource Keys

When adding a resource, you can specify a custom resource key—a logical name that identifies the resource within your app configuration. The default key varies by resource type (for example, `experiment` for an MLflow experiment). This key is used to reference the resource in the `valueFrom` field of your environment variable definitions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Environment Variable Exposure

At deployment time, Databricks exposes the resource's identifier through environment variables that can be referenced using the `valueFrom` field in the app's YAML configuration. The specific environment variable name and value depend on the resource type. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example configuration for an MLflow experiment resource:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment  # Use your custom resource key if different
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Using Injected Environment Variables in Application Code

Once injected, the environment variable is accessible through standard runtime mechanisms. For example, in Python:

```python
import os

experiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

Application code can then use this value to interact with the resource through the appropriate API. For the MLflow experiment example, the experiment ID can be passed to `mlflow.set_experiment()` for tracking runs:

```python
import mlflow

mlflow.set_experiment(experiment_id=experiment_id)

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Scope and Permissions

When a resource is added to an app:

- Databricks grants the app's service principal the specified permissions (e.g., `Can read`, `Can edit`, `Can manage`) on the selected resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- Access is scoped to the selected resource only. The app cannot access other resources of the same type unless they are added as separate resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Resource Removal

When a resource is removed from an app, the app's service principal loses access to that resource. The resource itself remains unchanged and continues to be available to other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Supported Resource Types

Environment variable injection is supported for resources including:

- [MLflow Experiment](/concepts/mlflow-experiment.md) — Injects the experiment ID for tracking runs, logging parameters, and storing artifacts. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- Databricks SQL Warehouse — Injects connection details for executing SQL queries.
- [Secrets Scope](/concepts/databricks-secret-scopes.md) — Injects references for accessing secrets at runtime.
- Serving Endpoint — Injects endpoint identifiers for model serving.

## Related Concepts

- Databricks Apps
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- Environment Variables in Databricks
- Service Principals in Databricks Apps
- App Configuration (app.yaml)

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
