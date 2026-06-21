---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd0b2fa68676e1936f66d9aa2bf753a6c1fb492c0cdd2b7ab70a2b95255da655
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tag-based-policy-conditions-and-built-in-functions
    - Built-in Functions and Tag-based Policy Conditions
    - TPCABF
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Tag-based Policy Conditions and Built-in Functions
description: The has_tag() and has_tag_value() functions used in ABAC policy WHEN and MATCH COLUMNS clauses to match tables and columns based on governed tag attributes.
tags:
  - sql
  - access-control
  - functions
timestamp: "2026-06-18T11:11:43.281Z"
---

# Tag-based Policy Conditions and Built-in Functions

**Tag-based policy conditions** are tag-driven Boolean expressions that determine which securable objects an [ABAC](/concepts/abac-attribute-based-access-control.md) policy — a [Row Filter Policy](/concepts/abac-row-filter-policy.md), [Column Mask Policy](/concepts/column-mask-policies.md), or [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — applies to within its scope. They are written using two built-in functions evaluated by Unity Catalog against securable metadata. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Built-in Functions

### `has_tag(tag_key)`
Returns `TRUE` if the securable object has a governed tag with the given key, either directly or through inheritance from a parent catalog or schema. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### `has_tag_value(tag_key, tag_value)`
Returns `TRUE` if the securable object has a governed tag with the given key **and** the tag’s value matches the specified value. Like `has_tag()`, it checks inherited tags. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Both functions use snake\_case naming. The older camelCase forms (`hasTag`, `hasTagValue`) continue to work but are not recommended for new policies. Databricks plans to deprecate the camelCase forms when creating new policies; existing policies are unaffected. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Table Conditions (`WHEN` Clause)

The `WHEN` clause in a policy definition contains a Boolean expression that matches tables based on their tags. If omitted, the clause defaults to `TRUE`, meaning the policy applies to **all** tables in the scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Example table condition:
```sql
WHEN has_tag_value('lifecycle', 'production')
```

## Column Conditions (`MATCH COLUMNS` Clause)

The `MATCH COLUMNS` clause specifies one or more comma-separated Boolean expressions that identify which columns within a table the policy targets. Each expression can be a single built-in function or a combination using logical operators like `AND`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

A policy can include up to three column expressions. **All** expressions must match for the policy to apply to a particular table. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

**Important**: Tags do not propagate from tables to columns. Using `has_tag()` in a `MATCH COLUMNS` clause only matches **column-level** tags, not tags on the parent table or its ancestors. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Aliases

Each column expression can be assigned an alias (using `AS`) that can be referenced in the `ON COLUMN` and `USING COLUMNS` clauses. The alias refers to the column that matched the expression. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Example with alias:
```sql
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col
USING COLUMNS (4)
```

## Usage in Policy Types

- In **row filter** and **column mask** policies, the conditions are combined with a [User-defined function (UDF)](/concepts/abac-user-defined-functions-udfs.md) to apply filtering or masking. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- In **GRANT policies** (Beta), the condition is expressed inline in the `WHEN` clause, and no UDF is used. The privilege is granted dynamically when the condition matches. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Evaluation

Conditions are evaluated at access time by Unity Catalog against the metadata of the securable object. For inherited tags, the policy sees the effective tag set (direct tags plus inherited tags). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The key-value pairs that form the basis of tag conditions
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Policy type that uses these conditions to grant privileges
- [Row Filter Policies](/concepts/row-filter-policies.md) — Policy type that uses conditions to filter table rows
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policy type that uses conditions to mask column values
- UDF (User-Defined Function) — Used with row filter and column mask policies
- [ABAC Policy Scoping and Sprawl Prevention](/concepts/abac-policy-scoping-and-sprawl-prevention.md) — Best practices for policy placement

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
