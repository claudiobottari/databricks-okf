---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbef175c6d5043a2d3fc5426977193b63190afa1821bc508c58f2f12fe0e4dcc
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - resource-key-customization
    - RKC
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Resource Key Customization
description: The ability to specify a custom resource key when adding a resource to a Databricks App, which controls how the resource is referenced in app configuration and environment variable injection.
tags:
  - databricks-apps
  - configuration
  - resource-management
timestamp: "2026-06-18T14:18:50.113Z"
---

# Resource Key Customization

**Resource Key Customization** refers to the ability to specify a custom identifier — a resource key — when adding an [MLflow Experiment](/concepts/mlflow-experiment.md) as a resource to a Databricks App. The resource key is used to reference the experiment from within the app’s configuration and environment variables.

## Overview

When a developer adds an [MLflow Experiment](/concepts/mlflow-experiment.md) resource to a Databricks App, they can optionally provide a custom resource key. This key acts as the name by which the app references the resource in its configuration. If no custom key is supplied, the system uses a default key. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Default Key

The default resource key for an MLflow experiment resource is `experiment`. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Customizing the Key

During the resource creation or editing process (under **App resources**), you can specify a custom resource key. This is useful when an app includes multiple MLflow experiment resources or when a more descriptive name improves readability in the app configuration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

The custom key must be unique within the app’s resource set.

## Usage in Environment Variables

When the app is deployed, the experiment ID is exposed through environment variables. In the `app.yaml` file, the `valueFrom` field references the resource key. If a custom key was set, that key must be used in the `valueFrom` declaration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example configuration:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment # Use your custom resource key if different
```

If a custom key such as `my-training-experiment` was assigned, the `valueFrom` would be `my-training-experiment` instead of `experiment`. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- Use descriptive keys that clearly identify the purpose of the experiment (e.g., `churn-model-exp`, `production-eval`).
- Ensure the key is consistent across the app configuration and environment variable mappings.
- When an app has multiple experiment resources, give each a unique custom key to avoid confusion. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps — The deployment platform that uses resource keys
- [MLflow experiments](/concepts/mlflow-experiment.md) — The objects being referenced by the resource key
- [Environment variables in Databricks Apps](/concepts/environment-variable-injection-for-app-resources.md) — How resource keys are used to inject values into the app runtime
- App configuration (app.yaml) — The file where resource keys are referenced

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
