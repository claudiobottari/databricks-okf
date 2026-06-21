---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b243c82e1f117947eab7f0387c093c62dbb164d53afe4dae2d2b109ea91eb0c
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-for-distributed-training
    - DRMFDT
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Databricks Runtime ML for Distributed Training
description: Databricks Runtime 13.0 ML or above as the required environment for running TorchDistributor with Spark 3.4
tags:
  - databricks
  - requirements
  - ml-runtime
timestamp: "2026-06-19T18:39:27.495Z"
---

# Databricks Runtime ML for Distributed Training

**Databricks Runtime ML for Distributed Training** is a specialized runtime environment on Databricks that includes pre-configured libraries and tools for scaling machine learning workloads across multiple GPUs and nodes. It simplifies the process of training large models by providing integrated support for distributed computing frameworks such as PyTorch, TensorFlow, and Spark.

## Overview

Databricks Runtime ML is built on top of Databricks Runtime and includes additional ML libraries, including PyTorch, TensorFlow, Scikit-learn, [XGBoost](/concepts/xgboostspark-module.md), and [Spark MLlib](/concepts/apache-spark-mllib.md). For distributed training, it provides native integration with [TorchDistributor](/concepts/torchdistributor.md), which allows users to launch PyTorch training jobs as Spark jobs across a cluster. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Key Features for Distributed Training

### TorchDistributor Integration

TorchDistributor is an open-source module in PySpark (`pyspark.ml.torch.distributor`) that enables distributed training with PyTorch on Spark clusters. Under the hood, it initializes the environment and communication channels between workers and uses the CLI command `torch.distributed.run` to execute distributed training across worker nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Requirements

- Spark 3.4 or later
- Databricks Runtime 13.0 ML or above

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Development Workflow

When using Databricks Runtime ML for distributed training from a notebook, the typical workflow involves four steps:

1. **Prepare single-node code**: Develop and test training code with PyTorch, PyTorch Lightning, or frameworks based on them (such as the HuggingFace Trainer API).
2. **Convert to distributed training**: Adapt the code for standard distributed training using PyTorch's [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) or [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). Encompass all distributed code within a single training function.
3. **Move imports inside the training function**: Place necessary library imports (e.g., `import torch`) within the training function to avoid common pickling errors. Use `int(os.environ["LOCAL_RANK"])` to determine the device ID.
4. **Launch distributed training**: Instantiate `TorchDistributor` with desired parameters and call `.run(*args)` to start training.

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

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

## Migrating Training from External Repositories

To migrate an existing distributed training procedure to Databricks Runtime ML:

1. Import the external repository as a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md).
2. Create a new notebook within the repository.
3. Launch distributed training using `TorchDistributor` with a training file path:

```python
from pyspark.ml.torch.distributor import TorchDistributor

train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]
distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train_file, *args)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting Common Issues

### Pickling Errors

If objects cannot be found or pickled during distributed training, include all import statements (e.g., `import torch`) both at the top of the training function called with `TorchDistributor` and inside any other user-defined functions called within the training method. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### CUDA Peer Access Failure

On AWS G5 GPU instances, you may encounter `peer access is not supported between these two devices`. Add the following environment variable:

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### NCCL Internal Check Failed

For multi-node training, NCCL communication errors can arise when NCCL cannot use certain network interfaces. Configure the primary network interface:

```python
import os
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Gloo Connection Refused

When using Gloo for distributed training on CPU instances:

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Serverless GPU Support

Databricks Runtime ML also supports [Serverless GPU Compute](/concepts/serverless-gpu-compute.md), including configurations like [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) with eight NVIDIA H100 80GB GPUs. The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs on a single node, with `runtime` module access to local and global GPU ranks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Large Language Model (LLM) Training
- [HuggingFace Transformers](/concepts/hugging-face-transformers-trainer.md)
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
