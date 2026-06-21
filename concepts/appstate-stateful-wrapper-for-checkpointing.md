---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b00be4d2365a57685ebd93b21100de313e0f2160720b54eb42c520976acedc85
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - appstate-stateful-wrapper-for-checkpointing
    - ASWFC
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
      start: 47
      end: 55
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
      start: 57
      end: 62
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
      start: 147
      end: 175
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
      start: 190
      end: 200
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
      start: 161
      end: 163
title: AppState Stateful Wrapper for Checkpointing
description: A PyTorch Stateful protocol-compliant wrapper class that encapsulates model and optimizer state, automatically managing FSDP fully qualified names and sharded state dict types during dcp.save/load operations.
tags:
  - pytorch
  - checkpointing
  - design-pattern
timestamp: "2026-06-19T18:36:41.637Z"
---

# AppState Stateful Wrapper for Checkpointing

The **AppState Stateful Wrapper for Checkpointing** is a utility class that implements PyTorch's `Stateful` protocol to enable distributed checkpointing of model and optimizer state using PyTorch's Distributed Checkpoint (DCP) API. It is designed to work with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) models by automatically handling the sharded state dictionaries required for distributed training. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

`AppState` wraps a model and optionally an optimizer, providing a clean interface for saving and loading checkpoint state in [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) environments. Because it is compliant with the `Stateful` protocol, DCP automatically calls `state_dict()` and `load_state_dict()` as needed when using the `dcp.save()` and `dcp.load()` APIs. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Class Definition

```python
class AppState(Stateful):
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer
```

The wrapper accepts two parameters:
- `model`: The PyTorch model to checkpoint (typically wrapped with FSDP).
- `optimizer` (optional): The optimizer whose state should be saved alongside the model.

## State Dictionary Methods

### `state_dict()`

The `state_dict()` method calls `get_state_dict()` from `torch.distributed.checkpoint.state_dict`, which automatically manages FSDP fully qualified names (FQNs) and sets the default state dict type to `FSDP.SHARDED_STATE_DICT`. It returns a dictionary containing both `"model"` and `"optim"` state dictionaries. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:47-55]

### `load_state_dict(state_dict)`

The `load_state_dict()` method calls `set_state_dict()` to restore the model and optimizer state from the loaded checkpoint data. This operation is the inverse of `state_dict()` and properly handles sharded state dictionaries. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:57-62]

## Usage in Checkpoint Saving

During training, the wrapper is used with `dcp.save()` as follows:

```python
from torch.distributed.checkpoint import FileSystemWriter as StorageWriter
import torch.distributed.checkpoint as dcp

writer = StorageWriter(cache_staged_state_dict=False, path=CHECKPOINT_DIR)
state_dict = { 'app': AppState(model, optimizer) }
dcp.save(state_dict, storage_writer=writer, checkpoint_id=f"{CHECKPOINT_DIR}/step{batch_idx}")
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:147-175]

The wrapper is particularly useful in [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) training loops where periodic checkpointing is needed for fault tolerance and experiment tracking.

## Usage in Checkpoint Loading

To load a checkpoint outside of a distributed training context (when no process group is initialized), DCP automatically disables collective operations. The wrapper handles loading as follows:

```python
state_dict = { 'app': AppState(model, optimizer) }
dcp.load(
    state_dict=state_dict,
    checkpoint_id=f'{CHECKPOINT_DIR}/step0',
)
model.load_state_dict(state_dict['app'].state_dict()['model'])
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:190-200]

## Integration with MLflow

When used in [Databricks Serverless GPU Compute](/concepts/databricks-serverless-gpu-compute.md) training pipelines, checkpoints saved through the `AppState` wrapper can be logged as MLflow artifacts for versioning and reproducibility. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:161-163]

## Related Concepts

- [Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md) — The PyTorch API for saving and loading distributed training state.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — The distributed training strategy that shards model parameters across GPUs.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The managed compute infrastructure for running distributed training workloads.
- Stateful Protocol — The PyTorch protocol that `AppState` implements for checkpoint compatibility.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Typical hardware setup for FSDP training on Databricks.

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
2. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:47-55](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
3. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:57-62](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
4. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:147-175](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
5. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:190-200](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
6. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:161-163](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
