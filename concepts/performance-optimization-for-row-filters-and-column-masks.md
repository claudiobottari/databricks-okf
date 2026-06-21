---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16c1ad4cd66274195ebd1f24bb141bb98a5367108213190de76c3f7fb51de584
  pageDirectory: concepts
  sources:
    - row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - performance-optimization-for-row-filters-and-column-masks
    - column masks and Performance optimization for row filters
    - POFRFACM
    - Performance considerations for row filter and column mask policies
  citations:
    - file: row-filters-and-column-masks-databricks-on-aws.md
title: Performance optimization for row filters and column masks
description: Best practices to minimize query performance impact when using row filters and column masks, including UDF simplicity, deterministic expressions, and avoiding Python UDFs.
tags:
  - performance
  - unity-catalog
  - optimization
timestamp: "2026-06-19T20:16:56.638Z"
---

# Performance optimization for row filters and column masks

**Row filters** and **column masks** are [Unity Catalog](/concepts/unity-catalog.md) access controls that restrict which rows and column values users can see at query time. When the query engine must choose between optimization and protecting against information leakage from filtered or masked values, it always makes the secure choice, which can affect query performance.^[row-filters-and-column-masks-databricks-on-aws.md]

## General principles

Row filters and column masks control data visibility by ensuring that users cannot view base table values before filtering or masking is applied. This security-first approach means the query engine may avoid certain optimizations that could reveal intermediate results through error messages or timing differences.^[row-filters-and-column-masks-databricks-on-aws.md]

## Performance recommendations

Use the following strategies to minimize the performance impact of row filters and column masks:

### Use simple UDFs
Functions with fewer expressions perform better. Prefer simple `CASE` expressions over mapping tables or expression subqueries.^[row-filters-and-column-masks-databricks-on-aws.md]

### Limit the number of distinct column masks on large tables
Each distinct mask is evaluated during queries. Apply masks only to truly sensitive columns and reuse masking functions where possible.^[row-filters-and-column-masks-databricks-on-aws.md]

### Reduce the number of UDF arguments
Databricks cannot optimize away column references that come from UDF arguments, even if those columns are not used in the query. Use UDFs with fewer arguments where possible.^[row-filters-and-column-masks-databricks-on-aws.md]

### Avoid row filters with too many `AND` conjuncts
Only one distinct row filter can resolve at runtime for a given user and table, so a common pattern is to combine logic with `AND`. The more conjuncts you add, the more likely the combined filter includes one of the patterns that prevents optimization. Use fewer conjuncts where possible.^[row-filters-and-column-masks-databricks-on-aws.md]

### Use deterministic expressions that cannot throw errors
Expressions that can throw errors (such as ANSI division) prevent the SQL compiler from pushing operations down in the query plan, because errors like "division by zero" could reveal information about values before filtering or masking. Use deterministic expressions that never throw errors, such as `try_divide`.^[row-filters-and-column-masks-databricks-on-aws.md]

### Prefer SQL to Python UDFs
Python UDFs are less performant than SQL and offer fewer optimization opportunities. If you must use Python, mark the UDF as `DETERMINISTIC` when applicable.^[row-filters-and-column-masks-databricks-on-aws.md]

## Related concepts

For full UDF performance guidance (including [predicate pushdown](/concepts/selective-caching-with-predicate-pushdown.md) and engine-level optimization details), see [Performance considerations for row filter and column mask policies](/concepts/performance-optimization-for-row-filters-and-column-masks.md). Most of that guidance applies equally to manually-applied row filters and column masks. For example UDFs, see Common patterns for row filtering and column masking.^[row-filters-and-column-masks-databricks-on-aws.md]

## Related concepts

- [Row filters](/concepts/row-filter-policies.md)
- [Column masks](/concepts/column-mask-policies.md)
- User-defined functions
- ABAC policies
- [Unity Catalog](/concepts/unity-catalog.md)
- Predicate pushdown

## Sources

- row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [row-filters-and-column-masks-databricks-on-aws.md](/references/row-filters-and-column-masks-databricks-on-aws-f091f827.md)
