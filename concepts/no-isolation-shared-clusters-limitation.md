---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cefbbb48e9b8d6bd1638874665c5aacf35747eda571d65b4c99ee5a440dd496d
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - no-isolation-shared-clusters-limitation
    - NISCL
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: No Isolation Shared Clusters Limitation
description: No Isolation shared clusters do not respect the legacy Hive metastore disablement setting, requiring the Enforce User Isolation setting to prevent users from bypassing the disablement.
tags:
  - databricks
  - clusters
  - security
  - hive-metastore
  - isolation
timestamp: "2026-06-18T15:27:58.686Z"
---

---
title: No Isolation Shared Clusters Limitation
summary: No Isolation shared clusters ignore the legacy Hive [Metastore](/concepts/metastore.md) disablement setting, requiring workspace-level user isolation enforcement to prevent their use.
sources:
  - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:00:00.000Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - databricks
  - security
  - unity-catalog
aliases:
  - no-isolation-shared-clusters-limitation
  - NISCL
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# No Isolation Shared Clusters Limitation

The **No Isolation Shared Clusters Limitation** refers to the behavior where No Isolation shared clusters in Databricks do not respect the workspace setting that disables direct access to the legacy [Hive metastore](/concepts/built-in-hive-metastore.md). This can allow users to bypass [Unity Catalog](/concepts/unity-catalog.md) governance even after the workspace admin has disabled legacy access for other cluster types. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Cause

No Isolation shared clusters are designed with a different security model compared to other cluster types. The workspace-level **Disable legacy access** setting, which prevents all clusters from querying the `hive_metastore` catalog, is not enforced on No Isolation shared clusters. As a result, users can still create and use these clusters to access Hive [Metastore](/concepts/metastore.md) tables directly. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Solution

To prevent users from creating and using No Isolation shared clusters that bypass the legacy access disablement, workspace admins must enable the **Enforce User Isolation** setting for the workspace. Once enabled, No Isolation shared clusters cannot be created or run. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

See Enforce User Isolation Cluster Types on a Workspace for details on how to enable this setting.

## Related Concepts

- [Disable Legacy Access](/concepts/disable-legacy-hive-metastore-access.md) – The workspace setting that No Isolation shared clusters ignore.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance framework that Hive [Metastore](/concepts/metastore.md) bypass undermines.
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) – Alternative way to govern Hive tables after disabling direct access.
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) – The cluster type subject to this limitation.
- Data Governance on Databricks – Broader context for security controls.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
