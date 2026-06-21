---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ada8e611133b782e4d4b6cd68d24ec8b91e74d132ea89e1cf48d92838975a826
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-mllib-limitation
    - DCML
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect MLlib Limitation
description: Databricks Connect has limited compatibility with Apache Spark MLlib because MLlib uses RDDs while Databricks Connect only supports the DataFrame API.
tags:
  - databricks
  - spark-mllib
  - limitations
timestamp: "2026-06-19T18:10:13.795Z"
---

# Databricks Connect MLlib Limitation

**Databricks Connect MLlib Limitation** refers to the reduced functionality of [Apache Spark MLlib](/concepts/apache-spark-mllib.md) when used through [Databricks Connect](/concepts/databricks-connect.md). This limitation primarily affects R users via the [sparklyr](/concepts/sparklyr.md) package and stems from architectural differences between the MLlib API and the Databricks Connect execution model. ^[databricks-connect-for-r-databricks-on-aws.md]

## Cause

Spark MLlib was originally built on top of Spark’s Resilient Distributed Datasets (RDDs), whereas Databricks Connect supports only the DataFrame API. Because Databricks Connect translates client-side DataFrame operations into server-side execution, RDD‑based operations—including many MLlib algorithms—cannot be dispatched through the Databricks Connect client. As a result, only a subset of MLlib functionality that has been re‑implemented for DataFrames is available. ^[databricks-connect-for-r-databricks-on-aws.md]

## Workaround

To access the full set of Spark MLlib functions within R, Databricks recommends one of the following alternatives:

- Use Databricks notebooks directly, where MLlib runs without the Databricks Connect layer.
- Use the `db_repl` function from the brickster package, which provides an interactive REPL that bypasses the Databricks Connect client. ^[databricks-connect-for-r-databricks-on-aws.md]

These options allow RDD‑based MLlib stages to execute correctly, since they are not constrained by the DataFrame‑only limitation of Databricks Connect.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client‑side library for remote Spark execution.
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) – The machine learning library affected by this limitation.
- [sparklyr](/concepts/sparklyr.md) – The R interface to Spark that uses Databricks Connect.
- brickster – An R package that provides alternative access to Databricks APIs.
- DataFrame API – The only API supported by Databricks Connect.
- RDD – The lower‑level distributed data structure used by older MLlib implementations.

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
