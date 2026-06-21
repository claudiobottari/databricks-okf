---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a41d9315edbb60b1d5c6b48042217cacc2da28a5b5d59f0cd322daa03cb6ad5f
  pageDirectory: concepts
  sources:
    - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pythonscala-udf-wrapper-pattern-for-column-masks
    - PUWPFCM
  citations:
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
    - file: ^@
title: Python/Scala UDF Wrapper Pattern for Column Masks
description: The requirement to wrap Python or Scala UDFs in a SQL UDF before applying them as row filters or column masks, because only SQL UDFs can be directly assigned as filters or masks.
tags:
  - unity-catalog
  - udf
  - python
  - scala
timestamp: "2026-06-19T19:30:59.839Z"
---

# Python/Scala UDF Wrapper Pattern for Column Masks

The **Python/Scala UDF Wrapper Pattern** is a required architectural pattern for applying column masks that use Python or Scala logic in [Unity Catalog](/concepts/unity-catalog.md). Because Unity Catalog column masks and row filters can only accept SQL user-defined functions (UDFs), any masking logic written in Python or Scala must be wrapped in a SQL UDF before it can be applied to a table column. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Motivation

When you need to implement complex masking logic—such as regular expression transformations, data format conversions, or other operations not easily expressed in SQL—you must write the logic as a Python or Scala UDF. However, Unity Catalog requires that the function applied as a column mask be a SQL UDF. The wrapper pattern bridges this gap by creating a thin SQL function that delegates execution to the underlying Python or Scala implementation. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## How the Pattern Works

The pattern consists of two steps:

1. **Create the Python or Scala UDF** containing the actual masking logic.
2. **Create a SQL wrapper function** that calls the Python or Scala UDF.

The SQL wrapper function is what you apply as the column mask on your table. The Python or Scala UDF is never applied directly. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Example: Email Masking with Python

This example demonstrates the pattern by creating a Python UDF that masks email addresses, then wrapping it in a SQL UDF:

### Step 1: Create the Python UDF

```sql
CREATE OR REPLACE FUNCTION email_mask_python(email STRING)
RETURNS STRING
LANGUAGE PYTHON
AS $$
import re
return re.sub(r'^[^@]+', lambda m: '*' * len(m.group()), email)
$$;
```

The Python UDF uses a regular expression to replace the local part of the email address (everything before the `@` symbol) with asterisks, preserving the length. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

### Step 2: Create the SQL Wrapper

```sql
CREATE OR REPLACE FUNCTION email_mask_sql(email STRING)
RETURN email_mask_python(email);
```

This SQL wrapper function simply delegates to the Python UDF. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

### Step 3: Apply the SQL Wrapper as a Column Mask

```sql
CREATE TABLE contacts (
  name STRING,
  email STRING MASK email_mask_sql
);
```

Only the SQL wrapper function (`email_mask_sql`) is applied as the column mask. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Important Requirements

- **Type matching**: UDF parameter types must match the data types of the table columns passed to them. If a column type differs from the UDF parameter type, the column value is implicitly cast. With ANSI mode disabled, values that can't be cast are silently converted to `NULL`, which can cause the mask to produce incorrect results without raising an error. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]
- **Direct application is not allowed**: You must apply the SQL wrapper function as the column mask, not the Python or Scala UDF directly. Attempting to use the Python UDF directly results in a `[ROUTINE_NOT_FOUND]` error. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]
- **Function registration**: Both the Python/Scala UDF and the SQL wrapper function must be registered in Unity Catalog. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Prerequisites

To use this pattern, you must have: ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

- A workspace enabled for [Unity Catalog](/concepts/unity-catalog.md).
- The `EXECUTE` privilege on the function, `USE SCHEMA` on the schema, and `USE CATALOG` on the parent catalog.
- Appropriate privileges for altering tables (table ownership or `MANAGE` privilege for existing tables; `CREATE TABLE` for new tables).

## Related Concepts

- Column Masks — Overview of column-level masking in Unity Catalog.
- [Row Filters](/concepts/row-filter-policies.md) — Row-level filtering using similar SQL UDF patterns.
- SQL UDFs — The function type required for direct application as column masks.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance framework that enforces these policies.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — An alternative centralized approach for managing access policies.

## Sources

- manually-apply-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
2. ^@
