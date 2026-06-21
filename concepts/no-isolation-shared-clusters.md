---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32ad6cf5bf11165526491d9eefdfc694901e6f89f396d1c26f55244ca17a34d0
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - no-isolation-shared-clusters
    - NISC
    - Enable admin protection for no isolation shared clusters
    - No-Isolation Shared Access Mode
    - No-isolation shared access mode
    - Shared Cluster
    - no-isolation shared access mode
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: No Isolation Shared Clusters
description: A cluster type that does not respect the legacy Hive metastore disablement setting, requiring the Enforce User Isolation setting to prevent users from bypassing Unity Catalog governance.
tags:
  - unity-catalog
  - compute-clusters
  - security
timestamp: "2026-06-19T10:13:43.905Z"
---

# No Isolation Shared Clusters

**No Isolation Shared Clusters** are a type of compute cluster in Databricks where users share the same JVM and thus are not isolated from one another. These clusters do **not** respect the workspace-level setting that disables access to the legacy Hive [Metastore](/concepts/metastore.md). As a result, even after an admin has disabled direct Hive [Metastore](/concepts/metastore.md) access for the workspace, users running on a No Isolation shared cluster can still query tables registered in the `hive_metastore` catalog, bypassing Unity Catalog governance entirely. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

To prevent users from creating and using No Isolation shared clusters, workspace admins should enable the **Enforce User Isolation** setting. When enabled, only user isolation cluster types are allowed, and No Isolation shared clusters cannot be launched. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that No Isolation shared clusters can bypass.
- Hive Metastore Disablement – The workspace setting that No Isolation shared clusters do not respect.
- Enforce User Isolation – The setting that prevents creation of No Isolation shared clusters.
- User Isolation Clusters – The alternative cluster type that respects Unity Catalog policies.
- Cluster Types in Databricks – Overview of shared, single-user, and No Isolation clusters.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
