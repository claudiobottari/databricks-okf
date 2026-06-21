---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97618a894281a09d73de5144b8b2e640d9c3705baac334c5773cf65862b8ffb8
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-and-foreign-iceberg-table-sharing
    - Foreign Iceberg Table Sharing and Managed
    - MAFITS
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Managed and Foreign Iceberg Table Sharing
description: Sharing managed Iceberg tables (native to Databricks) and foreign Iceberg tables (federated from external Iceberg catalogs) with Delta Uniform support, history sharing, and specific limitations.
tags:
  - delta-sharing
  - iceberg
  - lakehouse-federation
timestamp: "2026-06-19T14:38:35.985Z"
---

# Managed and Foreign Iceberg Table Sharing

**Managed and Foreign Iceberg Table Sharing** refers to the ability to share Apache Iceberg tables — both those [managed natively in Unity Catalog](/unity-catalog/managed-iceberg-tables) and those [federated from external Iceberg catalogs via Lakehouse Federation](/lakehouse-federation/foreign-iceberg-tables) — with other Databricks workspaces or open recipients using Delta Sharing and OpenSharing. This enables organizations to securely share Iceberg-format data across business boundaries without copying underlying files.

## Overview

OpenSharing allows you to add both managed Iceberg tables and foreign Iceberg tables to a share. Shares are [securable objects in Unity Catalog](/unity-catalog/shares) that can contain tables, views, streaming tables, volumes, models, and other AI assets. A share can contain data assets from only one Unity Catalog [Metastore](/concepts/metastore.md). ^[create-shares-for-opensharing-databricks-on-aws.md]

Adding either type of Iceberg table to a share follows the same general procedure as adding other table types, but each has specific requirements and limitations.

## Managed Iceberg Tables

[Managed Iceberg tables](/iceberg/managed-tables) are Iceberg tables created and managed entirely within Databricks Unity Catalog. They are stored in the managed storage location of the catalog or schema.

### Requirements

- The share must already be created (see [Create shares for OpenSharing](/delta-sharing/create-share)).
- You must meet the general compute requirements for adding assets to a share: Databricks Runtime 11.3 LTS or above with standard or dedicated access mode for notebook operations; SQL warehouses or compute running Runtime 13.3 LTS or above for SQL-based additions.
- All [Iceberg table limitations](https://docs.databricks.com/aws/en/iceberg/#iceberg-limitations) apply.

^[create-shares-for-opensharing-databricks-on-aws.md]

### Limitations

Databricks does not support sharing managed Iceberg tables to external Iceberg clients. They can only be shared to other Databricks recipients (Databricks-to-Databricks sharing) or to open recipients using the Delta Sharing protocol. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Adding a Managed Iceberg Table to a Share

You can add a managed Iceberg table using Catalog Explorer, SQL commands, or the Databricks Unity Catalog CLI.

**Catalog Explorer**:
1. From your workspace, open **Catalog** and navigate to **OpenSharing** (gear icon).
2. On the **Shared by me** tab, select the share and click **Manage assets > Edit assets**.
3. Search or browse for the managed Iceberg table and select it.
4. (Optional) Provide an alias for the table name that recipients will use.
5. Click **Save**.

**SQL** example:
```sql
ALTER SHARE share_name ADD TABLE catalog.schema.managed_iceberg_table;
```

^[create-shares-for-opensharing-databricks-on-aws.md]

## Foreign Iceberg Tables

[Foreign Iceberg tables](/lakehouse-federation/foreign-tables) are tables federated from remote Iceberg catalogs using [Lakehouse Federation](/lakehouse-federation/). They allow you to query external Iceberg data as if it were local, and OpenSharing enables you to share these foreign tables without copying data into Databricks.

### Additional Requirements

- You must enable the **Lakehouse Federation Sharing** preview at the account level (see [Manage Databricks previews](/admin/workspace-settings/manage-previews)). ^[create-shares-for-opensharing-databricks-on-aws.md]
- If you are sharing foreign Iceberg tables with open recipients who are not using Iceberg clients, you must use [default storage](/storage/default-storage) and enable the **OpenSharing for Default Storage – Expanded Access** preview. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Foreign Iceberg tables must have [Delta Uniform](https://docs.databricks.com/aws/en/delta/uniform) enabled. Without Uniform, the table cannot be added to a share. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing with open recipients not using Iceberg clients, data is filtered and materialized using the provider's compute and storage, which may incur additional costs. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Databricks recommends periodically refreshing foreign Iceberg tables to ensure recipients receive the freshest data. Set up a scheduled job or run `REFRESH TABLE` to keep metadata in sync with the remote source. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Limitations

- Partitions are not supported when sharing foreign Iceberg tables. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When sharing with open recipients not using an Iceberg client, `LIMIT` clauses and predicate pushdown are not supported. The system fully materializes all query results before returning them to the recipient, regardless of query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Adding a Foreign Iceberg Table to a Share

The procedure is similar to adding a managed Iceberg table.

**Catalog Explorer**:
1. Open **Catalog** > **OpenSharing** (gear icon) > **Shared by me**.
2. Select the share and click **Manage assets > Edit assets**.
3. Search or browse for the foreign Iceberg table and select it.
4. (Optional) Provide an alias for the table name that recipients will use.
5. Click **Save**.

Foreign Iceberg tables are automatically shared with full history. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Sharing to External Iceberg Clients

You can also share foreign Iceberg tables to recipients using external Iceberg clients. This capability requires specific configuration; see [Enable sharing to external Iceberg clients](/delta-sharing/iceberg-clients) for more information. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol for Databricks-to-open sharing
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying open protocol for sharing data
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) – Connects Databricks to external databases and catalogs
- [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md) – Storage and governance for managed tables
- Foreign Tables – Federated tables from external systems
- [Delta Uniform](/concepts/delta-uniform.md) – Enables Iceberg clients to read Delta Lake tables
- [Default Storage](/concepts/workspace-default-storage-path.md) – System storage used for materialization in OpenSharing

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
