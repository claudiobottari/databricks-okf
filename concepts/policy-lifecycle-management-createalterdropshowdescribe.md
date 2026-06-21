---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1b5370543dac719530104110c32ec7c306372f6b02b87eb2db9383129911a3f
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policy-lifecycle-management-createalterdropshowdescribe
    - PLM(
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Policy Lifecycle Management (CREATE/ALTER/DROP/SHOW/DESCRIBE)
description: SQL statements and UI workflows for creating, editing, deleting, listing, and describing ABAC row filter and column mask policies on securable objects.
tags:
  - data-governance
  - unity-catalog
  - abac
  - operations
timestamp: "2026-06-19T14:34:17.183Z"
---

# Policy Lifecycle Management (CREATE/ALTER/DROP/SHOW/DESCRIBE)

**Policy Lifecycle Management** refers to the set of SQL commands and UI operations used to create, alter, delete, show, and describe ABAC policies (row filters and column masks) in Unity Catalog. These operations are essential for managing attribute-based access control on data objects.

## Overview

All policy lifecycle operations require `MANAGE` privilege on the securable object where the policy is attached (catalog, schema, or table) or ownership of the object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Creating a policy also requires:
- Databricks Runtime 16.4 or above, or serverless compute.
- A user-defined function (UDF) in Unity Catalog on which you have `EXECUTE` privilege, or a SQL function defined inline.
- [Governed Tags](/concepts/governed-tags.md) applied to the target objects. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## CREATE POLICY

The `CREATE POLICY` SQL statement (or the Catalog Explorer UI) creates a new row filter or column mask policy on a catalog, schema, or table.

The creator must have `MANAGE` on the securable object and `EXECUTE` on the UDF that implements the filtering or masking logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

When creating a policy, you specify:
- **Policy identification**: name and description.
- **Principals and scope**: which identities the policy applies to.
- **Policy type**: row filter or column mask.
- **Function logic**: either a pre‑existing UDF or an inline SQL function.
- **Function inputs**: parameters mapped to columns (by tag or custom expression) or constant values. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

The policy can be created via Catalog Explorer, the SQL `CREATE POLICY` command, or the Databricks Python SDK and REST APIs. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## ALTER POLICY (Edit)

Policies are edited using the Catalog Explorer UI, SQL `ALTER POLICY`, or the Python SDK. Editable fields include description, principals, policy type, conditions, and function input mappings. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

The policy name and the securable object on which the policy is applied cannot be changed after creation. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## DROP POLICY (Delete)

Deleting a policy removes it from the securable object. The operation is available via Catalog Explorer, SQL `DROP POLICY`, or the Python SDK. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## SHOW POLICIES

Use `SHOW POLICIES` to list policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to include policies inherited from parent scopes (e.g., a catalog-level policy that applies to a table). ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Syntax:

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name
```

The result includes the policy name, policy type, and the full path of the catalog, schema, or table where it is defined. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Viewing effective policies on a table does not require permissions on the parent catalog or schema. This allows a table admin to see applicable rules without accessing sibling tables' policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## DESCRIBE POLICY

Use `DESCRIBE POLICY` to view the details of a specific policy. This command requires `MANAGE` on the target securable object or ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Syntax:

```sql
DESC | DESCRIBE POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name
```

The result shows the policy's properties as key-value pairs: name, securable object type, securable object name, principals, conditions, function name, and creation/update timestamps. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging

All ABAC policy CRUD operations (create, delete, get, list) are logged in the audit log system table under service name `unityCatalog`. Example queries are available to track policy creation, deletion, and listing. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- ABAC policies – Attribute-based access control using row filters and column masks.
- [Row filter policy](/concepts/row-filter-policies.md) – A policy that excludes rows from query results.
- [Column mask policy](/concepts/column-mask-policies.md) – A policy that masks column values.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that hosts policies.
- [Governed Tags](/concepts/governed-tags.md) – Tags used to match columns for policy application.
- [User-defined functions in Unity Catalog](/concepts/abac-user-defined-functions-udfs.md) – UDFs that implement filtering/masking logic.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI for managing policies.
- Audit logs system table – System table that records policy operations.

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
