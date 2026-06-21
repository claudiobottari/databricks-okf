---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a263add057f5c1b425c60b7602d95892d37d861dd24fceb6cc30d9a6481ccadb
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-installation
    - M3I
    - MLflow 3 Installation and Setup
  citations:
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
title: MLflow 3 Installation
description: Instructions for installing MLflow 3 by upgrading to version 3.0 or above using pip.
tags:
  - mlflow
  - installation
  - databricks
timestamp: "2026-06-19T10:45:34.202Z"
---

# MLflow 3 Installation

**MLflow 3 Installation** refers to the process of upgrading to MLflow version 3.0 or later within a Databricks environment to access new features for traditional machine learning, deep learning, and GenAI application development. MLflow 3 introduces enhanced experiment tracking, model management, evaluation, and production deployment capabilities while preserving core concepts from MLflow 2.x. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Overview

MLflow 3 is divided into two broad areas: **MLflow 3 for Models**, which delivers state-of-the-art experiment tracking, performance evaluation, and production management for machine learning models, and **MLflow 3 for GenAI**, which introduces tracing and observability, evaluation and monitoring, human feedback collection, and a Prompt Registry. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

Key new concepts in MLflow 3 include `LoggedModel`, which tracks a model’s lifecycle across different training and evaluation runs, and deployment jobs that manage model evaluation, approval, and deployment through Unity Catalog–governed workflows. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Installation Steps

To use MLflow 3, you must update the installed package to a version greater than or equal to 3.0. The following lines of code must be executed each time a notebook is run:

```python
%pip install mlflow>=3.0 --upgrade
dbutils.library.restartPython()
```

^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

The `%pip install mlflow>=3.0 --upgrade` command upgrades the MLflow library to the latest 3.x release, and `dbutils.library.restartPython()` restarts the Python kernel to ensure the updated package is loaded correctly.

## Version Requirements

MLflow 3 requires at least version 3.0.0 of the `mlflow` package. The command `mlflow>=3.0` ensures that the minimum version is satisfied and will upgrade from any earlier 2.x release. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Post-Installation Considerations

After upgrading, be aware of the following changes that affect how you interact with MLflow:

- **Logging Models:** The `artifact_path` parameter (used in MLflow 2.x) has been deprecated in favor of `name`. You can now log a model without first starting a run. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Model Artifacts Location:** Model artifacts are now stored under a model-specific path (`experiments/<experiment_id>/models/<model_id>/artifacts/`) instead of under the run’s artifact path. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Model Registry URI:** The default registry URI is now `databricks-uc`, directing model registration to the [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md). If you need to continue using the Workspace Model Registry, set the registry URI to `databricks` via `mlflow.set_registry_uri("databricks")` or the environment variable `MLFLOW_REGISTRY_URI`. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Deprecated APIs:** `mlflow.evaluate` has been deprecated in favor of `mlflow.models.evaluate` (for traditional/ deep learning) and `mlflow.genai.evaluate` (for GenAI). The `run_uuid` attribute has been removed from `RunInfo`; use `run_id` instead. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Compatibility:** MLflow 3 clients can load all runs, models, and traces logged with MLflow 2.x. However, resources logged with MLflow 3 may not be loadable by older 2.x clients. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- **Spark Model Logging:** `mlflow.spark.log_model` continues to work but does not use the new `LoggedModel` concept; it remains compatible with MLflow 2.x runs and artifacts. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) — Tracing, evaluation, monitoring, and prompt management features.
- [MLflow 3 for Models](/concepts/mlflow-3-for-models.md) — Experiment tracking and model management for traditional ML and deep learning.
- [MLflow LoggedModel](/concepts/mlflow-loggedmodel.md) — The new first-class model object tracking lifecycle performance.
- [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md) — Unity Catalog–governed workflows for model evaluation and deployment.
- [Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) — Default registry for managing model versions.
- Databricks Notebooks — The environment where installation commands are executed.
- dbutils — Databricks utility library, used here to restart the Python kernel after package upgrade.

## Sources

- get-started-with-mlflow-3-for-models-databricks-on-aws.md

# Citations

1. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
