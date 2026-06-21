---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5057be840ab846565e24b1cd33bacb19b2a337d518d7a53ad4130b6e37d389ae
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tag-inheritance
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Tag Inheritance
description: Unity Catalog securables inherit governed tags from parent catalogs and schemas by default, but column tags do not inherit from parent tables and must be applied directly.
tags:
  - abac
  - tagging
  - hierarchy
timestamp: "2026-06-19T17:53:50.217Z"
---

# Tag Inheritance

**Tag Inheritance** is a mechanism in [Unity Catalog](/concepts/unity-catalog.md) by which governed tags applied to a parent securable object (catalog or schema) automatically propagate to its descendant objects (tables, columns, models, volumes, etc.), unless explicitly overridden. This propagation allows administrators to define broad attribute-based policies once at a high scope and have them apply consistently across the data estate.

## Definition

Tag inheritance means that by default, securables inherit tags from their parent catalog or schema. Inherited tags can be overridden at every level except the column level. Column tags do **not** inherit from the parent table; they must be applied directly to the column using `APPLY TAG` or through [Automatic Data Classification](/concepts/automated-data-classification-with-ai.md). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Hierarchy

![Governed tags hierarchy diagram](https://docs.databricks.com/aws/en/assets/images/governed-tags-hierarchy-2740348868f29ddf0611089d4684adec.png)

The governed tag hierarchy in Unity Catalog flows from top to bottom:

- **Account-level** tag definitions
- **Catalog**
- **Schema**
- **Table** (and materialized views, streaming tables)
- **Column**

Tags applied at a higher level are inherited by all objects in that scope. For example, a tag applied to a catalog is inherited by all schemas, tables, and columns within that catalog, unless overridden at a lower level. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Inheritance Rules

- Tags propagate from a catalog to all schemas, tables, and columns in that catalog.
- Tags propagate from a schema to all tables and columns in that schema.
- Inherited tags can be **overridden** at any level except the column level. Override means applying a different value for the same tag key, which replaces the inherited value for that object and its descendants (where allowed). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- Tables, including streaming tables and materialized views, inherit tags from their parent schema and catalog.
- Tag inheritance is considered when evaluating policy conditions. The built-in functions `has_tag()` and `has_tag_value()` check if a given tag is present on the target data object **either directly or through tag inheritance**. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Column-Level Exception

A critical exception to the inheritance chain is that **column tags do not inherit from the parent table or any ancestor**. The source document explicitly states:

> Tags don't propagate from tables to columns. Using `has_tag()` in a `MATCH COLUMNS` clause only matches column-level tags, not tags on the parent table or its ancestors. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

This means that to apply a tag to a column, the column must be tagged directly. Inherited tags from the table, schema, or catalog are not visible at the column level for policy matching. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Usage in ABAC Policies

Tag inheritance is fundamental to how [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) policies in Unity Catalog evaluate scope and conditions. When a policy is attached at a catalog or schema level, it evaluates against all objects in that scope that match the tag conditions. Because tags are inherited, a policy can automatically apply to new objects created within the scope without additional configuration. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

For example, a [Row Filter Policy](/concepts/abac-row-filter-policy.md) or [Column Mask Policy](/concepts/column-mask-policies.md) can use the `WHEN` clause with `has_tag('HR')` to target any table in a catalog that has the `HR` tag — whether that tag was applied directly to the table or inherited from its parent schema or catalog. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) – The key-value pairs that define attributes for access control.
- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) – The access control model that uses tag inheritance for dynamic policy evaluation.
- [Row Filter Policies](/concepts/row-filter-policies.md) – Policies that restrict rows based on column values identified by tags.
- [Column Mask Policies](/concepts/column-mask-policies.md) – Policies that mask column values based on tag conditions.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance platform that manages securable objects and tags.
- [Automatic Data Classification](/concepts/automated-data-classification-with-ai.md) – A feature that can automatically apply tags to columns, bypassing the need for manual tagging.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – A monitoring table that may reference tagged columns for drift analysis.

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
