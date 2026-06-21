---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a578efb7ba8e1d877d2840fe5eb5a607f72f59eae4ea51643aab31732950602
  pageDirectory: concepts
  sources:
    - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-mask-for-nested-struct-fields
    - CMFNSF
  citations:
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
title: Column Mask for Nested STRUCT Fields
description: A technique to apply column masks to individual fields within a STRUCT column by reconstructing the STRUCT with named_struct(), conditionally redacting sensitive sub-fields.
tags:
  - unity-catalog
  - column-masks
  - nested-data
timestamp: "2026-06-19T19:30:38.929Z"
---

# Column Mask for Nested STRUCT Fields

**Column Mask for Nested STRUCT Fields** is a feature in [Unity Catalog](/concepts/unity-catalog.md) that allows fine-grained access control on individual fields within a `STRUCT` column. By applying a column mask to a nested structure, you can selectively redact sensitive sub-fields while preserving other fields, enabling different access levels based on user attributes such as group membership. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## How It Works

To mask nested `STRUCT` fields, you create a masking function (UDF) that reconstructs the `STRUCT` using `named_struct()`. The function conditionally replaces sensitive field values (for example, with `'REDACTED'`) while keeping other fields intact. The function’s return type must match the original `STRUCT` type exactly to avoid schema mismatches during `INSERT`, `MERGE`, and `UPDATE` operations. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

Commonly, the function uses `is_account_group_member()` to check whether the current user belongs to a privileged group. If the user is a member of the group, the function returns the original `STRUCT`; otherwise it returns the reconstructed `STRUCT` with the sensitive field redacted. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Example

Consider a `STRUCT` column containing both a public `value` field and a sensitive `secret` field. The following SQL function masks the `secret` field for users who are not in the `privileged_users` group.

```sql
CREATE OR REPLACE FUNCTION mask_nested_field(data STRUCT<value: STRING, secret: STRING>)
RETURN IF(
  is_account_group_member('privileged_users'),
  data,
  named_struct('value', data.value, 'secret', 'REDACTED')
);
```
^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

Apply the mask when creating a table:

```sql
CREATE TABLE sensitive_data (
  id INT,
  nested_column STRUCT<value: STRING, secret: STRING>
    MASK mask_nested_field
);
```
^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

You can also apply the mask to an existing table using `ALTER TABLE`:

```sql
ALTER TABLE sensitive_data
  ALTER COLUMN nested_column
  SET MASK mask_nested_field;
```
^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

After the mask is in place, a query by a non‑privileged user returns redacted secrets while the `value` field remains visible:

```sql
SELECT * FROM sensitive_data;
-- 1  {"value":"public_info","secret":"REDACTED"}
-- 2  {"value":"general_data","secret":"REDACTED"}
```
^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Important Considerations

- The masking function must return a value with the same `STRUCT` type as the masked column. In the example, the return type is `STRUCT<value: STRING, secret: STRING>`. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]
- The function’s first parameter maps to the column being masked. No `USING COLUMNS` clause is required when the function only depends on the masked column itself. For masks that need additional column values, see the general Column Mask pattern with `USING COLUMNS`.
- The same UDF requirements apply as for any column mask: the function must be a SQL UDF registered in Unity Catalog; Python or Scala logic must first be wrapped in a SQL UDF. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Related Concepts

- Column Mask — General mechanism for masking column values at query time.
- [Row Filter](/concepts/row-filter-policies.md) — Row‑level filtering using a similar function‑based approach.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that supports row filters and column masks.
- is_account_group_member — Function used to check group membership inside mask logic.
- named_struct — Function used to reconstruct `STRUCT` values in a mask.
- STRUCT type — Databricks data type for nested, complex structures.

## Sources

- manually-apply-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
