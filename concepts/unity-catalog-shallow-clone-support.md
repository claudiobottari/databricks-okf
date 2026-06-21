---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f5106950461735809f7010d5eccf1e8ea41ee6aa6e5f817864cf84b9739c007
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-shallow-clone-support
    - UCSCS
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Unity Catalog Shallow Clone Support
description: Shallow clone is supported for Unity Catalog managed tables in Databricks SQL and Databricks Runtime 13.3 LTS and above, but not in 12.2 LTS and below.
tags:
  - unity-catalog
  - cloning
  - compatibility
timestamp: "2026-06-19T18:02:38.936Z"
---

# Unity Catalog Shallow Clone Support

**Unity Catalog Shallow Clone Support** refers to the ability to create shallow clones of tables managed by [Unity Catalog](/concepts/unity-catalog.md) in Databricks. A shallow clone creates a copy of a table's metadata and definition but references the source table's data files rather than copying them, providing a lightweight, storage-efficient way to duplicate table structures. ^[create-table-clone-databricks-on-aws.md]

## Overview

Shallow cloning is supported for Unity Catalog managed tables in Databricks SQL and Databricks Runtime 13.3 LTS and above. In Databricks Runtime 12.2 LTS and below, shallow clones are not supported for Unity Catalog tables. ^[create-table-clone-databricks-on-aws.md]

## Supported Source Table Types

The following table types support shallow cloning to Unity Catalog:

- **Delta tables** — Both managed and external Delta tables can be shallow cloned.
- **Parquet tables** — Parquet tables can be shallow cloned.
- **Foreign Iceberg tables** — Apache Iceberg tables managed outside Unity Catalog can be shallow cloned.

Managed Iceberg tables within Unity Catalog support only deep cloning, not shallow cloning. ^[create-table-clone-databricks-on-aws.md]

## Syntax

Shallow clones are created using the `CREATE TABLE ... SHALLOW CLONE` or `REPLACE TABLE ... SHALLOW CLONE` SQL commands:

```sql
-- Create a new shallow clone
CREATE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;

-- Replace an existing table with a shallow clone
CREATE OR REPLACE TABLE target_catalog.target_schema.target_table
SHALLOW CLONE source_catalog.source_schema.source_table;
```

^[create-table-clone-databricks-on-aws.md]

## Parameters

- **`SHALLOW CLONE`** — Specifies that only the table definition and metadata should be copied, while data files remain referenced from the source table.
- **`source_table_name`** — The name of the source table to clone. May include a temporal specification or options specification.
- **`TBLPROPERTIES`** — Optionally sets one or more user-defined properties on the target table.
- **`LOCATION path`** — Optionally creates an external table at the specified storage path. ^[create-table-clone-databricks-on-aws.md]

## Behavior

A shallow clone creates a new table entry in Unity Catalog with its own metadata, schema, and table properties. However, the underlying data files are shared with the source table. This means:

- Writes to the shallow clone create new data files without affecting the source table (copy-on-write semantics).
- Reads from the shallow clone return the data as it existed at the time of cloning, plus any changes made through the clone.
- The shallow clone does not consume additional storage for the original data.

## Limitations

- Streaming tables and materialized views are not supported as source or target tables for `CLONE` operations. ^[create-table-clone-databricks-on-aws.md]
- Managed Iceberg tables support only deep cloning, not shallow cloning. ^[create-table-clone-databricks-on-aws.md]
- The table format cannot be changed during cloning for managed Iceberg tables. ^[create-table-clone-databricks-on-aws.md]

## Use Cases

Shallow clones are useful for:

- **Development and testing** — Creating lightweight copies of production tables for experimentation without duplicating data.
- **Data snapshots** — Capturing a point-in-time view of a table for reporting or analysis.
- **Incremental data migration** — Using shallow clones as part of workflows to incrementally clone Parquet and Iceberg tables to Delta Lake.

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — Creates a complete, independent copy of the source table including all data files.
- Clone a Table on Databricks — General guidance on cloning operations and differences between shallow and deep clones.
- [Incrementally Clone Parquet and Apache Iceberg Tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Workflow for migrating data using clone operations.
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) — Tables fully managed by Unity Catalog with centralized governance.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for most Databricks tables.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
