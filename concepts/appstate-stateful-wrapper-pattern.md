---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72330506902fb1b3606a21958adf4b929431d2f9fe2d220fe2f437b230cc84d1
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - appstate-stateful-wrapper-pattern
    - ASWP
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: AppState Stateful Wrapper Pattern
description: A design pattern implementing PyTorch's Stateful protocol to wrap model and optimizer state for use with Distributed Checkpoint API, handling FSDP fully qualified names and SHARDED_STATE_DICT automatically.
tags:
  - pytorch
  - checkpointing
  - design-pattern
timestamp: "2026-06-18T12:08:19.908Z"
---

# AppState Stateful Wrapper Pattern

The **AppState Stateful Wrapper Pattern** is a design pattern for checkpointing machine learning models trained with [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md). It implements the `Stateful` protocol from PyTorch's distributed checkpoint API, enabling seamless saving and loading of model and optimizer state in distributed training contexts. The pattern is particularly useful for [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) workloads where checkpointing must handle sharded model parameters across multiple GPUs. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Purpose

When training large models with FSDP, model parameters, gradients, and optimizer states are sharded across multiple GPUs. Standard PyTorch serialization methods (`torch.save`) do not natively handle this sharded state. The `AppState` wrapper addresses this by leveraging PyTorch's distributed checkpoint (DCP) API, which automatically manages the sharded state dict format required by FSDP. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Implementation

The pattern defines a class that wraps a model and optional optimizer, implementing two key methods required by the `Stateful` protocol: `state_dict()` and `load_state_dict()`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
from torch.distributed.checkpoint.stateful import Stateful
from torch.distributed.checkpoint.state_dict import get_state_dict, set_state_dict

class AppState(Stateful):
    """Wrapper for checkpointing model and optimizer state.

    This wrapper is compliant with the Stateful protocol, so DCP will
    automatically call state_dict/load_state_dict as needed in the
    dcp.save/load APIs.
    """
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer

    def state_dict(self):
        # Automatically manages FSDP FQN's and sets default state dict type
        # to FSDP.SHARDED_STATE_DICT
        model_state_dict, optimizer_state_dict = get_state_dict(
            self.model, self.optimizer
        )
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

### Key Methods

- **`state_dict()`**: Calls `get_state_dict()` internally, which handles the conversion of FSDP's sharded state into a format suitable for checkpointing. It automatically manages fully qualified names (FQNs) and sets the default state dict type to `FSDP.SHARDED_STATE_DICT`. Returns a dictionary containing model and optimizer state. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

- **`load_state_dict(state_dict)`**: Calls `set_state_dict()` to restore the model and optimizer from the saved checkpoint. Accepts the state dict previously saved by `state_dict()`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Usage in Training

During training, the `AppState` wrapper is used with `dcp.save()` for saving checkpoints and `dcp.load()` for restoring them. The wrapper is passed as part of a state dictionary to the distributed checkpoint API. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Saving Checkpoints

```python
import torch.distributed.checkpoint as dcp
from torch.distributed.checkpoint import FileSystemWriter as StorageWriter

checkpoint_dir = "/Volumes/catalog/schema/volume/model_name"
writer = StorageWriter(cache_staged_state_dict=False, path=checkpoint_dir)

state_dict = {'app': AppState(model, optimizer)}
dcp.save(state_dict, storage_writer=writer, checkpoint_id=f"{checkpoint_dir}/step{batch_idx}")
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Loading Checkpoints

When loading outside a distributed training context — for example, during inference — the DCP API automatically disables collective operations since no process group is initialized. The checkpoint loads on a single device. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
model = SimpleTransformer(input_dim=512, num_layers=4, num_classes=10)
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)

state_dict = {'app': AppState(model, optimizer)}
dcp.load(state_dict=state_dict, checkpoint_id=f"{checkpoint_dir}/step0")
model.load_state_dict(state_dict['app'].state_dict()['model'])
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Benefits

- **Automatic shard management**: Eliminates manual handling of FSDP's sharded state dict format. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Unified save/load interface**: Provides a consistent API for both training and inference checkpointing. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Graceful degredation outside distributed context**: When loading without a process group, collective operations are automatically disabled, allowing checkpoints to be loaded on single-GPU or CPU systems. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Integration with MLflow**: Checkpoints saved using the wrapper can be logged as MLflow artifacts for versioning and reproducibility tracking. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- Distributed Training using PyTorch FSDP on Serverless GPU Compute
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [PyTorch Distributed Checkpoint API](/concepts/pytorch-distributed-checkpoint-dcp.md)
- FSDP State Dict Management

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
