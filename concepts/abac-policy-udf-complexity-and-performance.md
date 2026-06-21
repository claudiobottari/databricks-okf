---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92678920c51f0094323d38b7f5359535aded744fc3db40400fd0b3e498825a5d
  pageDirectory: concepts
  sources:
    - performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-udf-complexity-and-performance
    - performance and ABAC policy UDF complexity
    - APUCAP
  citations:
    - file: performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC policy UDF complexity and performance
description: How the complexity of UDFs in row filter and column mask policies directly affects query execution time, with guidance on keeping UDFs simple, avoiding external calls, and favoring built-in SQL functions.
tags:
  - performance
  - abac-policies
  - udf-optimization
timestamp: "2026-06-19T19:54:26.366Z"
---

# ABAC Policy UDF Complexity and Performance

**ABAC policy UDF complexity and performance** refers to the query‑time cost introduced by [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md) on Databricks. Because these policies execute user‑defined functions (UDFs) for every row (row filters) or every matching column value (column masks), the design of the UDF directly affects query performance. There is no single right approach for every workload; the best approach depends on data volume, query patterns, user interactions with protected tables, and the desired masking or filtering behavior. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Reduce UDF Complexity

The UDF in an ABAC policy executes for every row or column value, so keeping it simple is critical. Favor basic `CASE` statements and simple boolean expressions. Reference only target table columns in the UDF as much as possible to enable [predicate pushdown](/concepts/selective-caching-with-predicate-pushdown.md). If the UDF must reference external tables, keep the external reference small enough to broadcast, and ensure referenced tables are optimized and partitioned to match the access pattern (for example, partition a policy lookup table by username). Avoid external API calls or lookups to other databases, complex subqueries or joins against large tables (which force nested loop joins), heavy regex on large text fields, and per‑row metadata lookups. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Approach for Targeting Principals

Two mechanisms exist for principal‑based logic: the policy’s `TO`/`EXCEPT` clauses, and identity functions like `current_user()` and `is_account_group_member()` inside the UDF. In general, use `TO`/`EXCEPT` to define which principals a policy applies to. This keeps the UDF focused on data transformation, and the `EXCEPT` clause eliminates the policy entirely for exempt users, avoiding any UDF execution. When the conditional logic is too complex for the policy’s principal clauses, identity functions inside the UDF are an alternative. These functions are resolved once during query analysis, not per row, and multiple calls with different group arguments result in a single UC API call, so performance impact is typically minimal. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Use Deterministic, Error‑Safe Expressions

Non‑deterministic functions (e.g., `rand()`, `now()`) prevent the optimizer from caching results or applying constant folding. For SQL UDFs, the optimizer derives determinism automatically, but for Python UDFs the optimizer cannot inspect the body, so explicitly marking a Python UDF as `DETERMINISTIC` is important to enable result caching. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

Expressions that can throw errors (e.g., ANSI division by zero) also block the optimizer from pushing operations down in the query plan. Use error‑safe alternatives like `try_divide`, `try_cast`, and `try_to_number`, which return `NULL` on failure instead of throwing, allowing the optimizer to rearrange and fold expressions freely. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Avoid Python UDFs

Avoid Python UDFs in ABAC policies whenever possible. Python UDFs must be wrapped in a SQL UDF to be used in policies and are generally slower than SQL UDFs because the optimizer cannot inline or optimize them, and the Python function executes for every row. If a Python UDF is unavoidable, mark it as `DETERMINISTIC` to enable result caching. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Keep Lookup Tables Small

A common pattern is to check access rights against a small lookup table. If the lookup table is significantly smaller than the target table, the optimizer converts the subquery into a broadcast hash join, copying the lookup table to each executor and storing it in memory as a hashmap. If the lookup table is large, the optimizer falls back to a slower shuffle join. Even with broadcast hash join, each row still incurs the cost of a hash table lookup during execution. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Understand Predicate Pushdown on Protected Tables

The `SecureView` barrier used by row filters and column masks prevents predicates with side effects from being pushed across the policy boundary, protecting against side‑channel data leakage. This can block partition pruning and liquid clustering optimizations, potentially forcing full table scans — even when the UDF resolves to constant `true`. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

Simple equality comparisons (e.g., `WHERE col = 'value'`) and basic range comparisons are free of side effects and can still be pushed down. Predicates that call functions (e.g., `WHERE date_format(col, ...) = '1995-07-29'`) or introduce implicit type casts are kept above the barrier, causing the engine to scan the table before applying the filter. For exempt users, use the `EXCEPT` clause in the policy to eliminate the barrier entirely. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Reuse Column Masks Where Possible

Applying many distinct column masks to a single table compounds the per‑column cost. Mask only columns that contain truly sensitive data. When multiple columns require the same transformation (e.g., redacting to `NULL`), reuse the same masking function rather than creating a separate function per column. Databricks recognizes policies that reference the same UDF with the same arguments as the same effective mask, so reusing functions avoids unnecessary overhead. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Avoid Regex Masking on Large Text Fields

Using `regexp_replace` inside a column mask to redact elements within a serialized document (XML or JSON stored as a `STRING` column) is expensive. `regexp_replace` walks the full string for every row, and the engine reads and rewrites the entire payload even when only a few fields are needed. Instead, materialize sensitive fields into typed columns in a separate table and apply column masks to those scalar columns. If the data can be stored as a struct column, use the VARIANT flexible masking pattern to redact individual fields. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Test UDF Performance

Test UDF performance on at least 1 million rows before deploying to production. Run queries that represent the actual workload expected on the protected table. Make incremental changes to policy functions and measure the effect of each change. Use a test query that applies the mask function over a range of synthetic data and compares the duration with and without the policy applied to isolate the overhead. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Row filter policy](/concepts/row-filter-policies.md)
- [Column mask policy](/concepts/column-mask-policies.md)
- ABAC policy
- SecureView barrier
- Predicate pushdown
- Broadcast hash join
- Deterministic UDF
- Error‑safe expressions

## Sources

- performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws-b415eba9.md)
