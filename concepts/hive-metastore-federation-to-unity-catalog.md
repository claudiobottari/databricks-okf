---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e187e975d5fd8f7bde8dce06e4095fadbf3520fa1b89b8950be93f73b969f6f
  pageDirectory: concepts
  sources:
    - work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-federation-to-unity-catalog
    - HMFTUC
    - Hive metastore migration to Unity Catalog
    - Work with the legacy Hive metastore alongside Unity Catalog
  citations:
    - file: work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
title: Hive Metastore Federation to Unity Catalog
description: Hive Metastore federation creates a foreign catalog in Unity Catalog that mirrors the Hive metastore, offering a gradual migration path as an alternative to upgrading all tables at once.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - federation
  - migration
timestamp: "2026-06-19T23:27:00.471Z"
---

# [Hive Metastore Federation](/concepts/hive-metastore-federation.md) to [Unity Catalog](/concepts/unity-catalog.md)

**Hive [Metastore](/concepts/metastore.md) Federation to Unity Catalog** is a migration approach that creates a foreign catalog in [Unity Catalog](/concepts/unity-catalog.md) which mirrors the existing legacy [Hive Metastore](/concepts/built-in-hive-metastore.md). It enables users to gradually migrate tables and workloads away from the per-workspace Hive [Metastore](/concepts/metastore.md) without requiring an immediate, wholesale upgrade. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Overview

When a workspace was created before being enabled for [Unity Catalog](/concepts/unity-catalog.md), it typically retains a Hive [Metastore](/concepts/metastore.md) containing existing data. Databricks recommends migrating that data to [Unity Catalog](/concepts/unity-catalog.md) to benefit from features such as built-in auditing, lineage, and fine-grained access control. Two migration paths are available: directly upgrading all tables, or federating the Hive [Metastore](/concepts/metastore.md) using **Hive [Metastore](/concepts/metastore.md) federation**. The latter provides a more gradual transition by allowing users to continue working with Hive-metastore tables through a foreign catalog in [Unity Catalog](/concepts/unity-catalog.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## How It Works

When [Hive Metastore Federation](/concepts/hive-metastore-federation.md) is applied, a foreign catalog is created inside [Unity Catalog](/concepts/unity-catalog.md) that mirrors the structure of the legacy Hive [Metastore](/concepts/metastore.md). This catalog can be queried using the standard [Three-level namespace (catalog.schema.table)](/concepts/three-level-namespace-catalogschematable.md) alongside native [Unity Catalog](/concepts/unity-catalog.md) objects. The legacy Hive [Metastore](/concepts/metastore.md) itself remains in place during the transition, so existing scripts and applications that reference the `hive_metastore` catalog continue to function. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Benefits and Limitations

The primary benefit of federation is that it avoids a big‑bang migration. Users can move tables and workloads to [Unity Catalog](/concepts/unity-catalog.md) incrementally, reducing risk and operational disruption. However, tables accessed via the foreign catalog do not automatically inherit the full set of [Unity Catalog governance](/concepts/unity-catalog-governance.md) features (e.g., lineage, account‑level auditing, or the [Unity Catalog](/concepts/unity-catalog.md) privilege model). Once the migration is complete, Databricks recommends disabling direct access to the Hive [Metastore](/concepts/metastore.md) and removing the foreign catalog. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The account‑level data governance solution.
- [Legacy Hive Metastore](/concepts/disable-legacy-hive-metastore-access.md) – The per‑workspace [Metastore](/concepts/metastore.md) that federation replaces.
- Foreign Catalog – A [Unity Catalog](/concepts/unity-catalog.md) object that mirrors an external [Metastore](/concepts/metastore.md).
- Migration to Unity Catalog – The broader process of upgrading from the Hive [Metastore](/concepts/metastore.md).
- hive_metastore Catalog – The default top‑level catalog representing the legacy [Metastore](/concepts/metastore.md) in the three‑level namespace.

## Sources

- work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md

# Citations

1. [work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md](/references/work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws-c5d018d3.md)
