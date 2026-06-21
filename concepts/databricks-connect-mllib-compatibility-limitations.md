---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94e6f2aca50dad2a063067eed55df94d33aef7e202f4c9452bdbcaabc4b5d6fd
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-mllib-compatibility-limitations
    - DCMCL
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect MLlib Compatibility Limitations
description: A limitation where Databricks Connect has limited compatibility with Apache Spark MLlib because MLlib uses RDDs while Databricks Connect only supports the DataFrame API.
tags:
  - mllib
  - limitations
  - spark
timestamp: "2026-06-18T15:04:23.746Z"
---

# Databricks Connect MLlib Compatibility Limitations

**Databricks Connect MLlib Compatibility Limitations** refers to the known restrictions when using [Apache Spark MLlib](/concepts/apache-spark-mllib.md) functions through Databricks Connect, which primarily supports the DataFrame API rather than RDD-based operations.

## Overview

Databricks Connect has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md). This limitation exists because Spark MLlib uses RDDs (Resilient Distributed Datasets), while Databricks Connect only supports the DataFrame API.^[databricks-connect-for-r-databricks-on-aws.md]

## Impact on sparklyr

For R users working with Databricks Connect through `sparklyr`, the limited MLlib compatibility means that not all of sparklyr's Spark MLlib functions are available. This restriction applies to Databricks Runtime 13.0 and above.^[databricks-connect-for-r-databricks-on-aws.md]

## Workarounds

To use all of sparklyr's Spark MLlib functions, users have two alternative options:^[databricks-connect-for-r-databricks-on-aws.md]

- **Databricks notebooks**: Run MLlib operations directly in Databricks notebooks, which have full support for RDD-based operations.
- **`db_repl` function**: Use the `db_repl` function from the brickster package, which provides an alternative connection method that supports the full range of Spark MLlib functionality.

## Related Concepts

- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — The main R integration for Databricks Connect
- [Databricks Connect](/concepts/databricks-connect.md) — The overall remote connection framework
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — The machine learning library with limited compatibility
- Spark DataFrame API — The supported API for Databricks Connect operations
- brickster package — Alternative package providing full MLlib support

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
