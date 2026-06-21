---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6266265d503192a9d0e58ddd8140746aa40b90de29c77eba574ee2c17a9e1200
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-app-service-principal-authorization
    - DASPA
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Databricks App Service Principal Authorization
description: The mechanism by which Databricks grants a Databricks App's service principal specific permissions on resources like MLflow experiments, scoping access to only the explicitly added resources.
tags:
  - authentication
  - authorization
  - databricks-apps
timestamp: "2026-06-19T17:26:59.924Z"
---

## Databricks App Service Principal Authorization

**Databricks App Service Principal Authorization** is the mechanism by which a Databricks App authenticates and gains permissions to access workspace resources such as MLflow experiments. When you create a Databricks App, it is backed by a [service principal](/dev-tools/databricks-apps/auth#app-authorization) that acts as the app’s identity. All resource access requests made by the app go through this service principal. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### How Authorization Works

When you add a resource (for example, an [MLflow Experiment Resource](/concepts/mlflow-experiment-resource.md)) to a Databricks App, Databricks automatically grants the app’s service principal the specified permission level on that resource. The service principal then uses those permissions to interact with the resource on behalf of the app. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Permission Levels

The following permission levels are available when adding a resource:

- **Can read** – Allows the app to view resource metadata, runs, parameters, and metrics. Appropriate for apps that display experiment results.
- **Can edit** – Allows the app to modify resource settings and metadata.
- **Can manage** – Grants full administrative access to the resource.

All three levels are scoped to the selected resource only. The app cannot access other resources of the same type unless they are added as separate resources with their own permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Environment Variable Injection

When the app is deployed with a resource, Databricks exposes the resource identifier (such as an experiment ID) through environment variables that the app can reference using the `valueFrom` field in `app.yaml`. This allows the app’s code to securely retrieve the resource ID without hardcoding it. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Removing a Resource

If you remove a resource from an app, the app’s service principal loses access to that resource. The resource itself remains unchanged and continues to be available to other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Related Concepts

- Databricks Apps
- Service Principal
- App Authorization
- [MLflow Experiment Resource](/concepts/mlflow-experiment-resource.md)
- Environment Variables in Databricks Apps

### Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
