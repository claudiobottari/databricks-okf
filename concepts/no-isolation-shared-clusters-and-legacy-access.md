---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8782bb9b890c0a94a0807f7aebd7331aa45ea732768f7d7f992982edf0894e0
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - no-isolation-shared-clusters-and-legacy-access
    - Legacy Access and No Isolation Shared Clusters
    - NISCALA
    - Enabling admin protection for no isolation shared clusters
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: No Isolation Shared Clusters and Legacy Access
description: No Isolation shared clusters do not respect the legacy Hive metastore disablement setting; Enforce User Isolation must be enabled instead.
tags:
  - databricks
  - security
  - compute
  - hive-metastore
timestamp: "2026-06-19T18:31:44.626Z"
---

# No Isolation Shared Clusters and Legacy Access

**No Isolation Shared Clusters** are a cluster type in Databricks that do not enforce user-level isolation. These clusters bypass the workspace-level setting that disables direct access to the legacy Hive [Metastore](/concepts/metastore.md) (`hive_metastore`). Even when a workspace admin has disabled legacy Hive [Metastore](/concepts/metastore.md) access to enforce Unity Catalog usage, users can still create and use No Isolation shared clusters to query tables registered in the Hive [Metastore](/concepts/metastore.md). ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Why This Matters

The workspace admin setting **Disable legacy access** is designed to prevent all clusters and workloads from connecting to the Hive [Metastore](/concepts/metastore.md), forcing users to rely entirely on [Unity Catalog](/concepts/unity-catalog.md) for data governance. However, because No Isolation shared clusters do not respect this setting, they create a security gap: users can bypass Unity Catalog and access ungoverned Hive [Metastore](/concepts/metastore.md) tables. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

Additionally, disabling legacy access does not prevent users from using cluster-level credentials (such as instance profiles or service principals) that are available on a cluster. Databricks recommends removing such credentials from clusters to further tighten security. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Solution: Enforce User Isolation

To prevent users from creating and using No Isolation shared clusters, the workspace admin must enable the **Enforce User Isolation** setting for the workspace. This setting restricts cluster types to those that provide full user isolation (e.g., high-concurrency clusters), thereby eliminating the ability to create No Isolation clusters and closing the legacy access loophole. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

Enforce User Isolation can be enabled in the workspace admin settings under **Workspace admin > Security > Enforce User Isolation cluster types**. After enabling this setting, only user-isolated cluster types are available in the workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Legacy Hive Metastore](/concepts/disable-legacy-hive-metastore-access.md) — The Hive [Metastore](/concepts/metastore.md) (`hive_metastore`) that holds ungoverned tables.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that supersedes the Hive [Metastore](/concepts/metastore.md).
- Enforce User Isolation — The workspace setting that restricts cluster types to those with user isolation.
- [Disable Legacy Access](/concepts/disable-legacy-hive-metastore-access.md) — The workspace admin setting that blocks direct Hive [Metastore](/concepts/metastore.md) access.
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — An alternative approach to govern Hive [Metastore](/concepts/metastore.md) tables via Unity Catalog while disabling direct access.

## Best Practices

- **Before disabling legacy access**, migrate all Hive [Metastore](/concepts/metastore.md) tables to Unity Catalog or federate them as foreign catalogs. Ensure all jobs are upgraded to Databricks Runtime 13.3 LTS or above. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- **After disabling legacy access**, enable **Enforce User Isolation** to close the No Isolation shared cluster loophole. Remove any cluster-level credentials (instance profiles, service principals) from clusters. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- **Monitor audit logs** for any attempts to create No Isolation clusters after user isolation is enforced.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
