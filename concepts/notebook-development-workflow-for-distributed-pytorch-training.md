---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 244ffa9963c8b10558427b269f030bf5c915ace8c35772bd70e7ca69582ae41b
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - notebook-development-workflow-for-distributed-pytorch-training
    - NDWFDPT
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Notebook Development Workflow for Distributed PyTorch Training
description: A four-step workflow to convert single-node PyTorch code to distributed training using TorchDistributor in notebooks
tags:
  - pytorch
  - distributed-training
  - workflow
  - databricks
timestamp: "2026-06-18T15:34:46.029Z"
---

# Notebook Development Workflow for Distributed PyTorch Training

**Notebook Development Workflow for Distributed PyTorch Training** describes the process of adapting single‑node PyTorch training code to run in a distributed fashion using [TorchDistributor](/concepts/torchdistributor.md) directly from a notebook environment — either a local machine or a Databricks Notebook. The workflow requires only minor changes to existing single‑node code and leverages PySpark’s `TorchDistributor` module to launch `torch.distributed.run` across worker nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Requirements

- Spark 3.4
- Databricks Runtime 13.0 ML or above ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Workflow Steps

The notebook development workflow consists of four steps:

### 1. Prepare single‑node code

Write and test the training code using PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), or frameworks built on them (for example, the [HuggingFace Trainer API](/concepts/hugging-face-trainer.md)). This code should run correctly on a single GPU or CPU before distribution. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### 2. Prepare code for standard distributed training

Convert the single‑process training to distributed training by following the [PyTorch DDP tutorial](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html). The resulting distributed code must be encapsulated in a single training function that can be passed to `TorchDistributor`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### 3. Move imports within the training function

To avoid common pickling errors, place all necessary imports (e.g., `import torch`) **inside** the training function rather than at the top of the notebook cell. The device ID that models and data are bound to is determined by:

```python
device_id = int(os.environ["LOCAL_RANK"])
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### 4. Launch distributed training

Instantiate the `TorchDistributor` with the desired parameters (number of processes, local mode flag, GPU usage) and call `.run(*args)` to start training. Example:

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

## Migrating Training from External Repositories

If existing distributed training code lives in an external repository, migration to Databricks involves:

1. **Import the repository** as a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md).
2. **Create a new notebook** inside that repository.
3. **Launch distributed training** by calling `TorchDistributor` with the path to the training script and any arguments:

```python
from pyspark.ml.torch.distributor import TorchDistributor

train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]
distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train_file, *args)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting

### Pickling errors

If library import statements are not distributed to other executors, objects cannot be pickled. To avoid this, include all import statements **both** at the top of the training function passed to `TorchDistributor` **and** inside any other user‑defined functions called by that training method. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### CUDA failure: peer access not supported (G5 GPUs on AWS)

Add the following environment variable:

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### NCCL failure: internal check failed (multi‑node)

Set the primary network interface:

```python
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Gloo failure: connection refused (CPU instances)

Set the Gloo socket interface:

```python
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Example Notebooks

The source material references several example notebooks that demonstrate the workflow:

- End‑to‑end distributed training on a Databricks notebook
- Distributed fine‑tuning a Hugging Face model
- Distributed training using a PyTorch file
- Distributed training using PyTorch Lightning

These are not reproduced here but are linked in the official documentation. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The PySpark module used to launch distributed PyTorch jobs.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – PyTorch’s standard distributed training paradigm.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime version that supports this workflow.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – A framework that can be used in the single‑node preparation step.
- [HuggingFace Trainer API](/concepts/hugging-face-trainer.md) – Another framework that works with this workflow.

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
