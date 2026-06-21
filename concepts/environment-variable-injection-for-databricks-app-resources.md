---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 861f5ddb1809d776aea57f621115730e98a91a14959e0444cf580081cc103099
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - environment-variable-injection-for-databricks-app-resources
    - EVIFDAR
    - Environment variables in Databricks Apps
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Environment Variable Injection for Databricks App Resources
description: The mechanism by which Databricks exposes resource identifiers (such as experiment IDs) as environment variables in deployed apps, accessible via the valueFrom field in app.yaml.
tags:
  - databricks
  - configuration
  - environment-variables
timestamp: "2026-06-19T21:58:06.880Z"
---

# Environment Variable Injection for Databricks App Resources

**Environment Variable Injection for Databricks App Resources** is a mechanism that automatically exposes resource identifiers (such as experiment IDs) as environment variables in a Databricks Apps runtime. When you deploy an app that includes one or more resources (for example, an [MLflow experiments|MLflow experiment](/concepts/mlflow-experiment.md)), Databricks injects the resource’s ID into the app’s environment so that application code can reference it without hardcoding values. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## How it works

The injection is configured in the `app.yaml` file using the `valueFrom` field. You map an environment variable name to a custom resource key that you defined when adding the resource to the app. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

For example, if you add an MLflow experiment resource with the default resource key `experiment`, you can expose its ID as an environment variable named `MLFLOW_EXPERIMENT_ID`:

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment # Use your custom resource key if different
```

When the app is deployed, Databricks sets `MLFLOW_EXPERIMENT_ID` to the actual experiment ID. If you specified a custom resource key (instead of the default `experiment`), you use that key in the `valueFrom` field. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Accessing injected variables in application code

In your app’s source code, you read the environment variable using standard runtime methods. For instance, in Python you would use `os.getenv()`:

```python
import os
import mlflow

experiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")
mlflow.set_experiment(experiment_id=experiment_id)
```

This allows the app to use the resource without embedding static identifiers. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Scope and applicability

The injection pattern applies to Databricks App resources that expose an identifier or connection string. The source material documents this for [MLflow experiments](/concepts/mlflow-experiment.md), but the same `valueFrom` mechanism is available for other resource types (subject to their own documentation). Only resources added to the app through the **App resources** section are eligible for injection. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related concepts

- Databricks Apps – The platform for deploying AI applications.
- [MLflow experiments](/concepts/mlflow-experiment.md) – A resource type that can be added to an app and injected.
- app.yaml configuration – The deployment manifest where environment variables are declared.
- Service principal authorization – Permissions granted to the app’s service principal for each resource.
- Resource keys – Custom identifiers used to reference resources in `valueFrom`.

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
