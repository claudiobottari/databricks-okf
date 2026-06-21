---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4a185cd562defd69f93934a817a9d46bb0242dd5f297fc719d709a389517e57
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - effects-of-disabling-legacy-hive-metastore
    - EODLHM
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Effects of Disabling Legacy Hive Metastore
description: The observable changes in a Databricks workspace after disabling legacy Hive metastore access, including job failures, UI changes, and SQL command impacts.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - workspace-admin
timestamp: "2026-06-18T15:28:37.687Z"
---

# Effects of Disabling Legacy Hive [Metastore](/concepts/metastore.md)

**Disabling the legacy Hive metastore** is a workspace admin setting that prevents users and workloads from directly accessing tables registered in the Hive [Metastore](/concepts/metastore.md) — whether the workspace-local Hive [Metastore](/concepts/metastore.md) or an external Hive [Metastore](/concepts/metastore.md), including AWS Glue. This setting is a critical step in completing a migration to [Unity Catalog](/concepts/unity-catalog.md) and ensuring full data governance. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Overview

Data in the Hive [Metastore](/concepts/metastore.md) is not governed by Unity Catalog. Disabling direct Hive [Metastore](/concepts/metastore.md) access is an important step in the process of migrating to Unity Catalog and ensuring that you take full advantage of Unity Catalog data governance. You can disable direct access and continue to query tables managed by your Hive [Metastore](/concepts/metastore.md) by taking advantage of [Hive Metastore Federation](/concepts/hive-metastore-federation.md). You can federate Hive [Metastore](/concepts/metastore.md) tables either before or after you disable direct workspace access to the Hive [Metastore](/concepts/metastore.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites

Before you disable the legacy Hive [Metastore](/concepts/metastore.md), you should meet the following criteria: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- You're done migrating all tables registered in the legacy [Metastore](/concepts/metastore.md) to Unity Catalog, or you have always used Unity Catalog and never the legacy Hive [Metastore](/concepts/metastore.md).
- You want to force your users to stop using tables registered in the legacy [Metastore](/concepts/metastore.md).
- You have upgraded all jobs to Databricks Runtime 13.3 LTS or above.
- You are prepared for any jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) to fail after disablement.

## Immediate Effects

When you disable the legacy Hive [Metastore](/concepts/metastore.md) through the **Disable legacy access** workspace admin setting, the following effects occur: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

| Effect | Description |
|--------|-------------|
| Job failures | Any jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) will fail. |
| Fallback disabled | Fallback — the mechanism that allows queries to access the Hive [Metastore](/concepts/metastore.md) when a table is not found in Unity Catalog — is disabled. |
| Runtime version restriction | Jobs that run on Databricks Runtime versions below 13.3 will fail. Currently running jobs will continue to work until they are terminated, but restarts on those clusters will fail. |
| Catalog Explorer changes | The **Legacy** heading and `hive_metastore` catalog disappear from the Catalog Explorer browser pane. |
| SQL command failures | SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail. |

### Important Note

Even after migrating to Unity Catalog, Databricks compute clusters connect to the Hive [Metastore](/concepts/metastore.md) by default unless you explicitly disable Hive [Metastore](/concepts/metastore.md) access. To prevent Hive [Metastore](/concepts/metastore.md) maintenance from affecting your Unity Catalog workloads, you can disable direct access to Hive [Metastore](/concepts/metastore.md) for all clusters and workloads at once. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Disablement Methods

### Workspace-Level Disablement

Disable your workspace's legacy Hive [Metastore](/concepts/metastore.md) using the **Disable legacy access** workspace admin setting: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

1. As a workspace admin, log in to your Databricks workspace.
2. Click the user profile menu at the top right and select **Settings** from the menu.
3. Go to **Workspace admin > Security**.
4. Set **Disable legacy access** to **Disabled: legacy access features cannot be used**.
5. To ensure that the new setting has taken effect, wait approximately five minutes.
6. Restart all running clusters.

### Account-Level Default

To disable access to the Hive [Metastore](/concepts/metastore.md) at the account level for new workspaces, use the [Disable legacy features account setting](/concepts/disable-legacy-features-setting.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

### Cluster-by-Cluster Disablement

You can also disable direct access to the Hive [Metastore](/concepts/metastore.md) gradually, on a cluster-by-cluster basis. This approach can be useful during a Unity Catalog migration when you want to reduce reliance on Hive [Metastore](/concepts/metastore.md) incrementally until you can disable it for the entire workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

To disable direct access, set the following Spark configurations on the cluster: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

```
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). When you enable Unity Catalog-only mode, you must also set an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Security Considerations

Disabling legacy access does not prevent users from using cluster-level credentials, such as instance profiles or service principals, that are available on a cluster. Databricks recommends that you remove such credentials from your clusters. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

_No Isolation shared_ clusters do not respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting. To prevent users from creating and using such clusters, enable the **Enforce User Isolation** setting for the workspace. See Enforce user isolation cluster types on a workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that replaces the legacy Hive [Metastore](/concepts/metastore.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — The ability to govern tables registered in a Hive [Metastore](/concepts/metastore.md) through Unity Catalog
- Fallback — The mechanism that allows queries to access the Hive [Metastore](/concepts/metastore.md) when a table is not found in Unity Catalog
- [Legacy features account setting](/concepts/account-level-legacy-feature-settings.md) — The account-level setting for disabling legacy features in new workspaces
- Spark configurations — Cluster-level settings that control legacy Hive [Metastore](/concepts/metastore.md) access
- Enforce user isolation — A workspace setting that prevents _No Isolation shared_ clusters from bypassing Hive [Metastore](/concepts/metastore.md) disablement
- Upgrade Hive tables and views to Unity Catalog — The migration process for moving tables from Hive [Metastore](/concepts/metastore.md) to Unity Catalog

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
