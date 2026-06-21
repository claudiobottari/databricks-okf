---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53ea03a74133e784cb630517452cf8136063250c7913a7920604ddc2d1076fd3
  pageDirectory: concepts
  sources:
    - image-classification-using-convolutional-neural-networks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-distributed-checkpoint-stateful-protocol
    - PDCSP
  citations:
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
title: PyTorch Distributed Checkpoint Stateful Protocol
description: A pattern using AppState as a Stateful wrapper around model and optimizer to enable distributed checkpointing with dcp.save/dcp.load, automatically managing state_dict serialization.
tags:
  - pytorch
  - distributed-training
  - checkpointing
timestamp: "2026-06-19T19:09:26.812Z"
---

# PyTorch Distributed Checkpoint Stateful Protocol

The **PyTorch Distributed Checkpoint Stateful Protocol** is a mechanism that enables [torch.distributed.checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) (DCP) to automatically manage the saving and loading of state dictionaries for distributed model components. By implementing the `Stateful` protocol, custom wrapper classes can hook into DCP's save/load APIs, allowing DCP to automatically call `state_dict()` and `load_state_dict()` as needed during checkpoint operations. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Overview

The Stateful protocol is particularly useful for managing [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) model states and optimizer states in distributed training scenarios. When a class implements the `Stateful` protocol, DCP will automatically handle the distribution of state dict operations across processes, ensuring proper management of fully qualified names (FQN) and state dict types. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Implementation

To implement the Stateful protocol, a class must inherit from `torch.distributed.checkpoint.stateful.Stateful` and implement two required methods:

### state_dict()
The `state_dict()` method returns a dictionary containing the model and optimizer state. It should call `get_state_dict()` to automatically manage FSDP FQN's and set the default state dict type to `FSDP.SHARDED_STATE_DICT`. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

### load_state_dict()
The `load_state_dict()` method receives the loaded state dictionary and calls `set_state_dict()` to restore the model and optimizer state from the checkpoint. ^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]

## Example Implementation

```python
from torch.distributed.checkpoint.stateful import Stateful
from torch.distributed.checkpoint.state_dict import get_state_dict, set_state_dict

class AppState(Stateful):
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer
    
    def state_dict(self):
        model_state_dict, optimizer_state_dict = get_state_dict(
            self.model, 
            self.optimizer
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

## Usage with DCP

When using the Stateful protocol, DCP save and load operations work seamlessly:

### Saving Checkpoints
```python
state_dict = { "app": AppState(model, optimizer) }
dcp.save(state_dict, checkpoint_id=CHECKPOINT_DIR)
```

### Loading Checkpoints
```python
app_state = AppState(model, optimizer)
state_dict = { "app": app_state }
dcp.load(state_dict, checkpoint_id=CHECKPOINT_DIR)
```

## Benefits

The Stateful protocol provides several advantages for distributed training:
- **Automatic state dict management**: DCP handles the distribution of state dict operations across processes
- **FSQ integration**: Automatically manages FSDP fully qualified names and sharded state dict types
- **Simplified checkpointing**: Reduces boilerplate code for saving and loading distributed model states
- **Consistent API**: Provides a uniform interface for both single and multi-GPU checkpoint scenarios

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- Model Checkpointing
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)

## Sources

- image-classification-using-convolutional-neural-networks-databricks-on-aws.md

# Citations

1. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
