---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df096cb60c9479954710b73f97eca1f20a254645e9a8e6469233a51a7e057b44
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-permissions-and-access-control
    - Access Control and Lineage Permissions
    - LPAAC
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Permissions and Access Control
description: Lineage visibility is governed by Unity Catalog's BROWSE permission on catalog objects and workspace-level permissions on notebooks, jobs, and dashboards, with cross-workspace masking.
tags:
  - security
  - access-control
  - unity-catalog
timestamp: "2026-06-19T18:04:59.149Z"
---

# Lineage Permissions and Access Control

**Lineage Permissions and Access Control** defines the authorization model that governs visibility of data lineage graphs in [Unity Catalog](/concepts/unity-catalog.md). The permission model for lineage is identical to the underlying Unity Catalog permission model: tables and other data objects registered in the [Metastore](/concepts/metastore.md) are visible only to users who have at least the `BROWSE` privilege on those objects. If a user lacks `BROWSE` or `SELECT` privilege on a table, they cannot explore its lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Requirements for Viewing Lineage

To view data lineage in Unity Catalog, the following permissions are required:

- At least the `BROWSE` privilege on the parent catalog of the table or view. The parent catalog must also be accessible from the workspace via [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- For notebooks, jobs, or dashboards, the user must have permissions on those workspace objects as defined by [access control lists](/concepts/table-access-control-databricks.md) (ACLs) in the workspace. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- For a Unity Catalog-enabled pipeline, the user must have `CAN VIEW` permission on the pipeline. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Additionally, tables must be registered in a Unity Catalog [Metastore](/concepts/metastore.md), and queries must use Spark DataFrame or Databricks SQL interfaces. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Permissions Model

### Table and Object Visibility

Lineage graphs display only those tables and data objects for which the user has at least `BROWSE` permission. For example, granting `SELECT` on a specific table (`lineage_data.lineagedemo.menu`) to `userA` allows that user to see the `menu` table in its lineage graph. However, associated tables that `userA` does not have permission to access (such as a downstream `dinner` table) appear as **masked** nodes. The user cannot expand the graph to reveal downstream tables from nodes they lack permission to access. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Granting `BROWSE` on a broader schema (e.g., `lineage_data`) allows the user to view the lineage graph for any table in that schema. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Workspace Object Granularity

Lineage can include links to workspace-level objects such as notebooks, jobs, dashboards, and queries. Detailed information about these objects (name, content) is visible only in the workspace where they were created. When a user views lineage from a different workspace attached to the same [Metastore](/concepts/metastore.md), these workspace objects are masked. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Users must have the appropriate ACL permissions on those workspace objects (e.g., read access on a notebook) to view detailed information. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Cross-Workspace Lineage Aggregation

Lineage is aggregated across all workspaces attached to a Unity Catalog [Metastore](/concepts/metastore.md). Lineage captured in one workspace is visible in any other workspace sharing that [Metastore](/concepts/metastore.md), provided the user has adequate object permissions. However, detailed information about notebooks, jobs, and dashboards in other workspaces is masked unless the user has explicit permissions on those objects. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Managing Permissions

To control access to lineage, administrators manage privileges on Unity Catalog securable objects (catalogs, schemas, tables) using standard [Unity Catalog Privilege Management](/concepts/unity-catalog-privilege-management.md). For workspace objects, administrators manage permissions through [access control lists](/concepts/table-access-control-databricks.md). The `BROWSE` privilege is the minimum required to see a table in the lineage graph; `SELECT` is not sufficient for lineage visibility. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of permission types (BROWSE, SELECT, MODIFY, etc.)
- BROWSE privilege — The minimum privilege required to see a table in the lineage graph
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI where lineage graphs are viewed
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Requirement for catalog accessibility
- System tables for lineage — Programmatic querying of lineage via `system.access.table_lineage` and `system.access.column_lineage`
- [Access control lists](/concepts/table-access-control-tacl.md) — Permissions for workspace objects like notebooks and jobs
- [Masked nodes in lineage](/concepts/lineage-permissions-and-masked-nodes.md) — How unauthorized tables appear in lineage graphs

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)
