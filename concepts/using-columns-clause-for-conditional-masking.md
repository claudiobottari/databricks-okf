---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 671f5f476089ce6494c660c51066d9d55313f5d98b8ec8197956d7149303e528
  pageDirectory: concepts
  sources:
    - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - using-columns-clause-for-conditional-masking
    - UCCFCM
  citations:
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
title: Using Columns Clause for Conditional Masking
description: A pattern enabling column masks to reference additional columns or static parameters via the USING COLUMNS clause, allowing conditional logic based on values beyond the masked column itself.
tags:
  - unity-catalog
  - column-masks
  - conditional-masking
timestamp: "2026-06-19T19:30:28.848Z"
---

# Using Columns Clause for Conditional Masking

The **`USING COLUMNS`** clause allows a column mask function to reference static parameters or other columns in the same table beyond the column being masked. This enables conditional masking logic that depends on data values elsewhere in the row, such as a country code or user group. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Purpose

Without `USING COLUMNS`, a masking function can only receive the value of the column it is applied to. When the masking decision must consider additional context — for example, “redact the address unless the user belongs to a group that matches the customer’s country” — the function needs access to other columns or static parameters. `USING COLUMNS` provides those extra arguments. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Syntax

When defining a column mask with `USING COLUMNS`:

- The **first parameter** of the masking function always maps to the masked column itself.
- **Additional parameters** are supplied using `USING COLUMNS`, which can include either column names from the same table or static literal values.

The masking function receives these additional arguments in the order they are listed in the `USING COLUMNS` clause. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Example

The following example creates a column mask that redacts addresses differently based on the value in another column (`country`). The function takes an additional parameter `group_suffix` (static) and uses the country column to build a group name. Only members of the resulting country-group pair can view addresses for that country.

```sql
-- Create a masking function that accepts two parameters:
-- 1. address (the masked column)
-- 2. country (an additional column used for conditional logic)
-- 3. group_suffix (group the user belongs to)
CREATE FUNCTION mask_address_by_country(
  address STRING,
  country STRING,
  group_suffix STRING DEFAULT '_address_viewers'
)
RETURN IF(
  is_account_group_member(country || group_suffix),
  address,
  'REDACTED'
);

-- Create a table and apply the mask using USING COLUMNS to pass the country column
-- and a static suffix.
CREATE TABLE customers (
  name STRING,
  address STRING MASK mask_address_by_country USING COLUMNS (country, '_address_viewers'),
  country STRING
);

-- Insert sample data
INSERT INTO customers VALUES
  ('Alice', '123 Main St, New York', 'US'),
  ('Bob',   '456 High St, London',   'UK'),
  ('Charlie','789 Rue de Rivoli, Paris','FR');
```

Query results depend on group membership. If the user is a member of `US_address_viewers`, they see US addresses but others are redacted:

```sql
-- As a member of 'US_address_viewers' group
SELECT * FROM customers;
  Alice    | 123 Main St, New York | US
  Bob      | REDACTED              | UK
  Charlie  | REDACTED              | FR
```

You can also apply the mask to an existing table using `ALTER TABLE`:

```sql
ALTER TABLE customers
  ALTER COLUMN address
  SET MASK mask_address_by_country USING COLUMNS (country, '_address_viewers');
```

^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Important Considerations

- **Data type matching**: UDF parameter types must match the data types of the columns passed to them. If a column type differs from the UDF parameter type, the column value is implicitly cast. With ANSI mode disabled, values that cannot be cast are silently converted to `NULL`, which can cause the mask to produce incorrect results without raising an error. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]
- Default values can be used for parameters that are not strictly required (as in the `group_suffix` example above).
- The `USING COLUMNS` clause is only applicable to column masks, not row filters.

## Related Concepts

- [Column mask](/concepts/column-mask-policies.md) — The fundamental mechanism for redacting column values.
- [Row filter](/concepts/row-filter-policies.md) — Row‑level filtering using similar function‑based policies.
- [Mapping tables](/concepts/mapping-tables-for-access-control.md) — An alternative approach for implementing access‑control lists.
- Data type mismatch behavior — How Databricks handles type mismatches in masking functions.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — A centralized, tag‑driven alternative to manual filters and masks.

## Sources

- manually-apply-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
