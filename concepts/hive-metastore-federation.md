---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d65759fc22afb52d99077e857cd242798dc275d19fef15ed16271611805c3e16
  pageDirectory: concepts
  sources:
    - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
    - use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - hive-metastore-federation
    - HMF
    - Hive Metastore Migration
    - Hive metastore deprecation
    - Hive metastore federation fallback
    - Hive metastore migration
    - Hive-Metastore Federation#Fallback
    - hive_metastore catalog
  citations:
    - file: upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
    - file: use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
title: Hive Metastore Federation
description: A technique to federate an existing Hive metastore or AWS Glue catalog as a foreign catalog in Unity Catalog, enabling table upgrades without data movement.
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - federation
timestamp: "2026-06-19T23:17:39.016Z"
---

---
title: Hive [Metastore](/concepts/metastore.md) Federation
summary: A Databricks feature that enables [Unity Catalog](/concepts/unity-catalog.md) to govern tables registered in a Hive [Metastore](/concepts/metastore.md) by exposing them as a foreign catalog, easing migration and providing a path to disable legacy access.
sources:
  - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
  - use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T20:15:23.000Z"
updatedAt: "2026-06-19T20:15:23.000Z"
tags:
  - databricks
  - unity-catalog
  - hive-metastore
  - federation
  - migration
aliases:
  - hive-metastore-federation
  - HMF
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Hive [Metastore](/concepts/metastore.md) Federation

**Hive [Metastore](/concepts/metastore.md) Federation** is a Databricks integration feature that enables [Unity Catalog](/concepts/unity-catalog.md) to govern tables registered in a legacy Hive metastore—including workspace-local Hive metastores and external Hive metastores such as AWS Glue—by exposing them as a foreign catalog. This allows administrators to apply [Unity Catalog](/concepts/unity-catalog.md)'s access controls, governance capabilities, and [Three-Level Namespace](/concepts/three-level-namespace.md) (`catalog.schema.table`) to these tables without requiring an immediate full migration or data movement. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md] ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Overview

When you federate a Hive [Metastore](/concepts/metastore.md), [Unity Catalog](/concepts/unity-catalog.md) creates a foreign catalog that mirrors the [Metastore](/concepts/metastore.md)'s schemas and tables as governed securable objects. Users query those tables through [Unity Catalog](/concepts/unity-catalog.md), and all privilege checks are enforced by [Unity Catalog](/concepts/unity-catalog.md) rather than by the legacy [Metastore](/concepts/metastore.md)'s own access controls. The underlying data files remain in their original cloud storage location; federation does not move data. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Use Cases

Hive [Metastore](/concepts/metastore.md) Federation serves multiple purposes in the [Unity Catalog](/concepts/unity-catalog.md) adoption journey:

### Migration to [Unity Catalog](/concepts/unity-catalog.md) (Recommended Path)

Databricks recommends a two-step migration: first federate the Hive [Metastore](/concepts/metastore.md) or AWS Glue catalog as a foreign catalog, then upgrade the foreign tables in place using `ALTER TABLE ... SET MANAGED` or `ALTER TABLE ... SET EXTERNAL`. This in-place upgrade preserves table history, configuration, permissions, and views, and avoids any data movement. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

After tables are migrated and you no longer rely on federation to your external catalog, you can remove the connection using `ALTER CATALOG <foreign_catalog> DROP CONNECTION`. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Continued Long-Term Federation

If you choose not to upgrade your tables and want to continue working with the federated catalog permanently, you can do so. However, Databricks recommends completing the upgrade to take full advantage of [Unity Catalog](/concepts/unity-catalog.md) features such as predictive optimization. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Disabling Direct Hive [Metastore](/concepts/metastore.md) Access

After federation is in place, workspace admins can prevent users from bypassing [Unity Catalog](/concepts/unity-catalog.md) and accessing tables registered in the Hive [Metastore](/concepts/metastore.md) directly. See [Disable access to the Hive [Metastore](/concepts/metastore.md) used by your Databricks workspace]. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Federation During Migration

Hive [Metastore](/concepts/metastore.md) Federation aids in migration by enabling you to run workloads on both your legacy Hive [Metastore](/concepts/metastore.md) and its mirror in [Unity Catalog](/concepts/unity-catalog.md), easing the transition. While you are transitioning, you can continue to use queries and jobs that reference the data registered in the Hive [Metastore](/concepts/metastore.md), using Hive [Metastore](/concepts/metastore.md) Federation rather than direct Hive [Metastore](/concepts/metastore.md) access. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md] ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

The UCX project (a Databricks Labs migration toolkit) provides dedicated utilities for enabling Hive [Metastore](/concepts/metastore.md) Federation during migration:

- `enable-hms-federation`
- `create-federated-catalog`

These commands help automate the federation process as part of a larger workspace upgrade workflow. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Best Practices

- **Federate first, then disable legacy access.** This ensures a smooth transition with no loss of access to existing Hive [Metastore](/concepts/metastore.md) tables. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Upgrade foreign tables to managed tables** using `ALTER TABLE ... SET MANAGED` where possible to unlock [Unity Catalog](/concepts/unity-catalog.md) predictive optimization, which includes automatic maintenance (compaction, clustering, vacuuming) and performance improvements. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Upgrade compute to [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) or above** before disabling legacy access to avoid job failures. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Audit queries and jobs** before disabling legacy access to confirm that no references to the Hive [Metastore](/concepts/metastore.md) remain outside of federated access. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that provides federation capabilities
- [Hive metastore](/concepts/built-in-hive-metastore.md) — The legacy metadata store that federation replaces
- AWS Glue — An external Hive [Metastore](/concepts/metastore.md) commonly federated via this feature
- Foreign catalog — The [Unity Catalog](/concepts/unity-catalog.md) construct that represents the federated [Metastore](/concepts/metastore.md)
- UCX — Databricks Labs project providing utilities for [Unity Catalog](/concepts/unity-catalog.md) migration, including federation setup commands
- [Upgrade a Databricks workspace to Unity Catalog](/concepts/migrating-existing-workspaces-to-unity-catalog.md) — The overall upgrade process that federation supports
- [Disable access to the Hive metastore used by your Databricks workspace](/concepts/disabling-direct-access-to-the-legacy-hive-metastore.md) — Workspace admin setting that prevents direct Hive [Metastore](/concepts/metastore.md) usage after federation

## Sources

- upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
- use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws-30141815.md)
2. [use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md](/references/use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws-0023b143.md)
