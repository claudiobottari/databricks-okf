---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c5ec91fdae2ed1afdfe049b0653d1981de8bd01524f81f4908c746ccae82335
  pageDirectory: concepts
  sources:
    - mlflow-system-tables-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-control-for-mlflow-system-tables
    - ACFMST
  citations:
    - file: mlflow-system-tables-reference-databricks-on-aws.md
title: Access Control for MLflow System Tables
description: By default only account admins can access system tables; they can grant USE and SELECT permissions to other users, who then see metadata across all experiments in the account.
tags:
  - mlflow
  - databricks
  - access-control
  - security
timestamp: "2026-06-19T19:40:49.436Z"
---

# Access Control for MLflow System Tables

**Access Control for MLflow System Tables** governs which users can view and query the `system.mlflow` schema within Databricks. These tables contain experiment and run metadata from the [MLflow Tracking Service](/concepts/remote-mlflow-tracking-server.md) across all workspaces in a region, making access management a critical security consideration. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Default Access

By default, only **account admins** have access to system schemas, including the `system.mlflow` schema. No other users or service principals can query these tables unless explicitly granted permissions. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Granting Access to Users

To give additional users access to the MLflow system tables, an account admin must grant the `USE` and `SELECT` permissions on the `system.mlflow` schema. This follows standard [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) conventions. ^[mlflow-system-tables-reference-databricks-on-aws.md]

**Important security implication**: Any user who has access to these tables can view metadata across **all** MLflow experiments for **all** workspaces within the account. This includes experiment names, run configurations, metrics, parameters, and tags. ^[mlflow-system-tables-reference-databricks-on-aws.md]

### Granting Access to Groups

Rather than granting access to individual users, Databricks recommends configuring access for groups following Unity Catalog Best Practices. This simplifies permission management and ensures consistent access across team members. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Fine-Grained Access Control with Dynamic Views

If the default table-level access is too broad for your requirements, you can implement finer-grained control using Dynamic Views. Dynamic views allow you to create custom views over the system tables with specific filtering criteria. ^[mlflow-system-tables-reference-databricks-on-aws.md]

For example, you could create a dynamic view that only exposes records from a particular set of experiment IDs or a specific workspace. After configuring such a view, provide the view name to your users instead of the system table directly. This way, users can query the dynamic view while the underlying system table remains restricted. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Use Cases

Access to MLflow system tables enables privileged users to:

- Build custom AI/BI Dashboards with MLflow metadata
- Set up [SQL Alerts](/concepts/databricks-sql-alerts.md) for experiment reliability monitoring
- Perform large-scale analytical queries across experiments
- Answer questions like which experiments have the lowest reliability or what the average GPU utilization is across different experiments

^[mlflow-system-tables-reference-databricks-on-aws.md]

## Related Concepts

- Unity Catalog Privileges Reference — Documentation on `USE` and `SELECT` permissions
- Unity Catalog Best Practices — Guidance on group-based access management
- Dynamic Views — Mechanism for row- and column-level security in Unity Catalog
- [MLflow Tracking Service](/concepts/remote-mlflow-tracking-server.md) — The service that generates the metadata stored in system tables
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for MLflow runs
- [MLflow Runs](/concepts/mlflow-run.md) — Individual training or evaluation executions

## Sources

- mlflow-system-tables-reference-databricks-on-aws.md

# Citations

1. [mlflow-system-tables-reference-databricks-on-aws.md](/references/mlflow-system-tables-reference-databricks-on-aws-4d1f3c50.md)
