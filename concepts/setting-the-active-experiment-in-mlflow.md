---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5be2972499ad87b651a7e01d7321fe6d99647cefdcdd79dd485ee79bddd02ca8
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - setting-the-active-experiment-in-mlflow
    - STAEIM
    - Set tracking URI and experiment
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Setting the active experiment in MLflow
description: How to control where MLflow runs are logged by setting the active experiment using mlflow.set_experiment(), mlflow.start_run(), or environment variables.
tags:
  - mlflow
  - experiments
  - tracking
timestamp: "2026-06-18T10:56:06.863Z"
---



# Setting the active experiment in MLflow

**Setting the active experiment** in MLflow controls where subsequent runs are logged within the tracking server's namespace. By default, all MLflow runs are logged to the workspace's tracking server using the **active experiment**. If no experiment is explicitly set, runs are logged to the notebook-associated experiment — the so-called [notebook experiment](/concepts/notebook-experiment-in-databricks.md). ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Methods for setting the active experiment

You can set the active experiment programmatically using `mlflow.set_experiment()`, or implicitly by passing an experiment parameter to `mlflow.start_run()`. Both approaches are valid; the choice depends on whether you want to establish a persistent default for a session or bind the experiment only to a specific run. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### `mlflow.set_experiment()`

The `mlflow.set_experiment()` function sets the experiment for all subsequent runs in the current Python process. It accepts an experiment name — which can be a workspace-relative path such as `"/Shared/my-experiment"` — or an experiment ID. If the named experiment does not exist, MLflow creates it automatically. Once set, every subsequent call to `mlflow.start_run()` logs to that experiment unless a different experiment is explicitly passed. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

### `mlflow.start_run()` with `experiment_id` or `experiment_name`

You can also specify the experiment directly when starting a run by passing the `experiment_id` or `experiment_name` keyword argument to `mlflow.start_run()`. This overrides any previously set active experiment for that single run without changing the default for subsequent runs in the same process. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
with mlflow.start_run(experiment_id="123456789"):
    mlflow.log_param("learning_rate", 0.01)
```

### Environment variables

An alternative mechanism is to set the `MLFLOW_EXPERIMENT_NAME` or `MLFLOW_EXPERIMENT_ID` environment variable before launching any MLflow code. When that variable is present, `mlflow.start_run()` uses the experiment it specifies, even if `mlflow.set_experiment()` has not been called. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Active experiment scope and lifecycle

Setting an active experiment is a **process-wide** operation. It persists for the lifetime of the Python interpreter unless overwritten by another call to `mlflow.set_experiment()` or by a different `MLFLOW_EXPERIMENT_NAME` / `MLFLOW_EXPERIMENT_ID` environment variable at process start. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

Within a single process, if you call `mlflow.start_run()` multiple times without an explicit experiment argument, each run is logged to the experiment that was most recently set via `mlflow.set_experiment()` (or to the notebook experiment if none was ever set). ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Default experiment for notebooks

In a Databricks notebook, if no `mlflow.set_experiment()` call has been made and no environment variable overrides the experiment, MLflow uses the **notebook experiment** — an experiment that is automatically associated with the running notebook. It is named after the notebook and lives under the workspace's experiment list. Chapter 8 explains how to locate and navigate to that experiment in the UI. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Remote tracking servers

When logging to a [Remote MLflow tracking server](/concepts/remote-mlflow-tracking-server.md), you must configure both the tracking URI and the experiment path before starting runs. The tracking URI points to the remote server's endpoint; the experiment path identifies which experiment on that server should receive the runs. The two are independent: you can set one without the other, but both are required for remote logging. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import mlflow

# Set the tracking URI to the remote server
mlflow.set_tracking_uri("databricks://remote-workspace-url")

# Set the experiment path in the remote server
mlflow.set_experiment("/Shared/centralized-experiments/my-project")

# All subsequent runs will be logged to the remote server
with mlflow.start_run():
    mlflow.log_param("model_type", "random_forest")
    mlflow.log_metric("accuracy", 0.95)
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core logging component that uses the active experiment
- [MLflow Experiments](/concepts/mlflow-experiment.md) — An overview of experiment creation and management
- [MLflow Runs](/concepts/mlflow-run.md) — The unit of logged data within an experiment
- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) — How the tracking server stores and manages experiment data
- [Notebook experiment](/concepts/notebook-experiment-in-databricks.md) — The default experiment for Databricks notebooks
- [Databricks-hosted tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md) — The default managed tracking server provided by Databricks
- [Remote MLflow tracking server](/concepts/remote-mlflow-tracking-server.md) — A tracking server outside the current workspace

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
