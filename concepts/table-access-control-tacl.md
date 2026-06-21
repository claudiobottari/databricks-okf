---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 490a61c7f25b00cde65344b662c1a6d4d535196bf00da2bd3cd7752b4313477c
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-access-control-tacl
    - TAC(
    - Table Access Control
    - Table access control
    - table access control
    - Access control lists
    - Delta Lake table access controls
    - Legacy Table Access Control
    - Legacy table access control
    - Table access control (legacy)
    - legacy table access control
    - table access control (legacy)
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Table Access Control (TACL)
description: A workspace-level and cluster-level setting that must be enabled for Hive metastore privilege enforcement in Databricks.
tags:
  - databricks
  - access-control
  - security
timestamp: "2026-06-19T10:47:05.952Z"
---

# Table Access Control (TACL)

**Table Access Control (TACL)** is the legacy privilege model for the built-in Hive [Metastore](/concepts/metastore.md) in a Databricks workspace. It governs what users, service principals, and groups can do with data objects such as schemas, tables, views, and functions. TACL is distinct from the access control model used by [Unity Catalog](/concepts/unity-catalog.md), which follows a different privilege and inheritance system. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Requirements

To use TACL, a workspace administrator must first [enable and enforce table access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl#enable-table-acl-workspace) for the workspace. In addition, the cluster or Databricks SQL warehouse used to run queries must be enabled for table access control. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

> **Note:** Data access control is _always enabled_ in Databricks SQL, even if TACL is not enabled for the workspace. If TACL is enabled and ACLs have already been granted or denied, those ACLs are respected in Databricks SQL. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Securable Objects in the Hive [Metastore](/concepts/metastore.md)

TACL applies to the following hierarchy of securable objects:

- **CATALOG** – controls access to the entire data catalog.
  - **SCHEMA** – controls access to a schema.
    - **TABLE** – controls access to a managed or external table.
    - **VIEW** – controls access to SQL views.
    - **FUNCTION** – controls access to a named function.
- **ANONYMOUS FUNCTION** – controls access to temporary or anonymous functions (not supported in Databricks SQL).
- **ANY FILE** – controls access to the underlying filesystem. Granting this privilege allows users to bypass restrictions on catalog, schemas, tables, and views by reading files directly. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Privileges on global and local temporary views are not supported; however, privileges on the underlying objects referenced by any temporary view are enforced. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Types

The available privilege types in TACL are:

| Privilege | Effect |
|-----------|--------|
| `SELECT` | Read access to an object. |
| `CREATE` | Ability to create an object (e.g., a table inside a schema). |
| `MODIFY` | Ability to add, delete, or modify data in an object. |
| `USAGE` | Required, in addition to the specific action privilege, to perform any action on a schema object. |
| `READ_METADATA` | Ability to view an object and its metadata. |
| `CREATE_NAMED_FUNCTION` | Ability to create a named UDF in an existing catalog or schema. |
| `MODIFY_CLASSPATH` | Ability to add files to the Spark class path (not supported in Databricks SQL). |
| `ALL PRIVILEGES` | Grants all the privileges listed above. |

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### The `USAGE` Privilege

To act on a schema object, a user must have the `USAGE` privilege on that schema (or on the containing catalog) in addition to the privilege that authorizes the specific action. The requirement is satisfied if the user is a workspace admin, owns the schema, has `USAGE` on the schema or catalog, or belongs to a group that has those privileges. Even the owner of an object inside a schema must hold `USAGE` on the schema to use the object. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Privilege Hierarchy and Inheritance

When TACL is enabled, privileges are inherited downward through the object hierarchy. Granting or denying a privilege on a `CATALOG` automatically applies to all schemas in that catalog, and granting or denying on a schema applies to all tables, views, and functions in that schema. If a user is denied a privilege on a table, they cannot see that table when listing objects in the schema; similarly, denial on a schema hides the schema from the user's listing. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Object Ownership

When TACL is enabled on a cluster or SQL warehouse, the user who creates a schema, table, view, or function becomes its owner. The owner is granted all privileges and can grant privileges to other users. Groups may also own objects; in that case all group members are considered owners. Ownership can be transferred by the current owner or a workspace admin using the `ALTER <object> OWNER TO <user>` command. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

> **Note:** If TACL is disabled on a cluster or SQL warehouse, owners are not registered at creation time. A workspace admin must assign an owner manually using the `ALTER` command. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Managing Privileges with SQL

Privileges are managed using standard SQL statements: `GRANT`, `REVOKE`, `DENY`, `MSCK`, and `SHOW GRANTS`. The general syntax is:

```sql
GRANT privilege_type ON securable_object TO principal
```

Where `principal` is a user, service principal (by its applicationId), or group. Names with special characters must be enclosed in backticks. To grant a privilege to all users in the workspace, grant it to the `users` group. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Privileges can also be managed programmatically using the Databricks Terraform provider and the `databricks_sql_permissions` resource. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Dynamic View Functions

TACL provides two built-in functions for implementing column-level and row-level permissions with dynamic views:

- `current_user()` – returns the user name of the current session.
- `is_member(<group>)` – returns `true` if the current user belongs to the specified Databricks workspace-level group.

These functions are used inside view definitions to filter or mask data dynamically. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Column-Level Permissions

A view can limit which columns a user sees. For example, only members of the `auditors` group see full email addresses; all others see the value `'REDACTED'`:

```sql
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  CASE WHEN is_group_member('auditors') THEN email ELSE 'REDACTED' END AS email,
  country, product, total
FROM sales_raw;
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Row-Level Permissions

Similarly, rows can be filtered based on group membership. The following example shows only transactions up to $1,000,000 to non-managers, while managers see all rows:

```sql
CREATE VIEW sales_redacted AS
SELECT user_id, country, product, total
FROM sales_raw
WHERE CASE
  WHEN is_group_member('managers') THEN TRUE
  ELSE total <= 1000000
END;
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### Data Masking

More advanced masking is possible with standard SQL expressions. The following example lets all users see the domain of an email address, while `auditors` see the full email:

```sql
CREATE VIEW sales_redacted AS
SELECT
  user_id, region,
  CASE WHEN is_group_member('auditors') THEN email
       ELSE regexp_extract(email, '^.*@(.*), 1)
  END
FROM sales_raw;
```

^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Comparison with Unity Catalog

TACL is a legacy feature specific to the built-in Hive [Metastore](/concepts/metastore.md). [Unity Catalog](/concepts/unity-catalog.md) uses a different privilege model and is the recommended approach for workspace-level data governance in Databricks. See the [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference) for details. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- Databricks SQL
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- Data governance on Databricks
- GRANT, REVOKE, DENY statements

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
