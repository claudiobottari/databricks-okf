---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f20fd1ad87b95cf7682934848bbb4b494203ecff402d645575432065ac24f183
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-apache-spark-compatibility
    - DLASC
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Delta Lake Apache Spark Compatibility
description: Delta Lake runs on top of existing data lakes and is fully compatible with Apache Spark APIs.
tags:
  - apache-spark
  - compatibility
timestamp: "2026-06-18T11:48:28.923Z"
---

# Delta Lake Apache Spark Compatibility

**Delta Lake** is an open source storage layer that brings reliability and performance to data lakes. It is built on top of existing data lake infrastructure and is designed to be fully compatible with **Apache Spark APIs**. This means that any Spark application can read from and write to Delta tables using standard Spark DataFrame and SQL operations, with no additional configuration or code changes required. ^[delta-lake-api-reference-databricks-on-aws.md]

## Key Features That Spark Applications Leverage

Delta Lake provides ACID transactions, scalable metadata handling, and unified streaming and batch data processing — all of which are available through Spark’s standard APIs. Spark jobs that use Delta Lake benefit from:

- **ACID transactions**: Multiple concurrent readers and writers see a consistent snapshot of the data, with automatic conflict resolution.
- **Scalable metadata**: Delta Lake handles large numbers of files and partitions without performance degradation, even with petabytes of data.
- **Unified batch and streaming**: The same Delta table can serve as both a batch source/sink and a streaming source/sink using Spark Structured Streaming.

Because Delta Lake exposes these capabilities through the Spark SQL and PySpark APIs, existing ETL pipelines, machine learning workflows, and analytics queries require minimal migration effort. ^[delta-lake-api-reference-databricks-on-aws.md]

## API References

The Delta Lake project provides official API references for Scala, Java, and Python on the [Delta Lake website](https://docs.delta.io/latest/delta-apidoc.html#delta-spark). For use on Databricks, refer to the [Databricks Delta Lake documentation](https://docs.databricks.com/aws/en/delta/) for tutorials and API guidance. ^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer powering reliable data lakes
- Apache Spark — The unified analytics engine Delta Lake is fully compatible with
- [ACID Transactions on Data Lakes](/concepts/acid-transactions-on-data-lakes.md) — Transactional guarantees provided by Delta Lake
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — Real-time stream processing against Delta tables
- [Delta table](/concepts/delta-lake-table.md) — The core storage abstraction built on top of Parquet files

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
