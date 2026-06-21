---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7db062cee98ca26c84c6cbadd3382bea902bd4339e0efd2c9e298240ffb34ff7
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - query-timeout-3600-seconds
    - QT(S
    - Query Timeout
  citations:
    - file: limitations-with-databricks-connect-for-scala-databricks-on-aws.md
title: Query Timeout (3600 seconds)
description: Long queries exceeding 3600 seconds are not supported in Databricks Connect for Databricks Runtime 13.3 LTS and above.
tags:
  - databricks-connect
  - limitations
  - scala
timestamp: "2026-06-19T19:12:26.439Z"
---

# Query Timeout (3600 seconds)

**Query Timeout (3600 seconds)** is a limitation in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) that restricts the maximum execution time for queries submitted through the client. Queries that exceed this 3600-second (1 hour) threshold will fail.

## Overview

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), any query that runs longer than 3600 seconds is not supported and will result in an error. This timeout applies to the query execution duration, not to data transfer or other operations. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Affected Versions

This limitation applies to Databricks Connect for Databricks Runtime 13.3 LTS and above. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Workarounds

For queries that require longer execution times, consider the following approaches:

- Break long-running queries into smaller, incremental operations that complete within the 3600-second limit.
- Use alternative execution methods that do not go through Databricks Connect, such as running queries directly on the Databricks cluster using notebooks or jobs.
- Optimize query performance to reduce execution time below the threshold.

## Related Limitations

The 3600-second query timeout is one of several limitations in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). Other notable limitations include:

- [Streaming foreachBatch](/concepts/streaming-upserts-with-foreachbatch-and-merge.md) is not available on Databricks Runtime 13.3 LTS and below.
- Creating DataFrames with an unresolved logical plan larger than 128 MB is not supported.
- Scalar UDFs are not supported on compute resources using dedicated access mode.
- Databricks Utilities functions such as `credentials`, `library`, `notebook workflow`, and `widgets` are not available.
- Spark Context and RDDs are not supported.
- Distributed ML training is not available.

## Sources

- limitations-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-scala-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-scala-databricks-on-aws-8e97ac24.md)
