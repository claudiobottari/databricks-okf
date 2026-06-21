---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9855d6a09667f953cf9dcf5d5bb15133698fb9234294e622af740d9b8abe3951
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-limitations-and-constraints
    - Constraints and Online Table Limitations
    - OTLAC
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table Limitations and Constraints
description: Comprehensive set of constraints for Databricks online tables including metastore-wide size limits, column count limits, data type restrictions, primary key requirements, and throughput caps.
tags:
  - databricks
  - limitations
  - constraints
  - online-tables
timestamp: "2026-06-19T18:15:06.004Z"
---

---  
title: Online Table Limitations and Constraints  
summary: Defined constraints for online tables including 2TB uncompressed metastore-wide limit, ~750 MB/s max read throughput, 1000-column max, 64KB string column limit, 2MB row size, and restrictions on primary key data types and naming conventions.  
sources:  
  - databricks-online-tables-legacy-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-18T15:09:04.990Z"  
updatedAt: "2026-06-19T14:52:40.498Z"  
tags:  
  - databricks  
  - limitations  
  - quotas  
aliases:  
  - online-table-limitations-and-constraints  
  - Constraints and Online Table Limitations  
  - OTLAC  
confidence: 1  
provenanceState: extracted  
inferredParagraphs: 0  
---

# Online Table Limitations and Constraints

This page documents the known limitations and constraints for [Databricks Online Tables (Legacy)](/concepts/databricks-online-tables-legacy.md) during Public Preview. Understanding these restrictions is essential when planning to use online tables for real-time serving, RAG applications, or Model Serving with automatic feature lookup.

## Source Table Constraints

- **One online table per source table**: Only a single online table can be created from a given source Delta table.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Unsupported source table types**: Foreign tables, system tables, and internal tables cannot be used as source tables for an online table.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Supported source table types**: The source table must have a supported `Securable Kind`, such as `TABLE_EXTERNAL`, `TABLE_DELTA`, `TABLE_DELTA_EXTERNAL`, `TABLE_DELTASHARING`, `TABLE_DELTASHARING_MUTABLE`, `TABLE_STREAMING_LIVE_TABLE`, `TABLE_STANDARD`, `TABLE_FEATURE_STORE`, `TABLE_FEATURE_STORE_EXTERNAL`, `TABLE_VIEW`, `TABLE_VIEW_DELTASHARING`, or `TABLE_MATERIALIZED_VIEW`.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **OpenSharing tables**: Only **Snapshot** sync mode is supported for OpenSharing source tables.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Change data feed requirement**: To use **Triggered** or **Continuous** sync mode, the source table must have Delta Change Data Feed enabled. Source tables without this feature only support **Snapshot** mode.^[databricks-online-tables-legacy-databricks-on-aws.md]

## Schema and Data Type Constraints

- **Maximum columns**: An online table and its source table together can have at most 1,000 columns.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Primary key restrictions**: Columns of data types `ARRAY`, `MAP`, or `STRUCT` cannot be used as primary keys. If a primary key column contains `NULL` values in the source table, those rows are ignored during synchronization.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **String column length**: Columns of type `String` are limited to 64 KB in length.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Maximum row size**: The total size of a single row is limited to 2 MB.^[databricks-online-tables-legacy-databricks-on-aws.md]

## Naming Constraints

- **Allowed characters**: Catalog, schema, and table names for an online table may only contain alphanumeric characters (`a–z`, `A–Z`, `0–9`) and underscores (`_`). Names must not start with a digit. Dashes (`-`) are not permitted.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Column name length**: Column names are limited to 64 characters.^[databricks-online-tables-legacy-databricks-on-aws.md]

## Performance and Scalability Limits

- **Metastore-wide storage limit**: During Public Preview, the combined uncompressed size of all online tables in a Unity Catalog [Metastore](/concepts/metastore.md) is limited to 2 TB (uncompressed user data). The uncompressed, row-oriented size can be significantly larger than the compressed size shown in Catalog Explorer — the difference can be up to 100× depending on data content.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Maximum read throughput**: The maximum read throughput for a [Metastore](/concepts/metastore.md) is approximately 750 MB/sec.^[databricks-online-tables-legacy-databricks-on-aws.md]

## Access and Permission Requirements

- **Unity Catalog requirement**: The workspace must be enabled for Unity Catalog. A model must be registered in Unity Catalog to access online tables.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Serverless Terms of Service**: A Databricks admin must accept the Serverless Terms of Service in the account console before online tables can be used.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Lakehouse Federation restrictions**: When using online tables via Lakehouse Federation, only read operations (`SELECT`) are supported, and a Serverless SQL warehouse must be used. This access mode is intended for interactive or debugging purposes only and should not be used for production or mission-critical workloads.^[databricks-online-tables-legacy-databricks-on-aws.md]

## Sync Mode Constraints

- **Snapshot-only for certain tables**: Source tables without Delta Change Data Feed, as well as OpenSharing tables, support only the **Snapshot** sync mode. **Triggered** and **Continuous** modes are not available.^[databricks-online-tables-legacy-databricks-on-aws.md]

## Troubleshooting Common Failures

- **Source table deletion**: If the source table is deleted (or deleted and recreated with the same name) while the online table is synchronizing, the online table pipeline will fail. This is common with continuously syncing tables.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Firewall blocking**: Serverless Compute must be able to access the source table. If the source table is behind a firewall, the pipeline may fail with an error about failing to start the Lakeflow Spark Declarative Pipelines service.^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Exceeding [Metastore](/concepts/metastore.md) storage limit**: When the aggregate size of all online tables exceeds the 2 TB uncompressed limit, updates may fail. Use the following query from a Serverless SQL Warehouse to estimate the uncompressed row-expanded size of a Delta table: `SELECT sum(length(to_csv(struct(*)))) FROM source_table;`.^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Online tables (legacy)](/concepts/databricks-online-tables-legacy.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- [Model Serving with Automatic Feature Lookup](/concepts/model-serving-with-automatic-feature-lookup.md)
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)
- Serverless SQL warehouse
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md)

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
