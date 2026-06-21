---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a8413e9de294ba91445ba5c78291961cc0f0bf0fb2e40f6bc750572fedc7d0e
  pageDirectory: concepts
  sources:
    - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-upgrade-process
    - UCUP
    - Unity Catalog upgrade
  citations:
    - file: upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
title: Unity Catalog Upgrade Process
description: The structured step-by-step process for upgrading a Databricks workspace from legacy Hive metastore and DBFS to Unity Catalog governance.
tags:
  - databricks
  - unity-catalog
  - migration
timestamp: "2026-06-19T23:20:19.431Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) Upgrade Process

The **Unity Catalog Upgrade Process** is the set of steps required to migrate a Databricks workspace from using a legacy Hive [Metastore](/concepts/metastore.md) and DBFS to being governed by [Unity Catalog](/concepts/unity-catalog.md). The upgrade involves provisioning account-level identities, attaching a workspace to a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md), migrating tables and data, updating workloads, and disabling legacy features. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Overview of Upgrade Steps

To upgrade to [Unity Catalog](/concepts/unity-catalog.md), you must complete the following high-level phases: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

1. **Provision identities** – Provision users, groups, and service principals directly to your Databricks account and turn off any workspace-level identity provisioning. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
2. **Convert workspace-local groups** – Convert any workspace-local groups to account-level groups. [Unity Catalog](/concepts/unity-catalog.md) centralizes identity management at the account level. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
3. **Attach the workspace** – Attach the workspace to a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). If no [Metastore](/concepts/metastore.md) exists for your workspace region, an account admin must create one. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
4. **Upgrade tables and views** – Upgrade tables and views managed in the [Hive metastore](/concepts/built-in-hive-metastore.md) to [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
5. **Grant access** – Grant account-level users, groups, or service principals access to the upgraded tables. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
6. **Update queries and jobs** – Update queries and jobs to reference the new [Unity Catalog](/concepts/unity-catalog.md) tables instead of the old Hive [Metastore](/concepts/metastore.md) tables. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
7. **Migrate files from DBFS** – Migrate files, notebooks, and scripts from DBFS. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
8. **Upgrade compute** – Upgrade active compute resources to supported Databricks Runtime versions. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
9. **Disable legacy features** – Disable access to legacy features in your workspaces. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Before You Begin

Before beginning the upgrade, you should familiarize yourself with basic [Unity Catalog](/concepts/unity-catalog.md) concepts, including [metastores](/concepts/metastore.md) and [managed storage](/concepts/managed-storage-location.md). See [What is [Unity Catalog](/concepts/unity-catalog.md)?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

You must also confirm you meet the following requirements: for most setup steps, you must be a Databricks account admin. Permission requirements for specific tasks are listed in the task-specific documentation. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Provision Identities

[Unity Catalog](/concepts/unity-catalog.md) references account-level identities. Before you attach a [Metastore](/concepts/metastore.md) to your workspace, you must: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

- If you are using SCIM to provision identities from your IdP to your workspace, turn it off and set up provisioning to your Databricks account instead. See [Sync identities from your identity provider](https://docs.databricks.com/aws/en/admin/users-groups/#assign-users-to-account) and [Identities](https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices#identities). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- Update any automation configured to manage users, groups, and service principals (such as SCIM provisioning connectors and Terraform automation) to refer to account endpoints instead of workspace endpoints. See [Account-level and workspace-level SCIM provisioning](https://docs.databricks.com/aws/en/admin/users-groups/scim/#account-workspace-scim). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Attach the Workspace to a [Metastore](/concepts/metastore.md)

If your workspace was in service before it was enabled for [Unity Catalog](/concepts/unity-catalog.md), it has a Hive [Metastore](/concepts/metastore.md) that likely contains data you want to continue using. Databricks recommends upgrading the tables managed by the Hive [Metastore](/concepts/metastore.md) to the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Option 1: Federate, Then Upgrade Foreign Tables

The recommended approach is to first federate your Hive [Metastore](/concepts/metastore.md) or AWS Glue catalog as a foreign catalog, then upgrade the foreign tables in place. This two-step process allows you to migrate tables without data movement while preserving table history, configuration, permissions, and views. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

To upgrade a foreign table to a [Unity Catalog](/concepts/unity-catalog.md) managed table, run the following command: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```sql
ALTER TABLE <foreign_catalog>.<schema>.<table_name> SET MANAGED;
```

Databricks recommends upgrading to a [managed table](/concepts/unity-catalog-managed-tables.md) to unlock [Unity Catalog](/concepts/unity-catalog.md) predictive optimization, which includes automatic maintenance (compaction, clustering, vacuuming) and performance improvements. To upgrade a foreign table to a [Unity Catalog](/concepts/unity-catalog.md) external table instead, run: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```sql
ALTER TABLE <foreign_catalog>.<schema>.<table_name> SET EXTERNAL;
```

After your tables are migrated and you no longer rely on federation to your external catalog, you can remove the connection: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```sql
ALTER CATALOG <foreign_catalog> DROP CONNECTION;
```

### Option 2: Upgrade Tables Directly

If you choose not to use the federation-based upgrade workflow, you can upgrade tables directly using `SYNC` or `CREATE TABLE AS SELECT`. See [Upgrade Hive tables and views to [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Grant Access to Upgraded or Federated Tables

Grant account-level users, groups, or service principals access to the new tables. See [Manage privileges in [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Update Queries and Jobs

While transitioning from the workspace-local Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md), you can continue using queries and jobs that reference the data registered in the Hive [Metastore](/concepts/metastore.md) using [Hive Metastore Federation](/concepts/hive-metastore-federation.md) (recommended) or the syntax described in [Work with the legacy Hive [Metastore](/concepts/metastore.md) alongside [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/hive-metastore). Eventually, you should update all queries and jobs to use [Unity Catalog](/concepts/unity-catalog.md) tables and syntax. Likewise, update queries and jobs that use PATH_BASED target error|path-based access to files to use [Unity Catalog](/concepts/unity-catalog.md) [volumes](/concepts/ucvolumedataset.md) instead. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Disable Access to DBFS

As part of [Unity Catalog](/concepts/unity-catalog.md) migration, Databricks recommends disabling access to DBFS in your workspaces. This ensures all data and workflows are governed by [Unity Catalog](/concepts/unity-catalog.md). You can use the DBFS scanner scripts by Databricks Labs to scan your current DBFS usage and decide for each asset whether to register in place, migrate to [Unity Catalog](/concepts/unity-catalog.md), or archive. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Migrate Files Stored in DBFS

### Step 1: Set Up an [External location](/concepts/external-location.md)

Set up a [Unity Catalog](/concepts/unity-catalog.md) [External location](/concepts/external-location.md) for the cloud storage container or path where the files currently reside. For detailed instructions, see [Connect to cloud object storage using [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 2: Create a Volume

[Unity Catalog](/concepts/unity-catalog.md) volumes provide a governed way to organize files. Create an external volume in a schema that refers to a subpath of your [External location](/concepts/external-location.md). For example: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```sql
USE CATALOG main;
USE SCHEMA data;
CREATE VOLUME IF NOT EXISTS raw_files
LOCATION 'my_data_loc/csv-files/';
```

### Step 3: Copy Files from DBFS Root

If your files were previously stored in DBFS root, copy them to the cloud storage path using `dbutils.fs.cp` or the Databricks CLI for large numbers of files. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 4: Verify Migrated Files

After migrating, list and read files from volumes using standard commands. [Unity Catalog](/concepts/unity-catalog.md) enforces that the principal reading the file has `READ` permission on the volume or [External location](/concepts/external-location.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 5: Clean Up DBFS Mounts

After verifying, unmount old DBFS mount points and consider locking down or deleting data in DBFS root. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Migrate Workspace Assets from DBFS

- **Notebooks**: Import notebooks into the Databricks workspace. Store as workspace objects or in [Git folders](/concepts/databricks-git-folders-for-cicd.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Job scripts**: Move scripts to workspace files, managed in a Git folder for version control. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Build artifacts and libraries**: Store JAR files and Python wheels in [Unity Catalog](/concepts/unity-catalog.md) volumes. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Compute-scoped init scripts**: Store in [Unity Catalog](/concepts/unity-catalog.md) volumes. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Upgrade Compute to Supported Versions

As part of [Unity Catalog](/concepts/unity-catalog.md) migration, Databricks recommends upgrading all compute and jobs to [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) or above and using [Unity Catalog](/concepts/unity-catalog.md) [access modes](/concepts/standard-access-mode.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

To programmatically find compute running versions below 13.3 LTS, query the `system.compute.clusters` table: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```sql
SELECT workspace_id, cluster_id, dbr_version
FROM system.compute.clusters
WHERE TRY_CAST(SPLIT(dbr_version, '\\.')[0] AS INT) < 13
   OR (TRY_CAST(SPLIT(dbr_version, '\\.')[0] AS INT) = 13
       AND TRY_CAST(SPLIT(dbr_version, '\\.')[1] AS INT) < 3);
```

To query for compute running in [no-isolation shared access mode](/concepts/no-isolation-shared-clusters.md), query the same table: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```sql
SELECT workspace_id, cluster_id, dbr_version, data_security_mode
FROM system.compute.clusters
WHERE data_security_mode IN ('NONE','NO_ISOLATION')
LIMIT 100;
```

## Disable Legacy Features

After completing the migration steps, you can disable access to legacy features: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

- **Disable DBFS**: See [Disable access to DBFS root and mounts](https://docs.databricks.com/aws/en/dbfs/disable-dbfs-root-mounts). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Disable the Hive metastore**: See [Disable access to the Hive [Metastore](/concepts/metastore.md)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/disable-hms). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Disable no-isolation shared compute**: See [Enable admin protection for [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md)](https://docs.databricks.com/aws/en/admin/account-settings/no-isolation-shared). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- UCX – A Databricks Labs project providing tools to help with larger-scale migrations. See [Use the UCX utilities to upgrade](https://docs.databricks.com/aws/en/data-governance/unity-catalog/ucx). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) – Enables [Unity Catalog](/concepts/unity-catalog.md) to govern tables registered in a Hive [Metastore](/concepts/metastore.md).
- [External location](/concepts/external-location.md) – Governs cloud storage paths in [Unity Catalog](/concepts/unity-catalog.md).
- Volume – A governed way to organize non-tabular data in [Unity Catalog](/concepts/unity-catalog.md).

## Sources

- upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws-30141815.md)
