---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d147c7d4b688287ee6b2d6c458320931a5190c47ee6887ff5d8bb0469ec8da21
  pageDirectory: concepts
  sources:
    - mlflow-3-traditional-ml-workflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-vs-logged-model-distinction
    - MRVLMD
  citations:
    - file: mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md
title: MLflow Run vs Logged Model distinction
description: MLflow 3 separates the concept of a Run (training/evaluation job execution) from a Logged Model (the persistent model artifact with its own metadata lifecycle), enabling clearer tracking across training, evaluation, and deployment.
tags:
  - mlflow
  - model-lifecycle
  - machine-learning
timestamp: "2026-06-19T19:37:46.281Z"
---

# [MLflow Run](/concepts/mlflow-run.md) vs Logged Model Distinction

In [MLflow 3](/concepts/mlflow-3.md), a clear separation exists between an **MLflow Run** and an **MLflow Logged Model**. Understanding this distinction is essential for navigating the model development lifecycle on Databricks.

## Overview

An [MLflow Run](/concepts/mlflow-run.md) represents a single execution of a machine learning workflow—such as a training job—that tracks parameters, metrics, and artifacts. An MLflow Logged Model is the **trained model artifact** produced by that run, which can be independently tracked, registered, and compared across experiments. ^[mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md]

> "The example notebook runs a model training job, which is tracked as an [MLflow Run](/concepts/mlflow-run.md), to produce a trained model, which is tracked as an MLflow Logged Model." ^[mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md]

## Key Distinctions

| Aspect | [MLflow Run](/concepts/mlflow-run.md) | MLflow Logged Model |
|--------|------------|----------------------|
| **What it represents** | A single training or evaluation execution | A trained model artifact (e.g., an `elasticnet` model) |
| **UI location** | **Runs** tab on the experiment page | **Models** tab on the experiment page |
| **Lifecycle role** | Contains the provenance, parameters, and metrics of a specific job | Serves as a versionable, deployable unit that can be registered to [Unity Catalog](/concepts/unity-catalog.md) |
| **Relationship** | A run *produces* a logged model; the logged model retains a reference to its source run | A logged model is linked to one or more runs (e.g., training run and evaluation run) |

In the [MLflow UI](/concepts/mlflow.md), the experiment page shows two primary tabs: **Runs** and **Models**. The Runs tab lists all executed runs (training, evaluation, etc.). The Models tab shows all `LoggedModel` objects tracked within that experiment, along with aggregated parameters and metrics from the runs that produced or evaluated them. ^[mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md]

## Role in the MLflow UI

When you open an experiment in the MLflow UI:

- The **Runs** tab displays individual runs, each with its own parameters, metrics, and artifacts.
- The **Models** tab displays a consolidated view of logged models, including all parameters and metrics linked from the training and evaluation runs. Clicking a model name reveals details such as its source run, relevant datasets, and any model versions registered to Unity Catalog. ^[mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md]

The **Models** tab is distinct from the model version page in [Catalog Explorer](/concepts/catalog-explorer.md). The Models tab presents results from a single experiment, while the Catalog Explorer page shows a model’s performance across all linked environments (workspaces, endpoints, and experiments) and is intended for monitoring and deployment review. ^[mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md]

## Role in the Model Lifecycle

- **MLflow Run** is the unit of *tracking*: it captures all the details of a single training or evaluation job.
- **MLflow Logged Model** is the unit of *comparison, registration, and deployment*. From the Models tab, users can select model versions to register to Unity Catalog for possible deployment. When a logged model is registered, its version page in Catalog Explorer aggregates performance data from all linked runs and environments, making it suitable for approval workflows in deployment jobs. ^[mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md]

## Related Concepts

- [MLflow Run](/concepts/mlflow-run.md) – Detailed view of a single tracking execution.
- [MLflow Logged Model](/concepts/mlflow-logged-model.md) – Deeper dive into the logged model artifact.
- [Unity Catalog](/concepts/unity-catalog.md) – Central repository for registering and managing model versions.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI for viewing model version details across workspaces.
- Model Version – A specific version of a logged model registered to Unity Catalog.
- [MLflow 3](/concepts/mlflow-3.md) – The version of MLflow that introduced the formal Logged Model abstraction.

## Sources

- mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md

# Citations

1. mlflow-3-traditional-mlflow-workflow-databricks-on-aws.md
