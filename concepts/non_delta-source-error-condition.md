---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e29c97336d333ef93977000e928bf48913b64bd31736382336ab66225ed05611
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_delta-source-error-condition
    - NSEC
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: NON_DELTA source error condition
description: A specific sub-error of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE raised when the source table format is not Delta (e.g., Parquet, CSV, JSON)
tags:
  - databricks
  - error-messages
  - delta-lake
timestamp: "2026-06-19T18:22:31.713Z"
---

# NON_DELTA Source Error Condition

The **NON_DELTA source error condition** is a specific error sub-type under the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error class in Databricks. This error condition occurs when attempting to perform a CLONE operation with history on a source table that is not in [Delta Lake](/concepts/delta-lake.md) format.

## Error Message

The error displays the following message when triggered:

```
Source table of `<format>` format is not supported.
```

Where `<format>` is replaced with the actual table format being used as the source.

## Error Context

This error is returned with SQLSTATE code `0AKDC` (Feature Not Supported class). It specifically applies to the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error class, which has two sub-conditions: `NON_DELTA` and `TIME_TRAVELLED_BY_TIMESTAMP`. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

The `NON_DELTA` condition indicates that the source table format is not Delta Lake. The `CLONE` operation with history requires a [Delta Lake](/concepts/delta-lake.md) source table

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
