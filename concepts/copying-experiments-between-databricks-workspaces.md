---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9fcd0d08ddf3d9199e70d964f20747aeaf7964648555627700eaf14f36119089
  pageDirectory: concepts
  sources:
    - organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copying-experiments-between-databricks-workspaces
    - CEBDW
  citations:
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
title: Copying Experiments Between Databricks Workspaces
description: MLflow experiments can be migrated between workspaces using the community-driven MLflow Export-Import open source tool, enabling cross-workspace collaboration, cloning experiments, and backup of experiments and models.
tags:
  - mlflow
  - experiments
  - migration
  - export-import
timestamp: "2026-06-19T19:53:29.956Z"
---

# Copying Experiments Between Databricks Workspaces

To migrate [MLflow experiments](/concepts/mlflow-experiment.md) between Databricks workspaces, you can use the community-driven open source project **MLflow Export-Import**. This tool provides a practical method for transferring experiments and their associated runs from one tracking server to another. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Use Cases

The export‑import approach supports several common migration scenarios:

* **Share and collaborate** – Clone an experiment from another user’s workspace into your own workspace, enabling cross‑workspace collaboration.
* **Copy from a local tracking server** – Move experiments and runs from your local MLflow tracking server to a Databricks workspace.
* **Back up experiments and models** – Create backups of mission‑critical experiments and models in a separate Databricks workspace for disaster recovery. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Availability

The MLflow Export‑Import project is maintained by the community and is not an official Databricks product. You can find the source code and usage instructions on its GitHub repository at [github.com/mlflow/mlflow-export-import](https://github.com/mlflow/mlflow-export-import). ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) – Units of organization for MLflow runs.
- Workspace – A Databricks deployment environment.
- [Tracking server](/concepts/remote-mlflow-tracking-server.md) – The server that stores [MLflow Run](/concepts/mlflow-run.md) data.
- MLflow Export-Import – The community tool used for migration.

## Sources

- organize-training-runs-with-mlflow-experiments-databricks-on-aws.md

# Citations

1. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
