---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9fdebab874adf205873561f83d8e455a3e358bd53359a5e135d84a8018c3c019
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - variant-based-masking-functions
    - VMF
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: VARIANT-based masking functions
description: Using the VARIANT type to write a single masking UDF that handles multiple target column types (INT, DOUBLE, DECIMAL, DATE, STRUCT) by accepting and returning VARIANT, which Databricks automatically casts to the target column's type.
tags:
  - data-governance
  - abac
  - column-masking
  - unity-catalog
  - variant
timestamp: "2026-06-19T17:46:55.742Z"
---

# VARIANT-based Masking Functions

**VARIANT-based masking functions** refer to user-defined functions (UDFs) used in [Column Mask Policies](/concepts/column-mask-policies.md) that accept and return the `VARIANT` type. This approach allows a single masking function to handle columns of different data types (e.g., `INT`, `DOUBLE`, `DECIMAL(10,2)`, `DATE`, `STRING`) instead of writing a separate function for each type. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Overview

When a column mask UDF accepts and returns `VARIANT`, Databricks automatically casts the function's output to match the target column's data type following ANSI SQL standards. This reduces the number of UDFs and policies needed. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Mask Multiple Numeric Types with a Single Function

Instead of creating a separate mask function for each numeric precision (e.g., `TINYINT`, `INT`, `DOUBLE`, `DECIMAL`), you can use `VARIANT` to handle them all:

```sql
CREATE FUNCTION mask_numeric(val VARIANT)
RETURNS VARIANT
DETERMINISTIC
RETURN 0::VARIANT;
```

This function returns `0` as a `VARIANT`, which Databricks automatically casts to the target column's type. A single ABAC policy using this function can mask `INT`, `DOUBLE`, and `DECIMAL` columns. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Branching on Type with `schema_of_variant()`

To preserve type information explicitly or apply different masking logic per type, you can branch on the type using [`schema_of_variant()`](https://docs.databricks.com/aws/en/semi-structured/variant#return-the-schema-of-a-variant): ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

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

## Masking Struct Columns with VARIANT

For Databricks Runtime 18.1 and above, you can also mask struct columns by casting them to `VARIANT` within an ABAC column mask policy. Use `schema_of_variant()` to identify the struct's shape and selectively redact fields. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

> **Note**: Casting structs to `VARIANT` for masking is supported only within ABAC column mask policies. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

Example: redact `email` in one struct shape and `ssn` in another:

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

## Related Concepts

- [Column Mask Policies](/concepts/column-mask-policies.md) — The ABAC policy type that invokes masking UDFs
- ABAC policies — Attribute-based access control policies in Unity Catalog
- VARIANT type — Databricks semi-structured data type that accommodates multiple column types
- schema_of_variant — Function used to inspect the schema of a VARIANT value
- Common patterns for row filtering and column masking — Broader guidance on ABAC masking

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
