---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8cfb06e243a006c5ef12726ff4ff697f982e29d4bcf74d56a497dcf472ae6d09
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-app-resource-permission-levels
    - DARPL
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: Databricks App Resource Permission Levels
description: Three permission levels (Can read, Can edit, Can manage) that control an app's service principal access to a resource like an MLflow experiment.
tags:
  - databricks
  - permissions
  - app-resources
timestamp: "2026-06-19T08:51:52.745Z"
---

```markdown
---
title: Databricks App Resource Permission Levels
summary: Three permission tiers (Can read, Can edit, Can manage) that govern what an app's service principal can do with a bound MLflow experiment resource.
sources:
  - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:39:14.418Z"
updatedAt: "2026-06-18T10:39:14.418Z"
tags:
  - databricks
  - permissions
  - security
aliases:
  - databricks-app-resource-permission-levels
  - DARPL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks App Resource Permission Levels

When you add a resource to a Databricks Apps|Databricks app—such as an MLflow experiment, a model, or a secret—you must assign a permission level that determines what operations the app’s service principal can perform on that resource. Permission levels are resource‑specific; this page covers the levels available for **MLflow experiment** resources, which are representative of the general model. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Available Permission Levels for MLflow Experiment Resources

| Permission Level | Capabilities |
|-----------------|--------------|
| **Can read** | View experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results. |
| **Can edit** | Modify experiment settings and metadata. |
| **Can manage** | Full administrative access to the experiment (e.g., delete, change permissions). |

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## How Permissions Are Applied

When you add an MLflow experiment resource with a specified permission level, Databricks automatically grants the app’s service principal the corresponding privileges on that experiment. Access is scoped exclusively to the selected experiment—the app cannot access other experiments unless they are added as separate resources with their own permission assignments. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- Choose the minimum permission level needed for the app’s functionality. For example, use **Can read** when the app only needs to display experiment results, and reserve **Can manage** for administrative tools.
- Organise experiments logically by project or model type to simplify permission management.
- Use consistent naming conventions for runs and parameters across your organisation. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removing a Resource

When a resource is removed from the app, the app’s service principal loses all permissions on that resource. The resource itself remains unchanged and continues to be accessible to other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps — The platform for building and deploying applications
- Service Principal — The identity under which the app runs
- [[MLflow Experiment]] — A resource that can be attached to an app
- App Resource Configuration — How resources are declared in `app.yaml`

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
```

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
