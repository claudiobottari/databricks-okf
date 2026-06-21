---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 873a7274310837deb831747730a70149db03b87189633125157fae212557b751
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-limitations
    - OTL
    - OTLP
    - online-table-limitations-and-constraints
    - Constraints and Online Table Limitations
    - OTLAC
    - online-tables-limitations
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table Limitations
description: Constraints on online tables including 1 per source table, 1000 column max, 2TB metastore-wide preview limit, 750 MB/sec max read throughput, and restrictions on primary key data types.
tags:
  - databricks
  - limitations
  - scalability
timestamp: "2026-06-19T09:53:32.502Z"
---

# Online Table Limitations

**Online Table Limitations** documents the constraints and unsupported configurations that apply when using Databricks Online Tables. Online tables are read-only, row-oriented copies of Delta Tables optimized for low-latency online access, but they are subject to several technical and operational limits.

## General Service Constraints

Online tables are in **Public Preview** and available only in specific AWS regions: `us-east-1`, `us-west-2`, `eu-west-1`, `ap-southeast-1`, and `ap-southeast-2`. ^[databricks-online-tables-legacy-databricks-on-aws.md]

When accessed via [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md), only read operations (`SELECT`) are supported and a Serverless SQL warehouse must be used. This usage is intended for interactive or debugging purposes only and should not be used for production or mission-critical workloads. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Source Table and Sync Limitations

- **Only one online table is supported per source table.** ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Foreign, system, and internal tables are not supported as source tables.** ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **OpenSharing tables** are only supported in **Snapshot** sync mode. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Source tables without [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) enabled** support only the **Snapshot** sync mode. Triggered or Continuous modes require Change Data Feed to be enabled on the source table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Supported source securable kinds** include `TABLE_EXTERNAL`, `TABLE_DELTA`, `TABLE_DELTA_EXTERNAL`, `TABLE_DELTASHARING`, `TABLE_DELTASHARING_MUTABLE`, `TABLE_STREAMING_LIVE_TABLE`, `TABLE_STANDARD`, `TABLE_FEATURE_STORE`, `TABLE_FEATURE_STORE_EXTERNAL`, `TABLE_VIEW`, `TABLE_VIEW_DELTASHARING`, and `TABLE_MATERIALIZED_VIEW`. Source tables of other types cannot be used. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Column and Data Type Constraints

- **Maximum of 1000 columns** per online table and its source table combined. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Primary key columns** cannot be of type `ARRAY`, `MAP`, or `STRUCT`. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Null primary keys cause row omission**: if a column used as a primary key contains a null value, the entire row from the source table is ignored. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Column names** are limited to 64 characters. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **String columns** are limited to 64 KB in length. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Maximum row size** is 2 MB. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Naming Rules

- Catalog, schema, and table names of an online table can only contain alphanumeric characters and underscores, and must not start with numbers. Dashes (`-`) are not allowed. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Capacity and Throughput Limits

- **Metastore-wide size limit** during Public Preview: the combined size of all online tables in a Unity Catalog [Metastore](/concepts/metastore.md) is 2 TB (uncompressed user data). This uncompressed size can be significantly larger than the compressed size shown in Catalog Explorer; the difference can be up to 100×. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Maximum read throughput** per [Metastore](/concepts/metastore.md) is approximately 750 MB/sec. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Permission Model Requirements

- The Unity Catalog [Metastore](/concepts/metastore.md) must have **Privilege Model Version 1.0** to create online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- A Databricks admin must accept the **Serverless Terms of Service** in the account console. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Delta Table](/concepts/delta-lake-table.md) – The source table type for online tables.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Required for incremental sync modes.
- Feature Serving – Common use case for online tables.
- [Model Serving](/concepts/model-serving.md) – Automatic feature lookup from online tables.
- RAG Applications – Structured data lookup using online tables.
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) – Alternative access method with read-only limitation.

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
