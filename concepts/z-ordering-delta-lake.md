---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75274729fb7017ac4aedac41d5150be3bb459f1e20b16bad0fb234dd0c2730c8
  pageDirectory: concepts
  sources:
    - optimize-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - z-ordering-delta-lake
    - Z(L
    - Z-ordering in Delta Lake
    - Data skipping in Delta Lake
    - Z-Ordering
    - Z-ordering
  citations:
    - file: optimize-databricks-on-aws.md
title: Z-Ordering (Delta Lake)
description: A non-idempotent, incremental clustering technique that co-locates related data by number of tuples, improving data skipping performance.
tags:
  - delta-lake
  - optimization
  - data-engineering
timestamp: "2026-06-19T19:51:14.635Z"
---

## Z-Ordering (Delta Lake)

**Z-Ordering** is a data layout optimization technique for [Delta Lake](/concepts/delta-lake.md) that clusters related data within files based on one or more specified columns. It is designed to improve query performance by reducing the amount of data scanned during filter operations. ^[optimize-databricks-on-aws.md]

### Characteristics

- **Not idempotent**: Running Z-Ordering on a dataset multiple times can produce different file layouts; it operates incrementally rather than being a fixed transformation. The time required for Z-Ordering is not guaranteed to decrease over successive runs. However, if no new data has been added to a partition that was just Z-Ordered, running Z-Ordering again on that partition has no effect. ^[optimize-databricks-on-aws.md]

- **Tuple-balanced, not size-balanced**: Z-Ordering produces files that are evenly balanced with respect to the number of tuples (rows), but not necessarily with respect to file size on disk. This contrasts with [Bin-packing optimization](/concepts/bin-packing-optimization-delta-lake.md), which balances file sizes but not tuple counts. While the two measures are often correlated, divergence can cause skew in optimization task times. ^[optimize-databricks-on-aws.md]

- **Incremental**: Because Z-Ordering is not idempotent, each run can further refine the clustering. This incremental nature makes it suitable for continuously updated tables. The optimization only re‑organizes files within a partition; it does not affect partitions that have not changed since the last run. ^[optimize-databricks-on-aws.md]

### Comparison with Bin‑packing

| Property | Bin‑packing (Delta Lake OPTIMIZE) | Z-Ordering (Delta Lake) |
|----------|-----------------------------------|--------------------------|
| Idempotent | Yes | No |
| Balancing criteria | File size on disk | Number of tuples (rows) |
| Behavior on repeated runs | No effect on same data set | Operates incrementally; time not guaranteed to shrink |

^[optimize-databricks-on-aws.md]

### Use Cases

Z-Ordering is most beneficial when queries frequently filter on specific columns (e.g., date, customer ID, region). By co‑locating rows with similar values into the same files, Z-Ordering reduces the number of files that must be read for a given filter predicate.

### Related Concepts

- [Delta Lake OPTIMIZE](/concepts/delta-lake-optimized-writes.md) — The command that triggers both bin‑packing and Z-Ordering.
- [Bin-packing optimization](/concepts/bin-packing-optimization-delta-lake.md) — A complementary technique that compacts small files.
- Data Partitioning — Physical layout of table data into directories.
- Idempotent — Property of an operation that produces the same result regardless of how many times it is applied.

### Sources

- optimize-databricks-on-aws.md

# Citations

1. [optimize-databricks-on-aws.md](/references/optimize-databricks-on-aws-342a11f5.md)
