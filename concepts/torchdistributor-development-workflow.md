---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df4547ee863418127063b1f58fbd034deb6f21fca37cc1e5addd7cd246c91c0a
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-development-workflow
    - TDW
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: TorchDistributor Development Workflow
description: "A four-step workflow for converting single-node PyTorch training to distributed training using TorchDistributor: prepare single-node code, convert to distributed, move imports inside training function, and launch with distributor.run()."
tags:
  - workflow
  - distributed-training
  - pyspark
timestamp: "2026-06-18T12:09:08.714Z"
---

# TorchDistributor Development Workflow

**TorchDistributor Development Workflow** describes the process of adapting PyTorch training code to run in a distributed manner using the [TorchDistributor](/concepts/torchdistributor.md) module in PySpark. TorchDistributor is an open-source module that enables distributed training with PyTorch on Spark clusters by initializing the environment and communication channels between workers and utilizing the CLI command `torch.distributed.run` to execute training across worker nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Requirements

To use TorchDistributor, you need Spark 3.4 and Databricks Runtime 13.0 ML or above. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Development Workflow for Notebooks

If the model creation and training process happens entirely from a notebook on your local machine or a Databricks Notebook, you only need to make minor changes to prepare your code for distributed training. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 1: Prepare Single Node Code

Prepare and test the single node code with PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), or other frameworks based on PyTorch/PyTorch Lightning, such as the [HuggingFace Trainer API](/concepts/hugging-face-trainer.md). ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 2: Prepare Code for Standard Distributed Training

Convert your single process training to distributed training following the [PyTorch DDP tutorial](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html). Encompass all distributed code within one training function that you can use with the `TorchDistributor`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 3: Move Imports Within Training Function

Add necessary imports, such as `import torch`, within the training function to avoid common pickling errors. The `device_id` that models and data are tied to is determined by: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
device_id = int(os.environ["LOCAL_RANK"])
```

### Step 4: Launch Distributed Training

Instantiate the `TorchDistributor` with the desired parameters and call `.run(*args)` to launch training. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Training Code Example

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

distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train, 1e-3, True)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Migrate Training from External Repositories

If you have an existing distributed training procedure stored in an external repository, you can migrate to Databricks by following these steps: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

1. **Import the repository:** Import the external repository as a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md).
2. **Create a new notebook:** Initialize a new Databricks Notebook within the repository.
3. **Launch distributed training:** In a notebook cell, call `TorchDistributor` as shown below:

```python
from pyspark.ml.torch.distributor import TorchDistributor

train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]
distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train_file, *args)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting

### Pickling Errors

A common error for the notebook workflow is that objects cannot be found or pickled when running distributed training. This can happen when library import statements are not distributed to other executors. To avoid this issue, include all import statements (for example, `import torch`) both at the top of the training function called with `TorchDistributor(...).run(<func>)` and inside any other user-defined functions called in the training method. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### CUDA Failure: Peer Access Not Supported

This is a potential error on the G5 suite of GPUs on AWS. To resolve this error, add the following snippet in your training code: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

### NCCL Failure: Internal Check Failed

When you encounter this error during multi-node training, it typically indicates a problem with network communication among GPUs. This issue arises when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. To resolve this error, add the following snippet in your training code to use the primary network interface: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

### Gloo Failure: Connection Refused

You may potentially run into this error when using Gloo for distributed training on CPU instances. To resolve this error, add the following snippet in your training code: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

## Related Concepts

- [TorchDistributor API](/concepts/torchdistributor-api-methods.md) — The API reference for TorchDistributor methods and parameters
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — PyTorch's distributed training paradigm
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) — A lightweight PyTorch wrapper for distributed training
- [HuggingFace Trainer API](/concepts/hugging-face-trainer.md) — A high-level API for training HuggingFace models
- [Databricks Git Folders](/concepts/databricks-git-folders-for-cicd.md) — For importing external repositories
- Spark Clusters — The compute environment for distributed training

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
