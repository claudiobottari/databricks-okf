---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fad2c799717d8830d384cbef01a2b19ac110b96b3f56f03d1f511b3439f5a5c6
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-permissions-and-masked-nodes
    - Masked Nodes and Lineage Permissions
    - LPAMN
    - Masked nodes in lineage
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Permissions and Masked Nodes
description: Access control model where lineage visibility is governed by Unity Catalog BROWSE/SELECT privileges, and unauthorized tables appear as masked nodes in the lineage graph.
tags:
  - unity-catalog
  - permissions
  - lineage
timestamp: "2026-06-18T11:29:25.158Z"
---

# Lineage Permissions and Masked Nodes

**Lineage Permissions and Masked Nodes** describes how Unity Catalog's data lineage visualization respects existing access controls by hiding or masking lineage information for tables and workspace objects that a user does not have permission to view. This ensures that the lineage graph does not leak information about data assets or workflows the user is not authorized to see. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## How Permissions Control Lineage Visibility

Lineage graphs in Unity Catalog share the same permission model as the underlying Unity Catalog securable objects. A user can see a table or other data object in the lineage graph only if they have at least the `BROWSE` permission on that object's parent catalog. If a user lacks `BROWSE` or `SELECT` on a table, they cannot explore its lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Lineage is aggregated across all workspaces attached to a Unity Catalog [Metastore](/concepts/metastore.md). This means lineage captured in one workspace is visible from any other workspace that shares that [Metastore](/concepts/metastore.md) — but only if the user has adequate object permissions. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Masked Nodes

When a user views a lineage graph but does not have permission to see certain connected tables, those tables appear as **masked nodes**. A masked node shows that a connection exists but does not reveal the table's name, details, or further lineage relationships. The user cannot expand the graph from a masked node to see downstream dependencies. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Example

Consider a user `userA` who has been granted `SELECT` on `lineage_data.lineagedemo.menu` but not on the downstream table `lineage_data.lineagedemo.dinner`. When `userA` views the lineage graph for `menu`, the `dinner` table appears as a masked node. `userA` can see that some connection exists but cannot view the table's identity or explore its downstream lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

By contrast, `userB` who has been granted the broader `BROWSE` permission on the entire `lineage_data` schema can view the full lineage graph for any table in that schema, including all connected tables as regular (unmasked) nodes. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### SQL Example

The following SQL statements illustrate how different permission grants affect lineage visibility:

```sql
-- userA only has SELECT on a specific table
GRANT USE SCHEMA on lineage_data.lineagedemo TO `userA@company.com`;
GRANT SELECT on lineage_data.lineagedemo.menu TO `userA@company.com`;

-- userB has BROWSE on the schema, granting visibility to all tables
GRANT BROWSE on lineage_data TO `userB@company.com`;
```

After these grants, `userA` sees the `menu` table in the lineage graph but the `dinner` table appears as masked. `userB` sees both tables normally. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Cross-Workspace Masking

Lineage data is aggregated across all workspaces attached to a Unity Catalog [Metastore](/concepts/metastore.md). However, detailed information about **workspace-level objects** such as notebooks, jobs, and dashboards from other workspaces is masked. A user can see that such an object exists as a consumer or producer in the lineage graph, but cannot view the object's name, details, or other identifying information unless the object was created in their current workspace. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

To view detailed information about workspace objects (notebooks, jobs, dashboards), users must also have the appropriate permissions on those objects as defined by the workspace's access control settings. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Requirements for Viewing Lineage

To view data lineage in Catalog Explorer: ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

- You must have at least the `BROWSE` privilege on the parent catalog of the table or view.
- The parent catalog must be accessible from the workspace (see [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md)).
- For notebooks, jobs, or dashboards, you must have permissions on these objects as defined by the workspace's access control settings.
- For a Unity Catalog-enabled pipeline, you must have `CAN VIEW` permission on the pipeline.

## Use Cases

### Impact Analysis with Access Restrictions

When planning to change or delete a table, a user can see downstream dependencies only if they have permission to view those downstream assets. Masked nodes indicate dependencies that exist but that the user cannot investigate further, which may require escalating permissions or consulting with another team. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Sensitive Data Flow Tracking

For compliance audits, administrators with appropriate `BROWSE` permissions can trace where regulated data originates, how it is transformed, and which downstream assets consume it. Users without those permissions see masked nodes, preventing unauthorized discovery of sensitive data flows. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Best Practices

- **Grant `BROWSE` at the schema or catalog level** for users who need to perform impact analysis across multiple tables, rather than granting it per-table. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Use `BROWSE` carefully on sensitive schemas** — it allows users to discover the existence of all tables in that schema, even if they cannot read the data. Consider whether masked-node behavior provides sufficient protection or whether the schema itself should remain hidden. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Audit workspace object visibility separately** — lineage for notebooks, jobs, and dashboards is governed by workspace access controls, not Unity Catalog permissions alone.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that provides the lineage permission model
- [Data Lineage](/concepts/data-lineage.md) — The broader concept of tracking data origins and transformations
- BROWSE Permission — The Unity Catalog privilege that controls lineage visibility
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Controls which catalogs are accessible from a workspace
- [External Lineage](/concepts/external-lineage.md) — Extends the lineage graph to external assets outside Databricks
- Table Insights — Usage trends and popularity data visible in Catalog Explorer

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)
