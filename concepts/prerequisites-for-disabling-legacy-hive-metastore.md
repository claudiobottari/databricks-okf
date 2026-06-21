---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 239a70ac82f678eaecba78bfbc970b3eb2445a459db85261ec99cab07f89fbf0
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-disabling-legacy-hive-metastore
    - PFDLHM
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Prerequisites for Disabling Legacy Hive Metastore
description: Criteria that must be met before disabling the legacy Hive metastore, including completed Unity Catalog migration and Databricks Runtime 13.3 LTS or above
tags:
  - databricks
  - unity-catalog
  - migration
timestamp: "2026-06-19T15:12:23.320Z"
---

Based on the provided source material, here is the wiki page for "Prerequisites for Disabling Legacy Hive [Metastore](/concepts/metastore.md)".

---

## Prerequisites for Disabling Legacy Hive [Metastore](/concepts/metastore.md)

**Prerequisites for Disabling Legacy Hive Metastore** outlines the conditions that must be met before a Databricks workspace admin can disable direct access to the legacy Hive [Metastore](/concepts/metastore.md) — whether the workspace-local Hive [Metastore](/concepts/metastore.md), an external Hive [Metastore](/concepts/metastore.md), or AWS Glue. Disabling direct access prevents users from bypassing [Unity Catalog](/concepts/unity-catalog.md) and accessing tables registered in the Hive [Metastore](/concepts/metastore.md), which is an important step in ensuring full Unity Catalog data governance. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Criteria to Meet Before Disabling

Before you disable the legacy Hive [Metastore](/concepts/metastore.md), you should meet the following criteria: ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- **Migration or absence of legacy tables.** You are done migrating all tables registered in the legacy [Metastore](/concepts/metastore.md) to Unity Catalog, or you have always used Unity Catalog and never the legacy Hive [Metastore](/concepts/metastore.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- **Enforcement intent.** You want to force your users to stop using tables registered in the legacy [Metastore](/concepts/metastore.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- **Runtime version requirement.** You have upgraded all jobs to Databricks Runtime 13.3 LTS or above. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Considerations Before Disabling

Even after migrating to Unity Catalog, Databricks compute clusters connect to the Hive [Metastore](/concepts/metastore.md) by default unless you explicitly disable Hive [Metastore](/concepts/metastore.md) access. To prevent Hive [Metastore](/concepts/metastore.md) maintenance from affecting your Unity Catalog workloads, you can disable direct access at the workspace level or on a cluster-by-cluster basis using a Spark configuration. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

You can also disable access to the Hive [Metastore](/concepts/metastore.md) at the account level for new workspaces using the [Disable Legacy Features](/concepts/disable-legacy-features-setting.md) account setting. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

### Federation as an Alternative

You can disable direct access and continue to query tables managed by your Hive [Metastore](/concepts/metastore.md) by taking advantage of [Hive Metastore Federation](/concepts/hive-metastore-federation.md). [Hive Metastore Federation](/concepts/hive-metastore-federation.md) enables Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md). You can federate Hive [Metastore](/concepts/metastore.md) tables either before or after you disable direct workspace access to the Hive [Metastore](/concepts/metastore.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Effects of Disabling

After you disable the legacy [Metastore](/concepts/metastore.md): ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- Any jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) will fail.
- [Hive Metastore Federation#fallback|Fallback](/concepts/hive-metastore-fallback.md) is disabled.
- Jobs that run on Databricks Runtime versions below 13.3 will fail. Currently running jobs will continue to work until they are terminated, but restarts on those clusters will fail.
- The **Legacy** heading and `hive_metastore` catalog disappear from the Catalog Explorer browser pane.
- SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail.

## Additional Security Considerations

### Cluster-Level Credentials

Disabling legacy access does not prevent users from using cluster-level credentials, such as instance profiles or service principals, that are available on a cluster. Databricks recommends that you remove such credentials from your clusters. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

### No Isolation Shared Clusters

_No Isolation shared_ clusters do not respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting. To prevent users from creating and using such clusters, enable the _Enforce User Isolation_ setting for the workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Migration](/concepts/unity-catalog-migration-path.md) — The process of migrating Hive tables to Unity Catalog
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Governing Hive [Metastore](/concepts/metastore.md) tables through Unity Catalog
- [Disable Legacy Features](/concepts/disable-legacy-features-setting.md) — Account-level setting to disable legacy features for new workspaces
- Enforce User Isolation — Workspace setting to prevent No Isolation shared clusters
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for Databricks

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
