---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b28a5be4e25b50653178bd1c56d2502af437ade9b7a8188de752cff059bb205
  pageDirectory: concepts
  sources:
    - mlflow-3-traditional-ml-workflow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-deployment-job
    - M3DJ
  citations:
    - file: mlflow-3-traditional-ml-workflow-databricks-on-aws.md
title: MLflow 3 deployment job
description: A Databricks job that evaluates and deploys model versions, creating additional metrics viewable on the Catalog Explorer model version page for approver review before deployment approval.
tags:
  - mlflow
  - deployment
  - ci-cd
timestamp: "2026-06-19T19:37:48.101Z"
---

# MLflow 3 Deployment Job

A **deployment job** in [MLflow 3](/concepts/mlflow-3.md) is a mechanism for approving and deploying model versions registered in [Unity Catalog](/concepts/unity-catalog.md). It integrates with the model version page in [Catalog Explorer](/concepts/catalog-explorer.md) to provide a unified view of model performance and evaluation results across linked environments, such as different workspaces, endpoints, and experiments. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Overview

The model version page in Catalog Explorer shows model parameters, metrics, and traces from all connected environments. This centralized view is especially useful for monitoring and deployment workflows, and works well with deployment jobs. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Evaluation Task

A deployment job includes an evaluation task. When the evaluation task runs, it creates additional metrics that appear on the model version page in Catalog Explorer. The approver of the deployment job can then review these metrics alongside the rest of the model version information to decide whether to approve the model version for deployment. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Relationship to Other MLflow 3 Components

- The [MLflow Logged Model](/concepts/mlflow-logged-model.md) track records a trained model during an [MLflow Run](/concepts/mlflow-run.md).
- MLflow experiments display logged models on the **Models** tab, which provides visualizations on the **Charts** tab to help compare models and select versions to register in Unity Catalog.
- Once a model version is registered, the deployment job workflow uses the Catalog Explorer model version page as the single source of truth for review and approval.

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- [MLflow Logged Model](/concepts/mlflow-logged-model.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Model version page
- Evaluation task

## Sources

- mlflow-3-traditional-ml-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-traditional-ml-workflow-databricks-on-aws.md](/references/mlflow-3-traditional-ml-workflow-databricks-on-aws-faedda9d.md)
