---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a3337e86252a9d01bd6aa10af72b20ae8dc88346e204c4dc3cddb018a942dcf
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apache-spark-api-compatibility-with-delta-lake
    - ASACWDL
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Apache Spark API compatibility with Delta Lake
description: Full compatibility of Delta Lake with Apache Spark APIs, allowing users to leverage existing Spark knowledge and codebases when working with Delta Lake.
timestamp: "2026-06-19T09:59:52.792Z"
---

# Apache Spark API Compatibility with Delta Lake

**Apache Spark API compatibility with Delta Lake** refers to the design principle that Delta Lake is fully compatible with existing Apache Spark APIs, allowing users to work with Delta tables using the same DataFrame, SQL, and streaming APIs they already use with Spark. ^[delta-lake-api-reference-databricks-on-aws.md]

## Overview

Delta Lake is an open source storage layer that runs on top of existing data lakes. A key design goal is maintaining full compatibility with Apache Spark APIs so that users can adopt Delta Lake without learning new programming interfaces or rewriting existing code. ^[delta-lake-api-reference-databricks-on-aws.md]

By providing ACID transactions, scalable metadata handling, and unified streaming and batch processing, Delta Lake enhances the reliability of data lakes while preserving the familiar Spark programming model. ^[delta-lake-api-reference-databricks-on-aws.md]

## Supported APIs

Delta Lake is fully compatible with the following Apache Spark APIs:

- **Scala API** – Delta Lake tables can be read and written using the standard Spark Scala DataFrame and Dataset APIs. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Java API** – Java applications can interact with Delta tables using the same Spark Java interfaces. ^[delta-lake-api-reference-databricks-on-aws.md]
- **Python API** – PySpark users can read, write, and manipulate Delta tables using the familiar PySpark DataFrame API. ^[delta-lake-api-reference-databricks-on-aws.md]
- **SQL API** – Delta Lake supports standard Spark SQL statements for creating, querying, and modifying Delta tables. ^[delta-lake-api-reference-databricks-on-aws.md]

## Streaming Compatibility

Delta Lake unifies streaming and batch data processing. Users can apply [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) APIs to Delta tables for both stream reading and stream writing, enabling continuous ingestion and processing pipelines. ^[delta-lake-api-reference-databricks-on-aws.md]

## Delta Lake-Specific APIs

While Delta Lake is compatible with general Spark APIs, it also provides additional Delta-specific APIs for advanced operations. These are documented in the Delta Lake API reference for Scala, Java, and Python on the [Delta Lake website](https://docs.delta.io/latest/delta-apidoc.html#delta-spark). ^[delta-lake-api-reference-databricks-on-aws.md]

## Getting Started

To learn how to use Delta Lake APIs on Databricks:

- [What is Delta Lake in Databricks?](/concepts/delta-lake-on-databricks.md)
- Tutorial: Create and manage Delta Lake tables

For detailed API documentation, see the [Delta Lake API documentation](https://docs.databricks.com/aws/en/delta/#delta-api) in the Databricks documentation. ^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The open source storage layer providing ACID transactions on data lakes.
- Apache Spark DataFrames – The primary API for working with structured data in Spark.
- [Delta Lake on Databricks](/concepts/delta-lake-on-databricks.md) – Managed Delta Lake experience within the Databricks platform.
- Structured Streaming with Delta Lake – Streaming data processing on Delta tables.

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
