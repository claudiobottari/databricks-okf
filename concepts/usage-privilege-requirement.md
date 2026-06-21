---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 54add2697b8eeec128c1ac69e971f2df011554e338c28cee12cbf0bf6e4dd2ca
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - usage-privilege-requirement
    - UPR
    - USAGE privilege
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: USAGE Privilege Requirement
description: The requirement that users must have the USAGE privilege on a schema (or meet one of several alternative conditions) in addition to any action-specific privilege to operate on objects within that schema.
tags:
  - hive-metastore
  - access-control
  - sql-privileges
timestamp: "2026-06-19T19:04:26.342Z"
---

---
title: USAGE Privilege Requirement
summary: The requirement that users must have the USAGE privilege on a schema (or catalog/ownership) before they can perform any action on objects within that schema.
sources:
  - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:47:17.140Z"
updatedAt: "2026-06-19T10:47:17.140Z"
tags:
  - databricks
  - authorization
  - hive-metastore
aliases:
  - usage-privilege-requirement
  - UPR
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# USAGE Privilege Requirement

The **USAGE Privilege Requirement** is a mandatory access control rule in the legacy Databricks Hive [Metastore](/concepts/metastore.md) that requires users to possess the `USAGE` privilege on a schema before they can perform any action on objects within that schema. This requirement applies in addition to any other privileges needed for the specific action. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Overview

In the Hive [Metastore](/concepts/metastore.md) privilege model, `USAGE` does not grant any abilities on its own. Instead, it functions as a prerequisite — a user must have `USAGE` on a schema to be allowed to use any objects (tables, views, functions) inside that schema, even if they hold other privileges like `SELECT` or `MODIFY` on those objects. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## How the Requirement Is Satisfied

Any one of the following conditions satisfies the `USAGE` requirement for a schema: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- Be a workspace admin
- Have the `USAGE` privilege on the schema, or be in a group that has the `USAGE` privilege on the schema
- Have the `USAGE` privilege on the `CATALOG`, or be in a group that has the `USAGE` privilege on the catalog
- Be the owner of the schema, or be in a group that owns the schema

## Key Implications

### Owners Are Not Exempt

Even the owner of an object inside a schema must have the `USAGE` privilege in order to use that object. Object ownership alone does not bypass the requirement. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Inheritance Through the Privilege Hierarchy

Because SQL objects in Databricks are hierarchical and privileges are inherited downward, granting `USAGE` on the `CATALOG` automatically grants `USAGE` to all schemas within that catalog. Similarly, granting `USAGE` on a schema grants it to all objects in that schema. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Practical Effect

Without `USAGE` on a schema, a user cannot see that the schema exists when listing schemas in the catalog, and cannot access any tables, views, or functions within it — regardless of other privileges they may hold on those objects. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Granting USAGE Privilege

The `USAGE` privilege can be granted using the standard SQL `GRANT` statement: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

```sql
GRANT USAGE ON SCHEMA <schema-name> TO <principal>
```

Where `principal` is a user, service principal, or group. To grant `USAGE` to all users in a workspace, grant it to the `users` group. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore Privileges](/concepts/hive-metastore-privilege-types.md) — The full set of privilege types in the legacy Hive [Metastore](/concepts/metastore.md)
- [Securable Objects in Hive Metastore](/concepts/hive-metastore-privileges-and-securable-objects.md) — The hierarchy of catalog, schema, table, view, and function objects
- [Privilege Hierarchy](/concepts/privilege-hierarchy-and-inheritance.md) — How privileges are inherited downward through the object hierarchy
- [Table Access Control](/concepts/table-access-control-tacl.md) — The workspace-level setting that enables this privilege model
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The modern privilege model that replaces the Hive [Metastore](/concepts/metastore.md) approach

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
