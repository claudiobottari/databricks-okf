---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 044eeddf1d20b2e4101be2a6e54d97e58ef0ee46e19e58e26c5a99d411d5b5cb
  pageDirectory: concepts
  sources:
    - migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-deprecation-in-new-workspaces
    - HMDINW
  citations:
    - file: migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
title: Hive metastore deprecation in new workspaces
description: The Hive metastore will not be available in new workspaces created after September 30, 2026; existing Hive tables and views must be upgraded to Unity Catalog.
tags:
  - unity-catalog
  - hive-metastore
  - migration
timestamp: "2026-06-19T19:36:14.047Z"
---

# Hive [Metastore](/concepts/metastore.md) Deprecation in New Workspaces

**Hive [Metastore](/concepts/metastore.md) deprecation in new workspaces** refers to the planned removal of Hive [Metastore](/concepts/metastore.md) support in newly provisioned Databricks workspaces, effective September 30, 2026. This change is part of a broader initiative to transition all new workspaces to [Unity Catalog](/concepts/unity-catalog.md) and remove dependency on legacy features.

## Overview

Starting September 30, 2026, all new workspaces in Databricks accounts will be provisioned without access to the Hive [Metastore](/concepts/metastore.md). This change applies to accounts created both before and after December 18, 2025. Existing workspaces and their workflows are not impacted by this change. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Affected Features

The Hive [Metastore](/concepts/metastore.md) deprecation is one of several legacy features being removed from new workspaces. The full list of features that will no longer be available includes:

- [DBFS root and DBFS mounts](/concepts/dbfs-root-and-dbfs-mounts-deprecation.md)
- Hive [Metastore](/concepts/metastore.md)
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md)
- Databricks Runtime versions prior to 13.3 LTS

^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Timeline

- **December 18, 2025**: Accounts created after this date do not have access to legacy features, including the Hive [Metastore](/concepts/metastore.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]
- **September 30, 2026**: All new workspaces in all accounts will be provisioned without access to the Hive [Metastore](/concepts/metastore.md) and other legacy features. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Preparation Steps

### Remove Dependency on Hive [Metastore](/concepts/metastore.md) in Workspace Provisioning

If your organization uses automation for workspace provisioning, ensure that the automation does not rely on the Hive [Metastore](/concepts/metastore.md). Adjust any CI/CD scripts and internal operational procedures for workspace creation processes that use the Hive [Metastore](/concepts/metastore.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Set Metastores to Auto-Assign

Set a Unity Catalog [Metastore](/concepts/metastore.md) to auto-assign for every region in which you deploy workspaces. Failure to do so requires a [Metastore](/concepts/metastore.md) to be assigned manually when a workspace is provisioned. See Enable a metastore to be automatically assigned to new workspaces. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Test the New Default Behavior

If you want to test the new default behavior before September 30, 2026, you can do so by enabling the **Disable legacy features** setting in your account console. See [Disable access to legacy features in new workspaces](/concepts/disable-legacy-features-setting.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Migration to Unity Catalog

Though not required by the September 30, 2026 deadline, Databricks recommends migrating existing workspaces to Unity Catalog to take advantage of unified governance, enterprise-grade security, and advanced platform features. Key migration steps include:

- Upgrading Hive tables and views to Unity Catalog
- Migrating files stored in DBFS to volumes and external locations
- Migrating notebooks and scripts
- [Updating jobs to work with Unity Catalog](/concepts/upgrading-jobs-to-unity-catalog.md)
- Migrating to supported Databricks Runtime versions
- Migrate compute to Unity Catalog access modes
- [Disabling access to legacy features in your workspaces](/concepts/disable-legacy-features-setting.md)

^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The modern data governance solution replacing the Hive [Metastore](/concepts/metastore.md)
- [Hive metastore](/concepts/built-in-hive-metastore.md) — The legacy metadata store being deprecated
- DBFS deprecation in new workspaces — Related deprecation of DBFS root and mounts
- [No-isolation shared clusters deprecation](/concepts/no-isolation-shared-clusters-deprecation.md) — Related deprecation of legacy cluster access modes
- Workspace provisioning — The process affected by these changes

## Sources

- migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md

# Citations

1. [migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md](/references/migrate-your-account-to-uc-only-workspaces-databricks-on-aws-222dccd3.md)
