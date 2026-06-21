---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8bfeadf6fa68a5730dfab61dce01acadac3348bd6331fb483453782237cc64e
  pageDirectory: concepts
  sources:
    - performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lookup-table-optimization-for-abac-policy-udfs
    - LTOFAPU
  citations:
    - file: performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Lookup table optimization for ABAC policy UDFs
description: Using small lookup tables in policy UDFs enables broadcast hash joins where the lookup table is copied to each executor for fast filtering, but large lookup tables or complex predicates force slower shuffle joins.
tags:
  - optimization
  - lookup-tables
  - broadcast-join
  - abac-policies
timestamp: "2026-06-19T19:54:56.814Z"
---

# Lookup table optimization for ABAC policy UDFs

**Lookup table optimization** refers to a set of design patterns and performance considerations for ABAC policies that use [row filters](/concepts/row-filter-policies.md) or [column masks](/concepts/delta-lake-column-masks.md) relying on secondary tables to determine access rights. Because the policy UDF executes for every row (row filter) or every column value (column mask), the choice and structure of any lookup table directly affects query performance. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Overview

A common ABAC pattern is to check access rights against a small lookup table — for example, a table that maps users to allowed priority levels. The performance of such policies depends on the size of the lookup table relative to the target table, the complexity of the join predicate, and whether the optimizer can choose a broadcast hash join over a slower shuffle join. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## When to use lookup tables in policies

Lookup tables are appropriate when the conditional logic required for filtering or masking is too complex to express solely through the policy's `TO`/`EXCEPT` principal clauses. The policy’s identity functions (`current_user()`, `is_account_group_member()`) are resolved once during query analysis and are typically more efficient, but lookup tables can encode mappings that change frequently or are derived from external data sources. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

If a lookup table is unavoidable, ensure it is **significantly smaller** than the target table so the optimizer can treat it as a broadcast relation. Keep the predicate simple (equality checks on indexed columns) to maximize the chance of a broadcast hash join. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Performance characteristics

When the lookup table is small enough to broadcast, the optimizer converts the subquery into a **broadcast hash join**: the lookup table is copied to each executor and stored in memory as a hashmap, enabling fast filtering during the table scan. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

If the lookup table is large, the optimizer falls back to a **shuffle join**, which requires shuffling both tables across the network and is substantially slower. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

Even with a broadcast hash join, every row still incurs the cost of a hash table lookup during execution. Complex predicates (anything beyond a simple equality check) may also make the broadcast join ineligible, forcing a slower join strategy. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Best practices for lookup tables in ABAC UDFs

- **Keep lookup tables small** relative to the target table. The optimizer will automatically use a broadcast hash join if the lookup table fits within the configured broadcast threshold. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Use simple equality predicates** in the lookup condition. Non-equi joins or complex expressions prevent broadcast optimization. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Partition the lookup table by the access pattern** (for example, by username) to minimize scan overhead when the table is used in the UDF. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Avoid referencing large external tables** in the UDF. If an external reference is necessary, ensure it is small enough to broadcast. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Do not use external API calls or per-row metadata lookups** (e.g., querying `information_schema`) inside the policy UDF. These introduce latency and may cause timeouts. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Prefer identity functions** over lookup tables when the mapping can be expressed with `current_user()` or `is_account_group_member()`. These are resolved once per query, not per row, and are more performant. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Avoid Python UDFs** for policy lookup logic. Python UDFs cannot be inlined and execute row-by-row, making them much slower than SQL UDFs that can use broadcast hash joins. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Use deterministic, error-safe expressions** in the UDF. Non‑deterministic functions prevent result caching; error‑prone expressions block predicate pushdown and join optimizations. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Testing lookup table performance

Test UDF performance with at least 1 million rows and with queries that represent the actual workload on the protected table. The following pattern isolates the policy overhead:

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

Replace `your_mask_function` with the UDF under test. Compare results with and without the policy applied to isolate the policy’s overhead. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related concepts

- ABAC policies
- [Row filters](/concepts/row-filter-policies.md)
- [Column masks](/concepts/column-mask-policies.md)
- Broadcast hash join
- Predicate pushdown
- SecureView barrier
- Deterministic UDFs
- [Identity functions in ABAC policies](/concepts/abac-policy-conditions-and-built-in-functions.md)

## Sources

- performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws-b415eba9.md)
