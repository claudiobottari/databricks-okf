---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba7c652f730b1b1cb1f485580feb057ebda7ceb57313cd0ab38dd1727f6a5af1
  pageDirectory: concepts
  sources:
    - read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-to-databricks-opensharing-protocol
    - DOP
    - Databricks-to-Databricks Sharing Protocol
    - OpenSharing Databricks-to-Databricks Sharing Protocol
  citations:
    - file: read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
title: Databricks-to-Databricks OpenSharing Protocol
description: A Databricks-managed secure data sharing protocol that does not require credential files, relying instead on Unity Catalog metastore identifiers for establishing connections between provider and recipient workspaces.
tags:
  - delta-sharing
  - security
  - data-sharing
timestamp: "2026-06-19T20:07:15.140Z"
---

# Databricks-to-Databricks OpenSharing Protocol

The **Databricks-to-Databricks OpenSharing Protocol** is a secure data-sharing mechanism managed by Databricks that enables organizations to share data assets — including tables, views, volumes, notebooks, models, Python UDFs, and `FeatureSpecs` — directly between two Databricks workspaces that are both enabled for [Unity Catalog](/concepts/unity-catalog.md). Unlike the [open sharing](/concepts/opensharing.md) protocol, the Databricks-to-Databricks protocol does not require a credential file or bearer token; instead, Databricks manages a secure connection between the provider and the recipient using the recipient's Unity Catalog [Metastore](/concepts/metastore.md) identifier. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Requirements

To participate as a recipient in the Databricks-to-Databricks protocol, both of the following conditions must be met: the recipient must have access to a Databricks workspace that is enabled for Unity Catalog, and the data provider must be using the Databricks-to-Databricks protocol rather than the Databricks-to-Open sharing protocol. If either requirement is not satisfied, the recipient must follow the instructions for reading data using the [open sharing protocol with bearer tokens](/concepts/opensharing.md). ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## How It Works

A member of the recipient's team provides the data provider with a unique identifier for their Unity Catalog [Metastore](/concepts/metastore.md). The provider uses this identifier to create a secure sharing connection. Shared data then becomes visible in the recipient's workspace as a **share** — a container for datasets and notebooks. A privileged user in the recipient's workspace creates a **catalog** from the share, and the data objects within the catalog (schemas, tables, views, volumes, notebooks, models) can be granted read-only access to other users. This access is read-only; write and update privileges cannot be granted. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

Updates made by the provider to shared tables, views, volumes, and partitions are reflected in the recipient's workspace in near real time. However, column changes (add, rename, delete) may take up to one minute to appear in Catalog Explorer, and new shares and share updates are cached for one minute before they become available for viewing and querying. Metadata in `information_schema` from a shared catalog is updated only when the shared table is queried directly or when a `DESCRIBE` or `REFRESH FOREIGN` command is run. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Permissions Required

Listing and viewing details about providers and shares requires the `USE PROVIDER` privilege; otherwise, users see only the providers and shares they own. Creating a catalog from a provider share requires either [Metastore](/concepts/metastore.md) admin privileges, or having both `CREATE CATALOG` and `USE PROVIDER` privileges, or having `CREATE CATALOG` with ownership of the provider object. Granting read-only access to schemas, tables, and volumes follows the standard Unity Catalog privilege hierarchy. Viewing notebooks requires the `USE CATALOG` privilege on the catalog. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Working with Shares and Catalogs

A catalog created from a share has an **OpenSharing** catalog type. It can be created via Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands (`CREATE CATALOG`). Alternatively, a share can be mounted to an existing shared catalog. The 3-level namespace (`catalog.schema.table` or `catalog.schema.volume`) is preserved. The catalog owner (by default the creator) can delegate ownership of data objects and manage permissions. Unmounting a share removes the data asset from its catalog; users with `USE CATALOG` and `MANAGE` privileges on the shared catalog can perform this operation. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Supported Data Types and Operations

### Tables

Shared tables can be queried using any Databricks tool (Catalog Explorer, notebooks, SQL, CLI, REST APIs) with `SELECT` privilege. If the table is shared **with history**, users can query historical versions (`VERSION AS OF`, `TIMESTAMP AS OF`) and use the change data feed (CDF). Tables with deletion vectors or column mapping enabled support batch reads on Databricks Runtime 14.1+; CDF and streaming queries require 14.2+. Row tracking columns are accessible if the provider enabled row tracking. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Foreign Tables and Foreign Iceberg Tables

Shared foreign tables (including foreign Iceberg tables) can be queried similarly, with additional costs for sharing. Foreign Iceberg tables require Databricks Runtime 15.4 LTS or above and support only snapshot and streaming queries. Cluster restriction bypass is not allowed for foreign tables. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Views

Shared views support a subset of built-in functions. Recipients cannot query more than 20 shared views in a single query, and those views cannot come from more than five provider shares. When the provider is from the same account (or when using serverless compute in a different account), dependent views from the same provider cannot be referenced together in one query. The catalog name for a shared catalog containing a view must differ from any provider catalog that contains a table referenced by the view. Queries that require on-the-fly materialization time out after 5 minutes unless serverless compute is used. History and streaming are not supported on views. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Streaming Tables and Materialized Views

Shared streaming tables and materialized views can be queried similarly to tables, with some SQL limitations (e.g., `current_recipient` and `DESCRIBE EXTENDED` are not supported). When using classic compute across accounts, column-mapped materialized views or streaming tables require the `responseFormat=delta` option. History cannot be queried, and the refresh status and schedule of materialized views are not accessible. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Volumes, Notebooks, Models, Python UDFs, and FeatureSpecs

Volumes can be read with `READ VOLUME` privilege. Notebooks can be previewed and cloned by any user with `USE CATALOG` on the catalog. Models can be loaded for batch inference with `EXECUTE` on the model plus schema and catalog privileges. Python UDFs and `FeatureSpecs` are accessible after mounting the share. Serving a shared `FeatureSpec` requires creating an online store and publishing dependent tables in the recipient's workspace. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## ABAC and Row Filters / Column Masks

Attribute-based access control (ABAC) policies can be created for shared tables, schemas, and catalogs. Row filters and column masks can be manually applied to shared tables and foreign tables, but not to streaming tables or materialized views. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Limitations

- Column changes and new shares are cached for up to one minute. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- `information_schema` metadata may appear stale until the shared table is queried directly or `REFRESH FOREIGN` is run. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- View queries are limited to 20 views and 5 provider shares, with a 5-minute timeout for on-the-fly materialization (unless using serverless compute). ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- Shared streaming tables and materialized views do not support history, refresh schedules, or `DESCRIBE EXTENDED`. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- Private endpoints prevent reading shared notebooks. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- SAP BDC shares require serverless compute or Databricks Runtime 15+. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying open standard for sharing data.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance platform that enables Databricks-to-Databricks sharing.
- [OpenSharing](/concepts/opensharing.md) — The alternative protocol using bearer tokens.
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for managing shared catalogs.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Feature for tracking table changes in shared tables.
- Spark Structured Streaming — Supported streaming source for shared tables with history.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Policy-based access control applicable to shared objects.

## Sources

- read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md](/references/read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws-21150d4f.md)
