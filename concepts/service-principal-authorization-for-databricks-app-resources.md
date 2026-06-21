---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f2e851716bbbed4c0b8af1e915f2edf311ec49d536ad8325a713fdae7749af0
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - service-principal-authorization-for-databricks-app-resources
    - SPAFDAR
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Service Principal Authorization for Databricks App Resources
description: The authorization model where Databricks grants an app's associated service principal specific permissions on linked resources, scoping access to only those explicitly added resources.
tags:
  - databricks
  - authentication
  - authorization
  - security
timestamp: "2026-06-18T10:41:48.882Z"
---

# Service Principal Authorization for Databricks App Resources

**Service Principal Authorization for Databricks App Resources** is the mechanism by which Databricks Apps use service principals to authenticate and gain permissions to access workspace resources such as MLflow experiments, models, and other Databricks assets. When you add a resource to a Databricks app, Databricks automatically grants the app's associated service principal the specified permissions on that resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## How It Works

Each Databricks App is associated with a service principal that acts as the app's identity for accessing workspace resources. When you add a resource to your app (such as an MLflow experiment, model, or other supported resource type), you specify a permission level for the app's service principal on that resource. Databricks provisions the service principal with the specified permissions, enabling the app to interact with the resource programmatically. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Resource Permissions

When adding a resource to a Databricks app, you can choose from the following permission levels:

| Permission Level | Capabilities |
|---|---|
| **Can read** | Grants the app permission to view resource metadata, settings, and data. Use for apps that display or analyze existing resource content. |
| **Can edit** | Grants the app permission to modify resource settings and metadata. |
| **Can manage** | Grants the app full administrative access to the resource. |

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

The permission level you select determines what operations the app can perform on that resource through its service principal identity. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Resource Scoping

Access is scoped to the specific resource you add to the app. For example, when you add an MLflow experiment as a resource, the app's service principal is granted permissions only on that experiment. The app cannot access other experiments unless you add them as separate resources. This granular scoping follows the principle of least privilege. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variable Injection

When you deploy an app with a resource, Databricks exposes resource identifiers (such as experiment IDs) through environment variables. You can reference these variables in your application code using the `valueFrom` field in your `app.yaml` configuration. The environment variable name corresponds to the resource key you specify when adding the resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Example configuration for an MLflow experiment resource:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment # Use your custom resource key if different
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

**Using the injected environment variable in application code:**

```python
import os
import mlflow

# Access the experiment using the injected environment variable
experiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")

# Set the experiment for tracking
mlflow.set_experiment(experiment_id=experiment_id)
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removing a Resource

When you remove a resource from a Databricks app, the app's service principal loses its permissions on that resource. The resource itself remains unchanged and continues to be available to other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Resource Types

The following resource types can be added to Databricks apps and authorized via service principal permissions:

- **MLflow experiments** — For experiment tracking, run logging, and trace data access
- Additional resource types (models, etc.) as supported by the Databricks Apps resource framework

## Prerequisites

Before adding a resource to a Databricks app, review the app resource prerequisites for your workspace. These ensure that the resource and the app are properly configured for service principal authorization. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- **Use the minimum necessary permission level** for each resource. Prefer **Can read** for apps that only display data, and only use **Can manage** when the app requires full administrative access. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Use descriptive custom resource keys** to make your `app.yaml` configuration clearer and to avoid confusion when multiple resources of the same type are attached.
- **Organize experiments logically by project or model type** to improve discoverability when adding resources to apps. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Use consistent naming conventions** for runs and parameters across your organization. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps — The application platform that uses service principal authorization for resource access
- Service Principals — The identity used by Databricks Apps to authenticate and access resources
- [MLflow Experiments](/concepts/mlflow-experiment.md) — A common resource type that can be authorized via service principals
- [Databricks Apps Service Principal Authentication](/concepts/databricks-apps-service-principal-authorization.md) — The broader authentication model for Databricks Apps
- Environment Variables in Databricks Apps — How resource identifiers are injected into app environments

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
