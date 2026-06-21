---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 615e4c5658e686889151822f559737c5b2c21713d5b262019353b2dbff50fc46
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-tables-limitations
    - OTL
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Tables Limitations
description: Boundaries including 2TB metastore-wide limit, 1000 column max, 64KB string limit, 2MB row max, 750 MB/s read throughput, and restrictions on certain source table types.
tags:
  - databricks
  - limits
  - configuration
timestamp: "2026-06-18T11:40:28.455Z"
---

# Online Tables Limitations

**Online Tables** are read-only, row-oriented copies of Delta Tables optimized for low-latency access in [Model Serving](/concepts/model-serving.md), Feature Serving, and [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. While they provide serverless, auto-scaling throughput, several limitations apply to their creation, configuration, and usage. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Table-Level Limitations

- **One online table per source table.** Only a single online table can be created from any given source Delta table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Maximum of 1000 columns.** Both the online table and its source table are limited to 1000 columns. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Primary key restrictions.** Columns of data types `ARRAY`, `MAP`, or `STRUCT` cannot be used as primary keys. Additionally, any row in the source table where a primary key column contains a `NULL` value is ignored in the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **String column size limit.** Columns of `String` type are limited to 64KB in length. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Column name length limit.** Column names are limited to 64 characters. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Maximum row size.** The maximum size of a single row is 2MB. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Naming restrictions.** Catalog, schema, and table names for the online table can only contain alphanumeric characters and underscores, and must not start with numbers. Dashes (`-`) are not allowed. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Source Table Restrictions

- **Unsupported source table types.** Foreign tables, system tables, and internal tables are not supported as source tables for online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Change data feed requirement for incremental sync.** Source tables without [Delta Change Data Feed](/concepts/delta-change-data-feed-cdf.md) enabled support only the **Snapshot** sync mode. **Triggered** and **Continuous** sync modes require change data feed to be enabled on the source table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **OpenSharing tables.** Tables using OpenSharing are only supported in the **Snapshot** sync mode. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Metastore-Wide Limitations

- **2TB storage limit during Public Preview.** The combined size of all online tables in a Unity Catalog [Metastore](/concepts/metastore.md) is limited to 2TB of uncompressed user data. Note that the uncompressed, row-expanded size can be significantly larger (up to 100x) than the compressed columnar size shown in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Maximum read throughput.** The maximum read throughput for a [Metastore](/concepts/metastore.md) is approximately 750 MB/sec. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Regional Availability (Public Preview)

Online tables are in Public Preview only in the following AWS regions: `us-east-1`, `us-west-2`, `eu-west-1`, `ap-southeast-1`, `ap-southeast-2`. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Lakehouse Federation Limitations

When using online tables with [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md), only read operations (`SELECT`) are supported, and a Serverless SQL warehouse is required. This capability is intended for interactive or debugging purposes only and should not be used for production or mission-critical workloads. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Permission and Ownership Limitations

- The Unity Catalog [Metastore](/concepts/metastore.md) must have Privilege Model Version 1.0. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- To manage the data synchronization pipeline, you must either be the owner of the online table or be granted the `REFRESH` privilege on it. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- Users without `USE CATALOG` and `USE SCHEMA` privileges on the catalog will not see the online table in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Common Failure Scenarios

### Source Table Deletion or Recreation

If the source table is deleted, or deleted and recreated with the same name, while the online table is synchronizing, the online table update may fail or show an offline status. This is particularly common with continuous online tables because they are constantly synchronizing. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Firewall Restrictions

If the source table cannot be accessed through Serverless Compute due to firewall settings, the error details may show the message "Failed to start the Lakeflow Spark Declarative Pipelines service on cluster xxx…". ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Storage Limit Exceeded

When the aggregate size of online tables exceeds the 2 TB metastore-wide limit, updates may fail. To estimate the uncompressed, row-expanded size of a Delta table, use the following query from a Serverless SQL Warehouse: ^[databricks-online-tables-legacy-databricks-on-aws.md]

```sql
SELECT sum(length(to_csv(struct(*)))) FROM `source_table`;
```

## Related Concepts

- [Online Tables](/concepts/online-tables.md) — Overview and creation guide
- [Delta Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Required for incremental sync modes
- Feature Serving — Common use case for online tables
- [Model Serving](/concepts/model-serving.md) — Automatic feature lookup from online tables
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) — Querying online tables via federation
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for online tables

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
