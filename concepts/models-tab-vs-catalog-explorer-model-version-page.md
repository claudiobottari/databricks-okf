---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44c786b93da3017b8c9b261c39d389375aa256933e516009a6b9a78e2cf11988
  pageDirectory: concepts
  sources:
    - mlflow-3-deep-learning-workflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - models-tab-vs-catalog-explorer-model-version-page
    - MTVCEMVP
  citations:
    - file: mlflow-3-deep-learning-workflow-databricks-on-aws.md
title: Models Tab vs Catalog Explorer Model Version Page
description: The Models tab on the MLflow experiment page focuses on comparing logged models for selection, while the Catalog Explorer model version page provides a holistic view for monitoring and deployment across environments.
tags:
  - mlflow
  - databricks
  - ui
  - model-lifecycle
timestamp: "2026-06-19T19:36:39.891Z"
---

# Models Tab vs Catalog Explorer Model Version Page

The **Models Tab** on the MLflow experiment page and the **Model Version Page** in Catalog Explorer both display information about models, but serve different roles in the model development and deployment lifecycle. Understanding their differences helps practitioners choose the right view for their task. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Models Tab (Experiment Page)

The **Models Tab** is located on the [MLflow experiments|MLflow experiment page](/concepts/mlflow-experiment.md). It presents the results of logged models from a single experiment on one page. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

### Primary Use

This view is designed for **model comparison and selection**. The Charts tab on this page provides visualizations to help you compare logged models and select the best model versions to register to [Unity Catalog](/concepts/unity-catalog.md) for potential deployment. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

### Key Capabilities

- Displays all [checkpoint models](/concepts/mlflow-loggedmodel.md) from a training run, along with their accuracy metrics, parameters, and metadata. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]
- From this tab, you can click a model to view its details page and then register it to Unity Catalog using the **Register model** button. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]
- Supports ranking and filtering logged models via the search API using `mlflow.search_logged_models()`. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Model Version Page (Catalog Explorer)

The **Model Version Page** is accessed through [Catalog Explorer](/concepts/catalog-explorer.md) and provides an overview of all model performance and evaluation results for a registered model version. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

### Primary Use

This view is designed for **monitoring and deployment**. It shows model parameters, metrics, and traces across all linked environments, including different workspaces, endpoints, and experiments. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

### Key Capabilities

- Aggregates data from multiple environments, making it useful for understanding model behavior in production. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]
- Works especially well with [deployment jobs](/concepts/mlflow-deployment-jobs.md), which create additional metrics that appear on this page. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]
- Approvers for deployment jobs can review this page to assess whether to approve the model version for deployment. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Comparison Summary

| Aspect | Models Tab (Experiment Page) | Model Version Page (Catalog Explorer) |
|--------|------------------------------|----------------------------------------|
| **Purpose** | Compare and select models for registration | Monitor and assess models for deployment |
| **Scope** | Single experiment | All linked environments (workspaces, endpoints, experiments) |
| **Key Action** | Register model to Unity Catalog | Approve model version for deployment |
| **Visualizations** | Charts tab for comparison | Aggregated metrics across environments |
| **Lifecycle Stage** | Development and selection | Monitoring and deployment |

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow LoggedModel](/concepts/mlflow-loggedmodel.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Deployment jobs](/concepts/mlflow-deployment-jobs.md)
- Model versioning

## Sources

- mlflow-3-deep-learning-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-deep-learning-workflow-databricks-on-aws.md](/references/mlflow-3-deep-learning-workflow-databricks-on-aws-71fc96e5.md)
