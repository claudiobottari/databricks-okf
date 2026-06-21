---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92e92f6fcf699d00bf1e24dd4b458bf2891637cc0c0fe0fe6645af6dd4c1d6ad
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-incompatibility-with-open-source-apache-spark
    - DCIWOSAS
  citations:
    - file: troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect incompatibility with open source Apache Spark
description: Databricks Connect is built against Databricks Runtime and cannot connect to open source Apache Spark servers due to dependency differences such as json4s library versions.
tags:
  - databricks
  - apache-spark
  - compatibility
timestamp: "2026-06-19T23:14:52.210Z"
---

# [Databricks Connect](/concepts/databricks-connect.md) Incompatibility with Open Source Apache Spark

**Databricks Connect Incompatibility with Open Source Apache Spark** refers to a documented limitation: [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) (and by extension for Python) is built against Databricks Runtime and is not compatible with an open-source Apache Spark server, such as a locally running [Spark Connect](/concepts/spark-connect.md) instance. Attempting to use [Databricks Connect](/concepts/databricks-connect.md) against an open-source Spark server yields errors including class‑not‑found exceptions, API behavior mismatches, or serialization failures. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Issue

When a user configures [Databricks Connect](/concepts/databricks-connect.md) to connect to an open-source Apache Spark server (for example, an Apache Spark 3.5.x [Spark Connect](/concepts/spark-connect.md) server reachable at `sc://localhost`), the connection fails with errors that may read:

- `class not found`
- `API behavior mismatches`
- `serialization failures`

^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Cause

[Databricks Connect](/concepts/databricks-connect.md) is compiled and tested against Databricks Runtime, which ships with its own set of dependencies that differ from those in open-source Apache Spark. In particular, [Databricks Connect](/concepts/databricks-connect.md) versions 15.4 and 16.4 are incompatible with Apache Spark 3.5.x because they use a different version of the `json4s` library. This dependency mismatch is the root cause of the errors observed. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Solution

The only supported compute targets for [Databricks Connect](/concepts/databricks-connect.md) are Databricks clusters or [serverless compute](/concepts/serverless-gpu-compute.md). Users must not point [Databricks Connect](/concepts/databricks-connect.md) at an open-source Apache Spark server. To resolve the issue, configure [Databricks Connect](/concepts/databricks-connect.md) to use a Databricks cluster or serverless compute endpoint instead of a local or third‑party Spark server. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that enables IDEs, notebooks, and applications to run Spark code on Databricks clusters.
- Databricks Runtime – The proprietary runtime environment that includes Spark and many additional optimizations and libraries.
- [Spark Connect](/concepts/spark-connect.md) – The protocol used for remote Spark execution; [Databricks Connect](/concepts/databricks-connect.md) implements its own variant.
- json4s library – The specific dependency that causes incompatibility between [Databricks Connect](/concepts/databricks-connect.md) 15.4/16.4 and Apache Spark 3.5.x.
- [Serverless compute](/concepts/serverless-gpu-compute.md) – A Databricks compute option supported as a target for [Databricks Connect](/concepts/databricks-connect.md).

## Sources

- troubleshooting-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-scala-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-scala-databricks-on-aws-fde9e272.md)
