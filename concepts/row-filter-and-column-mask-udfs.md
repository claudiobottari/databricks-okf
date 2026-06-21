---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1f52c12cb45d6ee84219fed1dc42eb3a511f8767e2aedd0dfcb0834c412d52f
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-filter-and-column-mask-udfs
    - Column Mask UDFs and Row Filter
    - RFACMU
    - Column Mask UDF
    - Row Filter UDF
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Row Filter and Column Mask UDFs
description: User-defined functions used by row filter and column mask policies to implement filtering or masking logic, with SQL UDFs recommended for performance over Python UDFs.
tags:
  - udf
  - sql
  - data-filtering
timestamp: "2026-06-19T14:27:32.931Z"
---

# Row Filter and Column Mask UDFs

**Row Filter and Column Mask UDFs** are user-defined functions (UDFs) registered in [Unity Catalog](/concepts/unity-catalog.md) that implement the filtering or masking logic used by [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md) and [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md). These UDFs determine which rows a user can see or how column values are presented when a policy’s tag-based conditions are met. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## How UDFs Work in ABAC Policies

In Unity Catalog’s ABAC model, row filter and column mask policies reference a UDF that evaluates per-row or per-column values. The policy’s `USING COLUMNS` clause passes arguments to the UDF. For row filters, the UDF returns a boolean: rows where the function returns `FALSE` are excluded from query results. For column masks, the UDF returns the original value or a masked version, and the return type must match or be castable to the column’s data type. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Row Filter UDF Example

A row filter UDF takes arguments that represent column values and returns a boolean. The policy passes those arguments via `USING COLUMNS`, using aliases from the `MATCH COLUMNS` clause or constant values. 

```sql
CREATE FUNCTION filter_by_region(region STRING, allowed STRING) RETURNS BOOLEAN
    RETURN region = allowed;

CREATE POLICY regional_access_emea
ON CATALOG sales
ROW FILTER filter_by_region
TO `emea team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS rgn
USING COLUMNS (rgn, 'EMEA');
```

In this example, `filter_by_region` receives the value from the column tagged `region` and the constant `'EMEA'`. The policy applies the filter to all tables in the `sales` catalog that have a column tagged `region`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Column Mask UDF Example

A column mask UDF takes the column value as its first argument (automatically bound from the `ON COLUMN` clause) and can accept additional arguments through `USING COLUMNS`. The function must return a value of the same type as the masked column (or a castable type).

```sql
CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING
    RETURN CONCAT('***-**-', RIGHT(ssn, show_last));

CREATE POLICY mask_ssn_columns
ON CATALOG hr_catalog
COLUMN MASK mask_ssn
TO `account users` EXCEPT `compliance team`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col
USING COLUMNS (4);
```

Here, `mask_ssn` receives the actual SSN value from the column tagged `pii : ssn` and the integer `4` to show the last four digits. The policy applies only to tables that have a column matching the tag condition. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Argument Passing

The `USING COLUMNS` clause in an ABAC policy passes arguments to the UDF. It accepts:

- Aliases for columns that match a tag-based expression (defined in the `MATCH COLUMNS` clause).
- Constant values: quoted strings, numeric literals, boolean values (`TRUE`/`FALSE`), or `NULL`.

Arguments are supplied in the order the function expects them. For column mask policies, the masked column’s value is automatically bound as the first argument from the `ON COLUMN` clause; additional arguments follow from `USING COLUMNS`. This design allows a single UDF to be reused across policies with different parameters. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## UDF Language Options

Databricks recommends using **SQL UDFs** for better performance because the query optimizer can inline and optimize them. **Python UDFs** registered in Unity Catalog are also supported, but the optimizer cannot inline or optimize them as effectively, which may lead to lower query performance. See [Performance considerations for ABAC policies](/concepts/best-practices-for-abac-grant-policies.md). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Permissions Required

To create an ABAC policy that references a row filter or column mask UDF, the creator must have:

- `MANAGE` permission or object ownership on the securable object where the policy is attached (e.g., the catalog, schema, or table).
- `EXECUTE` privilege on the UDF.

These permissions allow a governance admin to attach a policy that uses the UDF. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Relation to Other Policy Types

[ABAC GRANT Policies](/concepts/abac-grant-policy.md) do not use UDFs; instead, they grant privileges directly when tag-based conditions match. Row filter and column mask policies are the only types that rely on UDFs for their enforcement logic. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- User-defined functions (UDFs) in Unity Catalog
- Common patterns for row filtering and column masking
- [Governed Tags](/concepts/governed-tags.md)

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
