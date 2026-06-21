---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5acbbca4f6d06f9222c96faab0da80aa30c4c1d175d705801c7bc3fdb4bfe63b
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privileges-and-ownership
    - Ownership and Privileges
    - PAO
    - Privileges
    - Privileges and Ownership in Unity Catalog
    - privileges
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Privileges and Ownership
description: The traditional RBAC-style model controlling who can access what securable objects via grants and ownership in Unity Catalog.
tags:
  - unity-catalog
  - access-control
  - permissions
timestamp: "2026-06-18T10:36:19.946Z"
---

# Privileges and Ownership

**Privileges and ownership** form the foundational access control model in Unity Catalog, determining *who* can access *what* by using grants on securable objects. This model works alongside attribute-based access control (ABAC), table-level filtering and masking, and workspace-level restrictions to enforce secure, fine-grained access across your data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

The privileges and ownership model is built on a hierarchical object structure where permissions can be inherited from parent to child objects. Understanding this hierarchy is essential for designing an effective access control strategy. ^[access-control-in-unity-catalog-databricks-on-aws.md]

Unity Catalog organizes data into a three-level namespace: **catalog → schema → object** (such as tables, views, volumes, models, and functions). Privileges granted on a parent object are typically inherited by its children, though some privileges must be granted directly on the child object. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Key Concepts

### Securable Objects

Securable objects are the entities in Unity Catalog that can have privileges granted on them. The object hierarchy includes:

- **Metastore** — The top-level container for all metadata
- **Catalog** — A container for schemas
- **Schema** — A container for tables, views, volumes, models, functions, and other objects
- **Tables, Views, Volumes, Models, Functions** — Individual data and metadata objects

Privileges flow downward through this hierarchy. For example, granting a privilege on a catalog typically grants that privilege on all schemas and objects within that catalog. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Privileges

Privileges are permissions that control what actions a principal (user, group, or service principal) can perform on a securable object. Common privileges include:

- **`USE CATALOG`** and **`USE SCHEMA`** — Prerequisite permissions for accessing objects within a catalog or schema
- **`SELECT`** — Read data from a table or view
- **`MODIFY`** — Insert, update, or delete data
- **`CREATE`** — Create objects within a schema or catalog
- **`EXECUTE`** — Execute a function or model
- **`MANAGE`** — Full administrative control over the object, including granting privileges to others

Each privilege has a specific scope and behavior. For detailed descriptions of every privilege, see the Unity Catalog Privileges Reference. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Ownership

Every securable object in Unity Catalog has an **owner**. The owner has implicit full control over the object, including the ability to:

- Grant and revoke privileges on the object
- Alter or drop the object
- Transfer ownership to another principal

Ownership is typically assigned when the object is created. The creator of an object becomes its owner by default, unless another owner is specified. Ownership can be transferred using the `ALTER ... OWNER TO` SQL statement. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Privilege Inheritance

Privileges granted on a parent object are inherited by its child objects, unless explicitly overridden. This inheritance model simplifies administration by allowing you to grant broad access at the catalog or schema level rather than on individual objects. ^[access-control-in-unity-catalog-databricks-on-aws.md]

For example, granting `SELECT` on a catalog grants `SELECT` on all tables and views within all schemas in that catalog. However, some privileges (such as `CREATE` on a schema) are not inherited in the same way and must be granted at the appropriate level. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Managing Privileges

### Granting Privileges

Privileges are granted using the `GRANT` SQL statement or through Catalog Explorer. The basic syntax is:

```sql
GRANT privilege_type ON securable_type securable_name TO principal;
```

For example:

```sql
GRANT SELECT ON CATALOG sales TO `analysts`;
GRANT MODIFY ON SCHEMA sales.raw TO `data_engineers`;
GRANT EXECUTE ON MODEL system.ai.databricks-claude-sonnet-4-5 TO `data_scientists`;
```

^[access-control-in-unity-catalog-databricks-on-aws.md]

### Revoking Privileges

Privileges are revoked using the `REVOKE` SQL statement:

```sql
REVOKE privilege_type ON securable_type securable_name FROM principal;
```

Revoking a privilege on a parent object does not automatically revoke it on child objects if the privilege was granted directly on the child. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Viewing Privileges

Use `SHOW GRANTS` to view the privileges granted on a securable object:

```sql
SHOW GRANTS ON securable_type securable_name;
```

This shows all direct grants on the specified object. To see the effective privileges (including inherited grants), use the effective permissions API or Catalog Explorer. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Admin Roles

Unity Catalog defines several administrative roles with elevated privileges:

- **Account admin** — Manages the [Metastore](/concepts/metastore.md), workspaces, and account-level settings
- **Metastore admin** — Manages the [Metastore](/concepts/metastore.md) and its contents
- **Workspace admin** — Manages workspace-level settings and user access

These roles have broad privileges and should be assigned carefully. For detailed information, see the Admin Roles documentation. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Interaction with Other Access Control Models

Privileges and ownership work alongside other access control mechanisms:

- **[Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)** — ABAC policies dynamically grant privileges based on governed tags, complementing direct grants
- **[Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)** — These restrict data content within tables that users already have access to via privileges
- **[Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md)** — Restricts which workspaces can access specific catalogs

These models evaluate access at different levels and are designed to be used together. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Best Practices

- **Use groups for privilege management** — Grant privileges to groups rather than individual users to simplify administration. Adding or removing users from a group automatically updates their effective privileges. ^[access-control-in-unity-catalog-databricks-on-aws.md]
- **Grant at the appropriate level** — Grant privileges at the highest level that still provides the necessary access control. For example, grant `SELECT` on a schema rather than on individual tables when appropriate. ^[access-control-in-unity-catalog-databricks-on-aws.md]
- **Use ABAC for dynamic access** — For tag-based access control, use [ABAC GRANT Policies](/concepts/abac-grant-policies.md) instead of managing individual grants on each object. ^[access-control-in-unity-catalog-databricks-on-aws.md]
- **Audit privileges regularly** — Use `SHOW GRANTS` and the effective permissions API to review who has access to what, and revoke unnecessary privileges. ^[access-control-in-unity-catalog-databricks-on-aws.md]
- **Understand privilege inheritance** — Be aware that privileges on parent objects flow to children, which can lead to broader access than intended if not carefully managed. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that provides the privileges and ownership model
- Unity Catalog Privileges Reference — Detailed descriptions of every privilege
- Admin Roles — Account admin, [Metastore](/concepts/metastore.md) admin, and workspace admin roles
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — Attribute-based policies that dynamically grant privileges
- [Row Filter Policies](/concepts/row-filter-policies.md) — Table-level filters that restrict data content
- [Column Mask Policies](/concepts/column-mask-policies.md) — Column-level masks that protect sensitive data
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Restricting catalog access to specific workspaces

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
