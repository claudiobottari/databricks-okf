---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ac91e08811f233a9876ef0037442f4c945a28580b8a1e4318170526a36b5e6e
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-permission-levels-for-apps
    - MEPLFA
    - MLflow Experiment Permissions
    - MLflow Experiment permissions
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment Permission Levels for Apps
description: Three permission levels (Can read, Can edit, Can manage) that control what a Databricks App's service principal can do with a linked MLflow experiment resource.
tags:
  - permissions
  - mlflow
  - databricks-apps
timestamp: "2026-06-19T17:26:52.718Z"
---

---
title: MLflow Experiment Permission Levels for Apps
summary: The three permission levels (Can read, Can edit, Can manage) that Databricks Apps can be granted on an MLflow experiment resource, and how they control access to experiment data and operations.
sources:
  - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T16:00:00.000Z"
updatedAt: "2026-06-18T16:00:00.000Z"
tags:
  - databricks
  - mlflow
  - permissions
  - apps
aliases:
  - mlflow-experiment-permission-levels-for-apps
  - MEPLA
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Experiment Permission Levels for Apps

When you add an [MLflow Experiment](/concepts/mlflow-experiment.md) as a resource in a Databricks App, you must choose a permission level that defines what the app’s service principal can do with that experiment. The permission level is set when you add the resource and determines whether the app can view, modify, or administer the experiment. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Permission Levels

Three permission levels are available, each granting a different scope of access to the experiment and its data.

| Level | Description | Typical Use Case |
|-------|-------------|------------------|
| **Can read** | Grants the app permission to view experiment metadata, runs, parameters, and metrics. | Displaying experiment results in a dashboard or reporting tool. |
| **Can edit** | Grants the app permission to modify experiment settings and metadata, in addition to read access. | Applications that need to update experiment descriptions, tags, or run metadata. |
| **Can manage** | Grants the app full administrative access to the experiment, including the ability to change permissions, delete runs, or modify the experiment itself. | Applications that fully administer the experiment lifecycle. |

When you select a permission level, Databricks automatically grants your app's service principal those permissions on the chosen experiment. The app can then use the [MLflow Tracking API](/concepts/mlflow-tracking.md) to log runs and access data consistent with the granted level. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Access Scoping

Access is scoped to the selected experiment only. The app cannot access other experiments unless they are added as separate resources with their own permission levels. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps resource prerequisites
- [Databricks Apps authorization and service principals](/concepts/databricks-apps-service-principal-authorization.md)
- Environment variables for MLflow experiments in apps
- [MLflow experiment management](/concepts/mlflow-experiment.md)
- App.yaml configuration
- Remove an MLflow Experiment resource

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
