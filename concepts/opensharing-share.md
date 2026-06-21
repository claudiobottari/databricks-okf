---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 978c3304fa061e7d7f8d88c15020c7fe032069ba975e482bd842e586965f5f17
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-share
    - OpenSharing Data Shares
    - OpenSharing Shares
    - OpenSharing shares
    - Manage OpenSharing Data Shares
    - Managing OpenSharing Shares
    - OpenSharing shared tables
    - creating shares
    - opensharing-share-object
    - OSO
    - Share Object
    - opensharing-share-unity-catalog
    - OS(C
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
    - file: manage-shares-for-opensharing-databricks-on-aws.md
title: OpenSharing Share
description: A securable object in Unity Catalog used to share data and AI assets (tables, views, models, notebooks, volumes, etc.) with one or more recipients.
tags:
  - delta-sharing
  - unity-catalog
  - data-sharing
timestamp: "2026-06-19T14:38:18.821Z"
---

---
title: OpenSharing Share
summary: A securable object in Unity Catalog used to share data assets (tables, views, notebooks, models, etc.) with recipients across Databricks-to-Databricks or Databricks-to-Open sharing protocols.
sources:
  - create-shares-for-opensharing-databricks-on-aws.md
  - manage-shares-for-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:24:21.737Z"
updatedAt: "2026-06-19T09:37:56.559Z"
tags:
  - delta-sharing
  - unity-catalog
  - data-sharing
aliases:
  - opensharing-share
confidence: 0.98
provenanceState: merged
inferredParagraphs: 2
---

# OpenSharing Share

**OpenSharing Share** is a securable object in [Unity Catalog](/concepts/unity-catalog.md) that bundles tables, views, volumes, notebooks, AI models, and other data or AI assets for sharing with one or more recipients through the OpenSharing protocol. Shares are the fundamental building block for distributing data across different Databricks accounts, workspaces, and external platforms.^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

A share acts as a container for assets you want to share. After creating a share, you add assets to it and then grant access to recipients. Assets can be added, updated, or removed at any time. A share can contain assets from only one Unity Catalog [Metastore](/concepts/metastore.md).^[create-shares-for-opensharing-databricks-on-aws.md]

If you share an entire schema (database), the recipient gains access to all tables, streaming tables, views, materialized views, models, and volumes in the schema at the moment you share it, along with any assets added to the schema in the future.^[create-shares-for-opensharing-databricks-on-aws.md]

Share details include the owner, creator, creation timestamp, updater, updated timestamp, comments, and the list of data assets and recipients with access.^[manage-shares-for-opensharing-databricks-on-aws.md]

## Shareable Asset Types

OpenSharing Shares support a variety of asset types:^[create-shares-for-opensharing-databricks-on-aws.md]

- **Tables** – Regular Delta tables, including table partitions.
- **Streaming tables** – Tables designed for append-only streaming data.
- **Managed Iceberg tables** – Iceberg tables managed in Unity Catalog.
- **Foreign Iceberg tables** – Iceberg tables federated from external catalogs.
- **Foreign schemas and tables** – Tables federated from external data sources.
- **Views** – Read-only objects created from other tables or views.
- **Dynamic views** – Views that restrict access at the row and column level.
- **Materialized views** – Pre-computed views for improved performance.
- **Volumes** – Non-tabular data assets (files, directories).
- **Python UDFs** – User-defined functions in Python.
- **Notebooks** – Databricks notebook files.
- **AI models** – Registered MLflow models.
- **Genie Spaces** – Genie-powered AI spaces.
- **FeatureSpecs** – Feature specifications for ML.

## Creating a Share

### Requirements

Before creating a share, you must first set up OpenSharing for your account. The share owner should be a group rather than an individual user. Compute requirements vary:^[create-shares-for-opensharing-databricks-on-aws.md]

- Creating a share using a Databricks notebook requires compute running Databricks Runtime 11.3 LTS or above with standard or dedicated access mode.
- Adding a schema to a share using SQL requires a SQL warehouse or compute running Databricks Runtime 13.3 LTS or above.
- Using Catalog Explorer to create shares has no compute requirements.

### Creating a Share in Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, click **Share data**.
4. Enter the share **Name** and an optional comment.
5. Click **Save and continue**.
6. On the **Add data assets** tab, select the assets you want to share.
7. Click **Save and continue**.
8. On the **Add notebooks** tab, select any notebooks to share.
9. Click **Save and continue**.
10. On the **Add recipients** tab, select the recipients to share with.
11. Click **Share data**.

^[create-shares-for-opensharing-databricks-on-aws.md]

### Creating a Share Using SQL

```sql
CREATE SHARE share_name [COMMENT 'description'];
```

^[create-shares-for-opensharing-databricks-on-aws.md]

### Creating a Share Using CLI

```bash
databricks shares create --name share_name
```

^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding Assets to a Share

Assets can be added to an existing share through Catalog Explorer, SQL commands, or the CLI. The following sections describe specific requirements and limitations for each asset type.

### Adding Tables

To add tables to a share, you must have the `USE SCHEMA` and `USE CATALOG` permissions on the schema and catalog containing the table. Tables can be added with optional aliases, partitions, and history sharing.^[create-shares-for-opensharing-databricks-on-aws.md]

**History sharing** allows recipients to perform time travel queries, read tables with Spark Structured Streaming, or run transactions. For Databricks-to-Databricks shares, the table's Delta log is also shared to improve performance. History sharing requires Databricks Runtime 12.2 LTS or above.^[create-shares-for-opensharing-databricks-on-aws.md]

**Cloud tokens** (temporary, path-scoped cloud credentials) give recipients direct read access to shared Delta table files. Cloud tokens are used when:
- For Databricks-to-Databricks sharing: The table is shared `WITH HISTORY` and without a partition filter.
- For Databricks-to-Open sharing: The shared object is a managed or external Delta table, shared `WITH HISTORY`, without a partition filter, not a CCv2 table, and does not use default storage.

^[create-shares-for-opensharing-databricks-on-aws.md]

When cloud token access is used, recipients receive credentials scoped to the root directory of the shared Delta table, granting read access to both data files and the Delta log. The Delta log contains the commit history, information about the committer, and deleted data that has not been vacuumed.^[create-shares-for-opensharing-databricks-on-aws.md]

### Adding Partitioned Tables

To share only part of a table, provide a partition specification when adding the table to a share:^[create-shares-for-opensharing-databricks-on-aws.md]

```sql
ALTER SHARE share_name
ADD TABLE inventory
PARTITION (year = "2021"),
          (year = "2020", month = "Dec"),
          (year = "2019", month = "Dec", date = "2019-12-25");
```

### Parameterized Partition Sharing

You can share a table partition that matches recipient properties using the `CURRENT_RECIPIENT()` function, enabling dynamic partition filtering. This allows sharing the same tables across multiple accounts while maintaining data boundaries between them.^[create-shares-for-opensharing-databricks-on-aws.md]

Default properties include `databricks.accountId`, `databricks.metastoreId`, and `databricks.name`. Custom properties can be created when creating or updating a recipient. Example:^[create-shares-for-opensharing-databricks-on-aws.md]

```sql
(country = CURRENT_RECIPIENT().country)
```

### Adding Streaming Tables

Streaming tables are regular Delta tables with extra support for streaming or incremental data processing. They are designed for append-only data sources. Shareable streaming tables must be defined on Delta tables or other shareable streaming tables or views. Adding streaming tables requires a SQL warehouse or compute on Databricks Runtime 13.3 LTS or above.^[create-shares-for-opensharing-databricks-on-aws.md]

Limitations for streaming table sharing include:
- The streaming table cannot have row filters, column masks, or partition filters.
- Databricks-to-Open sharing recipients can only read the current snapshot – time travel, query history, streaming reads, and CDF are not supported.
- If the recipient doesn't have direct access to underlying data, `LIMIT` clauses and predicate pushdown aren't supported.

^[create-shares-for-opensharing-databricks-on-aws.md]

### Adding Foreign Tables and Schemas

Foreign tables are tables federated from external data sources using [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md). Sharing foreign schemas and tables requires enabling the **Lakehouse Federation Sharing** preview at the account level, and enabling serverless compute.^[create-shares-for-opensharing-databricks-on-aws.md]

When sharing foreign tables, data is queried and temporarily materialized on the provider's side. By default, the materialized data is stored in a hidden schema using Databricks default storage. To opt out of using default storage and use your own storage, open a support case.^[create-shares-for-opensharing-databricks-on-aws.md]

Foreign tables shared as part of a share do not support `LIMIT` clauses or predicate pushdown – the system fully materializes all query results before returning them to the recipient.^[create-shares-for-opensharing-databricks-on-aws.md]

For recommended performance, keep typical query results under 10 GB, use ad-hoc exploratory queries instead of frequent data dumps, and consider sharing materialized views created on top of foreign tables when using cloud-token sharing.^[create-shares-for-opensharing-databricks-on-aws.md]

### Adding Views

Views are read-only objects created from one or more tables or other views. Shareable views must be defined on Delta tables, other shareable views, or local materialized views and streaming tables. Views cannot be defined on foreign tables. Adding views requires a SQL warehouse or compute on Databricks Runtime 13.3 LTS or above.^[create-shares-for-opensharing-databricks-on-aws.md]

When sharing views, data might be queried and temporarily materialized on the provider side depending on the recipient's compute type and account relationship. The materialized data is stored in the storage location of the view's parent schema or catalog, or in the [Metastore](/concepts/metastore.md) root location.^[create-shares-for-opensharing-databricks-on-aws.md]

Limitations for view sharing include:
- Views cannot reference shared tables or shared views.
- Views cannot reference foreign tables, including foreign Iceberg tables.
- If the recipient doesn't have direct access to underlying data, `LIMIT` clauses and predicate pushdown aren't supported.

^[create-shares-for-opensharing-databricks-on-aws.md]

### Dynamic Views for Fine-Grained Access Control

Dynamic views using the `CURRENT_RECIPIENT()` function can limit recipient access according to properties specified in the recipient definition. This enables row-level and column-level access control for shared data. The `CURRENT_RECIPIENT` function is supported in Databricks Runtime 14.2 and above.^[create-shares-for-opensharing-databricks-on-aws.md]

### Adding Schemas

Adding an entire schema to a share provides recipients with access to all data assets in the schema at the time of sharing, as well as any assets added to the schema over time. This includes all tables, views, and volumes. Tables shared this way always include full history.^[create-shares-for-opensharing-databricks-on-aws.md]

Schema sharing limitations include:
- Schemas with unsupported data assets have those assets filtered out and not shared.
- Table aliases, partitions, and volume aliases are not available if you share an entire schema.
- Schema-level aliasing is not supported.

^[create-shares-for-opensharing-databricks-on-aws.md]

### Sharing ABAC-Secured Tables

Tables or schemas secured by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies can be shared like standard tables. However, the share owner must be a *privileged user* – the share owner and a user who is excluded from the ABAC policies applied to the data asset. The policy does not govern the recipient's access; recipients have full access to the shared

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
2. [manage-shares-for-opensharing-databricks-on-aws.md](/references/manage-shares-for-opensharing-databricks-on-aws-a4962f9a.md)
