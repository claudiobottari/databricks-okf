---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed9247595d68936c6650f147cbad94332a8189defabfff4dfe00d3816b6265a6
  pageDirectory: concepts
  sources:
    - row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-type-casting-for-column-mask-functions
    - ATCFCMF
  citations:
    - file: row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
title: Automatic Type Casting for Column Mask Functions
description: Databricks automatically casts input column values to match the mask function's parameter type and the function output to match the target column's data type, with special support for struct-to-VARIANT casting on Runtime 18.1+.
tags:
  - abac
  - column-masks
  - type-casting
  - udf
timestamp: "2026-06-19T20:15:53.207Z"
---

# Automatic Type Casting for Column Mask Functions

**Automatic Type Casting for Column Mask Functions** is a Databricks Runtime feature that ensures type consistency when column masks are applied through ABAC policies. When an ABAC column mask policy resolves at query time, Databricks automatically casts both the input to the mask function and its output to the appropriate data types.

## Overview

When a column mask function is executed as a result of policy evaluation, Databricks performs automatic type casting in two directions: the input column value is cast to match the mask function's parameter type, and the function's output is cast to match the target column's data type. This ensures reliable query behavior and prevents type mismatches during query execution. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## How It Works

The automatic casting process follows three steps:

1. **Masking function execution**: When policy evaluation determines that masking applies, the masking function executes on the matching column values.
2. **Automatic type casting**: Databricks casts the input column value to match the function's parameter type, and casts the function output to match the target column's data type.
3. **Result return**: The properly typed result is returned to the query.

^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Compatibility and Error Handling

If the input or output types aren't compatible, the cast fails and the query returns a runtime error. Casting follows ANSI SQL standards for `CAST` operations, with one addition: on Databricks Runtime 18.1 and above, ABAC column mask policies can cast structs to `VARIANT`, which isn't supported in general SQL. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Best Practices

You must ensure mask functions return types compatible with target columns. For examples and the VARIANT approach for flexible masking across column types, see [Cast-compatible masking functions](/concepts/cast-compatible-masking-functions.md). ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Related Concepts

- ABAC Policies — Attribute-based access control for Unity Catalog securable objects.
- [Column Mask Functions](/concepts/column-masks-unity-catalog.md) — User-defined functions (UDFs) that transform column values for masking.
- [Row Filters](/concepts/row-filter-policies.md) — Similar enforcement mechanism for row-level filtering.
- [Policy Evaluation and Enforcement](/concepts/abac-policy-evaluation-and-enforcement.md) — The two-stage process (Unity Catalog evaluation and Databricks Runtime enforcement) for ABAC policies.

## Sources

- row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md

# Citations

1. [row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md](/references/row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws-2d8da254.md)
