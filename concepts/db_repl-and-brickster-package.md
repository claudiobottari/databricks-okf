---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cad834ae246dbd5d8b7fada222a7bc46782c299159f5c1785e26995ea4ce17b6
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - db_repl-and-brickster-package
    - brickster Package and db_repl
    - DABP
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: db_repl and brickster Package
description: The brickster R package provides a db_repl function as an alternative to sparklyr for using full Spark MLlib capabilities within Databricks.
tags:
  - r
  - databricks
  - mllib
timestamp: "2026-06-19T18:10:23.034Z"
---

# db_repl and brickster Package

The **`db_repl`** function and the **`brickster`** package provide an alternative way to use [Spark MLlib](/concepts/apache-spark-mllib.md) functions from R on Databricks. They are particularly relevant when [Databricks Connect for R](/concepts/databricks-connect-for-r.md) cannot be used.

## Overview

[Databricks Connect for R](/concepts/databricks-connect-for-r.md) has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md) because MLlib uses RDDs (Resilient Distributed Datasets), while Databricks Connect only supports the DataFrame API. To use all of `sparklyr`'s Spark MLlib functions, you can use Databricks notebooks or the `db_repl` function of the `brickster` package. ^[databricks-connect-for-r-databricks-on-aws.md]

## brickster Package

The `brickster` package is a Databricks Labs package available at [https://databrickslabs.github.io/brickster/](https://databrickslabs.github.io/brickster/). It provides the `db_repl` function, which allows R users to run interactive Spark MLlib code on Databricks clusters. This approach bypasses the limitations of Databricks Connect for R when working with MLlib's RDD-based operations.

## db_repl Function

The `db_repl` function, part of the `brickster` package, enables R users to execute `sparklyr` MLlib operations on Databricks clusters. It is a recommended alternative to Databricks Connect for R when full MLlib functionality is required. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – The primary method for connecting R IDEs to Databricks, with limited MLlib support.
- [sparklyr](/concepts/sparklyr.md) – The R interface to Apache Spark.
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) – Spark's machine learning library, which relies on RDDs.
- Databricks notebooks – The native execution environment for R on Databricks.

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
