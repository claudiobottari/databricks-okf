---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26c4886e72794a74a454d62d50f565c1552d21a82a61b920b6dc3af26267b291
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-object-ownership
    - HMOO
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Hive Metastore Object Ownership
description: The ownership model where creators of objects become owners (or group membership confers ownership), with ability to transfer ownership via ALTER command.
tags:
  - databricks
  - hive-metastore
  - authorization
timestamp: "2026-06-19T10:47:16.292Z"
---

# Hive [Metastore](/concepts/metastore.md) Object Ownership

**Hive [Metastore](/concepts/metastore.md) Object Ownership** defines who controls securable objects (schemas, tables, views, and functions) in the legacy Databricks Hive [Metastore](/concepts/metastore.md) and how ownership affects privilege management. Ownership determines who can grant, deny, or revoke privileges on an object and who can transfer that ownership to another principal. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Ownership Rules

When [table access control](/concepts/table-access-control-tacl.md) is enabled on a cluster or SQL warehouse, the user who creates a schema, table, view, or function automatically becomes its owner. The owner is granted all privileges on the object and can grant privileges to other users. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Groups can also own objects. When a group owns an object, all members of that group are considered owners for the purpose of privilege management. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Transferring Ownership

Ownership can be transferred to another principal by either the current owner or a workspace admin. The transfer is performed using SQL:

```sql
ALTER <object> OWNER TO `<user-name>@<user-domain>.com`
```

In this command, the principal must be enclosed in backticks if the name contains special characters. The supported object types for ownership transfer include `CATALOG`, `SCHEMA`, `TABLE`, `VIEW`, `FUNCTION`, `ANONYMOUS FUNCTION`, and `ANY FILE`. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Ownership When Table Access Control Is Disabled

If table access control is disabled on a cluster or SQL warehouse, owners are not registered when schemas, tables, or views are created. In this case, a workspace admin must explicitly assign an owner using the `ALTER <object> OWNER TO` command. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Interaction with the USAGE Privilege

Even the owner of an object that resides inside a schema must have the `USAGE` privilege on that schema to use the object. This requirement applies to all principals, including owners. A user satisfies the `USAGE` requirement if they are a workspace admin, have the `USAGE` privilege on the schema or catalog, or are the owner of the schema. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Relationship to Unity Catalog

This ownership model applies only to the legacy Hive [Metastore](/concepts/metastore.md) built into each Databricks workspace. [Unity Catalog](/concepts/unity-catalog.md) uses a different privilege model for object ownership and access control. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Related Concepts

- [Table access control](/concepts/table-access-control-tacl.md)
- Hive metastore privileges and securable objects (legacy)
- GRANT
- REVOKE
- DENY
- [Unity Catalog privileges reference](/concepts/privileges-and-ownership.md)
- Workspace admin
- SQL permissions with Terraform

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
