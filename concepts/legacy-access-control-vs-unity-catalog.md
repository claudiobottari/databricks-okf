---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc70986cf601deeba43d32ef9500c20c4ce971d88a0826a2f008b29fd4871aab
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-access-control-vs-unity-catalog
    - LACVUC
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Legacy Access Control vs Unity Catalog
description: The access control model described applies only to Databricks workspaces not enabled for Unity Catalog; Unity Catalog-enabled workspaces use Unity Catalog privileges instead.
tags:
  - databricks
  - feature-store
  - access-control
  - unity-catalog
timestamp: "2026-06-19T13:51:17.720Z"
---

# Legacy Access Control vs Unity Catalog

**Legacy Access Control vs Unity Catalog** compares the two permission systems available for managing access to [Feature Store](/concepts/feature-store.md) resources on Databricks. The choice between them depends on whether a workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md).

## Overview

Databricks provides two distinct approaches to controlling access to feature tables: the legacy Feature Store access control system and the Unity Catalog privileges system. Workspaces not enabled for Unity Catalog use the legacy system, while Unity Catalog-enabled workspaces use the standard [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md).^[access-control-legacy-databricks-on-aws.md]

## Legacy Access Control

Legacy access control is available in workspaces that are **not** enabled for Unity Catalog. It provides fine-grained permissions specifically on feature table metadata.^[access-control-legacy-databricks-on-aws.md]

### Permission Levels

The legacy system offers three permission levels for feature table metadata:^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Abilities |
|-----------------|-----------|
| **CAN VIEW METADATA** | View a feature table in the UI |
| **CAN EDIT METADATA** | Edit feature table descriptions |
| **CAN MANAGE** | Manage other users' permissions and delete the table |

### Default Permissions

When a feature table is created in the legacy system:^[access-control-legacy-databricks-on-aws.md]

- The creator receives **CAN MANAGE** permission
- Workspace admins receive **CAN MANAGE** permission
- All other users receive **NO PERMISSIONS**

Any user can create a new feature table.^[access-control-legacy-databricks-on-aws.md]

### Configuring Permissions

**Per-Feature Table:** Users with CAN MANAGE permission can configure permissions by clicking the arrow next to the feature table name and selecting **Permissions**.^[access-control-legacy-databricks-on-aws.md]

**Global Feature Store Permissions:** Workspace administrators can set permission levels on all feature tables (current and future) from the Feature Store page's **Permissions** button. Permissions set at this level can only be removed from that page, and individual feature table pages cannot set more restrictive permissions—only add to them.^[access-control-legacy-databricks-on-aws.md]

## Unity Catalog Access Control

For workspaces enabled with Unity Catalog, access control uses [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead of the legacy Feature Store system. This provides a unified governance model across all data assets, including feature tables, models, and other catalog objects.^[access-control-legacy-databricks-on-aws.md]

Unity Catalog privileges follow standard SQL-based permission models (such as `SELECT`, `MODIFY`, `OWNERSHIP`) applied to securable objects in the [Metastore](/concepts/metastore.md) hierarchy (catalog → schema → table). Feature tables become governed under the same framework as other tables and views, simplifying administration.

## Key Differences

| Aspect | Legacy Access Control | Unity Catalog |
|--------|----------------------|---------------|
| **Workspace requirement** | Workspace not enabled for Unity Catalog | Workspace enabled for Unity Catalog |
| **Permission model** | Feature Store-specific (CAN VIEW METADATA, CAN EDIT METADATA, CAN MANAGE) | Standard Unity Catalog privileges |
| **Scope** | Feature table metadata only | All governed data assets |
| **Granularity** | Feature table level | Catalog, schema, and table level |
| **Management** | Feature Store UI | Unity Catalog UI, SQL commands, or APIs |

## Migration Considerations

When migrating from legacy access control to Unity Catalog:^[access-control-legacy-databricks-on-aws.md]

- Existing feature table permissions in the legacy system do **not** automatically transfer to Unity Catalog
- Administrators must grant Unity Catalog privileges on the corresponding tables after migration
- Any user who could create feature tables in the legacy system must be granted appropriate creation privileges under Unity Catalog

## Related Concepts

- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) — The standard permission system for Unity Catalog-enabled workspaces
- [Feature Store](/concepts/feature-store.md) — The resource governed by both access control systems
- Data Governance on Databricks — Broader governance strategies across data assets
- [Workspace Administration](/concepts/workspace-admin-unity-catalog.md) — Role responsible for configuring both permission systems

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
