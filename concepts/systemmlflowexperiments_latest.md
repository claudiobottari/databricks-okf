---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb3ca9fad17b8950fc28d1cb35fe6b87b8270870bfcc35aa509355b9670a8bb4
  pageDirectory: concepts
  sources:
    - mlflow-system-tables-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systemmlflowexperiments_latest
    - system.mlflow.experiments_latest
  citations:
    - file: mlflow-system-tables-reference-databricks-on-aws.md
title: system.mlflow.experiments_latest
description: A system table that records experiment names, soft-deletion events, and lifecycle information for MLflow experiments.
tags:
  - mlflow
  - databricks
  - table-schema
  - experiments
timestamp: "2026-06-19T19:40:18.483Z"
---

# system.mlflow.experiments_latest

The `system.mlflow.experiments_latest` table is a system table in the Databricks `mlflow` schema that records experiment names and soft-deletion events. It is part of the MLflow system tables, which capture experiment metadata managed within the MLflow tracking service. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Overview

This table provides a centralized view of MLflow experiment metadata across all workspaces within a region. The data stored in `system.mlflow.experiments_latest` is similar to the information available on the experiments page in the MLflow UI. ^[mlflow-system-tables-reference-databricks-on-aws.md]

Privileged users can use this table to take advantage of Databricks lakehouse tooling on their MLflow data, including building custom AI/BI dashboards, setting up SQL alerts, or performing large-scale analytical queries. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Data Availability

The `mlflow` system tables began recording MLflow data from all regions on September 2, 2025. Data from before that date may not be available. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Related Tables

The `mlflow` schema includes two additional tables that complement `experiments_latest`:

- `system.mlflow.runs_latest`: Records run-lifecycle information, including params, tags, and aggregated metric statistics (min, max, and latest values). ^[mlflow-system-tables-reference-databricks-on-aws.md]
- `system.mlflow.run_metrics_history`: Records the name, value, timestamp, and step of all metrics logged on runs, enabling detailed time series analysis. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Common Use Cases

### Joining with Runs Data

The `experiments_latest` table is frequently joined with `runs_latest` to get combined experiment and run information. For example, you can retrieve run names, experiment names, start dates, statuses, and run durations in a single query. ^[mlflow-system-tables-reference-databricks-on-aws.md]

### Building Dashboards

You can build dashboards on top of MLflow system tables data to analyze experiments and runs from the entire workspace. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Access Control

By default, only account admins have access to system schemas. To grant additional users access to the `experiments_latest` table, an account admin must grant them the `USE` and `SELECT` permissions on the `system.mlflow` schema. ^[mlflow-system-tables-reference-databricks-on-aws.md]

**Important:** Any user who has access to these tables can view metadata across all MLflow experiments for all workspaces in the account. For finer-grained control, you can use dynamic views with custom criteria to grant groups access to only specific experiment IDs. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations
- [MLflow tracking service](/concepts/remote-mlflow-tracking-server.md) — The service that manages experiment and run metadata
- system.mlflow.runs_latest — Related table for run lifecycle information
- system.mlflow.run_metrics_history — Related table for detailed metric history
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that controls access to system tables
- Dynamic views — Used for implementing fine-grained access control on system tables

## Sources

- mlflow-system-tables-reference-databricks-on-aws.md

# Citations

1. [mlflow-system-tables-reference-databricks-on-aws.md](/references/mlflow-system-tables-reference-databricks-on-aws-4d1f3c50.md)
