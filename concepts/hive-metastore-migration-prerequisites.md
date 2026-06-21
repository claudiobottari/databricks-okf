---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b4f707de9e0032e1d227209c863d3d53ec1d18f2718f4f8c2fb7a0248fe09940
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-migration-prerequisites
    - HMMP
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Hive Metastore Migration Prerequisites
description: The criteria that must be met before disabling legacy Hive metastore access, including completing table migration to Unity Catalog and upgrading all jobs to Databricks Runtime 13.3 LTS or above.
tags:
  - unity-catalog
  - migration
  - best-practices
timestamp: "2026-06-19T10:13:54.709Z"
---

# Hive [Metastore](/concepts/metastore.md) Migration Prerequisites

**Hive [Metastore](/concepts/metastore.md) Migration Prerequisites** are the conditions that must be met before you can disable direct access to the legacy Hive [Metastore](/concepts/metastore.md) used by a Databricks workspace. Disabling direct Hive [Metastore](/concepts/metastore.md) access is an important step in migrating to [Unity Catalog](/concepts/unity-catalog.md) and ensuring full data governance coverage. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Overview

Data in the Hive [Metastore](/concepts/metastore.md) is not governed by Unity Catalog. Disabling direct access prevents users from bypassing Unity Catalog and accessing tables registered in the Hive [Metastore](/concepts/metastore.md). You can disable access and continue to query Hive [Metastore](/concepts/metastore.md) tables by using [Hive Metastore Federation](/concepts/hive-metastore-federation.md), which allows Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md). Federation can be set up either before or after disabling direct workspace access. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites

Before disabling the legacy Hive [Metastore](/concepts/metastore.md), you must meet the following criteria: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- **Migration completion**: You have finished migrating all tables registered in the legacy [Metastore](/concepts/metastore.md) to Unity Catalog, or you have always used Unity Catalog and never used the legacy Hive [Metastore](/concepts/metastore.md).
- **User enforcement**: You want to force your users to stop using tables registered in the legacy [Metastore](/concepts/metastore.md).
- **Runtime version**: All jobs have been upgraded to Databricks Runtime 13.3 LTS or above.

## Effects of Disabling Legacy Access

After you disable the legacy [Metastore](/concepts/metastore.md), the following changes take effect: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- Any jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) will fail.
- [Hive metastore federation fallback](/concepts/hive-metastore-fallback.md) is disabled.
- Jobs running on Databricks Runtime versions below 13.3 will fail. Currently running jobs continue to work until terminated, but restarts on those clusters will fail.
- The **Legacy** heading and `hive_metastore` catalog disappear from the Catalog Explorer browser pane.
- SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail.

## Important Considerations

### Cluster Credentials

Disabling legacy access does not prevent users from using cluster-level credentials, such as instance profiles or service principals, that are available on a cluster. Databricks recommends removing such credentials from your clusters. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

### No Isolation Shared Clusters

_No Isolation shared_ clusters do not respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting. To prevent users from creating and using such clusters, enable the **Enforce User Isolation** setting for the workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## How to Disable Legacy Access

### Workspace-Level Disablement

As a workspace admin, use the **Disable legacy access** workspace admin setting: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

1. Log in to your Databricks workspace as a workspace admin.
2. Click the user profile menu at the top right and select **Settings**.
3. Go to **Workspace admin > Security**.
4. Set **Disable legacy access** to **Disabled: legacy access features cannot be used**.
5. Wait approximately five minutes for the setting to take effect.
6. Restart all running clusters.

### Account-Level Disablement

To disable access to the Hive [Metastore](/concepts/metastore.md) at the account level for new workspaces, use the **Disable legacy features** account setting. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

### Cluster-by-Cluster Disablement

You can also disable direct access gradually on a cluster-by-cluster basis. This approach is useful during a Unity Catalog migration when you want to reduce reliance on the Hive [Metastore](/concepts/metastore.md) incrementally. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

To disable direct access, set the following Spark configurations on the cluster:

```
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). When you enable Unity Catalog-only mode, you must also set an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Migration](/concepts/unity-catalog-migration-path.md) — The process of migrating tables and views from Hive [Metastore](/concepts/metastore.md) to Unity Catalog
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Enabling Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md)
- Upgrade Hive Tables and Views to Unity Catalog — Detailed migration guidance
- Enforce User Isolation — Workspace setting to prevent No Isolation shared clusters
- [Default Catalog Configuration](/concepts/default-catalog-configuration-in-unity-catalog.md) — Setting the initial catalog for Unity Catalog-only mode

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
