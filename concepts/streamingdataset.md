---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb30aff4788ddc3822fee3e811f413a47233d831b6af568e7536547db4cd76cc
  pageDirectory: concepts
  sources:
    - load-data-using-mosaic-streaming-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streamingdataset
    - Mosaic StreamingDataset
    - Streaming Datasets
    - Streaming data ingestion
    - streaming reads
  citations:
    - file: load-data-using-mosaic-streaming-databricks-on-aws.md
title: StreamingDataset
description: A PyTorch IterableDataset variant that features elastically deterministic shuffling, enabling fast mid-epoch resumption during distributed training.
tags:
  - pytorch
  - distributed-training
  - data-loading
timestamp: "2026-06-19T19:14:14.909Z"
---

## StreamingDataset

**StreamingDataset** is an open-source data loading utility provided by the **Mosaic Streaming** library. It is a variant of PyTorch’s `IterableDataset` designed for efficient single-node or distributed training and evaluation of deep learning models. Its key innovation is *elastically deterministic shuffling*, which enables fast mid-epoch resumption. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

### Overview

Mosaic Streaming is pre-installed in all versions of Databricks Runtime 15.2 ML and higher. ^[load-data-using-mosaic-streaming-databricks-on-aws.md] The recommended workflow for using StreamingDataset is:

1. **Load and preprocess data** with Apache Spark (as a Spark DataFrame).
2. **Convert the DataFrame to MDS format** using `streaming.base.converters.dataframe_to_mds` and save it to transient or persistent storage (e.g., a Unity Catalog volume).
3. **Load the data with `StreamingDataset`** – this step moves the MDS-format data into memory.
4. **Use `StreamingDataLoader`** – a PyTorch `DataLoader` variant that adds a checkpoint/resumption interface, tracking the number of samples seen by each rank. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

StreamingDataset supports any data type (images, text, video, multimodal) and works with major cloud storage providers (AWS, OCI, GCS, Azure, Databricks UC Volume, and any S3-compatible object store). ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

### Integration with Training Frameworks

StreamingDataset primarily integrates with Mosaic Composer, but also works with native PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), and the [TorchDistributor](/concepts/torchdistributor.md). ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

### Troubleshooting

#### Authentication Error when Loading from Unity Catalog Volume

If you receive a `ValueError: default auth: cannot configure default credentials` when using `StreamingDataset` to load data from a Unity Catalog volume, set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` on the driver and, when using distributed training with `TorchDistributor`, also on the worker nodes. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

```python
db_host = "https://your-databricks-host.databricks.com"
db_token = "YOUR API TOKEN"

def your_training_function():
    import os
    os.environ['DATABRICKS_HOST'] = db_host
    os.environ['DATABRICKS_TOKEN'] = db_token
```

#### Python 3.11 Shared Memory Issues

On Databricks Runtime 15.4 LTS for Machine Learning (Python 3.11), `StreamingDataset` can encounter transient shared memory problems. These are resolved by upgrading to Databricks Runtime 16.4 LTS for Machine Learning (Python 3.12), which includes a fix for the underlying shared memory implementation. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

### Related Concepts

- [Mosaic Streaming](/concepts/mosaic-streaming.md)
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md)
- MDS format
- [StreamingDataLoader](/concepts/streamingdataloader.md)
- [TorchDistributor](/concepts/torchdistributor.md)
- Mosaic Composer
- PyTorch
- Unity Catalog Volume

### Sources

- load-data-using-mosaic-streaming-databricks-on-aws.md

# Citations

1. [load-data-using-mosaic-streaming-databricks-on-aws.md](/references/load-data-using-mosaic-streaming-databricks-on-aws-4083e8c0.md)
