---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a297401732ec95ff265534a8db96a3d95f0cfd2fa14a707312a9253eeabbdfa0
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - active-experiment-in-mlflow
    - AEIM
    - Experiments (MLflow)
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Active Experiment in MLflow
description: Mechanism to control where MLflow runs are logged by setting an active experiment via set_experiment(), start_run(), or environment variables.
tags:
  - mlflow
  - experiments
  - tracking
timestamp: "2026-06-19T14:11:20.619Z"
---

## Active Experiment in MLflow

The **active experiment** in MLflow determines where all subsequent MLflow runs are logged. By setting an active experiment, you control the destination — typically a workspace's tracking server — for experiment metadata, parameters, metrics, and artifacts. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Default Behavior

By default, MLflow runs are logged to the workspace’s tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the notebook experiment associated with the current notebook. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Setting the Active Experiment

You can set the active experiment for all subsequent runs using one of the following methods:

- `mlflow.set_experiment()`
- `mlflow.start_run()`
- Environment variables

The most common approach is to call `mlflow.set_experiment()` with an experiment path. For example:

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

After this call, every `mlflow.start_run()` within the same Python process logs to `/Shared/my-experiment`. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Active Experiment for Remote Tracking

When logging to a remote MLflow tracking server (for example, a Databricks workspace different from the one you are currently running in), you must configure both the **tracking URI** and the **experiment path**. The active experiment is then set on the remote server: ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import mlflow

mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/centralized-experiments/my-project")
```

Subsequent runs are logged to that experiment on the remote server. Authentication methods such as Personal Access Tokens (PAT) or OAuth (service principals) are required for remote connections. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

### Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md) — The organizational unit for runs, parameters, and metrics.
- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) — The service that stores experiment data and model metadata.
- [Remote MLflow Tracking](/concepts/remote-mlflow-tracking-server.md) — Logging experiments to a tracking server in a different workspace.
- [MLflow Runs](/concepts/mlflow-run.md) — Individual executions of code under an experiment.
- Databricks Notebook Experiment — The default experiment automatically created for each notebook.

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
