---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 879e92de9d31186b79768dc348d85fec029993f3a4932c405a61e586798ad2c7
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-compatibility-with-apache-spark
    - DLCWAS
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Delta Lake Compatibility with Apache Spark
description: Delta Lake runs on top of existing data lakes and is fully compatible with Apache Spark APIs.
tags:
  - apache-spark
  - compatibility
  - integration
timestamp: "2026-06-18T15:15:07.083Z"
---

# Delta Lake Compatibility with Apache Spark

**Delta Lake** is an [open source storage layer](https://delta.io/) that brings reliability to data lakes. It provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. Delta Lake runs on top of your existing data lake and is **fully compatible with Apache Spark APIs**. ^[delta-lake-api-reference-databricks-on-aws.md]

This compatibility means that any code written using the native Spark DataFrame or SQL APIs can be used to read, write, and manipulate Delta Lake tables without modification. Spark’s Catalyst optimizer and Tungsten execution engine work directly with Delta Lake’s transaction log, enabling efficient query planning and execution.

## Compatibility

Delta Lake implements the Spark DataSourceV2 interface for reading and writing data. It supports all Spark data types and provides a drop-in replacement for Parquet or JSON tables in Spark workloads. The following table summarizes key compatibility aspects:

| Feature | Delta Lake Support |
|---------|-------------------|
| Spark SQL DDL/DML | Fully supported (e.g., `CREATE TABLE`, `MERGE`, `UPDATE`, `DELETE`) |
| Structured Streaming | Source and sink for streaming queries |
| Catalyst optimization | Full integration (predicate pushdown, partition pruning, file skipping) |
| Spark Connect | Supported in recent releases |
| Delta Sharing | Works with Spark’s shared DataFrame APIs |

Delta Lake also preserves schema evolution and time travel capabilities while remaining transparent to the Spark execution engine.

## API Support

Delta Lake provides dedicated [Delta Lake API](/concepts/delta-lake-api.md) references for Scala, Java, and Python. These APIs extend Spark’s standard DataFrame API with Delta-specific operations such as `vacuum`, `history`, and `clone`. ^[delta-lake-api-reference-databricks-on-aws.md]

For detailed API documentation, see the [Delta Lake website](https://docs.delta.io/latest/delta-apidoc.html#delta-spark). ^[delta-lake-api-reference-databricks-on-aws.md]

On Databricks, additional guidance is available in the [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta/) tutorial and the [Delta Lake API documentation](https://docs.databricks.com/aws/en/delta/#delta-api). ^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- Apache Spark – The core engine that Delta Lake runs on
- [ACID Transactions](/concepts/delta-acid-transactions.md) – Guaranteed by Delta Lake on data lake storage
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – Unified batch/streaming processing with Delta Lake
- Databricks Runtime – Optimized runtime that includes Delta Lake
- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for sharing Delta tables

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
