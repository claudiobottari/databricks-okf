---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 065e04c83c444bcebe29b6120665279abf629da1eb1afbcfcecb6c4556e393e2
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake
    - Delta Lake DML
    - Delta Lake SQL
    - Data lake
    - Delta Lake Views
    - Delta Lake format
    - Delta Lake on AWS
    - Delta Lake on S3
    - VACUUM for Delta Lake
    - data lakes
    - deltalake library
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
    - file: what-is-delta-lake-in-databricks-databricks-on-aws.md
title: Delta Lake
description: An open source storage layer that brings reliability, ACID transactions, scalable metadata handling, and unified streaming/batch processing to data lakes.
tags:
  - data-lake
  - storage-layer
  - open-source
timestamp: "2026-06-19T18:20:18.059Z"
---



# Delta Lake

**Delta Lake** is an open source storage layer that brings reliability to data lakes by extending Parquet data files with a file-based [transaction log](/concepts/delta-transaction-log.md). It provides [ACID transactions](/concepts/delta-acid-transactions.md), scalable metadata handling, and unifies streaming and batch data processing. Delta Lake runs on top of your existing data lake and is fully compatible with Apache Spark APIs. ^[delta-lake-api-reference-databricks-on-aws.md, what-is-delta-lake-in-databricks-databricks-on-aws.md]

## Key Features

Delta Lake provides the following core capabilities:

- **ACID transactions** – Ensures data integrity with atomic, consistent, isolated, and durable transactions, even with concurrent readers and writers. ^[delta-lake-api-reference-databricks-on-aws.md, what-is-delta-lake-in-databricks-databricks-on-aws.md]
- **Scalable metadata handling** – The [transaction log](/concepts/delta-transaction-log.md) scales efficiently with large numbers of files, avoiding metadata bottlenecks common in classical data lakes. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Unified streaming and batch** – The same [Delta Lake Table](/concepts/delta-lake-table.md) can serve as both a source and sink for [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) and batch workloads, enabling incremental processing at scale with a single copy of data. ^[what-is-delta-lake-in-databricks-databricks-on-aws.md]
- **Schema enforcement and evolution** – Delta Lake validates schema on write, preventing data corruption. It supports schema updates (rename, drop, add columns) without rewriting data. ^[what-is-delta-lake-in-databricks-databricks-on-aws.md]
- **Time travel** – Each write creates a new table version. The transaction log enables reviewing modifications and querying previous table versions. ^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## Usage on Databricks

Delta Lake is the default format for all tables on Databricks. All operations use Delta Lake unless otherwise specified. Databricks originally developed the Delta Lake protocol and continues to actively contribute to the open source project. ^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

You can use standard Spark SQL or [Apache Spark DataFrame](/concepts/apache-spark-dataframes-to-tfrecord-conversion.md) APIs for most read and write operations. For Delta Lake–specific SQL statements, see the Delta Lake statements documentation. ^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

Databricks ensures binary compatibility with Delta Lake APIs in Databricks Runtime. To view the Delta Lake API version packaged in each Databricks Runtime version, see the **System environment** section in the [Databricks Runtime release notes](https://docs.databricks.com/aws/en/release-notes/runtime/). ^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## API References

API references for Scala, Java, and Python are available on the [Delta Lake website](https://docs.delta.io/latest/delta-apidoc.html#delta-spark). ^[delta-lake-api-reference-databricks-on-aws.md]

To learn how to use Delta Lake APIs on Databricks, see:
- [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta/)
- [Tutorial: Create and manage Delta Lake tables](https://docs.databricks.com/aws/en/delta/tutorial)
- [Delta Lake API documentation](https://docs.databricks.com/aws/en/delta/#delta-api) within the Databricks documentation

^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- [ACID transactions](/concepts/delta-acid-transactions.md)
- data lake
- Apache Spark
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)
- [transaction log](/concepts/delta-transaction-log.md)
- Databricks
- Parquet
- Schema enforcement

## Sources

- delta-lake-api-reference-databricks-on-aws.md
- what-is-delta-lake-in-databricks-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
2. [what-is-delta-lake-in-databricks-databricks-on-aws.md](/references/what-is-delta-lake-in-databricks-databricks-on-aws-49c98a82.md)
