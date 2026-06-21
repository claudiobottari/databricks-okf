---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ac7db23eee05ab376cbe93ecb5cf181aaf1287e739a4120078eb7804c0bccff
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apache-spark-server-incompatibility-with-databricks-connect
    - ASSIWDC
  citations:
    - file: troubleshooting-databricks-connect-for-python-databricks-on-aws.md
title: Apache Spark Server Incompatibility with Databricks Connect
description: Databricks Connect is built against Databricks Runtime and is incompatible with open-source Apache Spark servers due to differing dependencies such as the json4s library version, causing class-not-found, API mismatch, or serialization errors.
tags:
  - databricks-connect
  - apache-spark
  - compatibility
  - troubleshooting
timestamp: "2026-06-19T23:14:35.790Z"
---

## Apache Spark Server Incompatibility with [Databricks Connect](/concepts/databricks-connect.md)

[Databricks Connect](/concepts/databricks-connect.md) is built against Databricks Runtime, which has different dependencies than open-source Apache Spark. Attempting to connect to an open-source Apache Spark server (for example, a locally running Spark 3.5.x [Spark Connect](/concepts/spark-connect.md) server) results in errors such as class not found, API behavior mismatches, or serialization failures. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

### Cause

The incompatibility is rooted in dependency differences. Databricks Runtime includes libraries and versions that diverge from those in open-source Apache Spark. In particular, for [Databricks Connect](/concepts/databricks-connect.md) 15.4 and 16.4, the conflict stems from a different version of the `json4s` library used by those releases compared with the `json4s` library in Apache Spark 3.5.x. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

### Manifestations

When attempting to connect to an open-source Spark server, users may encounter:

- Class not found errors
- API behavior mismatches
- Serialization failures

These errors can appear as `StatusCode.UNAVAILABLE`, `StatusCode.UNKNOWN`, `DNS resolution failed`, or `Received http2 header with status: 500` messages. However, the same error messages can also indicate connectivity problems unrelated to server incompatibility. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

### Affected Versions

The documented example of incompatibility specifies [Databricks Connect](/concepts/databricks-connect.md) 15.4 and 16.4 against Apache Spark 3.5.x. This illustrates a broader principle: [Databricks Connect](/concepts/databricks-connect.md) is designed for Databricks Runtime and is not intended to work with arbitrary open-source Spark servers. Users must ensure the cluster version is compatible with their [Databricks Connect](/concepts/databricks-connect.md) version. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

### Recommended Solution

Instead of connecting to an open-source Apache Spark server, use a Databricks cluster or [serverless compute](/concepts/serverless-gpu-compute.md). Both are supported targets for [Databricks Connect](/concepts/databricks-connect.md) and avoid dependency mismatches. See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) for details. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – General overview of the tool
- Databricks Runtime – The execution environment [Databricks Connect](/concepts/databricks-connect.md) expects
- Serverless Compute – A supported compute target for [Databricks Connect](/concepts/databricks-connect.md)
- [PySpark and Databricks Connect conflicts](/concepts/pyspark-and-databricks-connect-conflict.md) – Another common installation issue
- json4s library – The specific dependency that causes the documented version mismatch

### Sources

- troubleshooting-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-python-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-python-databricks-on-aws-bb4d5efd.md)
