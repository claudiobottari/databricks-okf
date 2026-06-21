---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93078cea3890bfd7a3b59fd0f2e963a893d047b01f63357c1ed9f6a72e07ebc2
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-mlflow-tracking-server
    - DMTS
    - Databricks-hosted tracking server
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Databricks-hosted MLflow tracking server
description: Default managed MLflow tracking server provided by Databricks that stores experiment data in the workspace with no additional setup required.
tags:
  - mlflow
  - databricks
  - tracking-server
timestamp: "2026-06-19T17:42:42.117Z"
---

Here is the wiki page for "Databricks-hosted MLflow tracking server".

---

---
title: Databricks-hosted MLflow Tracking Server
summary: The default managed MLflow tracking server provided by Databricks that stores experiment data in the workspace with no additional setup required.
sources:
  - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:55:57.680Z"
updatedAt: "2026-06-18T10:55:57.680Z"
tags:
  - mlflow
  - databricks
  - tracking-server
aliases:
  - databricks-hosted-mlflow-tracking-server
  - DMTS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks-hosted MLflow Tracking Server

**Databricks-hosted MLflow Tracking Server** is the default, managed MLflow tracking server that Databricks automatically provisions for each workspace. It stores and manages experiment data, runs, and models with no additional setup or configuration required, integrating seamlessly with Databricks notebooks and clusters. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Overview

The Databricks-hosted tracking server eliminates the need for users to deploy, configure, or maintain their own MLflow tracking infrastructure. Experiment data is stored directly in the workspace, and the server is available out-of-the-box for all users and clusters within that workspace. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Setting the Active Experiment

By default, all MLflow runs are logged to the workspace's tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the [notebook experiment](/concepts/notebook-experiment-in-databricks.md). ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

You can control where runs are logged by setting the active experiment programmatically. The following methods are available:

- `mlflow.set_experiment()`
- `mlflow.start_run()`
- Environment variables

For example, setting an experiment for all subsequent runs in the execution: ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import mlflow
mlflow.set_experiment("/Shared/my-experiment")
```

## Remote Tracking Configuration

While the default is the workspace-hosted server, you can also configure MLflow to log to a different tracking server. Common scenarios include developing locally while tracking against a Databricks-hosted server, or logging to a tracking server in a different workspace. This requires setting both the tracking URI and the experiment path: ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

```python
import mlflow
mlflow.set_tracking_uri("databricks://remote-workspace-url")
mlflow.set_experiment("/Shared/centralized-experiments/my-project")
```

Remote tracking server connections require proper authentication, either via [Personal Access Tokens (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) or OAuth using service principals. PATs offer simple setup suitable for development, while OAuth with service principals is recommended for production scenarios. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Key Benefits

- **Zero configuration**: No need to set up or maintain a separate tracking server. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]
- **Seamless integration**: Works automatically with Databricks notebooks, clusters, and jobs. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]
- **Workspace-scoped storage**: Experiment data stays within your workspace's boundaries. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]
- **Managed infrastructure**: Databricks handles availability, backups, and scaling. ^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) — General concept of a server that stores experiment data
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Collections of related runs within a tracking server
- [Notebook Experiment](/concepts/notebook-experiment-in-databricks.md) — Auto-created experiment linked to each notebook
- [Remote MLflow tracking server](/concepts/remote-mlflow-tracking-server.md) — Alternative configurations for cross-workspace tracking

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
