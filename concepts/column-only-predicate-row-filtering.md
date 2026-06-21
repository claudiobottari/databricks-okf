---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b751f7517096de68567cc792a91472950907478cce4be2e50fdd1bbb4c7f98f
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-only-predicate-row-filtering
    - CPRF
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Column-only predicate row filtering
description: Pattern for row filter policies that use simple boolean logic referencing only table columns, enabling predicate pushdown for better query performance on protected tables.
tags:
  - abac
  - row-filtering
  - predicate-pushdown
  - performance
  - unity-catalog
timestamp: "2026-06-18T14:39:49.042Z"
---

# Column-only Predicate Row Filtering

**Column-only predicate row filtering** is a pattern for implementing [Row Filter Policies](/concepts/row-filter-policies.md) in [Unity Catalog](/concepts/unity-catalog.md) that uses simple boolean logic referencing only table columns. This approach enables [predicate pushdown](/concepts/selective-caching-with-predicate-pushdown.md), allowing the query engine to skip irrelevant data during table scans for improved performance. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Overview

Row filter policies restrict which rows users can see in a table. When the filter function references only table columns (rather than external state or complex computations), the engine can push the filter predicate down into the scan phase, reducing the amount of data read from storage. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Implementation

### Basic Pattern

Create a deterministic function that accepts column values and an allowed list as parameters, then returns a boolean indicating whether the row should be visible:

```sql
CREATE FUNCTION filter_by_region(region STRING, allowed STRING)
RETURNS BOOLEAN
DETERMINISTIC
  RETURN array_contains(split(allowed, ','), lower(region));
```

Apply the function in a policy that passes allowed values as a constant:

```sql
CREATE POLICY regional_access
ON CATALOG analytics
ROW FILTER filter_by_region
TO 'emea_team'
FOR TABLES
MATCH COLUMNS has_tag('region') AS rgn
USING COLUMNS (rgn, 'emea,apac');
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Multi-Column Filtering

When a table has multiple columns representing related attributes (for example, `ship_to_country` and `bill_to_country`), you can match them with separate tag conditions and pass both to a single UDF. This avoids creating separate policies for each column. A policy can include up to three column expressions in the `MATCH COLUMNS` clause. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

```sql
CREATE FUNCTION filter_by_countries(
  ship_country STRING,
  bill_country STRING,
  allowed STRING
)
RETURNS BOOLEAN
DETERMINISTIC
  RETURN array_contains(split(allowed, ','), lower(ship_country))
      OR array_contains(split(allowed, ','), lower(bill_country));

CREATE POLICY regional_orders
ON SCHEMA prod.orders
ROW FILTER filter_by_countries
TO analysts
FOR TABLES
WHEN has_tag_value('sensitivity', 'high')
MATCH COLUMNS
  has_tag('ship_country') AS ship,
  has_tag('bill_country') AS bill
USING COLUMNS (ship, bill, 'us,ca,mx');
```

An analyst sees only orders where either the shipping or billing country is in their allowed list. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Performance Benefits

Column-only predicates enable [predicate pushdown](/concepts/selective-caching-with-predicate-pushdown.md), which allows the engine to skip irrelevant data during scans. This is more efficient than filter conditions that require external lookups or complex computations, as the filtering happens at the storage layer rather than after data retrieval. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Best Practices

- **Use `DETERMINISTIC` functions** to help the engine optimize query execution. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]
- **Reference only table columns** in the filter logic to maximize predicate pushdown opportunities.
- **Pass allowed values as constants** in the `USING COLUMNS` clause rather than hardcoding them in the function.
- **Use [Governed Tags](/concepts/governed-tags.md)** with `MATCH COLUMNS` to dynamically identify which columns to filter, rather than hardcoding column names in policies.

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) — The broader mechanism for restricting row-level access
- [Predicate Pushdown](/concepts/selective-caching-with-predicate-pushdown.md) — The query optimization technique enabled by column-only predicates
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — Attribute-based access control for granting privileges
- [Column Mask Policies](/concepts/column-mask-policies.md) — Complementary mechanism for masking column values
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The permission model governing access to securable objects

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
