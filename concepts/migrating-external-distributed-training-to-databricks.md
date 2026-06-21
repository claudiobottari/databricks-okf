---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62ce1f5d7f92fa092713230e2be5fcef9fdd97df7349e80a6ab139eb01234120
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migrating-external-distributed-training-to-databricks
    - MEDTTD
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Migrating External Distributed Training to Databricks
description: Process to import an external training repository as a Databricks Git folder and launch distributed training via TorchDistributor
tags:
  - databricks
  - migration
  - distributed-training
  - git
timestamp: "2026-06-18T15:35:03.543Z"
---



# Migrating External Distributed Training to Databricks

**Migrating External Distributed Training to Databricks** is the process of taking an existing distributed training workflow, typically stored in an external Git repository, and adapting it to run within the Databricks environment using [TorchDistributor](/concepts/torchdistributor.md) (part of PySpark ML).

## Overview

If you have an existing distributed training procedure stored in an external repository (such as a Python script with PyTorch distributed code), you can migrate it to Databricks by importing the repository as a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md), creating a new notebook, and launching training via `TorchDistributor`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Migration Steps

### 1. Import the repository

Import the external repository as a Databricks Git folder. This brings your code and version history directly into the workspace. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### 2. Create a new notebook

Initialize a new Databricks Notebook within the repository. The notebook will contain the `TorchDistributor` call. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### 3. Launch distributed training

In a notebook cell, instantiate `TorchDistributor` with the desired parameters and call `.run()` on the training script file and its arguments: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
from pyspark.ml.torch.distributor import TorchDistributor

train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]
distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train_file, *args)
```

Under the hood, `TorchDistributor` initializes the environment and communication channels between workers and uses the CLI command `torch.distributed.run` to run distributed training across the worker nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Requirements

- **Spark 3.4** ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- **Databricks Runtime 13.0 ML or above** ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Alternative Workflow: Notebook-Based Development

If model creation and training happens entirely from a notebook (e.g., local machine or Databricks Notebook), the migration steps differ slightly. You must: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

1. **Prepare single node code** – Test training with PyTorch, PyTorch Lightning, or frameworks like the HuggingFace Trainer API. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
2. **Convert to standard distributed training** – [Convert single process to distributed training](/concepts/adapting-single-node-pytorch-to-distributed-training.md) so all code is within one training function. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
3. **Move imports within the training function** – Add necessary imports (e.g., `import torch`) inside the function to avoid pickling errors. The `device_id` is determined by `int(os.environ["LOCAL_RANK"])`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
4. **Launch with `TorchDistributor`** – Instantiate and call `.run()`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting Common Errors

### Missing objects or pickling errors

Library import statements may not be distributed to other executors. To fix this, include all imports (e.g., `import torch`) both at the top of the training function and inside any other user-defined functions called in the training method. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### CUDA: `peer access is not supported between these two devices`

This error can occur on the G5 GPU suite on AWS. Set the environment variable `NCCL_P2P_DISABLE=1`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### NCCL: `ncclInternalError: Internal check failed`

Indicates a network communication problem among GPUs during multi-node training. Set `NCCL_SOCKET_IFNAME="eth0"` to use the primary network interface. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Gloo: `RuntimeError: Connection refused`

May occur when using Gloo on CPU instances. Set `GLOO_SOCKET_IFNAME="eth0"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor API](/concepts/torchdistributor-api-methods.md)
- [Databricks Git folders](/concepts/databricks-git-folders-for-cicd.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- [HuggingFace Trainer API](/concepts/hugging-face-trainer.md)
- GPU scheduling

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
