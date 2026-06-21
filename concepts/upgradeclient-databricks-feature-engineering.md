---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24dc8ca8217dba1bd2d7865180e79e2b34eb335239e176e2da2ed8805e81194c
  pageDirectory: concepts
  sources:
    - upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - upgradeclient-databricks-feature-engineering
    - U(FE
    - Migrate to databricks-feature-engineering
    - Migration to databricks-feature-engineering
  citations:
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
title: UpgradeClient (Databricks Feature Engineering)
description: A Python client class from databricks.feature_engineering used to upgrade workspace feature table metadata to Unity Catalog.
tags:
  - databricks
  - api
  - migration
timestamp: "2026-06-19T23:18:23.433Z"
---

# UpgradeClient (Databricks Feature Engineering)

The **UpgradeClient** is a class in the `databricks-feature-engineering` Python library used to migrate workspace [Feature Table](/concepts/feature-table.md) metadata to [Unity Catalog](/concepts/unity-catalog.md). It provides the `upgrade_workspace_table` method that transfers [Feature Table](/concepts/feature-table.md) metadata from the workspace-level [Feature Store](/concepts/feature-store.md) to a Unity Catalog-managed table.

## Overview

The UpgradeClient is designed to support the migration path from workspace-level [Feature Tables](/concepts/feature-tables.md) to [Unity Catalog](/concepts/unity-catalog.md)-governed [Feature Tables](/concepts/feature-tables.md). It operates on [Feature Tables](/concepts/feature-tables.md) whose underlying Delta tables have already been upgraded to [Unity Catalog](/concepts/unity-catalog.md). The client handles the migration of feature-specific metadata that would otherwise be lost in a direct table upgrade. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before using the UpgradeClient, the underlying workspace Delta table must first be upgraded to [Unity Catalog](/concepts/unity-catalog.md). Follow the instructions in the Databricks documentation for upgrading tables and views to [Unity Catalog](/concepts/unity-catalog.md). Attempting to call `upgrade_workspace_table` without first completing this step will result in an error. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Usage

### Initialization

```python
from databricks.feature_engineering import UpgradeClient

upgrade_client = UpgradeClient()
```

Databricks recommends always using the latest version of `databricks-feature-engineering` for this operation, regardless of the Databricks Runtime version you are using. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Basic Upgrade

The `upgrade_workspace_table` method takes two required parameters: the source workspace table name and the target [Unity Catalog](/concepts/unity-catalog.md) table name.

```python
upgrade_client.upgrade_workspace_table(
  source_workspace_table='recommender_system.customer_features',
  target_uc_table='ml.recommender_system.customer_features'
)
```

^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Overwriting Existing Metadata

By default, if metadata on the target [Unity Catalog](/concepts/unity-catalog.md) table conflicts with the source table metadata, the upgrade fails with an error. To bypass this behavior and overwrite any existing metadata on the target table, pass `overwrite=True`:

```python
upgrade_client.upgrade_workspace_table(
  source_workspace_table='recommender_system.customer_features',
  target_uc_table='ml.recommender_system.customer_features',
  overwrite=True
)
```

^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Metadata Upgraded

The following [Feature Table](/concepts/feature-table.md) metadata is transferred to [Unity Catalog](/concepts/unity-catalog.md) by the UpgradeClient: ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

- Primary keys
- Time series columns
- Table and column comments (descriptions)
- Table and column tags
- Notebook and job lineage

## Metadata Conflict Handling

The UpgradeClient handles metadata conflicts differently depending on the metadata type: ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

- **Table and column comments**: If the target table has existing comments that differ from the source, the upgrade method skips upgrading comments and logs a warning. If you are using version 0.1.2 or below of `databricks-feature-engineering`, an error is thrown and the upgrade does not run.
- **All other metadata**: A mismatch between the target table and source table causes an error and prevents the upgrade, unless `overwrite=True` is specified.

## Limitations

- Upgrading tags and time series columns is not supported in Databricks Runtime 13.2 ML and below. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]
- If the target table in [Unity Catalog](/concepts/unity-catalog.md) was created using `CREATE TABLE AS SELECT` or a similar method that cloned the source table, updates to the source table are not automatically synchronized in the target table. Notify producers and consumers of the upgraded [Feature Table](/concepts/feature-table.md) to start using the new [Unity Catalog](/concepts/unity-catalog.md) table name. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – The workspace-level [Feature Store](/concepts/feature-store.md) management system
- [Unity Catalog](/concepts/unity-catalog.md) – The governance and metadata catalog for Databricks
- upgrade_workspace_table method|UpgradeClient.upgrade_workspace_table – The primary method for migrating [Feature Table](/concepts/feature-table.md) metadata
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md) – Overview of the feature engineering workflow
- Databricks Feature Store vs Unity Catalog – Comparison of workspace and catalog-managed [Feature Tables](/concepts/feature-tables.md)

## Sources

- upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
