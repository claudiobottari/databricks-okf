---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c23f6f970d573413445df45aea4cb00a9ece5a49315ebe55e15da05a35b2e6cf
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-stream-input-rate-limiting
    - DLSIRL
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Delta Lake Stream Input Rate Limiting
description: Options maxFilesPerTrigger and maxBytesPerTrigger to control how much data each micro-batch processes, helping manage memory, latency, and cloud storage costs
tags:
  - delta-lake
  - streaming
  - performance
  - structured-streaming
timestamp: "2026-06-19T15:00:47.075Z"
---

# Delta Lake Stream Input Rate Limiting

**Delta Lake Stream Input Rate Limiting** refers to the configuration options available in Spark Structured Streaming that control the amount of data processed in each micro-batch when reading from [Delta Lake](/concepts/delta-lake.md) tables as a streaming source. These limits help manage memory usage, stabilize latency, and control cloud storage costs.

## Overview

By default, Structured Streaming processes as many files as possible in each micro-batch when reading from a [Delta Lake Table](/concepts/delta-lake-table.md). This default behavior can lead to unpredictable resource consumption and latency spikes. To address this, Delta Lake provides rate-limiting options that allow you to constrain the volume of data processed per micro-batch. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Configuration Options

### `maxFilesPerTrigger`

The `maxFilesPerTrigger` option specifies the maximum number of new files to be considered in every micro-batch. The default value is 1000. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### `maxBytesPerTrigger`

The `maxBytesPerTrigger` option sets the approximate amount of data that gets processed in each micro-batch. This option sets a "soft max," meaning that a batch processes approximately this amount of data and might process more than the limit in order to make the streaming query move forward in cases when the smallest input unit is larger than this limit. This option is not set by default. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Combined Usage

If you use both `maxFilesPerTrigger` and `maxBytesPerTrigger`, the micro-batch processes data until either the `maxFilesPerTrigger` or `maxBytesPerTrigger` limit is reached, whichever comes first. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Use Cases

Input rate limiting is beneficial in several scenarios:

- **Managing memory usage**: Preventing excessive data from being loaded into memory in a single micro-batch, especially important for resource-constrained clusters. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Stabilizing latency**: Avoiding large, unpredictable batch processing times by capping the amount of work per micro-batch. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Reducing cloud storage costs**: Controlling the volume of data scanned and processed in each batch iteration. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Spark Structured Streaming – The streaming engine that processes Delta Lake tables incrementally.
- [Delta Lake Table Streaming Reads and Writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md) – Comprehensive documentation on streaming with Delta Lake.
- maxFilesPerTrigger – Option for limiting files per micro-batch.
- maxBytesPerTrigger – Option for limiting bytes per micro-batch.
- Stream Processing Triggers – Trigger modes that balance cost and latency in streaming queries.
- Structured Streaming Monitoring – Tools for tracking streaming query progress and metrics.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
