---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ef0ace0480b07ad23870acc50b2d6bc1a7d9e288d67ccc5d40490fa84913271
  pageDirectory: concepts
  sources:
    - multi-gpu-workload-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ucvolumedataset-and-ucvolumewriter
    - UCVolumeWriter and UCVolumeDataset
    - UAU
    - volume|volumes
  citations:
    - file: multi-gpu-workload-databricks-on-aws.md
title: UCVolumeDataset and UCVolumeWriter
description: Databricks utilities for streaming file-based data from Unity Catalog volumes and checkpointing distributed training across ranks.
tags:
  - databricks
  - data-loading
  - checkpointing
  - unity-catalog
timestamp: "2026-06-19T19:48:17.814Z"
---

# UCVolumeDataset and UCVolumeWriter

**UCVolumeDataset** and **UCVolumeWriter** are components of the `serverless_gpu.data` module in Databricks designed for efficient data loading and checkpointing to and from [Unity Catalog](/concepts/unity-catalog.md) volumes in distributed training workflows. They are particularly useful when working with the serverless GPU `@distributed` API.

## Overview

When training models on multiple GPUs using the [serverless_gpu](/concepts/serverless-gpu-compute.md) library, data loading and model checkpointing present unique challenges. Datasets may be too large to serialize via pickle, and writing checkpoints from distributed processes requires coordination to avoid race conditions. UCVolumeDataset and UCVolumeWriter address these issues by providing streaming, partitioning, and caching capabilities integrated with Unity Catalog volumes. ^[multi-gpu-workload-databricks-on-aws.md]

## UCVolumeDataset

`UCVolumeDataset` is a dataset class for loading file-based data stored in Unity Catalog volumes. It is designed to be used inside the `@distributed` decorator function, making it suitable for distributed training where the dataset size may exceed the maximum size allowed by pickle serialization.

### Key Features

- **Streaming with local caching**: Files are streamed from the volume and cached locally for performance.
- **Automatic partitioning**: Data is automatically partitioned across ranks and workers, ensuring each GPU processes a distinct subset of the data without manual sharding code.
- **Pickle-safe**: Because data loading happens inside the decorated function, the dataset never needs to be pickled and distributed—only the loading logic is serialized.

### Usage

```python
from serverless_gpu.data import UCVolumeDataset
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def run_train():
    dataset = UCVolumeDataset(volume_path="/Volumes/my_catalog/my_schema/my_volume/data")
    # dataset is automatically partitioned across GPUs
    ...
```

^[multi-gpu-workload-databricks-on-aws.md]

## UCVolumeWriter

`UCVolumeWriter` is a utility for writing model checkpoints and other outputs to Unity Catalog volumes during distributed training. It complements UCVolumeDataset by providing the write path for saving state from distributed processes.

### Key Features

- **Distributed-safe checkpointing**: Handles concurrent writes from multiple GPUs to a unified volume path.
- **Compatible with UCVolumeReader**: Checkpoints written with UCVolumeWriter can be read back using `UCVolumeReader` for model resumption or evaluation.

### Usage

```python
from serverless_gpu.data import UCVolumeWriter

# Inside a @distributed function
UCVolumeWriter.save_checkpoint(
    checkpoint_dir="/Volumes/my_catalog/my_schema/my_volume/checkpoints",
    epoch=epoch,
    model_state_dict=model.state_dict(),
    optimizer_state_dict=optimizer.state_dict()
)
```

^[multi-gpu-workload-databricks-on-aws.md]

## Relationship with the `@distributed` Decorator

UCVolumeDataset and UCVolumeWriter are intended to be used inside functions decorated with `@distributed`. This is important because:

1. **Dataset size**: Placing data loading *outside* the `@distributed` function may cause pickle errors if the dataset exceeds serialization limits. Moving it inside circumvents this issue entirely. ^[multi-gpu-workload-databricks-on-aws.md]

2. **Automatic partitioning**: The `@distributed` infrastructure provides rank and worker context that UCVolumeDataset uses to partition data. When called from a distributed function, each process automatically receives a unique shard of the data.

3. **Checkpoint coordination**: UCVolumeWriter operates in the context of distributed processes, ensuring that checkpoints are written without conflicts.

## Related Concepts

- Unity Catalog volumes – The storage layer for datasets and checkpoints
- [serverless_gpu API](/concepts/serverless-gpu-api.md) – The distributed compute framework these utilities belong to
- Model checkpointing on AI Runtime – Broader context for saving and resuming training
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – The typical hardware setup for distributed training workloads
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – A common parallelism strategy used with these data utilities

## Sources

- multi-gpu-workload-databricks-on-aws.md

# Citations

1. [multi-gpu-workload-databricks-on-aws.md](/references/multi-gpu-workload-databricks-on-aws-c6af01f5.md)
