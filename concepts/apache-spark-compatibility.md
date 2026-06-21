---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba12ab49871f8a722b359d094dad8725b8c2af0a8520c350af9dc350d9964221
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apache-spark-compatibility
    - ASC
    - PySpark Compatibility
    - OSS Apache Spark
    - Spark API Compatibility
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Apache Spark Compatibility
description: Delta Lake is fully compatible with Apache Spark APIs, allowing users to leverage existing Spark code and workflows when working with Delta Lake tables.
tags:
  - apache-spark
  - compatibility
  - integration
timestamp: "2026-06-19T18:20:19.178Z"
---

# Apache Spark Compatibility

**Apache Spark Compatibility** for [Delta Lake](/concepts/delta-lake.md) means that Delta Lake tables work seamlessly with the standard Apache Spark APIs. Because Delta Lake is built as a storage layer on top of an existing data lake, it does not require any changes to how users write Spark code; all existing Spark DataFrame, SQL, and RDD operations can read from and write to Delta tables. ^[delta-lake-api-reference-databricks-on-aws.md]

## Compatibility Details

Delta Lake is **fully compatible with Apache Spark APIs**. This compatibility extends to all major Spark programming languages — Scala, Java, and Python — and covers both batch and streaming operations. ^[delta-lake-api-reference-databricks-on-aws.md]

Because Delta Lake operates as a file-format layer rather than a separate system, Spark jobs that use DataFrame readers/writers or the Spark SQL engine can directly access Delta tables simply by specifying the Delta format. No additional connectors or configuration changes are needed to leverage Delta Lake’s reliability features. ^[delta-lake-api-reference-databricks-on-aws.md]

## API Support

Delta Lake provides dedicated API references for Scala, Java, and Python on the [Delta Lake website](https://docs.delta.io/latest/delta-apidoc.html#delta-spark). These APIs extend the standard Spark APIs with Delta‑specific operations such as time travel, schema enforcement, and vacuum. However, the core compatibility guarantee means that any Spark code written for Parquet or other formats can be migrated to Delta Lake with minimal effort. ^[delta-lake-api-reference-databricks-on-aws.md]

## Benefits of Compatibility

The close integration between Delta Lake and Apache Spark enables users to:

- Use existing Spark pipelines unchanged.
- Apply ACID transactions and scalable metadata handling without rewriting ETL logic.
- Unify streaming and batch data processing under the same API surface.
- Rely on the full Spark ecosystem (MLlib, GraphX, Structured Streaming) while gaining Delta Lake’s reliability improvements. ^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- [Delta Lake API Reference](/concepts/delta-lake-api-reference.md) — Documentation for Delta‑specific Spark APIs.
- [ACID Transactions](/concepts/delta-acid-transactions.md) — A core reliability feature enabled by the Delta storage layer.
- Data Lake — The underlying storage platform on which Delta Lake runs.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — Spark’s streaming engine, fully compatible with Delta tables.
- Schema Enforcement — A Delta Lake feature that validates data against the table schema at write time.

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
