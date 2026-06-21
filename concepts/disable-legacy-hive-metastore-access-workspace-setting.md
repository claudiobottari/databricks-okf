---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e7f194375f221b2d158a295a4f30088c6ee4cbb542488d695b08b047304d59b
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disable-legacy-hive-metastore-access-workspace-setting
    - DLHMA(S
    - Disable Legacy Access (Workspace Setting)
    - Disable Legacy Access Workspace Setting
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Disable Legacy Hive Metastore Access (Workspace Setting)
description: A workspace admin setting that prevents users from bypassing Unity Catalog and directly accessing tables registered in the legacy Hive metastore.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - data-governance
timestamp: "2026-06-18T15:27:57.493Z"
---

# Disable Legacy Hive [Metastore](/concepts/metastore.md) Access (Workspace Setting)

**Disable Legacy Hive [Metastore](/concepts/metastore.md) Access** is a workspace admin setting in Databricks that prevents users and jobs from directly accessing tables registered in the legacy Hive [Metastore](/concepts/metastore.md), including the workspace-local Hive [Metastore](/concepts/metastore.md), an external Hive [Metastore](/concepts/metastore.md), or AWS Glue. This setting is a key step in enforcing Unity Catalog governance after migration. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Purpose

Data stored in the legacy Hive [Metastore](/concepts/metastore.md) is not governed by [Unity Catalog](/concepts/unity-catalog.md). By disabling direct access, workspace admins ensure that users cannot bypass Unity Catalog's data governance controls. Even after migrating tables to Unity Catalog, Databricks compute clusters continue to connect to the Hive [Metastore](/concepts/metastore.md) by default unless access is explicitly disabled. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites

Before disabling the legacy Hive [Metastore](/concepts/metastore.md) access, you should meet the following criteria: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- You have completed migrating all tables registered in the legacy [Metastore](/concepts/metastore.md) to Unity Catalog, or you have always used Unity Catalog and never used the legacy Hive [Metastore](/concepts/metastore.md).
- You want to force users to stop using tables registered in the legacy [Metastore](/concepts/metastore.md).
- You have upgraded all jobs to Databricks Runtime 13.3 LTS or above.

## Effects of Disabling Legacy Access

After you disable the legacy [Metastore](/concepts/metastore.md): ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- Any jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) will fail.
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) fallback is disabled.
- Jobs that run on Databricks Runtime versions below 13.3 will fail. Currently running jobs will continue to work until terminated, but restarts on those clusters will fail.
- The **Legacy** heading and `hive_metastore` catalog disappear from the [Catalog Explorer](/concepts/catalog-explorer.md) browser pane.
- SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail.

## Limitations and Considerations

- Disabling legacy access does **not** prevent users from using cluster-level credentials (such as instance profiles or service principals) that are available on a cluster. Databricks recommends removing such credentials from your clusters. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) do **not** respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting. To prevent users from creating and using such clusters, enable the **Enforce User Isolation** setting for the workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## How to Disable Legacy Access (Workspace-Wide)

1. As a workspace admin, log in to your Databricks workspace.
2. Click the user profile menu at the top right and select **Settings**.
3. Go to **Workspace admin > Security**.
4. Set **Disable legacy access** to **Disabled: legacy access features cannot be used**.
5. Wait approximately five minutes to ensure the setting has taken effect.
6. Restart all running clusters.

^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Disable Access for Individual Compute Clusters

You can also disable direct access to the Hive [Metastore](/concepts/metastore.md) gradually, on a cluster-by-cluster basis. This is useful during a Unity Catalog migration when you want to reduce reliance on the Hive [Metastore](/concepts/metastore.md) incrementally. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

Set the following Spark configurations on the cluster:

```
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). When you enable Unity Catalog-only mode, you must also set an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Alternative: Account-Level Setting

To disable access to the Hive [Metastore](/concepts/metastore.md) at the account level for new workspaces, use the [Disable legacy features](/concepts/disable-legacy-features-setting.md) account setting. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Relationship to [Hive Metastore Federation](/concepts/hive-metastore-federation.md)

You can disable direct access and continue to query tables managed by your Hive [Metastore](/concepts/metastore.md) by taking advantage of [Hive Metastore Federation](/concepts/hive-metastore-federation.md). Federation allows Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md). You can federate Hive [Metastore](/concepts/metastore.md) tables either before or after disabling direct workspace access. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Hive Metastore](/concepts/built-in-hive-metastore.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Disable legacy features](/concepts/disable-legacy-features-setting.md) (account-level setting)
- Upgrade Hive tables and views to Unity Catalog
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md)
- Enforce user isolation

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
