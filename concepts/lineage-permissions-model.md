---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16e6d5296f999e5e3972fb7ec22df4fc60401b952153c476ac815ef1a0dd1539
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-permissions-model
    - LPM
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Permissions Model
description: Access control for lineage data requiring BROWSE privilege on catalog objects and workspace-level permissions on notebooks, jobs, and dashboards, with masked nodes for unauthorized objects.
tags:
  - security
  - permissions
  - unity-catalog
timestamp: "2026-06-19T09:41:39.018Z"
---

# Lineage Permissions Model

The **Lineage Permissions Model** governs which users can view data lineage information in [Unity Catalog](/concepts/unity-catalog.md). It determines the visibility of tables, notebooks, jobs, and dashboards in lineage graphs, ensuring that users can only see lineage connections for objects they have permission to access. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Core Principle

Lineage graphs share the same permission model as Unity Catalog. Tables and other data objects registered in the Unity Catalog [Metastore](/concepts/metastore.md) are visible only to users who have at least `BROWSE` permissions on those objects. If a user does not have the `BROWSE` or `SELECT` privilege on a table, they cannot explore its lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Required Privileges

### Table and Data Object Permissions

To view lineage for a table or view, a user must have at least the `BROWSE` privilege on the parent catalog of that object. The parent catalog must also be accessible from the workspace (see [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md)). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Example: Granting `BROWSE` on a catalog allows a user to view lineage for any table within that catalog: ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

```sql
GRANT BROWSE on lineage_data to `userB@company.com`;
```

### Workspace Object Permissions

For notebooks, jobs, or dashboards, users must have permissions on these objects as defined by the access control settings in the workspace. For detailed information about managing access to these workspace-level objects, see [Access control lists](/concepts/table-access-control-tacl.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Pipeline Permissions

For a Unity Catalog-enabled pipeline, users must have `CAN VIEW` permission on the pipeline. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Masked Nodes

When a user does not have sufficient permissions on an upstream or downstream table, that table appears as a **masked node** in the lineage graph. For example: ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

```sql
GRANT USE SCHEMA on lineage_data.lineagedemo to `userA@company.com`;
GRANT SELECT on lineage_data.lineagedemo.menu to `userA@company.com`;
```

In this case, `userA` sees the `menu` table but cannot see information about associated tables such as the downstream `lineage_data.lineagedemo.dinner` table. The `dinner` table appears as a masked node, and `userA` cannot expand the graph to reveal downstream connections from tables they do not have permission to access. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Cross-Workspace Visibility

Lineage is aggregated across all workspaces attached to a Unity Catalog [Metastore](/concepts/metastore.md). This means lineage captured in one workspace is visible in any other workspace that shares that [Metastore](/concepts/metastore.md), as long as the user has adequate object permissions. However, detailed information about workspace-level objects (such as notebooks and dashboards) from other workspaces is masked. Detailed information about these objects is visible only in the workspace where they were created. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The broader permission system that underpins lineage visibility.
- BROWSE Privilege — The minimum privilege needed to see object lineage.
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Controls which catalogs are accessible from a workspace.
- [Access control lists](/concepts/table-access-control-tacl.md) — Manages permissions for workspace objects like notebooks and dashboards.
- Manage privileges in Unity Catalog — Guide for granting and managing permissions.

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)
