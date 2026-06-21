---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d25870dd5566f77ca050a0b6cfb2f25736a71eb5759d191554872f422c7133c
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cast-compatible-masking-functions
    - CMF
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Cast-compatible masking functions
description: Patterns for designing row filter and column mask UDFs where the return type is automatically cast to match the target column's data type, including techniques to avoid numeric overflow and return compatible types in all branches.
tags:
  - data-governance
  - abac
  - column-masking
  - unity-catalog
timestamp: "2026-06-19T17:46:55.171Z"
---

```markdown
---
title: Cast-compatible masking functions
summary: Patterns for designing column mask UDFs that return types safely castable to the target column's data type, including avoiding numeric overflow and using VARIANT for multi-type support.
sources:
  - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:02:14.462Z"
updatedAt: "2026-06-19T14:18:17.072Z"
tags:
  - abac
  - column-masking
  - data-governance
  - type-safety
aliases:
  - cast-compatible-masking-functions
  - CMF
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Cast-compatible masking functions

**Cast-compatible masking functions** are user-defined functions (UDFs) used in [[Column Mask Policies]] that are designed to return values Databricks can automatically cast to the target column's data type according to ANSI SQL standards. Databricks performs this automatic cast when applying the mask to the column.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Return a castable type

When masking a column, return the same data type as the column or a type that is castable to it. Check the data types of the columns your policy targets and verify that every branch of the function returns a compatible value.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

The following example succeeds because it masks a `DOUBLE` column and returns `DOUBLE` in every branch:

```sql
CREATE FUNCTION mask_salary(salary DOUBLE, user_role STRING)
RETURNS DOUBLE
RETURN CASE
  WHEN user_role IN ('admin', 'hr') THEN salary
  WHEN user_role = 'manager' THEN ROUND(salary / 1000) * 1000
  ELSE 0.0
END;
```

The following example fails because `'CONFIDENTIAL'` cannot be cast to a `DOUBLE` column type:

```sql
CREATE FUNCTION mask_salary_as_text(salary DOUBLE, user_role STRING)
RETURNS STRING
RETURN CASE
  WHEN user_role IN ('admin', 'hr') THEN CAST(salary AS STRING)
  ELSE 'CONFIDENTIAL'
END;
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Avoid numeric overflow

When a mask function accepts and returns a wider numeric type than the target column, the result is automatically cast back to the column's narrower type. If the returned value exceeds the range of the narrower type, the cast overflows and the query fails at runtime.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

```sql
-- The target column is TINYINT (max 127). The input is upcast to BIGINT
-- for the function. Adding 1000 produces a BIGINT result that overflows
-- when cast back to TINYINT.
CREATE FUNCTION mask_score(score BIGINT)
RETURNS BIGINT
RETURN score + 1000;
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Use VARIANT for multiple column types

When you need to mask columns of different data types (for example, `INT`, `DOUBLE`, `DECIMAL(10,2)`, `DECIMAL(15,5)`), you can write a single masking UDF that accepts and returns a `VARIANT` type. Databricks automatically casts the output to match the target column's type. This reduces the number of UDFs and policies needed.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Mask multiple numeric types with a single function

Rather than creating a separate mask function for each numeric precision, use `VARIANT` to handle them all with one function:

```sql
CREATE FUNCTION mask_numeric(val VARIANT)
RETURNS VARIANT
DETERMINISTIC
RETURN 0::VARIANT;
```

This function returns `0` as a `VARIANT`, which Databricks automatically casts to the target column's type. A single ABAC policy using this function can mask `INT`, `DOUBLE`, and `DECIMAL` columns without requiring separate functions for each precision. If you prefer to preserve the type explicitly within the function, you can branch on the type using [`schema_of_variant()`](https://docs.databricks.com/aws/en/semi-structured/variant#return-the-schema-of-a-variant) and return an appropriate masked value for each:

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

### Mask struct columns with VARIANT

For Databricks Runtime 18.1 and above, you can also mask struct columns by casting them to `VARIANT` within an ABAC policy. Use `schema_of_variant()` to branch on the struct's shape and selectively redact fields:

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

Note: Casting structs to `VARIANT` for masking is supported only within ABAC column mask policies.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Test cast compatibility

Test masking functions with different data patterns to verify cast compatibility:

```sql
SELECT CAST(mask_salary(salary, 'admin') AS DOUBLE) FROM employees;
SELECT CAST(mask_salary(salary, 'manager') AS DOUBLE) FROM employees;
SELECT CAST(mask_salary(salary, 'viewer') AS DOUBLE) FROM employees;
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related concepts

- [[VARIANT-based masking functions for multiple column types]] — A pattern that uses `VARIANT` to handle columns of different data types with a single masking UDF.
- [[Column Mask Policies]] — ABAC policies that mask sensitive column values.
- [[Row Filter Policies]] — ABAC policies that restrict which rows are visible.
- [[Attribute-Based Access Control (ABAC)]] — The access control model that these policies implement.
- [[Unity Catalog]] — The governance layer providing ABAC capabilities.

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
```

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
