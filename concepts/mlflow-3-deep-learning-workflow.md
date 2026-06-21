---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 923fdcb9c6e40fde0bbb28ab9272014757e4e6afca3d635b5a4b98edadd1c514
  pageDirectory: concepts
  sources:
    - mlflow-3-deep-learning-workflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-deep-learning-workflow
    - M3DLW
    - MLflow 3 deep learning workflow notebook
  citations:
    - file: mlflow-3-deep-learning-workflow-databricks-on-aws.md
title: MLflow 3 Deep Learning Workflow
description: A workflow for training deep learning models with PyTorch on Databricks, using MLflow 3 to log checkpoints, track metrics, and register models to Unity Catalog.
tags:
  - mlflow
  - deep-learning
  - databricks
  - workflow
timestamp: "2026-06-19T19:36:41.865Z"
---

# MLflow 3 Deep Learning Workflow

**MLflow 3 Deep Learning Workflow** refers to the process of tracking, comparing, and registering deep learning model checkpoints using the enhanced model tracking capabilities introduced in MLflow 3. This workflow enables practitioners to track individual checkpoint models as LoggedModels within a single [MLflow Run](/concepts/mlflow-run.md), inspect their performance metrics, and selectively register the best-performing checkpoints to [Unity Catalog](/concepts/unity-catalog.md).

## Overview

Traditional MLflow workflows typically track one model per run. With MLflow 3's deep learning workflow, you can log multiple checkpoint models within a single training run. Each checkpoint is tracked as a [LoggedModel](/concepts/loggedmodel.md) with its own metrics, parameters, and metadata, enabling side-by-side comparison of model performance across training epochs. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

A typical deep learning workflow with MLflow 3 involves:

1. Running a deep learning training job (e.g., with PyTorch) and logging checkpoint models at regular intervals.
2. Using the MLflow UI to explore and compare checkpoint models by accuracy.
3. Registering the best-performing model to Unity Catalog.
4. Using the search API to programmatically rank and retrieve checkpoint models.

## Example Notebook

The example notebook demonstrates a single deep learning model training job with PyTorch, tracked as an [MLflow Run](/concepts/mlflow-run.md). It logs a checkpoint model after every 10 epochs, with each checkpoint tracked as an MLflow LoggedModel. The notebook installs the `scikit-learn` and `torch` libraries.

## Exploring Model Performance in the UI

After running the training notebook, checkpoint models are visible in the MLflow experiments UI:

1. Click **Experiments** in the workspace sidebar.
2. Find your experiment in the experiments list. You can filter by selecting **Only my experiments** or using the **Filter experiments** search box.
3. Click the experiment name to open the **Runs** page, which contains one [MLflow Run](/concepts/mlflow-run.md).
4. Click the **Models** tab to view individual checkpoint models. For each checkpoint, you can see the model's accuracy, parameters, and metadata.

## Registering a Model to Unity Catalog

You can register the best-performing model to Unity Catalog from the UI:

1. From the **Models** tab, click the name of the checkpoint model to register.
2. On the model details page, click **Register model** in the upper-right corner.

> **Tip:** It can take a few minutes for a model to appear in the UI after registering it. Do not press **Register model** more than once, otherwise you will register duplicate models.

3. Select **Unity Catalog** and either select an existing model name from the drop-down menu or type a new name.
4. Click **Register**.

## Ranking Checkpoint Models with the API

You can use `mlflow.search_logged_models()` to rank checkpoint models by accuracy or other metrics: ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

```python
ranked_checkpoints = mlflow.search_logged_models(
    output_format="list",
    order_by=[{"field_name": "metrics.accuracy", "ascending": False}]
)

best_checkpoint = ranked_checkpoints[0]
print(best_checkpoint.metrics[0])

worst_checkpoint = ranked_checkpoints[-1]
print(worst_checkpoint.metrics[0])
```

Each checkpoint model's metrics include the metric key, value, step (epoch), dataset name and digest, model ID, run ID, and timestamp. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Models Tab vs. Catalog Explorer

The **Models** tab on the experiment page and the model version page in [Catalog Explorer](/concepts/catalog-explorer.md) serve different roles in the model lifecycle: ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

| View | Purpose |
|------|---------|
| **Models tab** (experiment page) | Presents logged models from a single experiment. The Charts tab provides visualizations to help compare models and select versions to register to Unity Catalog for potential deployment. |
| **Catalog Explorer** (model version page) | Shows model performance and evaluation results across all linked environments, including different workspaces, endpoints, and experiments. Useful for monitoring and deployment, especially with [deployment jobs](/concepts/mlflow-deployment-jobs.md). Evaluation tasks in deployment jobs create additional metrics visible on this page. |

## Next Steps

- Learn more about [LoggedModel](/concepts/loggedmodel.md) tracking in [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).
- Explore the [MLflow 3 traditional ML workflow](/concepts/mlflow-3-traditional-ml-workflow.md) for traditional machine learning use cases.

## Sources

- mlflow-3-deep-learning-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-deep-learning-workflow-databricks-on-aws.md](/references/mlflow-3-deep-learning-workflow-databricks-on-aws-71fc96e5.md)
