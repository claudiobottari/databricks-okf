---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f5c6a42af1e67937c824e7ef9e8a34c1fa404e027691a206bb39060fb57f405
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-filtering-with-column-only-predicates
    - RFWCP
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Row filtering with column-only predicates
description: Filtering rows using simple boolean logic that references only table columns, enabling predicate pushdown for query optimization, including patterns for matching multiple country/region columns with a single policy.
tags:
  - data-governance
  - abac
  - row-filtering
  - performance
  - predicate-pushdown
timestamp: "2026-06-19T17:47:11.812Z"
---

```markdown
---
title: Row filtering with column-only predicates
summary: Writing row filter UDFs that reference only table columns (no subqueries or non-deterministic functions) to enable predicate pushdown, allowing the engine to skip irrelevant data during scans.
sources:
  - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:02:38.739Z"
updatedAt: "2026-06-19T09:18:18.664Z"
tags:
  - abac
  - row-filter
  - predicate-pushdown
  - performance
aliases:
  - row-filtering-with-column-only-predicates
  - RFWCP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Row Filtering with Column-Only Predicates

**Row filtering with column-only predicates** is a pattern for implementing [[row filter policies]] in [[Unity Catalog]] that uses simple boolean logic referencing only table columns. This approach leverages [[Selective Caching with Predicate Pushdown|predicate pushdown]], allowing the query engine to skip irrelevant data during scans and improve performance on protected tables.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## How It Works

The filtering function accepts column values as parameters and returns a boolean result based on those values alone. Because the predicate references only table columns (rather than external functions, system calls, or subqueries), the optimizer can push the filter condition down to the data scan layer, reducing the amount of data that needs to be read. This contrasts with approaches that use lookup tables or complex conditional logic, which may prevent such optimization.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Basic Example

The following function filters rows by comparing a region column against an allowed list:

```sql
CREATE FUNCTION filter_by_region(region STRING, allowed STRING)
RETURNS BOOLEAN
DETERMINISTIC
  RETURN array_contains(split(allowed, ','), lower(region));
```

Use with a policy that passes the allowed regions as a constant:

```sql
CREATE POLICY regional_access
ON CATALOG analytics
ROW FILTER filter_by_region
TO `emea_team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS rgn
USING COLUMNS (rgn, 'emea,apac');
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Handling Multiple Related Columns

When a table has multiple columns representing related attributes (for example, `ship_to_country` and `bill_to_country`), you can match them with separate tag conditions and pass both to a single UDF. This avoids creating separate policies for each column. A policy can include up to three column expressions in the `MATCH COLUMNS` clause.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

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

An analyst sees only orders where either the shipping or billing country is in their allowed list.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Benefits

- **Predicate pushdown**: The engine can push filter conditions down to the storage layer, skipping irrelevant data during scans.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]
- **Performance**: Simple boolean functions with column‑only references are more efficient than approaches requiring external lookups or complex computation.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]
- **Simplicity**: The pattern is straightforward to implement and maintain, reducing the number of separate policies needed.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Best Practices

- Mark functions as `DETERMINISTIC` to tell the engine the function always returns the same result for the same input, which helps optimize queries.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related Concepts

- [[Row filter policies]] — ABAC policies that restrict which rows users can see.
- Predicate pushdown — Optimization technique for skipping irrelevant data.
- [[Unity Catalog]] — The data governance platform for ABAC policies.
- [[Attribute-Based Access Control (ABAC)]] — The access control model for Unity Catalog.
- [[ABAC row filter policies]] — Implementation using column‑only predicates.
- Deterministic functions — Functions that return the same output for the same input, enabling query optimizations.

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
```

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
