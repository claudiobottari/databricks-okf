---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ed0953dae129a6007549e8379b8817140edf4c52a41b0f3d041f36f119d6e21
  pageDirectory: concepts
  sources:
    - migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - uc-only-workspaces
    - Migrate your account to UC-only workspaces
  citations:
    - file: migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
title: UC-only workspaces
description: New Databricks workspaces provisioned without legacy features such as DBFS root, Hive metastore, no-isolation shared clusters, and old Databricks Runtime versions.
tags:
  - unity-catalog
  - workspace-provisioning
  - migration
timestamp: "2026-06-19T19:36:06.276Z"
---

# UC-Only Workspaces

**UC-only workspaces** are Databricks workspaces that are provisioned with [Unity Catalog](/concepts/unity-catalog.md) enabled and without access to certain legacy features. Starting on **September 30, 2026**, all new workspaces in every account will be created in this mode. Existing workspaces and their workflows are not impacted by this change.^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

This page applies only to accounts created before December 18, 2025 that still use legacy features. Accounts created after that date do not have access to legacy features to begin with.^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## What’s Changing

Starting September 30, 2026, new workspaces will be provisioned **without** access to the following legacy features:^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

- [DBFS root](/concepts/dbfs-root-location.md) and DBFS mounts
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md)
- Databricks Runtime versions prior to 13.3 LTS

## Preparation Steps for Admins

To prepare for this change, admins must update their account-level workspace provisioning process to remove dependency on legacy features. Databricks recommends the following actions:^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### 1. Remove Dependency on DBFS and the Hive [Metastore](/concepts/metastore.md)

If your organization uses automation for workspace provisioning, ensure that the automation does not rely on DBFS root, DBFS mounts, or the Hive [Metastore](/concepts/metastore.md). Adjust any CI/CD scripts and internal operational procedures for workspace creation.^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

To test the new default behavior before September 30, 2026, you can enable the **Disable legacy features** setting in your account console. See [Disable access to legacy features in new workspaces](https://docs.databricks.com/aws/en/admin/account-settings/legacy-features).^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### 2. Set Metastores to Auto-Assign

Set a [Metastore](/concepts/metastore.md) to auto-assign for every region in which you deploy workspaces. Failure to do so requires a [Metastore](/concepts/metastore.md) to be assigned manually when a workspace is provisioned. See [Enable a [Metastore](/concepts/metastore.md) to be automatically assigned to new workspaces](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-metastore#auto-assign).^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### 3. Migrate Workflows to Non-Legacy Access Modes

New workspaces will be provisioned without support for no-isolation shared clusters. If you plan to migrate any existing workflows to new workspaces created after September 30, 2026, make sure they do not rely on this legacy access mode. See [Enable admin protection for no isolation shared clusters](https://docs.databricks.com/aws/en/admin/account-settings/no-isolation-shared).^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Migrate Existing Workspaces to Unity Catalog

Although not required by the September 30, 2026 deadline, Databricks recommends migrating existing workspaces to Unity Catalog to take advantage of unified governance, enterprise-grade security, and advanced platform features. Detailed guidance is available in the [Upgrade a Databricks workspace to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/) documentation, including:^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

- Upgrading Hive tables and views to Unity Catalog
- Migrating files stored in DBFS to volumes and external locations
- Migrating notebooks and scripts
- Updating jobs to work with Unity Catalog
- Migrating to supported Databricks Runtime versions
- Migrating compute to Unity Catalog access modes
- Disabling access to legacy features in your workspaces

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [DBFS root](/concepts/dbfs-root-location.md) and DBFS mounts
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md)
- Legacy features in Databricks

## Sources

- migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md

# Citations

1. [migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md](/references/migrate-your-account-to-uc-only-workspaces-databricks-on-aws-222dccd3.md)
