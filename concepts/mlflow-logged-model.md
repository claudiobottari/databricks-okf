---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d940e5d036496ee1cd8b7989aa212839bca9f6e22234050b857f8c20cf13e855
  pageDirectory: concepts
  sources:
    - mlflow-3-traditional-ml-workflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-logged-model
    - MLM
  citations:
    - file: mlflow-3-traditional-ml-workflow-databricks-on-aws.md
title: MLflow Logged Model
description: A trained model tracked as a first-class entity in MLflow 3, capturing parameters, metrics, metadata, source runs, datasets, and model versions separately from MLflow Runs.
tags:
  - mlflow
  - model-registry
  - machine-learning
timestamp: "2026-06-19T19:38:20.341Z"
---

---
title: MLflow Logged Model
summary: A model artifact tracked within an MLflow experiment run, encapsulating its training parameters, evaluation metrics, source run, and linked datasets, introduced in MLflow 3.
sources:
  - mlflow-3-traditional-ml-workflow-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:14:08.234Z"
updatedAt: "2026-06-18T08:14:08.234Z"
tags:
  - mlflow
  - model-registry
  - experiment-tracking
aliases:
  - logged-model
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Logged Model

An **MLflow Logged Model** (referred to as `LoggedModel` in the MLflow 3 API) is a trained model artifact that is tracked as part of an [MLflow Run](/concepts/mlflow-run.md). The logged model captures the complete set of training parameters, metadata, evaluation metrics, and links to its source run and relevant datasets. It is the primary unit of model tracking in the MLflow 3 traditional ML workflow. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Overview

In the MLflow 3 traditional ML workflow, a model training job produces a trained model artifact. This artifact is tracked as an MLflow Logged Model. The logged model serves as a single, unified view that consolidates all information related to a particular model, including:

- Model parameters and hyperparameters.
- Performance metrics from both training and evaluation runs.
- Links to its source run (the run that produced the model).
- Links to relevant datasets used during training or evaluation.
- Registered model versions in [Unity Catalog](/concepts/unity-catalog.md).

^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Viewing the Logged Model

The logged model is visible on the **Models** tab of an MLflow experiment's **Runs** page. From there, a user can:

1. Click the **Experiments** link in the workspace sidebar.
2. Select an experiment and filter by `Only my experiments` or use the search box.
3. Navigate to the **Runs** page to see the two MLflow runs (one for training, one for evaluation).
4. Click the **Models** tab to see all logged models (`LoggedModel`) for that experiment.

Each logged model entry shows its parameters, metadata, and linked metrics. Clicking the model name opens a detailed model page with additional information such as its source run, datasets, and model versions registered in Unity Catalog. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Relationship to Unity Catalog

The logged model is registered to [Unity Catalog](/concepts/unity-catalog.md) during the MLflow 3 workﬂow. After registration, all model parameters and performance data are available on the model version page in Catalog Explorer. This page provides an overview of all model performance and evaluation results across linked environments, including different workspaces, endpoints, and experiments. It is especially useful for monitoring and deployment workflows. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

Clicking the model ID or source run on the Catalog Explorer model version page navigates back to the corresponding MLflow model page or run page, respectively. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Key Distinction: Models Tab vs. Catalog Explorer

The **Models** tab on the MLflow experiment page and the model version page in Catalog Explorer present similar information but serve different roles:

- **Models tab (experiment page):** Presents results of logged models from a single experiment. The Charts tab on this page provides visualizations to compare models and select versions to register for deployment.
- **Model version page (Catalog Explorer):** Provides a cross‑environment overview of all model performance and evaluation results, including metrics from deployment jobs. It is the review page for a job approver to assess whether to approve a model version for deployment.

^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Related Concepts

- [MLflow Run](/concepts/mlflow-run.md) – The container for a model training job that produces a logged model.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit that groups runs and logged models.
- [Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) – The system for managing model versions and lifecycle.
- [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md) – An alternative workﬂow for deep learning models.
- Track and Compare Models – Guidance on using logged models for model selection.
- [Deployment Job](/concepts/mlflow-deployment-jobs.md) – A job that generates additional metrics on the model version page.

## Sources

- mlflow-3-traditional-ml-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-traditional-ml-workflow-databricks-on-aws.md](/references/mlflow-3-traditional-ml-workflow-databricks-on-aws-faedda9d.md)
