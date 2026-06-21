---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8fb7ce71d8a657c9dd3f9c4babc2c3136711896a37a4a02d43e6c3a886df8f35
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - service-principal-authorization-for-databricks-apps
    - SPAFDA
    - Authorize service principal access to Databricks with OAuth
    - Service Principal Authorization
    - Service Principal Permissions for Apps
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Service Principal Authorization for Databricks Apps
description: The authorization model where Databricks Apps use a service principal, which is granted specific permissions to resources (like MLflow experiments) when those resources are added to the app.
tags:
  - databricks
  - authentication
  - security
timestamp: "2026-06-19T21:58:08.507Z"
---

# Service Principal Authorization for Databricks Apps

**Service Principal Authorization for Databricks Apps** refers to the mechanism by which a Databricks App’s service principal is granted permissions to access resources (such as [MLflow experiments](/concepts/mlflow-experiment.md)) when those resources are declared as part of the app’s configuration. This authorization model is declarative: adding a resource to an app causes Databricks to automatically grant the app’s service principal the specified permission level on that resource. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## How It Works

When you add a resource to a Databricks App — for example, an MLflow experiment — Databricks grants the app’s service principal the permissions you specify for that resource. The service principal is the identity under which the app runs; it authenticates and authorizes every API call the app makes to Databricks services. The grant happens automatically at deployment time and is scoped to the selected resource only. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Permission Levels

For MLflow experiments, the following permission levels are available when adding the resource:

- **Can read** – Grants the service principal permission to view experiment metadata, runs, parameters, and metrics. Suitable for apps that only display experiment results.
- **Can edit** – Grants permission to modify experiment settings and metadata.
- **Can manage** – Grants full administrative access to the experiment.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Scoping

Authorization is strictly scoped to the selected resource. The app’s service principal cannot access other resources unless they are added as separate resources to the same app. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md] This principle of least privilege ensures that an app only has access to the resources it explicitly declares.

## Resource Removal

When you remove a resource from an app, the app’s service principal loses access to that resource. The resource itself remains unchanged and continues to be available for other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps – The platform that uses service principal authorization for resource access.
- Service Principal – The identity used by a Databricks App to authenticate and authorize API calls.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – An example resource type that can be authorized via service principal permissions.
- Databricks App Resources – The mechanism for declaring which resources an app needs.

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
