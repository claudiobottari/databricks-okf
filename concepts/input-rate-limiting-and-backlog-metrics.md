---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4ce22c2b8a511248692cbc9bfcae35b317dd6534d352df01b565f121f7c6253
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - input-rate-limiting-and-backlog-metrics
    - Backlog Metrics and Input Rate Limiting
    - IRLABM
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Input Rate Limiting and Backlog Metrics
description: Options (maxFilesPerTrigger, maxBytesPerTrigger) and metrics (numBytesOutstanding, numFilesOutstanding) to control and monitor streaming query processing rate from Delta sources.
tags:
  - structured-streaming
  - delta-lake
  - monitoring
  - performance
timestamp: "2026-06-19T18:21:01.952Z"
---

# Input Rate Limiting and Backlog Metrics

**Input Rate Limiting and Backlog Metrics** are features of Spark Structured Streaming when using [Delta Lake](/concepts/delta-lake.md) tables as a streaming source. They help manage the volume of data processed per micro-batch and monitor the size of the unprocessed backlog, enabling more predictable latency, memory usage, and cloud storage costs.

## Backlog Metrics

When a streaming query reads from a [Delta Lake Table](/concepts/delta-lake-table.md), the following metrics are available in the streaming query progress dashboard (under the **Raw Data** tab) to monitor the backlog:

- `numBytesOutstanding`: Number of bytes yet to be processed in the backlog.  
- `numFilesOutstanding`: Number of files yet to be processed in the backlog.  
- `numNewListedFiles`: Number of Delta Lake files listed to calculate the backlog for this batch.  
- `backlogEndOffset`: The [Delta Lake Table](/concepts/delta-lake-table.md) version used to calculate the backlog.

These metrics appear in the `sources` array of the progress JSON, as shown in the example:  
```json
{  "sources": [    {      "description": "DeltaSource[file:/path/to/source]",      "metrics": {        "numBytesOutstanding": "3456",        "numFilesOutstanding": "8"      }    }  ]}
```
^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Input Rate Limiting Options

By default, Structured Streaming processes as many files as possible in each micro-batch. To control the amount of data processed per batch, use the following options on the `readStream`:

- `maxFilesPerTrigger`: The number of new files to be considered in every micro-batch. The default is 1000.  
- `maxBytesPerTrigger`: The approximate amount of data processed per micro-batch. This is a “soft max”; a batch may process more than this limit if the smallest input unit exceeds it. Not set by default.

If both options are specified, the micro-batch stops when either limit is reached. These options help stabilize latency, manage memory usage, and reduce cloud storage costs.  
^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Additional Considerations

When using input rate limiting, be aware of the source table’s transaction log retention (`logRetentionDuration`, default 30 days). If the streaming query falls behind because of rate limiting and the cleanup removes transactions, the query may fail with `DELTA_FILE_NOT_FOUND_DETAILED`. By default, such failures prevent data loss. You can set the option `failOnDataLoss` to `false` to ignore lost data and continue processing, but Databricks does not recommend using `spark.sql.files.ignoreMissingFiles` as a workaround because it can silently produce incorrect results.  
^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Spark Structured Streaming  
- [Delta Lake](/concepts/delta-lake.md)  
- Streaming Query Checkpoints  
- Trigger Modes (processingTime, availableNow, realTime)  
- [Delta Lake Change Data Feed](/concepts/delta-lake-change-data-feed-cdf.md)  

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
