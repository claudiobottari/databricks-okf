---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97784849e9e7ea8d4c46cb6708e0f50be318cfb2f4c9fa5a81c043d08aa3b8f1
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-vs-legacy-access-control-for-feature-store
    - UCVLACFFS
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Unity Catalog vs Legacy Access Control for Feature Store
description: Distinction between Unity Catalog-based privilege management and the older fine-grained permission model for workspaces not enabled for Unity Catalog
tags:
  - unity-catalog
  - migration
  - feature-store
  - comparison
timestamp: "2026-06-18T14:16:48.822Z"
---

# Unity Catalog vs Legacy Access Control for Feature Store

**Unity Catalog vs Legacy Access Control for Feature Store** describes the two distinct access control models available for managing permissions on feature tables in Databricks Feature Store. The choice between them depends on whether your workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md).

## Overview

Databricks Feature Store supports two access control paradigms. Workspaces not enabled for Unity Catalog use a legacy permission system with three fixed permission levels on feature table metadata. Workspaces enabled for Unity Catalog use Unity Catalog's standard privilege model, which provides a more granular and integrated governance framework. ^[access-control-legacy-databricks-on-aws.md]

## Legacy Access Control (Non-Unity Catalog Workspaces)

In workspaces not enabled for Unity Catalog, Feature Store access control grants fine-grained permissions on feature table metadata. You can control a user's ability to view a feature table in the UI, edit its description, manage other users' permissions on the table, and delete the table. ^[access-control-legacy-databricks-on-aws.md]

### Permission Levels

Legacy access control provides three permission levels for feature table metadata: ^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Abilities |
|-----------------|-----------|
| CAN VIEW METADATA | View the feature table in the UI |
| CAN EDIT METADATA | Edit the feature table's description |
| CAN MANAGE | Manage other users' permissions on the table and delete the table |

### Default Permissions

When a feature table is created, the following default permissions apply: ^[access-control-legacy-databricks-on-aws.md]

- The creator has CAN MANAGE permission
- Workspace admins have CAN MANAGE permission
- Other users have NO PERMISSIONS

### Configuring Permissions

**Per-table permissions:** On the feature table page, click the arrow to the right of the name and select **Permissions**. This option is only available if you have CAN MANAGE permission for the feature table. ^[access-control-legacy-databricks-on-aws.md]

**Global Feature Store permissions:** Workspace administrators can use the Feature Store UI to set permission levels on all feature tables for specific users or groups. Permissions set from the Feature Store page also apply to all future feature tables. ^[access-control-legacy-databricks-on-aws.md]

Permissions set on the Feature Store page can only be removed from that page. On the feature table page, you can override settings from the Feature Store page to add permissions, but you cannot set more restrictive permissions. When navigating to a specific feature table page, permissions set from the Feature Store page are marked "Some permissions cannot be removed because they are inherited." ^[access-control-legacy-databricks-on-aws.md]

## Unity Catalog Access Control

If your workspace is enabled for Unity Catalog, you should use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead of the legacy Feature Store permission system. Unity Catalog provides a unified governance model across all data assets, including feature tables. ^[access-control-legacy-databricks-on-aws.md]

Unity Catalog offers several advantages over the legacy system:

- **Unified governance:** Manage permissions for feature tables alongside other data assets (tables, views, models) using the same privilege model
- **Granular control:** Use standard SQL `GRANT` and `REVOKE` statements
- **Integration:** Permissions integrate with [ABAC GRANT Policies](/concepts/abac-grant-policies.md) and other Unity Catalog security features
- **Auditability:** Full audit logging through Unity Catalog's system tables

## Key Differences

| Aspect | Legacy Access Control | Unity Catalog |
|--------|----------------------|---------------|
| Permission levels | CAN VIEW METADATA, CAN EDIT METADATA, CAN MANAGE | Standard Unity Catalog privileges (e.g., SELECT, MODIFY, OWNERSHIP) |
| Configuration | Feature Store UI only | SQL statements, Catalog Explorer, REST API |
| Inheritance | Global Feature Store permissions apply to all tables | Standard catalog/schema inheritance model |
| Integration | Feature Store only | Unified across all data assets |
| Audit | Limited | Full audit logging via system tables |

## Migration Considerations

If you are migrating from a legacy workspace to a Unity Catalog-enabled workspace, you must reconfigure feature table permissions using Unity Catalog's privilege model. The legacy permission levels do not automatically translate to Unity Catalog privileges. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for Databricks
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The standard permission model for Unity Catalog
- [Feature Store](/concepts/feature-store.md) — The feature management platform
- [Feature Tables](/concepts/feature-tables.md) — The securable objects managed by these access control systems
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — Attribute-based access control policies in Unity Catalog

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
