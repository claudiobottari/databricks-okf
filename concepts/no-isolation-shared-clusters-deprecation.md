---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6c49958ee2c3f18d517a18c48e2febe1b7bafc95363b6a9afdf709dd8062ddd
  pageDirectory: concepts
  sources:
    - migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - no-isolation-shared-clusters-deprecation
    - NSCD
  citations:
    - file: migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
title: No-isolation shared clusters deprecation
description: No-isolation shared cluster access mode will not be available in new workspaces after September 30, 2026, requiring migration of compute to Unity Catalog access modes.
tags:
  - unity-catalog
  - clusters
  - compute
  - migration
timestamp: "2026-06-19T19:36:12.850Z"
---

# No-Isolation Shared Clusters Deprecation

**No-Isolation Shared Clusters Deprecation** refers to the planned removal of support for no-isolation shared clusters in new Databricks workspaces, effective September 30, 2026. This change is part of Databricks' broader migration toward [Unity Catalog](/concepts/unity-catalog.md)-only workspaces and the elimination of legacy features.

## Timeline

Starting **September 30, 2026**, all new workspaces will be provisioned without access to no-isolation shared clusters. Existing workspaces and their workflows are not impacted by this change. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## What Is Changing

New workspaces created after the deadline will not support no-isolation shared clusters as an access mode. This is one of several legacy features being removed, alongside [DBFS root and DBFS mounts](/concepts/dbfs-root-and-dbfs-mounts-deprecation.md), the [Hive metastore](/concepts/built-in-hive-metastore.md), and Databricks Runtime versions prior to 13.3 LTS. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Required Actions

### For Account Admins

To prepare for this change, admins must update their account-level workspace provisioning processes to remove dependency on no-isolation shared clusters. Key steps include:

- **Migrate workflows to non-legacy access modes**: If you plan to migrate any existing workflows to new workspaces created after September 30, 2026, ensure they do not rely on no-isolation shared clusters. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]
- **Review automation**: Adjust any CI/CD scripts and internal operational procedures for workspace creation that reference no-isolation shared clusters. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

### For Testing the New Behavior

If you want to test the new default behavior before the deadline, you can enable the **Disable legacy features** setting in your account console. This allows you to validate that your workflows function correctly without no-isolation shared clusters. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Migration Guidance

Databricks recommends migrating existing workspaces to [Unity Catalog](/concepts/unity-catalog.md) to take advantage of unified governance, enterprise-grade security, and advanced platform features. As part of this migration, you should:

- Migrate compute to Unity Catalog access modes — Replace no-isolation shared clusters with supported access modes.
- [Upgrade a Databricks workspace to Unity Catalog](/concepts/migrating-existing-workspaces-to-unity-catalog.md) — Follow the detailed guidance for upgrading Hive tables, migrating files, updating jobs, and disabling legacy features. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that replaces legacy metastores and access modes.
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) — The legacy cluster access mode being deprecated.
- [Enable admin protection for no isolation shared clusters](/concepts/no-isolation-shared-clusters.md) — Account-level controls for managing this access mode.
- [Disable access to legacy features in new workspaces](/concepts/disable-legacy-features-setting.md) — The account console setting for testing the new behavior.
- [Migrate your account to UC-only workspaces](/concepts/uc-only-workspaces.md) — The overarching migration guide.

## Sources

- migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md

# Citations

1. [migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md](/references/migrate-your-account-to-uc-only-workspaces-databricks-on-aws-222dccd3.md)
