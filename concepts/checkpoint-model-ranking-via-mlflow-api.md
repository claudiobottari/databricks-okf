---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c085e966e3553d71346d831c428cad9efbe18f302d9da85162b4515ea42ee29e
  pageDirectory: concepts
  sources:
    - mlflow-3-deep-learning-workflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - checkpoint-model-ranking-via-mlflow-api
    - CMRVMA
  citations:
    - file: mlflow-3-deep-learning-workflow-databricks-on-aws.md
title: Checkpoint Model Ranking via MLflow API
description: Using mlflow.search_logged_models to rank checkpoint models by metrics like accuracy, enabling programmatic selection of the best-performing model version.
tags:
  - mlflow
  - api
  - model-ranking
  - deep-learning
timestamp: "2026-06-19T19:36:35.265Z"
---

# Checkpoint Model Ranking via MLflow API

The **Checkpoint Model Ranking via MLflow API** refers to the programmatic technique of ordering checkpoint models saved during an [MLflow Run](/concepts/mlflow-run.md) by a specified metric (such as accuracy) using the `mlflow.search_logged_models()` function. This approach enables users to programmatically identify the best or worst performing checkpoints without relying on the MLflow UI. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Overview

In MLflow 3, each checkpoint saved during a training run is tracked as a [MLflow LoggedModel](/concepts/mlflow-loggedmodel.md). When multiple checkpoints are logged in the same run, they can be searched, filtered, and ordered by any metric recorded at the checkpoint step. The `search_logged_models` API accepts an `order_by` parameter that accepts a list of field specifications, enabling ranking by metrics like `accuracy` in ascending or descending order. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## API Usage

The following Python example demonstrates ranking checkpoint models by accuracy and retrieving the best and worst checkpoints: ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

```python
ranked_checkpoints = mlflow.search_logged_models(
    output_format="list",
    order_by=[{"field_name": "metrics.accuracy", "ascending": False}]
)

best_checkpoint: mlflow.entities.LoggedModel = ranked_checkpoints[0]
print(best_checkpoint.metrics[0])
# <Metric: dataset_digest='9951783d', dataset_name='train', key='accuracy',
#  model_id='m-bba8fa52b6a6499281c43ef17fcdac84',
#  run_id='394928abe6fc4787aaf4e666ac89dc8a', step=90, timestamp=1730828771880,
#  value=0.9553571428571429>

worst_checkpoint: mlflow.entities.LoggedModel = ranked_checkpoints[-1]
print(worst_checkpoint.metrics[0])
# <Metric: dataset_digest='9951783d', dataset_name='train', key='accuracy',
#  model_id='m-88885bc26de7492f908069cfe15a1499',
#  run_id='394928abe6fc4787aaf4e666ac89dc8a', step=0, timestamp=1730828730040,
#  value=0.35714285714285715>
```

The `order_by` parameter specifies the metric name (`metrics.accuracy`) and direction (`ascending: False` for descending order). The result is a list of [LoggedModel](/concepts/loggedmodel.md) objects, where the first element is the highest‑scoring checkpoint and the last is the lowest. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Alternative: UI Ranking

The same ranking can be performed interactively in the [MLflow Experiments UI](/concepts/mlflow-experiment.md). The **Models** tab of an experiment page displays all saved checkpoint models along with their accuracy and other metadata. Users can visually compare models, use the Charts tab for visualizations, and register the best performing model to Unity Catalog from the model details page. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Comparison with Catalog Explorer

The **Models** tab on the experiment page and the model version page in [Catalog Explorer](/concepts/catalog-explorer.md) serve different roles. The experiment page focuses on comparing checkpoints from a single experiment to select versions for registration. In contrast, the Catalog Explorer model version page aggregates performance metrics and evaluation results across linked environments (workspaces, endpoints, and experiments), making it more suitable for monitoring and deployment approval workflows. ^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Related Concepts

- [MLflow LoggedModel](/concepts/mlflow-loggedmodel.md) – The entity representing a single checkpoint or model version in MLflow 3.
- [MLflow search_logged_models](/concepts/mlflow-loggedmodel.md) – API for searching and filtering logged models.
- Checkpoint tracking in MLflow – Mechanism for saving intermediate model snapshots during training.
- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) – Destination for registering and managing model versions.

## Sources

- mlflow-3-deep-learning-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-deep-learning-workflow-databricks-on-aws.md](/references/mlflow-3-deep-learning-workflow-databricks-on-aws-71fc96e5.md)
