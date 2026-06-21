---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6c9332eae40528e17deed89e119f5c43b875e6651c7c52940ff8df56b1395d5
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-iceberg-table-clone-limitations
    - MITCL
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Managed Iceberg Table Clone Limitations
description: Managed Iceberg tables support only deep cloning and cannot be shallow cloned or have their table format changed during cloning.
tags:
  - iceberg
  - cloning
  - limitations
timestamp: "2026-06-19T18:02:35.216Z"
---

# Managed Iceberg Table Clone Limitations

When cloning [Managed Iceberg Table|managed Iceberg tables](/concepts/managed-iceberg-table-cloning.md) on Databricks using the [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) command, the following restrictions apply. These limitations affect which clone types are permitted, whether the table format can be changed, and which table types are eligible as source or target.

## Only Deep Clones Are Supported

Managed Iceberg tables support **only deep clones**; shallow clones are **not** supported. If you specify `SHALLOW CLONE` on a managed Iceberg source, the command fails. ^[create-table-clone-databricks-on-aws.md]

- **Deep clone** – Makes a complete, independent copy of the source table’s data and metadata. ^[create-table-clone-databricks-on-aws.md]
- **Shallow clone** – Copies only the table definition and references the source table’s data files without copying the data. This operation is **not allowed** for managed Iceberg tables. ^[create-table-clone-databricks-on-aws.md]

By contrast, Delta Table|Delta, Parquet Table|Parquet, and [Foreign Iceberg Table|foreign Iceberg tables](/concepts/foreign-iceberg-table-sharing.md) support both deep and shallow cloning. ^[create-table-clone-databricks-on-aws.md]

## Table Format Cannot Be Changed During Clone

When cloning a managed Iceberg table, you **cannot change the table format** as part of the clone operation. The clone must remain in Iceberg format; converting the clone to another format (e.g., Delta) is not supported in the same statement. ^[create-table-clone-databricks-on-aws.md]

## Streaming Tables and Materialized Views Are Not Eligible

[Streaming Tables|Streaming tables](/concepts/streaming-tables-in-databricks.md) and [Materialized Views|materialized views](/concepts/materialized-views-in-databricks.md) cannot be used as the source or the target of a `CLONE` operation, regardless of the table format. This limitation applies to all clone operations on Databricks, including those targeting managed Iceberg tables. ^[create-table-clone-databricks-on-aws.md]

## Summary

| Restriction | Applies to Managed Iceberg Tables |
|-------------|-----------------------------------|
| Shallow clone not supported | Yes |
| Only deep clone allowed | Yes |
| Cannot change format during clone | Yes |
| Streaming tables / materialized views as source or target | Not supported at all for CLONE |

For more details on clone syntax and options, see the [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) reference. For step-by-step examples of cloning managed Iceberg tables, refer to **Clone a managed Iceberg table** in the Databricks documentation.

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) – Complete, independent copy of table data.
- [Shallow Clone](/concepts/shallow-clone.md) – Metadata-only copy (not available for managed Iceberg).
- [Managed Iceberg Table](/concepts/managed-iceberg-table-cloning.md) – Iceberg table managed by Unity Catalog.
- Foreign Iceberg Table – Iceberg table not managed by Unity Catalog.
- Streaming Tables – Table type that cannot be used with CLONE.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) – View type that cannot be used with CLONE.
- [Delta Lake Clone](/concepts/delta-clone.md) – General cloning functionality for Delta tables.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
