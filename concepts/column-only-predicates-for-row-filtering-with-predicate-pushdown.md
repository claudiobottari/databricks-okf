---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 171fbeddbb84325caa5bace9a55a0942baa85d911793427e2200122e6ca426bb
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-only-predicates-for-row-filtering-with-predicate-pushdown
    - CPFRFWPP
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Column-only predicates for row filtering with predicate pushdown
description: Using simple boolean expressions that reference only table columns in row filter UDFs to enable predicate pushdown, allowing the engine to skip irrelevant data during scans.
tags:
  - abac
  - row-filter
  - predicate-pushdown
  - performance
timestamp: "2026-06-19T14:19:32.341Z"
---

# Column-only predicates for row filtering with predicate pushdown

**Column-only predicates** are a pattern for implementing row filter policies in Unity Catalog that reference only table columns using simple boolean logic, without external function calls or complex subqueries. This design enables **predicate pushdown**, allowing the query engine to skip irrelevant data during scan operations for improved performance.

## Overview

When a row filter uses column-only predicates, the engine can push the filter condition down to the data source level, filtering rows before they are read into memory. This is particularly important for large tables where reading all rows and then applying a filter would be inefficient.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Example Implementation

### Filter Function

Create a deterministic function that accepts table columns and filter parameters:

```sql
CREATE FUNCTION filter_by_region(region STRING, allowed STRING)
RETURNS BOOLEAN
DETERMINISTIC
  RETURN array_contains(split(allowed, ','), lower(region));
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Policy Definition

Apply the function with constant filter values passed through the `USING COLUMNS` clause:

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

In this example, the `USING COLUMNS` clause passes the matched column value (`rgn`) along with a constant string `'emea,apac'` specifying allowed regions. Because the predicate references only table columns and constants, the engine can push the filter down to the scan level.

## Multi-Column Predicates

When a table contains multiple related attributes — such as `ship_to_country` and `bill_to_country` — you can match them with separate tag conditions and pass both to a single UDF. This avoids creating separate policies for each column. A policy can include up to three column expressions in the `MATCH COLUMNS` clause.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

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

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

An analyst sees only orders where either the shipping or billing country is in their allowed list. The engine can push both column comparisons down to the data source.

## Performance Benefits

Column-only predicates enable predicate pushdown, which allows the engine to skip irrelevant data during scans. This is a key performance optimization for row-filtered tables. For best results, the function should be marked `DETERMINISTIC` so the optimizer can reliably plan the pushdown.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) — The broader framework for filtering rows in Unity Catalog
- Predicate pushdown — The optimization technique that column-only predicates enable
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model that row filters are part of
- Using COLUMNS clause — The mechanism for passing columns and constants to filter UDFs
- Performance optimization for ABAC — Best practices for efficient row filter execution
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages row filter policies

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
