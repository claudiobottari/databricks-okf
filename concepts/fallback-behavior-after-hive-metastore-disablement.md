---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89f835284298ecec867da5719b945f3acaa6a0b25f4bdd9f36acaaa9f8bed9d3
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fallback-behavior-after-hive-metastore-disablement
    - FBAHMD
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Fallback Behavior After Hive Metastore Disablement
description: When legacy Hive metastore access is disabled, fallback to hive_metastore catalog is disabled and jobs referencing legacy tables fail.
tags:
  - databricks
  - hive-metastore
  - unity-catalog
  - jobs
timestamp: "2026-06-19T18:32:13.296Z"
---

# Fallback Behavior After Hive [Metastore](/concepts/metastore.md) Disablement

**Fallback Behavior After Hive [Metastore](/concepts/metastore.md) Disablement** refers to the consequences and limitations that occur when a workspace admin disables direct access to the legacy [Hive Metastore](/concepts/built-in-hive-metastore.md) used by a Databricks workspace. This action is typically taken after completing a [Unity Catalog](/concepts/unity-catalog.md) migration to ensure full data governance.

## Overview

When a workspace admin disables direct access to the Hive [Metastore](/concepts/metastore.md) through the **Disable legacy access** workspace admin setting, fallback behavior is one of the key features that gets disabled. Fallback is the mechanism that allows Databricks to automatically use the Hive [Metastore](/concepts/metastore.md) when queries cannot be resolved through [Unity Catalog](/concepts/unity-catalog.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Effects on Fallback

### Fallback is Disabled

Once direct Hive [Metastore](/concepts/metastore.md) access is disabled, the fallback mechanism is completely turned off. This means:

- Queries that previously would have fallen back to the legacy Hive [Metastore](/concepts/metastore.md) for table resolution will now fail.
- Jobs running against tables registered only in the Hive [Metastore](/concepts/metastore.md) will fail after the setting takes effect.
- The `hive_metastore` catalog disappears from the Catalog Explorer browser pane.
- SQL commands attempting to show contents of the `hive_metastore` catalog will fail. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

### [Hive Metastore Federation](/concepts/hive-metastore-federation.md) Alternative

Users can avoid query failures by taking advantage of [Hive Metastore Federation](/concepts/hive-metastore-federation.md), which enables Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md). This approach can be used either before or after disabling direct workspace access to the Hive [Metastore](/concepts/metastore.md), allowing continued querying of Hive [Metastore](/concepts/metastore.md) tables under Unity Catalog governance. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Cluster-Level Fallback Control

Fallback behavior can also be managed on a per-cluster basis using Spark configurations, without disabling it workspace-wide. This gradual approach is useful during migration:

```spark
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

When enabling Unity Catalog-only mode on a cluster, you must also set an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites for Disabling Fallback

Before disabling the legacy Hive [Metastore](/concepts/metastore.md) (and thus fallback), the following criteria should be met:

- Migration of all tables registered in the legacy [Metastore](/concepts/metastore.md) to Unity Catalog is complete.
- Users are ready to stop using tables registered in the legacy [Metastore](/concepts/metastore.md).
- All jobs have been upgraded to Databricks Runtime 13.3 LTS or above. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that replaces Hive [Metastore](/concepts/metastore.md).
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Allows Unity Catalog to govern Hive [Metastore](/concepts/metastore.md) tables without fallback.
- [Disable Legacy Access](/concepts/disable-legacy-hive-metastore-access.md) — The workspace admin setting that controls fallback behavior.
- Hive Metastore Migration — The process of moving from Hive [Metastore](/concepts/metastore.md) to Unity Catalog.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The browser interface where `hive_metastore` disappears after disablement.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
