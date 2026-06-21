---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a32f0fca01b6f8a109374a95ff3501f987e1eb352393254d1aab815f675f578a
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scoped-resource-access-in-databricks-apps
    - SRAIDA
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Scoped Resource Access in Databricks Apps
description: The principle that adding a resource (like an MLflow experiment) to an app grants access only to that specific resource instance, not to all resources of that type in the workspace.
tags:
  - databricks
  - security
  - access-control
timestamp: "2026-06-19T21:58:16.413Z"
---

# Scoped Resource Access in Databricks Apps

**Scoped Resource Access in Databricks Apps** refers to the security model where a Databricks App's service principal is granted permissions only to the specific resources explicitly added to the app's configuration. This means the app can access and interact with only those workspace resources it has been explicitly authorized to use, rather than having broad, unrestricted access to all resources in the workspace. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## How Scoped Resource Access Works

When you define Databricks Apps resources in your app configuration (such as [MLflow experiments](/concepts/mlflow-experiment.md), [Unity Catalog](/concepts/unity-catalog.md) volumes, or [model serving endpoints](/concepts/model-serving-endpoint.md)), Databricks automatically grants the app's associated service principal the specified permissions on each selected resource. The app's service principal receives only the permissions you explicitly assign for each resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

For example, when you add an MLflow experiment as a resource:

- If you select **Can read** permission, the app's service principal can view experiment metadata, runs, parameters, and metrics — but cannot modify the experiment. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- If you select **Can edit** or **Can manage**, the service principal receives correspondingly broader access. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Benefits of Scoped Resource Access

- **Security by default**: Apps cannot access resources they don't need, reducing the attack surface. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Explicit access control**: You must deliberately choose which resources your app can use and what permissions it has on each. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **No automatic inheritance**: The app does not inherit other permissions the service principal may have — resource access is strictly limited to what is declared in the app's resource configuration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removing Resource Access

When you remove a resource from an app's configuration, the app's service principal immediately loses access to that resource. The resource itself remains unchanged and continues to be available to other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps Service Principal — The identity used by the app to access workspace resources.
- [App Resource Permissions](/concepts/app-resource-permission-levels.md) — The permission levels available for different resource types.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — A common resource type that supports scoped access for experiment tracking.
- [Environment Variables from Resources](/concepts/environment-variable-injection-for-app-resources.md) — How apps access resource IDs and connections through environment variables.

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
