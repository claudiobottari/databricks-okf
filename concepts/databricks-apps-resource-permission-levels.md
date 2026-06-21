---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c634102090c5637f5510dcc92cc1c3f227ba1589df1c62f5925775282797adfa
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-apps-resource-permission-levels
    - DARPL
    - Databricks Apps Resource Model
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Databricks Apps Resource Permission Levels
description: Three permission tiers (Can read, Can edit, Can manage) that control what a Databricks App can do with a bound resource like an MLflow experiment, from viewing metadata to full administrative access.
tags:
  - databricks-apps
  - permissions
  - access-control
timestamp: "2026-06-19T13:53:26.123Z"
---

# Databricks Apps Resource Permission Levels

**Databricks Apps Resource Permission Levels** define the access rights that a Databricks Apps|Databricks app’s service principal is granted when an [MLflow experiments|MLflow experiment](/concepts/mlflow-experiment.md) is added as a resource to the app. These permissions control what operations the app can perform on the experiment, such as viewing metadata, logging runs, or modifying settings.

## Overview

When you add an MLflow experiment as a resource to a Databricks app, you must select a permission level for the app’s service principal. The selected level determines the scope of access the app has to the experiment. Permissions are applied only to the chosen experiment; the app cannot access other experiments unless they are added as separate resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Permission Levels

Three permission levels are available when adding an MLflow experiment resource:

| Level      | Description |
|------------|-------------|
| **Can read**  | Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results. |
| **Can edit**  | Grants the app permission to modify experiment settings and metadata. |
| **Can manage** | Grants the app full administrative access to the experiment. |

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Can read

The `Can read` level is appropriate for apps that only need to retrieve experiment data, such as dashboards or reporting tools. The app can read runs, parameters, metrics, and artifacts, but cannot create new runs or modify the experiment. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Can edit

The `Can edit` level allows the app to modify experiment metadata and settings, in addition to read access. This level is suitable for apps that need to update experiment descriptions, tags, or other configuration, without requiring full administrative control. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Can manage

The `Can manage` level provides full administrative access, including the ability to delete the experiment or change permissions. Use this level sparingly, only for apps that require complete control over the experiment lifecycle. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## How Permissions Are Granted

When an MLflow experiment resource is added to a Databricks app, the platform automatically grants the app’s service principal the specified permissions on the selected experiment. This enables the app to interact with the experiment through the [MLflow Tracking API](/concepts/mlflow-tracking.md). The permission assignment is managed by Databricks and scoped strictly to the chosen experiment. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- Choose the **minimum permission level** required for the app’s functionality. Prefer `Can read` unless the app must log runs or modify experiment metadata.
- Use `Can manage` only when the app needs to administer the experiment (e.g., cleaning up old runs or adjusting permissions).
- Permissions are per-experiment; add separate resources for each experiment the app needs to access. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]


## Related Concepts

- Databricks Apps – The platform for deploying custom applications.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational unit for MLflow runs.
- Service principal – The identity used by a Databricks app for authorization.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) – The API for logging and retrieving experiment data.
- App resource prerequisites – Requirements for adding resources to a Databricks app.

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
