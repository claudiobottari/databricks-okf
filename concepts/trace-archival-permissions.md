---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1829ad46ebb6ffdfda9a58f043f831d0e2101e57fb5c97f7af4078444b33a13
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-archival-permissions
    - TAP
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Trace Archival Permissions
description: The requirement for users to have the necessary write permissions on the target Unity Catalog Delta table to enable trace archiving.
tags:
  - permissions
  - security
  - unity-catalog
timestamp: "2026-06-18T14:27:16.746Z"
---

# Trace Archival Permissions

**Trace Archival Permissions** refers to the Unity Catalog access controls required to save [Traces](/concepts/traces.md) and their associated assessments to a Delta table for long-term storage and advanced analysis. Without the appropriate permissions, attempts to archive traces will fail.

## Required Permissions

To archive traces to a Unity Catalog Delta table, you must have the necessary permissions to write to the specified table. The target table will be created if it does not already exist. If the table already exists, new traces are appended to it.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

The exact set of required Unity Catalog privileges depends on whether the Delta table already exists:

- **Creating a new table:** You need `CREATE` privileges on the target schema, plus `USE SCHEMA` and `USE CATALOG` permissions on the parent [Catalog and Schema](/concepts/catalog-and-schema.md).
- **Appending to an existing table:** You need `MODIFY` (or equivalent write) privileges on the target table, plus `USE SCHEMA` and `USE CATALOG` on the parent [Catalog and Schema](/concepts/catalog-and-schema.md).

## Enabling Trace Archival

The `enable_databricks_trace_archival` function requires you to specify the full name of the target Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md). The function will attempt to write to the table using the permissions of the caller's identity.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance system that manages permissions for Delta tables
- [Delta Tables](/concepts/delta-lake-table.md) — The storage format used for archived traces
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that generates traces eligible for archival
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Workflows that benefit from archived trace data

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
