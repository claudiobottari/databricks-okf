---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1589b4a6b9e49e4665784aafc27d888bd5d94b1dc9982cb36e36507f7ea2c161
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
    - what-is-delta-lake-in-databricks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-transaction-log
    - DLTL
    - Delta Lake Transactions
    - Delta Lake transaction history
    - Delta Lake transactions
    - Delta Table Transaction Log
    - Delta Lake Read Transactions
  citations:
    - file: what-is-delta-lake-in-databricks-databricks-on-aws.md
    - file: convert-to-delta-databricks-on-aws.md
title: Delta Lake Transaction Log
description: The metadata structure created during CONVERT TO DELTA that tracks all Parquet files, infers schema from file footers, and enables Delta Lake features on the table.
tags:
  - delta-lake
  - metadata
  - architecture
timestamp: "2026-06-19T17:53:02.693Z"
---

# Delta Lake Transaction Log

The **Delta Lake transaction log** (also known as the Delta Log) is a file-based transaction log that extends Parquet data files with ACID transaction support and scalable metadata handling. It records every change made to a Delta table, ensuring atomicity, consistency, isolation, and durability for all operations. The transaction log has a well-defined open protocol that any system can use to read the log.^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## Overview

The Delta Lake transaction log is stored as a series of JSON files within a `_delta_log` directory, located alongside the table's Parquet data files. Each write operation — insert, update, delete, or merge — creates a new entry in the log. This mechanism enables ACID transactions, scalable metadata handling, and time travel capabilities (querying previous table versions).^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

Databricks recommends that you avoid interacting directly with data and transaction log files in Delta Lake file directories to prevent table corruption.^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## How the Transaction Log Works

When a Delta table is written to, the transaction log records the set of files that are part of the table at each version, along with metadata such as schema changes, partition information, and operation details. Each write to a [Delta Lake Table](/concepts/delta-lake-table.md) creates a new table version. The transaction log can be used to review modifications and query previous table versions.^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## Open Protocol

The Delta Lake transaction log follows a well-defined open protocol documented in the [Delta Transaction Log Protocol](/concepts/delta-lake-table-protocol-changes.md) specification. This protocol allows tools and engines beyond Apache Spark — such as Presto, Apache Flink, and Trino — to read Delta tables by parsing the transaction log directly, without requiring proprietary connectors.^[what-is-delta-lake-in-databricks-databricks-on-aws.md]

## Converting to Delta Lake

When you convert an existing Apache Parquet table to a Delta table using `CONVERT TO DELTA`, the command lists all files in the directory, creates a Delta Lake transaction log that tracks these files, and automatically infers the data schema by reading the footers of all Parquet files. The conversion process collects statistics to improve query performance on the converted table.^[convert-to-delta-databricks-on-aws.md]

For Apache Iceberg tables whose underlying file format is Parquet, the converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information.^[convert-to-delta-databricks-on-aws.md]

The `NO STATISTICS` option can be used to bypass statistics collection during conversion and finish faster. After conversion, Databricks recommends using liquid clustering to reorganize data layout and generate statistics.^[convert-to-delta-databricks-on-aws.md]

The `CONVERT TO DELTA` command populates the catalog information, such as schema and table properties, to the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata is different from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown.^[convert-to-delta-databricks-on-aws.md]

## Structure

The `_delta_log` directory contains JSON files named with zero-padded version numbers (e.g., `0000000000000000XXXX.json`), each containing the transaction's actions — such as add file, remove file, or metadata update. Periodically, checkpoint files in Parquet format are created that contain a snapshot of the entire table state at a given version, allowing faster reconstruction without replaying every JSON file.

Any file not tracked by Delta Lake is invisible and can be deleted when you run `VACUUM`.^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The optimized storage layer built on the transaction log
- [ACID Transactions](/concepts/delta-acid-transactions.md) — Guarantees provided by the transaction log
- [Time Travel](/concepts/delta-lake-time-travel.md) — Querying previous table versions using the log
- Data Skipping — Performance optimization using log statistics
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — Creating a transaction log for existing Parquet/Iceberg tables
- [Delta Transaction Log Protocol](/concepts/delta-lake-table-protocol-changes.md) — The open specification for the log format
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended post-conversion data reorganization for statistics generation

## Sources

- what-is-delta-lake-in-databricks-databricks-on-aws.md
- convert-to-delta-databricks-on-aws.md

# Citations

1. [what-is-delta-lake-in-databricks-databricks-on-aws.md](/references/what-is-delta-lake-in-databricks-databricks-on-aws-49c98a82.md)
2. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
