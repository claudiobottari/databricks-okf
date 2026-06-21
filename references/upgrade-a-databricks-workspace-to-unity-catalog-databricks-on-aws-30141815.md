---
title: Upgrade a Databricks workspace to Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/
ingestedAt: "2026-06-18T08:04:57.939Z"
---

This page gives an overview of how to upgrade a non-Unity Catalog workspace to Unity Catalog. It also gives instructions for migrating off of the legacy Hive metastore, DBFS, and unsupported Databricks Runtime versions.

## Overview of upgrade steps[​](#overview-of-upgrade-steps "Direct link to Overview of upgrade steps")

To upgrade to Unity Catalog, you must:

1.  Provision identities (users, groups, and service principals) directly to your Databricks account, if you aren't doing so already. Turn off any workspace-level identity provisioning.
2.  Convert any workspace-local groups to account-level groups. Unity Catalog centralizes identity management at the account level.
3.  Attach the workspace to a Unity Catalog metastore. If no metastore exists for your workspace region, an account admin must create one.
4.  Upgrade tables and views managed in Hive metastore to Unity Catalog.
5.  Grant account-level users, groups, or service principals access to the upgraded tables.
6.  Update queries and jobs to reference the new Unity Catalog tables instead of the old Hive metastore tables.
7.  Migrate files, notebooks, and scripts from DBFS.
8.  Upgrade active compute resources to supported Databricks Runtime versions.
9.  Disable access to legacy features in your workspaces. See [Disable access to legacy features in your workspaces](#disable-legacy).

UCX, a Databricks Labs project, provides tools that help you upgrade your non-Unity-Catalog workspace to Unity Catalog. UCX is a good choice for larger-scale migrations. See [Use the UCX utilities to upgrade your workspace to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/ucx).

## Before you begin[​](#before-you-begin "Direct link to before-you-begin")

Before you begin, you should familiarize yourself with the basic Unity Catalog concepts, including metastores and managed storage. See [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

You should also confirm that you meet the following requirements:

*   For most setup steps, you must be a Databricks account admin. For any task that follows for which there are other permission requirements, they are listed in the task-specific documentation.

### Upgrade to Unity Catalog demos[​](#upgrade-to-unity-catalog-demos "Direct link to upgrade-to-unity-catalog-demos")

Watch the following short, guided demos to see key upgrade tasks in action. Each demo covers a specific step and links to detailed documentation where applicable.

*   [Convert workspace-local groups to account-level groups](https://app.getreprise.com/launch/myM3VNn/)
*   Upgrade tables in your Hive metastore to Unity Catalog tables
    *   [Upgrade foreign tables to managed tables using `SET MANAGED`](https://www.youtube.com/watch?v=0suBlnwHLUY)
    *   [Upgrade external tables using `SYNC`](https://app.getreprise.com/launch/m6ErK0n/).
    *   [Upgrade managed tables using `SYNC`](https://app.getreprise.com/launch/MXxjgN6/).
    *   [Upgrade managed tables using `CREATE TABLE AS SELECT`](https://app.getreprise.com/launch/dyRBKBy/)
*   Update compute for Unity Catalog
    *   [All-purpose compute](https://app.getreprise.com/launch/MXxj186/)
    *   [SQL warehouses](https://app.getreprise.com/launch/V6WabBX/)
*   [Update queries and jobs to work with your upgraded tables](https://app.getreprise.com/launch/m6ErgVn/)

Alternatively, you can follow the demo [Use UCX to upgrade to Unity Catalog](https://app.getreprise.com/launch/96m2d3n/).

## Provision users, groups, and service principals to your account[​](#provision-users-groups-and-service-principals-to-your-account "Direct link to Provision users, groups, and service principals to your account")

Unity Catalog references account-level identities. Before you attach a metastore to your workspace, you should do the following:

*   If you are using SCIM to provision users, groups, and service principals from your IdP to your workspace, turn it off and set up provisioning to your Databricks account instead. See [Sync identities from your identity provider](https://docs.databricks.com/aws/en/admin/users-groups/#assign-users-to-account) and [Identities](https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices#identities).
    
*   Update any automation that has been configured to manage users, groups, and service principals, such as SCIM provisioning connectors and Terraform automation, so that they refer to account endpoints instead of workspace endpoints. See [Account-level and workspace-level SCIM provisioning](https://docs.databricks.com/aws/en/admin/users-groups/scim/#account-workspace-scim).
    

## Convert workspace-local groups to account-level groups[​](#convert-workspace-local-groups-to-account-level-groups "Direct link to Convert workspace-local groups to account-level groups")

See [Migrate workspace-local groups to account groups](https://docs.databricks.com/aws/en/admin/users-groups/workspace-local-groups#migrate).

If your workspace is not enabled for Unity Catalog (attached to a metastore), the next step depends on whether or not you already have a Unity Catalog metastore defined for your workspace region:

*   If your account already has a Unity Catalog metastore defined for your workspace region, you can simply attach your workspace to the existing metastore. Go to [Enable a workspace for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces).
*   If there is no Unity Catalog metastore defined for your workspace's region, you must create a metastore and then attach the workspace. Go to Go to [Create a Unity Catalog metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/create-metastore).

If your workspace was in service before it was enabled for Unity Catalog, it has a Hive metastore that likely contains data that you want to continue to use. Databricks recommends that you upgrade the tables managed by the Hive metastore to the Unity Catalog metastore.

### Option 1: Federate, then upgrade foreign tables[​](#option-1-federate-then-upgrade-foreign-tables "Direct link to Option 1: Federate, then upgrade foreign tables")

The recommended approach is to first federate your Hive metastore or AWS Glue catalog as a foreign catalog, then upgrade the foreign tables in place. This two-step process allows you to migrate tables without data movement while preserving table history, configuration, permissions, and views.

First, federate your Hive metastore or AWS Glue catalog as a foreign catalog in Unity Catalog. This allows you to access your existing tables through Unity Catalog, and prepares them for upgrading.

For instructions on federating your Hive metastore, see [Hive metastore federation: enable Unity Catalog to govern tables registered in a Hive metastore](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts).

note

If you choose not to upgrade your tables and want to continue working with the federated catalog permanently, you can do so. However, Databricks recommends completing the upgrade to take full advantage of Unity Catalog features.

After federating your Hive metastore or AWS Glue catalog, you can upgrade the foreign tables to Unity Catalog tables without any data movement. This workflow upgrades tables in place, preserving table history, configuration, permissions, and views.

To upgrade a foreign table to a Unity Catalog managed table, run the following command:

SQL

    ALTER TABLE <foreign_catalog>.<schema>.<table_name> SET MANAGED;

Databricks recommends upgrading to a managed table to unlock Unity Catalog predictive optimization, which includes automatic maintenance (compaction, clustering, vacuuming) and performance improvements. To upgrade a foreign table to a Unity Catalog external table instead, run the following command:

SQL

    ALTER TABLE <foreign_catalog>.<schema>.<table_name> SET EXTERNAL;

After your tables are migrated and you no longer rely on federation to your external catalog, you can remove the connection:

SQL

    ALTER CATALOG <foreign_catalog> DROP CONNECTION;

For more details on this workflow, see [Convert a foreign table to a managed Unity Catalog table](https://docs.databricks.com/aws/en/tables/convert-foreign-managed).

### Option 2: Upgrade tables directly[​](#option-2-upgrade-tables-directly "Direct link to Option 2: Upgrade tables directly")

If you choose not to use the federation-based upgrade workflow, you can upgrade tables directly using `SYNC` or `CREATE TABLE AS SELECT`. See [Upgrade Hive tables and views to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate).

## Grant access to upgraded or federated tables[​](#-grant-access-to-upgraded-or-federated-tables "Direct link to -grant-access-to-upgraded-or-federated-tables")

Grant account-level users, groups, or service principals access to the new tables. See [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).

## Update queries and jobs to work with your upgraded tables and paths to data[​](#-update-queries-and-jobs-to-work-with-your-upgraded-tables-and-paths-to-data "Direct link to -update-queries-and-jobs-to-work-with-your-upgraded-tables-and-paths-to-data")

While you are transitioning from the workspace-local Hive metastore to Unity Catalog, you can continue to use queries and jobs that reference the data registered in the Hive metastore, using [Hive metastore federation](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts) (recommended) or the syntax described in [Work with the legacy Hive metastore alongside Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/hive-metastore). However, eventually you should update all queries and jobs to use Unity Catalog tables and syntax.

Likewise, update queries and jobs that use path-based access to files to use Unity Catalog [volumes](https://docs.databricks.com/aws/en/volumes/) instead.

For detailed recommendations, see [Update jobs when you upgrade legacy workspaces to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/jobs-update).

## Disable access to DBFS[​](#disable-access-to-dbfs "Direct link to Disable access to DBFS")

As part of Unity Catalog migration, Databricks recommends disabling access to DBFS in your workspaces. This ensures that all data and workflows are governed by Unity Catalog, and that you take full advantage of Unity Catalog features.

You can use the [DBFS scanner scripts](https://github.com/databrickslabs/sandbox/tree/main/dbfs-scanner) by Databricks Labs to scan your current DBFS usage and decide for each whether to register the asset in place (using an external location), migrate to Unity Catalog, or archive if you no longer need it. Databricks Labs is a public GitHub repo that isn't supported directly by Databricks.

The following sections describe how to migrate different assets from DBFS to Unity Catalog.

## Migrate files stored in DBFS[​](#migrate-files-stored-in-dbfs "Direct link to migrate-files-stored-in-dbfs")

If you have raw files such as Parquet, CSV, JSON, or images stored in DBFS root (for example, under `/FileStore` or other DBFS root directories) or in cloud storage mounted to DBFS (under `/mnt/...`), migrate them using Unity Catalog [volumes](https://docs.databricks.com/aws/en/volumes/), and access them using [external locations](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#cloud-storage-governance).

The following steps describe how to migrate files from DBFS to Unity Catalog volumes. For more information about when to use volumes versus workspace files, see [Recommendations for files in volumes and workspace files](https://docs.databricks.com/aws/en/files/files-recommendations).

### Step 1: Set up an external location[​](#step-1-set-up-an-external-location "Direct link to Step 1: Set up an external location")

To register the assets in Unity Catalog, set up a Unity Catalog external location for the cloud storage container or path where the files currently reside. You can do this using Catalog Explorer, SQL commands, Terraform, or the Databricks CLI.

For detailed instructions, see [Connect to cloud object storage using Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/).

### Step 2: Create a volume[​](#step-2-create-a-volume "Direct link to Step 2: Create a volume")

Unity Catalog volumes provide a governed way to organize files. Databricks recommends using volumes to govern all non-tabular data. You can create an external volume in a schema that refers to a subpath of your external location. For example:

SQL

    USE CATALOG main;USE SCHEMA data;CREATE VOLUME IF NOT EXISTS raw_filesLOCATION 'my_data_loc/csv-files/';

All files under that path are now accessible through the external location and governed by Unity Catalog permissions.

For more information, see [What are Unity Catalog volumes?](https://docs.databricks.com/aws/en/volumes/).

### Step 3: Copy files from DBFS root[​](#step-3-copy-files-from-dbfs-root "Direct link to Step 3: Copy files from DBFS root")

If your files were previously stored in DBFS root, copy them to the cloud storage path. For example, in a notebook:

Python

    dbutils.fs.cp(  "dbfs:/FileStore/tables/data.csv",  "/Volumes/main/data/raw_files/data.csv")

tip

If you have a large number of files or files larger than a few GB, consider using the Databricks CLI or a distributed copy using Apache Spark to parallelize the move. The [Databricks CLI `fs cp` command](https://docs.databricks.com/aws/en/dev-tools/cli/reference/fs-commands) can recursively copy directories.

### Step 4: Verify migrated files[​](#step-4-verify-migrated-files "Direct link to Step 4: Verify migrated files")

After migrating, list and read files from volumes using standard commands:

Python

    # List files in the volumedbutils.fs.ls("/Volumes/main/data/raw_files/")# Read a CSV file into a DataFramedf = spark.read.option("header", True).csv(  "/Volumes/main/data/raw_files/2024-01-01-data.csv")

This code requires appropriate Unity Catalog permissions on the volume or external location and a compute resource that supports Unity Catalog. Unity Catalog enforces that the principal reading the file has `READ` permission on the volume or external location.

### Step 5: Clean up DBFS mounts[​](#step-5-clean-up-dbfs-mounts "Direct link to Step 5: Clean up DBFS mounts")

After verifying that the files in the new location are accessible, unmount old DBFS mount points to prevent confusion or accidental use:

Python

    dbutils.fs.unmount("/mnt/oldpath")

Consider locking down or deleting data in DBFS root if it has been moved, because leaving copies can lead to inconsistent updates or security risks.

## Migrate workspace assets from DBFS[​](#migrate-workspace-assets-from-dbfs "Direct link to migrate-workspace-assets-from-dbfs")

Some workspaces have notebooks, code files, or reference scripts stored on DBFS. These might include:

*   Notebooks saved as HTML or DBC files in `/FileStore` for sharing
*   Python scripts or JAR files used in Databricks jobs
*   Compute-scoped init scripts (for example, `dbfs:/databricks/init/...`)

Notebooks and code should be stored as [workspace files](https://docs.databricks.com/aws/en/files/files-recommendations) or in [Git folders](https://docs.databricks.com/aws/en/repos/git-folders-concepts), not on DBFS. DBFS does not provide access control per file and should not be used for source code or notebooks.

*   **Notebooks**: If you have notebooks as files on DBFS, import them into the Databricks workspace. You can do this manually using the UI's import function or using the CLI. Ensure that [notebook permissions](https://docs.databricks.com/aws/en/notebooks/notebooks-collaborate#notebook-permissions) in the workspace are set appropriately for team access. Going forward, store notebooks as workspace objects or in Git folders, and use Git for version control.
*   **Job scripts**: If jobs are configured to run a Python script from DBFS (for example, a job with a task type "Python script" referencing `dbfs:/mnt/scripts/my_etl.py`), move those scripts to [workspace files](https://docs.databricks.com/aws/en/files/files-recommendations). Manage them in a Git folder for version control and change tracking.
*   **Build artifacts and libraries**: Assets like JAR files and Python wheels should be stored in Unity Catalog [volumes](https://docs.databricks.com/aws/en/volumes/).
*   **Compute-scoped init scripts**: Compute-scoped init scripts should be stored in Unity Catalog [volumes](https://docs.databricks.com/aws/en/volumes/). See [What are init scripts?](https://docs.databricks.com/aws/en/init-scripts/).

## Locate and migrate compute to supported Databricks Runtime versions and access modes[​](#locate-and-migrate-compute-to-supported-databricks-runtime-versions-and-access-modes "Direct link to locate-and-migrate-compute-to-supported-databricks-runtime-versions-and-access-modes")

note

This section includes queries that access the `system.compute.clusters` table. To access this system table, you must be a Databricks account admin or have been granted `USE` and `SELECT` permissions on the `compute` system schema. See [Grant access to system tables](https://docs.databricks.com/aws/en/admin/system-tables/#grant-access).

As part of Unity Catalog migration, Databricks recommends upgrading all compute and jobs to Databricks Runtime 13.3 LTS or above and to use Unity Catalog access modes.

To manually review the compute in your workspace, navigate to the workspace's **Compute** page. In the **All-purpose compute** section, review each compute's Databricks Runtime version. Sort or filter by version to identify clusters running versions below 13.3 LTS. Repeat for the **Job compute** section, because jobs can also be configured to use a particular Databricks Runtime version.

To programmatically find compute running versions below 13.3 LTS, query the `system.compute.clusters` table. For example:

SQL

    SELECT  workspace_id,  cluster_id,  dbr_versionFROM system.compute.clustersWHERE  TRY_CAST(SPLIT(dbr_version, '\\.')[0] AS INT) < 13  OR (    TRY_CAST(SPLIT(dbr_version, '\\.')[0] AS INT) = 13    AND TRY_CAST(SPLIT(dbr_version, '\\.')[1] AS INT) < 3  );

This will return a list of all-purpose compute and job compute resources running versions below 13.3 LTS.

### Upgrade compute to supported access modes[​](#upgrade-compute-to-supported-access-modes "Direct link to upgrade-compute-to-supported-access-modes")

If you still have compute running in no-isolation shared access mode, you can upgrade it to supported access modes. See [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-mode). To query for compute running in no-isolation shared access mode, query the `system.compute.clusters` table. For example:

SQL

    SELECT  workspace_id,  cluster_id,  dbr_version,  data_security_modeFROM system.compute.clustersWHERE data_security_mode IN ('NONE','NO_ISOLATION')LIMIT 100;

## Disable access to legacy features in your workspaces[​](#disable-access-to-legacy-features-in-your-workspaces "Direct link to disable-access-to-legacy-features-in-your-workspaces")

After you have completed the migration steps above, you can disable access to legacy features in your workspaces.

*   **Disable DBFS root and mounts**: Once you have migrated all data and workflows that rely on DBFS root or mounts, and upgraded all jobs and clusters to Databricks Runtime 13.3 LTS or above, workspace admins can disable DBFS in existing workspaces. See [Disable access to DBFS root and mounts in your existing Databricks workspace](https://docs.databricks.com/aws/en/dbfs/disable-dbfs-root-mounts).
*   **Disable the Hive metastore**: When you have completed your Unity Catalog migration or federated your Hive metastore as a foreign catalog governed by Unity Catalog, workspace admins can prevent users from bypassing Unity Catalog and accessing tables registered in the Hive metastore. See [Disable access to the Hive metastore used by your Databricks workspace](https://docs.databricks.com/aws/en/data-governance/unity-catalog/disable-hms).
*   **Disable no-isolation shared compute resources**: To prevent userse from creating any new no-isolation shared compute resources, workspace admins can disable no-isolation shared compute resources in their workspaces. See [Enable admin protection for no isolation shared clusters in your account](https://docs.databricks.com/aws/en/admin/account-settings/no-isolation-shared).
