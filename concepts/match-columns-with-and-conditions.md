---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 933bf57a329e3a4d6a6bd5ecd64c56c361f25f53ed09119c68ede87d0111d609
  pageDirectory: concepts
  sources:
    - implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - match-columns-with-and-conditions
    - conditions AND MATCH COLUMNS with
    - MCWAC
    - MATCH COLUMNS
  citations:
    - file: implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md
title: MATCH COLUMNS with AND conditions
description: Using logical AND inside MATCH COLUMNS to target columns that satisfy multiple tag criteria simultaneously, enabling fine-grained policy targeting across tag dimensions.
tags:
  - unity-catalog
  - sql-patterns
  - access-control
timestamp: "2026-06-19T19:09:36.023Z"
---

# MATCH COLUMNS with AND Conditions

**MATCH COLUMNS with AND Conditions** is a syntax feature in [Unity Catalog](/concepts/unity-catalog.md) access control policies (column masks and row filters) that allows the policy to target only those columns that satisfy multiple tag constraints simultaneously. By combining multiple `has_tag()` or `has_tag_value()` predicates with the `AND` operator inside the `MATCH COLUMNS` clause, administrators can write a single policy that applies to a precise subset of columns rather than creating separate policies for each tag combination. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Syntax

Within a `COLUMN MASK` or `ROW FILTER` policy definition, the `MATCH COLUMNS` clause accepts a parenthesized Boolean expression that references one or more tag functions. The AND operator links the conditions:

```
MATCH COLUMNS (
  has_tag_value('domain', 'hr')
  AND has_tag_value('sensitivity', 'internal')
) AS m
ON COLUMN m
```

The result of the expression determines which columns are covered by the policy. Only columns that have **both** the required tag key/value pairs will be matched. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Use Case: Multi‑Domain Column Masking with Sensitivity Tiers

The primary documented use case for `MATCH COLUMNS` with AND conditions is the tutorial for implementing domain-aware column masking with sensitivity tiers. In that scenario, an organization maintains a shared `employee_records` table where each sensitive column is tagged with a `domain` tag (e.g., `hr`, `finance`, `marketing`) and a `sensitivity` tag (`internal` or `confidential`). ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

The combination of the two tags is unique for each column, so a single policy can target, for example, all columns that belong to the **hr** domain and have an **internal** sensitivity level. The AND condition ensures that a column must match both criteria before the policy applies. This avoids the need for a separate policy for every individual column. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Interaction with the EXCEPT Clause

When `MATCH COLUMNS` with AND conditions is combined with the `TO … EXCEPT …` clause, the policy applies to all columns matching the AND condition except for users belonging to specific groups. This pattern is used to grant owning teams unmasked access to their own columns while masking those columns for everyone else. Since each column has exactly one `domain` and one `sensitivity` value, each column is matched by exactly one policy per user, preventing policy conflicts. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Example

The following policy creates a column mask that applies only to columns tagged with both `domain = 'hr'` and `sensitivity = 'internal'`. Members of the `hr_team` are exempted and see the raw values; all other users see a partial mask (`first character + ***`). ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

```sql
CREATE POLICY mask_internal_hr
ON SCHEMA my_schema
COLUMN MASK my_db.partial_mask
TO `account users` EXCEPT `hr_team`
FOR TABLES
MATCH COLUMNS (
  has_tag_value('domain', 'hr')
  AND has_tag_value('sensitivity', 'internal')
) AS m
ON COLUMN m;
```

## Benefits

- **Precision**: Targets columns that satisfy multiple tag conditions simultaneously, reducing the risk of accidentally masking or filtering unintended columns. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]
- **Scalability**: Adding a new domain or sensitivity level requires only a new policy and new tags; existing policies remain unchanged. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]
- **Clarity**: The policy’s intent is explicit: it applies to columns that are *both* of a certain type *and* of a certain sensitivity. ^[implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md]

## Related Concepts

- [MATCH COLUMNS](/concepts/match-columns-with-and-conditions.md) — The base clause for tag‑based column selection.
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policies that transform column values at read time.
- [Row Filter Policies](/concepts/row-filter-policies.md) — Policies that filter rows based on tags.
- [Unity Catalog governed tags](/concepts/unity-catalog-system-governed-tags.md) — The tagging system that `MATCH COLUMNS` relies on.
- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) — The broader access control model.
- has_tag_value() — The function that checks a specific tag key/value pair.

## Sources

- implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md

# Citations

1. [implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws.md](/references/implement-multi-domain-column-masking-with-sensitivity-tiers-databricks-on-aws-e7fa5eba.md)
