---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f981bde075592443f09934438dd3b1e56e98396369181f39758f3a9bd1e6922
  pageDirectory: concepts
  sources:
    - mlflow-3-deep-learning-workflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-experiment-page-models-tab
    - M3EPMT
  citations:
    - file: mlflow-3-deep-learning-workflow-databricks-on-aws.md
title: MLflow 3 Experiment Page Models Tab
description: A UI view in MLflow 3 experiments that displays all logged checkpoint models from a run, with metrics, parameters, and visualization tools for model comparison.
tags:
  - mlflow
  - ui
  - experiment-tracking
  - deep-learning
timestamp: "2026-06-19T19:36:49.992Z"
---

# MLflow 3 Experiment Page Models Tab

The **Models tab** on the [MLflow experiments|MLflow experiment](/concepts/mlflow-experiment.md) page in [MLflow 3](/concepts/mlflow-3.md) provides a dedicated view of all [Logged Models](/concepts/loggedmodel.md) produced by runs within that experiment. It is primarily designed to help practitioners compare checkpoint models from deep learning training jobs and decide which model version to promote to [Unity Catalog](/concepts/unity-catalog.md) for deployment. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## What the Models Tab Displays

After running a deep learning training job that logs checkpoints (e.g., every 10 epochs), each checkpoint appears as an individual entry on the Models tab. For every logged model, the tab shows:

- The model’s accuracy (or other logged metrics)
- All logged parameters
- Associated metadata

This layout allows you to quickly assess which checkpoints performed best and to investigate the corresponding run details. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Accessing the Models Tab

1. Open the MLflow experiment by navigating to **Experiments** in the workspace sidebar.
2. Locate your experiment (use the **Only my experiments** filter or the search box as needed).
3. Click the experiment name to open the **Runs** page.
4. Click the **Models** tab to see the list of logged checkpoint models.

From the Models tab you can click on any model entry to open its detail page. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Registering a Model from the Models Tab

From the model detail page (reached by clicking on a model name), you can register that model to Unity Catalog:

1. Click **Register model** in the upper‑right corner.
2. Choose **Unity Catalog** as the target.
3. Select an existing registered model from the drop‑down or type a new name.
4. Click **Register**.

> **Note:** Registration may take a few minutes to appear in the UI. Do not press **Register model** more than once, otherwise you will register duplicate models.

^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Using the Models Tab with the API

You can also rank logged models programmatically using `mlflow.search_logged_models()`. For example, to order checkpoint models by accuracy:

```python
ranked_checkpoints = mlflow.search_logged_models(
    output_format="list",
    order_by=[{"field_name": "metrics.accuracy", "ascending": False}]
)
best_checkpoint = ranked_checkpoints[0]
```

This API returns `LoggedModel` entities that correspond to the entries shown on the Models tab. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Comparison with Catalog Explorer

Both the Models tab of the experiment page and the model version page in [Catalog Explorer](/concepts/catalog-explorer.md) display similar information about a model, but they serve different roles in the development and deployment lifecycle:

| Aspect | Models Tab (Experiment Page) | Model Version Page (Catalog Explorer) |
|--------|-----------------------------|----------------------------------------|
| Purpose | Compare logged models from a single experiment and select a candidate to register. | Provide an overview of a model version’s performance, metrics, and traces across all linked environments (workspaces, endpoints, experiments). |
| Visualizations | Includes a Charts tab|Charts tab for comparing models visually. | Shows evaluation results from [deployment jobs](/concepts/mlflow-deployment-jobs.md) and other sources. |
| Workflow | Used during experimentation to choose checkpoints to register. | Used during monitoring, deployment, and approval of model versions. |

The Models tab is ideal for the early stage of model development, while Catalog Explorer’s version page is better suited for later stages such as deployment and governance. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md)
- [Track and compare models using MLflow Logged Models](/concepts/mlflow-loggedmodel.md)
- [MLflow experiments](/concepts/mlflow-experiment.md)
- [LoggedModel](/concepts/loggedmodel.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Deployment jobs](/concepts/mlflow-deployment-jobs.md)
- Charts tab

## Sources

- mlflow-3-deep-learning-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-deep-learning-workflow-databricks-on-aws.md](/references/mlflow-3-deep-learning-workflow-databricks-on-aws-71fc96e5.md)
