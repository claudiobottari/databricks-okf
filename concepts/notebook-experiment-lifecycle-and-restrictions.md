---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 653c9fed7bca1346cac3ccfed340bba7a2b6ef1199b57a310777273049f49e1f
  pageDirectory: concepts
  sources:
    - organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - notebook-experiment-lifecycle-and-restrictions
    - Restrictions and Notebook Experiment Lifecycle
    - NELAR
  citations:
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
title: Notebook Experiment Lifecycle and Restrictions
description: Notebook experiments share name/ID with their notebook and cannot be independently deleted or renamed. Deleting a notebook experiment via UI or API also deletes the notebook. Git-folder notebook experiments can only be managed at the Git folder level.
tags:
  - mlflow
  - notebooks
  - experiment-lifecycle
timestamp: "2026-06-19T19:53:38.407Z"
---

# Notebook Experiment Lifecycle and Restrictions

A **notebook experiment** is an MLflow experiment that is automatically associated with a specific Databricks notebook. Databricks creates a notebook experiment when you start a run using `mlflow.start_run()` and no active experiment exists. A notebook experiment shares the same name and ID as its corresponding notebook. The notebook ID is the numerical identifier at the end of a notebook URL. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Lifecycle

### Creation

Notebook experiments are created automatically by Databricks when a run is started with `mlflow.start_run()` and there is no active experiment set. Alternately, you can pass a Databricks workspace path to an existing notebook in `mlflow.set_experiment()` to create a notebook experiment for it. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

Users running MLflow on compute with dedicated group access must verify the group has permission to write to the directory where the notebook lives, or use `mlflow.set_tracking_uri("<path>")` to specify a folder for MLflow to write to. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Viewing

In the notebook's right sidebar, click the **Experiment** icon to display the Experiment Runs sidebar. This sidebar shows a summary of each run associated with the notebook experiment, including run parameters and metrics. At the top of the sidebar is the name of the experiment that the notebook most recently logged runs to (either a notebook experiment or a workspace experiment). ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

From the sidebar, you can navigate to the experiment details page or directly to a run. You can also copy the full path of the experiment by clicking the path icon in the notebook's experiment sidebar. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Accessing Experiment ID and Path

On the experiment details page, click the information icon to display a pop-up that shows the path to the experiment, the experiment ID, and the artifact location. You can use the experiment ID in the MLflow command `set_experiment` to set the active MLflow experiment. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Restrictions

### Deletion Behavior

Notebook experiments are **part of the notebook and cannot be deleted separately**. When you delete a notebook, the associated notebook experiment is deleted. Similarly, if you delete a notebook experiment using the UI, the notebook is also deleted. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

If you delete a notebook experiment using the API (for example, `MlflowClient.tracking.delete_experiment()` in Python), the notebook itself is moved into the Trash folder. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

To delete notebook experiments using the API, use the Workspace API to ensure both the notebook and experiment are deleted from the workspace. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Renaming and Permissions

You cannot directly rename, delete, or manage permissions on an MLflow experiment that was created by a notebook in a Databricks Git folder. You must perform these actions at the Git folder level. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

For information on experiment permission levels, see MLflow experiment ACLs. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Comparison with Workspace Experiments

Unlike notebook experiments, Workspace Experiment|workspace experiments are not associated with any notebook, and any notebook can log a run to these experiments by using the experiment ID or the experiment name. Workspace experiments can be created from the Databricks UI or the MLflow API. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — Units of organization for MLflow runs
- Workspace Experiment — Experiments not tied to a specific notebook
- [MLflow Runs](/concepts/mlflow-run.md) — Individual training runs logged to experiments
- MLflow experiment ACLs — Permission levels for experiments
- Databricks Notebooks — The environment that hosts notebook experiments

## Sources

- organize-training-runs-with-mlflow-experiments-databricks-on-aws.md

# Citations

1. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
