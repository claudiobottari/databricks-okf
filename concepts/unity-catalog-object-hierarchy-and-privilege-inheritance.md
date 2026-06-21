---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d32ce7a9fd65da9217036ec7bcdca9464dd8785d0ebf6d3457a947c0284d0ea
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-object-hierarchy-and-privilege-inheritance
    - Privilege Inheritance and Unity Catalog Object Hierarchy
    - UCOHAPI
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Object Hierarchy and Privilege Inheritance
description: The hierarchical structure of securable objects in Unity Catalog where privileges flow from parent to child objects.
tags:
  - unity-catalog
  - object-hierarchy
  - permissions
timestamp: "2026-06-19T21:55:35.389Z"
---



# [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md) and Privilege Inheritance

The **Unity Catalog Object Hierarchy and Privilege Inheritance** model defines how permissions flow between securable objects in Databricks Unity Catalog. Understanding this hierarchy is fundamental to implementing effective access control in any Unity Catalog-managed environment.

## Object Hierarchy

Unity Catalog organizes data assets into a strict four-level hierarchy:

1. **Metastore** – The top-level container that holds all metadata and manages access for the entire account.
2. **Catalog** – A logical grouping of schemas, tables, views, volumes, and other objects within a single [Metastore](/concepts/metastore.md).
3. **Schema** – A namespace within a catalog that contains tables, views, functions, and other database objects.
4. **Objects** – The actual data assets (tables, views, volumes, functions, etc.) and their underlying storage credentials, external locations, and connections.

^[access-control-in-unity-catalog-databricks-on-aws.md]

This hierarchy is enforced at the [Metastore](/concepts/metastore.md) level, which manages access across the entire account, down to individual objects within schemas.

## Privilege Inheritance

Privileges in Unity Catalog are **inherited from parent objects to child objects**. When a privilege is granted on a parent object (such as a catalog), that privilege automatically applies to all child objects (such as schemas and tables) within that parent, unless an explicit deny or more restrictive privilege overrides it at the child level.

^[access-control-in-unity-catalog-databricks-on-aws.md]

The inheritance model works as follows:

- **Metastore-level privileges** flow down to all catalogs within the [Metastore](/concepts/metastore.md).
- **Catalog-level privileges** flow down to all schemas within the catalog.
- **Schema-level privileges** flow down to all tables, views, and functions within the schema.

^[access-control-in-unity-catalog-databricks-on-aws.md]

### Inheritance Example

If a user is granted `SELECT` privilege on a catalog, they automatically have `SELECT` access on all tables and views within every schema in that catalog. To restrict access, you must either:
- Remove the privilege at the catalog level and grant it only on specific schemas or tables.
- Use row filters and column masks for fine-grained control.

^[access-control-in-unity-catalog-databricks-on-aws.md]

### Inheritance and Object Ownership

Object ownership plays a key role in privilege inheritance. The owner of a securable object can grant privileges on that object to other users or groups. Ownership can be transferred, but the original owner retains the ability to manage the object's permissions until ownership is explicitly changed.

^[access-control-in-unity-catalog-databricks-on-aws.md]

## Key Principles

1. **Privilege propagation** – Privileges granted on a parent object are automatically propagated to all current and future child objects.
2. **No automatic revocation** – Revoking a privilege from a parent does not automatically revoke it from child objects if the child was granted the privilege independently. Separate `REVOKE` statements are required at the child level.
3. **Inheritance is unidirectional** – Privileges only flow from parent to child, not from child to parent or between siblings.

^[access-control-in-unity-catalog-databricks-on-aws.md]

## Practical Implications

When designing access controls:
- **Grant at the highest necessary level** to minimize administrative overhead. For broad data access, grant on the catalog rather than on individual tables.
- **Grant at the lowest necessary level** for security-sensitive data. Use schema- or table-level grants to limit exposure.
- **Use schema-level grants** as a balance between simplicity and control.

^[access-control-in-unity-catalog-databricks-on-aws.md]

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- Privileges in Unity Catalog
- [Metastore](/concepts/metastore.md)
- [Catalog](/concepts/unity-catalog.md)
- Schema
- Securable Objects
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)
- [Data Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md)

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
