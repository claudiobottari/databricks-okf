---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a172581c407ee06f0bcba8f8cff131cb35ba04125d3404e2dd42465ec6a7840d
  pageDirectory: concepts
  sources:
    - pytorch-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-pytorch-training-on-databricks
    - DPTOD
    - Distributed PyTorch Training
  citations:
    - file: pytorch-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Distributed PyTorch Training on Databricks
description: Approaches and best practices for running distributed PyTorch training workloads on Databricks clusters
tags:
  - distributed-training
  - pytorch
  - databricks
timestamp: "2026-06-19T20:00:33.148Z"
---

# Distributed PyTorch Training on Databricks

**Distributed PyTorch Training on Databricks** refers to the set of tools, APIs, and best practices for scaling PyTorch workloads across multiple GPUs and nodes on the Databricks platform. PyTorch is included in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md), which provides a pre-configured environment for deep learning, and can also be installed on standard Databricks Runtime via PyPI libraries. ^[pytorch-databricks-on-aws.md]

Databricks supports several distributed training strategies for PyTorch, from simple multi‑GPU parallelism on a single node to full sharded data parallelism for models with billions of parameters. The choice of strategy depends on model size, available hardware, and memory constraints. ^[pytorch-databricks-on-aws.md, fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Distributed Training Options

### TorchDistributor (Recommended for Standard PyTorch Workloads)

For PyTorch workloads that rely on `torch.nn.DataParallel` or `torch.nn.parallel.DistributedDataParallel`, Databricks provides the **TorchDistributor** API (`pyspark.ml.torch.distributor.TorchDistributor`). This utility simplifies launching distributed training across a cluster without manually managing process groups or environment variables. ^[pytorch-databricks-on-aws.md]

Example usage:

```python
from pyspark.ml.torch.distributor import TorchDistributor

def train_fn(learning_rate):
    # ...

num_processes = 2
distributor = TorchDistributor(num_processes=num_processes, local_mode=True)
distributor.run(train_fn, 1e-3)
```

`TorchDistributor` is available in Databricks Runtime ML 13.0 and above. ^[pytorch-databricks-on-aws.md]

### Fully Sharded Data Parallel (FSDP)

For training large models (20B to 120B+ parameters), Databricks recommends [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/fsdp-fully-sharded-data-parallel.md). FSDP shards model parameters, gradients, and optimizer states across GPUs, drastically reducing per‑GPU memory usage. This enables training models that would otherwise exceed single‑GPU memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

FSDP is preferred over standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) for models that do not fit in a single GPU. For even more advanced memory optimization, practitioners may use [DeepSpeed](/concepts/deepspeed.md) as an alternative. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Multi‑Node Training with Serverless GPU

Databricks Serverless GPU compute provides configurations such as the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md), which provisions eight H100 GPUs on one node. For larger workloads, multiple nodes can be coordinated using TorchDistributor or FSDP. The `@distributed` decorator from the `serverless_gpu` library can also be used to run arbitrary Python functions across GPUs within a single node. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Installation

**Databricks Runtime ML** includes PyTorch and `torchvision`. To find the exact version, consult the Databricks Runtime Release Notes. ^[pytorch-databricks-on-aws.md]

If using the standard Databricks Runtime, install PyTorch as a PyPI library:

- On GPU clusters: `torch==1.5.0`, `torchvision==0.6.0`
- On CPU clusters: use CPU‑specific wheel files from PyTorch’s download site.

Databricks recommends using Databricks Runtime ML to avoid manual installation. ^[pytorch-databricks-on-aws.md]

## Example Notebooks

Databricks provides example notebooks for PyTorch distributed training, including:
- MLflow PyTorch end‑to‑end model training
- Basic PyTorch notebook
- MLflow PyTorch with TensorFlow

These notebooks are linked from the [PyTorch on Databricks](/concepts/pytorch-on-databricks.md) documentation. ^[pytorch-databricks-on-aws.md]

## Troubleshooting Common Errors

### “process 0 terminated with exit code 1”

This error can occur when using notebooks or scripts that call `torch.multiprocessing.spawn`. The workaround is to use `torch.multiprocessing.start_processes` with `start_method="fork"`:

```python
torch.multiprocessing.start_processes(
    train_fn, args=(1e-3,), nprocs=num_processes, start_method="fork"
)
```

Be aware that `fork` is not CUDA‑compatible – calling `.cuda()` before launching processes can cause failures. Add a guard to detect CUDA initialization before spawning. ^[pytorch-databricks-on-aws.md]

### “The server socket has failed to bind to port”

This error appears when restarting distributed training after interrupting a cell, because the port remains in use. Restart the cluster. If the problem persists, check for code errors in the training function. ^[pytorch-databricks-on-aws.md]

## Related Concepts

- [PyTorch on Databricks](/concepts/pytorch-on-databricks.md)
- [TorchDistributor](/concepts/torchdistributor.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

## Sources

- pytorch-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [pytorch-databricks-on-aws.md](/references/pytorch-databricks-on-aws-b092c491.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
