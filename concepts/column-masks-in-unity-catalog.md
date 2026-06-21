---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64ff04355bf99365def8a3c48def1996aaeec2b23b2dcc24e0caba03c6801c44
  pageDirectory: concepts
  sources:
    - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-masks-in-unity-catalog
    - CMIUC
  citations:
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
    - file: ^@
title: Column Masks in Unity Catalog
description: A column-level security feature that uses SQL UDFs to mask or transform column values at query time based on user identity or group membership.
tags:
  - data-governance
  - unity-catalog
  - column-security
timestamp: "2026-06-19T19:30:11.652Z"
---

# Column Masks in Unity Catalog

**Column Masks in Unity Catalog** are a Fine-Grained Access Control in Unity Catalog|fine-grained access control feature that allows you to apply data masking policies to specific columns in a table. When a column mask is applied, query results automatically transform the column's values according to the mask logic, typically based on the user's identity or group membership. Column masks are part of Databricks' [Unity Catalog](/concepts/unity-catalog.md) security framework and are used alongside [row filters](/concepts/row-filters-in-unity-catalog.md) to implement comprehensive data governance. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Overview

A column mask is created by writing a [User-Defined Function (UDF)|user-defined function (UDF)](/concepts/abac-user-defined-functions-udfs.md) that defines the masking logic and then applying that function to a table column. The UDF accepts one or more parameters: the first parameter always maps to the masked column itself, and additional parameters can be supplied via the `USING COLUMNS` clause to reference other columns in the same table or static values. The function returns a transformed value that replaces the original column value in query results. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Prerequisites

To apply column masks, you must have:
- A workspace enabled for Unity Catalog
- A SQL UDF registered in Unity Catalog (or a Python/Scala UDF wrapped in a SQL UDF)
- The `EXECUTE` privilege on the masking function
- The `USE SCHEMA` privilege on the schema and `USE CATALOG` on the parent catalog
- The `CREATE TABLE` privilege (for new tables) or table ownership/`MANAGE` privilege (for existing tables)

^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

Compute resources must use a SQL Warehouse, standard access mode (Databricks Runtime 12.2 LTS+), or dedicated access mode (Databricks Runtime 15.4 LTS+) to read tables with column masks. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Important Considerations

### Data Type Matching

UDF parameter types must match the data types of the columns passed to them. If a column type differs from the UDF parameter type, the column value is implicitly cast. With ANSI mode disabled, values that cannot be cast are silently converted to `NULL`, which can cause the mask to produce incorrect results without raising an error. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

### Mask Preservation on Table Replacement

When you run `REPLACE TABLE`, column masks are retained if the new table includes columns with the same names as those that had masks in the original table. This prevents accidental loss of data access policies. However, if a retained policy references a column that was removed or changed, subsequent queries might fail. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Applying Column Masks

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Browse or search for the table.
3. On the **Overview** tab, find the row you want to apply the column mask to and click the **Mask** edit icon.
4. On the **Add column mask** dialog, select the [Catalog and Schema](/concepts/catalog-and-schema.md) containing the masking function, then select the function.
5. If the function includes additional parameters beyond the column being masked, select the table columns for those parameters.
6. Click **Add**.

To remove the column mask, click **fx Column mask** in the table row and click **Remove**. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

### Using SQL

Apply a column mask when creating a table:

```sql
CREATE TABLE users (
  name STRING,
  ssn STRING MASK ssn_mask
);
```

Apply a column mask to an existing table:

```sql
ALTER TABLE users ALTER COLUMN ssn SET MASK ssn_mask;
```

Remove a column mask:

```sql
ALTER TABLE users ALTER COLUMN ssn DROP MASK;
```

^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Example: Basic Column Mask

This example creates a user-defined function that masks the `ssn` column so that only users who are members of the `HumanResourceDept` group can view values in that column:

```sql
CREATE FUNCTION ssn_mask(ssn STRING)
  RETURN CASE WHEN is_account_group_member('HumanResourceDept') THEN ssn ELSE '***-**-****' END;
```

Apply the mask to a table:

```sql
CREATE TABLE users (
  name STRING,
  ssn STRING MASK ssn_mask
);
```

When a non-member of `HumanResourceDept` queries the table, the `ssn` column shows `***-**-****` for all rows. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Advanced Usage

### Column Mask with Python UDF

To use Python or Scala logic in a column mask, create a Python or Scala UDF, then wrap it in a SQL UDF. The SQL wrapper function is what you apply as the column mask:

```sql
-- Step 1: Create the Python UDF with masking logic
CREATE OR REPLACE FUNCTION email_mask_python(email STRING)
RETURNS STRING
LANGUAGE PYTHON
AS $
import re
return re.sub(r'^[^@]+', lambda m: '*' * len(m.group()), email)
$;

-- Step 2: Create a SQL wrapper function
CREATE OR REPLACE FUNCTION email_mask_sql(email STRING)
RETURN email_mask_python(email);

-- Step 3: Apply the SQL wrapper as the column mask
CREATE TABLE contacts (
  name STRING,
  email STRING MASK email_mask_sql
);
```

You must apply the SQL wrapper function as the column mask, not the Python UDF directly. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

### Column Mask with Additional Columns (`USING COLUMNS`)

Use the `USING COLUMNS` clause when a masking function must reference other columns or static parameters. This enables conditional masking based on values beyond the column being masked:

```sql
-- Create a masking function with an additional parameter
CREATE FUNCTION mask_address_by_country(address STRING, country STRING, group_suffix STRING DEFAULT '_address_viewers')
RETURN IF(
  is_account_group_member(country || group_suffix),
  address,
  'REDACTED'
);

-- Apply the mask using USING COLUMNS
CREATE TABLE customers (
  name STRING,
  address STRING MASK mask_address_by_country USING COLUMNS (country, '_address_viewers'),
  country STRING
);
```

In this example, users see addresses only for countries where they are members of the corresponding group (e.g., `US_address_viewers` for US addresses). ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

### Column Mask for Nested `STRUCT` Fields

You can apply column masks to nested `STRUCT` columns to selectively mask specific fields within the structure:

```sql
CREATE FUNCTION mask_nested_field(data STRUCT<value: STRING, secret: STRING>)
RETURN IF(
  is_account_group_member('privileged_users'),
  data,
  named_struct('value', data.value, 'secret', 'REDACTED')
);

CREATE TABLE sensitive_data (
  id INT,
  nested_column STRUCT<value: STRING, secret: STRING>
    MASK mask_nested_field
);
```

The masking function should return a value with the same STRUCT type as the masked column to avoid schema mismatches during `INSERT`, `MERGE`, and `UPDATE` operations. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Relationship with Other Features

- [Row Filters in Unity Catalog](/concepts/row-filters-in-unity-catalog.md) — Filter entire rows from query results, complementing column-level masking
- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) — Centralized tag-based approach for managing access policies across many tables
- User-Defined Functions (UDFs) in Unity Catalog — Functions used to define masking logic
- [Mapping Tables for Access Control](/concepts/mapping-tables-for-access-control.md) — Tables used to define access-control lists for row-level security

## Sources

- manually-apply-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
2. ^@
