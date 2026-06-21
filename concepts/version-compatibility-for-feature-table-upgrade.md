---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37dc75d83e80c88ead262ed1bcd658583eb5572a90db3a360a06d10a3619f83a
  pageDirectory: concepts
  sources:
    - upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - version-compatibility-for-feature-table-upgrade
    - VCFFTU
  citations:
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
title: Version compatibility for feature table upgrade
description: Upgrading tags and time series columns is not supported in Databricks Runtime 13.2 ML and below; older client versions (0.1.2 and below) throw errors on comment mismatch instead of skipping.
tags:
  - databricks
  - compatibility
  - versioning
timestamp: "2026-06-19T23:18:23.887Z"
---

## Version Compatibility for [Feature Table](/concepts/feature-table.md) Upgrade

**Version compatibility for [Feature Table](/concepts/feature-table.md) upgrade** refers to the required versions of the `databricks-feature-engineering` library and the Databricks Runtime that are needed to successfully upgrade a workspace feature table to [Unity Catalog](/concepts/unity-catalog.md) using the `upgrade_workspace_table` API.

### Overview

When upgrading a workspace feature table’s metadata to [Unity Catalog](/concepts/unity-catalog.md), you must use the `UpgradeClient` from the `databricks-feature-engineering` library. The operation has specific version constraints on both the library and the Databricks Runtime that determine which metadata can be migrated and whether the upgrade succeeds or fails. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Version Requirements

Databricks recommends always using the **latest version** of `databricks-feature-engineering` for the upgrade operation, regardless of the Databricks Runtime version in use. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

The library version **0.1.2 or below** is not supported. If you attempt to run `upgrade_workspace_table` with one of these older versions, an error is thrown and the upgrade does not run. Use version **0.1.3 or higher** to avoid this failure. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Runtime Limitations

The upgrade of **tags** and **time series columns** to [Unity Catalog](/concepts/unity-catalog.md) is **not supported** in Databricks Runtime **13.2 ML and below**. If you are using one of these runtimes, you can still perform the upgrade, but tags and time series columns will not be migrated. Upgrading to a newer ML Runtime (14.0 ML or later) is required to preserve those metadata. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Related Concepts

- Workspace feature table
- [Unity Catalog migration](/concepts/unity-catalog-migration-path.md)
- UpgradeClient
- [databricks-feature-engineering library](/concepts/databricks-feature-engineering-client.md)
- Delta table upgrade to Unity Catalog

### Sources

- upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
