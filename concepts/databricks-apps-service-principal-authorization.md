---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15e57404b62f24df1025d578c3043c92fa4f4eb11ec9c05b7816f0474f94acbd
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-apps-service-principal-authorization
    - DASPA
    - Databricks Apps Service Principal Authentication
    - Databricks Apps authorization and service principals
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Databricks Apps Service Principal Authorization
description: The mechanism by which Databricks Apps use a service principal to obtain permissions on resources — when a resource is added, the app's service principal is granted the specified permissions on that resource.
tags:
  - databricks-apps
  - service-principal
  - authorization
  - security
timestamp: "2026-06-19T13:53:27.433Z"
---

Here is the wiki page for "Databricks Apps Service Principal Authorization", written based solely on the provided source material.

---

## Databricks Apps Service Principal Authorization

**Databricks Apps Service Principal Authorization** refers to the mechanism by which a Databricks app authenticates and is granted permissions to access workspace resources, such as [MLflow experiments](/concepts/mlflow-experiment.md), when deployed. Instead of using a user's personal credentials, each deployed Databricks app is associated with its own service principal, which governs the app's identity and access rights within the workspace. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### How it Works

When a resource, such as an MLflow experiment, is added to a Databricks app, Databricks automatically grants the app's service principal the specified permissions on that resource. This scoped access ensures the app can only interact with the resources explicitly attached to it. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Permission Levels

When adding a resource, you select the permission level for the app's service principal. For an MLflow experiment resource, the available levels are: ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

| Permission Level | Description |
|-----------------|-------------|
| **Can read** | Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results. |
| **Can edit** | Grants the app permission to modify experiment settings and metadata. |
| **Can manage** | Grants the app full administrative access to the experiment. |

### Scoped Access

Access is scoped to the selected resource only. Your app cannot access other experiments or resources unless they are added as separate resources to the app configuration. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Revoking Access

When a resource is removed from an app, the app's service principal loses access to that resource. The resource itself remains unchanged and continues to be available for other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Related Concepts

- Databricks Apps Resources
- Service Principal
- [MLflow experiments](/concepts/mlflow-experiment.md)
- Databricks Apps Environment Variables
- App Authentication and Authorization

### Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
