---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c33ddd751025f2959a6bd3a467bf1a15dc51dc03b861f15206d143a11795676
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-source-table-compatibility
    - CSTC
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: Clone Source Table Compatibility
description: Delta, Parquet, and foreign Iceberg tables support both deep and shallow cloning; managed Iceberg tables support only deep cloning.
tags:
  - databricks
  - iceberg
  - parquet
  - cloning
timestamp: "2026-06-19T14:38:52.593Z"
---

# Clone Source Table Compatibility

**Clone Source Table Compatibility** refers to which table formats are supported as source tables for the `CREATE TABLE [SHALLOW | DEEP] CLONE` command in Databricks. The clone operation copies a source Delta, managed Apache Iceberg, or Apache Parquet table to a target location at a specific version. The type of clone (deep or shallow) available depends on the source table format.^[create-table-clone-databricks-on-aws.md]

## Supported Source Table Formats

| Source Table Format | Deep Clone | Shallow Clone | Notes |
|---------------------|------------|---------------|-------|
| Delta               | Supported  | Supported     |       |
| Parquet             | Supported  | Supported     |       |
| Foreign Iceberg     | Supported  | Supported     |       |
| Managed Iceberg     | Supported  | Not supported | Cannot change table format during cloning |

^[create-table-clone-databricks-on-aws.md]

- **Delta, Parquet, and Foreign Iceberg** tables support both deep and shallow cloning.^[create-table-clone-databricks-on-aws.md]
- **Managed Iceberg** tables support only deep cloning; shallow cloning is not available. Additionally, you cannot change the table format when cloning a managed Iceberg source.^[create-table-clone-databricks-on-aws.md]

## Unsupported Source Types

Streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md) are not supported as source tables for the `CLONE` command.^[create-table-clone-databricks-on-aws.md]

## Additional Details

In Databricks SQL and Databricks Runtime 13.3 LTS and above, shallow clone is also supported when the **target** is a Unity Catalog managed table. This capability is independent of the source table format but is subject to the source format's compatibility with shallow clones as listed above.^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- Deep clone vs shallow clone — Trade-offs between full data copy and metadata-only copy.
- Clone a table on Databricks — General guidance on using clone operations.
- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Migration workflow for non-Delta sources.
- Unity Catalog table cloning — Shallow clone support for Unity Catalog managed tables.
- STREAMING LIMITATIONS — Restrictions on streaming tables with CLONE.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
