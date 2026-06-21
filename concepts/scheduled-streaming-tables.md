---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 090ba285a88b995377657f549d688ccdfd64cc2e98349d23347d0cc7bea4884c
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scheduled-streaming-tables
    - SST
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Scheduled Streaming Tables
description: Streaming tables configured to run on a schedule, which are not supported for deep clone operations in Databricks
tags:
  - databricks
  - streaming
  - scheduling
timestamp: "2026-06-18T15:18:50.210Z"
---

# Scheduled Streaming Tables

Scheduled Streaming Tables are a type of Streaming Table that runs on a user-defined schedule to automate data ingestion and transformation. They are refreshed at regular intervals (e.g., every 10 minutes) rather than continuously, allowing cost-effective batch-oriented streaming without manual trigger.

## Deep Clone Limitation

Scheduled streaming tables **cannot** be used as the source of a `DEEP CLONE` operation. Attempting to deep clone a scheduled streaming table raises the error:

```
DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR
SCHEDULED_TABLE_NOT_SUPPORTED
```

This is a known limitation in Databricks. Only streaming tables using the **default publishing mode** (i.e., continuous, non-scheduled) are eligible for deep clone. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Restrictions

Deep clone of a streaming table also has the following constraints, which apply to all streaming tables (scheduled or not):

- Specifying a `LOCATION` is not supported; the cloned table uses managed storage. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]
- The `WITH HISTORY` clause is required when performing the deep clone. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]
- Time travel is not supported for streaming table deep clone. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Use Cases

Scheduled streaming tables are commonly used for:

- Cost-efficient periodic ingestion where sub-minute latency is not required.
- Reducing compute costs compared to continuous streaming.
- Aligning data refreshes with downstream batch pipelines.

## Related Concepts

- Streaming Tables
- [Deep Clone](/concepts/deep-clone.md)
- Scheduled Queries
- Delta Live Tables

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
