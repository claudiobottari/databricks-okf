---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66d94c09ffdbd1320dd49bbab772f122f845a64d9fb85abfcad415fe79fbeec8
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - app-resource-permission-levels
    - ARPL
    - App Resource Permissions
    - app resource prerequisites
    - databricks-app-resource-permission-levels
    - DARPL
    - databricks-app-resource-permissions
    - DARP
    - Databricks Apps resources
    - databricks-apps-resource-permission-levels
    - Databricks Apps Resource Model
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: App Resource Permission Levels
description: Three-tiered permission model (Can read, Can edit, Can manage) for granting Databricks app service principals access to MLflow experiment resources.
tags:
  - databricks-apps
  - permissions
  - access-control
timestamp: "2026-06-18T14:18:39.740Z"
---

# App Resource Permission Levels

**App Resource Permission Levels** define the access rights that a Databricks App's service principal is granted when a resource is added to the app. Permissions are assigned when adding a resource and are scoped to the selected resource only.

## Permission Levels for MLflow Experiment Resources

When adding an [MLflow Experiment](/concepts/mlflow-experiment.md) as a resource to a Databricks App, you can choose from the following permission levels: ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

- **Can read**: Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results.
- **Can edit**: Grants the app permission to modify experiment settings and metadata.
- **Can manage**: Grants the app full administrative access to the experiment.

## How Permissions Are Applied

When you add an MLflow experiment resource, Databricks grants the app's service principal the specified permissions on the selected experiment. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

Access is **scoped to the selected experiment only**. The app cannot access other experiments unless they are added as separate resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removing a Resource

When you remove an MLflow Experiment resource from an app, the app's service principal loses access to the experiment. The experiment itself remains unchanged and continues to be available for other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps — The application platform that uses these resource permissions
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- Service principal — The identity used by the app for authentication
- App resource prerequisites — Requirements before adding resources
- [Access environment variables from resources](/concepts/environment-variable-injection-for-app-resources.md) — How to reference resources in app configuration

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
