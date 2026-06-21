---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8fad2ffb7add5f690adf1127fe1e308951531c4c630e5ea0fcfd641055b20868
  pageDirectory: concepts
  sources:
    - mlflow-3-traditional-ml-workflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-version-page-in-catalog-explorer
    - MVPICE
  citations:
    - file: mlflow-3-traditional-ml-workflow-databricks-on-aws.md
title: Model version page in Catalog Explorer
description: A Unity Catalog page providing an overview of all model performance and evaluation results across linked environments including different workspaces, endpoints, and experiments, used for monitoring, deployment, and approval workflows.
tags:
  - unity-catalog
  - mlflow
  - model-deployment
timestamp: "2026-06-19T19:37:39.245Z"
---

# Model version page in Catalog Explorer

**Model version page in Catalog Explorer** is a view in Databricks that provides an overview of all model performance and evaluation results for a specific model version registered in [Unity Catalog](/concepts/unity-catalog.md). It consolidates model parameters, metrics, and traces across linked environments, including different workspaces, endpoints, and experiments. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Navigation

You can access the model version page by clicking on the model version from the MLflow model page. Alternatively, you can navigate directly through [Catalog Explorer](/concepts/catalog-explorer.md) by selecting the model and its version. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Content

The page displays:

- Model parameters and metadata
- Model performance metrics
- Traces across linked environments
- Source run information
- Datasets used
- Registered model versions in Unity Catalog

It also shows metrics created by [deployment job|deployment jobs](/concepts/mlflow-deployment-jobs.md). The approver for the job can review this page to assess whether to approve the model version for deployment. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Comparison with the Models tab on the MLflow experiment page

The **Models tab of the [MLflow experiment page](/concepts/mlflow-experiment.md)** and the model version page in Catalog Explorer serve different roles in the model development and deployment lifecycle:

- The **Models tab** presents the results of logged models from an experiment on a single page. The Charts tab on that page provides visualizations to help compare models and select model versions to register to Unity Catalog for possible deployment.
- The **model version page in Catalog Explorer** provides an overview of all model performance and evaluation results. It shows model parameters, metrics, and traces across all linked environments, making it useful for monitoring and deployment, especially with deployment jobs.

^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Related Concepts

- [Catalog Explorer](/concepts/catalog-explorer.md)
- [MLflow experiment page](/concepts/mlflow-experiment.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [LoggedModel](/concepts/loggedmodel.md)
- MLflow model page
- Model version
- [Deployment job](/concepts/mlflow-deployment-jobs.md)
- Model lifecycle

## Sources

- mlflow-3-traditional-ml-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-traditional-ml-workflow-databricks-on-aws.md](/references/mlflow-3-traditional-ml-workflow-databricks-on-aws-faedda9d.md)
