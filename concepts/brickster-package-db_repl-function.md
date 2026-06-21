---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb9a3542b13eec0dd3d8da1336416a599139bd9b1dfdf028ca742e644955c172
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - brickster-package-db_repl-function
    - BPDF
  citations:
    - file: databricks-connect-for-r-datatbricks-on-aws.md
    - file: databricks-connect-for-r-databricks-on-aws.md
title: brickster package db_repl function
description: Alternative approach using the brickster package's db_repl function to use all sparklyr's Spark MLlib functions when Databricks Connect's DataFrame-API-only limitation is a blocker.
tags:
  - databricks
  - r
  - mllib
  - package
timestamp: "2026-06-18T11:35:02.603Z"
---

# brickster package `db_repl` function

The **`brickster` package** is a community-maintained R package that provides an alternative interface for interacting with Databricks clusters. Its `db_repl` function serves as a [Databricks Connect](/concepts/databricks-connect.md)–compatible method for running code on remote clusters, particularly useful when users need capabilities beyond what the standard `sparklyr`–Databricks Connect integration offers. ^[databricks-connect-for-r-datatbricks-on-aws.md]

## Purpose

The standard `sparklyr` integration with Databricks Connect has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md), because Spark MLlib uses RDDs while Databricks Connect only supports the DataFrame API. To use **all** of `sparklyr`'s Spark MLlib functions — including those that rely on RDD operations — users can turn to the `db_repl` function from the `brickster` package instead. ^[databricks-connect-for-r-databricks-on-aws.md]

## Key Characteristics

- `db_repl` is part of the **`brickster`** package, maintained by Databricks Labs.
- It is designed as a fallback for scenarios where Databricks Connect's DataFrame-only API cannot cover certain MLlib operations.
- The function is documented on the [brickster package website](https://databrickslabs.github.io/brickster/), which details how to install and use it.
- Users should note that the `brickster` package is **neither provided by Databricks nor directly supported** by Databricks; questions and issue reports should go to the Posit Community or the `sparklyr` GitHub repository respectively. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — the primary integration approach for R users
- [Spark MLlib](/concepts/apache-spark-mllib.md) — the machine learning library whose RDD-dependent functions benefit from `db_repl`
- brickster package — the community package that hosts `db_repl`

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. databricks-connect-for-r-datatbricks-on-aws.md
2. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
