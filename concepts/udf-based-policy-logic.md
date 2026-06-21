---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 579ed5c7ab144ecbcd19ee6ced5fcc93f6ff7bc859432dca1a3f71efba4fa2f3
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - udf-based-policy-logic
    - UPL
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: UDF-based Policy Logic
description: ABAC row filter and column mask policies rely on user-defined functions (UDFs) in Unity Catalog that implement the filtering or masking logic, requiring EXECUTE permission on the UDF.
tags:
  - data-governance
  - udf
  - unity-catalog
timestamp: "2026-06-19T09:34:44.705Z"
---

# UDF-based Policy Logic

**UDF-based Policy Logic** is a mechanism in Unity Catalog that uses user-defined functions (UDFs) to implement the filtering or masking rules for [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies. When creating a row filter or column mask policy, the policy references a UDF that contains the actual logic for determining which rows to show or how to transform column values for non-exempt users.

## Overview

UDF-based policies use [Unity Catalog user-defined functions](/concepts/abac-user-defined-functions-udfs.md) to define the behavior of row filters and column masks. For row filters, the UDF evaluates each row and returns a boolean; rows where the function returns `FALSE` are excluded from query results. For column masks, the UDF returns the original or masked value, with the return type castable to the target column's data type. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Creating the UDF

Before creating a policy, you need a UDF in Unity Catalog that implements the filtering or masking logic. The UDF can be:

- A **SQL UDF** defined using `CREATE FUNCTION` — recommended for better performance because the query optimizer can inline SQL UDFs.
- A **Python UDF** — supported but cannot be inlined by the query optimizer, which may impact performance. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### UDF Requirements

- The UDF's return type must match or be castable to the column's data type. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- The first argument to the UDF is always the masked column value (bound automatically from the `ON COLUMN` clause). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- Additional arguments are supplied via the `USING COLUMNS` clause, which can reference other columns matching tag expressions or constant values. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Example Column Mask UDF

The following SQL UDF masks a Social Security Number to show only the last N digits:

```sql
CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING
  RETURN CONCAT('***-**-', RIGHT(ssn, show_last));
```

^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

This UDF takes the original column value (`ssn`) and a constant (`show_last`) that controls how many characters are visible.

## Assigning the UDF to a Policy

Once the UDF exists in Unity Catalog, you assign it to a policy using the CREATE POLICY SQL statement or the Catalog Explorer UI. The policy references the UDF by name and specifies:

- Which columns to target (via `MATCH COLUMNS` and tag conditions)
- Which principals are subject to the policy
- Additional function argument values (via `USING COLUMNS`)

### Example Column Mask Policy

```sql
CREATE POLICY mask_ssn_columns
ON CATALOG hr_catalog
COLUMN MASK mask_ssn
TO `account users` EXCEPT `compliance team`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col
USING COLUMNS (4);
```

^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

In this example, the policy uses the `mask_ssn` UDF and passes the constant `4` as the second argument, causing only the last four digits of the SSN to be visible to non-exempt users.

## Row Filter UDFs

For row filters, the UDF receives column values and returns a boolean. The policy references the UDF in the `ROW FILTER` clause:

- **Select existing**: Choose a UDF already defined in Unity Catalog. The UDF evaluates each row and returns a boolean. Rows where the function returns `FALSE` are excluded from query results. You must have `EXECUTE` on the UDF. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Create**: Define a SQL function inline when creating the policy in the UI. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Function inputs for row filters can be a column matched by tags, a column matched by a custom expression, or a constant value. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Permissions

To use a UDF in a policy, the policy creator must have `EXECUTE` privilege on the UDF. Additionally, users querying data through the policy need `SELECT` (or appropriate) privileges on the target table — the policy controls how data appears but does not grant access. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits of UDF-based Policy Logic

- **Reusability**: The same UDF can be referenced by multiple policies, ensuring consistent masking or filtering logic across the estate. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Centralized Updates**: Modifying the UDF updates the masking or filtering logic for all policies that reference it, without needing to edit each policy individually. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Flexibility**: UDFs support complex business logic that goes beyond simple tag matching, such as conditional masking based on user attributes or data values.

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md) – Policies that use UDFs for column-level masking.
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md) – Policies that use UDFs for row-level filtering.
- [Unity Catalog User-Defined Functions](/concepts/abac-user-defined-functions-udfs.md) – The catalog system that stores and manages UDFs.
- CREATE POLICY – The SQL syntax for creating ABAC policies.
- [Governed Tags](/concepts/governed-tags.md) – The attributes used to identify target columns in policy definitions.
- Policy Evaluation Order – How multiple policies and UDFs interact at query time.

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
2. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
