---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 905b56fc8cf8d606c59d6278dc0972ac2b838ea64200835f38657dc781a4bb0c
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-iceberg-table-clone-restrictions
    - MITCR
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Managed Iceberg Table Clone Restrictions
description: Managed Iceberg tables support only deep cloning (not shallow), and the table format cannot be changed during cloning.
tags:
  - databricks
  - iceberg
  - cloning
timestamp: "2026-06-18T11:25:08.970Z"
---

# Managed Iceberg Table Clone Restrictions

**Managed Iceberg Table Clone Restrictions** describes the limitations and constraints that apply when using `CREATE TABLE CLONE` to clone managed [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables in Databricks. Unlike [Delta Lake](/concepts/delta-lake.md) or Apache Parquet tables, managed Iceberg tables support only a subset of clone operations, with specific restrictions on clone depth and table format changes.

## Supported Clone Types

Managed Iceberg tables support only **deep cloning** — not shallow cloning. A deep clone creates a complete, independent copy of the source table, including all data and metadata. A shallow clone is not supported for managed Iceberg tables. ^[create-table-clone-databricks-on-aws.md]

For comparison:
- [Delta Lake](/concepts/delta-lake.md) tables support both deep and shallow cloning.
- Apache Parquet tables support both deep and shallow cloning.
- Managed **Iceberg** tables support only deep cloning.

## Format Change Restriction

You **cannot change the table format** during cloning. The cloned target table must remain a managed Iceberg table. This means you cannot clone a managed Iceberg table and convert the output to a [Delta Lake](/concepts/delta-lake.md) or Parquet format in the same operation. ^[create-table-clone-databricks-on-aws.md]

## Syntax Requirements

When cloning a managed Iceberg table, you must use the `DEEP CLONE` clause explicitly. The `SHALLOW CLONE` clause is not supported for managed Iceberg source tables and will result in an error. ^[create-table-clone-databricks-on-aws.md]

```sql
CREATE TABLE target_catalog.target_schema.target_table
DEEP CLONE source_catalog.source_schema.source_table;
```

## Restrictions Summary

| Restriction | Details |
|-------------|---------|
| **Clone depth** | Only deep cloning is supported. Shallow cloning is not available. |
| **Format change** | The table format cannot be changed during cloning. The target must remain a managed Iceberg table. |
| **Source table type** | The source must be a managed Iceberg table. Foreign Iceberg tables may have different restrictions. |

## Related Concepts

- Deep Clone vs Shallow Clone — Differences between clone types in Databricks
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) — The general `CLONE` command syntax
- [Clone a Managed Iceberg Table](/concepts/managed-iceberg-table-cloning.md) — Practical guide for cloning Iceberg tables
- [Delta Lake Table Cloning](/concepts/delta-table-cloning.md) — Clone capabilities for Delta Lake tables
- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Alternative approach for converting Iceberg to Delta

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
