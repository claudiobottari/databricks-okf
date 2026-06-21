---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c26d4cee2921bef722f06108211ad4699de2d0e1abc84c24c57e2d4d5fe695d7
  pageDirectory: concepts
  sources:
    - use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conditional-column-masking
    - CCM
    - Conditional Masking
    - Data Masking
    - Dynamic Data Masking
  citations:
    - file: use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
title: Conditional Column Masking
description: A column masking technique where the mask applied to PII data depends on the value of another column on the same row (e.g., order_priority), allowing confidential rows to override user clearance levels.
tags:
  - data-governance
  - column-masking
  - PII
timestamp: "2026-06-19T23:22:52.529Z"
---

# Conditional Column Masking

**Conditional Column Masking** is a [data governance](/concepts/ai-governance.md) pattern in [Unity Catalog](/concepts/unity-catalog.md) where the masking applied to a Personally Identifiable Information (PII) column varies depending on the value of another column in the same row. It extends standard column masking by making the mask output sensitive to row-level attributes beyond the querying user's identity or clearance level. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Overview

In a standard column masking setup, a mask function receives only the column value and a static parameter indicating the PII type. Conditional masking adds a third parameter — the value of a second column on the same row — and uses that value to decide how aggressively to mask the PII. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

A common use case for conditional masking is **confidential orders**: when an order record is marked as `confidential`, its PII columns (`customer_name`, `customer_email`) are always fully redacted to `***REDACTED***`, regardless of the user's Clearance Level or PII Access Permission stored in a mapping table. This ensures that high-priority or sensitive records receive a stronger mask even for users who would normally have `full` PII visibility. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Implementation

Conditional column masking is implemented by passing the value of the second column into the mask User-Defined Function (UDF) at query time. The mechanism that enables this is Tag Matching with `MATCH COLUMNS`. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Tagging the trigger column

The column that drives the conditional masking — for example, `order_priority` — is tagged with a key-only [Governed Tag](/concepts/governed-tags.md). A column mask policy then uses `has_tag('priority')` in its `MATCH COLUMNS` clause to match the tagged column and pass its value to the mask UDF as an additional argument. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

```sql
ALTER TABLE orders
  ALTER COLUMN order_priority SET TAGS ('priority' = '');
```

### Creating the mask UDF with conditional logic

The mask UDF accepts three parameters: the column value to mask, the PII type indicator (e.g., `'name'` or `'email'`), and the row's priority value (e.g., `'standard'` or `'confidential'`). The UDF contains a `CASE` expression that checks the priority first: if the priority is `confidential`, it always returns the full-redaction string, bypassing any user-clearance lookups. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

```sql
CREATE OR REPLACE FUNCTION pii_mask(
  val STRING,
  pii_type STRING,
  order_pri STRING
) RETURNS STRING
RETURN CASE
  WHEN order_pri = 'confidential' THEN '***REDACTED***'
  WHEN EXISTS (
    SELECT 1 FROM user_access
    WHERE user_email = current_user() AND pii_access = 'full'
  ) THEN val
  WHEN EXISTS (
    SELECT 1 FROM user_access
    WHERE user_email = current_user() AND pii_access = 'masked'
  ) THEN
    CASE pii_type
      WHEN 'email' THEN CONCAT(LEFT(val, 1), '***@', SUBSTRING_INDEX(val, '@', -1))
      WHEN 'name'  THEN CONCAT(LEFT(val, 1), '***')
      ELSE CONCAT(LEFT(val, 1), '***')
    END
  ELSE '***REDACTED***'
END;
```

### Creating the column mask policy

The policy definition uses `MATCH COLUMNS` to match two sets of columns: the PII column (matched via `has_tag_value('pii', 'name')` or `has_tag_value('pii', 'email')`) and the priority column (matched via `has_tag('priority')`). The `USING COLUMNS` clause passes both the PII type constant and the row's priority value to the UDF. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

```sql
CREATE POLICY pii_mask_name
ON SCHEMA mapping_demo
COLUMN MASK pii_mask
TO `account users`
FOR TABLES
MATCH COLUMNS
  has_tag_value('pii', 'name') AS m,
  has_tag('priority') AS pri
ON COLUMN m
USING COLUMNS ('name', pri);
```

## Behavior

When a user queries a table protected by a conditional mask policy, the following evaluation occurs for each row: ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

1. The mask UDF receives the row's PII value, the PII type indicator, and the row's `order_priority` value.
2. If `order_priority` is `confidential`, the UDF returns `***REDACTED***` and the user-clearance lookup is skipped entirely.
3. If `order_priority` is `standard`, the UDF proceeds to check the user's clearance level in the Mapping Table and applies the appropriate mask (`full`, `masked`, or `none`).

This means that a user with `full` clearance still sees `***REDACTED***` on confidential rows — the row's own attribute overrides the user's permission. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Related Concepts

- [Mapping Tables](/concepts/mapping-tables-for-access-control.md) — A single table storing user access entries, used to drive both [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md).
- [Row Filter Policies](/concepts/row-filter-policies.md) — Controls which rows a user can see, based on region and department.
- [Column Mask Policies](/concepts/column-mask-policies.md) — Controls how PII values are displayed, with conditional logic.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The broader access control model that conditional masking implements.
- Tag-Based Matching — The mechanism that discovers which columns to pass to mask UDFs.
- Fail-Closed Design — Policy evaluation where unmatched users see no rows rather than all rows.
- [Access Expiration](/concepts/access-expiration-via-mapping-tables.md) — The `expires_on` pattern that silently revokes access without manual intervention.

## Sources

- use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md

# Citations

1. [use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md](/references/use-mapping-tables-for-dynamic-access-control-databricks-on-aws-cfb1e1c1.md)
