---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42aad01acccfee02b0368b1c9f0fa5b1ae25c68c35b37c6efeda168010b65683
  pageDirectory: concepts
  sources:
    - migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - when-to-avoid-delta-lake-conversion
    - WTADLC
  citations:
    - file: migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
title: When to Avoid Delta Lake Conversion
description: Scenarios where maintaining Parquet format may be preferable, such as upstream/downstream system incompatibility with Delta Lake.
tags:
  - delta-lake
  - parquet
  - architecture
timestamp: "2026-06-19T19:32:03.114Z"
---

# When to Avoid Delta Lake Conversion

**When to Avoid Delta Lake Conversion** describes scenarios where maintaining data in Parquet format is preferable to converting to [Delta Lake](/concepts/delta-lake.md), despite Delta Lake being the recommended format for most Databricks lakehouse workloads. Understanding these exceptions helps practitioners make informed migration decisions.

## Overview

Delta Lake is built on top of Parquet and provides many optimized features for the Databricks lakehouse, including [ACID transactions](/concepts/delta-acid-transactions.md), schema enforcement, and [time travel](/concepts/delta-lake-time-travel.md). Databricks recommends using Delta Lake for all tables that receive regular updates or queries from Databricks. However, there are specific cases where maintaining data in Parquet format is the better choice. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## When to Keep Parquet Format

### Upstream Systems Without Delta Lake Support

If an upstream system that writes data to Parquet does not support native writing to Delta Lake, you may need to keep the data in Parquet format. In this case, you might consider replicating the data to Delta Lake to leverage performance benefits while reading, writing, updating, and deleting records in the table. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

### Downstream Systems Without Delta Lake Support

If a downstream system that reads Parquet data cannot read Delta Lake, maintaining the original Parquet format may be necessary. As with upstream systems, replication to Delta Lake can provide performance benefits while preserving the original format for downstream consumers. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Important Considerations

### Concurrent Modifications on S3

Simultaneously modifying data in the same Delta table stored in S3 from multiple workspaces or data systems is not recommended. This limitation may influence your decision to convert certain tables, particularly those accessed by multiple independent systems. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

### Over-Partitioned Tables

While you can convert to Delta Lake and maintain your existing partitioning structure, over-partitioned tables are one of the main culprits that cause slow workloads on Delta Lake. If your Parquet data lake has a partitioning strategy optimized for existing workloads, you should evaluate whether that strategy is appropriate for Delta Lake before converting. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Alternative Approach: Replication

In both upstream and downstream compatibility scenarios, you might want to replicate your tables to Delta Lake to leverage performance benefits while reading, writing, updating, and deleting records in the table. This approach allows you to maintain the original Parquet format for compatibility while gaining Delta Lake benefits for Databricks workloads. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying format in the Databricks lakehouse
- [Parquet to Delta Lake Migration](/concepts/parquet-to-delta-lake-migration.md) — Approaches for converting Parquet data lakes
- [CLONE Parquet](/concepts/clone-parquet.md) — Incremental migration using shallow or deep clones
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — Single-command transformation to Delta Lake
- [Delta Lake Limitations on S3](/concepts/delta-lake-limitations-on-s3.md) — Constraints for concurrent modifications
- Table Partitioning on Databricks — Guidelines for partitioning strategies

## Sources

- migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md

# Citations

1. [migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md](/references/migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws-01ccec95.md)
