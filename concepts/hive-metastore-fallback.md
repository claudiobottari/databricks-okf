---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d4971bc0902f0613722d5a01f2ebe034376a1ba8617ddb0b7243a17c68544d8
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-fallback
    - HMF
    - Hive Metastore Federation#fallback|Fallback
    - Hive metastore federation fallback
    - Hive-Metastore Federation#Fallback
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Hive Metastore Fallback
description: A mechanism that allows queries to fall back to legacy Hive metastore tables when they cannot be resolved in Unity Catalog, which is disabled when legacy access is turned off.
tags:
  - unity-catalog
  - hive-metastore
  - query-routing
timestamp: "2026-06-19T10:14:42.842Z"
---

# Hive [Metastore](/concepts/metastore.md) Fallback

**Hive [Metastore](/concepts/metastore.md) Fallback** refers to a mechanism in Databricks that allows queries against a federated Hive [Metastore](/concepts/metastore.md) to be resolved, even when direct workspace access to the Hive [Metastore](/concepts/metastore.md) has been disabled. This feature is part of [Hive Metastore Federation](/concepts/hive-metastore-federation.md), which enables [Unity Catalog](/concepts/unity-catalog.md) to govern tables registered in a Hive [Metastore](/concepts/metastore.md).

## Overview

When a workspace disables direct access to the legacy Hive [Metastore](/concepts/metastore.md), fallback is disabled as a consequence. This means jobs running against tables registered in the Hive [Metastore](/concepts/metastore.md) will fail if they cannot be resolved through Unity Catalog. The fallback mechanism is automatically disabled when the workspace admin setting to disable legacy access is enabled. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Relationship to [Hive Metastore Federation](/concepts/hive-metastore-federation.md)

[Hive Metastore Federation](/concepts/hive-metastore-federation.md) allows Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md) by creating a foreign catalog that references the [Metastore](/concepts/metastore.md). When federation is set up, users can query Hive [Metastore](/concepts/metastore.md) tables through Unity Catalog without needing direct Hive [Metastore](/concepts/metastore.md) access. In this context, fallback refers to the ability to query the Hive [Metastore](/concepts/metastore.md) directly when Unity Catalog cannot resolve a query — a capability that is turned off when legacy access is disabled. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

You can federate Hive [Metastore](/concepts/metastore.md) tables either before or after disabling direct workspace access to the Hive [Metastore](/concepts/metastore.md), providing flexibility in migration strategies. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Effects of Disabling Fallback

When fallback is disabled through the workspace admin setting:

- Jobs running against tables registered in the Hive [Metastore](/concepts/metastore.md) that are not accessible through Unity Catalog will fail. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- The **Legacy** heading and `hive_metastore` catalog disappear from the Catalog Explorer browser pane. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- Jobs running on Databricks Runtime versions below 13.3 LTS will fail. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites for Disabling Fallback

Before disabling the legacy Hive [Metastore](/concepts/metastore.md) (which also disables fallback), you should meet the following criteria: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- Migration of all tables registered in the legacy [Metastore](/concepts/metastore.md) to Unity Catalog is complete, or Unity Catalog has been used exclusively from the start.
- You intend to force users to stop using tables registered in the legacy [Metastore](/concepts/metastore.md).
- All jobs have been upgraded to Databricks Runtime 13.3 LTS or above.

## Cluster-Level Control

As an alternative to workspace-wide disabling, you can disable direct Hive [Metastore](/concepts/metastore.md) access (and thus fallback) on a cluster-by-cluster basis using Spark configurations. This approach is useful during a gradual Unity Catalog migration when you want to reduce reliance on Hive [Metastore](/concepts/metastore.md) incrementally. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

To disable fallback on a cluster, set the following Spark configurations: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

```
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

When Unity Catalog-only mode is enabled, you must also set an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — Data governance solution that replaces the legacy Hive [Metastore](/concepts/metastore.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Method to govern Hive [Metastore](/concepts/metastore.md) tables through Unity Catalog
- Hive metastore migration — Process of moving tables from Hive [Metastore](/concepts/metastore.md) to Unity Catalog
- [Disable legacy access](/concepts/disable-legacy-hive-metastore-access.md) — Workspace admin setting that controls Hive [Metastore](/concepts/metastore.md) fallback
- Databricks Runtime Versions — Compatibility requirements for disabling Hive [Metastore](/concepts/metastore.md) access

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
