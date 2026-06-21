---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc7f33de449cd65143134c3a9107bd97f4fbf420275a62210b8abbb12b59c358
  pageDirectory: concepts
  sources:
    - secure-new-tables-by-default-with-control-tags-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systemdata_classificationmask_value
  citations:
    - file: secure-new-tables-by-default-with-control-tags-databricks-on-aws.md
title: system.data_classification.mask_value
description: A built-in, type-aware masking UDF in Databricks that returns safe placeholder values based on column data types (e.g., 0 for integers, SHA-256 hash for strings, DATE '1970-01-01' for dates).
tags:
  - unity-catalog
  - masking
  - udf
timestamp: "2026-06-19T20:20:16.938Z"
---

# system.data_classification.mask_value

**`system.data_classification.mask_value`** is a built-in, type-aware masking function provided by Databricks as part of the Unity Catalog [Data Classification](/concepts/data-classification.md) system. It returns a safe placeholder value based on the runtime data type of the column being masked, enabling column-level security without requiring custom user-defined functions (UDFs). ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Overview

The function is designed for use in [Column Masking Policies](/concepts/column-mask-policies.md) to automatically obscure sensitive data. When applied to a column, `system.data_classification.mask_value` replaces the original value with a type-appropriate placeholder. For example, it returns `0` for integer columns, `DATE '1970-01-01'` for date columns, and a SHA-256 hash for string columns. This type-awareness ensures that masked values remain compatible with the column's schema, preventing type errors in downstream queries. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Usage

`system.data_classification.mask_value` is invoked inside a `COLUMN MASK` clause when creating or altering a masking policy. It does not require any arguments — the function automatically detects the column's data type and applies the appropriate masking logic. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

### Example in a Masking Policy

The following example creates a policy that masks all columns in a schema when a table has `review_status = pending`:

```sql
CREATE POLICY review_pending_policy
ON SCHEMA abac_tutorial.secure_default
COLUMN MASK system.data_classification.mask_value
TO `account users`
FOR TABLES
WHEN has_tag_value('review_status', 'pending')
MATCH COLUMNS TRUE AS m
ON COLUMN m;
```

^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

In this policy:
- `MATCH COLUMNS TRUE` applies the mask to every column in the table.
- `system.data_classification.mask_value` handles the actual masking logic.
- The `TO` clause specifies which roles or users the policy applies to.

### Selective Masking with Tags

The function can also be used in policies that mask only columns tagged with specific System Governed Tags (e.g., `class.name`, `class.email_address`, `class.us_ssn`):

```sql
CREATE POLICY review_complete_policy
ON SCHEMA abac_tutorial.secure_default
COLUMN MASK system.data_classification.mask_value
TO `account users`
FOR TABLES
WHEN has_tag_value('review_status', 'reviewed')
MATCH COLUMNS (
  has_tag('class.name')
  OR has_tag('class.email_address')
  OR has_tag('class.us_ssn')
  OR has_tag('class.phone_number')
  OR has_tag('class.credit_card')
  OR has_tag('class.date_of_birth')
) AS m
ON COLUMN m;
```

^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Type-Aware Masking Behavior

The function's key advantage is its type-awareness. The exact placeholder returned depends on the column's SQL data type:

| Data Type | Masked Value |
|-----------|--------------|
| `INT`, `BIGINT`, etc. | `0` |
| `DATE` | `DATE '1970-01-01'` |
| `STRING` | SHA-256 hash of the original value |
| Other types | Type-appropriate safe placeholder |

^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Requirements

- Databricks Runtime 16.4 or above, or serverless compute. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
- The user must have `EXECUTE` permission on the function (typically granted automatically when using Unity Catalog). ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The system that automatically detects and tags sensitive columns with `class.*` tags.
- [Column Masking Policies](/concepts/column-mask-policies.md) — The broader mechanism for applying masks to columns based on conditions.
- System Governed Tags — Predefined tags like `class.name` and `class.email_address` used to identify sensitive data.
- Control Tags — User-defined tags (e.g., `review_status`) that control which masking policy applies.
- Secure New Tables by Default — A tutorial pattern that uses `system.data_classification.mask_value` to lock down new tables automatically.

## Sources

- secure-new-tables-by-default-with-control-tags-databricks-on-aws.md

# Citations

1. [secure-new-tables-by-default-with-control-tags-databricks-on-aws.md](/references/secure-new-tables-by-default-with-control-tags-databricks-on-aws-955564d7.md)
