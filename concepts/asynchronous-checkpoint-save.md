---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f40aded18f799699b295a044376e95031773d6cb50e9a1195a6414a2761f2f9a
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - asynchronous-checkpoint-save
    - ACS
    - Synchronous Checkpoint Save
    - Checkpoints
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Asynchronous Checkpoint Save
description: AI Runtime supports dcp.async_save with a UCVolumeWriter to upload checkpoints in the background while training continues, requiring a CPU backend on the process group.
tags:
  - checkpointing
  - async
  - performance
timestamp: "2026-06-19T18:45:45.551Z"
---

# Asynchronous Checkpoint Save

**Asynchronous Checkpoint Save** is a technique for saving model training state that allows computation to continue while checkpoint data is being written to persistent storage, reducing training throughput loss from I/O operations. This contrasts with Synchronous Checkpoint Save, where training must pause until the save completes.

## Overview

During large-scale [Distributed Training](/concepts/workload-yaml-for-distributed-training.md), writing model checkpoints to storage can consume significant time. The **asynchronous save** pattern decouples the checkpoint serialization from the upload step: the model state is written to a fast local staging area, and the upload to the target storage system proceeds in the background while training resumes. ^[experiment-tracking-and-observability-databricks-on-aws.md]

The key benefit is reduced training downtime. Instead of blocking on a slow network write to [Unity Catalog](/concepts/unity-catalog.md) or Amazon S3, the GPU node can move to the next training step while the checkpoint data is transferred asynchronously. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Implementation

Asynchronous checkpoint saves are implemented using the [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) (DCP) API combined with a dedicated storage writer that stages I/O through a local directory.

### Storage Writer

The [`UCVolumeWriter`](https://docs.databricks.com/aws/en/volumes/volume-files) from the `serverless_gpu.data` package is used as the storage writer for asynchronous saves. This writer:

- Stages all checkpoint data through a fast local directory (`/tmp`, which is NVMe-backed on serverless GPU nodes) ^[experiment-tracking-and-observability-databricks-on-aws.md]
- Uploads to Unity Catalog volumes after local staging is complete ^[experiment-tracking-and-observability-databricks-on-aws.md]
- Preserves metadata atomicity: the `.metadata` file is published only after all data shards finish uploading ^[experiment-tracking-and-observability-databricks-on-aws.md]

### CPU Backend Requirement

Asynchronous saves require a **CPU backend** on the process group because the upload step uses CPU-based I/O. The process group must be initialized with both a CPU backend (for the upload) and a CUDA backend (for computation):

```python
import torch.distributed as dist
dist.init_process_group(backend="cpu:gloo,cuda:nccl", ...)
```
^[experiment-tracking-and-observability-databricks-on-aws.md]

### Code Pattern

```python
import torch.distributed.checkpoint as dcp
from serverless_gpu.data import UCVolumeWriter

checkpoint_path = "/Volumes/my_catalog/my_schema/model/checkpoints"
writer = UCVolumeWriter(checkpoint_path)

future = dcp.async_save(state_dict, storage_writer=writer)
# ...continue training...
future.result()  # blocks until the upload lands on the UC volume
```
^[experiment-tracking-and-observability-databricks-on-aws.md]

The `dcp.async_save()` call returns a Future object immediately. Training can continue on the GPU while the upload runs. Calling `future.result()` blocks until the checkpoint data is fully written to the Unity Catalog volume.

## Loading asynchronously saved checkpoints

To load a checkpoint that was saved asynchronously, use `UCVolumeReader`:

```python
from serverless_gpu.data import UCVolumeReader

reader = UCVolumeReader(checkpoint_path)
dcp.load(state_dict, storage_reader=reader)
```
^[experiment-tracking-and-observability-databricks-on-aws.md]

## Data Pipeline Considerations

An asynchronous model checkpoint captures only the model and optimizer state — it does **not** capture the position of the Data Pipeline within the dataset. This means that when training resumes from an asynchronous checkpoint, it cannot fast-forward to the exact sample where it stopped. To account for this gap:

- Restart from an epoch boundary rather than a sample boundary, or
- Track processed samples or shards in your own training state so you can skip them on resume.
^[experiment-tracking-and-observability-databricks-on-aws.md]

## Checkpoint Frequency

Checkpoint often enough to limit lost work after an interruption, but not so often that I/O overhead slows training. A good target is **one checkpoint every 30 minutes to an hour**. Tune the interval based on your step time and checkpoint size. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- Synchronous Checkpoint Save – The blocking alternative to asynchronous save.
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) – The API used for both synchronous and asynchronous saves.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer used as the target storage for checkpoints.
- Model Checkpointing – General strategies for saving and loading model state during training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – A common training paradigm where checkpointing helps manage state across shards.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Another training paradigm where checkpointing may be needed.

## Requirements

`UCVolumeWriter`, `UCVolumeReader`, and `UCVolumeDataset` require GPU environment 5 (Serverless GPU Python API 0.5.16+) or above. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
