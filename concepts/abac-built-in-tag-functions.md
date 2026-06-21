---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60429849284d7b00a5721e0f946909a28124167f4f4a2faf4cb89f49fd1f408f
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-built-in-tag-functions
    - ABTF
    - ABAC Built-in Functions
    - Built-in Functions
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC Built-in Tag Functions
description: The has_tag() and has_tag_value() functions used in policy conditions to match tables and columns based on governed tags, supporting logical operators and snake_case naming.
tags:
  - sql
  - policies
  - tagging
  - unity-catalog
timestamp: "2026-06-19T14:28:03.303Z"
---

# ABAC Built-in Tag Functions

**ABAC Built-in Tag Functions** are special functions used in [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy conditions within [Unity Catalog](/concepts/unity-catalog.md) to evaluate governed tags on securable objects. These functions enable dynamic access control decisions by checking whether tags exist on tables, columns, or other objects without requiring explicit knowledge of which objects are tagged.

## Overview

ABAC policies use conditions expressed with built-in tag functions to determine which tables and columns the policy targets within its scope. These functions are evaluated by Unity Catalog against securable metadata, not against the data stored in tables or columns. There are two primary built-in tag functions: `has_tag()` and `has_tag_value()`.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Function Reference

### has_tag

`has_tag(tag_key)` is a boolean function that returns `TRUE` if the target object has a governed tag with the specified key, either directly or through tag inheritance from parent objects. This function checks for the presence of any tag with the given key, regardless of its value.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

**Usage example in a policy condition:**
```sql
WHEN has_tag('HR')
```

This condition matches tables that have an `HR` tag, either directly applied or inherited from a parent catalog or schema.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### has_tag_value

`has_tag_value(tag_key, tag_value)` is a boolean function that returns `TRUE` if the target object has a governed tag with both the specified key and the specified value. This is more specific than `has_tag()` because it matches both the key and the value of the tag.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

**Usage example in a policy condition:**
```sql
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
```

This condition matches columns tagged with `pii : ssn` (key `pii`, value `ssn`).^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Scope and Inheritance

### Tag Inheritance

By default, securables inherit tags from their parent catalog or schema. The `has_tag()` and `has_tag_value()` functions evaluate inherited tags when checking objects, meaning that a table inheriting an `HR` tag from its parent schema will match `has_tag('HR')`.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Column Tag Limitation

Tags do not propagate from tables to columns. When using `has_tag()` or `has_tag_value()` in a `MATCH COLUMNS` clause, these functions only match column-level tags, not tags on the parent table or its ancestors. Column tags must be applied directly to columns and are not inherited.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Usage in Policy Conditions

### Table Conditions (WHEN clause)

Table conditions use tag functions to match tables based on their tags. If the `WHEN` clause is omitted, it defaults to `TRUE`, meaning the policy applies to all tables in scope.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

**Example:**
```sql
WHEN has_tag('sensitive')
```

This condition matches all tables with a `sensitive` tag within the policy's scope.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Column Conditions (MATCH COLUMNS clause)

Column conditions use one or more comma-separated boolean expressions to identify which columns the policy targets. Each expression can be a single tag function or a combination using logical operators like `AND`. A policy can include up to 3 column expressions, and all must match for the policy to apply.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

**Example with two column conditions:**
```sql
MATCH COLUMNS has_tag_value('pii', 'email') AS m,
             has_tag('consent_to_contact') AS c
```

This matches only tables that have both a column tagged `pii : email` and a column tagged `consent_to_contact`. Both conditions must be satisfied for the policy to apply.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Combined Conditions

Tag functions can be combined using logical operators for more complex matching:

```sql
MATCH COLUMNS has_tag_value('pii', 'ssn') AND has_tag('sensitive')
```

This matches columns tagged with both `pii : ssn` and `sensitive`.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Aliases

Each column condition expression can be assigned an alias (specified after `AS`) that can be referenced in the `ON COLUMN` and `USING COLUMNS` clauses of the policy. This allows the policy to refer to matched columns by their aliases rather than repeating the full tag function expression.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Naming Convention

The recommended naming convention uses snake_case (e.g., `has_tag`, `has_tag_value`). Databricks plans to deprecate the older camelCase forms (`hasTag`, `hasTagValue`) when creating new policies, though existing policies using camelCase are not affected.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The key-value attributes that these functions evaluate
- [ABAC Policy Types](/concepts/abac-policy-types.md) — Row filter, column mask, and GRANT policies that use these functions
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model that uses these functions
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — The objects that can be tagged and evaluated
- Policy Evaluation Model — How Unity Catalog evaluates these functions at query time

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
