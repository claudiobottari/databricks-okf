---
title: Migrate your account to UC-only workspaces | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/uc-only-migration
ingestedAt: "2026-06-18T08:04:59.344Z"
---

note

This page only applies to accounts created before December 18, 2025 that use legacy features. Accounts created after December 18, 2025 do not have access to legacy features.

Starting on September 30, 2026, all new workspaces will be provisioned with Unity Catalog and without access to certain legacy features. Existing workspaces and their workflows are not impacted. This page provides guidance for accounts with legacy workspaces on how to prepare for this change.

## What's changing[​](#whats-changing "Direct link to What's changing")

Starting September 30, 2026, new workspaces in all accounts will be provisioned without access to:

*   [DBFS root and DBFS mounts](https://docs.databricks.com/aws/en/dbfs/).
*   [Hive metastore](https://docs.databricks.com/aws/en/archive/external-metastores/external-hive-metastore).
*   [No-isolation shared clusters](https://docs.databricks.com/aws/en/admin/account-settings/no-isolation-shared).
*   Databricks Runtime versions prior to 13.3 LTS.

## What you need to do to prepare[​](#what-you-need-to-do-to-prepare "Direct link to What you need to do to prepare")

To prepare for this change, admins must update their account-level workspace provisioning process to remove dependency on legacy features. Additionally, Databricks recommends upgrading existing workspaces to Unity Catalog to take advantage of the new features and capabilities.

*   **Remove dependency on DBFS and the Hive metastore in workspace provisioning**
    
    If your organization uses automation for workspace provisioning, make sure the automation does not rely on legacy features. Adjust any CI/CD scripts and internal operational procedures for workspace creation processes that use DBFS root, DBFS mounts, or the Hive metastore.
    
    If you want to test the new default behavior before September 30, 2026, you can do so by enabling the **Disable legacy features** setting in your account console. See [Disable access to legacy features in new workspaces](https://docs.databricks.com/aws/en/admin/account-settings/legacy-features).
    
*   **Set metastores to auto-assign**
    
    Set a metastore to auto-assign for every region in which you deploy workspaces. Failure to do so requires a metastore to be assigned manually when a workspace is provisioned. See [Enable a metastore to be automatically assigned to new workspaces](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-metastore#auto-assign).
    
*   **Migrate workflows to non-legacy access modes**
    
    New workspaces will be provisioned without support for no-isolation shared clusters. If you plan to migrate any existing workflows to new workspaces created after September 30, 2026, make sure they do not rely on this legacy access mode. See [Enable admin protection for no isolation shared clusters in your account](https://docs.databricks.com/aws/en/admin/account-settings/no-isolation-shared).
    

## Migrate to Unity Catalog in existing workspaces[​](#migrate-to-unity-catalog-in-existing-workspaces "Direct link to migrate-to-unity-catalog-in-existing-workspaces")

Though not required by the September 30, 2026 deadline, Databricks recommends migrating existing workspaces to Unity Catalog to take advantage of unified governance, enterprise-grade security, and advanced platform features.

See [Upgrade a Databricks workspace to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/) for detailed guidance, including:

*   [Upgrading Hive tables and views to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/#hive-upgrade)
*   [Migrating files stored in DBFS to volumes and external locations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/#migrate-files)
*   [Migrating notebooks and scripts](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/#migrate-notebooks)
*   [Updating jobs to work with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/#jobs)
*   [Migrating to supported Databricks Runtime versions](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/#migrate-dbr)
*   [Migrate compute to Unity Catalog access modes](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/#migrate-access)
*   [Disabling access to legacy features in your workspaces](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/#disable-legacy)
