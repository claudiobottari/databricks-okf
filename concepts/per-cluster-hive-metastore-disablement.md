---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72ebc844231aa4ba84427d8af77a29de5256514cad4182eab3bbfce4451f8908
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - per-cluster-hive-metastore-disablement
    - PHMD
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Per-Cluster Hive Metastore Disablement
description: A gradual approach to disabling Hive metastore access on a cluster-by-cluster basis using Spark configurations, useful during incremental Unity Catalog migration.
tags:
  - unity-catalog
  - hive-metastore
  - spark-configuration
  - compute-clusters
timestamp: "2026-06-18T12:00:55.695Z"
---

# Per-Cluster Hive [Metastore](/concepts/metastore.md) Disablement

**Per-cluster Hive [Metastore](/concepts/metastore.md) disablement** allows you to gradually turn off direct access to the legacy Hive [Metastore](/concepts/metastore.md) — including the workspace-local [Metastore](/concepts/metastore.md), an external Hive [Metastore](/concepts/metastore.md), or AWS Glue — on a cluster-by-cluster basis. This incremental approach is useful during a [Unity Catalog](/concepts/unity-catalog.md) migration when you want to reduce reliance on the Hive [Metastore](/concepts/metastore.md) step by step before disabling it for the entire workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Use Case

During a migration from the legacy Hive [Metastore](/concepts/metastore.md) to Unity Catalog, you may want to test workloads against Unity Catalog without immediately cutting off all access to the Hive [Metastore](/concepts/metastore.md) workspace-wide. Per-cluster disablement lets you enforce Unity Catalog–only mode on specific clusters while other clusters continue to have access to the Hive [Metastore](/concepts/metastore.md). Once all critical workloads have been validated on Unity Catalog, you can proceed to Workspace-Level Hive Metastore Disablement|disable the legacy metastore for the entire workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Configuration

To disable direct Hive [Metastore](/concepts/metastore.md) access on a given cluster, set the following Spark configuration properties: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

```text
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

- `spark.databricks.unityCatalogOnlyMode` – Enables Unity Catalog–only mode on the cluster. This prevents the cluster from connecting to the legacy Hive [Metastore](/concepts/metastore.md) directly. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- `spark.databricks.sql.initial.catalog.namespace` – Sets the default catalog for the cluster. Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). This is required because the cluster can no longer use `hive_metastore` as the default catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

The configuration can be set when creating or editing a compute cluster in the Databricks UI under **Spark configuration**, or via the Clusters API. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Requirements

- All jobs running on the cluster must use Databricks Runtime 13.3 LTS or above. Clusters on older runtimes will fail after this configuration is applied. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- The specified `<catalog-name>` must already exist in your Unity Catalog [Metastore](/concepts/metastore.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- [Hive metastore federation](/concepts/hive-metastore-federation.md) is often used alongside per-cluster disablement to continue querying legacy tables through Unity Catalog after direct access is blocked. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Side Effects

- The **Legacy** heading and the `hive_metastore` catalog disappear in Catalog Explorer for queries run from this cluster. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- SQL commands that attempt to show the contents of `hive_metastore` from this cluster will fail. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- Fallback to the Hive [Metastore](/concepts/metastore.md) (as described in [Hive-Metastore Federation#Fallback](/concepts/hive-metastore-fallback.md)) is disabled for the cluster. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Best Practices

1. **Test on non‑critical clusters first.** Apply the Spark configuration to development or staging clusters to validate that workloads function correctly under Unity Catalog–only mode. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
2. **Combine with workspace-level disablement.** After all clusters are confirmed working, set the workspace admin setting **Disable legacy access** to permanently enforce the restriction. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
3. **Remove cluster-level credentials.** Disabling direct Hive access does not remove cluster-level credentials (e.g., instance profiles or service principals) that might still be used to bypass Unity Catalog. Databricks recommends removing such credentials from clusters. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- Workspace-Level Hive Metastore Disablement – The admin setting that disables legacy access for all clusters at once.
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) – Allows Unity Catalog to govern tables registered in a legacy Hive [Metastore](/concepts/metastore.md) even after direct access is disabled.
- [Unity Catalog Migration](/concepts/unity-catalog-migration-path.md) – The process of upgrading Hive tables and views to Unity Catalog.
- Account-Level Legacy Feature Disablement – A setting that prevents new workspaces from enabling legacy features.
- Enforce User Isolation – Required to prevent _No Isolation shared_ clusters from bypassing the disablement setting.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
