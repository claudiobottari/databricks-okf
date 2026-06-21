---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a511067f90a080c2c7d7f93a92d04a0004226cd4b3212678cfc511926b614700
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disabling-legacy-hive-metastore-access-in-databricks
    - DLHMAID
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Disabling Legacy Hive Metastore Access in Databricks
description: A workspace admin setting that prevents users from bypassing Unity Catalog and accessing tables registered in the Hive metastore
tags:
  - databricks
  - unity-catalog
  - hive-metastore
timestamp: "2026-06-19T15:11:44.298Z"
---

# Disabling Legacy Hive [Metastore](/concepts/metastore.md) Access in Databricks

**Disabling Legacy Hive [Metastore](/concepts/metastore.md) Access in Databricks** refers to the process of preventing users and compute clusters from directly accessing tables registered in a [Hive Metastore](/concepts/built-in-hive-metastore.md) (either workspace-local, external, or AWS Glue) once those tables have been migrated to or federated under [Unity Catalog](/concepts/unity-catalog.md). This is a key governance step that ensures all data access is governed by Unity Catalog, eliminating the bypass path through the legacy [Metastore](/concepts/metastore.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Overview

Data in the Hive [Metastore](/concepts/metastore.md) is not governed by Unity Catalog. Disabling direct Hive [Metastore](/concepts/metastore.md) access is an important part of migrating to Unity Catalog and taking full advantage of its data governance capabilities. You can disable direct access while still querying Hive [Metastore](/concepts/metastore.md) tables by using [Hive Metastore Federation](/concepts/hive-metastore-federation.md), which allows Unity Catalog to govern those tables as a foreign catalog. Federation can be enabled either before or after disabling direct workspace access. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

Even after migrating to Unity Catalog, Databricks compute clusters connect to the Hive [Metastore](/concepts/metastore.md) by default unless you explicitly disable access. To prevent Hive [Metastore](/concepts/metastore.md) maintenance from affecting Unity Catalog workloads, you can disable access for all clusters at once or on a cluster-by-cluster basis. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites

Before disabling the legacy Hive [Metastore](/concepts/metastore.md), you should meet the following criteria:

- You have migrated all tables registered in the legacy [Metastore](/concepts/metastore.md) to Unity Catalog, or you have always used Unity Catalog and never the legacy Hive [Metastore](/concepts/metastore.md).
- You want to force users to stop using tables registered in the legacy [Metastore](/concepts/metastore.md).
- You have upgraded all jobs to Databricks Runtime 13.3 LTS or above.

^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Effects of Disabling

After you disable the legacy Hive [Metastore](/concepts/metastore.md):

- Any jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) will fail.
- Fallback (the ability to automatically route queries to the Hive [Metastore](/concepts/metastore.md) when a table is not found in Unity Catalog) is disabled.
- Jobs running on Databricks Runtime versions below 13.3 will fail. Currently running jobs continue until termination, but restarts on those clusters will fail.
- The **Legacy** heading and the `hive_metastore` catalog disappear from [Catalog Explorer](/concepts/catalog-explorer.md).
- SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail.

^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

Disabling legacy access does not prevent users from using cluster-level credentials (e.g., instance profiles or service principals) that are available on a cluster. Databricks recommends removing such credentials from clusters. Additionally, [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) do not respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting. To prevent users from creating and using such clusters, enable the **Enforce User Isolation** setting for the workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## How to Disable Access

### Workspace‑Level Disablement

Use the **Disable legacy access** workspace admin setting:

1. As a workspace admin, log in to your Databricks workspace.
2. Click the user profile menu and select **Settings**.
3. Navigate to **Workspace admin > Security**.
4. Set **Disable legacy access** to **Disabled: legacy access features cannot be used**.
5. Wait approximately five minutes for the setting to take effect.
6. Restart all running clusters.

^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

To disable legacy access at the account level for new workspaces, use the **Disable legacy features** account setting. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

### Cluster‑Level Disablement

You can also disable direct access gradually on a per‑cluster basis, which is useful during a staged migration. Set the following Spark Configurations on the cluster:

```
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). When Unity Catalog‑only mode is enabled, you must set an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution that replaces the legacy Hive [Metastore](/concepts/metastore.md).
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) – Allows Unity Catalog to govern tables in an external Hive [Metastore](/concepts/metastore.md) without migration.
- Fallback – Mechanism that routes queries to the Hive [Metastore](/concepts/metastore.md) when a table is not found in Unity Catalog.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The Databricks UI for browsing catalogs and schemas.
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) – Cluster mode that does not respect the legacy disable setting.
- Enforce User Isolation – Workspace setting to prevent No Isolation shared clusters.
- Spark Configurations – Cluster‑level settings used to enable Unity Catalog‑only mode.
- Databricks Runtime – The runtime version requirement for disabled legacy access.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
