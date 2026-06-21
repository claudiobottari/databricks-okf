---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23ad14d32a36b877257777b081fa71ce611a120b0cb2dab8bc222d50af911e91
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-fully-sharded-data-parallel-fsdp
    - PFSDP(
    - PyTorch FSDP
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: PyTorch Fully Sharded Data Parallel (FSDP)
description: A distributed training strategy that shards model parameters, gradients, and optimizer states across multiple GPUs to reduce per-GPU memory and enable training of large models that don't fit on a single GPU.
tags:
  - distributed-training
  - pytorch
  - deep-learning
timestamp: "2026-06-19T18:36:32.420Z"
---

# PyTorch Fully Sharded Data Parallel (FSDP)

**PyTorch Fully Sharded Data Parallel (FSDP)** is a distributed training strategy that shards model parameters, gradients, and optimizer states across multiple GPUs, reducing per‑GPU memory usage and enabling efficient training of large models that do not fit on a single GPU. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

FSDP is a data parallelism technique – each GPU processes a different batch of data, but the model itself is partitioned (sharded) among the devices rather than fully replicated. This makes it possible to train models with billions of parameters on a cluster of GPUs where a single GPU would be insufficient. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## How FSDP Works

### Parameter, Gradient, and Optimizer State Sharding

FSDP divides the parameters of each layer, the gradients computed during backpropagation, and the optimizer state (e.g., momentum buffers) across the participating GPUs. During the forward pass, FSDP uses all‑gather operations to collect the sharded parameters for the current layer; after the backward pass, the gradients are reduced and re‑sharded. This design keeps only the shard resident in GPU memory at any given time, dramatically lowering memory consumption. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Wrapping with `fully_shard`

FSDP is applied to a model by wrapping individual layers and the whole model with the `fully_shard()` function from `torch.distributed.fsdp`. Typically, each transformer layer is wrapped first, then the entire model is wrapped, giving FSDP full control over how parameters are sharded. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
from torch.distributed.fsdp import fully_shard

# Apply FSDP to each transformer layer
for layer in model.layers:
    fully_shard(layer)

# Apply FSDP to the entire model
fully_shard(model)
```

### Distributed Process Group Setup

Before FSDP can operate, a distributed process group must be initialized with the NCCL backend. A typical `setup()` function checks environment variables `RANK`, `WORLD_SIZE`, and `LOCAL_RANK`, calls `dist.init_process_group()`, and sets the current CUDA device to the local rank. If only one GPU is detected, FSDP wrapping is skipped. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
def setup():
    if 'RANK' in os.environ and 'WORLD_SIZE' in os.environ:
        rank = int(os.environ['RANK'])
        world_size = int(os.environ['WORLD_SIZE'])
        local_rank = int(os.environ.get('LOCAL_RANK', 0))
    else:
        rank = 0; world_size = 1; local_rank = 0
    if world_size > 1:
        if not dist.is_initialized():
            dist.init_process_group(backend='nccl', rank=rank, world_size=world_size)
    if torch.cuda.is_available():
        device = torch.device(f'cuda:{local_rank}')
        torch.cuda.set_device(device)
    return rank, world_size, device
```

## Distributed Checkpointing

FSDP integrates with PyTorch’s distributed checkpoint API (`torch.distributed.checkpoint`). An `AppState` wrapper class that implements the `Stateful` protocol manages model and optimizer state dicts. The `get_state_dict()` and `set_state_dict()` functions automatically handle FSDP’s sharded state dict format, defaulting to `SHARDED_STATE_DICT`. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
from torch.distributed.checkpoint.stateful import Stateful
from torch.distributed.checkpoint.state_dict import get_state_dict, set_state_dict

class AppState(Stateful):
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer

    def state_dict(self):
        model_state_dict, optimizer_state_dict = get_state_dict(self.model, self.optimizer)
        return {"model": model_state_dict, "optim": optimizer_state_dict}

    def load_state_dict(self, state_dict):
        set_state_dict(
            self.model,
            self.optimizer,
            model_state_dict=state_dict["model"],
            optim_state_dict=state_dict["optim"]
        )
```

Checkpoints are saved using `dcp.save()` with a `StorageWriter` (e.g., `FileSystemWriter`) to a storage path such as a [Unity Catalog](/concepts/unity-catalog.md) volume. When loading a checkpoint outside a distributed context (no process group initialized), PyTorch automatically disables collective operations and loads the checkpoint on a single device. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Usage Patterns

### Single‑Node Multi‑GPU Training

The most common pattern is training across multiple GPUs on one node. On [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) on Databricks, the `@distributed` decorator provisions the specified number of GPUs and sets up the distributed environment automatically. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu.compute import GPUType

@distributed(gpus=8, gpu_type=GPUType.H100)
def run_fsdp_training():
    # Training logic using FSDP
    pass
```

Inside the decorated function, the model is created, moved to the device, wrapped with FSDP if `world_size > 1`, and trained using a `DistributedSampler` to split the dataset across workers. Training metrics (loss) are logged to [MLflow](/concepts/mlflow.md), and checkpoints are saved periodically to a Unity Catalog volume. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Multi‑Node Distributed Training

While the provided source focuses on single‑node training with 8 H100 GPUs, FSDP can also be used in multi‑node configurations. In such setups, `torchrun` or similar launchers are used, and checkpoints are often stored in a Unity Catalog volume while training is tracked with MLflow. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
