---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 961fa2017cdcce3ca3213023cf27eba02f7981aa0508b2f6a3d3c44a019c1ac2
  pageDirectory: concepts
  sources:
    - mlflow-system-tables-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-recency-constraint-for-mlflow-system-tables
    - DRCFMST
    - Data Recency Constraint
  citations:
    - file: mlflow-system-tables-reference-databricks-on-aws.md
title: Data Recency Constraint for MLflow System Tables
description: The MLflow system tables began recording data from all regions on September 2, 2025; data before that date may not be available.
tags:
  - mlflow
  - databricks
  - data-recency
  - limitations
timestamp: "2026-06-19T19:40:40.959Z"
---

# Data Recency Constraint for MLflow System Tables

The **Data Recency Constraint for MLflow System Tables** is a temporal limitation on the historical data available through the `system.mlflow` schema. These system tables began recording MLflow data from all regions on September 2, 2025, meaning that data from before that date may not be available in the tables. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Overview

The `mlflow` system tables capture experiment metadata managed within the MLflow tracking service, allowing privileged users to leverage Databricks lakehouse tooling on their MLflow data across all workspaces within a region. Users can build custom dashboards, set up SQL alerts, or perform large-scale analytical queries using these tables. ^[mlflow-system-tables-reference-databricks-on-aws.md]

Due to the September 2, 2025 start date for data recording, any queries that attempt to analyze MLflow activity before this cutoff will return incomplete results. This is particularly important when analyzing long-running experiments or comparing historical trends that predate the system table availability. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Impact on Queries

When querying `system.mlflow.experiments_latest`, `system.mlflow.runs_latest`, or `system.mlflow.run_metrics_history`, users should be aware that data from before September 2, 2025 is not guaranteed to be present. This recency constraint affects the following use cases:

- **Trend analysis**: Long-term trend calculations may have a gap in historical data.
- **Reliability metrics**: Experiment success ratios computed over extended periods may be based on a shorter timeframe than expected.
- **Usage statistics**: Queries measuring average GPU utilization or other aggregate metrics across experiments will only reflect data from the recording start date onward.

The system tables provide an ER diagram and detailed schemas for each table, which can help users understand the available fields and plan their queries accordingly. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md) — The schema that contains experiment metadata for analytical queries.
- [MLflow Tracking Service](/concepts/remote-mlflow-tracking-server.md) — The service that manages experiment and run metadata.
- [Data Recency Constraint](/concepts/data-recency-constraint-for-mlflow-system-tables.md) — General concept of temporal data availability limitations in system tables.
- Unity Catalog System Tables — Broader ecosystem of system tables on Databricks.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) — Alerting mechanism that can be configured on system table queries.

## Sources

- mlflow-system-tables-reference-databricks-on-aws.md

# Citations

1. [mlflow-system-tables-reference-databricks-on-aws.md](/references/mlflow-system-tables-reference-databricks-on-aws-4d1f3c50.md)
