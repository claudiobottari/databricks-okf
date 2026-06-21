---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75a0968e0c40a80224777af66d1539559f667be204c6029c60c5fc4c48245016
  pageDirectory: concepts
  sources:
    - read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-catalog
  citations:
    - file: read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
title: OpenSharing Catalog
description: A special catalog type in Unity Catalog created from a share, providing read-only access to shared data assets (tables, views, volumes, notebooks) with a 3-level namespace structure (catalog.schema.table).
tags:
  - unity-catalog
  - data-sharing
  - catalog-management
timestamp: "2026-06-19T20:07:19.418Z"
---

## OpenSharing Catalog

An **OpenSharing Catalog** is a [Unity Catalog](/concepts/unity-catalog.md) catalog created from a provider's share using the [Databricks-to-Databricks OpenSharing](/concepts/databricks-to-databricks-sharing.md) protocol. Unlike regular catalogs, an OpenSharing Catalog provides read-only access to the data, schemas, views, volumes, notebooks, and models that a data provider has shared. The data is available in near real‑time and can be queried using standard three‑level namespace syntax (`catalog.schema.table`). ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

OpenSharing Catalogs are listed under **Catalog > Shared** in Databricks Catalog Explorer and have a catalog type of **OpenSharing**. You can view this type on the catalog details page or by running `DESCRIBE CATALOG`. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Creating an OpenSharing Catalog

A privileged user creates an OpenSharing Catalog from a provider share. The required permissions are:

- A [Metastore](/concepts/metastore.md) admin, **or**
- A user with both the `CREATE CATALOG` and `USE PROVIDER` privileges for the Unity Catalog [Metastore](/concepts/metastore.md), **or**
- A user with `CREATE CATALOG` privilege and ownership of the provider object. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

Creation is supported through Catalog Explorer, SQL commands (`CREATE CATALOG`), the Databricks CLI, or the Databricks REST APIs. You may also mount a share to an existing OpenSharing Catalog if you have the `USE PROVIDER` privilege (or own the provider object) and either own the existing catalog or have both `MANAGE` and `USE CATALOG` on it. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

If the share includes views, the catalog name must differ from the name of the provider’s catalog that contains the referenced tables. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Permissions

By default, the catalog creator is the owner of all objects in the OpenSharing Catalog and can manage permissions for any of them. Privileges are inherited downward in the catalog schema hierarchy. Only read privileges can be granted:

- `SELECT` on tables (and by inheritance on schemas and catalog).
- `READ VOLUME` on volumes.
- `USE CATALOG` to allow notebook preview and cloning.
- `EXECUTE` on registered models for inference.

Write or update privileges cannot be granted. The catalog owner can delegate ownership of objects to other users or groups. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Reading Data

Data in an OpenSharing Catalog can be read using Catalog Explorer, notebooks, SQL queries, the Databricks CLI, or the Databricks REST APIs. Supported object types include:

- **Tables** – including managed Delta tables, foreign tables, foreign Iceberg tables, streaming tables, and materialized views.
- **Views** – shared views have specific restrictions (e.g., support for a subset of functions, no history, streaming limitations).
- **Volumes** – readable with `READ VOLUME` privilege.
- **Notebooks** – previewable and clonable with `USE CATALOG` privilege.
- **Models** – loadable for batch inference with `EXECUTE` privilege.
- **Python UDFs** – accessible like tables.
- **FeatureSpecs** – deployable to serving endpoints after publishing to an online store.

If the table is shared with history, you can query as-of versions or timestamps, and use change data feed (CDF) or Spark Structured Streaming. Deletion vectors and column mapping require Databricks Runtime 14.1+ (batch) or 14.2+ (CDF/streaming). ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Supported Features

- **Attribute‑Based Access Control (ABAC)** – create row filters and column masks on shared tables (except streaming tables and materialized views).
- **Row tracking** – query `_metadata.row_id` columns when the provider enables row tracking.
- **Transactions** – supported on tables shared with history, foreign tables, views, and streaming tables/materialized views (with limitations).
- **Cross‑account sharing** – within the same account or across accounts using serverless or classic compute (with some `responseFormat` requirements).

### Limitations

- All data is read‑only.
- Creating streaming tables on shared materialized views is not allowed.
- History queries are not supported on shared materialized views.
- Naming conflicts can occur for shared views if the catalog name matches a provider catalog.
- Query timeouts for views that require on‑the‑fly materialization (5‑minute limit; avoid with serverless compute).
- Column changes from the provider may take up to one minute to appear in Catalog Explorer.
- Private endpoints block notebook cloning from shared catalogs.
- When accessing shared foreign tables, you cannot bypass cluster restrictions.

^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Databricks-to-Databricks OpenSharing](/concepts/databricks-to-databricks-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Data Sharing](/concepts/delta-sharing.md)
- [Profiling Metrics Table](/concepts/profile-metrics-table.md) (for monitoring shared data quality)
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md) (applies to profiling, not to OpenSharing itself)

### Sources

- read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md](/references/read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws-21150d4f.md)
