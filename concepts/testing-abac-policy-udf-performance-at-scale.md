---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10102faee493af41ebebd840f2f63971cab76c8f69fbec25877916c2e1928df0
  pageDirectory: concepts
  sources:
    - performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - testing-abac-policy-udf-performance-at-scale
    - TAPUPAS
  citations:
    - file: performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Testing ABAC policy UDF performance at scale
description: Guidelines for testing policy UDFs on at least 1 million rows before production deployment, including a template SQL query using range() and WITH test_data to isolate policy overhead.
tags:
  - testing
  - performance
  - abac-policies
  - udf
timestamp: "2026-06-19T19:54:38.732Z"
---

# Testing ABAC Policy UDF Performance at Scale

**Testing ABAC policy UDF performance at scale** refers to the practice of evaluating the runtime impact of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy user-defined functions (UDFs) on large datasets before deploying them to production. Because row filter and column mask policies execute UDFs at query time, their performance characteristics must be validated against representative data volumes and query patterns. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Why Scale Testing Matters

Row filter UDFs execute for every row in the target table, and column mask UDFs execute for every matching column value. Even a simple UDF can introduce significant overhead when applied to millions of rows. Testing at scale reveals performance bottlenecks that are invisible on small datasets, such as full table scans caused by the SecureView barrier or slow hash table lookups from large lookup tables. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Recommended Approach

### Test on at Least 1 Million Rows

Before deploying a policy to production, test UDF performance on at least 1 million rows. This volume is sufficient to surface partition pruning failures, broadcast join eligibility issues, and per-row execution costs. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Use Representative Queries

In addition to synthetic scale tests, run queries that represent the actual workload you expect on the protected table. Different query patterns (simple equality filters, range scans, aggregations, joins) interact differently with the SecureView barrier and the optimizer's ability to push predicates down. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Measure Incrementally

Make incremental changes to your policy functions and measure the effect of each change rather than testing only the final version. This approach helps isolate which design decisions (e.g., adding a lookup table join, introducing a regex, switching from SQL to Python UDF) cause performance regressions. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Example: Synthetic Scale Test

The following SQL pattern tests a mask UDF against 1 million rows and reports total processing time:

```sql
WITH test_data AS (
  SELECT
    id,
    your_mask_function(id) AS masked_id,
    current_timestamp() AS ts
  FROM (
    SELECT CONCAT('ID', LPAD(CAST(id AS STRING), 6, '0')) AS id
    FROM range(1000000)
  )
)
SELECT
  COUNT(*) AS rows_processed,
  MAX(ts) - MIN(ts) AS total_duration
FROM test_data;
```

Replace `your_mask_function` with the UDF you are testing. Compare results with and without the policy applied to isolate the policy's overhead. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## What to Look For

When testing at scale, watch for the following indicators of poor performance:

- **Full table scans** where partition pruning or liquid clustering should apply. Check the `EXPLAIN` plan for predicates appearing in `PhotonFilter` above the `PhotonSecureView` node instead of in `PartitionFilters` inside the scan. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Shuffle joins** instead of broadcast hash joins when the policy references a lookup table. If the lookup table is large or the join predicate is complex, the optimizer falls back to a slower shuffle join. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **High per-row latency** from Python UDFs, regex on large text fields, or external API calls. These operations execute for every row and cannot be optimized by the query engine. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Performance considerations for row filter and column mask policies](/concepts/performance-optimization-for-row-filters-and-column-masks.md) — Full guidance on UDF design, predicate pushdown, and the SecureView barrier.
- SecureView barrier — The mechanism that blocks predicate pushdown across policy boundaries.
- Predicate pushdown — Optimization that pushes filter conditions to the storage layer.
- Broadcast hash join — Fast join strategy for small lookup tables in policy UDFs.
- [Row Filter Policies](/concepts/row-filter-policies.md) — Policies that filter rows based on UDF evaluation.
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policies that transform column values based on UDF evaluation.
- EXPLAIN command — Tool for inspecting query plans and identifying performance issues.

## Sources

- performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws-b415eba9.md)
