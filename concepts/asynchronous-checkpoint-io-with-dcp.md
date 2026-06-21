---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a31ce039c7ff72a784c5189a34e9939925443e5230c6cdcd45f3c22eb53e702
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - asynchronous-checkpoint-io-with-dcp
    - ACIWD
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Asynchronous Checkpoint I/O with DCP
description: Using dcp.async_save with UCVolumeWriter to upload checkpoints in the background while training continues, requiring a CPU backend on the process group with gloo and nccl.
tags:
  - distributed-training
  - checkpointing
  - performance
timestamp: "2026-06-19T10:26:29.391Z"
---

# Asynchronous Checkpoint I/O with DCP

**Asynchronous Checkpoint I/O with DCP** refers to the use of the [Torch Distributed Checkpoint](https://pytorch.org/docs/stable/distributed.checkpoint.html) (DCP) API together with Unity Catalog volume storage backends to save model checkpoints in the background while training continues. This approach reduces training stalls caused by blocking I/O and is supported on Databricks AI Runtime nodes that use Serverless GPU environment 5 or above.^[experiment-tracking-and-observability-databricks-on-aws.md]

## Overview

When training large models on GPU clusters, checkpoint I/O can become a bottleneck because writing model and optimizer states to persistent storage typically halts forward/backward computation. Async checkpointing decouples the save operation from the training loop: the state dictionary is written to a fast local NVMe-backed directory (`/tmp`) and then uploaded to a Unity Catalog volume in the background. The trainer can proceed to the next step without waiting for the upload to complete.^[experiment-tracking-and-observability-databricks-on-aws.md]

Databricks provides two storage backends in the `serverless_gpu.data` package for use with DCP:

- **`UCVolumeWriter`** – writes checkpoints asynchronously via `dcp.async_save()`.
- **`UCVolumeReader`** – loads a checkpoint synchronously via `dcp.load()`.

These backends stage all I/O through the local NVMe directory, which is faster than writing checkpoint shards directly to the Unity Catalog Volumes FUSE mount. Metadata atomicity is preserved: the writer publishes the `.metadata` file only after all data shards have finished uploading.^[experiment-tracking-and-observability-databricks-on-aws.md]

## Requirements

- AI Runtime with [GPU environment 5](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/five-gpu) or above (Serverless GPU Python API 0.5.16+).^[experiment-tracking-and-observability-databricks-on-aws.md]
- A Unity Catalog volume to store the checkpoint files.
- A CPU backend on the process group, because asynchronous saves cannot run on the CUDA backend. Initialize the process group with `torch.distributed.init_process_group(backend="cpu:gloo,cuda:nccl", ...)`.^[experiment-tracking-and-observability-databricks-on-aws.md]

## How It Works

1. **Write (asynchronous)** – Pass a `UCVolumeWriter` as the `storage_writer` argument to `dcp.async_save()`. The function returns a future object. Training can continue while the upload proceeds. Call `future.result()` at a convenient point to ensure the upload has landed on the volume before proceeding to a code path that depends on the checkpoint (e.g., model export or termination).^[experiment-tracking-and-observability-databricks-on-aws.md]

   ```python
   import torch.distributed.checkpoint as dcp
   from serverless_gpu.data import UCVolumeWriter

   checkpoint_path = "/Volumes/my_catalog/my_schema/model/checkpoints"
   writer = UCVolumeWriter(checkpoint_path)
   future = dcp.async_save(state_dict, storage_writer=writer)

   # ... continue training ...

   future.result()  # block until upload completes
   ```

2. **Read (synchronous)** – Use `UCVolumeReader` with `dcp.load()` to load a previous checkpoint. The backend downloads the shards to local storage and then restores the state dictionary.^[experiment-tracking-and-observability-databricks-on-aws.md]

   ```python
   from serverless_gpu.data import UCVolumeReader

   reader = UCVolumeReader(checkpoint_path)
   dcp.load(state_dict, storage_reader=reader)
   ```

## Data Pipeline Checkpointing

A model checkpoint captures only the model and optimizer state, not the position of the data pipeline within the dataset. Therefore, a resumed run cannot fast-forward to the exact sample where training stopped. Practitioners must account for this in their resume logic: either restart from an epoch boundary or track processed samples or shards in a custom training state so that they can be skipped on resume.^[experiment-tracking-and-observability-databricks-on-aws.md]

## Best Practices

- **Checkpoint frequency** – Aim for one checkpoint every 30 minutes to an hour. Tune the interval based on step time and checkpoint size. Frequent saves can add I/O overhead; infrequent saves increase the amount of lost work after an interruption.^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Process group initialization** – Always include a CPU backend in the process group when using `dcp.async_save`, e.g., `backend="cpu:gloo,cuda:nccl"`. Without a CPU backend, the asynchronous writer cannot run in the background.^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Metadata atomicity** – Rely on the property that the `.metadata` file is written only after all shards have been successfully uploaded. This prevents partial checkpoints from being loaded on resume.^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Unity Catalog volume paths** – Use absolute paths starting with `/Volumes/` to specify checkpoint locations. These paths respect Unity Catalog’s governance and access control.^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- Model Checkpointing – General strategies for saving and resuming training.
- Unity Catalog Volumes – Storage locations for checkpoints with governance.
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) – The underlying API for save/load of distributed model state.
- [GPU Environment on AI Runtime](/concepts/serverless-gpu-environments-in-ai-runtime.md) – Required runtime version for async checkpoint support.
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – Complementary tool for logging metrics and artifacts alongside checkpoints.

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
