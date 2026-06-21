---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2dc1c983ad80738c46608f4db1e58673716fc67ed2dabb52d60d85f79ab0ef3
  pageDirectory: concepts
  sources:
    - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disabling-legacy-features-after-unity-catalog-migration
    - DLFAUCM
  citations:
    - file: upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
title: Disabling Legacy Features After Unity Catalog Migration
description: Post-migration steps to disable legacy DBFS root and mounts, the Hive metastore, and no-isolation shared compute resources to enforce Unity Catalog governance.
tags:
  - databricks
  - unity-catalog
  - security
  - governance
timestamp: "2026-06-19T23:17:45.451Z"
---

# Disabling Legacy Features After [Unity Catalog](/concepts/unity-catalog.md) Migration

After completing the core steps of migrating a Databricks workspace to [Unity Catalog](/concepts/unity-catalog.md), workspace admins should **disable access to legacy features** to ensure that all data and workflows are governed by [Unity Catalog](/concepts/unity-catalog.md) and that users cannot bypass its security and governance controls. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before disabling legacy features, the following migration steps must be fully completed:

- All data and workflows that rely on DBFS root or mounts have been migrated to [Unity Catalog](/concepts/unity-catalog.md) [volumes](/concepts/ucvolumedataset.md) or [external locations](/concepts/external-location.md).
- All jobs and clusters have been upgraded to Databricks Runtime 13.3 LTS or above.
- The [Hive metastore](/concepts/built-in-hive-metastore.md) tables have been either upgraded directly to [Unity Catalog](/concepts/unity-catalog.md) or federated as a foreign catalog.

^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Disable DBFS Root and Mounts

Once migration is complete, workspace admins can disable DBFS root and mounts in existing workspaces. This prevents users from accessing data through legacy DBFS paths, ensuring that all data access is governed by [Unity Catalog](/concepts/unity-catalog.md) permissions. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

Refer to the documentation on [Disable access to DBFS root and mounts in your existing Databricks workspace](https://docs.databricks.com/aws/en/dbfs/disable-dbfs-root-mounts) for detailed instructions. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Disable the Hive [Metastore](/concepts/metastore.md)

When you have completed your [Unity Catalog](/concepts/unity-catalog.md) migration or federated your Hive [Metastore](/concepts/metastore.md) as a foreign catalog governed by [Unity Catalog](/concepts/unity-catalog.md), workspace admins can prevent users from bypassing [Unity Catalog](/concepts/unity-catalog.md) and accessing tables registered in the legacy Hive [Metastore](/concepts/metastore.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

Refer to [Disable access to the Hive [Metastore](/concepts/metastore.md) used by your Databricks workspace](https://docs.databricks.com/aws/en/data-governance/unity-catalog/disable-hms) for step-by-step guidance. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Disable No-Isolation Shared Compute Resources

To prevent users from creating any new no‑isolation shared compute resources, workspace admins can disable no‑isolation shared compute resources in their workspaces. This ensures that all compute uses the supported [access modes](/concepts/standard-access-mode.md) required by [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

Refer to [Enable admin protection for [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) in your account](https://docs.databricks.com/aws/en/admin/account-settings/no-isolation-shared) for instructions. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Centralized data governance and access control.
- DBFS – Legacy file system being deprecated after migration.
- [Hive metastore](/concepts/built-in-hive-metastore.md) – Legacy table catalog that can be disabled after migration.
- [No-isolation shared access mode](/concepts/no-isolation-shared-clusters.md) – Legacy compute mode that should be disabled.
- [Volumes](/concepts/ucvolumedataset.md) – [Unity Catalog](/concepts/unity-catalog.md) governed file storage for non‑tabular data.
- [External locations](/concepts/external-location.md) – [Unity Catalog](/concepts/unity-catalog.md) governed cloud storage paths.
- [Access modes](/concepts/standard-access-mode.md) – Supported compute security modes for [Unity Catalog](/concepts/unity-catalog.md).

## Sources

- upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws-30141815.md)
