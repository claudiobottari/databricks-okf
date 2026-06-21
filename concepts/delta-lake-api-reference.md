---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ec660dc3d97087160e0b09d1d6edc0513075413ded812c90571ccc04db1aaea
  pageDirectory: concepts
  sources:
    - delta-lake-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-api-reference
    - DLAR
    - Delta Lake SQL Reference
  citations:
    - file: delta-lake-api-reference-databricks-on-aws.md
title: Delta Lake API Reference
description: The official API documentation for Delta Lake, providing Scala, Java, and Python programming interfaces for interacting with Delta Lake tables and operations.
tags:
  - api
  - documentation
  - scala
  - java
  - python
timestamp: "2026-06-19T18:20:09.358Z"
---

# Delta Lake API Reference

**Delta Lake** is an open source storage layer that brings reliability to data lakes by providing ACID transactions, scalable metadata handling, and unified streaming and batch data processing. Delta Lake runs on top of existing data lakes and is fully compatible with Apache Spark APIs. ^[delta-lake-api-reference-databricks-on-aws.md]

## Official API Documentation

The Delta Lake project provides official API references for three programming languages, hosted on the [Delta Lake website](https://delta.io/): ^[delta-lake-api-reference-databricks-on-aws.md]

- **Scala API** — [https://docs.delta.io/latest/delta-apidoc.html#delta-spark](https://docs.delta.io/latest/delta-apidoc.html#delta-spark)
- **Java API** — [https://docs.delta.io/latest/delta-apidoc.html#delta-spark](https://docs.delta.io/latest/delta-apidoc.html#delta-spark)
- **Python API** — [https://docs.delta.io/latest/delta-apidoc.html#delta-spark](https://docs.delta.io/latest/delta-apidoc.html#delta-spark)

These references cover core Delta Lake operations, including reading, writing, and managing Delta tables. The source code is available on [GitHub](https://github.com/delta-io/delta). ^[delta-lake-api-reference-databricks-on-aws.md]

## Using Delta Lake APIs on Databricks

For guidance on using Delta Lake APIs specifically within the Databricks environment, see the following resources: ^[delta-lake-api-reference-databricks-on-aws.md]

- [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta/)
- [Tutorial: Create and manage Delta Lake tables](https://docs.databricks.com/aws/en/delta/tutorial)
- [Delta Lake API documentation](https://docs.databricks.com/aws/en/delta/#delta-api) within the Databricks documentation

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — Overview and features of the storage layer
- Apache Spark — The distributed processing engine Delta Lake integrates with
- [ACID Transactions](/concepts/delta-acid-transactions.md) — Transactional guarantees provided by Delta Lake
- Databricks — The platform providing managed Delta Lake capabilities
- Data Lakes — The storage architecture Delta Lake operates on top of

## Sources

- delta-lake-api-reference-databricks-on-aws.md

# Citations

1. [delta-lake-api-reference-databricks-on-aws.md](/references/delta-lake-api-reference-databricks-on-aws-4e26d809.md)
