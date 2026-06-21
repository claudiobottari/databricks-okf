---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a436296b952bb6a96164bcc21978e9d3f3bddcf1549231b9a08c1331712a5d51
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-feature-store-access-control-vs-unity-catalog
    - LFSACVUC
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Legacy Feature Store Access Control vs Unity Catalog
description: "Databricks Feature Store offers two access control models: legacy fine-grained permissions for workspaces without Unity Catalog, and Unity Catalog privileges for workspaces with Unity Catalog enabled."
tags:
  - access-control
  - feature-store
  - unity-catalog
  - architecture
timestamp: "2026-06-19T17:24:22.611Z"
---

---

## Legacy Feature Store Access Control vs Unity Catalog

**Legacy Feature Store Access Control** refers to the permission model used for feature tables in Databricks workspaces **not** enabled for [Unity Catalog](/concepts/unity-catalog.md). Workspaces that **are** enabled for Unity Catalog must use Unity Catalog privileges instead. ^[access-control-legacy-databricks-on-aws.md]

---

## Legacy Access Control

Legacy Feature Store access control provides fine‑grained permissions on feature table **metadata** (not the underlying data). It controls a user's ability to view a feature table in the UI, edit its description, manage other users’ permissions, and delete the table. ^[access-control-legacy-databricks-on-aws.md]

### Permission Levels

Three permission levels are available for feature table metadata:

| Permission | Capabilities |
|------------|--------------|
| **CAN VIEW METADATA** | View the feature table in the UI. |
| **CAN EDIT METADATA** | Edit the table’s description and other metadata. |
| **CAN MANAGE** | Manage permissions of other users and delete the feature table. |

Any user can **create** a new feature table; the creator automatically receives CAN MANAGE. ^[access-control-legacy-databricks-on-aws.md]

### Default Permissions

When a feature table is first created:

- The creator has **CAN MANAGE** permission.
- Workspace admins have **CAN MANAGE** permission.
- All other users have **NO PERMISSIONS** (i.e., cannot see the table). ^[access-control-legacy-databricks-on-aws.md]

### Configuring Permissions

**Per feature table:**
1. On the feature table page, click the arrow next to the table name and select **Permissions** (requires CAN MANAGE on that table).
2. Edit permissions and click **Save**. ^[access-control-legacy-databricks-on-aws.md]

**Globally (all current and future feature tables in the workspace):**
- Workspace admins (or users with **CAN MANAGE** on the Feature Store itself) can set default permissions for all feature tables from the Feature Store **Permissions** button.
- These global permissions are **inherited** by each feature table and cannot be removed from the table’s own permissions page (they are marked “Some permissions cannot be removed because they are inherited”). However, additional permissions can be added per table. ^[access-control-legacy-databricks-on-aws.md]

> **Note:** Permissions set globally can only be removed from the Feature Store page, not from an individual feature table’s page. ^[access-control-legacy-databricks-on-aws.md]

---

## Unity Catalog

If a workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md), legacy Feature Store access control is **not** used. Instead, all feature table permissions are managed through Unity Catalog’s unified privilege model (e.g., `SELECT`, `MODIFY`, `OWNERSHIP` on tables and schemas). The source document does not describe Unity Catalog privileges in detail; for guidance, see the Databricks documentation on [Unity Catalog privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/). ^[access-control-legacy-databricks-on-aws.md]

---

## Key Differences

| Aspect | Legacy Feature Store | Unity Catalog |
|--------|---------------------|---------------|
| **Scope** | Feature table **metadata** only | Both metadata and underlying data (table objects) |
| **Permission levels** | `CAN VIEW METADATA`, `CAN EDIT METADATA`, `CAN MANAGE` | Standard SQL privileges: `SELECT`, `MODIFY`, `OWNERSHIP`, etc. |
| **Global defaults** | Workspace‑wide default permissions set via Feature Store UI | Catalog‑ or schema‑level default privileges (via `USE` grants) |
| **Inheritance** | Global permissions inherited and cannot be overridden per table | Privileges can be inherited from catalog/schema but can be overridden at table level |
| **Admin control** | Workspace admins always have CAN MANAGE on every table | Workspace admins become Unity Catalog [Metastore](/concepts/metastore.md) admins; granular ownership possible |

These differences stem from the fact that Unity Catalog is a full‑featured data governance solution, while legacy Feature Store access control is a simpler, metadata‑only permission system predating Unity Catalog. ^[access-control-legacy-databricks-on-aws.md]

---

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The modern data governance layer for Databricks.
- [Feature Store](/concepts/feature-store.md) — The service for managing and sharing feature tables.
- Access Control in Databricks — Overview of permission models.
- [Feature Table Permissions](/concepts/feature-table-permission-levels.md) — Detailed legacy permission reference.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
