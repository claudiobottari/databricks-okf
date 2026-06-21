---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f70b226ec53d67bd38a2ca110971297712da65d40bedc14a98cfb61978038d1
  pageDirectory: concepts
  sources:
    - performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deterministic-and-error-safe-expressions-in-policy-udfs
    - error-safe expressions in policy UDFs and Deterministic
    - DAEEIPU
    - Deterministic vs non-deterministic expressions
    - Use deterministic, error-safe expressions
  citations:
    - file: performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Deterministic and error-safe expressions in policy UDFs
description: Using DETERMINISTIC functions and error-safe alternatives (try_divide, try_cast, try_to_number) in policy UDFs enables the optimizer to cache results, apply constant folding, and safely rearrange query plans without risking side-channel data leakage.
tags:
  - optimization
  - deterministic-functions
  - udf-design
timestamp: "2026-06-19T19:54:33.929Z"
---

# Deterministic and Error‑Safe Expressions in Policy UDFs

**Deterministic and error‑safe expressions** are a recommended design pattern for user‑defined functions (UDFs) used in [row filter](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md) on Databricks. Following this pattern enables the SQL optimizer to apply caching, constant folding, and predicate pushdown, which directly improves query performance against protected tables. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Deterministic UDFs

A **deterministic** function always returns the same output for the same input. Non‑deterministic functions — such as `rand()` or `now()` — prevent the optimizer from caching results or applying constant folding, because the value could change across invocations. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Marking UDFs as Deterministic

Both SQL and Python UDFs support the `DETERMINISTIC` keyword in the `CREATE FUNCTION` statement. For SQL UDFs, the optimizer derives determinism from the function body automatically, but you can set it explicitly for clarity. For Python UDFs, the optimizer cannot inspect the function body, so explicitly marking a Python UDF as `DETERMINISTIC` is essential to enable result caching for calls with identical arguments. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Error‑Safe Expressions

Expressions that throw errors on invalid inputs — such as ANSI division by zero — can block optimizations. When the SQL compiler detects that an expression might throw an error, it cannot safely push operations like filters down in the query plan; doing so could trigger errors that reveal information about values before filtering or masking takes effect. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

To avoid this, use error‑safe alternatives that return `NULL` instead of throwing exceptions:

| Risky expression | Error‑safe alternative |
|------------------|------------------------|
| `/` (ANSI division) | `try_divide` |
| `CAST` | `try_cast` |
| `to_number` | `try_to_number` |

These alternatives let the optimizer rearrange and fold expressions freely. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Scope

These considerations apply only to row filter and column mask policies that execute UDFs at query time. GRANT policies (Beta) are not subject to them. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- ABAC policy performance considerations
- [Predicate pushdown on protected tables](/concepts/secureview-barrier-and-predicate-pushdown-on-protected-tables.md)
- UDF optimization

## Sources

- performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws-b415eba9.md)
