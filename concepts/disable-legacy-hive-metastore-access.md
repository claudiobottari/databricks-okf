---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3db575bd573b8b4efde096fdfb1685bf60a5e8e3d428742f83f40ca1e73d286f
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disable-legacy-hive-metastore-access
    - DLHMA
    - Disable Hive Metastore Access
    - Disable Access to the Hive Metastore
    - Disable Legacy Access
    - Disable legacy access
    - Legacy Hive Metastore
    - disable-legacy-hive-metastore-access-workspace-setting
    - DLHMA(S
    - Disable Legacy Access (Workspace Setting)
    - Disable Legacy Access Workspace Setting
    - disabling-legacy-hive-metastore-access-in-databricks
    - DLHMAID
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Disable Legacy Hive Metastore Access
description: Workspace admin setting to prevent users from bypassing Unity Catalog and directly accessing the legacy Hive metastore in Databricks.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - data-governance
timestamp: "2026-06-19T18:31:58.034Z"
---

# Disable Legacy Hive [Metastore](/concepts/metastore.md) Access

**Disable Legacy Hive [Metastore](/concepts/metastore.md) Access** is a workspace admin setting in Databricks that prevents users and compute clusters from directly accessing tables registered in the legacy Hive [Metastore](/concepts/metastore.md) — whether the workspace-local Hive [Metastore](/concepts/metastore.md), an external Hive [Metastore](/concepts/metastore.md), or AWS Glue. This setting is a critical step in completing a migration to [Unity Catalog](/concepts/unity-catalog.md) and ensuring that all data access is governed by Unity Catalog's data governance controls. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Overview

Data in the Hive [Metastore](/concepts/metastore.md) is not governed by Unity Catalog. Disabling direct Hive [Metastore](/concepts/metastore.md) access ensures that users cannot bypass Unity Catalog and access tables registered in the Hive [Metastore](/concepts/metastore.md). You can disable direct access and continue to query tables managed by your Hive [Metastore](/concepts/metastore.md) by taking advantage of [Hive Metastore Federation](/concepts/hive-metastore-federation.md), which allows Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md). Federation can be set up either before or after disabling direct workspace access. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

Even after migrating to Unity Catalog, Databricks compute clusters connect to the Hive [Metastore](/concepts/metastore.md) by default unless you explicitly disable Hive [Metastore](/concepts/metastore.md) access. To prevent Hive [Metastore](/concepts/metastore.md) maintenance from affecting your Unity Catalog workloads, you can disable direct access for all clusters and workloads at once, or use a Spark configuration to disable access on a cluster-by-cluster basis. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

To disable access to the Hive [Metastore](/concepts/metastore.md) at the account level for new workspaces, use the [Disable legacy features](/concepts/disable-legacy-features-setting.md) account setting. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites

Before disabling the legacy Hive [Metastore](/concepts/metastore.md), you should meet the following criteria: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- You have completed migrating all tables registered in the legacy [Metastore](/concepts/metastore.md) to Unity Catalog, or you have always used Unity Catalog and never the legacy Hive [Metastore](/concepts/metastore.md).
- You want to force your users to stop using tables registered in the legacy [Metastore](/concepts/metastore.md).
- You have upgraded all jobs to Databricks Runtime 13.3 LTS or above.

## Effects of Disabling Legacy Access

After you disable the legacy [Metastore](/concepts/metastore.md): ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- Any jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) will fail.
- [Hive metastore federation fallback](/concepts/hive-metastore-fallback.md) is disabled.
- Jobs that run on Databricks Runtime versions below 13.3 will fail. Currently running jobs will continue to work until they are terminated, but restarts on those clusters will fail.
- The **Legacy** heading and `hive_metastore` catalog disappear from the Catalog Explorer browser pane.
- SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail.

### Important Caveats

Disabling legacy access does not prevent users from using cluster-level credentials, such as instance profiles or service principals, that are available on a cluster. Databricks recommends that you remove such credentials from your clusters. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

_No Isolation shared_ clusters do not respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting. To prevent users from creating and using such clusters, enable the **Enforce User Isolation** setting for the workspace. See Enforce user isolation cluster types on a workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Disabling Legacy Access for the Entire Workspace

Disable your workspace's legacy Hive [Metastore](/concepts/metastore.md) using the **Disable legacy access** workspace admin setting: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

1. As a workspace admin, log in to your Databricks workspace.
2. Click the user profile menu at the top right and select **Settings** from the menu.
3. Go to **Workspace admin > Security**.
4. Set **Disable legacy access** to **Disabled: legacy access features cannot be used**.
5. To ensure that the new setting has taken effect, wait approximately five minutes.
6. Restart all running clusters.

## Disabling Access for Individual Compute Clusters

You can also disable direct access to the Hive [Metastore](/concepts/metastore.md) gradually, on a cluster-by-cluster basis. This approach can be useful during a Unity Catalog migration when you want to reduce reliance on Hive [Metastore](/concepts/metastore.md) incrementally until you can disable it for the entire workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

To disable direct access, set the following Spark configurations on the cluster: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

```
spark.databricks.unityCatalogOnlyMode true
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). When you enable Unity Catalog-only mode, you must also set an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that replaces the legacy Hive [Metastore](/concepts/metastore.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Enables Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md)
- Migrate Hive tables and views to Unity Catalog — The process of moving tables from Hive [Metastore](/concepts/metastore.md) to Unity Catalog
- Default catalog — The catalog used when no catalog is specified in a query
- Enforce user isolation cluster types — Prevents creation of No Isolation shared clusters that bypass legacy access settings
- [Disable legacy features](/concepts/disable-legacy-features-setting.md) — Account-level setting to disable legacy features for new workspaces

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
