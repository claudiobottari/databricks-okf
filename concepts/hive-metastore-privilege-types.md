---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78c18d3b6a991d85dd31c4b227f43a8b9a0f7cef8c73732801b51c7bea5d1130
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-privilege-types
    - HMPT
    - Hive Metastore Privileges
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Hive Metastore Privilege Types
description: The set of privileges (SELECT, CREATE, MODIFY, USAGE, READ_METADATA, CREATE_NAMED_FUNCTION, MODIFY_CLASSPATH, ALL PRIVILEGES) used with legacy Hive metastore access control.
tags:
  - hive-metastore
  - data-governance
  - sql-privileges
timestamp: "2026-06-19T19:04:30.896Z"
---

# Hive [Metastore](/concepts/metastore.md) Privilege Types

**Hive [Metastore](/concepts/metastore.md) Privilege Types** define the access control permissions available for data objects managed by the legacy Databricks Hive [Metastore](/concepts/metastore.md). These privileges are used with SQL commands (`GRANT`, `REVOKE`, `DENY`) and apply only when [Table Access Control](/concepts/table-access-control-tacl.md) is enabled in the workspace and on the cluster or SQL warehouse. Databricks also supports a separate privilege model for [Unity Catalog](/concepts/unity-catalog.md).^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Requirements

- A workspace administrator must [enable and enforce table access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl#enable-table-acl-workspace) for the workspace.
- The cluster or SQL warehouse must be enabled for [table access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl#table-access-control).

> **Note:** Data access control is *always enabled* in Databricks SQL even if table access control is not enabled for the workspace. However, if table access control is enabled and you have already specified ACLs (granted and denied privileges) in the workspace, those ACLs are respected in Databricks SQL.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Types

The following privilege types can be granted on [Securable Objects in the Hive Metastore](/concepts/hive-metastore-privileges-and-securable-objects.md):

- **`SELECT`** — gives read access to an object.
- **`CREATE`** — gives ability to create an object (for example, a table in a schema).
- **`MODIFY`** — gives ability to add, delete, and modify data to or from an object.
- **`USAGE`** — does not give any abilities by itself, but is an additional requirement to perform any action on a schema object (see [#Usage privilege](/concepts/usage-privilege-requirement.md)).
- **`READ_METADATA`** — gives ability to view an object and its metadata.
- **`CREATE_NAMED_FUNCTION`** — gives ability to create a named UDF in an existing catalog or schema.
- **`MODIFY_CLASSPATH`** — gives ability to add files to the Spark class path. (Supported only in non–Databricks SQL environments.)
- **`ALL PRIVILEGES`** — grants all of the above privileges simultaneously.

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

> **Note:** `MODIFY_CLASSPATH` is not supported in Databricks SQL.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### USAGE Privilege

To perform any action on a schema object, a user must have the **`USAGE`** privilege on that schema in addition to the privilege that authorizes the action itself (e.g., `SELECT`). The `USAGE` requirement is satisfied by any one of the following conditions:^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- The user is a workspace admin.
- The user (or a group they belong to) has the `USAGE` privilege on the schema.
- The user (or a group they belong to) has the `USAGE` privilege on the parent `CATALOG`.
- The user is the owner of the schema (or belongs to a group that owns it).

Even the owner of an object inside a schema must have the `USAGE` privilege in order to use that object.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Hierarchy

When table access control is enabled, SQL objects in the Hive [Metastore](/concepts/metastore.md) form a hierarchy and privileges are inherited downward. Granting or denying a privilege on a `CATALOG` automatically grants or denies the privilege to all schemas within that catalog. Similarly, privileges granted on a schema are inherited by all objects (tables, views, functions) in that schema. This inheritance pattern holds for all [Securable Objects in the Hive Metastore](/concepts/hive-metastore-privileges-and-securable-objects.md).^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

If a user is denied privileges on a table, they cannot see that table when listing all tables in the schema. If denied on a schema, the schema itself is invisible when listing all schemas in the catalog.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Object Ownership

When table access control is enabled, the user who creates a schema, table, view, or function becomes its owner. The owner is automatically granted all privileges and can grant privileges to other users. Groups may also own objects, in which case all members of that group are considered owners.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Ownership can be transferred using the `ALTER <object> OWNER TO` command, which requires either being the current owner or a workspace admin.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Securable Objects

Privileges are granted on the following securable objects in the Hive [Metastore](/concepts/metastore.md):

- **`CATALOG`** — controls access to the entire data catalog.
- **`SCHEMA`** — controls access to a schema (also called a database).
- **`TABLE`** — controls access to a managed or external table.
- **`VIEW`** — controls access to a SQL view.
- **`FUNCTION`** — controls access to a named function.
- **`ANONYMOUS FUNCTION`** — controls access to anonymous or temporary functions. (Not supported in Databricks SQL.)
- **`ANY FILE`** — controls access to the underlying filesystem. **Warning:** Users granted `ANY FILE` can bypass restrictions on catalog, schemas, tables, and views by reading from the filesystem directly.

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Privileges on global and local temporary views are not supported; privileges on the underlying tables and views referenced by temporary views are enforced instead.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Dynamic View Functions for Fine-Grained Access Control

Databricks provides two user functions that can be used inside view definitions to implement column-level and row-level permissions:

- **`current_user()`** — returns the current user name.
- **`is_member(<group>)`** — returns `true` if the current user is a member of a workspace-level group.

These functions enable dynamic views that restrict data visibility at query time. For example, you can use `is_member('auditors')` inside a `CASE` expression to show a redacted value to non‑members, or in a `WHERE` clause to limit which rows a user can see. More complex SQL expressions (e.g., `regexp_extract` for email domains) can be used for data masking.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

See [Dynamic Views for Access Control](/concepts/dynamic-views-for-fine-grained-access-control.md) for full examples of column-level and row-level permissions.

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
