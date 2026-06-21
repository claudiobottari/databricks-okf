---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 248dbacc38caefaf82ea805302c1a93dd1287a5305a1e16aaf080f96ae668a9d
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-privilege-model-legacy
    - HMPM(
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Hive Metastore Privilege Model (Legacy)
description: The legacy access control system for the built-in Hive metastore in Databricks workspaces, distinct from Unity Catalog's privilege model.
tags:
  - data-governance
  - hive-metastore
  - access-control
timestamp: "2026-06-19T19:04:03.671Z"
---

Here is the wiki page for "Hive [Metastore](/concepts/metastore.md) Privilege Model (Legacy)".

---

## Hive [Metastore](/concepts/metastore.md) Privilege Model (Legacy)

The **Hive [Metastore](/concepts/metastore.md) Privilege Model (Legacy)** is the access control system for data objects managed by the built-in Hive [Metastore](/concepts/metastore.md) in each Databricks workspace. This model uses SQL commands to grant, deny, and revoke privileges on securable objects. It is distinct from the Unity Catalog Privileges Reference|Unity Catalog privilege model, which uses a different approach for managing permissions. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Requirements

To use the Hive [Metastore](/concepts/metastore.md) privilege model, an administrator must enable and enforce table access control for the workspace, and the cluster must be enabled for [Table Access Control](/concepts/table-access-control-tacl.md). ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Data access control is always enabled in Databricks SQL, even if table access control is not enabled for the workspace. If table access control is enabled and ACLs have already been specified, those ACLs are respected in Databricks SQL. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Managing Privileges

Privileges on data objects managed by the Hive [Metastore](/concepts/metastore.md) can be granted by either a workspace admin or the owner of an object. Privileges are managed using SQL commands such as `GRANT`, `REVOKE`, `DENY`, `MSCK`, and `SHOW GRANTS` in a notebook or the Databricks SQL query editor. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

The general syntax for granting a privilege is:

```sql
GRANT privilege_type ON securable_object TO principal
```

Where `privilege_type` is a Hive [Metastore](/concepts/metastore.md) privilege type, `securable_object` is a securable object in the Hive [Metastore](/concepts/metastore.md), and `principal` is a user, service principal (represented by its applicationId value), or group. Users, service principals, and group names with special characters must be enclosed in backticks. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

To grant a privilege to all users in a workspace, grant the privilege to the `users` group. For example:

```sql
GRANT SELECT ON TABLE <schema-name>.<table-name> TO users
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Table access control can also be managed in a fully automated setup using the Databricks Terraform provider and the `databricks_sql_permissions` resource. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Object Ownership

When table access control is enabled on a cluster or SQL warehouse, the user who creates a schema, table, view, or function becomes its owner. The owner is granted all privileges and can grant privileges to other users. Groups may own objects, in which case all members of that group are considered owners. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Either the owner of an object or a workspace admin can transfer ownership using the following command:

```sql
ALTER <object> OWNER TO `<user-name>@<user-domain>.com`
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

When table access control is disabled, owners are not registered when an object is created. A workspace admin must assign an owner using the `ALTER <object> OWNER TO` command. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Securable Objects

The Hive [Metastore](/concepts/metastore.md) defines a hierarchy of securable objects:

- **CATALOG**: Controls access to the entire data catalog.
  - **SCHEMA**: Controls access to a schema.
    - **TABLE**: Controls access to a managed or external table.
    - **VIEW**: Controls access to SQL views.
    - **FUNCTION**: Controls access to a named function.
- **ANONYMOUS FUNCTION**: Controls access to anonymous or temporary functions. Not supported in Databricks SQL.
- **ANY FILE**: Controls access to the underlying filesystem. Users granted access to `ANY FILE` can bypass restrictions on catalog, schemas, tables, and views by reading from the filesystem directly.

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Privileges on global and local temporary views are not supported. However, privileges on the underlying tables and views referenced by any temporary views are enforced. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Privilege Types

The following privilege types are available in the Hive [Metastore](/concepts/metastore.md) model:

- **SELECT**: Gives read access to an object.
- **CREATE**: Gives ability to create an object (for example, a table in a schema).
- **MODIFY**: Gives ability to add, delete, and modify data to or from an object.
- **USAGE**: Does not give any abilities, but is an additional requirement to perform any action on a schema object.
- **READ_METADATA**: Gives ability to view an object and its metadata.
- **CREATE_NAMED_FUNCTION**: Gives ability to create a named UDF in an existing catalog or schema.
- **MODIFY_CLASSPATH**: Gives ability to add files to the Spark class path. Not supported in Databricks SQL.
- **ALL PRIVILEGES**: Gives all privileges (translated into all the above privileges).

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### The `USAGE` Privilege

To perform an action on a schema object in the Hive [Metastore](/concepts/metastore.md), a user must have the `USAGE` privilege on that schema in addition to the privilege to perform that action. The `USAGE` requirement is satisfied if any of the following are true:

- The user is a workspace admin.
- The user has the `USAGE` privilege on the schema or is in a group that has the `USAGE` privilege on the schema.
- The user has the `USAGE` privilege on the `CATALOG` or is in a group that has the `USAGE` privilege.
- The user is the owner of the schema or is in a group that owns the schema.

Even the owner of an object inside a schema must have the `USAGE` privilege in order to use it. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Privilege Hierarchy

When table access control is enabled, SQL objects in Databricks are hierarchical and privileges are inherited downward. Granting or denying a privilege on the `CATALOG` automatically grants or denies the privilege to all schemas in the catalog. Similarly, privileges granted on a schema object are inherited by all objects in that schema. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

If a user is denied privileges on a table, the user cannot see the table by attempting to list all tables in the schema. If a user is denied privileges on a schema, the user cannot see that the schema exists by attempting to list all schemas in the catalog. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Dynamic View Functions

Databricks includes two user functions that allow expressing column- and row-level permissions dynamically in the body of a view definition managed by the Hive [Metastore](/concepts/metastore.md): ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- **`current_user()`**: Returns the current user name.
- **`is_member()`**: Determines if the current user is a member of a specific Databricks group at the workspace level.

#### Column-Level Permissions

Dynamic views can limit the columns a specific group or user can see. In the following example, only users who belong to the `auditors` group are able to see email addresses from the `sales_raw` table:

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

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

#### Row-Level Permissions

Dynamic views can specify permissions down to the row level. In the following example, only users who belong to the `managers` group are able to see transaction amounts greater than $1,000,000.00:

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

#### Data Masking

More advanced types of masking can be implemented with complex SQL expressions. The following example lets all users perform analysis on email domains, but lets members of the `auditors` group see full email addresses:

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

### Related Concepts

- Unity Catalog Privileges Reference
- [Table Access Control](/concepts/table-access-control-tacl.md)
- Databricks SQL Permissions
- Dynamic Views
- [Data Masking](/concepts/conditional-column-masking.md)
- User and Group Management

### Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
