---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1bf53ee8fdaf8cee8faeede7fd8a8398fe022cc691147f95eb25c54bd3b912b1
  pageDirectory: concepts
  sources:
    - create-bloom-filter-index-deprecated-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-bloom-filter-index
    - CBFI
  citations:
    - file: create-bloom-filter-index-deprecated-databricks-on-aws.md
title: CREATE BLOOM FILTER INDEX
description: The deprecated SQL command for creating Bloom filter indexes on Delta tables; no longer recommended for use.
tags:
  - databricks
  - sql
  - deprecated
timestamp: "2026-06-19T14:36:12.004Z"
---

Here is the wiki page for "CREATE BLOOM FILTER INDEX".

---

## CREATE BLOOM FILTER INDEX

**CREATE BLOOM FILTER INDEX** is a SQL command in Databricks that was used to create a [Bloom Filter Index](/concepts/bloom-filter-index.md) on columns in a [Delta Lake](/concepts/delta-lake.md) table. Bloom filter indexes improve query performance by skipping over data files that cannot possibly contain a requested value for the indexed column.

## Deprecation

Bloom filter indexes are deprecated. Do not create new Bloom filter indexes. Existing indexes may continue to work but are not recommended for new development.^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

### Recommended Replacements

Replace bloom filter indexes with one of the following features:

- [Predictive I/O](/concepts/predictive-io.md) — A Databricks optimization that automatically determines which data files to read for a query without requiring manual index creation.
- [Liquid Clustering](/concepts/liquid-clustering.md) — A table optimization technique that automatically reorganizes data to improve query performance by co-locating related data.

For details and migration guidance from bloom filter indexes to these alternatives, see [Bloom filter indexes (deprecated)|the Bloom filter indexes documentation](/concepts/bloom-filter-index-deprecated.md).^[create-bloom-filter-index-deprecated-databricks-on-aws.md]

## Related Concepts

- [Bloom Filter Index (Deprecated)](/concepts/bloom-filter-index-deprecated.md)
- [Predictive I/O](/concepts/predictive-io.md)
- [Liquid Clustering](/concepts/liquid-clustering.md)
- [Delta Lake](/concepts/delta-lake.md)
- Query Optimization in Databricks

## Sources

- create-bloom-filter-index-deprecated-databricks-on-aws.md

# Citations

1. [create-bloom-filter-index-deprecated-databricks-on-aws.md](/references/create-bloom-filter-index-deprecated-databricks-on-aws-ac15d2e3.md)
