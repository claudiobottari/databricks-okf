---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9339010eb42d0545be6b349338c9eea70dec1e6d370565cc1306b18d830af3a1
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autologging-security-and-data-management
    - Data Management and Autologging Security
    - ASADM
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Autologging Security and Data Management
description: The security model for autologged data, which is stored in MLflow Tracking and secured by MLflow Experiment permissions, allowing sharing, modification, or deletion via MLflow APIs or UI.
tags:
  - security
  - data-management
  - mlflow
  - access-control
timestamp: "2026-06-18T15:02:31.221Z"
---

## Autologging Security and Data Management

**Autologging Security and Data Management** encompasses the policies, permissions, and controls that govern how model training information captured by [Databricks Autologging](/concepts/databricks-autologging.md) is stored, accessed, and administered within MLflow Tracking.

### Overview

Databricks Autologging automatically records model parameters, metrics, files, and lineage information when training models from supported machine learning frameworks. All captured data is persisted in [MLflow Tracking](/concepts/mlflow-tracking.md) and is governed by the same security model as other MLflow artifacts. ^[databricks-autologging-databricks-on-aws.md]

### Security

All model training information tracked by Databricks Autologging is secured through [MLflow Experiment Permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md). Experiment permissions control which users and groups can read, edit, or manage the runs and artifacts within an experiment. This ensures that sensitive model metadata, such as hyperparameters or performance metrics, is only accessible to authorized personas. ^[databricks-autologging-databricks-on-aws.md]

### Data Management

Users can share, modify, or delete model training information collected by Autologging using the standard [MLflow Tracking API](/concepts/mlflow-tracking.md) or the [MLflow UI](/concepts/mlflow.md). This provides flexibility to curate experiment records after training, for example by removing outdated runs or correcting logged parameters. ^[databricks-autologging-databricks-on-aws.md]

### Administration

Workspace administrators have the ability to disable Databricks Autologging for all interactive notebook sessions across the entire workspace. This setting is configured from the **Advanced** tab of the [admin settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings). Changes to this setting only take effect after the affected cluster is restarted. ^[databricks-autologging-databricks-on-aws.md]

### Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [MLflow Experiment Permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- Admin Settings

### Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
