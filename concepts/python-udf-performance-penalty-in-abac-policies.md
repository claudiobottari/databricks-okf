---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4d0a442d820e951c1f43e79ac4071d3b6346423bda59dbe38f4d1d7faad8ca4
  pageDirectory: concepts
  sources:
    - performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-udf-performance-penalty-in-abac-policies
    - PUPPIAP
  citations:
    - file: performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Python UDF performance penalty in ABAC policies
description: Python UDFs used in ABAC policies must be wrapped in SQL UDFs and are generally slower than SQL UDFs because the optimizer cannot inline or optimize them, and the Python function executes for every row.
tags:
  - performance
  - python-udf
  - abac-policies
timestamp: "2026-06-19T19:54:49.987Z"
---

# Python UDF performance penalty in ABAC policies

**Python UDF performance penalty in ABAC policies** refers to the significant slowdown that occurs when Python user-defined functions (UDFs) are used in [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) row filter or column mask policies, compared to equivalent SQL UDFs. Python UDFs cannot be inlined or optimized by the query engine, and they execute once per row in the target table.

## Overview

Row filter and column mask policies in [Unity Catalog](/concepts/unity-catalog.md) execute a UDF for every row (row filters) or every matching column value (column masks) during query execution. The complexity and implementation language of the UDF directly affect query performance. Python UDFs are particularly costly because the optimizer cannot inline them or apply any plan-level optimizations.^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Why Python UDFs are slower

Python UDFs must be [wrapped in a SQL UDF](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply#wrapper-example) to be used in ABAC policies. This wrapping introduces an additional layer of execution overhead. More importantly, the Python function itself executes for every row in the target table — there is no batching or vectorization.^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

The optimizer cannot inline or optimize Python UDFs. For SQL UDFs, the engine can inspect the function body and apply optimizations such as constant folding or predicate pushdown. For Python UDFs, the function body is opaque, so the optimizer cannot derive any useful information about the function's behavior.^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Performance characteristics

| Language | Optimization | Execution model | Relative performance |
|----------|-------------|----------------|----------------------|
| SQL       | Inlineable, optimizer can inspect body | Executes per row but can be optimized | Faster |
| Python    | Opaque to optimizer, must be wrapped | Executes per row, no inlining | Slower |

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Mitigation: marking Python UDFs as deterministic

If a Python UDF is unavoidable, mark it as `DETERMINISTIC` in the `CREATE FUNCTION` statement to enable result caching for calls with identical arguments. The `DETERMINISTIC` keyword tells the engine that the function returns the same result for the same input every time, which allows the optimizer to cache results and avoid redundant executions.^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

For SQL UDFs, the optimizer derives determinism from the function body automatically. For Python UDFs, the optimizer cannot inspect the function body, so explicitly setting `DETERMINISTIC` is the only way to enable this caching.^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Best practices

**Do:**

- Use SQL UDFs instead of Python UDFs whenever possible.
- Mark any necessary Python UDFs as `DETERMINISTIC`.
- Keep UDFs simple with basic `CASE` statements and boolean expressions.
- Reference only target table columns in UDFs to enable [predicate pushdown](/concepts/selective-caching-with-predicate-pushdown.md).

**Avoid:**

- Python UDFs in ABAC policies unless absolutely necessary.
- Complex subqueries or joins against large tables within UDFs.
- External API calls or per-row metadata lookups.

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## See also

- Reduce UDF complexity — Guidance on keeping UDFs simple for performance
- [Use deterministic, error-safe expressions](/concepts/deterministic-and-error-safe-expressions-in-policy-udfs.md) — How determinism affects optimizer behavior
- [Predicate pushdown on protected tables](/concepts/secureview-barrier-and-predicate-pushdown-on-protected-tables.md) — How the SecureView barrier interacts with UDFs
- SecureView barrier — The barrier that limits predicate pushdown for protected tables

## Sources

- performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws-b415eba9.md)
