---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 11b86676be89dbea631b79b735e2232615129692619628861179dc74d4e3ad77
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-apis
    - DLA
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Delta Lake APIs
description: Programmatic interfaces for Scala, Java, and Python that allow developers to interact with Delta Lake tables using Apache Spark APIs.
timestamp: "2026-06-19T09:59:41.130Z"
---

# Delta Lake APIs

**Delta Lake APIs** provide programmatic interfaces for interacting with [Delta Lake](https://delta.io/), an open-source storage layer that brings reliability, performance, and governance to data lakes. The APIs enable users to perform operations such as reading, writing, and managing Delta tables using standard Spark programming languages.

## Overview

Delta Lake is an open-source storage layer that adds reliability to data lakes. It provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. Delta Lake runs on top of an existing data lake and is fully compatible with Apache Spark APIs. ^[delta-lake-api-reference-databricks-on-aws.md]

The Delta Lake APIs allow developers to interact with Delta tables using Spark's DataFrame and SQL APIs. These APIs are available for Scala, Java, and Python through the official Delta Lake library. ^[delta-lake-api-reference-databricks-on-aws.md]

## API Reference Links

The full API reference for Delta Lake (Scala, Java, and Python) is hosted on the Delta Lake documentation website at [docs.delta.io](https://docs.delta.io/latest/delta-apidoc.html#delta-spark). ^[delta-lake-api-reference-databricks-on-aws.md]

For detailed guidance on using Delta Lake APIs within Databricks, refer to the following resources in the Databricks documentation:

- [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta/)
- [Tutorial: Create and manage Delta Lake tables](https://docs.databricks.com/aws/en/delta/tutorial)

Also see the [Delta Lake API documentation](https://docs.databricks.com/aws/en/delta/#delta-api) in the Databricks documentation. ^[delta-lake-api-reference-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying open-source storage layer
- [ACID transactions](/concepts/delta-acid-transactions.md) – Core reliability feature provided by Delta Lake
- Apache Spark – The primary computation engine for Delta Lake APIs
- Databricks – The unified analytics platform where Delta Lake APIs are commonly used
- [Streaming and batch unification](/concepts/delta-lake-streaming-and-batch-unification.md) – Delta Lake's ability to process both streaming and batch data with a single interface
- [Data lake](/concepts/delta-lake.md) – The foundational storage architecture that Delta Lake enhances

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
