---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9411fd7b98e54cdb06fb3ff9db01496c078dd0acfe01e077275901cbeac6652
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-securable-objects
    - HMSO
    - Hive metastore securable objects (legacy)
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Hive Metastore Securable Objects
description: The hierarchical object model (CATALOG → SCHEMA → TABLE/VIEW/FUNCTION, plus ANONYMOUS FUNCTION and ANY FILE) to which privileges can be granted in the legacy Hive metastore.
tags:
  - hive-metastore
  - data-governance
  - object-model
timestamp: "2026-06-19T19:04:22.659Z"
---

---
title: Hive [Metastore](/concepts/metastore.md) Securable Objects
summary: The hierarchical securable objects in the Hive [Metastore](/concepts/metastore.md): CATALOG, SCHEMA, TABLE, VIEW, FUNCTION, ANONYMOUS FUNCTION, and ANY FILE.
sources:
  - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:47:18.350Z"
updatedAt: "2026-06-19T10:47:18.350Z"
tags:
  - databricks
  - hive-metastore
  - authorization
aliases:
  - hive-metastore-securable-objects
  - HMSO
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Hive [Metastore](/concepts/metastore.md) Securable Objects

**Hive [Metastore](/concepts/metastore.md) Securable Objects** are the data objects managed by the legacy built-in Hive [Metastore](/concepts/metastore.md) in a Databricks workspace. These objects form a hierarchical namespace — catalog, schema, table, view, and function — and each can have privileges granted or denied to control access. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

The privilege model for the Hive [Metastore](/concepts/metastore.md) is distinct from [Unity Catalog](/concepts/unity-catalog.md), which uses a different system for granting privileges. Table access control must be enabled at the workspace level and on the cluster or SQL warehouse for these privileges to be enforced. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Securable Objects

The following securable objects are defined in the Hive [Metastore](/concepts/metastore.md), arranged in a hierarchy from broadest to most specific: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- **`CATALOG`** – Controls access to the entire data catalog. Privileges granted on the catalog are inherited by all schemas and objects within it.
- **`SCHEMA`** – Controls access to a schema (also called a database). Privileges on a schema are inherited by all tables, views, and functions in that schema.
- **`TABLE`** – Controls access to a managed or external table.
- **`VIEW`** – Controls access to a SQL view.
- **`FUNCTION`** – Controls access to a named function.

In addition to these catalog-level objects, there are two special objects: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- **`ANONYMOUS FUNCTION`** – Controls access to anonymous or temporary functions. This object is not supported in Databricks SQL.
- **`ANY FILE`** – Controls access to the underlying filesystem. **Warning**: Users granted `ANY FILE` can bypass restrictions on catalog, schemas, tables, and views by reading from the filesystem directly.

Privileges on global and local temporary views are not supported. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Types

Privileges are granted, denied, or revoked using GRANT, DENY, and REVOKE SQL statements. The supported privilege types are: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

| Privilege | Effect |
|-----------|--------|
| `SELECT` | Read access to an object. |
| `CREATE` | Ability to create an object (e.g., a table in a schema). |
| `MODIFY` | Ability to add, delete, or modify data in an object. |
| `USAGE` | Does not provide any abilities by itself, but is an additional requirement to perform any action on a schema object. |
| `READ_METADATA` | Ability to view an object and its metadata. |
| `CREATE_NAMED_FUNCTION` | Ability to create a named UDF in an existing catalog or schema. |
| `MODIFY_CLASSPATH` | Ability to add files to the Spark class path (not supported in Databricks SQL). |
| `ALL PRIVILEGES` | All of the above privileges combined. |

## Object Ownership

When table access control is enabled, the user who creates a schema, table, view, or function becomes its owner. The owner is granted all privileges and can grant privileges to other users. Groups may also own objects; in that case, all group members are considered owners. Ownership can be transferred using the `ALTER <object> OWNER TO` command by the current owner or a workspace admin. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

If table access control is disabled, owners are not registered at creation time; a workspace admin must assign an owner afterward using the same `ALTER` command. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Hierarchy

Privileges in the Hive [Metastore](/concepts/metastore.md) are inherited downward. Granting or denying a privilege on a `CATALOG` automatically applies it to all schemas in that catalog. Similarly, privileges on a `SCHEMA` are inherited by all objects in that schema — tables, views, and functions. This inheritance is transitive and applies to all securable objects. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

If a user is denied privileges on a table, they cannot see that table when listing all tables in the schema. If denied on a schema, the schema itself is hidden from the user. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## The `USAGE` Privilege

To perform any action on a schema object, a user must have the `USAGE` privilege on that schema **in addition to** the privilege that authorizes the specific action. The `USAGE` requirement can be satisfied by any of the following: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- Being a workspace admin
- Having the `USAGE` privilege on the schema (or being in a group that has it)
- Having the `USAGE` privilege on the `CATALOG`
- Being the owner of the schema (or belonging to a owning group)

Even the owner of an object inside a schema must have `USAGE` on that schema to use the object. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Dynamic Views for Fine-Grained Access

Databricks provides two built-in functions — `current_user()` and `is_member()` — that can be used inside view definitions to implement column-level and row-level permissions dynamically. These functions allow the view’s logic to adapt based on the current user’s identity or group membership. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Column-Level Permissions

Column-level masking can be achieved with a `CASE WHEN` expression in the view definition. For example, only users who belong to the `auditors` group see full email addresses; others see `'REDACTED'`. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Row-Level Permissions

Row-level filtering restricts which rows are visible. For instance, a `WHERE` clause can limit high‑value transactions to members of the `managers` group. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Data Masking

More complex data masking is possible, such as extracting only the domain portion of an email address for analysts while allowing the `auditors` group to see the full address. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
