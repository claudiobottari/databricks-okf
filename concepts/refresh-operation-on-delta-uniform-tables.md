---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c49130465eeeb5558ff5d1bb7a02dd4824649984f8a30c1dbd4c5c340e2392d2
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - refresh-operation-on-delta-uniform-tables
    - ROODUT
  citations:
    - file: delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
title: Refresh operation on Delta Uniform tables
description: A metadata refresh operation for Delta Uniform tables, which may require specific arguments to function correctly
tags:
  - databricks
  - delta-lake
  - uniform
  - maintenance
timestamp: "2026-06-18T15:24:13.552Z"
---

Here is the wiki page for "Refresh operation on Delta Uniform tables".

---

## Refresh operation on Delta Uniform tables

A **Refresh operation on Delta Uniform tables** is a manual process used to update the read-only [Delta Uniform](/concepts/delta-uniform.md) manifest — the metadata that enables non-Databricks query engines (such as Apache Spark, Trino, and Presto) to read Delta tables via the Delta Lake In-Place Reader. This operation is necessary when the underlying Delta table has been modified outside of the Databricks environment, ensuring external query engines see the most recent data. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## When a refresh is needed

A Delta Uniform table uses a Uniform Iceberg connector or a Uniform Delta Lake In-Place Reader to present metadata that other query engines can understand. By default, Databricks automatically refreshes the Uniform manifest when a table is modified through Databricks. However, if the Delta table is updated by an external system — for example, by a process running outside of Databricks — the Uniform manifest becomes stale. In such cases, a manual refresh is required so that external readers can access the latest data. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## How to refresh

The refresh is performed by executing the following SQL command in a Databricks notebook or SQL editor: ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

```sql
REFRESH UNIFORM TABLE <table-identifier>;
```

Replace `<table-identifier>` with the full [Three-Level Namespace](/concepts/three-level-namespace.md) of the target table (e.g., `catalog.schema.table_name`). This command regenerates the Uniform manifest so that external query engines can see the current state of the Delta table. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Error conditions

The refresh operation can fail if it receives invalid arguments. When this occurs, Databricks returns the `DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT` error. This is a subclass of `DELTA_UNIFORM_REFRESH.INVALID_ARGUMENT`. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

For details on troubleshooting this error, see DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT Error Condition|DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT error condition. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Related concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature that makes Delta Lake tables readable by non-Databricks engines.
- Uniform Iceberg connector — The connector used to expose Delta tables as Iceberg tables.
- Delta Lake In-Place Reader — The reader that enables external engines to read Delta tables directly.
- [Managing Delta Lake table history](/concepts/delta-lake-table-history-retention.md) — Understanding table versioning and time travel in Delta Lake.
- [Three-Level Namespace](/concepts/three-level-namespace.md) — The catalog.schema.table naming convention used in Unity Catalog.

## Sources

- delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws-592e817e.md)
