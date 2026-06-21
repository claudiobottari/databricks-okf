---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 077888a755cd1b6e25a934311bfb03e976b7dc2567c7d5ce3a9a527a22bd8dc9
  pageDirectory: concepts
  sources:
    - migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-partitioning-considerations
    - DLPC
  citations:
    - file: migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
title: Delta Lake Partitioning Considerations
description: Guidance on avoiding over-partitioned tables when migrating from Parquet to Delta Lake, as over-partitioning is a common cause of slow workloads.
tags:
  - delta-lake
  - performance
  - partitioning
timestamp: "2026-06-19T19:32:49.269Z"
---

# Delta Lake Partitioning Considerations

**Delta Lake Partitioning Considerations** refers to the design decisions and trade-offs involved in choosing a partitioning strategy for [Delta Lake](/concepts/delta-lake.md) tables, especially when migrating from an existing Parquet data lake. An effective partitioning scheme is critical for query performance and storage efficiency, but common patterns from Parquet-based lakes can lead to suboptimal behavior in Delta Lake.

## Context and Common Pitfall

When migrating a Parquet data lake to Delta Lake, the existing partitioning strategy has usually been optimized for the legacy workloads and systems. While you can convert to Delta Lake and maintain this same partitioning structure, **over-partitioning** is one of the main causes of slow workloads on Delta Lake. Over-partitioned tables introduce excessive file metadata, increase the number of small files, and degrade the performance of operations like `MERGE`, `UPDATE`, and compaction. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Recommendations for Partitioning in Delta Lake

Databricks recommends reconsidering the partitioning strategy during or after conversion. General guidance includes:

- **Avoid over-partitioning** – choose partition columns with low-to-medium cardinality and use a reasonable number of partitions (typically tens to a few thousand). Over-partitioning creates many small files that reduce the benefit of data skipping and increase I/O overhead.
- **Leverage Delta Lake features** – Delta Lake’s data skipping (through file statistics) and `ZORDER` indexing can often reduce the need for fine-grained partitioning.
- **Follow established guidelines** – The Databricks documentation provides dedicated best practices in [When to partition tables on Databricks](https://docs.databricks.com/aws/en/tables/partitions) and [guidelines for adapting Spark code to Databricks](https://docs.databricks.com/aws/en/migration/spark#parquet-delta). ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Partitioning During Migration

The migration method you choose (e.g., `CLONE`, `CONVERT TO DELTA`, Auto Loader, or custom batch logic) determines whether the original partitioning is preserved or can be restructured. For example:

- **Shallow clone** keeps the original Parquet files in place and preserves the directory structure, inheriting the partitioning.
- **Deep clone** copies data to a new location and can optionally rewrite the data with a different partitioning scheme.
- **`CONVERT TO DELTA`** transforms the existing directory of Parquet files in place, maintaining the original partition layout.
- **Auto Loader or custom batch logic** allows you to re-partition the data when writing the target Delta table, offering the most flexibility. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Key Takeaway

When moving from Parquet to Delta Lake, do not assume the original partitioning strategy is optimal. Evaluate whether the table is over-partitioned and consider adjusting the partition scheme to align with Delta Lake’s strengths, such as data skipping and optimized file sizes.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying format for the Databricks lakehouse.
- Parquet – The predecessor format; Delta Lake is built on Parquet.
- Table Partitioning – General concept of splitting data by column values.
- [Data Lakehouse](/concepts/avoiding-data-silos-in-lakehouse.md) – The architecture enabled by Delta Lake.
- [Optimizing Delta Lake Performance](/concepts/delta-lake-merge-performance-tuning.md) – Broader topic including compaction, ZORDER, and vacuum.

## Sources

- migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md

# Citations

1. [migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md](/references/migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws-01ccec95.md)
