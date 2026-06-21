---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5da3f234e1955e6f3ec29a5c0369e1116fb864c44b7cb5c41bf839408dbd0e86
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privilege-hierarchy-and-inheritance
    - Inheritance and Privilege Hierarchy
    - PHAI
    - Privilege Hierarchy
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
    - file: hive-metabestore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Privilege Hierarchy and Inheritance
description: The hierarchical inheritance of privileges where granting on CATALOG cascades to all schemas and their objects, and DENY on a parent hides objects from listing.
tags:
  - databricks
  - authorization
  - hierarchical
timestamp: "2026-06-19T10:48:17.400Z"
---

# Privilege Hierarchy and Inheritance

**Privilege Hierarchy and Inheritance** refers to the cascading permission model used by the legacy Databricks Hive [Metastore](/concepts/metastore.md), where granting or denying a privilege on a higher-level securable object automatically applies that privilege to all nested objects below it.

## Overview

When table access control is enabled on a workspace and on all clusters, SQL objects in Databricks follow a hierarchical structure. Privileges are inherited downward through this hierarchy. This means that a privilege granted or denied on a `CATALOG` automatically applies to all schemas within that catalog, and privileges granted on a schema apply to all objects within that schema. This inheritance pattern holds true for all securable objects. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Securable Object Hierarchy

The Hive [Metastore](/concepts/metastore.md) defines the following hierarchy of securable objects: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- **CATALOG**: Controls access to the entire data catalog.
  - **SCHEMA**: Controls access to a schema.
    - **TABLE**: Controls access to a managed or external table.
    - **VIEW**: Controls access to SQL views.
    - **FUNCTION**: Controls access to a named function.

Additionally, there are two standalone securable objects that do not fit within the catalog-schema hierarchy: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- **ANONYMOUS FUNCTION**: Controls access to anonymous or temporary functions (not supported in Databricks SQL).
- **ANY FILE**: Controls access to the underlying filesystem. Users granted access to `ANY FILE` can bypass restrictions on catalogs, schemas, tables, and views by reading from the filesystem directly.

## Inheritance in Practice

The inheritance mechanism simplifies access control management. For example, granting a user `SELECT` on the `CATALOG` automatically gives them read access to all schemas, tables, views, and functions within that catalog. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

If you deny a user privileges on a table, that user cannot see the table when listing all tables in the schema. Similarly, if you deny a user privileges on a schema, the user cannot see that the schema exists when listing all schemas in the catalog. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## The `USAGE` Privilege Requirement

To perform any action on a schema object, a user must have the `USAGE` privilege on that schema, in addition to the privilege required for the specific action. The `USAGE` requirement can be satisfied by any of the following: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- Being a workspace admin
- Having the `USAGE` privilege on the schema (or being in a group that has it)
- Having the `USAGE` privilege on the `CATALOG` (or being in a group that has it)
- Being the owner of the schema (or being in a group that owns it)

Even the owner of an object inside a schema must have the `USAGE` privilege in order to use it. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Object Ownership

When table access control is enabled, the user who creates a schema, table, view, or function becomes its owner. The owner is granted all privileges and can grant privileges to other users. Groups may also own objects, in which case all members of that group are considered owners. Ownership can be transferred using the `ALTER <object> OWNER TO` command by either the current owner or a workspace admin. ^[hive-metabestore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

When table access control is disabled, owners are not registered upon object creation, and a workspace admin must assign an owner using the `ALTER <object> OWNER TO` command. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Types

The Hive [Metastore](/concepts/metastore.md) defines the following privilege types: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

| Privilege | Description |
|-----------|-------------|
| `SELECT` | Read access to an object |
| `CREATE` | Ability to create an object (e.g., a table in a schema) |
| `MODIFY` | Ability to add, delete, and modify data in an object |
| `USAGE` | Required to perform any action on a schema object |
| `READ_METADATA` | Ability to view an object and its metadata |
| `CREATE_NAMED_FUNCTION` | Ability to create a named UDF in an existing catalog or schema |
| `MODIFY_CLASSPATH` | Ability to add files to the Spark class path (not supported in Databricks SQL) |
| `ALL PRIVILEGES` | All the above privileges |

## Managing Privileges

Privileges are managed using SQL commands with the syntax: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

```sql
GRANT privilege_type ON securable_object TO principal
```

Where `principal` is a user, service principal, or group. To grant a privilege to all users in a workspace, grant it to the `users` group. Privileges can also be managed programmatically using the Databricks Terraform provider and the `databricks_sql_permissions` resource. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Comparison with Unity Catalog

This privilege model is specific to the legacy Hive [Metastore](/concepts/metastore.md) built into each Databricks workspace. [Unity Catalog](/concepts/unity-catalog.md) uses a different model for granting privileges. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Related Concepts

- [Table Access Control](/concepts/table-access-control-tacl.md) — The security framework that enables privilege management
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — The legacy metadata store for Databricks workspaces
- Unity Catalog Privileges Reference — The privilege model for Unity Catalog
- Dynamic Views — Views that use functions like `current_user()` and `is_member()` for fine-grained permissions
- Data Governance on Databricks — Overall data security and access control strategies

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
2. hive-metabestore-privileges-and-securable-objects-legacy-databricks-on-aws.md
