---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3892025984c7389fe9a946efa8b6c46febfc7f76a56c8928dff72be63f0618bd
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shareable-asset-types-in-opensharing
    - SATIO
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Shareable Asset Types in OpenSharing
description: The broad range of data and AI assets that can be included in an OpenSharing share, including Delta tables, streaming tables, Iceberg tables, views, volumes, notebooks, Python UDFs, AI models, FeatureSpecs, and Genie Spaces.
tags:
  - delta-sharing
  - asset-types
  - catalog
timestamp: "2026-06-18T11:25:07.284Z"
---

# Shareable Asset Types in OpenSharing

**Shareable Asset Types in OpenSharing** refers to the various data and AI assets that can be added to a [Unity Catalog](/concepts/unity-catalog.md) share and distributed to recipients through [OpenSharing](/concepts/opensharing.md) (formerly Delta Sharing). A share is a securable object in Unity Catalog that can contain one or more asset types, allowing providers to selectively expose data, code, and models to consumers. All assets within a single share must originate from the same Unity Catalog [Metastore](/concepts/metastore.md). ^[create-shares-for-opensharing-databricks-on-aws.md]

The following asset types are supported:

| Asset Type | Description |
|------------|-------------|
| Tables and table partitions | Standard Delta tables, with optional alias, partition filters, and history sharing |
| Schemas (databases) | Entire schemas including all current and future tables, views, and volumes |
| Streaming tables | Append-only Delta tables designed for incremental processing |
| Managed Iceberg tables | Iceberg tables created in Unity Catalog (not shared to external Iceberg clients) |
| Foreign Iceberg tables | Tables federated from foreign Iceberg catalogs via Lakehouse Federation |
| Foreign schemas and tables | Schemas and tables from external data sources via Lakehouse Federation |
| Views | Read-only SQL views defined on Delta tables or other shareable views |
| Dynamic views | Views using `CURRENT_RECIPIENT()` for row- and column-level access control |
| Materialized views | Pre-computed views that improve query performance |
| Volumes | Non-tabular data assets (files, directories) |
| Python UDFs | User-defined functions written in Python |
| Notebooks | Databricks notebook files |
| AI models | Registered MLflow models and foundation models |
| Genie Spaces | Interactive Genie query spaces |
| `FeatureSpecs` | Feature engineering specifications |

^[create-shares-for-opensharing-databricks-on-aws.md]

## Tables and Table Partitions

Tables are the most common shareable asset. Providers can add individual tables or entire schemas to a share. When adding a table, optional features include: ^[create-shares-for-opensharing-databricks-on-aws.md]

- **Alias** – An alternate table name visible to recipients; recipients must use the alias in queries. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Partition filters** – Share only a subset of data by specifying partition values. Partitions can be static (e.g., `year = 2021`) or dynamic using [Recipient Properties](/concepts/recipient-properties.md) (e.g., `country = CURRENT_RECIPIENT().country`). ^[create-shares-for-opensharing-databricks-on-aws.md]
- **History sharing** – Share the full Delta history, enabling time travel, change data feed (CDF), and streaming reads. Required for tables with [Deletion Vectors](/concepts/deletion-vectors.md) or [column mapping](/concepts/column-mapping-in-delta-lake.md). ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Cloud tokens** – Temporary, path-scoped cloud credentials that give recipients direct read access to Delta table files for improved performance. Eligibility depends on the sharing protocol and table type. ^[create-shares-for-opensharing-databricks-on-aws.md]

Tables shared with history and without partition filters may qualify for cloud token access, which bypasses the OpenSharing server for data reads. For [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), cloud tokens are exchanged directly between metastores. For [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md), open recipients can call the Generate Temporary Table Credentials endpoint. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Sharing ABAC-Governed Tables

Tables secured by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies (row filters, column masks) can be shared, but only by a privileged user – the share owner who is excluded from the ABAC policy. Recipients receive full access to the asset; the policy does not govern the recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Schemas

Adding an entire schema (database) to a share grants recipients access to all tables, streaming tables, views, materialized views, models, and volumes in the schema at the time of sharing, plus any new assets added later. Tables shared via schema always include full history. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Limitations:**
- Schema-level aliasing is not supported. Schemas with the same name from different catalogs cannot be added to the same share. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Table aliases, partitions, and volume aliases are removed when the entire schema is added. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Assets with certain features (liquid clustering with partitions, R2 V2 checkpoints, collations, row filters, column masks, `SHALLOW CLONE`) are filtered out and not shared. ^[create-shares-for-opensharing-databricks-on-aws.md]

Adding or updating a schema via SQL requires a SQL warehouse or compute running Databricks Runtime 13.3 LTS or above. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Streaming Tables

Streaming tables are Delta tables designed for append-only, incremental data processing. They can be shared as long as they are defined on Delta tables or other shareable streaming tables/views. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Requirements:**
- Compute or SQL warehouse on Databricks Runtime 13.3 LTS or above. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Workspace-catalog binding must allow read/write access if workspace-catalog bindings are enabled. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Limitations:**
- Cannot have row filters, column masks, or partition filters on the streaming table itself. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Open recipients can only read the current snapshot; time travel, CDF, and streaming reads are not supported for Databricks-to-Open sharing. ^[create-shares-for-opensharing-databricks-on-aws.md]
- `LIMIT` and predicate pushdown are not supported when recipients lack direct data access. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Managed Iceberg Tables

Managed Iceberg tables in Unity Catalog can be shared. Databricks does not support sharing managed Iceberg tables to external Iceberg clients. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Foreign Iceberg Tables

Foreign Iceberg tables are tables federated from external Iceberg catalogs using [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md). They require Delta Uniform to be enabled. Sharing is supported both to Databricks recipients and to external Iceberg clients. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Requirements:**
- Lakehouse Federation Sharing preview must be enabled at the account level. ^[create-shares-for-opensharing-databricks-on-aws.md]
- For open recipients not using Iceberg clients, default storage must be configured with the OpenSharing for Default Storage preview. ^[create-shares-for-opensharing-databricks-on-aws.md]

Foreign Iceberg tables are automatically shared with full history. Databricks recommends scheduling periodic `REFRESH TABLE` commands to keep the shared metadata current. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Foreign Schemas and Tables (Lakehouse Federation)

Through Lakehouse Federation, providers can share foreign schemas and tables from external data sources (e.g., databases like PostgreSQL, MySQL) without copying data. Data is queried and temporarily materialized on the provider side. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Requirements:**
- Lakehouse Federation Sharing preview enabled. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Serverless compute for workflows, notebooks, and Lakeflow Spark Declarative Pipelines must be enabled in the account. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Default storage must meet requirements and have the OpenSharing for Default Storage preview enabled. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Limitations:**
- `LIMIT` clauses and predicate pushdown are not supported; the system fully materializes results. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Large materializations may fail. Databricks recommends keeping query results under 10 GB. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Views

Views are read-only objects defined from one or more tables or other views. Views can be shared with recipients. They are queried and temporarily materialized on the provider side unless recipients have direct data access. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Requirements:**
- Views must be defined on Delta tables, other shareable views, local materialized views, or streaming tables (not on foreign tables). ^[create-shares-for-opensharing-databricks-on-aws.md]
- Compute or SQL warehouse on Databricks Runtime 13.3 LTS or above. ^[create-shares-for-opensharing-databricks-on-aws.md]
- If the view's storage location has network restrictions, recipients must be allowlisted or [SecureConnect](/concepts/secureconnect.md) can be used. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Limitations:**
- Cannot reference shared tables/views or foreign tables. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Without direct data access, `LIMIT` and predicate pushdown are unsupported. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Dynamic Views

Dynamic views use the `CURRENT_RECIPIENT()` function to enforce row- and column-level access control based on recipient properties. This allows a single view definition to serve multiple recipients with different access scopes. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Requirements:**
- Databricks Runtime 14.2 or above to define the view. ^[create-shares-for-opensharing-databricks-on-aws.md]

**Limitations:**
- All limitations for regular views apply. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Materialized Views

[Materialized views](/concepts/materialized-views-in-databricks.md) are pre-computed views that improve query performance. They can be shared like standard views, with similar materialization behavior. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Volumes

[Volumes](/concepts/ucvolumedataset.md) allow sharing of non-tabular data assets such as files and directories. They can be added to shares alongside tables and views. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Python UDFs

Python user-defined functions (UDFs) registered in Unity Catalog can be shared. Recipients can invoke shared UDFs in their queries. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Notebooks

Notebooks can be added to a share. Providers can share individual notebooks or select multiple notebooks. Recipients gain access to view and run the shared notebook files. ^[create-shares-for-opensharing-databricks-on-aws.md]

## AI Models

AI models registered in Unity Catalog, including both customer-registered MLflow Models and Databricks-hosted foundation models, can be shared. Models appear as securable objects in the share. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Genie Spaces

[Genie Spaces](/concepts/genie-space-snapshot.md) are interactive query spaces that can be shared with recipients. See the dedicated documentation for sharing Genie Spaces. ^[create-shares-for-opensharing-databricks-on-aws.md]

## FeatureSpecs

[FeatureSpecs](/concepts/featurespec.md) are feature engineering specifications used in ML pipelines. They can be included in a share for collaborative development. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
