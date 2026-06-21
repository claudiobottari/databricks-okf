---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9668985948be942a3bdb56625224060afbac39a55310068861ec72fef816b768
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-distributed-checkpoint-dcp
    - PDC(
    - Distributed Checkpoint (DCP)
    - PyTorch Distributed Checkpoint
    - PyTorch Distributed Checkpoint API
    - Torch Distributed Checkpoint
    - Torch Distributed Checkpoint (DCP)
    - torch.distributed.checkpoint
    - Checkpointing with torch.distributed.checkpoint
    - Distributed Checkpointing
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
      start: 46
      end: 62
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
      start: 164
      end: 170
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
      start: 143
      end: 145
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
      start: 218
      end: 228
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
      start: 165
      end: 170
title: PyTorch Distributed Checkpoint (DCP)
description: A PyTorch API for saving and loading model and optimizer state in distributed training contexts, supporting sharded state dicts and async checkpointing across multiple devices.
tags:
  - pytorch
  - checkpointing
  - distributed-training
timestamp: "2026-06-18T15:33:32.044Z"
---

---

title: PyTorch Distributed Checkpoint (DCP)
summary: A PyTorch API for saving and loading distributed model checkpoints across multiple devices, supporting sharded state dicts and automatic disabling of collectives when no process group is initialized.
sources:
  - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  - image-classification-using-convolutional-neural-networks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:08:01.011Z"
updatedAt: "2026-06-18T12:08:01.011Z"
tags:
  - pytorch
  - checkpointing
  - distributed-training
aliases:
  - pytorch-distributed-checkpoint-dcp
  - PDC(
confidence: 1.0
provenanceState: extracted
inferredParagraphs: 0
---

# PyTorch Distributed Checkpoint (DCP)

**PyTorch Distributed Checkpoint (DCP)** is a PyTorch API for saving and loading model and optimizer state across distributed training processes. Unlike traditional `torch.save`, DCP is designed to work with distributed parallelism strategies such as [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) and handles sharded state dictionaries, collective communication, and checkpoint consistency across multiple ranks. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

DCP provides a stateful protocol that simplifies saving and loading distributed training artifacts. The core API consists of `dcp.save()` and `dcp.load()`, which accept a state dictionary and a checkpoint identifier (typically a filesystem path). DCP automatically handles the distribution of state across ranks when a process group is initialized; when no process group exists (e.g., for inference on a single device), DCP disables collective operations and loads the full state on that device. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md, distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Stateful Protocol (`Stateful`)

DCP implements a `Stateful` protocol via the `torch.distributed.checkpoint.stateful.Stateful` class. Objects that inherit from `Stateful` must implement `state_dict()` and `load_state_dict()` methods. When passed inside the state dictionary to `dcp.save()` or `dcp.load()`, DCP calls these methods automatically, eliminating the need for manual serialization logic. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### The `AppState` Wrapper

A common pattern in Databricks notebooks is to wrap the model and optimizer in an `AppState` class that inherits from `Stateful`. This wrapper uses `torch.distributed.checkpoint.state_dict.get_state_dict()` and `set_state_dict()` to retrieve and set the distributed state dictionaries. The `get_state_dict()` function automatically manages FSDP fully qualified names (FQNs) and sets the default state dict type to `FSDP.SHARDED_STATE_DICT`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

Example definition from the FSDP notebook:

```python
class AppState(Stateful):
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer

    def state_dict(self):
        model_state_dict, optimizer_state_dict = get_state_dict(self.model, self.optimizer)
        return {"model": model_state_dict, "optim": optimizer_state_dict}

    def load_state_dict(self, state_dict):
        set_state_dict(
            self.model, self.optimizer,
            model_state_dict=state_dict["model"],
            optim_state_dict=state_dict["optim"]
        )
```
^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:46-62]

## Saving a Checkpoint

Checkpoints are saved using `dcp.save()` with a state dictionary and a checkpoint identifier. The identifier is typically a filesystem path pointing to a Unity Catalog Volume or other persistent storage. DCP writes per-rank shards and metadata.

Example from the FSDP notebook:

```python
state_dict = {'app': AppState(model, optimizer)}
writer = StorageWriter(cache_staged_state_dict=False, path=CHECKPOINT_DIR)
dcp.save(state_dict, storage_writer=writer, checkpoint_id=f"{CHECKPOINT_DIR}/step{batch_idx}")
```
^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:164-170]

In the single-GPU CNN notebook, the checkpoint is saved after each epoch:

```python
state_dict = { "app": AppState(model, optimizer) }
dcp.save(state_dict, checkpoint_id=CHECKPOINT_DIR)
```
^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md:143-145]

## Loading a Checkpoint

Checkpoints are loaded with `dcp.load()`. When loading outside a distributed context (no process group initialized), DCP automatically disables collective operations and loads the full state onto a single device. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:218-228]

Example loading a checkpoint for inference:

```python
model = SimpleTransformer(...)
optimizer = optim.AdamW(model.parameters(), ...)
state_dict = { 'app': AppState(model, optimizer) }
dcp.load(state_dict, checkpoint_id=f'{CHECKPOINT_DIR}/step0')
model.load_state_dict(state_dict['app'].state_dict()['model'])
```
^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:218-228]

In the CNN example, loading restores both model and optimizer state:

```python
model = Net()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=momentum)
app_state = AppState(model, optimizer)
state_dict = { "app": app_state }
dcp.load(state_dict, checkpoint_id=CHECKPOINT_DIR)
```
^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md:165-170]

## DCP with FSDP

When using FSDP, `get_state_dict()` automatically sets the state dict type to `FSDP.SHARDED_STATE_DICT`, ensuring that only the shard belonging to the current rank is saved. This reduces memory overhead and speeds up checkpointing. The `StorageWriter` (e.g., `FileSystemWriter`) handles writing the sharded files. DCP’s `cache_staged_state_dict=False` option avoids caching intermediate state in memory. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Best Practices

- **Use the `Stateful` wrapper** (`AppState` pattern) to let DCP manage state dict transfer automatically.
- **Specify a `checkpoint_id`** that is a path to a Unity Catalog Volume or other durable storage. On Databricks, the path follows the format `/Volumes/<catalog>/<schema>/<volume>/<model_name>`.
- **Log checkpoints as MLflow artifacts** by calling `mlflow.log_artifacts()` after saving, enabling traceability and versioning. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Call `dcp.load()` without a process group** for single-device inference; DCP will automatically disable collectives.
- **Use `StorageWriter`** when saving to paths that require explicit writer (e.g., distributed file systems).

## Limitations

- DCP is designed for distributed training and may not be suitable for very small models where `torch.save` overhead is negligible.
- Checkpoint compatibility across different PyTorch versions or FSDP configurations requires careful testing.
- On Databricks serverless GPU compute, ensure the checkpoint path exists (e.g., create the Unity Catalog Volume directory before saving).

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Distributed training strategy that DCP is commonly used with.
- Unity Catalog Volumes — Storage location for DCP checkpoints in Databricks.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — For logging checkpoints and training metrics.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute environment where DCP checkpoints are created and loaded.
- PyTorch Distributed Training — The broader framework for multi-GPU and multi-node training.

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
- image-classification-using-convolutional-neural-networks-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
2. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
3. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:46-62](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
4. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:164-170](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
5. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md:143-145](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
6. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md:218-228](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
7. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md:165-170](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
