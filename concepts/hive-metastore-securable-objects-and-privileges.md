---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 816187ee7d8621e7ec220611730f9e6f60622e895825a8b8a638ef5ec17040da
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - hive-metastore-securable-objects-and-privileges
    - Privileges and Hive Metastore Securable Objects
    - HMSOAP
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
title: Hive Metastore Securable Objects and Privileges
description: The permission model defining which Hive metastore objects (tables, databases, views, etc.) can be secured and what privileges can be granted on them using table access control.
tags:
  - databricks
  - permissions
  - hive
  - authorization
timestamp: "2026-06-19T19:05:40.632Z"
---

# Hive [Metastore](/concepts/metastore.md) Securable Objects and Privileges

**Hive [Metastore](/concepts/metastore.md) Securable Objects and Privileges** defines the access control model for the legacy Hive [Metastore](/concepts/metastore.md) in Databricks. When [Hive Metastore Table Access Control](/concepts/hive-metastore-table-access-control.md) is enabled on a cluster, administrators can grant and revoke permissions on specific data objects using SQL or Python commands. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Overview

The Hive [Metastore](/concepts/metastore.md) access control system organizes data into a hierarchy of securable objects. Each securable object type supports a specific set of privileges that determine what actions users can perform on that object. These privileges control both data access (reading, writing) and object management (creating, altering, dropping). ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Securable Objects

The Hive [Metastore](/concepts/metastore.md) defines a hierarchy of securable objects:

- **Catalog** (`CATALOG`): The top-level container that holds databases. Privileges granted on a catalog apply to all databases and tables within it.
- **Database** (`DATABASE`): Contains tables, views, and functions. Privileges granted on a database apply to all tables, views, and functions within it.
- **Table** (`TABLE`): A structured data collection stored in the [Metastore](/concepts/metastore.md). This includes managed tables, external tables, and views.
- **View** (`VIEW`): A virtual table based on a stored SQL query. Views have the same privilege model as tables.
- **Function** (`FUNCTION`): A user-defined function registered in the [Metastore](/concepts/metastore.md).
- **Column** (`COLUMN`): Individual columns within a table or view. Column-level privileges allow fine-grained control over which fields a user can access.
- **ANY FILE** (`ANY FILE`): A special securable that controls access to files in cloud storage that are not registered as tables in the [Metastore](/concepts/metastore.md). ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Privileges

The following privileges can be granted on Hive [Metastore](/concepts/metastore.md) securable objects:

| Privilege | Description |
|-----------|-------------|
| `SELECT` | Read data from a table, view, or column. |
| `INSERT` | Add new data to a table. |
| `UPDATE` | Modify existing data in a table. |
| `DELETE` | Remove data from a table. |
| `CREATE` | Create objects within a catalog or database. |
| `ALTER` | Modify the structure or properties of a table, view, or database. |
| `DROP` | Remove an object from the [Metastore](/concepts/metastore.md). |
| `READ_METADATA` | View metadata about an object (e.g., schema, location). |
| `ALL PRIVILEGES` | Grants all applicable privileges on the object. |

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Granting and Revoking Privileges

Privileges are managed using standard SQL statements:

```sql
-- Grant SELECT on a table to a user
GRANT SELECT ON TABLE my_database.my_table TO `user@example.com`;

-- Grant ALL PRIVILEGES on a database
GRANT ALL PRIVILEGES ON DATABASE my_database TO `team-group@example.com`;

-- Revoke INSERT on a table
REVOKE INSERT ON TABLE my_database.my_table FROM `user@example.com`;
```

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Privilege Inheritance

Privileges follow the object hierarchy through inheritance:

- Privileges granted on a **catalog** automatically apply to all databases within that catalog.
- Privileges granted on a **database** automatically apply to all tables, views, and functions within that database.
- Privileges granted on a **table** do **not** automatically apply to views built on that table; views require separate privilege grants.
- Column-level privileges override table-level privileges for the specified columns.

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## The `ANY FILE` Securable

The `ANY FILE` securable controls access to files stored in cloud storage that are not registered as tables in the Hive [Metastore](/concepts/metastore.md). This includes:

- Files accessed via Spark's file reading APIs (e.g., `spark.read.format("csv").load("s3://bucket/path")`)
- Files queried through temporary views or direct path references

Granting `SELECT` on `ANY FILE` allows a user to read any file in the workspace's configured cloud storage locations, regardless of whether the file is registered as a table. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Requirements

- Hive [Metastore](/concepts/metastore.md) table access control requires a [Databricks Premium Plan](/concepts/databricks-premium-plan-requirement.md) or above.
- This feature must be enabled on a Data Science & Engineering cluster or is automatically available on a SQL Warehouse.
- When table access control is disabled on a cluster, all users can access all data managed by the workspace's Hive [Metastore](/concepts/metastore.md). ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The modern data governance solution that replaces Hive [Metastore](/concepts/metastore.md) access control.
- [Hive Metastore Table Access Control](/concepts/hive-metastore-table-access-control.md) — How to enable and configure table access control on clusters.
- Data Governance — Overall framework for managing data access and security.
- SQL Permissions — General SQL permission models in Databricks.

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
