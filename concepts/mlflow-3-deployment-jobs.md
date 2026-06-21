---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2bbb0bee381675056c7d1d49b9e9ebf7738926aae00b3c4c604f83349ee42da
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-deployment-jobs
    - M3DJ
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
      start: 53
      end: 57
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
      start: 39
      end: 42
    - file: L53-L57
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
      start: 49
      end: 52
    - file: model-registry-improvements-with-mlflow-3-databricks-on-aws.md
title: MLflow 3 Deployment Jobs
description: Lakeflow Jobs-based workflows that manage the model lifecycle including evaluation, approval, and deployment steps, governed by Unity Catalog with full activity logging.
tags:
  - mlflow
  - machine-learning
  - deployment
  - mlops
timestamp: "2026-06-19T19:00:38.705Z"
---

# MLflow 3 Deployment Jobs

**MLflow 3 Deployment Jobs** are a new concept in MLflow 3 that uses [Lakeflow Jobs](/concepts/lakeflow-jobs.md) to orchestrate the model lifecycle — including steps like evaluation, approval, and deployment. These workflows are governed by [Unity Catalog](/concepts/unity-catalog.md), and all events are saved to an activity log that is displayed on the model version page in Unity Catalog. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md#L53-L57]

## Overview

Deployment jobs provide a structured, auditable mechanism for moving a model from development through production. They can include staged rollout and metrics collection, as illustrated by the deployment job UI showing steps such as evaluation, staged rollout, and production deployment. Because the jobs are governed by Unity Catalog, all events — approvals, rejections, rollouts, and metric thresholds — are recorded in an activity log that is accessible on the model version page. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md#L39-L42, L53-L57]

## Usage

To use deployment jobs, you define a model workflow (a Lakeflow job) that specifies the steps in the lifecycle. Common steps include:

- **Evaluation**: Running offline evaluations against a held-out dataset.
- **Approval**: Human or automated gate before promotion.
- **Staged rollout**: Gradually shifting traffic to a new model version, with metrics collection at each stage.
- **Deployment**: Final promotion to production serving endpoints.

All events from these steps are logged and visible in the model version page's activity log. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md#L39-L42, L53-L57]

## Relationship to Other MLflow 3 Features

Deployment jobs complement [MLflow Logged Models](/concepts/mlflow-loggedmodel.md), which capture metrics, parameters, and traces across development and evaluation. When a `LoggedModel` is promoted to a Unity Catalog model version, its performance data is visible on the same page where deployment job events are recorded. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md#L49-L52]

Deployment jobs also integrate with [Model Registry](/concepts/mlflow-model-registry.md) improvements in MLflow 3, such as unified trace views and cross-experiment metrics. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md] (Note: This citation is based on the source listed in the page metadata; the full content of that source was not provided.)

## Related Concepts

- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – The underlying job framework used to define and run deployment workflows.
- [Unity Catalog](/concepts/unity-catalog.md) – Governs model artifacts, permissions, and event logs.
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) – The model object that carries metrics, parameters, and traces across environments.
- [Model Registry](/concepts/mlflow-model-registry.md) – The Unity Catalog registry where model versions are stored and deployment logs are visible.
- [MLflow 3 for Models](/concepts/mlflow-3-for-models.md) – Overview of MLflow 3 features for traditional ML and deep learning.

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md
- model-registry-improvements-with-mlflow-3-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md:53-57](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
2. [get-started-with-mlflow-3-for-models-databricks-on-aws.md:39-42](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
3. L53-L57
4. [get-started-with-mlflow-3-for-models-databricks-on-aws.md:49-52](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
5. [model-registry-improvements-with-mlflow-3-databricks-on-aws.md](/references/model-registry-improvements-with-mlflow-3-databricks-on-aws-260d0089.md)
