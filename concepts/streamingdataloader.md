---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70497fc3fec2a59647c04041a4e7df18e45f4db8515f3c23de281625d7550375
  pageDirectory: concepts
  sources:
    - load-data-using-mosaic-streaming-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streamingdataloader
  citations:
    - file: load-data-using-mosaic-streaming-databricks-on-aws.md
title: StreamingDataLoader
description: A PyTorch DataLoader variant that provides an additional checkpoint/resumption interface by tracking the number of samples seen by the model per rank.
tags:
  - pytorch
  - distributed-training
  - checkpointing
timestamp: "2026-06-19T19:14:20.356Z"
---

# StreamingDataLoader

**StreamingDataLoader** is a component of the [Mosaic Streaming](/concepts/mosaic-streaming.md) open-source data loading library. It is a version of PyTorch's `DataLoader` that provides an additional checkpoint and resumption interface, tracking the number of samples seen by the model for the current rank. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Overview

Mosaic Streaming is designed for single-node or distributed training and evaluation of deep learning models. It is pre-installed on Databricks Runtime 15.2 ML and higher. The recommended workflow first converts data from Apache Spark DataFrames into the Mosaic Data Shard (MDS) format using `streaming.base.converters.dataframe_to_mds`. The data is then loaded into memory via `streaming.StreamingDataset`, and finally `streaming.StreamingDataLoader` is used to load the data for training, evaluation, or testing. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Checkpoint and Resumption

Unlike the standard PyTorch `DataLoader`, `StreamingDataLoader` explicitly tracks the number of samples consumed by the model on each rank. This tracking enables a reliable checkpoint and resumption mechanism, allowing training to resume precisely from where it left off, even mid-epoch. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Usage Example

After preparing a `StreamingDataset`, you can wrap it with a `StreamingDataLoader`:

```python
from streaming import StreamingDataset, StreamingDataLoader

dataset = StreamingDataset(local="/path/to/mds", shuffle=True)
dataloader = StreamingDataLoader(dataset, batch_size=32)
```

The resulting `dataloader` can be used like a standard PyTorch `DataLoader` but supports the additional checkpoint interface.

## Related Concepts

- [Mosaic Streaming](/concepts/mosaic-streaming.md) – The parent library providing data loading utilities.
- [StreamingDataset](/concepts/streamingdataset.md) – The elastic, deterministic dataset used with Mosaic Streaming.
- PyTorch DataLoader – The base class that `StreamingDataLoader` extends.
- [Mosaic Data Shard (MDS)](/concepts/mds-mosaic-data-shard-format.md) – The file format for storing converted data.
- [TorchDistributor](/concepts/torchdistributor.md) – A Databricks tool for distributed PyTorch training.

## Sources

- load-data-using-mosaic-streaming-databricks-on-aws.md

# Citations

1. [load-data-using-mosaic-streaming-databricks-on-aws.md](/references/load-data-using-mosaic-streaming-databricks-on-aws-4083e8c0.md)
