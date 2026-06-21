---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1fa0dc16a46e6ea51dc8bcd3324bbc4db2221e5562c63685551796435cb4b21
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - environment-variable-injection-from-app-resources
    - EVIFAR
    - Environment variables from app resources
    - Access environment variables from resources
    - Environment Variables from Resources
    - accessing environment variables from resources
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Environment Variable Injection from App Resources
description: The mechanism by which Databricks exposes resource IDs (e.g., MLflow experiment IDs) as environment variables to app code via the 'valueFrom' field in app.yaml configuration.
tags:
  - databricks
  - configuration
  - environment-variables
timestamp: "2026-06-18T10:39:35.006Z"
---

# Environment Variable Injection from App Resources

**Environment Variable Injection from App Resources** is a mechanism in Databricks Apps where resource declarations in an app's configuration automatically expose resource identifiers — such as experiment IDs — as environment variables inside the application runtime. This allows applications to discover and connect to their declared resources programmatically without hardcoding identifiers.

## Overview

When you add a resource to a Databricks app (for example, an [MLflow Experiment](/concepts/mlflow-experiment.md)), the Databricks deployment system injects the resource's identifier into the application's environment as an environment variable. The app's code can then reference these injected variables to connect to the resource, enabling a clean separation between configuration and code. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

This pattern is part of the broader [Databricks Apps Resource Model](/concepts/databricks-apps-resource-permission-levels.md), where resources represent external services or data stores that the app needs to access.

## How Injection Works

### Resource Declaration

When you add a resource through the Databricks App UI or define it in `app.yaml`, you can optionally specify a custom resource key. For example, an MLflow experiment resource defaults to the key `experiment`. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Environment Variable Exposure

During app deployment, Databricks creates environment variables corresponding to the resource. The variable name is derived from the resource type and the resource key you specified, allowing you to reference the resource using the `valueFrom` field in your `app.yaml` configuration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example `app.yaml` configuration:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment  # Use your custom resource key if different
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Access in Application Code

The injected environment variables are available using standard environment variable access in your programming language of choice. The following Python example shows how an application retrieves the MLflow experiment ID and uses it for experiment tracking:

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

## Supported Resources

The environment variable injection pattern applies to all resource types in Databricks Apps. For a complete list of supported resources and their corresponding environment variables, see the Databricks Apps Resource Reference.

## Security

When you add a resource and specify a permission level for the app (e.g., `CAN READ`, `CAN EDIT`, `CAN MANAGE`), Databricks grants the app's service principal the specified permissions on that resource. The injected environment variable itself does not carry permissions — it simply provides the identifier. The app's access is governed by the permissions assigned to its Databricks Apps Service Principal. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- **Use descriptive resource keys** to make environment variable names meaningful in your codebase.
- **Do not hardcode resource identifiers** in application code. Always reference injected environment variables.
- **Store the environment variable name mapping** in your `app.yaml` configuration rather than in code, to keep deployment configuration centralized.
- **Validate that environment variables are set** at application startup with appropriate error messages for missing variables.
- **Use different resource keys** when an app needs to access multiple resources of the same type.

## Related Concepts

- Databricks Apps — The application platform that provides resource injection
- [MLflow Experiments](/concepts/mlflow-experiment.md) — A common resource type used with injection
- [Databricks Apps Resource Model](/concepts/databricks-apps-resource-permission-levels.md) — The framework for declaring and consuming resources
- Databricks Apps Service Principal — The identity used to access resources
- Application Configuration and Environment Variables — General guidance on environment variable management in Databricks Apps

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
