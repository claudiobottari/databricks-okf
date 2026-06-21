---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b52e5d1bb6bc26cd18f7dcc8f5675fdbcce83689c1cea726d7ad4d461d52440
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-delta-table
    - UCDT
    - Unity Catalog Delta tables
    - Unity Catalog Tables
    - Unity Catalog table
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Unity Catalog Delta Table
description: The target storage format and catalog system used for archiving traces, requiring the full three-level name (catalog.schema.table) for write access.
tags:
  - databricks
  - storage
  - unity-catalog
timestamp: "2026-06-19T17:35:16.363Z"
---

# Unity Catalog Delta Table

**Unity Catalog Delta Table** refers to a Delta table managed within the Unity Catalog [Metastore](/concepts/metastore.md) on the Databricks platform. These tables combine Delta Lake's ACID transaction capabilities with Unity Catalog's centralized governance and discovery features.

## Overview

A Unity Catalog Delta Table is a [Delta Lake](/concepts/delta-lake.md) table that has been registered in and is governed by [Unity Catalog](/concepts/unity-catalog.md). The table's metadata, schema, and lineage are tracked centrally, enabling fine-grained access control, data discovery, and audit logging across workspaces. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Naming Convention

Unity Catalog Delta Tables are referenced using a three-level namespace: **catalog.schema.table_name**. This fully qualified name uniquely identifies the table within the Unity Catalog [Metastore](/concepts/metastore.md). When working with these tables, you must specify the full name including the [Catalog and Schema](/concepts/catalog-and-schema.md). ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Key Features

- **Centralized Governance**: Access controls and permissions are managed at the catalog level through Unity Catalog, rather than at the workspace level.
- **Cross-Workspace Access**: Tables registered in Unity Catalog can be accessed from any workspace that has been granted access to the catalog.
- **Data Lineage**: Unity Catalog automatically tracks the lineage of tables, showing how data flows through pipelines and queries.
- **ACID Transactions**: As Delta tables, they support atomic, consistent, isolated, and durable transactions for reliable data operations.

## Common Use Cases

### Trace Archiving

Unity Catalog Delta Tables are commonly used for archiving traces from [MLflow](/concepts/mlflow.md) experiments. The `enable_databricks_trace_archival` function allows you to save traces and associated assessments to a Unity Catalog Delta Table for long-term storage and analysis: ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

When the target table does not already exist, it is created automatically. If the table already exists, new traces are appended to it. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Advanced Analytics

Archived trace data in Unity Catalog Delta Tables can be queried for building custom dashboards, performing in-depth analytics on trace data, and maintaining a durable record of application behavior. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Permissions

You must have the necessary permissions to write to a Unity Catalog Delta Table. Unity Catalog's role-based access control (RBAC) governs who can create, read, write, or modify tables. When using archival functions, the user or service principal must have write access to the specified table. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that provides ACID transactions for tables.
- [Unity Catalog](/concepts/unity-catalog.md) — The centralized governance solution for data and AI assets.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that generates data stored in archived tables.
- Catalog Schema Table Naming Convention — The three-level namespace used for Unity Catalog objects.
- [Data Lineage](/concepts/data-lineage.md) — Tracking data origin and transformations across pipelines.
- Role-Based Access Control (RBAC) — The permission model for Unity Catalog objects.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
