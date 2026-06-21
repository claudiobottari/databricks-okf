---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f65ebd21669b4bfc15f3c97e36fcadaa9e64a71ee0809e274d8cfa46b12d03b4
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-user-defined-functions-udfs
    - AUF(
    - Pandas User-Defined Functions (UDFs)
    - User-Defined Function (UDF)
    - User-Defined Function (UDF)|UDFs
    - User-Defined Functions (UDFs)
    - User-defined function (UDF)
    - User-defined functions (UDF)
    - User-defined functions (UDFs)
    - User‑Defined Function (UDF)
    - User‑Defined Functions (UDFs)
    - user-defined function (UDF)
    - user-defined functions (UDFs)
    - user‑defined function (UDF)
    - user‑defined functions (UDFs)
    - Unity Catalog User-Defined Functions
    - Unity Catalog user-defined functions
    - Unity Catalog user‑defined functions
    - User-Defined Function (UDF)|user-defined function (UDF)
    - User-Defined Functions (UDF) – Databricks
    - User-defined functions in Unity Catalog
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC User-Defined Functions (UDFs)
description: Row filter and column mask policies rely on UDFs (SQL or Python) registered in Unity Catalog to implement filtering or masking logic, with SQL UDFs recommended for better performance.
tags:
  - abac
  - udf
  - policies
timestamp: "2026-06-19T17:54:00.555Z"
---

# ABAC User-Defined Functions (UDFs)

**ABAC User-Defined Functions (UDFs)** are custom functions registered in Unity Catalog that implement the filtering or masking logic used by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies. Specifically, row filter policies and column mask policies reference UDFs to decide which rows to return and how to transform column values for non-exempt principals. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Role in Row Filter Policies

Row filter policies use a UDF to evaluate each row. The UDF accepts arguments specified in the `USING COLUMNS` clause of the policy definition. Rows for which the UDF returns `FALSE` are excluded from query results. The UDF’s return type must be `BOOLEAN`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Role in Column Mask Policies

Column mask policies use a UDF to transform column values. The policy’s `ON COLUMN` clause automatically binds the masked column’s current value as the first argument to the UDF. Additional arguments can be passed through the `USING COLUMNS` clause. The UDF’s return type must match or be castable to the column’s data type. The UDF returns either the original value or a masked version depending on the policy logic. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## UDF Implementation and Performance Considerations

Databricks recommends **SQL UDFs** for ABAC policies because they perform better than Python UDFs. Python UDFs registered in Unity Catalog are also supported, but the query optimizer cannot inline or optimize them the same way it can with SQL UDFs. This can lead to slower query execution. See Performance considerations for ABAC for guidance on UDF language selection. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## UDF Registration

UDFs used in ABAC policies must be registered in Unity Catalog. Administrators create the UDF using the standard Unity Catalog UDF creation workflow. The UDF’s name is then referenced in the `CREATE POLICY` statement. For full details, see User-defined functions (UDFs) in Unity Catalog. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Using UDFs in Policy Definitions

When creating a policy, the UDF name appears in the `ROW FILTER` or `COLUMN MASK` clause. For example:

```sql
CREATE POLICY regional_access_emea
ON CATALOG sales
ROW FILTER filter_by_region
TO `emea team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS rgn
USING COLUMNS (rgn, 'EMEA');
```

Column mask policies bind the masked column automatically and allow additional arguments:

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

The `USING COLUMNS` clause accepts aliases for matched columns, literal constants (quoted strings, numeric literals, `TRUE`/`FALSE`, `NULL`), in the order the UDF expects them. This design lets a single UDF be reused across multiple policies with different parameters. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Exclusions

GRANT policies (Beta) do not use UDFs. Their conditions are expressed inline in the policy definition without a separate function. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC) Overview](/concepts/attribute-based-access-control-abac.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [GRANT Policies (Beta)](/concepts/grant-policies-beta.md)
- User-Defined Functions (UDFs) in Unity Catalog
- [Policy Conditions and Built-in Functions (has_tag, has_tag_value)](/concepts/abac-policy-conditions-and-built-in-functions.md)

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
