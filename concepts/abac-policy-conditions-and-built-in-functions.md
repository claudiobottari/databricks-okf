---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e5029c765144da5475c03961375be3b91cb625bb650ff0296d9818e4d14cbb80
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-conditions-and-built-in-functions
    - Built-in Functions and ABAC Policy Conditions
    - APCABF
    - Identity functions in ABAC policies
    - Policy Conditions and Built-in Functions (has_tag, has_tag_value)
    - tag-based-policy-conditions-and-built-in-functions
    - Built-in Functions and Tag-based Policy Conditions
    - TPCABF
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC Policy Conditions and Built-in Functions
description: Tag-based expressions using has_tag() and has_tag_value() functions to match tables (WHEN clause) and columns (MATCH COLUMNS clause) within a policy's scope, supporting up to 3 column expressions.
tags:
  - access-control
  - policy-evaluation
  - sql-functions
timestamp: "2026-06-19T09:25:43.342Z"
---

---

title: ABAC Policy Conditions and Built-in Functions
summary: Tag-based expression system using `has_tag()` and `has_tag_value()` functions in `WHEN` (table) and `MATCH COLUMNS` (column) clauses to determine which securable objects a policy targets within its scope.
sources:
  - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:45:56.352Z"
updatedAt: "2026-06-18T14:45:56.352Z"
tags:
  - policy-syntax
  - tag-functions
  - unity-catalog
aliases:
  - abac-policy-conditions-and-built-in-functions
  - Built-in Functions and ABAC Policy Conditions
  - APCABF
confidence: 0.97
provenanceState: extracted
inferredParagraphs: 0
---

# ABAC Policy Conditions and Built-in Functions

**ABAC Policy Conditions and Built-in Functions** are the tag-based expressions used within [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies in [Unity Catalog](/concepts/unity-catalog.md) to determine which data objects and columns a policy applies to. These conditions dynamically match securable objects based on their attributes, allowing a single policy to govern many objects without requiring per-object configuration.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## How Conditions Work

ABAC policies use two types of conditions: table-level and column-level. Both are evaluated at runtime by Unity Catalog based on the [Governed Tags](/concepts/governed-tags.md) present on the securable object, including any tags it inherits from its parent catalog or schema.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **`WHEN` clause (Table conditions):** A Boolean expression that determines if a policy applies to a specific table. It evaluates the tags on that table and its ancestors. If omitted, the condition defaults to `TRUE`, meaning the policy applies to all tables within the policy's scope.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **`MATCH COLUMNS` clause (Column conditions):** One or more comma-separated Boolean expressions that identify which columns a policy targets. Each expression can be a single function (like `has_tag('pii')`) or a compound condition using logical operators (like `has_tag_value('pii', 'ssn') AND has_tag('sensitive')`). A policy can include up to three column expressions, and all must match for the policy to apply. Each expression can be assigned an alias (via `AS`) that is then referenced in the `ON COLUMN` or `USING COLUMNS` clauses of the policy.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Built-in Functions

The following built-in functions are provided by Unity Catalog for use in policy conditions. They are evaluated against securable metadata (governed tags) at query time.

**`has_tag(tag_key)`** — Returns `TRUE` if the securable object has the specified governed tag key (regardless of its value).^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

**`has_tag_value(tag_key, tag_value)`** — Returns `TRUE` if the securable object has the specified governed tag key and that specific tag value. This is more specific than `has_tag()` because it requires both the key and the value to match.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Naming Conventions

The functions use snake_case naming (`has_tag`, `has_tag_value`). The older camelCase forms (`hasTag`, `hasTagValue`) continue to work with existing policies, but Databricks plans to deprecate the camelCase forms for new policy creation. Existing policies are not affected by this change.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Tag Inheritance and Scope

Tags are evaluated with their full inheritance chain. When a condition checks for a tag on a table, it considers tags applied directly to the table as well as tags inherited from the parent schema or catalog.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

However, tags do not propagate from a table to its columns. Using `has_tag()` or `has_tag_value()` in a `MATCH COLUMNS` clause only evaluates column-level tags, not tags on the parent table or its ancestors.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Example: Using Multiple Column Conditions

The following example shows a policy that uses two column conditions. It applies to a `customers` schema and masks email addresses (identified by a `pii : email` tag) unless the table also has a column tagged `consent_to_contact` (which the UDF uses to determine whether the email should be shown). The policy only activates when both column conditions are true.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

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

In this example:
- `has_tag_value('pii', 'email')` identifies the column to mask (the email column).
- `has_tag('consent_to_contact')` identifies a separate column that provides the consent flag, which the UDF uses to decide whether to reveal the email.

This policy only applies to tables that have both a column tagged `pii : email` and a column tagged `consent_to_contact`. If a table lacks either condition, the policy does not apply and data is returned unmasked.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The attribute system that powers policy conditions
- [ABAC Policy Types](/concepts/abac-policy-types.md) — Row filter, column mask, and GRANT policies
- ABAC Best Practices — Guidance on using tags and conditions effectively
- [Unity Catalog](/concepts/unity-catalog.md) — The governance system where ABAC policies are enforced

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
