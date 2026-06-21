---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bde649a8dbe789835da0afd4f3987ce57f719877190b6a62709b600b181cf29a
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-clone-databricks
    - DC(
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Deep Clone (Databricks)
description: A complete, independent copy of a source Delta, Iceberg, or Parquet table, copying both data and metadata to a target location.
tags:
  - databricks
  - delta-lake
  - cloning
timestamp: "2026-06-19T09:39:13.293Z"
---

# Deep Clone (Databricks)

**Deep Clone** is a cloning operation that creates a complete, independent copy of a source Delta, managed Apache Iceberg, or Apache Parquet table, including both data and metadata. Unlike [Shallow Clone (Databricks)](/concepts/shallow-clone-databricks.md), which only copies the table definition and references the source data files, a deep clone copies the underlying data files themselves, resulting in a fully self-contained table.^[create-table-clone-databricks-on-aws.md]

## Supported Table Formats

Deep cloning is supported for the following table formats:

- **Delta Lake tables** – both managed and external.
- **Apache Parquet tables** – can be cloned to Delta Lake (incremental cloning supported).
- **Foreign Apache Iceberg tables** – can be cloned to Delta Lake.
- **Managed Apache Iceberg tables** – Only deep cloning is supported; shallow cloning is not allowed, and the table format cannot be changed during the clone operation.^[create-table-clone-databricks-on-aws.md]

Deep clone is the default clone type when neither `DEEP CLONE` nor `SHALLOW CLONE` is explicitly specified.^[create-table-clone-databricks-on-aws.md]

## Syntax

```sql
CREATE TABLE [IF NOT EXISTS] table_name
  DEEP CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

Alternatively, `CREATE OR REPLACE TABLE` can be used to either replace an existing table or create a new one:

```sql
[CREATE OR] REPLACE TABLE table_name
  DEEP CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path]
```

^[create-table-clone-databricks-on-aws.md]

### Parameters

| Parameter | Description |
|-----------|-------------|
| `IF NOT EXISTS` | If the target table already exists, the statement is ignored. |
| `CREATE OR REPLACE` | If the table exists it is replaced; if it does not exist it is created. Without `CREATE OR`, the table must already exist for a `REPLACE`. |
| `table_name` | The name of the target table. Must not include temporal or options specifications. If unqualified, the table is created in the current schema. |
| `source_table_name` | The name of the table to clone. May include temporal or options specifications (e.g., `@v2` to clone at a specific version). |
| `TBLPROPERTIES` | Optional user-defined properties to set on the target table. |
| `LOCATION path` | Optionally creates an external table at the given location. `path` must be a STRING literal. |

^[create-table-clone-databricks-on-aws.md]

## Behavior

- A deep clone copies all data files from the source table to a new location, making the target table independent of the source. Subsequent changes to the source (e.g., inserts, deletes, or compaction) do not affect the clone.
- The clone includes the source table's schema, partitioning, table properties, and, for Delta tables, the commit history if the source is Delta.
- For managed Iceberg tables, only deep cloning is supported. The clone must remain in the Delta Lake format (not Iceberg).^[create-table-clone-databricks-on-aws.md]
- [Streaming tables and materialized views](/concepts/delta-streaming-tables-and-materialized-views.md) cannot be used as source or target tables for `CLONE` operations.^[create-table-clone-databricks-on-aws.md]

## Examples

### Deep Clone a [Delta Lake Table](/concepts/delta-lake-table.md)

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

### Deep Clone a Managed Iceberg Table

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

### Deep Clone with Custom Table Properties

```sql
CREATE OR REPLACE TABLE my_clone
DEEP CLONE my_source
TBLPROPERTIES ('purpose' = 'testing');
```

### Deep Clone to an External Location

```sql
CREATE TABLE my_external_clone
DEEP CLONE my_source
LOCATION '/path/to/external/location';
```

^[create-table-clone-databricks-on-aws.md]

## Use Cases

- **Data archiving** – Create point-in-time snapshots of production tables for historical analysis without impacting the source.
- **ML workflows** – Build independent training datasets by cloning a source table at a specific version.
- **Schema evolution testing** – Experiment with schema changes on a clone without risking the original table.
- **Data migration** – Copy data from Parquet or Iceberg into Delta Lake for better performance and governance.

## Related Concepts

- [Shallow Clone (Databricks)](/concepts/shallow-clone-databricks.md) – Copies only metadata; references source data files.
- Clone a table on Databricks – Overview page with detailed guidance and best practices.
- [Delta Lake](/concepts/delta-lake.md) – The storage format that deep cloning primarily targets.
- [Unity Catalog](/concepts/unity-catalog.md) – Supported target for deep clones from Databricks Runtime 13.3 LTS and above.
- [Incremental clone (Parquet/Iceberg to Delta)](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) – A variant that efficiently copies only new data.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
