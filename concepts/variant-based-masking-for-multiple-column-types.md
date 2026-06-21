---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a063d39957c4b59a1fce3f711ebd5cd18e63f52af3f0b7ea656281df0503b9e9
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - variant-based-masking-for-multiple-column-types
    - VMFMCT
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: VARIANT-based masking for multiple column types
description: Using a single VARIANT-accepting and VARIANT-returning masking UDF to handle columns of different types (INT, DOUBLE, DECIMAL, DATE, struct) without needing separate policies per type.
tags:
  - abac
  - column-masking
  - variant
  - data-governance
timestamp: "2026-06-19T09:17:56.319Z"
---

# VARIANT-based masking for multiple column types

**VARIANT-based masking** is a technique for writing a single ABAC column mask policy UDF that can handle multiple target column types — for example `INT`, `DOUBLE`, `DECIMAL(10,2)`, or even `STRUCT` columns — by using the `VARIANT` type as both the input and output of the masking function. Databricks automatically casts the function’s result to the target column’s data type following ANSI SQL standards. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Why use VARIANT-based masking

Without VARIANT, a governance team would need to write a separate masking UDF for every distinct numeric precision (or data type) that appears across their tables. A single VARIANT-based function reduces the number of UDFs and policies needed. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Mask multiple numeric types with a single function

The simplest approach is to define a UDF that accepts `VARIANT` and returns `VARIANT` with a constant masked value. Databricks casts the returned VARIANT to the column’s native type at query time. For example, the following function returns `0` for any numeric column, regardless of whether the column is `INT`, `DOUBLE`, or `DECIMAL`:

```sql
CREATE FUNCTION mask_numeric(val VARIANT)
RETURNS VARIANT
DETERMINISTIC
RETURN 0::VARIANT;
```

A single ABAC policy can then reference this function to mask all numeric columns tagged with a sensitive classification. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

If you need different masked values depending on the original data type, you can branch on the type using `schema_of_variant()`:

```sql
CREATE FUNCTION flexible_mask(data VARIANT)
RETURNS VARIANT
RETURN CASE
  WHEN schema_of_variant(data) = 'INT' THEN 0::VARIANT
  WHEN schema_of_variant(data) = 'DATE' THEN DATE'1970-01-01'::VARIANT
  WHEN schema_of_variant(data) = 'DOUBLE' THEN 0.00::VARIANT
  ELSE NULL::VARIANT
END;
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Mask struct columns with VARIANT

For Databricks Runtime 18.1 and above, you can also mask `STRUCT` columns by casting them to `VARIANT` within an ABAC column mask policy. The `schema_of_variant()` function can identify different struct shapes, and you can use `to_variant_object()` to selectively redact fields. Note that casting structs to `VARIANT` for masking is supported **only within ABAC column mask policies**, not in general SQL. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

The following example handles two different struct shapes and redacts the sensitive field in each:

```sql
CREATE FUNCTION flexible_mask(data VARIANT)
RETURNS VARIANT
RETURN CASE
WHEN schema_of_variant(data) = 'OBJECT<age: BIGINT, email: STRING>' THEN
  to_variant_object(named_struct('age', data:age, 'email', 'redacted'))
WHEN schema_of_variant(data) = 'OBJECT<id: BIGINT, ssn: STRING>' THEN
  to_variant_object(named_struct('id', data:id, 'ssn', 'xxx-xx-xxxx'))
ELSE NULL::VARIANT
END;
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Cast compatibility and overflow

When using any column mask UDF, Databricks automatically casts the function output to match the target column’s data type (see Cast compatibility). For VARIANT-based masks, the same automatic casting applies. If the returned VALUE overflows the target column’s range (for example, returning a `BIGINT` for a `TINYINT` column), the query fails at runtime. Always verify that the masked value fits the target column’s type. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – The policy type that uses these UDFs.
- [User-defined function (UDF)](/concepts/abac-user-defined-functions-udfs.md) – The mechanism for implementing masking logic.
- VARIANT type – The semi-structured type used as the function’s parameter.
- Cast compatibility – Rules for automatic type casting in column masks.
- [Core concepts for ABAC](/concepts/governed-tags-for-abac-policies.md) – Foundational reading for attribute-based access control.

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
