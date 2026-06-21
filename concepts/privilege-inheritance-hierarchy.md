---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 90e5720d7723f659afdce6d2ad2f7e8f07f7e763d96822e9667db9a793b8d0d4
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privilege-inheritance-hierarchy
    - PIH
    - Privilege Inheritance
    - Privilege inheritance
    - QPH
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Privilege Inheritance Hierarchy
description: The downward inheritance model where privileges granted or denied on a parent object (e.g., CATALOG) automatically apply to all child objects (schemas, tables, etc.).
tags:
  - hive-metastore
  - access-control
  - hierarchy
timestamp: "2026-06-19T19:03:44.550Z"
---

# Privilege Inheritance Hierarchy

**Privilege Inheritance Hierarchy** describes the downward inheritance model used by the legacy Databricks Hive [Metastore](/concepts/metastore.md): when a privilege is granted or denied on a higher-level securable object, that privilege is automatically inherited by all lower-level objects within it. This model applies to all securable objects in the Hive [Metastore](/concepts/metastore.md) when table access control is enabled on the workspace and on all clusters. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## How Inheritance Works

SQL objects in the Hive [Metastore](/concepts/metastore.md) form a hierarchy: `CATALOG` → `SCHEMA` → objects (tables, views, functions). Granting or denying a privilege on a `CATALOG` automatically grants or denies that same privilege to every schema in the catalog. Similarly, any privilege set on a schema is inherited by all tables, views, and functions within that schema. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

This cascading inheritance means that an administrator can manage access at a broad level without needing to configure individual objects. The inheritance rule holds for all privilege types, including `SELECT`, `MODIFY`, `USAGE`, `READ_METADATA`, and others. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Effects on Visibility

The inheritance hierarchy directly affects object visibility:

- If a user is denied all privileges on a table, the table is not visible in the schema listing.
- If a user is denied all privileges on a schema, the schema itself is not visible in the catalog listing. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

This behavior prevents users from even discovering the existence of objects they cannot access.

## Relationship with the `USAGE` Privilege

In addition to the inherited privileges, a separate `USAGE` privilege is required to perform any action on a schema object. The `USAGE` requirement can be satisfied by having the privilege on the schema, on the catalog, or by being the schema owner. Even the owner of an object inside a schema must personally satisfy the `USAGE` requirement. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

`USAGE` itself does not grant any data-access abilities; it is a prerequisite for other privileges to take effect.

## Context

This privilege model belongs to the **legacy Databricks Hive metastore**, which is built in to each Databricks workspace. It is distinct from the model used by [Unity Catalog](/concepts/unity-catalog.md), which employs a different set of securable objects and privilege types. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md] For Unity Catalog, see the [Unity Catalog privileges reference](/concepts/privileges-and-ownership.md).

## Related Concepts

- [Hive Metastore](/concepts/built-in-hive-metastore.md) – The legacy [Metastore](/concepts/metastore.md) where this hierarchy is applied.
- [Unity Catalog](/concepts/unity-catalog.md) – The modern data governance solution with a different privilege model.
- [Table Access Control](/concepts/table-access-control-tacl.md) – The workspace-level setting that enables privilege enforcement.
- USAGE Privilege – A prerequisite privilege for accessing schema objects.
- Dynamic Views – Views that use functions like `current_user()` and `is_member()` to implement finer-grained access control.
- GRANT, REVOKE, DENY – SQL commands used to manage privileges.

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
