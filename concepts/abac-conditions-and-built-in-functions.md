---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dce444a29ab2ac2fbfba6b5dfb575688616923fb5503a925940af8d50b4a0b28
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-conditions-and-built-in-functions
    - Built-in Functions and ABAC Conditions
    - ACABF
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC Conditions and Built-in Functions
description: Policy conditions use has_tag() and has_tag_value() built-in functions in WHEN (table) and MATCH COLUMNS (column) clauses to match objects based on governed tags, with support for logical operators and aliases.
tags:
  - abac
  - policies
  - functions
timestamp: "2026-06-19T17:54:18.081Z"
---

Here is the wiki page for "ABAC Conditions and Built-in Functions".

# ABAC Conditions and Built-in Functions

**ABAC conditions and built-in functions** are the tag-based expressions used within [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies to determine which data objects and columns they target. They form the core logic of [Row Filter Policies](/concepts/row-filter-policies.md), [Column Mask Policies](/concepts/column-mask-policies.md), and [GRANT Policies (Beta)](/concepts/grant-policies-beta.md).

## Overview

In [Unity Catalog](/concepts/unity-catalog.md), ABAC policies use conditions to dynamically apply to securable objects based on their attributes. These conditions are written using built-in functions that evaluate the [Governed Tags](/concepts/governed-tags.md) (key-value pairs) applied to catalogs, schemas, tables, columns, models, and volumes. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

This allows a single policy to automatically apply to many data objects that share the same tags, without needing per-object grants. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Types of Conditions

Policies have two main clauses for conditions:

1.  **Table conditions (`WHEN` clause):** Boolean expressions that determine which tables the policy applies to within its scope (e.g., a catalog or schema). If omitted, the condition defaults to `TRUE`, meaning the policy applies to all tables in that scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
2.  **Column conditions (`MATCH COLUMNS` clause):** One or more comma-separated boolean expressions that identify which columns the policy should act on. A policy can include up to three column expressions, and all must match for the policy to apply. Each expression can be assigned an alias (using `AS`) for use in other clauses like `ON COLUMN`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Built-in Functions

The following built-in functions are evaluated by Unity Catalog against object metadata and are used in policy conditions. Note that they use `snake_case` naming.

- **`has_tag(tag_key)`:** Returns `TRUE` if the a given tag key (e.g., `'pii'`) is present on the securable object, either directly or through inheritance from a parent object. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **`has_tag_value(tag_key, tag_value)`:** Returns `TRUE` if a given tag key has a specific value (e.g., `has_tag_value('pii', 'ssn')`). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Important notes on tag propagation

Tags do not propagate from tables to their columns. Using `has_tag()` in a `MATCH COLUMNS` clause only matches **column-level** tags, not tags on the parent table or other ancestors. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

The older `camelCase` forms (`hasTag`, `hasTagValue`) continue to work but are not recommended. Databricks plans to deprecate them when creating new policies. Existing policies are not affected. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Condition Evaluation

When a user attempts to access a securable object, Unity Catalog evaluates the policy's conditions. For example, a column mask policy might use two conditions: one to identify the column to mask (e.g., `has_tag_value('pii', 'email')`) and another to identify a column containing consent data (e.g., `has_tag('consent_to_contact')`). The policy only applies if both conditions match on the same table. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Example

The following policy masks email addresses only if a table has a column tagged with both `pii : email` and `consent_to_contact`. If a table lacks a column matching one of the conditions, the policy does not apply and data is returned unmasked. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

```sql
CREATE FUNCTION mask_email_by_consent(email STRING, consent BOOLEAN)
RETURNS STRING
RETURN CASE
  WHEN consent = true THEN email
  ELSE '****@****.***'
END;

CREATE POLICY mask_email_with_consent
ON SCHEMA customers
COLUMN MASK mask_email_by_consent
TO `account users`
FOR TABLES
MATCH COLUMNS
  has_tag_value('pii', 'email') AS m,
  has_tag('consent_to_contact') AS c
ON COLUMN m
USING COLUMNS (c);
```

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [GRANT Policies (Beta)](/concepts/grant-policies-beta.md)
- Policy Evaluation Model
- User-defined functions (UDFs) in Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
