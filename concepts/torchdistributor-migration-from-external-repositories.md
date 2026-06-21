---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 108cd34463813f1e85818d5282ea6cb7059b267126d4810c99b88eabe9b3f4f0
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-migration-from-external-repositories
    - TMFER
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: TorchDistributor Migration from External Repositories
description: Process to migrate existing distributed PyTorch training code from external repositories to Databricks using Git folders and TorchDistributor.run(train_file).
tags:
  - migration
  - databricks
  - distributed-training
timestamp: "2026-06-18T12:09:41.299Z"
---

# TorchDistributor Migration from External Repositories

**TorchDistributor Migration from External Repositories** is a process for moving existing distributed training procedures stored in external code repositories (such as GitHub, GitLab, or Bitbucket) to Databricks, where they can run using the [TorchDistributor](/concepts/torchdistributor.md) module in PySpark. This migration approach allows teams to leverage their existing training scripts while taking advantage of Databricks' managed Spark clusters and GPU infrastructure. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Overview

TorchDistributor is an open-source module in PySpark that enables distributed training with PyTorch on Spark clusters. When you have an existing distributed training pipeline stored in an external repository, you can bring it to Databricks with minimal code changes. The module initializes the environment and communication channels between workers, using the CLI command `torch.distributed.run` to execute distributed training across worker nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Migration Process

The migration process consists of three main steps: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 1: Import the Repository

Import the external repository as a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md) (formerly called Repos). This brings your existing training code into the Databricks environment while maintaining version control and collaboration features. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 2: Create a New Notebook

Initialize a new Databricks Notebook within the imported repository. This notebook will serve as the launcher for your distributed training job, calling the TorchDistributor with the path to your training script. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Step 3: Launch Distributed Training

In a notebook cell, instantiate the `TorchDistributor` with your desired configuration and call the `.run()` method, passing the file path to your training script and any command-line arguments. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Code Example

The following example demonstrates how to launch a distributed training job from an external training script: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
from pyspark.ml.torch.distributor import TorchDistributor

train_file = "/path/to/train.py"
args = ["--learning_rate=0.001", "--batch_size=16"]

distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train_file, *args)
```

## Requirements

- Apache Spark 3.4 or above
- Databricks Runtime 13.0 ML or above ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Key Differences from Notebook Workflow

When migrating from an external repository, as opposed to developing entirely within a notebook, you do not need to place import statements inside a training function to avoid pickling errors. Instead, you maintain your existing script structure and pass the file path directly to `TorchDistributor.run()`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting During Migration

### Common Issues

If your training script relies on dependencies not available in the default Databricks Runtime ML environment, you may need to install additional libraries using [cluster library installation](/concepts/manual-library-installation-on-databricks.md) or init scripts. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### CUDA Peer Access Error

On AWS G5 GPU instances, you may encounter CUDA errors about unsupported peer access between devices. Add the following to your training script: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

### NCCL Communication Error

For multi-node training, network communication issues may arise. To resolve: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

### Gloo Connection Error

For CPU-based distributed training using Gloo backend: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

## Use Cases

Common scenarios for migrating distributed training from external repositories include:

- Moving existing PyTorch training pipelines from on-premises or other cloud environments to Databricks
- Integrating training scripts that use [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), Hugging Face Transformers, or other PyTorch-based frameworks
- Transitioning from manual cluster management to Databricks' managed Spark infrastructure

## Best Practices

- **Test single-node first.** Before migrating to distributed training, verify that your training script runs correctly on a single node within Databricks.
- **Use environment variables for configuration.** Pass hyperparameters and configuration via command-line arguments rather than hardcoding them in your script.
- **Version control your code.** Keep your training scripts in [Databricks Git folders](/concepts/databricks-git-folders-for-cicd.md) to maintain a record of changes and enable collaboration.
- **Select appropriate GPU instances.** Choose Databricks Runtime ML clusters with GPU instances that match your training requirements, ensuring peer-to-peer GPU communication support.

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — The PySpark module for distributed PyTorch training
- [Distributed PyTorch Training](/concepts/distributed-pytorch-training-on-databricks.md) — General concepts for multi-node PyTorch training
- [Databricks Git Folders](/concepts/databricks-git-folders-for-cicd.md) — Repository integration for version-controlled code
- Databricks Notebooks — Interactive development environment for launching training jobs
- Cluster Configuration for Distributed Training — Setting up compute resources for distributed workloads
- [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The underlying PyTorch paradigm used by TorchDistributor

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
