---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f575c69ddf3e0b287ba9cdae1132dcfc470d9a8eae421333c6e38d7b297e95e4
  pageDirectory: concepts
  sources:
    - work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disabling-direct-access-to-the-legacy-hive-metastore
    - DDATTLHM
    - disable direct access to the Hive metastore
    - Disable access to Hive metastore
    - Disable access to the Hive metastore used by your Databricks workspace
  citations:
    - file: work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
title: Disabling Direct Access to the Legacy Hive Metastore
description: After migrating tables to Unity Catalog, Databricks recommends explicitly disabling direct Hive metastore access (workspace-wide or per-cluster) to avoid unnecessary connections and resource consumption.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - migration
timestamp: "2026-06-19T23:26:50.746Z"
---

# Disabling Direct Access to the Legacy Hive [Metastore](/concepts/metastore.md)

**Disabling Direct Access to the Legacy Hive Metastore** refers to the process of explicitly preventing Databricks compute clusters from connecting to the per-workspace [Hive Metastore](/concepts/built-in-hive-metastore.md) after migrating data and workloads to [Unity Catalog](/concepts/unity-catalog.md). This is a recommended post-migration step to fully transition away from the legacy [Metastore](/concepts/metastore.md) and benefit from [Unity Catalog](/concepts/unity-catalog.md)'s security and governance features.

## Motivation

The per-workspace Hive [Metastore](/concepts/metastore.md) is a legacy feature with significant limitations. Tables in the Hive [Metastore](/concepts/metastore.md) do not benefit from the full set of security and governance features provided by [Unity Catalog](/concepts/unity-catalog.md), such as built-in auditing, lineage, and access control. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

After migrating tables and workloads to [Unity Catalog](/concepts/unity-catalog.md), Databricks compute clusters continue to connect to the Hive [Metastore](/concepts/metastore.md) by default unless you explicitly disable Hive [Metastore](/concepts/metastore.md) access. This default behavior means that even after migration, resources are still consumed on the legacy [Metastore](/concepts/metastore.md), potentially hitting its connection limits. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

The Databricks-hosted legacy Hive [Metastore](/concepts/metastore.md) has resource limits to ensure reliability, including limits on concurrent (active) connections and connections per hour. If workloads exceed these limits, clusters and jobs might encounter [Metastore](/concepts/metastore.md) connection errors or fail to start. Disabling direct access eliminates these constraints because [Unity Catalog](/concepts/unity-catalog.md) doesn't use the legacy Hive [Metastore](/concepts/metastore.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## When to Disable Access

Databricks recommends explicitly disabling direct access to the Hive [Metastore](/concepts/metastore.md) after you have migrated your tables to [Unity Catalog](/concepts/unity-catalog.md). Two migration paths are available:

- **Upgrade all tables** registered in the Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md).
- **Federate your Hive metastore** to [Unity Catalog](/concepts/unity-catalog.md) using [Hive Metastore Federation](/concepts/hive-metastore-federation.md) for a more gradual approach, which creates a foreign catalog in [Unity Catalog](/concepts/unity-catalog.md) that mirrors the Hive [Metastore](/concepts/metastore.md).

See [Upgrade a Databricks workspace to Unity Catalog](/concepts/migrating-existing-workspaces-to-unity-catalog.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## How to Disable Access

You can disable direct access to the Hive [Metastore](/concepts/metastore.md) across your entire workspace, or individually per compute cluster. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

For detailed instructions, see [Disable access to the Hive metastore used by your Databricks workspace](/concepts/disabling-direct-access-to-the-legacy-hive-metastore.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore](/concepts/built-in-hive-metastore.md) — The legacy per-workspace [Metastore](/concepts/metastore.md)
- [Unity Catalog](/concepts/unity-catalog.md) — The modern governance solution replacing the Hive [Metastore](/concepts/metastore.md)
- [hive_metastore catalog](/concepts/hive-metastore-federation.md) — The top-level catalog name for legacy Hive [Metastore](/concepts/metastore.md) tables in the [Three-Level Namespace](/concepts/three-level-namespace.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — An alternative migration path providing a gradual approach
- [Legacy Table Access Control](/concepts/table-access-control-tacl.md) — Access controls that apply to Hive [Metastore](/concepts/metastore.md) tables in [Standard Access Mode](/concepts/standard-access-mode.md) clusters

## Sources

- work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md

# Citations

1. [work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md](/references/work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws-c5d018d3.md)
