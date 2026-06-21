---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02e759f8d354a897960392acb4f01a43ddc9272efad1faf0b1874f9a47657b49
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autologging-administration-in-databricks
    - AAID
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Autologging Administration in Databricks
description: Workspace-level control for administrators to enable or disable Databricks Autologging across all clusters from the admin settings page.
tags:
  - databricks
  - administration
  - cluster-management
timestamp: "2026-06-19T18:08:16.457Z"
---

## Autologging Administration in Databricks

**Autologging Administration in Databricks** refers to the workspace-level controls that administrators can use to enable or disable [Databricks Autologging](/concepts/databricks-autologging.md) for all interactive notebook sessions across the workspace. These settings allow administrators to manage the automatic capture of model parameters, metrics, files, and lineage information that is recorded as [MLflow Tracking](/concepts/mlflow-tracking.md) runs.

### Overview

By default, Databricks Autologging is enabled for interactive Python notebooks attached to clusters running Databricks Runtime 10.4 LTS ML or above (and select preview regions from 9.1 LTS ML). When a user attaches a notebook to a cluster, the system automatically calls `mlflow.autolog()` with a default configuration to set up tracking for supported ML frameworks.^[databricks-autologging-databricks-on-aws.md]

Administrators can override this default behavior at the workspace level, controlling whether autologging is available globally for all notebook sessions.

### Enabling and Disabling Autologging Workspace-Wide

To enable or disable Databricks Autologging for an entire workspace, administrators use the **Advanced** tab of the [admin settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings). This toggle applies to all clusters in the workspace.^[databricks-autologging-databricks-on-aws.md]

Disabling autologging at the workspace level prevents the automatic `mlflow.autolog()` call from being invoked when notebooks attach to clusters. Users can still explicitly call `mlflow.autolog()` in their notebooks to opt in on a per-notebook basis, unless autologging is also disabled via a workspace policy.^[databricks-autologging-databricks-on-aws.md]

### Effect of Cluster Restart

Changes to the workspace-level autologging setting **do not take effect until the affected clusters are restarted**. This is because the autologging configuration is loaded at cluster startup. Administrators should plan maintenance windows or communicate with users about expected restarts after toggling the setting.^[databricks-autologging-databricks-on-aws.md]

### Relationship to Per-Notebook Autologging

Even when autologging is enabled globally, users can disable it for a specific notebook by calling `mlflow.autolog(disable=True)` within that notebook. Conversely, if autologging is disabled workspace-wide, users can re-enable it for a notebook session by calling `mlflow.autolog()` with their desired parameters.^[databricks-autologging-databricks-on-aws.md]

Administrators should note that per-notebook calls to `mlflow.autolog()` take precedence over the workspace setting for the duration of the notebook session.

### Serverless Compute Considerations

Autologging is **not automatically enabled** on serverless compute clusters. Administrators who want users to benefit from autologging on serverless compute must instruct users to explicitly call `mlflow.autolog()` in their notebooks. There is no workspace-level toggle that forces autologging on serverless compute.^[databricks-autologging-databricks-on-aws.md]

### Limitations for Administrators

- **Driver‑node only**: Autologging is enabled only on the driver node. To use autologging from worker nodes, users must explicitly call `mlflow.autolog()` from code running on each worker. Administrators cannot change this with workspace settings.^[databricks-autologging-databricks-on-aws.md]
- **XGBoost scikit-learn integration**: The XGBoost scikit‑learn integration is not supported by Databricks Autologging.^[databricks-autologging-databricks-on-aws.md]
- **Existing automated integrations**: Disabling Databricks Autologging does not affect existing automated MLflow tracking integrations for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) or Hyperopt. Those integrations continue to behave as before.^[databricks-autologging-databricks-on-aws.md]

### Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) – Core feature for automatic MLflow tracking.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Underlying system where autologged data is stored.
- Admin Settings – Workspace configuration page with the autologging toggle.
- Cluster Restart – Required for autologging setting changes to apply.
- Serverless Compute – Compute type where autologging is not auto‑enabled.
- [MLflow Experiment Permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md) – Security model for autologged data.

### Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
