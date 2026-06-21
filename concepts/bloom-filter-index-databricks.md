---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf371c52373f9941f154b14576ece4a15ea5f71e011840e9f7b663a3fdd980fc
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-databricks
    - BFI(
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: Bloom Filter Index (Databricks)
description: A deprecated indexing feature in Databricks that used Bloom filters to speed up data skipping during queries on Delta tables.
tags:
  - databricks
  - indexing
  - deprecated
timestamp: "2026-06-18T14:53:20.369Z"
---

```markdown
# Bloom Filter Index (Databricks)

**Bloom Filter Index (Databricks)** refers to a deprecated data skipping optimization that was previously used to improve query performance on [[Delta Lake]] tables. Bloom filter indexes have been superseded by newer, more effective techniques, and Databricks no longer recommends creating them. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Deprecation Status

Bloom filter indexes are deprecated. Users should not create new Bloom filter indexes on any existing or new tables. ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Recommended Alternatives

Databricks recommends using one of the following alternatives instead of Bloom filter indexes:

- **[[Predictive I/O]]** – A modern data skipping technique that automatically prunes data files based on query predicates.
- **[[Liquid clustering]]** – A flexible clustering approach that replaces the older [[Z-Ordering (Delta Lake)|Z-ordering]] and provides more efficient data skipping for a wide range of queries.

For detailed migration guidance, refer to the documentation on [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters). ^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- Data skipping optimization
- Delta Lake performance tuning
- [[Bloom Filter Index (Deprecated)|CREATE BLOOM FILTER INDEX (deprecated)]] – The deprecated SQL command for creating Bloom filter indexes.

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md
```

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
