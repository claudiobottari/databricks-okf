---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05fb5e805427f412f5b37ded057b9bfbdecbb0474436a2271556054cc602db1f
  pageDirectory: concepts
  sources:
    - performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureview-barrier-and-predicate-pushdown-on-protected-tables
    - predicate pushdown on protected tables and SecureView barrier
    - SBAPPOPT
    - Predicate pushdown on protected tables
  citations:
    - file: performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: SecureView barrier and predicate pushdown on protected tables
description: The SecureView barrier introduced by row filters and column masks blocks certain predicates from being pushed to the storage layer, preventing partition pruning and liquid clustering optimizations. Simple equality predicates can still be pushed down, but functions and implicit casts are blocked, potentially forcing full table scans.
tags:
  - performance
  - predicate-pushdown
  - secureview
  - unity-catalog
timestamp: "2026-06-19T19:54:29.449Z"
---

# SecureView Barrier and Predicate Pushdown on Protected Tables

The **SecureView barrier** is a security boundary automatically introduced by Databricks when a table is protected by [Row Filter](/concepts/row-filter-policies.md) or Column Mask policies (both ABAC and table‑level policies). The barrier prevents predicates with side effects from being pushed across the policy boundary to the storage layer, which protects against side‑channel data leakage. However, the same barrier can block performance optimisations like partition pruning and liquid clustering, forcing full table scans even when the policy itself has no effect on the query result. This is the most common source of performance issues with protected tables and the most difficult to address because policy authors cannot control what queries users run. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## How the Barrier Affects Predicate Pushdown

[Predicate Pushdown](/concepts/selective-caching-with-predicate-pushdown.md) is an optimisation where the engine pushes filter conditions (e.g. `WHERE` clauses) down to the storage layer, allowing it to skip entire partitions of data that do not match the query. For tables protected by row filters or column masks, the `SecureView` barrier appears in the query plan as a `PhotonSecureView` node. The barrier blocks any predicate that could have side effects from being pushed below it, because executing such a predicate before the policy is applied could leak information about rows or column values that the policy would otherwise filter or mask. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

The barrier is present even when the policy UDF resolves to a constant `true` (i.e., no rows are actually filtered). The mere existence of a policy on a table introduces the barrier. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Filters Affected by the Barrier

The optimizer can push only **side‑effect‑free** predicates through the `SecureView` barrier. The following table summarises what is pushed down and what is blocked:

| Category | Behaviour | Example |
|----------|-----------|---------|
| **Pushed down (fast)** | Simple equality comparisons and basic range comparisons that are free of side effects | `WHERE col = 'value'` or `WHERE col > 100` |
| **Blocked (slower)** | Predicates that call functions (e.g., `date_format`, `concat`, `substr`) or introduce implicit type casts | `WHERE date_format(col, 'yyyy-MM-dd') = '1995-07-29'` |

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### EXPLAIN Plan Examples

The following examples contrast the query plans for a table `orders` partitioned on `o_orderdate`:

**Without any policy** — the predicate `date_format(...)` appears in `PartitionFilters` inside the `PhotonScan` node, enabling partition pruning:

```
+- PhotonScan parquet orders[...]
   PartitionFilters: [isnotnull(o_orderdate),
   (date_format(cast(o_orderdate as timestamp), yyyy-MM-dd, ...))]
```

**With a policy** — the `SecureView` barrier blocks the functional predicate, moving it to a `PhotonFilter` above the scan. Partition pruning is lost, resulting in a full table scan:

```
+- PhotonFilter (date_format(cast(o_orderdate as timestamp),
   yyyy-MM-dd, ...) = 1995-07-29)
    +- PhotonSecureView orders
        +- PhotonScan parquet orders[...]
           PartitionFilters: [isnotnull(o_orderdate)]
```

**With a simple equality predicate** — `WHERE o_orderdate = '1995-07-29'` has no side effects and is pushed down through the `SecureView` barrier, preserving partition pruning:

```
+- PhotonSecureView orders
    +- PhotonScan parquet orders[...]
       PartitionFilters: [isnotnull(o_orderdate),
       (o_orderdate = 1995-07-29)]
```

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Mitigations

- **Use simple equality predicates on protected tables** whenever possible. Avoid functional predicates (e.g., `date_format(col, ...) = ...`) that the optimizer cannot prove to be side‑effect‑free. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Use the `EXCEPT` clause** in the policy to exempt users who do not need the policy. When an exempt user queries the table, the `SecureView` barrier is removed entirely, restoring full predicate pushdown and partition pruning. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Keep policy UDFs simple** and reference only target table columns when possible, so that the optimizer can apply predicate pushdown more easily. See [Performance considerations for row filter and column mask policies](/concepts/performance-optimization-for-row-filters-and-column-masks.md). ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Predicate Pushdown](/concepts/selective-caching-with-predicate-pushdown.md)
- Partition Pruning
- [Row Filter](/concepts/row-filter-policies.md)
- Column Mask
- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Photon query engine

## Sources

- performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws-b415eba9.md)
