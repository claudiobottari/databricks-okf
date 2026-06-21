---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 812f02477ff5137534c800055bbcef540d86ba864d55ce3d9a440d3fbb57eca8
  pageDirectory: concepts
  sources:
    - machine-learning-lifecycle-databricks-on-aws.md
    - track-model-development-using-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-tracking
    - MLflow Run Tracking
    - MLflow Tracking API
    - MLflow Tracking Runs
    - MLflow tracking runs
    - MLflow Tracking UI
    - MLflow Tracking methods
    - Tracking API
  citations:
    - file: track-model-development-using-mlflow-databricks-on-aws.md
    - file: machine-learning-lifecycle-databricks-on-aws.md
title: MLflow Tracking
description: Experiment tracking system for logging parameters, metrics, artifacts, and model provenance (dataset, code, environment) across training runs, enabling reproducibility, comparison, and deployment.
tags:
  - machine-learning
  - experiment-tracking
  - mlflow
timestamp: "2026-06-19T19:20:58.954Z"
---

# MLflow Tracking

**MLflow Tracking** is the core component of [MLflow](/concepts/mlflow.md) that logs and organizes metadata from machine learning and deep learning experiments. It allows you to record parameters, metrics, tags, and artifacts associated with model training runs, and to compare results across runs to identify the best-performing configurations. ^[track-model-development-using-mlflow-databricks-on-aws.md] Databricks provides a hosted MLflow tracking server that stores experiment data directly in the workspace with no setup required. ^[track-model-development-using-mlflow-databricks-on-aws.md]

## Experiments, Runs, and Models

MLflow Tracking structures the model development process around three core entities: **experiments**, **runs**, and **models**. ^[track-model-development-using-mlflow-databricks-on-aws.md]

- **Experiment** – A collection of related runs. Within an experiment you can filter and compare runs to understand how parameter settings, input data, and other factors affect model performance. ^[track-model-development-using-mlflow-databricks-on-aws.md]
- **Run** – A single execution of model code. During a run, you can log parameters, metrics, tags, and artifacts. ^[track-model-development-using-mlflow-databricks-on-aws.md]
- **Logged Model** – In MLflow 3, `LoggedModel` elevates the concept of a model produced by a run to a distinct entity, enabling lifecycle tracking across different training and evaluation runs. A model is a collection of artifacts representing a trained machine learning model. ^[track-model-development-using-mlflow-databricks-on-aws.md]

For more details, see [MLflow experiments](/concepts/mlflow-experiment.md), [MLflow runs](/concepts/mlflow-run.md), and [MLflow Logged Models](/concepts/mlflow-loggedmodel.md).

## Tracking API

The [MLflow Tracking API](https://mlflow.org/docs/latest/tracking.html) provides Python, Java, and R interfaces for logging parameters, metrics, tags, and artifacts. The API communicates with an MLflow tracking server; when using Databricks, the hosted server logs the data automatically. ^[track-model-development-using-mlflow-databricks-on-aws.md]

MLflow is pre-installed on Databricks Runtime ML clusters. To use MLflow on a standard Databricks Runtime cluster, you must install the `mlflow` library. To take advantage of MLflow 3 features, upgrade to the latest version. ^[track-model-development-using-mlflow-databricks-on-aws.md]

## Logging Runs and Models

### Autologging

The easiest way to start tracking is **autologging**, which automatically logs training code written in many popular ML and deep learning frameworks (e.g., scikit-learn, TensorFlow, PyTorch). When autologging is enabled, parameters, metrics, and model artifacts are logged without manual API calls. ^[track-model-development-using-mlflow-databricks-on-aws.md] See [MLflow Autologging](/concepts/mlflow-autologging.md) for supported libraries.

### Logging API

For finer control, use the MLflow logging API to explicitly log parameters, metrics, and additional artifacts such as CSV files or plots. ^[track-model-development-using-mlflow-databricks-on-aws.md]

### Where Runs Are Logged

By default, when you train a model in a Databricks notebook, runs are logged to the **notebook experiment**. You can also log runs to a **workspace experiment** by calling `mlflow.set_experiment()`. The tracking URI determines which MLflow server is used; the default points to the current Databricks workspace, but you can connect to a remote workspace by setting a different URI. ^[track-model-development-using-mlflow-databricks-on-aws.md]

```python
import mlflow

# Connect to a different tracking server
mlflow.set_tracking_uri("databricks://remote-workspace-url")

# Set the experiment
mlflow.set_experiment("/Shared/my-experiment")
```

For more information, see Choose where MLflow data is stored.

## Analyzing Runs Programmatically

[MLflow Run](/concepts/mlflow-run.md) data can be accessed programmatically via two DataFrame APIs:

- **MLflow Python client `search_runs`** – returns a pandas DataFrame.
- **Read MLflow experiments data source** – returns an Apache Spark DataFrame. ^[track-model-development-using-mlflow-databricks-on-aws.md]

These APIs let you build dashboards or perform custom analysis, such as tracking evaluation metrics over time or counting runs per user. See [Build dashboards with MLflow metadata in system tables](/concepts/mlflow-dashboards-from-system-tables.md).

## Resource Limits

Starting March 27, 2024, MLflow imposes quota limits on total parameters, tags, metric steps per run, and total runs per experiment. If you hit the runs-per-experiment quota, use the [delete runs API](https://docs.databricks.com/aws/en/mlflow/runs#bulk-delete) to remove unnecessary runs. For other limits, adjust your logging strategy. To request a limit increase, contact your Databricks account team. ^[track-model-development-using-mlflow-databricks-on-aws.md] See Databricks resource limits.

## Variation in Training Results

Many ML algorithms contain stochastic elements (e.g., sampling, random initialisation), so results may vary between runs even under identical conditions. Use PySpark functions like `repartition` and `sortWithinPartitions` to control variation caused by data ordering and partitioning. ^[track-model-development-using-mlflow-databricks-on-aws.md]

## Role in the ML Lifecycle

MLflow Tracking is used during the **train models and track experiments** stage of the machine learning lifecycle. After exploring data and preparing features, you train models and log results with MLflow. The logged models can later be registered in the [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) for staging, testing, and production deployment. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- [MLflow runs](/concepts/mlflow-run.md)
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md)
- [MLflow Autologging](/concepts/mlflow-autologging.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Model Serving](/concepts/model-serving.md)
- [Feature Store](/concepts/feature-store.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- machine-learning-lifecycle-databricks-on-aws.md
- track-model-development-using-mlflow-databricks-on-aws.md

# Citations

1. [track-model-development-using-mlflow-databricks-on-aws.md](/references/track-model-development-using-mlflow-databricks-on-aws-fe722724.md)
2. [machine-learning-lifecycle-databricks-on-aws.md](/references/machine-learning-lifecycle-databricks-on-aws-d195211f.md)
