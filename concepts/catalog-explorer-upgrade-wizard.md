---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7158d6de83fe3c34c7d4c5e10b84556013fe24e79bcf01c7c5771433b8f48dbe
  pageDirectory: concepts
  sources:
    - upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - catalog-explorer-upgrade-wizard
    - CEUW
    - upgrade wizard
  citations:
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: Catalog Explorer Upgrade Wizard
description: UI-based tool in Databricks Catalog Explorer for upgrading Hive schemas and tables to Unity Catalog external tables with destination mapping, ownership assignment, and notebook generation.
tags:
  - unity-catalog
  - migration
  - user-interface
timestamp: "2026-06-19T23:19:02.314Z"
---

# [Catalog Explorer](/concepts/catalog-explorer.md) Upgrade Wizard

The **Catalog Explorer Upgrade Wizard** is a visual tool within [Catalog Explorer](/concepts/catalog-explorer.md) that enables you to upgrade tables and views from the workspace-local Hive [Metastore](/concepts/metastore.md) (`hive_metastore`) to [Unity Catalog](/concepts/unity-catalog.md). The wizard copies complete schemas (databases) and multiple tables into [Unity Catalog](/concepts/unity-catalog.md) as **external tables**, meaning no data is moved – only metadata and table definitions are registered in [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## What the Wizard Upgrades

The wizard can upgrade entire schemas and multiple tables from the `hive_metastore` catalog. Upgraded tables become [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md). Only external tables in formats supported by [Unity Catalog](/concepts/unity-catalog.md) can be upgraded using this wizard. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before using the wizard, you must have:

- A workspace with a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) and at least one catalog. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- A compute resource that supports [Unity Catalog](/concepts/unity-catalog.md) (a SQL warehouse or a cluster with standard or dedicated access mode). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- A [storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) for an IAM role that authorizes [Unity Catalog](/concepts/unity-catalog.md) to access the tables' location path. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- An [External location](/concepts/external-location.md) that references the storage credential and the data path. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- The `CREATE EXTERNAL TABLE` privilege on the external locations of the tables to be upgraded. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- If using [Standard Access Mode](/concepts/standard-access-mode.md), access to the tables in the Hive [Metastore](/concepts/metastore.md) granted via legacy table access control. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Upgrade Process

1. In the sidebar, click **Catalog** to open [Catalog Explorer](/concepts/catalog-explorer.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
2. Select `hive_metastore` as the catalog, then choose the schema (database) to upgrade. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
3. Click **Upgrade** at the top right of the schema detail view. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
4. Select all tables to upgrade and click **Next**. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
5. Set the destination catalog, schema (database), and owner for each table. You can assign the same values to multiple tables using the **Set destination** and **Set owner** buttons. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
6. Review the table configurations. Click **Previous** to modify them if needed. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
7. Choose **Run upgrade** to execute immediately or **Create notebook for upgrade** to generate a notebook that performs the upgrade. When the upgrade completes, each table's metadata is copied from the Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md), and the tables are marked as upgraded in the wizard. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Post-Upgrade Steps

After upgrading, you should:

- Define fine-grained access control using the **Permissions** tab of each new table. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- (Optional) Add a deprecated-table comment to the original Hive tables to warn users and provide a quick-fix link via [Genie Code](/concepts/genie-code.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- Modify workloads to reference the new [Unity Catalog](/concepts/unity-catalog.md) tables. If you added the deprecation comment, notebooks and SQL query editors will display the old table name in strikethrough and offer a **Quick Fix** to update code. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- (Optional) Drop the old Hive tables after verifying no dependencies remain. Dropping an external table does not delete the underlying data files. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Hive Metastore](/concepts/built-in-hive-metastore.md)
- External Tables
- [Managed Tables](/concepts/managed-tables-in-databricks.md)
- SYNC command — Alternative command-line method for upgrading external tables.
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) — Alternative method for upgrading managed Delta tables.
- CREATE TABLE AS SELECT — Another method for copying data to a managed table.
- [Genie Code](/concepts/genie-code.md) — Tool for updating deprecated table references.

## Sources

- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
