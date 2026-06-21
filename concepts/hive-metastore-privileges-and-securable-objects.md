---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adfb06dc02e0094f3ef7ca523fc54906496b4d2602df24c38c8d7eee9933bd76
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-privileges-and-securable-objects
    - Securable Objects and Hive Metastore Privileges
    - HMPASO
    - Hive Metastore Privileges and Securable Objects (Legacy)
    - Hive metastore privileges and securable objects (legacy)
    - Privileges and securable objects in the Hive metastore (SQL reference)
    - Securable Objects in Hive Metastore
    - Securable Objects in the Hive Metastore
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
title: Hive Metastore Privileges and Securable Objects
description: The permission model and set of securable objects (e.g., tables, databases, ANY FILE) used in the legacy Hive metastore table access control system.
tags:
  - databricks
  - access-control
  - hive-metastore
  - privileges
timestamp: "2026-06-19T10:47:44.368Z"
---

# Hive [Metastore](/concepts/metastore.md) Privileges and Securable Objects

**Hive [Metastore](/concepts/metastore.md) Privileges and Securable Objects** defines the authorization model for the legacy Hive [Metastore](/concepts/metastore.md) in Databricks. This model controls which users can perform specific actions on data objects — such as tables, views, databases, and functions — managed by the workspace's built-in Hive [Metastore](/concepts/metastore.md) when table access control is enabled on a cluster.^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Overview

The Hive [Metastore](/concepts/metastore.md) privilege model is a legacy data governance system. Databricks recommends migrating to [Unity Catalog](/concepts/unity-catalog.md) for simplified security and centralized administration across workspaces.^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

When table access control is enabled on a cluster, users can grant and revoke permissions on Hive [Metastore](/concepts/metastore.md) objects using SQL statements such as `GRANT` and `REVOKE`. Without table access control, all users on a cluster can access all data managed by the workspace's Hive [Metastore](/concepts/metastore.md).^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Requirements

- The workspace must be on the Premium plan or above.
- The feature requires a Data Science & Engineering cluster with table access control enabled, or a SQL warehouse.

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Securable Objects

Securable objects are the data entities that privileges can be granted on. The Hive [Metastore](/concepts/metastore.md) supports the following securable objects:

| Securable Object | Description |
|-----------------|-------------|
| **CATALOG** | A top-level namespace container for databases |
| **DATABASE** (or **SCHEMA**) | A collection of tables, views, functions, and other objects |
| **TABLE** | A structured data table |
| **VIEW** | A logical view defined by a query |
| **FUNCTION** | A user-defined function |
| **ANY FILE** | A special securable that grants access to files at the storage path level (see [What is the `ANY FILE` securable?](/concepts/any-file-securable.md)) |

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Privileges

The following table lists the available privileges and the securable objects they apply to:

| Privilege | Securable Objects | Description |
|-----------|------------------|-------------|
| **ALL PRIVILEGES** | CATALOG, DATABASE, TABLE, VIEW, FUNCTION | Grants all applicable privileges on the object |
| **ALTER** | DATABASE, TABLE, VIEW, FUNCTION | Allows modifying the object's metadata |
| **CREATE** | CATALOG, DATABASE | Allows creating objects within the securable |
| **CREATE_NAMED_FUNCTION** | DATABASE | Allows creating named user-defined functions |
| **CREATE_TEMP_FUNCTION** | CATALOG | Allows creating temporary functions |
| **CREATE_TABLE** | DATABASE | Allows creating tables within the database |
| **CREATE_VIEW** | DATABASE | Allows creating views within the database |
| **DELETE** | TABLE, VIEW | Allows deleting rows from a table or view |
| **DROP** | DATABASE, TABLE, VIEW, FUNCTION | Allows dropping the object |
| **EXECUTE** | FUNCTION | Allows executing a user-defined function |
| **INSERT** | TABLE, VIEW | Allows inserting data into a table or view |
| **MODIFY** | DATABASE, TABLE, VIEW | Allows modifying data or metadata |
| **READ_METADATA** | DATABASE, TABLE, VIEW, FUNCTION | Allows reading metadata about the object |
| **REFRESH** | TABLE | Allows refreshing a table's metadata |
| **SELECT** | TABLE, VIEW | Allows querying data from a table or view |
| **SET_CREATE** | CATALOG | Allows setting the default catalog for creation |
| **SUSPEND** | DATABASE | Allows suspending the database |
| **TRUNCATE** | TABLE | Allows truncating a table |
| **USAGE** | CATALOG, DATABASE, FUNCTION | Allows using the object without granting specific data access |
| **WRITE** | TABLE, VIEW | Allows writing data to a table or view |

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Granting and Revoking Privileges

Privileges are managed using standard SQL:

```sql
-- Grant SELECT on a table to a user
GRANT SELECT ON TABLE sales_data TO user@example.com;

-- Grant CREATE on a database to a group
GRANT CREATE ON DATABASE analytics TO developers;

-- Revoke INSERT on a view
REVOKE INSERT ON VIEW active_customers FROM analyst@example.com;

-- Grant ALL PRIVILEGES on a catalog
GRANT ALL PRIVILEGES ON CATALOG main TO admin_group;
```

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Privilege Inheritance and Resolution

- Privileges granted on a catalog apply to all databases and objects within that catalog.
- Privileges granted on a database apply to all tables, views, and functions within that database.
- The `USAGE` privilege on a catalog or database is required to access objects within it.
- The `ALL PRIVILEGES` privilege grants every applicable privilege for the specified object and any children.

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## The `ANY FILE` Securable

The `ANY FILE` securable is a special object that grants file-level access to data at the storage path level, bypassing table and view permissions. This allows users to read data directly from files in cloud storage without needing explicit table-level SELECT permissions. See the dedicated page on [What is the `ANY FILE` securable?](/concepts/any-file-securable.md) for details.

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Migration to Unity Catalog

Databricks recommends migrating Hive [Metastore](/concepts/metastore.md) tables to [Unity Catalog](/concepts/unity-catalog.md) for the following benefits:

- Centralized administration of data access across multiple workspaces
- Simplified auditing and governance
- Unified permission model for both tables and files
- Cross-workspace access control

^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The modern, recommended data governance solution
- [Table Access Control](/concepts/table-access-control-tacl.md) — The cluster-level setting that enables Hive [Metastore](/concepts/metastore.md) permissions
- [Hive Metastore Table Access Control (Legacy)](/concepts/hive-metastore-table-access-control-legacy.md) — The parent page covering enabling and configuration
- [What is the `ANY FILE` securable?](/concepts/any-file-securable.md) — Detailed documentation on the file-level permission object

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
