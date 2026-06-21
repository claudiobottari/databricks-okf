---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae5c0516194b502c4e63ff8d43ee5fbd1a66c661f15ce7846d84a2747cf5848f
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-permissions-for-trace-archival
    - UCPFTA
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Unity Catalog Permissions for Trace Archival
description: The requirement that users must have necessary write permissions to the specified Unity Catalog Delta table when archiving traces; the table is created if it does not exist or appended to if it already exists.
tags:
  - databricks
  - permissions
  - unity-catalog
timestamp: "2026-06-19T22:08:07.521Z"
---

# Unity Catalog Permissions for Trace Archival

**Unity Catalog Permissions for Trace Archival** refers to the access control requirements needed to save [[MLflow Trace|MLflow Traces]] and their associated assessments to a [Unity Catalog](/concepts/unity-catalog.md) Delta table for long-term storage and advanced analysis.

## Overview

When archiving traces to a Delta table, the user or service principal initiating the archival must have the necessary permissions to write to the specified Unity Catalog Delta table. The target table will be created if it does not already exist. If the table already exists, traces are appended to it. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Required Permissions

To successfully archive traces, the principal must have the following [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) on the target [Catalog and Schema](/concepts/catalog-and-schema.md):

- **WRITE** privileges on the target schema, enabling the creation of new tables
- **WRITE** privileges on the target table (if it already exists) to append trace data
- Sufficient privileges on the parent catalog to create tables within the specified schema

If the target table does not exist, Unity Catalog will create it automatically, provided the principal has the required permissions on the schema. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Specifying the Target Table

When enabling trace archival via the MLflow API, you must provide the fully qualified table name including [Catalog and Schema](/concepts/catalog-and-schema.md): ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

The `delta_table_fullname` parameter uses the three-level namespace format (`catalog.schema.table`), following standard Unity Catalog naming conventions. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Implications of Insufficient Permissions

If the principal lacks the required Unity Catalog permissions, the trace archival operation will fail with an error. The system will not attempt to create the target table or append data without the appropriate access rights. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of access control permissions available in Unity Catalog
- [Delta Table](/concepts/delta-lake-table.md) — The storage format used for archived traces
- [[MLflow Trace|MLflow Traces]] — The data being archived to the Delta table
- [Trace Archival](/concepts/trace-archival.md) — The broader feature for saving traces to Delta tables
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — Catalogs, schemas, and tables as permission targets

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
