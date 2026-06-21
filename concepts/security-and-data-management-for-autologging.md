---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0abb1f53caa51ad74860563d5191aa4cb17fe9156f2232352a3ffbe4eedc6946
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - security-and-data-management-for-autologging
    - Data Management for Autologging and Security
    - SADMFA
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Security and Data Management for Autologging
description: How model training information captured by Autologging is stored in MLflow Tracking and secured using MLflow Experiment permissions.
tags:
  - security
  - data-management
  - mlflow
  - access-control
timestamp: "2026-06-19T18:08:31.970Z"
---

# Security and Data Management for Autologging

**Security and Data Management for Autologging** describes how model training information captured by [Databricks Autologging](/concepts/databricks-autologging.md) is stored, secured, and managed. All data automatically recorded during model training sessions is persisted through [MLflow Tracking](/concepts/mlflow-tracking.md) and protected by [MLflow Experiment permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md). ^[databricks-autologging-databricks-on-aws.md]

## Data Storage

Every piece of model training information — including parameters, metrics, files, and model lineage — that Databricks Autologging captures is stored inside [MLflow Tracking](/concepts/mlflow-tracking.md). This storage layer provides a centralized repository for all experiment metadata. ^[databricks-autologging-databricks-on-aws.md]

## Access Control

The security model for autologged data relies entirely on **MLflow Experiment permissions**. These permissions govern who can view, modify, or delete the tracking information that Databricks Autologging records. Users can control access to their experiments through the [MLflow Tracking API](/concepts/mlflow-tracking.md) or the [MLflow UI](/concepts/mlflow.md). ^[databricks-autologging-databricks-on-aws.md]

## Data Management Operations

Users have full control over their autologged data after it is captured. They can perform the following operations using either the [MLflow Tracking API](/concepts/mlflow-tracking.md) or the [MLflow UI](/concepts/mlflow.md):

- **Share** tracking data with other workspace users by adjusting experiment permissions.
- **Modify** existing run metadata, such as adding new parameters or metrics.
- **Delete** runs or experiments that are no longer needed.

These management capabilities mirror the standard data governance tools available for any [MLflow Experiment](/concepts/mlflow-experiment.md). ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md) – The access control mechanism that secures autologged data.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The storage backend where autologging data is persisted.
- [Databricks Autologging](/concepts/databricks-autologging.md) – The feature that automatically captures model training information.
- Model lineage – The relationship tracking between models, runs, and experiments.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – A downstream service for model versioning and deployment.

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
