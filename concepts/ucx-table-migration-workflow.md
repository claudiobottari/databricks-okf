---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16974e90fbbcbee4564176190cae3f53786594bb9eae3ffc4dbcf460cc92b89f
  pageDirectory: concepts
  sources:
    - use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ucx-table-migration-workflow
    - UTMW
    - Table Migration Workflow
    - Table Migration Workflow|table migration
    - Table migration
    - Table migration commands
  citations:
    - file: use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
title: UCX Table Migration Workflow
description: A UCX workflow that upgrades tables from the Hive metastore to the Unity Catalog metastore, using SYNC for external tables and DEEP CLONE for managed tables.
tags:
  - databricks
  - unity-catalog
  - migration
  - tables
timestamp: "2026-06-19T23:22:47.193Z"
---

# UCX Table Migration Workflow

The **UCX Table Migration Workflow** is a component of the [UCX|UCX (Unity Catalog Migration Toolkit)](/concepts/ucx-unity-catalog-migration-toolkit.md) that upgrades tables from the workspace’s Hive [Metastore](/concepts/metastore.md) to a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). It is the third major workflow in the UCX migration process, following the [UCX Assessment Workflow](/concepts/ucx-assessment-workflow.md) and the [UCX Group Migration Workflow](/concepts/ucx-group-migration-workflow.md). ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## How tables are upgraded

The workflow handles two types of tables differently:

- **External tables** in the Hive [Metastore](/concepts/metastore.md) are upgraded as [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) using the SYNC command. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]
- **Managed tables** stored in workspace storage (DBFS root) are upgraded as [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md) using [Deep Clone](/concepts/deep-clone.md). ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

### Format requirements

Hive managed tables must be in Delta or Parquet format to be eligible for upgrade. External Hive tables must be in one of the data formats listed in Work with external tables. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Preparatory commands

Before running the actual migration, you must execute several CLI commands to prepare the workspace. These are run using the `databricks labs ucx` CLI:

- **`create-table-mapping`** — Generates a CSV file that maps each Hive table to a target [Unity Catalog](/concepts/unity-catalog.md) catalog, schema, and table name. You should review and edit this mapping before proceeding. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]
- **`create-uber-principal`** — Creates a service principal with read-only access to all storage used by the tables. This principal is used by the migration job’s compute resource to perform the upgrade. You should deprovision this principal after the migration is complete. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]
- **`principal-prefix-access`** (optional) — Identifies the storage accounts and storage access credentials used by the Hive tables. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]
- **`migrate-credentials`** (optional) — Creates [Unity Catalog](/concepts/unity-catalog.md) storage credentials from the access credentials identified by `principal-prefix-access`. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]
- **`migrate-locations`** (optional) — Creates [Unity Catalog](/concepts/unity-catalog.md) external locations from the storage locations identified by the assessment workflow, using the credentials created by `migrate-credentials`. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]
- **`create-catalogs-schemas`** (optional) — Creates the [Unity Catalog](/concepts/unity-catalog.md) catalogs and schemas that will hold the upgraded tables. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

For the full set of table migration commands and options, see the [Table migration commands](/concepts/ucx-table-migration-workflow.md) reference in the UCX documentation. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Running the table migration

Once the preparatory tasks are complete, you can execute the table migration workflow from the UCX‑generated README notebook or from **Jobs & Pipelines** in the Databricks workspace UI. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

The output of each workflow task is stored in Delta tables inside the `$inventory_database` schema that you specified during UCX installation. You can query these tables to verify progress and troubleshoot issues. It is normal to run the table migration workflow multiple times until all tables are upgraded successfully. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Related UCX utilities

UCX also provides utilities for [Hive Metastore Federation](/concepts/hive-metastore-federation.md), which can help ease the transition by enabling you to run workloads on both the legacy Hive [Metastore](/concepts/metastore.md) and its [Unity Catalog](/concepts/unity-catalog.md) mirror:

- `enable-hms-federation`
- `create-federated-catalog`

These are not part of the table migration workflow itself but are complementary tools for migration scenarios. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Sources

- use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md](/references/use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws-0023b143.md)
