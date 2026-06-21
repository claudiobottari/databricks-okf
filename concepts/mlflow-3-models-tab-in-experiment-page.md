---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffc939187024027a85dec05df810a26569f85cada29f807f0a0254cbfe7306d5
  pageDirectory: concepts
  sources:
    - mlflow-3-traditional-ml-workflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-models-tab-in-experiment-page
    - M3MTIEP
  citations:
    - file: mlflow-3-traditional-ml-workflow-databricks-on-aws.md
title: MLflow 3 Models tab in experiment page
description: A view showing all Logged Models produced by an experiment's runs, with a Charts tab for visual comparison of models before registering them to Unity Catalog for deployment.
tags:
  - mlflow
  - ui
  - experiment-tracking
timestamp: "2026-06-19T19:37:40.384Z"
---

# MLflow 3 Models Tab in Experiment Page

The **Models tab** on the [MLflow experiments|MLflow experiment page](/concepts/mlflow-experiment.md) provides a consolidated view of all [LoggedModel](/concepts/loggedmodel.md) objects produced during runs within that experiment. It displays model parameters, metadata, and metrics linked from both training and evaluation runs, enabling quick comparison of candidate models before registration to [Unity Catalog](/concepts/unity-catalog.md).^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Accessing the Models Tab

To open the Models tab:

1. Click **Experiments** in the workspace sidebar.
2. Find and click the desired experiment.
3. On the **Runs** page, click the **Models** tab.^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## What the Models Tab Shows

The tab lists every `LoggedModel` (e.g., `elasticnet` from a traditional ML workflow). For each model, the page shows:

- **Model name** – clickable to open the model details page.
- **Parameters** and **metadata**.
- **Metrics** aggregated from all linked training and evaluation runs.
- **Source run** – the run that produced the model.
- **Relevant datasets** used in evaluation.
- **Model versions** that have been registered in Unity Catalog.^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

The **Charts tab** (available on the same page) provides visualizations to help compare models and select the best version to register for deployment.^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Clicking a Model Name

Clicking a model name opens the **model details page**, which contains:

- Complete parameters and metrics.
- Source run link.
- Datasets used.
- Model versions registered in Unity Catalog.

From this page, clicking a model version takes you directly to the **model version page in [Catalog Explorer](/concepts/catalog-explorer.md)**, and clicking the source run returns you to the experiment’s run page.^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Comparison with Catalog Explorer’s Model Version Page

The Models tab on the experiment page and the model version page in Catalog Explorer serve different roles in the model lifecycle:^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

| Aspect | Models Tab (Experiment Page) | Model Version Page (Catalog Explorer) |
|--------|------------------------------|---------------------------------------|
| Purpose | Present logged models from a single experiment for comparison and selection. | Provide an overview of all model performance and evaluation results across linked environments (workspaces, endpoints, experiments). |
| Visualization | Includes the Charts tab for comparing models. | Shows metrics, parameters, and traces aggregated from multiple environments. |
| Use case | Experimentation and candidate selection. | Monitoring, deployment, and approval workflows (e.g., reviewing [deployment jobs](/concepts/mlflow-deployment-jobs.md)). |

The evaluation task in a deployment job creates additional metrics that appear on the Catalog Explorer page, where approvers can review model performance before approving a version for deployment.^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- [LoggedModel](/concepts/loggedmodel.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- model version
- [MLflow UI](/concepts/mlflow.md)
- [deployment jobs](/concepts/mlflow-deployment-jobs.md)

## Sources

- mlflow-3-traditional-ml-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-traditional-ml-workflow-databricks-on-aws.md](/references/mlflow-3-traditional-ml-workflow-databricks-on-aws-faedda9d.md)
