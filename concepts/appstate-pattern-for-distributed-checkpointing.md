---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dcfe4edf750dde4ead8b7d7a055d05a2ea9b6375a41d6cf20f086ef6459d5d8b
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - appstate-pattern-for-distributed-checkpointing
    - APFDC
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: AppState Pattern for Distributed Checkpointing
description: A Stateful-protocol-compliant wrapper class that encapsulates model and optimizer state dict logic for use with PyTorch's distributed checkpoint save/load APIs in FSDP contexts.
tags:
  - pytorch
  - checkpointing
  - design-pattern
timestamp: "2026-06-18T15:33:32.647Z"
---

# AppState Pattern for Distributed Checkpointing

The **AppState Pattern for Distributed Checkpointing** is a design pattern for saving and loading training state (model parameters and optimizer state) in [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md) workflows. It leverages the `Stateful` protocol from [PyTorch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) (DCP) to automatically manage the conversion between the native model/optimizer state dictionaries and the sharded state dictionaries required by FSDP. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

When training large models with FSDP, parameters, gradients, and optimizer states are sharded across devices. Standard `torch.save(model.state_dict())` cannot capture the sharded layout needed for checkpointing and resumption. The AppState wrapper encapsulates a model (and optionally an optimizer) and implements the `Stateful` protocol, so DCP handles the state dictionary transformation automatically during `dcp.save()` and `dcp.load()`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Implementation

The wrapper defines two key methods:

### `state_dict()`

Calls `get_state_dict(model, optimizer)` from `torch.distributed.checkpoint.state_dict`. This automatically manages FSDP fully qualified names (FQNs) and sets the default state dict type to `FSDP.SHARDED_STATE_DICT`. It returns a dictionary containing `"model"` and `"optim"` entries containing the sharded state dictionaries. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### `load_state_dict(state_dict)`

Calls `set_state_dict(model, optimizer, model_state_dict=..., optim_state_dict=...)` to restore the sharded state from the loaded checkpoint onto the model and optimizer. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Usage Example

```python
import torch.distributed.checkpoint as dcp
from torch.distributed.checkpoint.stateful import Stateful
from torch.distributed.checkpoint.state_dict import get_state_dict, set_state_dict

class AppState(Stateful):
    """A wrapper for checkpointing the application state.
    Since this object is compliant with the Stateful protocol,
    DCP will automatically call state_dict/load_state_dict as needed
    in the dcp.save/load APIs.
    """
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer

    def state_dict(self):
        model_state_dict, optimizer_state_dict = get_state_dict(
            self.model, self.optimizer
        )
        return {
            "model": model_state_dict,
            "optim": optimizer_state_dict,
        }

    def load_state_dict(self, state_dict):
        set_state_dict(
            self.model,
            self.optimizer,
            model_state_dict=state_dict["model"],
            optim_state_dict=state_dict["optim"],
        )
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Saving and Loading Checkpoints

### Saving

Create an `AppState` instance and pass it inside a state dictionary to `dcp.save()`. DCP calls `AppState.state_dict()` to obtain the sharded dictionaries:

```python
app_state = AppState(model, optimizer)
state_dict = { 'app': app_state }
dcp.save(state_dict, storage_writer=writer, checkpoint_id="/path/to/checkpoint")
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Loading

When loading, DCP calls `AppState.load_state_dict(state_dict)` to restore the model and optimizer. If no process group is initialized (e.g., for inference on a single device), DCP automatically disables collective operations and loads the checkpoint on a single device. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
model = SimpleTransformer(...)
optimizer = optim.AdamW(model.parameters(), ...)
app_state = AppState(model, optimizer)
state_dict = { 'app': app_state }
dcp.load(state_dict=state_dict, checkpoint_id="/path/to/checkpoint")
model.load_state_dict(app_state.state_dict()['model'])
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Key Benefits

- **Compatibility with FSDP**: Handles sharded state dictionaries automatically, avoiding common errors with naive `state_dict()` calls on FSDP-wrapped models. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Single checkpoint file per rank**: DCP can save and load sharded state across multiple ranks while the `AppState` wrapper abstracts the complexity. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Works outside distributed context**: When no process group is initialized, DCP disables collectives, making the same `AppState` pattern usable for inference or continued training on a single device. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md)
- [PyTorch Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md)
- Stateful Protocol
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
