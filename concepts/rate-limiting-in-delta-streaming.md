---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6af2e3e90a34b7beb484f7836e9611e1579077eb83269084c100ec685469140f
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limiting-in-delta-streaming
    - RLIDS
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Rate Limiting in Delta Streaming
description: Using maxFilesPerTrigger and maxBytesPerTrigger to control micro-batch input size and manage streaming processing performance
tags:
  - streaming
  - delta-lake
  - performance
timestamp: "2026-06-18T15:15:45.844Z"
---

# Rate Limiting in Delta Streaming

**Rate Limiting in Delta Streaming** refers to the configuration options available in Spark Structured Streaming that control the amount of data processed per micro-batch when reading from Delta Lake tables as a streaming source. These limits help manage memory usage, stabilize latency, and reduce cloud storage costs.

## Overview

By default, Structured Streaming processes as many files as possible in each micro-batch when reading from a [Delta Lake Table](/concepts/delta-lake-table.md). To prevent overwhelming system resources or incurring excessive costs, you can configure rate-limiting options that constrain the volume of data processed per batch. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Rate-Limiting Options

### `maxFilesPerTrigger`

The `maxFilesPerTrigger` option specifies the maximum number of new files to be considered in every micro-batch. The default value is 1000. This option is useful for controlling the granularity of data ingestion and preventing large spikes in processing load. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### `maxBytesPerTrigger`

The `maxBytesPerTrigger` option sets the amount of data that gets processed in each micro-batch. This option acts as a "soft max," meaning that a batch processes approximately this amount of data. It may process more than the limit in cases where the smallest input unit is larger than the specified limit. This option is not set by default. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

### Combined Usage

If you use both `maxFilesPerTrigger` and `maxBytesPerTrigger`, the micro-batch processes data until either the `maxFilesPerTrigger` or `maxBytesPerTrigger` limit is reached, whichever comes first. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Structured Streaming Triggers — Different trigger modes (processingTime, availableNow, realTime) that balance cost and latency
- [Delta Lake Table Streaming Reads and Writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md) — General guidance on using Delta Lake as a streaming source and sink
- Streaming Query Monitoring — Metrics for tracking backlog and processing progress
- Checkpointing in Structured Streaming — Managing streaming state and recovery

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
