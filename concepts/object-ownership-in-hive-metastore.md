---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2af25547e5f2b3c21b8a7d826c076509463785a9eab4a8e44bb7bc94118fb53c
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - object-ownership-in-hive-metastore
    - OOIHM
    - External Hive Metastore
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Object Ownership in Hive Metastore
description: The model where a user who creates a schema, table, view, or function becomes its owner with all privileges and grant authority; workspace admins can transfer ownership.
tags:
  - hive-metastore
  - ownership
  - access-control
timestamp: "2026-06-19T19:03:27.154Z"
---

# Object Ownership in Hive [Metastore](/concepts/metastore.md)

**Object Ownership in Hive Metastore** refers to the rights and responsibilities assigned to a user, service principal, or group that creates a schema, table, view, or function within the legacy Databricks Hive [Metastore](/concepts/metastore.md). Ownership determines who can grant, deny, or revoke privileges on the object and who can transfer ownership to another principal. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## How Ownership Is Established

When table access control is enabled on a cluster or SQL warehouse, the user who creates a schema, table, view, or function automatically becomes its owner. The owner is implicitly granted all privileges on the object and can grant privileges to other users. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Groups can also own objects. When a group is the owner, all members of that group are considered owners and inherit the associated capabilities. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Table Access Control Disabled

If table access control is not enabled on the cluster or SQL warehouse, owners are not registered automatically when a schema, table, or view is created. In this case, a workspace admin must later assign an owner using the `ALTER <object> OWNER TO` command. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Transferring Ownership

Object ownership can be transferred to another user by either the current owner or a workspace admin. The transfer is performed using SQL:

```sql
ALTER <object> OWNER TO `<user-name>@<user-domain>.com`
```

Where `<object>` is one of: `CATALOG`, `SCHEMA`, `TABLE`, `VIEW`, or `FUNCTION`. The target principal must be specified as a backtick-quoted name with domain. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Ownership and the USAGE Privilege

The [USAGE privilege](/concepts/usage-privilege-requirement.md) on a schema is required to perform any action on objects within that schema. Ownership satisfies this requirement: if a user is the owner of a schema (or is a member of a group that owns the schema), they automatically have the USAGE privilege on that schema — even if they are the owner of an object inside it. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Securable Objects Subject to Ownership

The following securable objects in the Hive [Metastore](/concepts/metastore.md) can have an owner:

- `CATALOG`
- `SCHEMA`
- `TABLE`
- `VIEW`
- `FUNCTION`

Anonymous functions (`ANONYMOUS FUNCTION`), the `ANY FILE` resource, and temporary views do not have ownership semantics in the same way. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore Privileges](/concepts/hive-metastore-privilege-types.md) – The full privilege model for the legacy [Metastore](/concepts/metastore.md).
- [Table Access Control](/concepts/table-access-control-tacl.md) – The prerequisite setting for automatic ownership registration.
- GRANT, REVOKE, DENY in Hive Metastore – Commands for managing privileges on owned objects.
- [Unity Catalog](/concepts/unity-catalog.md) – The modern governance model that uses a different ownership and privilege system.
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md) – The role that can transfer ownership and assign owners when table access control is disabled.

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
