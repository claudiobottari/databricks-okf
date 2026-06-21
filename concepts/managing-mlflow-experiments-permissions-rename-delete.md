---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe4dcce28f1fa5750c93a29a9aae70c7479935a684608174a8062018d1d84c73
  pageDirectory: concepts
  sources:
    - organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managing-mlflow-experiments-permissions-rename-delete
    - MMEPRD
  citations:
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
title: "Managing MLflow Experiments: Permissions, Rename, Delete"
description: Experiment owners can rename, delete, or change permissions from either the Experiments page or the experiment details page. Notebook experiments are tied to notebooks — deleting one deletes both. Git-folder notebook experiments must be managed at the Git folder level.
tags:
  - mlflow
  - permissions
  - experiment-management
timestamp: "2026-06-19T19:53:23.252Z"
---

# Managing MLflow Experiments: Permissions, Rename, Delete

**Managing MLflow Experiments: Permissions, Rename, Delete** covers the administrative operations you can perform on [MLflow experiments](/concepts/mlflow-experiment.md) that you own. These actions include changing access permissions, renaming an experiment, and deleting an experiment. You can perform these tasks from the **Experiments** page, the experiment details page, or the workspace menu. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Limitations

You cannot directly rename, delete, or manage permissions on an MLflow experiment that was created by a notebook in a Databricks Git folder. These actions must be performed at the Git folder level instead. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Permissions

To change permissions for an experiment you own, use the [experiment details page](#experiment-page). From that page, click the **Permissions** button. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

Alternatively, from the **Experiments** page, click the kebab menu (⋮) in the rightmost column of the experiment row and then select **Permissions**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

For detailed information on experiment permission levels, see MLflow experiment ACLs. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Rename Experiment

You can rename an experiment that you own from either the **Experiments** page or the experiment details page. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### From the Experiments Page

On the **Experiments** page, click the kebab menu (⋮) in the rightmost column of the experiment row and then click **Rename**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### From the Experiment Details Page

On the experiment details page, click the kebab menu (⋮) next to **Permissions** and then click **Rename**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### From the Workspace

You can also rename a workspace experiment from the workspace. Right-click the experiment name and then click **Rename**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Delete Experiment

You can delete an experiment that you own from the **Experiments** page or from the experiment details page. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

> **Important:** When you delete a notebook experiment, the associated notebook is also deleted. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### From the Experiments Page

On the **Experiments** page, click the kebab menu (⋮) in the rightmost column of the experiment row and then click **Delete**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### From the Experiment Details Page

On the experiment details page, click the kebab menu (⋮) next to **Permissions** and then click **Delete**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Delete a Workspace Experiment from the Workspace

You can delete a workspace experiment from the workspace. Right-click the experiment name and then click **Move to Trash**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Delete Notebook Experiments with the API

To delete notebook experiments using the API, use the Workspace API to ensure both the notebook and experiment are deleted from the workspace. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- MLflow experiment ACLs
- Workspace API
- Organize training runs with MLflow experiments

## Sources

- organize-training-runs-with-mlflow-experiments-databricks-on-aws.md

# Citations

1. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
