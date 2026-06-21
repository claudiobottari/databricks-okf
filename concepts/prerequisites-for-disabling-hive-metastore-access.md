---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 119e877305c4ea03e93bc8cc33a5542eb37930af48f8a9d7120494e53b778504
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-disabling-hive-metastore-access
    - PFDHMA
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Prerequisites for Disabling Hive Metastore Access
description: Conditions that must be met before disabling legacy Hive metastore, including completed migration, Databricks Runtime 13.3 LTS+, and user readiness.
tags:
  - databricks
  - migration
  - hive-metastore
  - unity-catalog
timestamp: "2026-06-19T18:31:58.168Z"
---

# Prerequisites for Disabling Hive [Metastore](/concepts/metastore.md) Access

**Prerequisites for Disabling Hive [Metastore](/concepts/metastore.md) Access** describes the conditions that should be met before a Databricks workspace admin turns off direct access to the legacy Hive [Metastore](/concepts/metastore.md) (workspace-local, external, or AWS Glue). Disabling this access is a key step in completing a migration to [Unity Catalog](/concepts/unity-catalog.md) and ensuring that all data governance is handled by Unity Catalog rather than the legacy [Metastore](/concepts/metastore.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites

Before a workspace admin disables the legacy Hive [Metastore](/concepts/metastore.md), the following criteria should be satisfied:

1. **All legacy tables must be migrated to Unity Catalog**, or the workspace must have always used Unity Catalog and never the legacy Hive [Metastore](/concepts/metastore.md). This ensures that no active workloads rely on tables registered outside Unity Catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
2. **All jobs must be upgraded to Databricks Runtime 13.3 LTS or above**. After the legacy [Metastore](/concepts/metastore.md) is disabled, any job running on a runtime version below 13.3 will fail. Currently running jobs continue until termination, but restarts will fail. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
3. **The admin must intend to force users to stop using tables registered in the legacy metastore**. Disabling access prevents any new queries against `hive_metastore` and removes the **Legacy** heading from the Catalog Explorer. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Additional Considerations

- **No Isolation shared clusters** do not respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting. To prevent users from creating and using such clusters after disabling, enable the **Enforce User Isolation** workspace setting. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- **Cluster-level credentials** (such as instance profiles or service principals) remain available on clusters even after disabling legacy access. Databricks recommends removing such credentials from clusters. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- The disablement can be performed at the **workspace level** via the **Disable legacy access** admin setting, or gradually on a **cluster-by-cluster basis** using Spark configurations (`spark.databricks.unityCatalogOnlyMode` and an initial catalog namespace). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Effects After Disabling

Once the setting is applied (and after a five-minute propagation delay and a restart of all running clusters):

- Jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) will fail.
- Fallback to the Hive [Metastore](/concepts/metastore.md) is disabled.
- The **Legacy** heading and `hive_metastore` catalog disappear from Catalog Explorer.
- SQL commands that attempt to show contents of `hive_metastore` fail.

^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that replaces the legacy Hive [Metastore](/concepts/metastore.md).
- [Hive metastore](/concepts/built-in-hive-metastore.md) – Legacy metadata store for Databricks tables.
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) – Allows Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md).
- Databricks Runtime – The runtime version requirement for jobs after disabling.
- Enforce User Isolation – Workspace setting required to make the disablement effective for all cluster types.
- [Disable legacy features (account level)](/concepts/disable-legacy-features-setting.md) – Account-level equivalent for new workspaces.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
