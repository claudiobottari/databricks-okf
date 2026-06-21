---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dbc4b326f25855ab1b1e42f976057003306db1c97eca5b3dc6ae1194d1129b64
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - pytorch-distributed-checkpoint-dcp-with-appstate-wrapper
    - PDC(WAW
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: PyTorch Distributed Checkpoint (DCP) with AppState Wrapper
description: A pattern for checkpointing distributed model training using PyTorch's distributed checkpoint API combined with a Stateful AppState wrapper that automatically handles FSDP state dict management and checkpoint save/load operations.
tags:
  - pytorch
  - checkpointing
  - distributed-training
timestamp: "2026-06-19T10:18:48.073Z"
---

---
title: PyTorch Distributed Checkpoint (DCP) with AppState Wrapper
summary: A pattern for checkpointing model and optimizer state in PyTorch FSDP training using the `AppState` wrapper and PyTorch's Distributed Checkpoint API.
sources:
  - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:00:00.000Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - pytorch
  - distributed-training
  - checkpointing
  - fsdp
aliases:
  - pytorch-distributed-checkpoint-appstate
  - dcp-appstate-wrapper
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# PyTorch Distributed Checkpoint (DCP) with AppState Wrapper

**PyTorch Distributed Checkpoint (DCP) with AppState Wrapper** is a design pattern for saving and loading the state of a PyTorch model and optimizer during distributed training — specifically when using [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). The `AppState` class wraps the model and optimizer and implements the `Stateful` protocol so that the standard PyTorch DCP APIs (`dcp.save` and `dcp.load`) can automatically manage the distributed state dictionaries. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

In FSDP training, model parameters, gradients, and optimizer states are sharded across multiple GPUs. Saving a checkpoint with plain `torch.save` does not correctly handle the sharded layout. PyTorch Distributed Checkpoint (DCP) solves this by providing APIs that understand sharded state dictionaries. The `AppState` wrapper simplifies integration by implementing the `Stateful` protocol that DCP expects. The wrapper is used in conjunction with `get_state_dict` and `set_state_dict` from `torch.distributed.checkpoint.state_dict`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## How AppState Works

The `AppState` class is defined as follows (source code from the Databricks example):

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

### Key Behaviors

- **`state_dict()`**: Calls `get_state_dict()`, which automatically manages FSDP fully qualified names (FQNs) and sets the default state dict type to `FSDP.SHARDED_STATE_DICT`. The method returns a flat dictionary with keys `"model"` and `"optim"` containing the sharded state. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **`load_state_dict()`**: Calls `set_state_dict()` to restore the model and optimizer states from the previously saved dictionaries. This function correctly distributes the sharded state across the available GPUs. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Usage in Training and Loading

### Saving a Checkpoint

During training, an `AppState` instance is created and passed as the value in a dictionary under the key `"app"`. The dictionary is then saved with `dcp.save()`:

```python
writer = StorageWriter(cache_staged_state_dict=False, path=CHECKPOINT_DIR)
state_dict = { 'app': AppState(model, optimizer) }
dcp.save(state_dict, storage_writer=writer, checkpoint_id=f"{CHECKPOINT_DIR}/step{batch_idx}")
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Loading a Checkpoint

To load a checkpoint, create the model and optimizer (without FSDP wrapping for single‑device inference), instantiate `AppState`, then call `dcp.load()`:

```python
model = SimpleTransformer(input_dim=512, num_layers=4, num_classes=10)
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)
state_dict = { 'app': AppState(model, optimizer) }
dcp.load(state_dict, checkpoint_id=f'{CHECKPOINT_DIR}/step0')
model.load_state_dict(state_dict['app'].state_dict()['model'])
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

When no process group is initialized (e.g., during inference on a single GPU), DCP automatically disables collective operations and loads the checkpoint locally. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Benefits

- **Simplifies checkpointing code**: By implementing the `Stateful` protocol, `AppState` allows the full checkpoint logic to be expressed as a single dictionary passed to `dcp.save()` / `dcp.load()`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Handles sharded state correctly**: Uses `get_state_dict` and `set_state_dict` to manage FSDP FQNs and sharded state types, avoiding common pitfalls with manual state management. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Reusable**: The same wrapper pattern can be applied to any PyTorch model and optimizer, not just the example transformer. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [PyTorch Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md)
- Stateful protocol
- get_state_dict / set_state_dict
- [Serverless GPU Distributed Training on Databricks](/concepts/serverless-gpu-training-on-databricks.md)

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
