---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 472710060999c0bc1eab0aeb8dca4f0a448290e08bdec8460c8aa28e110c31f6
  pageDirectory: concepts
  sources:
    - use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tags-for-abac-policy-discovery
    - GTFAPD
  citations:
    - file: use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
title: Governed Tags for ABAC Policy Discovery
description: Using governed tags on columns to automatically identify which columns should participate in row filter and column mask policies via MATCH COLUMNS, enabling attribute-based access control.
tags:
  - data-governance
  - ABAC
  - tagging
timestamp: "2026-06-19T23:22:11.683Z"
---

## [Governed Tags](/concepts/governed-tags.md) for ABAC Policy Discovery

**Governed Tags** are user-defined metadata labels that can be applied to columns in [Unity Catalog](/concepts/unity-catalog.md) tables. In the context of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) for Databricks, [Governed Tags](/concepts/governed-tags.md) are the primary mechanism for *policy discovery*: they allow row filter and [Column Mask Policies](/concepts/column-mask-policies.md) to automatically identify the columns they should apply to, without hardcoding column names in the policy definition. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Overview

A governed tag consists of a key and an optional value (e.g., `pii = 'email'`). Tags are stored in a global [Unity Catalog](/concepts/unity-catalog.md) registry and can be assigned to columns using `ALTER COLUMN SET TAGS`. Once a column is tagged, any policy that uses the `MATCH COLUMNS ... has_tag(...)` syntax will automatically apply its logic to that column at query time. This decouples the policy definition from the physical schema, enabling centralized, schema-agnostic access control rules. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Creating [Governed Tags](/concepts/governed-tags.md)

Before a tag can be applied to columns, it must first exist as a governed tag in the catalog. Admin users create [Governed Tags](/concepts/governed-tags.md) through the [Catalog Explorer](/concepts/catalog-explorer.md) UI:

1. Navigate to **Catalog** → **Govern** → **Governed Tags**.
2. Click **Create governed tag**.
3. Enter a tag name (key) and optionally a default value.

For example, in a typical ABAC tutorial, the following tags are created: `region`, `department`, `pii`, and `priority`. The `pii` tag distinguishes between `name` and `email` subtypes via its value. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

After creation, tags are applied to columns using SQL:

```sql
ALTER TABLE catalog.schema.orders
  ALTER COLUMN customer_name SET TAGS ('pii' = 'name');
ALTER TABLE catalog.schema.orders
  ALTER COLUMN order_priority SET TAGS ('priority' = '');
```

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Role in ABAC Policy Discovery

[Governed Tags](/concepts/governed-tags.md) are the foundation of **policy discovery** in ABAC. Row filter and [Column Mask Policies](/concepts/column-mask-policies.md) can use `has_tag()` and `has_tag_value()` inside their `MATCH COLUMNS` clauses. This tells the policy engine: *“Find all columns in the target table that carry the specified tag and apply the rule to them automatically.”* ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

For example, a row filter policy might use:

```sql
CREATE POLICY user_access_filter
  ON SCHEMA abac_tutorial.mapping_demo
  ROW FILTER abac_tutorial.mapping_demo.access_filter
  TO `account users`
  FOR TABLES
  MATCH COLUMNS has_tag('region') AS r, has_tag('department') AS d
  USING COLUMNS (r, d);
```

Here the `region` and `department` tags tell the policy which columns to extract from each table and pass to the filter UDF. Similarly, a column mask policy can use `has_tag_value('pii', 'name')` to target only columns tagged as personally identifiable information of type `name`. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

The `priority` tag (key-only, no value) is used to pass the `order_priority` column value to the mask UDF for conditional masking, enabling logic that varies masking based on the content of another column in the same row. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Security Considerations

Tag data is stored as **plain text** and may be replicated globally. Databricks explicitly warns:

> “Do not use tag names, values, or descriptors that could compromise the security of your resources. For example, do not use tag names, values or descriptors that contain personal or sensitive information.”

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Related Concepts

- [Mapping Tables for Dynamic Access Control](/concepts/mapping-tables-for-access-control.md) – The tutorial that heavily uses [Governed Tags](/concepts/governed-tags.md).
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The access control model [Governed Tags](/concepts/governed-tags.md) support.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) – The policies that consume [Governed Tags](/concepts/governed-tags.md) via `MATCH COLUMNS`.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where [Governed Tags](/concepts/governed-tags.md) are stored and managed.
- Manual Application of ABAC Policies – Alternative approach without [Governed Tags](/concepts/governed-tags.md).

### Sources

- use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md

# Citations

1. [use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md](/references/use-mapping-tables-for-dynamic-access-control-databricks-on-aws-cfb1e1c1.md)
