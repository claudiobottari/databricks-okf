---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88605897807de05c45563d97a74bbd899a56b89de4150e193e456df1098b71d2
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-checkpointing-with-pytorch-dcp
    - DCWPD
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: Distributed Checkpointing with PyTorch DCP
description: Saving and loading model and optimizer state during distributed training using PyTorch's distributed checkpoint (dcp) API, enabling fault tolerance and continued training or inference.
tags:
  - pytorch
  - checkpointing
  - distributed-training
timestamp: "2026-06-19T18:37:41.050Z"
---

# Distributed Checkpointing with PyTorch DCP

**Distributed Checkpointing with PyTorch DCP** (Distributed Checkpoint) is a PyTorch API for saving and loading model state, optimizer state, and application state across distributed training environments. DCP is designed to work seamlessly with parallelism strategies like [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), automatically handling the sharded state dictionaries that arise when model parameters, gradients, and optimizer states are distributed across multiple GPUs. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

PyTorch DCP provides a `torch.distributed.checkpoint` module that standardizes the serialization and deserialization of distributed training state. Unlike basic PyTorch checkpointing (e.g., `torch.save(model.state_dict())`), DCP understands the sharded layout of FSDP-wrapped models and correctly reconstructs the state regardless of the number of GPUs or their sharding configuration. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## The `Stateful` Protocol and `AppState` Wrapper

DCP defines a `Stateful` protocol that objects can implement to declare how their state is saved and loaded. A common pattern is to create an `AppState` wrapper class that holds the model and optimizer, and implements the `state_dict()` and `load_state_dict()` methods using DCP's `get_state_dict()` and `set_state_dict()` helper functions. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
class AppState(Stateful):
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer

    def state_dict(self):
        model_state_dict, optimizer_state_dict = get_state_dict(self.model, self.optimizer)
        return {
            "model": model_state_dict,
            "optim": optimizer_state_dict
        }

    def load_state_dict(self, state_dict):
        set_state_dict(
            self.model,
            self.optimizer,
            model_state_dict=state_dict["model"],
            optim_state_dict=state_dict["optim"]
        )
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

The `get_state_dict()` call automatically manages FSDP fully qualified names (FQNs) and sets the default state dict type to `FSDP.SHARDED_STATE_DICT`. Similarly, `set_state_dict()` restores the sharded state onto the model and optimizer. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Saving Checkpoints with `dcp.save()`

Checkpoints are saved using `dcp.save()` with a `state_dict` containing `AppState` instances and a `StorageWriter` that defines the output location. The `FileSystemWriter` supports writing to local files or mounted volumes such as Unity Catalog Volumes. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
from torch.distributed.checkpoint import FileSystemWriter as StorageWriter

writer = StorageWriter(cache_staged_state_dict=False, path=CHECKPOINT_DIR)
state_dict = { 'app': AppState(model, optimizer) }
dcp.save(state_dict, storage_writer=writer, checkpoint_id=f"{CHECKPOINT_DIR}/step{batch_idx}")
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

Key parameters:
- `cache_staged_state_dict=False` — controls whether intermediate state is cached during checkpoint writing
- `checkpoint_id` — a unique identifier for each checkpoint, typically including the step or epoch number

### Checkpointing During Training

In a distributed training loop, checkpoints are typically saved periodically (e.g., every N batches). The checkpoint directory should be accessible from all GPUs in the distributed job. For serverless GPU compute, the recommended storage location is a Unity Catalog Volume mounted at a path like `/Volumes/<catalog>/<schema>/<volume>/<model_name>`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Loading Checkpoints with `dcp.load()`

Checkpoints are loaded using `dcp.load()` with a `state_dict` that mirrors the structure used during saving. When loading outside a distributed training context (i.e., no process group initialized), DCP automatically disables collective operations and loads the checkpoint on a single device. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
model = SimpleTransformer(input_dim=512, num_layers=4, num_classes=10)
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)

state_dict = { 'app': AppState(model, optimizer) }
dcp.load(
    state_dict=state_dict,
    checkpoint_id=f'{CHECKPOINT_DIR}/step0',
)
model.load_state_dict(state_dict['app'].state_dict()['model'])
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Loading Without an Initialized Process Group

DCP supports loading checkpoints on a single GPU or CPU without a distributed process group. When no process group is initialized, DCP disables collective communication and reads the checkpoint data directly. The loaded state dictionary can then be applied to a non-sharded model for inference or continued training. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Integration with MLflow

Distributed checkpoints can be logged as [MLflow](/concepts/mlflow.md) artifacts for versioning and reproducibility. After saving a checkpoint with DCP, call `mlflow.log_artifacts()` to upload the checkpoint directory:

```python
mlflow.log_artifacts(f'{CHECKPOINT_DIR}/step{batch_idx}', artifact_path=f'checkpoints/step{batch_idx}')
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Use Cases

- **Resuming interrupted training** — load the latest checkpoint and continue training from the saved optimizer and model state
- **Model evaluation** — load a checkpoint for inference on a single GPU or CPU
- **Model versioning** — store checkpoints as MLflow artifacts for experiment tracking
- **Fine-tuning** — load a pre-trained checkpoint and continue training on a new dataset

## Best Practices

1. **Use a consistent checkpoint directory** — all GPUs should write to the same base path, with unique checkpoint IDs per save step
2. **Save checkpoints on sharded state** — DCP handles FSDP sharding automatically; do not manually gather parameters across GPUs
3. **Log checkpoints to MLflow** — use `mlflow.log_artifacts()` to track checkpoint versions with experiment runs
4. **Test checkpoint loading** — verify that checkpoints can be loaded outside the distributed context for inference and model serving

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- Unity Catalog Volumes
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Stateful Protocol in PyTorch DCP

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
