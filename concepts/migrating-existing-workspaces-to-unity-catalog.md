---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6c65536db1f5dea8df798b44d1cd2e79216d40308d5adc28da12b45f96c0ea3
  pageDirectory: concepts
  sources:
    - migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migrating-existing-workspaces-to-unity-catalog
    - MEWTUC
    - Upgrade a Databricks workspace to Unity Catalog
    - Upgrade legacy workspaces to Unity Catalog
  citations:
    - file: migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
title: Migrating existing workspaces to Unity Catalog
description: The recommended process of upgrading existing Databricks workspaces to Unity Catalog, including migrating Hive tables, DBFS files, notebooks, jobs, compute access modes, and Runtime versions.
tags:
  - unity-catalog
  - migration
  - upgrade
timestamp: "2026-06-19T19:37:29.839Z"
---

# Migrating Existing Workspaces to Unity Catalog

**Migrating existing workspaces to Unity Catalog** refers to the process of upgrading Databricks workspaces that were created before the platform-wide Unity Catalog transition to use [Unity Catalog](/concepts/unity-catalog.md) as their primary data governance layer. This migration is recommended by Databricks for all legacy workspaces to gain unified governance, enterprise-grade security, and advanced platform features. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Background

Starting on September 30, 2026, all new workspaces in every account will be provisioned with Unity Catalog and without access to certain legacy features, including DBFS root and mounts, the [Hive metastore](/concepts/built-in-hive-metastore.md), [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md), and Databricks Runtime versions prior to 13.3 LTS. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

Accounts created before December 18, 2025 that use legacy features are affected by this change. Accounts created after that date do not have access to legacy features. Existing workspaces and their workflows are not impacted by the September 30, 2026 deadline, but Databricks recommends upgrading ahead of time. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## What You Need to Do to Prepare

Admins must update their account-level workspace provisioning process to remove dependency on legacy features before September 30, 2026. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Remove Dependency on DBFS and the Hive [Metastore](/concepts/metastore.md)

If your organization uses automation for workspace provisioning, ensure that automation does not rely on legacy features. Adjust any CI/CD scripts and internal operational procedures for workspace creation processes that use DBFS root, DBFS mounts, or the Hive [Metastore](/concepts/metastore.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

To test the new default behavior before the deadline, enable the **Disable legacy features** setting in your account console. See [Disabling access to legacy features in new workspaces](/concepts/disable-legacy-features-setting.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Set Metastores to Auto-Assign

Set a [Metastore](/concepts/metastore.md) to auto-assign for every region in which you deploy workspaces. Failure to do so requires a [Metastore](/concepts/metastore.md) to be assigned manually when a workspace is provisioned. See Enabling a metastore to be automatically assigned to new workspaces. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Migrate Workflows to Non-Legacy Access Modes

New workspaces will be provisioned without support for [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md). If you plan to migrate any existing workflows to new workspaces created after the deadline, make sure they do not rely on this legacy access mode. See [Enabling admin protection for no isolation shared clusters](/concepts/no-isolation-shared-clusters-and-legacy-access.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Migrating Existing Workspaces to Unity Catalog

Though not required by the September 30, 2026 deadline, Databricks recommends migrating existing workspaces to Unity Catalog. The full upgrade guide covers: ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Upgrading Hive Tables and Views

Migrate Hive tables and views stored in the legacy Hive [Metastore](/concepts/metastore.md) to Unity Catalog. See Upgrading Hive tables and views to Unity Catalog. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Migrating Files Stored in DBFS

Move files stored in DBFS to [volumes](/concepts/ucvolumedataset.md) and [external locations](/concepts/external-location.md) managed by Unity Catalog. See Migrating files stored in DBFS to volumes and external locations. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Migrating Notebooks and Scripts

Update notebooks and scripts to reference Unity Catalog objects instead of legacy Hive [Metastore](/concepts/metastore.md) references. See Migrating notebooks and scripts. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Updating Jobs

Update jobs to work with Unity Catalog by ensuring they reference the correct catalog, schema, and table names. See [Updating jobs to work with Unity Catalog](/concepts/upgrading-jobs-to-unity-catalog.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Migrating to Supported Databricks Runtime Versions

Migrate to [supported Databricks Runtime versions](/concepts/databricks-ai-runtime-on-aws.md) (13.3 LTS or later) that are compatible with Unity Catalog. See Migrating to supported Databricks Runtime versions. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Migrating Compute to Unity Catalog Access Modes

Migrate compute resources to [Unity Catalog access modes](/concepts/unity-catalog-access-control-models.md) such as Shared access mode or Single user access mode. See Migrate compute to Unity Catalog access modes. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### Disabling Access to Legacy Features

After migration is complete, optionally [disable access to legacy features](/concepts/disable-legacy-features-setting.md) in your workspaces to prevent accidental re-use and enforce Unity Catalog as the sole data governance solution. See [Disabling access to legacy features in your workspaces](/concepts/disable-legacy-features-setting.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The unified data governance solution for Databricks.
- [Hive metastore](/concepts/built-in-hive-metastore.md) — The legacy metadata store being replaced by Unity Catalog.
- DBFS — The legacy file system being replaced by Unity Catalog volumes and external locations.
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) — A legacy cluster access mode being phased out.
- [Legacy features](/concepts/disable-legacy-features-setting.md) — Features that are disabled in new workspaces after September 30, 2026.
- Workspace provisioning — The process of creating new Databricks workspaces.
- [Metastore auto-assign](/concepts/metastore-admin-role-assignment.md) — Configuring Unity Catalog metastores to be automatically assigned to new workspaces.

## Sources

- migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md

# Citations

1. [migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md](/references/migrate-your-account-to-uc-only-workspaces-databricks-on-aws-222dccd3.md)
