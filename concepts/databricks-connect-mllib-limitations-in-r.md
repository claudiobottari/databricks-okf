---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 54b11254f4c1b45e995a085fe8c566d14e6f2c2fa84bc1fbadb5ec1e5493b72d
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-mllib-limitations-in-r
    - DCMLIR
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect MLlib limitations in R
description: Spark MLlib functions that rely on RDDs are incompatible with Databricks Connect, which only supports the DataFrame API, limiting sparklyr's MLlib capabilities.
tags:
  - databricks
  - mllib
  - limitation
timestamp: "2026-06-18T11:34:53.840Z"
---

# Databricks Connect MLlib limitations in R

**Databricks Connect for R** enables you to connect RStudio Desktop and other R environments to Databricks clusters using `sparklyr`, but it has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md). This limitation stems from architectural differences between the underlying data processing frameworks used by MLlib and Databricks Connect. ^[databricks-connect-for-r-databricks-on-aws.md]

## Technical Limitation

[Apache Spark MLlib](/concepts/apache-spark-mllib.md) operates on **RDDs** (Resilient Distributed Datasets), whereas Databricks Connect supports only the **DataFrame API**. Since Databricks Connect for R communicates with the cluster via Spark Connect, which relies on the DataFrame API, many MLlib functions that depend on RDDs cannot be executed remotely through Databricks Connect. ^[databricks-connect-for-r-databricks-on-aws.md]

This limitation applies to the `sparklyr` integration with Databricks Connect for Databricks Runtime 13.0 and above. The integration is neither provided nor directly supported by Databricks. ^[databricks-connect-for-r-databricks-on-aws.md]

## Workaround

To use the full set of `sparklyr`'s Spark MLlib functions, Databricks recommends one of the following approaches: ^[databricks-connect-for-r-databricks-on-aws.md]

- **Databricks notebooks** – Run your MLlib code directly in a notebook attached to the cluster.
- **`db_repl` function** – Use the `db_repl` function from the [brickster package](https://databrickslabs.github.io/brickster/), which provides an R REPL on a Databricks cluster and supports the full MLlib API.

These alternatives avoid the Databricks Connect layer and execute MLlib operations natively on the cluster. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall framework for connecting remote applications to Databricks clusters
- [Spark MLlib](/concepts/apache-spark-mllib.md) – Apache Spark's machine learning library
- Spark DataFrame API – The API that Databricks Connect supports
- [sparklyr](/concepts/sparklyr.md) – The R interface to Apache Spark
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Python counterpart of Databricks Connect
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – Scala counterpart of Databricks Connect

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
