---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d6d590b96c2eba6830d14b629b0c33b290ecdc8f739cf3815c5697dc20cbb53
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-development-workflow
    - DTDW
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Distributed Training Development Workflow
description: A four-step process for converting single-node PyTorch code to distributed training using TorchDistributor on Databricks notebooks.
tags:
  - workflow
  - pytorch
  - distributed-training
timestamp: "2026-06-19T10:20:54.175Z"
---

# Distributed Training Development Workflow

**Distributed Training Development Workflow** refers to the process of adapting single-node training code to run across multiple GPUs or nodes in a distributed environment. This workflow is essential for training large models that exceed the memory capacity of a single GPU or for accelerating training time through parallelism.

## Overview

Distributed training workflows typically follow a structured progression from single-node development to multi-node distributed execution. The general approach involves preparing and testing code locally, converting it for distributed execution, and then launching the training across worker nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Development Workflow for Notebooks

When model creation and training happen entirely from a notebook environment, only minor changes are needed to adapt code for distributed training. The following steps outline a typical workflow: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 1: Prepare Single Node Code

Begin by preparing and testing single-node code with PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), or other frameworks based on these libraries, such as the [HuggingFace Trainer API](/concepts/hugging-face-trainer.md). This step ensures the model architecture, data pipeline, and training loop work correctly on a single worker before scaling out. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 2: Convert to Standard Distributed Training

Convert the single-process training code to distributed training using standard approaches such as [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md). The distributed code should be encapsulated within a single training function that can be called by the distributed launcher. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 3: Move Imports Within the Training Function

Place all necessary imports (e.g., `import torch`) inside the training function rather than at the module level. This practice helps avoid common pickling errors when the function is serialized and distributed to worker nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

The device ID that models and data should be tied to is determined using:

```python
device_id = int(os.environ["LOCAL_RANK"])
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 4: Launch Distributed Training

Instantiate a distributed training launcher (such as [TorchDistributor](/concepts/torchdistributor.md)) with the desired parameters and call its run method to begin training. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

#### Example: TorchDistributor Workflow

```python
from pyspark.ml.torch.distributor import TorchDistributor

def train(learning_rate, use_gpu):
    import torch
    import torch.distributed as dist
    import torch.nn.parallel.DistributedDataParallel as DDP
    from torch.utils.data import DistributedSampler, DataLoader

    backend = "nccl" if use_gpu else "gloo"
    dist.init_process_group(backend)
    device = int(os.environ["LOCAL_RANK"]) if use_gpu else "cpu"
    model = DDP(createModel(), **kwargs)
    sampler = DistributedSampler(dataset)
    loader = DataLoader(dataset, sampler=sampler)
    output = train(model, loader, learning_rate)
    dist.cleanup()
    return output

distributor = TorchDistributor(
    num_processes=2,
    local_mode=False,
    use_gpu=True
)
distributor.run(train, 1e-3, True)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Migrating Training from External Repositories

For existing distributed training procedures stored in external repositories, the migration workflow includes: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

1. **Import the repository** as a [Git folder](/concepts/databricks-git-folders-for-cicd.md) in the platform.
2. **Create a new notebook** within the repository.
3. **Launch distributed training** by calling the distributed launcher with the training script path.

```python
from pyspark.ml.torch.distributor import TorchDistributor

train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]
distributor = TorchDistributor(
    num_processes=2,
    local_mode=False,
    use_gpu=True
)
distributor.run(train_file, *args)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Common Troubleshooting Issues

### Pickling Errors

If objects cannot be found or pickled during distributed training, include all import statements both at the top of the training function and inside any other user-defined functions called within the training method. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### CUDA Peer Access Errors

On certain GPU instances (such as the G5 suite on AWS), peer access between devices may not be supported. Resolve by setting: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

### NCCL Communication Errors

For multi-node training errors related to network communication, NCCL may not be able to use certain network interfaces. Set the environment variable to use the primary network interface: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

### Gloo Connection Errors

On CPU instances using Gloo for distributed training, connection refusal errors can occur. Resolve by configuring the Gloo socket interface: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

## Requirements

The notebook-based distributed training workflow using TorchDistributor requires: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

- Spark 3.4
- Databricks Runtime 13.0 ML or above

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — The PySpark module for launching PyTorch distributed training on Spark clusters
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The standard PyTorch approach for distributed training
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — An alternative approach for memory-constrained models
- [DeepSpeed](/concepts/deepspeed.md) — A deep learning optimization library with additional distributed training features
- GPU Scheduling — Optimizing GPU utilization for distributed workflows
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — The parameter range where advanced distributed strategies become necessary

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
