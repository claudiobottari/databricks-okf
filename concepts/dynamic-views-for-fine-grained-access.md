---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfb5b8381e34c604ae3478f67ee8ee256392834db24e8ce046d84dced7e284d4
  pageDirectory: concepts
  sources:
    - mlflow-system-tables-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-views-for-fine-grained-access
    - DVFFA
    - dynamic view definition
  citations:
    - file: mlflow-system-tables-reference-databricks-on-aws.md
title: Dynamic Views for Fine-Grained Access
description: Dynamic views can be created to restrict MLflow system table access to specific experiment IDs or other custom criteria, providing finer-grained control than granting full table access.
tags:
  - mlflow
  - databricks
  - access-control
  - dynamic-views
timestamp: "2026-06-19T19:40:29.066Z"
---

# Dynamic Views for Fine-Grained Access

**Dynamic Views for Fine-Grained Access** is a pattern that uses [dynamic views](https://docs.databricks.com/aws/en/views/dynamic) in [Unity Catalog](/concepts/unity-catalog.md) to restrict access to specific rows or columns of a table based on custom criteria. This approach is particularly useful when granting access to [MLflow System Tables](/concepts/mlflow-system-tables.md) or other sensitive system schemas, where administrators need to limit visibility to only a subset of the data.

## Overview

By default, only account admins have access to system schemas (e.g., `system.mlflow`). Account admins can grant `USE` and `SELECT` permissions on the schema to additional users, but this gives those users full visibility into all data across the entire account. For example, any user with access to the `system.mlflow` tables can view metadata from *all* MLflow experiments for *all* workspaces in the account. ^[mlflow-system-tables-reference-databricks-on-aws.md]

When finer-grained control is required, administrators can use dynamic views instead of granting direct table access. A dynamic view defined with custom criteria (such as filtering by experiment ID or workspace) can be created on top of the system table. Users are then granted access to the view rather than the underlying table, ensuring they only see the records they are authorized to view. ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Use with MLflow System Tables

The `system.mlflow` schema contains tables such as `experiments_latest`, `runs_latest`, and `run_metrics_history`. To restrict access, an admin can:

1. Create a dynamic view that includes a `WHERE` clause filtering on, for instance, a specific set of experiment IDs.
2. Grant `SELECT` on the dynamic view to the relevant group(s) or user(s).
3. Instruct users to query the dynamic view name rather than the original system table.

The source documentation explicitly gives this example: *“For example, you could create a view that only shows records from a particular set of experiment IDs. After configuring a custom view, give the name of the view to your users so that they can query the dynamic view rather than the system table directly.”* ^[mlflow-system-tables-reference-databricks-on-aws.md]

## Example

An account admin wants a data science team to see only experiment metadata from their own workspace. The admin creates a dynamic view:

```sql
CREATE OR REPLACE VIEW my_catalog.my_schema.filtered_experiments AS
SELECT *
FROM system.mlflow.experiments_latest
WHERE experiment_id IN (SELECT experiment_id FROM my_catalog.my_schema.allowed_experiments);
```

After granting `SELECT` on `my_catalog.my_schema.filtered_experiments` to the team, they can query the view without ever accessing the full `system.mlflow.experiments_latest` table.

## Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md)
- Dynamic Views
- [Unity Catalog](/concepts/unity-catalog.md)
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md)
- System tables
- [Row-level security](/concepts/row-level-security-rls-policies.md)

## Sources

- mlflow-system-tables-reference-databricks-on-aws.md

# Citations

1. [mlflow-system-tables-reference-databricks-on-aws.md](/references/mlflow-system-tables-reference-databricks-on-aws-4d1f3c50.md)
