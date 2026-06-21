---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae38c3f2e3e89ad3b65d73131958620e178421639865fa3ca787451aa77cca1c
  pageDirectory: concepts
  sources:
    - load-data-using-mosaic-streaming-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mosaic-streaming
    - Mosaic Streaming (MDS)
    - streaming
  citations:
    - file: load-data-using-mosaic-streaming-databricks-on-aws.md
title: Mosaic Streaming
description: An open-source data loading library for single-node or distributed training/evaluation of deep learning models, compatible with PyTorch, PyTorch Lightning, Mosaic Composer, and TorchDistributor.
tags:
  - data-loading
  - deep-learning
  - pytorch
  - databricks
timestamp: "2026-06-19T19:14:04.374Z"
---

# Mosaic Streaming

**Mosaic Streaming** is an open-source data loading library that enables single-node or distributed training and evaluation of deep learning models from datasets already loaded as Apache Spark DataFrames. It converts data from Spark to a PyTorch-compatible format, streamlining the transition from data preparation to model training. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Overview

Mosaic Streaming primarily supports Mosaic Composer, but also integrates with native PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), and the [TorchDistributor](/concepts/torchdistributor.md). The library is pre-installed in all versions of Databricks Runtime 15.2 ML and higher. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Key Features

Mosaic Streaming offers several advantages over traditional PyTorch DataLoaders: ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

- **Data type compatibility** – Works with any data type, including images, text, video, and multimodal data.
- **Cloud storage support** – Supports AWS, OCI, GCS, Azure, Databricks UC Volume, and any S3-compatible object store (e.g., Cloudflare R2, Coreweave, Backblaze B2).
- **Performance and correctness** – Maximizes correctness guarantees, performance, flexibility, and ease of use.

## Workflow: Spark to MDS to Training

The recommended workflow for using Mosaic Streaming consists of four steps: ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

1. **Load and preprocess data** using Apache Spark.
2. **Convert to MDS format** by calling `streaming.base.converters.dataframe_to_mds`. This saves the DataFrame to disk (for transient storage) or to a Unity Catalog volume (for persistent storage). The data is stored in the Mosaic Data Shard (MDS) format, with optional compression and hashing. Advanced use cases can apply preprocessing via Spark UDFs.
3. **Load data into memory** with `streaming.StreamingDataset`, a subclass of PyTorch’s `IterableDataset`. It provides elastically deterministic shuffling, enabling fast mid-epoch resumption.
4. **Feed data for training/evaluation/testing** using `streaming.StreamingDataLoader`. This is a version of PyTorch’s `DataLoader` that adds a checkpoint/resumption interface, tracking the number of samples seen by the model per rank.

## Supported Integrations

- Mosaic Composer
- PyTorch (native)
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- [TorchDistributor](/concepts/torchdistributor.md)

## Troubleshooting

### Authentication Error

When loading data from a Unity Catalog volume with `StreamingDataset`, you may encounter the following error: ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

```
ValueError: default auth: cannot configure default credentials, ...
```

To resolve, set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` before initializing `StreamingDataset`. If running distributed training with `TorchDistributor`, these variables must also be set on the worker nodes. A common pattern is to define them inside the training function: ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

```python
db_host = "https://your-databricks-host.databricks.com"
db_token = "YOUR API TOKEN"

def your_training_function():
    import os
    os.environ['DATABRICKS_HOST'] = db_host
    os.environ['DATABRICKS_TOKEN'] = db_token
```

### Python 3.11 Shared Memory Issues

On Databricks Runtime 15.4 LTS for Machine Learning (which uses Python 3.11), `StreamingDataset` can encounter transient shared memory problems. Upgrading to Databricks Runtime 16.4 LTS for Machine Learning (Python 3.12) resolves these issues. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Related Concepts

- [Mosaic Data Shard (MDS) format](/concepts/mds-mosaic-data-shard-format.md)
- [StreamingDataset](/concepts/streamingdataset.md)
- [StreamingDataLoader](/concepts/streamingdataloader.md)
- Apache Spark DataFrames
- Unity Catalog volume
- [TorchDistributor](/concepts/torchdistributor.md)
- Mosaic Composer

## Sources

- load-data-using-mosaic-streaming-databricks-on-aws.md

# Citations

1. [load-data-using-mosaic-streaming-databricks-on-aws.md](/references/load-data-using-mosaic-streaming-databricks-on-aws-4083e8c0.md)
