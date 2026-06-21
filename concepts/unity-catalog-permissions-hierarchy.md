---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: be517dc05c87a144d258b54e0ced80ab9013b6c4da39a290c74a24a1988b78be
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-permissions-hierarchy
    - UCPH
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Permissions Hierarchy
description: The object hierarchy and privilege inheritance model in Unity Catalog that governs how access flows from parent to child objects.
tags:
  - unity-catalog
  - permissions
  - hierarchy
  - privileges
timestamp: "2026-06-18T10:36:37.147Z"
---

# Unity Catalog Permissions Hierarchy

The Unity Catalog permissions hierarchy defines how access control flows through the object hierarchy in Unity Catalog, from the [Metastore](/concepts/metastore.md) down to individual securable objects. Understanding this hierarchy is essential for designing effective access control strategies and troubleshooting permission issues.

## Object Hierarchy

Unity Catalog organizes data assets in a three-level namespace: **catalog → schema → object** (such as tables, views, volumes, models, and functions). Permissions are inherited downward through this hierarchy, meaning a privilege granted on a parent object applies to all child objects unless explicitly overridden. ^[access-control-in-unity-catalog-databricks-on-aws.md]

The hierarchy from top to bottom is:

1. **Metastore** — The top-level container for all metadata and access control policies
2. **Catalog** — A logical container for schemas
3. **Schema** — A logical container for data objects
4. **Securable objects** — Tables, views, volumes, models, functions, and other data assets

## Privilege Inheritance

Privileges flow from parent to child objects. When you grant a privilege on a catalog, all schemas and objects within that catalog inherit that privilege. Similarly, a grant on a schema applies to all objects within that schema. ^[access-control-in-unity-catalog-databricks-on-aws.md]

This inheritance model means that granting `USE CATALOG` on a catalog and `USE SCHEMA` on a schema provides the prerequisite access needed to reach objects within that schema. Additional privileges like `SELECT`, `EXECUTE`, or `MODIFY` can then be granted at the object level or inherited from parent scopes. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Access Control Models

Unity Catalog uses several complementary access control models that work together within the permissions hierarchy:

### Privileges and Ownership

The traditional grant-based model controls *who* can access *what* using `GRANT` and `REVOKE` statements on securable objects. Ownership provides additional control, as object owners have implicit privileges on their objects. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Attribute-Based Access Control (ABAC)

Unity Catalog ABAC uses governed tags and centralized policies to dynamically control access based on object attributes. [GRANT Policies](/concepts/grant-policies-beta.md) are a type of ABAC policy that can be attached at the catalog or schema level and conditionally grant privileges based on tag values. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Row Filters and Column Masks

[Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md) control what data users can see within tables. These are applied at the table level and use user-defined functions (UDFs) to implement filtering or masking logic. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Workspace-Level Restrictions

[Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) restricts which workspaces can access specific catalogs, external locations, and storage credentials. This controls *where* users can access data. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## When to Use Each Mechanism

Databricks recommends using attribute-based access control (ABAC) to centralize and scale access control based on governed tags. Use row filters and column masks only when you need per-table logic or haven't adopted ABAC yet. ^[access-control-in-unity-catalog-databricks-on-aws.md]

The following table compares the access control mechanisms across common criteria:

| Mechanism | Controls | Level | Best For |
|---|---|---|---|
| Privileges and ownership | Who can access what | Object, schema, catalog | Basic access control |
| ABAC policies | What data users can access | Catalog, schema | Dynamic, tag-based access |
| Row filters/column masks | What data users see | Table | Per-table data masking |
| Workspace bindings | Where users can access | Catalog | Workspace isolation |

## Effective Permissions

The effective permissions on any securable object are the union of:

- Direct grants on the object itself
- Inherited grants from parent schemas and catalogs
- Privileges granted through group membership
- Privileges from applicable [GRANT Policies](/concepts/grant-policies-beta.md) (if any)
- Administrative privileges (such as [Metastore](/concepts/metastore.md) admin or object ownership)

To determine effective permissions, use `SHOW GRANTS` for direct grants and `SHOW EFFECTIVE POLICIES` for ABAC policy grants. The effective permissions API (`GET /api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}`) returns the union of direct and inherited grants. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Prerequisite Permissions

To access any securable object, a principal must have the prerequisite permissions on ancestor objects:

- `USE CATALOG` on the parent catalog
- `USE SCHEMA` on the parent schema

These permissions do not grant any data access themselves but are required to navigate the hierarchy and reach the target object. They must be granted directly and are not covered by [GRANT Policies](/concepts/grant-policies-beta.md). ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Best Practices

- **Grant at the highest appropriate level** to minimize the number of grant statements and simplify management.
- **Use groups for principal management** rather than individual users to simplify permission changes.
- **Combine privilege grants with ABAC policies** for fine-grained, dynamic access control.
- **Audit effective permissions regularly** using `SHOW GRANTS` and `SHOW EFFECTIVE POLICIES` to ensure access is as intended.
- **Use workspace bindings** to isolate data access to specific workspaces when needed.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that implements this hierarchy
- Unity Catalog ABAC — Attribute-based access control within Unity Catalog
- [GRANT Policies](/concepts/grant-policies-beta.md) — Dynamic, tag-based privilege grants
- [Row Filter Policies](/concepts/row-filter-policies.md) — Table-level data filtering
- [Column Mask Policies](/concepts/column-mask-policies.md) — Table-level data masking
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Workspace-level access restrictions
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of available privileges

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
