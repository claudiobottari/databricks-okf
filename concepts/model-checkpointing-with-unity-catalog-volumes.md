---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0763f47a83efdb499eeb639399675b1d781d02c0db03dda7b7f5d180bd651af
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-checkpointing-with-unity-catalog-volumes
    - MCWUCV
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Model Checkpointing with Unity Catalog Volumes
description: Distributed training on AI Runtime uses UCVolumeWriter and UCVolumeReader for asynchronous checkpoint saves/loads to Unity Catalog volumes, leveraging NVMe-backed local staging for performance.
tags:
  - checkpointing
  - unity-catalog
  - distributed-training
timestamp: "2026-06-19T18:44:57.976Z"
---

# Model Checkpointing with Unity Catalog Volumes

**Model Checkpointing with Unity Catalog Volumes** describes the practice of saving and loading model checkpoints to and from Unity Catalog Volumes using dedicated, high‑performance storage backends. This approach is designed for distributed training on Databricks and provides governed, persistent storage for model and optimizer state, enabling resumption of training and reproducibility across sessions. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Overview

For distributed training, model checkpoints can be saved asynchronously to Unity Catalog volumes. The `serverless_gpu.data` package provides `UCVolumeWriter` and `UCVolumeReader` that integrate with the [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) (DCP) API. These backends stage all I/O through a fast local directory (NVMe‑backed on serverless GPU nodes) and then upload to or download from the Unity Catalog volume. This approach is significantly faster than writing checkpoint shards directly to the FUSE mount. Metadata atomicity is preserved: the writer publishes the `.metadata` file only after all data shards have finished uploading. ^[experiment-tracking-and-observability-databricks-on-aws.md]

`UCVolumeWriter`, `UCVolumeReader`, and `UCVolumeDataset` require GPU environment 5 (Serverless GPU Python API 0.5.16+) or above. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Asynchronous Checkpointing

To avoid blocking training while a checkpoint is being saved, you can use `dcp.async_save` with a `UCVolumeWriter`. Asynchronous saves require a CPU backend on the process group, so the process group must be initialized with a hybrid backend (e.g., `"cpu:gloo,cuda:nccl"`). The following example shows how to initiate a non‑blocking save and continue training: ^[experiment-tracking-and-observability-databricks-on-aws.md]

```python
import torch.distributed.checkpoint as dcp
from serverless_gpu.data import UCVolumeWriter

checkpoint_path = "/Volumes/my_catalog/my_schema/model/checkpoints"
writer = UCVolumeWriter(checkpoint_path)
future = dcp.async_save(state_dict, storage_writer=writer)
# ... continue training ...
future.result()  # blocks until the upload finishes
```

## Loading Checkpoints

To load a previously saved checkpoint, use `UCVolumeReader` with the same checkpoint path: ^[experiment-tracking-and-observability-databricks-on-aws.md]

```python
from serverless_gpu.data import UCVolumeReader

reader = UCVolumeReader(checkpoint_path)
dcp.load(state_dict, storage_reader=reader)
```

## Data Pipeline Checkpointing

A model checkpoint captures model parameters and optimizer state, but it does **not** capture the position of the data pipeline within the dataset. This means a resumed run cannot fast‑forward to the exact sample where it stopped. When resuming, account for this by restarting from an epoch boundary or by tracking processed samples or shards in your own training state so you can skip them on resume. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Best Practices

- **Checkpoint frequency** – Checkpoint often enough to limit lost work after an interruption, but not so often that I/O overhead slows training. Aim for one checkpoint every 30 minutes to an hour, tuning the interval based on your step time and checkpoint size. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Storage governance** – Using Unity Catalog volumes ensures that checkpoints are governed by the same access controls and lineage as other Unity Catalog objects. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Use the fast local directory** – The UCVolumeWriter and UCVolumeReader automatically stage writes and reads through a local NVMe directory (`/tmp`), avoiding the slower FUSE mount for the bulk of the I/O. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- Unity Catalog Volumes – Governed file storage for Databricks.
- [Torch Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md) – PyTorch API for saving and loading sharded model states.
- GPU environment 5 – Required environment version for UCVolumeWriter/Reader.
- [Experiment tracking and observability](/concepts/mlflow-for-experiment-tracking-and-model-registry.md) – MLflow integration and monitoring on AI Runtime.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry.

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
