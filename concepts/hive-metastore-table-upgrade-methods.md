---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e1bbf26ad938103a3150f15e862eaebdec13329c79f10cd055df89076ff2264
  pageDirectory: concepts
  sources:
    - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-table-upgrade-methods
    - HMTUM
  citations:
    - file: upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
title: Hive Metastore Table Upgrade Methods
description: Techniques for upgrading Hive metastore tables to Unity Catalog, including ALTER TABLE SET MANAGED/EXTERNAL, SYNC, and CREATE TABLE AS SELECT.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - table-migration
timestamp: "2026-06-19T23:17:34.409Z"
---

# Hive [Metastore](/concepts/metastore.md) Table Upgrade Methods

**Hive [Metastore](/concepts/metastore.md) Table Upgrade Methods** are the techniques used to migrate tables and views from a legacy Hive [Metastore](/concepts/metastore.md) to a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) as part of upgrading a Databricks workspace to [Unity Catalog](/concepts/unity-catalog.md). These methods allow organizations to preserve existing data, table history, configurations, permissions, and views during the migration process. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Overview

When a workspace that was in service before it was enabled for [Unity Catalog](/concepts/unity-catalog.md) is upgraded, it has a Hive [Metastore](/concepts/metastore.md) containing data that users likely want to continue using. Databricks recommends upgrading the tables managed by the Hive [Metastore](/concepts/metastore.md) to the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). Two primary upgrade options are available: federation-based upgrade and direct table upgrade. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Option 1: Federate, Then Upgrade Foreign Tables

The recommended approach is a two-step process that first federates the Hive [Metastore](/concepts/metastore.md) or AWS Glue catalog as a foreign catalog, then upgrades the foreign tables in place. This method allows migration without data movement while preserving table history, configuration, permissions, and views. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 1: Federate the Hive [Metastore](/concepts/metastore.md)

Federate the Hive [Metastore](/concepts/metastore.md) or AWS Glue catalog as a foreign catalog in [Unity Catalog](/concepts/unity-catalog.md). This enables access to existing tables through [Unity Catalog](/concepts/unity-catalog.md) and prepares them for upgrading. For instructions, see [Hive Metastore Federation](/concepts/hive-metastore-federation.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

If you choose not to upgrade your tables and want to continue working with the federated catalog permanently, you can do so. However, Databricks recommends completing the upgrade to take full advantage of [Unity Catalog](/concepts/unity-catalog.md) features. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 2: Upgrade Foreign Tables

After federating, upgrade the foreign tables to [Unity Catalog](/concepts/unity-catalog.md) tables without any data movement. This workflow upgrades tables in place, preserving table history, configuration, permissions, and views. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

#### Upgrade to a Managed Table

To upgrade a foreign table to a [Unity Catalog](/concepts/unity-catalog.md) managed table, run the following SQL command:

```sql
ALTER TABLE <foreign_catalog>.<schema>.<table_name> SET MANAGED;
```

Databricks recommends upgrading to a managed table to unlock [Unity Catalog](/concepts/unity-catalog.md) predictive optimization, which includes automatic maintenance (compaction, clustering, vacuuming) and performance improvements. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

#### Upgrade to an External Table

To upgrade a foreign table to a [Unity Catalog](/concepts/unity-catalog.md) external table instead, run the following command:

```sql
ALTER TABLE <foreign_catalog>.<schema>.<table_name> SET EXTERNAL;
```

^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Remove the Connection

After tables are migrated and you no longer rely on federation to your external catalog, you can remove the connection:

```sql
ALTER CATALOG <foreign_catalog> DROP CONNECTION;
```

^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Option 2: Upgrade Tables Directly

If you choose not to use the federation-based upgrade workflow, you can upgrade tables directly using `SYNC` or `CREATE TABLE AS SELECT`. See Upgrade Hive tables and views to Unity Catalog for detailed instructions. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Post-Upgrade Steps

### Grant Access

After upgrading or federating tables, grant account-level users, groups, or service principals access to the new tables. See Manage privileges in Unity Catalog. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Update Queries and Jobs

While transitioning from the workspace-local Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md), you can continue to use queries and jobs that reference data registered in the Hive [Metastore](/concepts/metastore.md) using [Hive Metastore Federation](/concepts/hive-metastore-federation.md) (recommended) or the syntax described in [Work with the legacy Hive metastore alongside Unity Catalog](/concepts/hive-metastore-federation-to-unity-catalog.md). Eventually, update all queries and jobs to use [Unity Catalog](/concepts/unity-catalog.md) tables and syntax. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Disable the Hive [Metastore](/concepts/metastore.md)

When you have completed your [Unity Catalog](/concepts/unity-catalog.md) migration or federated your Hive [Metastore](/concepts/metastore.md) as a foreign catalog governed by [Unity Catalog](/concepts/unity-catalog.md), workspace admins can prevent users from bypassing [Unity Catalog](/concepts/unity-catalog.md) and accessing tables registered in the Hive [Metastore](/concepts/metastore.md). See Disable access to the Hive metastore. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for Databricks
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Enables [Unity Catalog](/concepts/unity-catalog.md) to govern tables registered in a Hive [Metastore](/concepts/metastore.md)
- Upgrade Hive tables and views to Unity Catalog — Direct upgrade methods using SYNC and CREATE TABLE AS SELECT
- [UCX utilities](/concepts/ucx-unity-catalog-upgrade-utilities.md) — Databricks Labs project for larger-scale migrations
- Convert a foreign table to a managed Unity Catalog table — Detailed workflow for the SET MANAGED approach
- Manage privileges in Unity Catalog — Granting access to upgraded tables

## Sources

- upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws-30141815.md)
