---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f35bdaae2907a4578d246d2728b880395212a8d8b406712958398acb51f5d240
  pageDirectory: concepts
  sources:
    - load-data-using-mosaic-streaming-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-311-shared-memory-issues-with-streamingdataset
    - P3SMIWS
  citations:
    - file: load-data-using-mosaic-streaming-databricks-on-aws.md
title: Python 3.11 Shared Memory Issues with StreamingDataset
description: Transient issues with StreamingDataset on Python 3.11 shared memory implementation in Databricks Runtime 15.4 LTS ML, resolved by upgrading to Databricks Runtime 16.4 LTS ML with Python 3.12.
tags:
  - troubleshooting
  - python
  - databricks
  - compatibility
timestamp: "2026-06-19T19:14:46.952Z"
---

# Python 3.11 Shared Memory Issues with StreamingDataset

**Python 3.11 Shared Memory Issues with StreamingDataset** refers to transient errors encountered when using Mosaic's [StreamingDataset](/concepts/streamingdataset.md) on Databricks Runtime 15.4 LTS for Machine Learning, caused by bugs in Python 3.11's shared memory implementation. These issues are resolved by upgrading to a runtime that uses Python 3.12 or later.

## Overview

[Mosaic Streaming](/concepts/mosaic-streaming.md) provides `StreamingDataset`, a version of PyTorch's `IterableDataset` that features elastically deterministic shuffling and fast mid-epoch resumption. On Databricks Runtime 15.4 LTS for Machine Learning, which ships with Python 3.11, `StreamingDataset` can encounter transient shared memory failures during data loading operations. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Symptoms and Behavior

The issues are **transient** — they may occur intermittently rather than consistently, making them difficult to reproduce or debug. The errors manifest during dataset construction or data iteration, particularly in distributed training scenarios where multiple worker processes share access to the same streaming dataset. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Root Cause

Python 3.11 contained known defects in its Python Shared Memory (`multiprocessing.shared_memory`) implementation, which underpins the cross-process data sharing mechanisms used by `StreamingDataset`. These defects could cause race conditions, memory corruption, or access violations when multiple processes attempted to map or access shared memory segments concurrently. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Resolution

Upgrade the Databricks Runtime to **Databricks Runtime 16.4 LTS for Machine Learning** or later. This runtime ships with Python 3.12, which includes fixes for the shared memory bugs present in Python 3.11. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

| Runtime Version | Python Version | Status |
|---|---|---|
| Databricks Runtime 15.4 LTS ML | Python 3.11 | Affected — shared memory issues present |
| Databricks Runtime 16.4 LTS ML | Python 3.12 | Fixed — shared memory issues resolved |

## Related Concepts

- [Mosaic Streaming](/concepts/mosaic-streaming.md) — The data loading library that provides `StreamingDataset`
- [StreamingDataset](/concepts/streamingdataset.md) — The dataset class affected by this issue
- [StreamingDataLoader](/concepts/streamingdataloader.md) — Companion loader for training and evaluation workflows
- PyTorch IterableDataset — The base class that `StreamingDataset` extends
- Distributed Training with Mosaic Streaming — Multi-worker training context where the issue manifests

## Sources

- load-data-using-mosaic-streaming-databricks-on-aws.md

# Citations

1. [load-data-using-mosaic-streaming-databricks-on-aws.md](/references/load-data-using-mosaic-streaming-databricks-on-aws-4083e8c0.md)
