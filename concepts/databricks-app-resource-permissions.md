---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d01ed925dd12bbd2f178d1529e9b3eec0b677075c8b27d77cf8fb9a08bfee3a
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-app-resource-permissions
    - DARP
    - Databricks Apps resources
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Databricks App Resource Permissions
description: Permission levels (Can read, Can edit, Can manage) that govern an app's service principal access to bound resources like MLflow experiments.
tags:
  - databricks
  - security
  - permissions
timestamp: "2026-06-19T21:57:57.866Z"
---

## Databricks App Resource Permissions

**Databricks App Resource Permissions** define the level of access an app has to a linked resource, such as an [MLflow Experiment](/concepts/mlflow-experiment.md). When you add a resource to a Databricks App, you must specify a permission level that controls what actions the app can perform on that resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Permission Levels

For an MLflow experiment resource, three permission levels are available:

- **Can read** – Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use this level for apps that only display experiment results.
- **Can edit** – Grants the app permission to modify experiment settings and metadata.
- **Can manage** – Grants the app full administrative access to the experiment.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### How Permissions Are Assigned

When you add a resource to an app (for example, during app creation or editing), Databricks automatically grants the app’s service principal the selected permissions on the specific resource. This assignment is scoped to that resource only; the app cannot access other resources of the same type unless they are added as separate resources with explicit permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

These permissions are not manually configurable outside the resource definition within the app. The service principal's access is managed entirely through the app's resource configuration.

### Removing a Resource and Revoking Permissions

When you remove a resource from an app, the app's service principal loses its permissions on that resource. The resource itself remains unchanged and continues to be available to other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Best Practices

- Assign the minimum permission level required for the app's functionality (principle of least privilege).
- Organize resources logically to reduce the number of resource declarations and simplify permission management.
- Regularly review the resources attached to each app and remove any that are no longer needed.
- Use consistent naming for resource keys to avoid confusion when referencing environment variables.

### Related Concepts

- Databricks Apps service principal
- [MLflow experiments](/concepts/mlflow-experiment.md)
- App resource configuration
- [Environment variables from app resources](/concepts/environment-variable-injection-from-app-resources.md)

### Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
