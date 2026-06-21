---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 413a24c7dfbae238f4c4f01f9c5dbc5215d89d6af49a9a7d7728678aeb1ce265
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-access-control-databricks
    - TAC(
    - Access Control in Databricks
    - access control lists
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Table Access Control (Databricks)
description: A workspace-level and cluster-level setting that must be enabled to enforce Hive metastore privileges on Databricks clusters and SQL warehouses.
tags:
  - data-governance
  - access-control
  - hive-metastore
timestamp: "2026-06-19T19:06:20.274Z"
---

# Table Access Control (Databricks)

**Table Access Control (Databricks)** is a legacy security model for managing permissions on data objects in the built-in Databricks Hive [Metastore](/concepts/metastore.md). It allows workspace admins and object owners to grant, deny, and revoke privileges on catalogs, schemas, tables, views, and functions using SQL commands. This model is distinct from [Unity Catalog](/concepts/unity-catalog.md), which uses a different privilege system. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Requirements

To use Table Access Control, an administrator must enable and enforce table access control for the workspace, and the cluster must be enabled for table access control. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Important notes:
- Data access control is always enabled in Databricks SQL, even if table access control is not enabled for the workspace. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]
- If table access control is enabled and ACLs have already been specified in the workspace, those ACLs are respected in Databricks SQL. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Managing Privileges

Privileges on Hive [Metastore](/concepts/metastore.md) data objects can be granted by either a workspace admin or the owner of an object. You manage privileges using SQL commands such as `GRANT`, `REVOKE`, `DENY`, `MSCK`, and `SHOW GRANTS` in a notebook or the Databricks SQL query editor. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

The basic syntax is:

```sql
GRANT privilege_type ON securable_object TO principal
```

Where:
- `privilege_type` is a Hive [Metastore](/concepts/metastore.md) privilege type
- `securable_object` is a securable object, such as a catalog, schema, table, view, or function
- `principal` is a user, service principal (represented by its applicationId value), or group. Enclose names with special characters in backticks. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

To grant a privilege to all users in the workspace, grant it to the `users` group:

```sql
GRANT SELECT ON TABLE <schema-name>.<table-name> TO users
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

You can also manage table access control in a fully automated setup using the Databricks Terraform provider and `databricks_sql_permissions`. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Object Ownership

When table access control is enabled on a cluster or SQL warehouse, the user who creates a schema, table, view, or function becomes its owner. The owner is granted all privileges and can grant privileges to other users. Groups may also own objects, in which case all members of that group are considered owners. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Either the object owner or a workspace admin can transfer ownership:

```sql
ALTER <object> OWNER TO `<user-name>@<user-domain>.com`
```

Note: When table access control is disabled, owners are not registered when objects are created. A workspace admin must assign an owner using the `ALTER` command. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Securable Objects

The securable objects in the Hive [Metastore](/concepts/metastore.md) form a hierarchy:

- **CATALOG**: controls access to the entire data catalog
  - **SCHEMA**: controls access to a schema
    - **TABLE**: controls access to a managed or external table
    - **VIEW**: controls access to SQL views
    - **FUNCTION**: controls access to a named function
- **ANONYMOUS FUNCTION**: controls access to anonymous or temporary functions (not supported in Databricks SQL)
- **ANY FILE**: controls access to the underlying filesystem. Users granted this privilege can bypass restrictions on catalogs, schemas, tables, and views by reading from the filesystem directly. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Note: Privileges on global and local temporary views are not supported. However, privileges on the underlying tables and views referenced by temporary views are enforced. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Types

| Privilege | Description |
|-----------|-------------|
| `SELECT` | Gives read access to an object |
| `CREATE` | Gives ability to create an object (e.g., a table in a schema) |
| `MODIFY` | Gives ability to add, delete, and modify data in an object |
| `USAGE` | Does not give abilities, but is required to perform any action on a schema object |
| `READ_METADATA` | Gives ability to view an object and its metadata |
| `CREATE_NAMED_FUNCTION` | Gives ability to create a named UDF in an existing catalog or schema |
| `MODIFY_CLASSPATH` | Gives ability to add files to the Spark class path (not supported in Databricks SQL) |
| `ALL PRIVILEGES` | Gives all privileges listed above |

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### The `USAGE` Privilege

To perform an action on a schema object, a user must have the `USAGE` privilege on that schema in addition to the privilege to perform the action. Any one of the following satisfies the `USAGE` requirement:

- Be a workspace admin
- Have the `USAGE` privilege on the schema or be in a group that has it
- Have the `USAGE` privilege on the `CATALOG` or be in a group that has it
- Be the owner of the schema or be in a group that owns the schema

Even the owner of an object inside a schema must have the `USAGE` privilege to use it. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Hierarchy

When table access control is enabled, SQL objects are hierarchical and privileges are inherited downward. Granting or denying a privilege on the `CATALOG` automatically grants or denies the privilege to all schemas in the catalog. Similarly, privileges granted on a schema object are inherited by all objects in that schema. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

If you deny a user privileges on a table, the user cannot see the table by attempting to list all tables in the schema. If you deny a user privileges on a schema, the user cannot see that the schema exists. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Dynamic View Functions

Databricks includes two user functions that allow dynamic column-level and row-level permissions within view definitions managed by the Hive [Metastore](/concepts/metastore.md):

- `current_user()`: Returns the current user name
- `is_member()`: Determines if the current user is a member of a specific Databricks workspace-level group

Example combining both functions:

```sql
SELECT
  current_user as user,
  is_member("Managers") as admin
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Column-Level Permissions

You can limit which columns a specific group or user can see using dynamic views. In the following example, only users in the `auditors` group can see email addresses:

```sql
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  CASE WHEN
    is_group_member('auditors') THEN email
    ELSE 'REDACTED'
  END AS email,
  country,
  product,
  total
FROM sales_raw
```

At analysis time, Spark replaces the `CASE` statement with either the literal `'REDACTED'` or the column `email`. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Row-Level Permissions

You can specify permissions down to the row level. In the following example, only users in the `managers` group can see transactions over $1,000,000:

```sql
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  country,
  product,
  total
FROM sales_raw
WHERE
  CASE
    WHEN is_group_member('managers') THEN TRUE
    ELSE total <= 1000000
  END;
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Data Masking

You can implement more advanced masking using SQL expressions. The following example lets all users see email domains, but only lets `auditors` group members see full email addresses:

```sql
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  region,
  CASE
    WHEN is_group_member('auditors') THEN email
    ELSE regexp_extract(email, '^.*@(.*), 1)
  END
FROM sales_raw
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Comparison with Unity Catalog

Unity Catalog uses a different model for granting privileges. For more information, see the [Unity Catalog privileges reference](/concepts/unity-catalog-privileges-and-ownership.md). Table Access Control is the legacy system that is built into each Databricks workspace. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- Data governance
- Access control
- [Privileges and securable objects in the Hive metastore (SQL reference)](/concepts/hive-metastore-privileges-and-securable-objects.md)
- Databricks Terraform

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
