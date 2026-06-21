---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b575a3af409149f123e3fcb2d49d3753aa0aa285877162ab76979d782dea3f1
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - variant-based-masking-functions-for-multiple-column-types
    - VMFFMCT
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: VARIANT-based masking functions for multiple column types
description: Using a single VARIANT-accepting UDF to mask columns of different data types (INT, DOUBLE, DECIMAL, DATE, etc.) and even struct columns, reducing the number of UDFs and policies needed.
tags:
  - abac
  - column-masking
  - variant
  - udf
timestamp: "2026-06-19T14:18:38.878Z"
---

```markdown
---
title: VARIANT-based masking functions for multiple column types
summary: Using a single VARIANT-accepting and VARIANT-returning UDF to mask columns of different data types (INT, DOUBLE, DECIMAL, DATE, struct) in ABAC policies.
sources:
  - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:01:58.562Z"
updatedAt: "2026-06-18T11:01:58.562Z"
tags:
  - abac
  - column-masking
  - variant
  - unity-catalog
aliases:
  - variant-based-masking-functions-for-multiple-column-types
  - VMFFMCT
confidence: 0.97
provenanceState: extracted
inferredParagraphs: 0
---

# VARIANT-based masking functions for multiple column types

**VARIANT-based masking functions** are a pattern for creating a single User-Defined Function (UDF)|masking UDF that can handle columns of different data types (such as `INT`, `DOUBLE`, `DECIMAL(10,2)`, `DECIMAL(15,5)`, and struct types) within [[Attribute-Based Access Control (ABAC)|ABAC]] [[column mask policies]]. Instead of writing separate masking functions for each column type, one function handles all types by accepting and returning the `VARIANT` datatype.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

Databricks automatically casts the masking function output to match the target column's data type following ANSI SQL standards. This automatic casting is what makes the single-function approach possible.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Benefits

Using VARIANT-based masking reduces the number of UDFs and policies needed. Rather than creating separate mask functions for each numeric precision (such as one for `INT`, another for `DOUBLE`, and yet another for each `DECIMAL` variant), one function handles all types.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Mask multiple numeric types with a single function

The simplest approach returns a literal value cast to `VARIANT`, which Databricks then automatically casts to the target column's type:

```sql
CREATE FUNCTION mask_numeric(val VARIANT)
RETURNS VARIANT
DETERMINISTIC
  RETURN 0::VARIANT;
```

This function returns `0` as a `VARIANT`. A single ABAC policy using this function can mask `INT`, `DOUBLE`, and `DECIMAL` columns without requiring separate functions for each precision.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

If you prefer to preserve the type explicitly within the function, you can branch on the type using `schema_of_variant()` and return an appropriate masked value for each:

```sql
-- Use VARIANT to accommodate different data types
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

For Databricks Runtime 18.1 and above, you can also mask struct columns by casting them to `VARIANT` within an ABAC policy. Branch on the struct's shape to selectively redact fields.

> **Note**: Casting structs to `VARIANT` for masking is supported only within ABAC column mask policies.

The following example uses `schema_of_variant()` to identify two different struct shapes and redact sensitive fields in each:

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

## How automatic type casting works

When you apply a VARIANT-based masking function as a [[Column Mask Policies|column mask policy]], Databricks automatically casts the `VARIANT` output to match the target column's data type. This means:

- A function returning `0::VARIANT` applied to an `INT` column results in the integer `0`.
- The same function applied to a `DOUBLE` column results in `0.0`.
- The same function applied to a `DECIMAL(10,2)` column results in `0.00`.

This automatic casting follows ANSI SQL standards and is the mechanism that enables a single masking function to cover multiple column types.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related concepts

- [[ABAC column mask policies]] — The policies that apply masking UDFs to columns
- [[Cast-compatible masking functions]] — Broader pattern for designing functions that return castable types
- User-Defined Function (UDF) — Functions used as the implementation for ABAC policies
- [[Attribute-Based Access Control (ABAC)]] — The access control model that uses these policies
- [[Row filter policies]] — Related ABAC policies that filter rows instead of masking columns
- Common patterns for ABAC policies — Additional design patterns for row filtering and column masking

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
```

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
