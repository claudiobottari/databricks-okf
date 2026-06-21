---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bab5bd025dea056819f4fb664603da87ac448d85ed808da5bbf6953994e37fe3
  pageDirectory: concepts
  sources:
    - managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
    - unity-catalog-permissions-model-concepts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - manage-privilege-in-unity-catalog
    - MPIUC
    - Manage Privileges in Unity Catalog
    - Manage privileges in Unity Catalog
    - Managing Privileges in Unity Catalog
    - Managing privileges in Unity Catalog
    - Privileges in Unity Catalog
    - privileges in Unity Catalog
    - ALL PRIVILEGES privilege
  citations:
    - file: unity-catalog-permissions-model-concepts-databricks-on-aws.md
title: MANAGE privilege in Unity Catalog
description: A Unity Catalog privilege that allows users to assign/revoke privileges, transfer ownership, and delete an object without being the owner
tags:
  - unity-catalog
  - access-control
  - privileges
timestamp: "2026-06-19T19:29:33.713Z"
---

# MANAGE privilege in Unity Catalog

The `MANAGE` privilege is a special administrative privilege in [Unity Catalog](/concepts/unity-catalog.md) that grants users the ability to manage access control, ownership, and deletion of a securable object without being the object's owner. It is designed to delegate governance tasks to users who need to administer objects but should not automatically receive all data‑access privileges. ^[unity-catalog-permissions-model-concepts-databricks-on-aws.md]

## Capabilities

A user or group granted the `MANAGE` privilege on an object can perform the following actions without owning the object:

- Grant and revoke privileges on the object.
- Transfer ownership of the object.
- Delete the object.

The `MANAGE` privilege does **not** automatically grant data‑access privileges (such as `SELECT`, `MODIFY`, or `READ VOLUME`). However, because users with `MANAGE` can grant privileges, they can explicitly grant themselves the data‑access privileges they need. ^[unity-catalog-permissions-model-concepts-databricks-on-aws.md]

## Inheritance

If `MANAGE` is granted on a container object (a catalog or a schema), the privilege cascades to all current and future child objects inside that container. For example, a user granted `MANAGE` on a catalog automatically receives `MANAGE` on every schema, table, view, volume, and function within that catalog. ^[unity-catalog-permissions-model-concepts-databricks-on-aws.md]

## Usage‑privilege requirements

To exercise the `MANAGE` privilege on an object, the user must also have the appropriate usage privileges on that object and on all parent container objects in the hierarchy. For instance:

- To use `MANAGE` on a schema, the user needs `USE SCHEMA` on the schema and `USE CATALOG` on the parent catalog.
- To use `MANAGE` on a table, the user needs `USE CATALOG` on the parent catalog, `USE SCHEMA` on the parent schema, and `MANAGE` on the table itself.

This requirement ensures that administrative actions still respect the boundary controls set by higher‑level administrators. ^[unity-catalog-permissions-model-concepts-databricks-on-aws.md]

## Comparison with Ownership

| Aspect | Ownership | `MANAGE` privilege |
|--------|-----------|--------------------|
| Predefined capabilities | Owner automatically has all capabilities on the object (without explicit `ALL PRIVILEGES` grant). | User has only the ability to manage privileges, ownership, and deletion; no automatic data‑access privileges. |
| Inheritance | Ownership does not inherit to child objects (but owners can manage all child objects). | `MANAGE` inherits to all child objects when granted on a container. |
| Data access | Owner implicitly has full data access on that object. | No implicit data access; user must explicitly grant themselves data privileges. |
| Usage privileges required | Owner does not need separate usage privileges on parent objects (implicit). | User must have `USE CATALOG` and `USE SCHEMA` on parent containers. |

^[unity-catalog-permissions-model-concepts-databricks-on-aws.md]

## Relationship with `ALL PRIVILEGES`

The `ALL PRIVILEGES` privilege does **not** include `MANAGE`. This is a deliberate safeguard to prevent accidental privilege escalation. A user or group granted `ALL PRIVILEGES` on an object can perform all standard operations (e.g., `SELECT`, `MODIFY`, `CREATE TABLE`) but cannot grant the `MANAGE` privilege or transfer ownership unless explicitly granted `MANAGE` separately. ^[unity-catalog-permissions-model-concepts-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md)
- [Privilege inheritance](/concepts/privilege-inheritance-hierarchy.md)
- [Ownership in Unity Catalog](/concepts/object-ownership-in-unity-catalog.md)
- [ALL PRIVILEGES privilege](/concepts/manage-privilege-in-unity-catalog.md)
- Usage privileges (USE CATALOG, USE SCHEMA)
- Container objects

## Sources

- unity-catalog-permissions-model-concepts-databricks-on-aws.md
- managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md

# Citations

1. [unity-catalog-permissions-model-concepts-databricks-on-aws.md](/references/unity-catalog-permissions-model-concepts-databricks-on-aws-8b967a7b.md)
