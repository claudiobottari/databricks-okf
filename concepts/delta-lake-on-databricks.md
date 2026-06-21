---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f5611c7648dd6ee214a16be4c364348d57c2f2a0e58e3e91f6a72c28695acf2
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-on-databricks
    - DLOD
    - What is Delta Lake in Databricks?
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Delta Lake on Databricks
description: Databricks' integration and documentation of Delta Lake, including tutorials for creating and managing Delta Lake tables within the Databricks environment on AWS.
timestamp: "2026-06-19T10:00:02.456Z"
---

# Delta Lake on Databricks

**Delta Lake** is an open-source storage layer that brings reliability to data lakes. On Databricks, Delta Lake is a core component, providing ACID transactions, scalable metadata handling, and unified streaming and batch data processing. It runs on top of your existing data lake and is fully compatible with Apache Spark APIs.^[delta-lake-api-reference-databricks-on-aws.md]

## Key Features

- **ACID transactions** – Ensures data integrity under concurrent reads and writes.
- **Scalable metadata handling** – Capable of managing metadata for large-scale datasets (e.g., billions of partitions and files).
- **Unified streaming and batch processing** – Allows batch and streaming workloads to use the same tables with consistent semantics.
- **Compatibility with Apache Spark APIs** – Works directly with standard Spark DataFrames and SQL, requiring minimal code changes.
- **Open source** – The Delta Lake project is hosted on GitHub and maintained by the Delta Lake community.^[delta-lake-api-reference-databricks-on-aws.md]

## Using Delta Lake on Databricks

Databricks provides full support for Delta Lake across all cloud providers (AWS, Azure, GCP). To learn how to use the Delta Lake APIs on Databricks, see:

- [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta/) – Overview and key concepts.
- [Tutorial: Create and manage Delta Lake tables](https://docs.databricks.com/aws/en/delta/tutorial) – Step-by-step guidance for working with Delta tables.

API references for Scala, Java, and Python are available on the [Delta Lake website](https://docs.delta.io/latest/delta-apidoc.html#delta-spark).^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- Apache Spark
- Databricks
- [ACID transactions](/concepts/delta-acid-transactions.md)
- [Data Lakehouse](/concepts/avoiding-data-silos-in-lakehouse.md)
- [Streaming on Databricks](/concepts/streaming-tables-in-databricks.md)
- [Delta Sharing](/concepts/delta-sharing.md)

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
