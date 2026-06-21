---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f25d8e15608ac96654f215898ab4c5f21af1e2a047489347fb830ff3c7e0241
  pageDirectory: concepts
  sources:
    - migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbfs-root-and-dbfs-mounts-deprecation
    - DBFS mounts deprecation and DBFS root
    - DRADMD
    - DBFS root and DBFS mounts
  citations:
    - file: migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
title: DBFS root and DBFS mounts deprecation
description: DBFS root storage and DBFS mounts will no longer be available in new workspaces created after September 30, 2026, requiring migration of files to volumes and external locations.
tags:
  - unity-catalog
  - dbfs
  - storage
timestamp: "2026-06-19T19:36:13.718Z"
---

# DBFS Root and DBFS Mounts Deprecation

The **DBFS Root and DBFS Mounts Deprecation** refers to the planned removal of access to legacy DBFS root storage and DBFS mounts when provisioning new Databricks workspaces. This change is part of Databricks’ transition to Unity Catalog–only workspaces, which will no longer support certain legacy features. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Effective Date

Starting **September 30, 2026**, all new workspaces in every account will be provisioned **without access** to DBFS root and DBFS mounts. Existing workspaces and their workflows are **not** impacted by this change — only newly created workspaces after that date are affected. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Background

Accounts created before December 18, 2025 still have access to legacy features such as DBFS root and DBFS mounts. Accounts created after that date do not have legacy features at all. The deprecation effectively extends the post-December 18, 2025 default to all accounts for new workspace creation. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Other Deprecated Features

DBFS root and DBFS mounts are not the only features being removed. New workspaces after September 30, 2026 will also be provisioned without:

- [Hive metastore](/concepts/built-in-hive-metastore.md) (external Hive [Metastore](/concepts/metastore.md) support)
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md)
- Databricks Runtime versions prior to 13.3 LTS

^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Impact on Workspace Provisioning

If your organization uses automation (CI/CD scripts, internal operational procedures) for workspace provisioning, any process that relies on DBFS root, DBFS mounts, or the Hive [Metastore](/concepts/metastore.md) must be updated. After the deadline, new workspaces will not have these capabilities, so provisioning automation must assume they are absent. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Preparation Steps

### 1. Remove Dependency on DBFS in Provisioning

- Audit any workspace creation automation that creates or references DBFS root storage or DBFS mounts.
- Adjust scripts to use [Unity Catalog](/concepts/unity-catalog.md)–based storage (volumes, external locations) instead. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### 2. Migrate Existing Files

Databricks recommends migrating files currently stored in DBFS to Unity Catalog volumes and [external locations](/concepts/external-location.md). This ensures that workflows can continue to access those files in future workspaces. Detailed guidance is available in the [Upgrade a workspace to Unity Catalog](/concepts/workspace-catalog-unity-catalog.md) documentation. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### 3. Test the New Behavior Early

You can test the post-deprecation behavior before September 30, 2026 by enabling the **Disable legacy features** setting in the account console. This setting causes new workspaces to be provisioned without DBFS root, DBFS mounts, and other legacy features. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### 4. Set Metastores to Auto-Assign

For workspaces to function properly without the Hive [Metastore](/concepts/metastore.md), an auto-assign [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) must be configured for every region in which you deploy workspaces. If no [Metastore](/concepts/metastore.md) is auto-assigned, one must be manually assigned during provisioning. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Related Concepts

- DBFS – The legacy file system that is being deprecated for new workspaces.
- [Unity Catalog](/concepts/unity-catalog.md) – The modern governance framework that replaces DBFS and Hive [Metastore](/concepts/metastore.md).
- Unity Catalog volumes – Managed storage volumes for mounting files in Unity Catalog.
- [External locations](/concepts/external-location.md) – Paths to cloud storage that can be used with Unity Catalog.
- Hive metastore deprecation – Related change affecting Hive [Metastore](/concepts/metastore.md) access.
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) – Another legacy feature being removed.
- Workspace provisioning – The process affected by the deprecation.
- [Upgrade a workspace to Unity Catalog](/concepts/workspace-catalog-unity-catalog.md) – Migration guide for existing workspaces.

## Sources

- migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md

# Citations

1. [migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md](/references/migrate-your-account-to-uc-only-workspaces-databricks-on-aws-222dccd3.md)
