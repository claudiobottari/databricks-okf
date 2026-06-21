---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c530d42a903021bc54b9edf9f63c12cacc25f2548ddd2d37b23826c87c00e28b
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-workflow-for-notebooks
    - DTWFN
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Distributed Training Workflow for Notebooks
description: A four-step workflow to convert single-node PyTorch training code for distributed execution using TorchDistributor on Databricks
tags:
  - workflow
  - pytorch
  - databricks
timestamp: "2026-06-19T18:39:11.804Z"
---

---

## Distributed Training Workflow for Notebooks

The **Distributed Training Workflow for Notebooks** describes the process for converting a single-node PyTorch training script into a distributed training job that runs on a Spark cluster via [TorchDistributor](/concepts/torchdistributor.md). This workflow is intended for users whose model development and training happen entirely within a notebook environment, such as a local Jupyter notebook or a Databricks Notebook.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Workflow Steps

1. **Prepare single-node code:** First, develop and test a single-node training script using PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), or higher-level APIs that build on them (such as the [Hugging Face](/concepts/hugging-face-trainer.md) Trainer API). This step verifies that the core model logic and data pipeline work correctly on one process.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

2. **Convert to standard distributed training:** Refactor the single-process code into a distributed training function. Follow the [standard PyTorch DDP tutorial](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html) to set up [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), a distributed sampler, and a distributed DataLoader. All of this distributed logic must be contained within one training function that can be passed to `TorchDistributor`.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

3. **Move imports inside the training function:** Place all necessary import statements (for example, `import torch`, `import torch.distributed`) **inside** the training function. This placement avoids common pickling errors that occur when Spark tries to serialize imported modules that are not available on the executors.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

    The device ID for each process is typically derived from an environment variable, set within the training function:
    
    ```python
    device_id = int(os.environ["LOCAL_RANK"])
    ```
    
    ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

4. **Launch distributed training:** Instantiate a `TorchDistributor` object with the desired parameters (e.g., `num_processes`, `use_gpu`) and call its `.run()` method, passing the training function and its arguments.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

    **Example:**
    
    ```python
    from pyspark.ml.torch.distributor import TorchDistributor
    
    def train(learning_rate, use_gpu):
        # ... distributed training code ...
        return output
    
    distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
    distributor.run(train, 1e-3, True)
    ```
    
    ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Migrating from External Repositories

If you already have a distributed training script in an external repository, you can migrate it to a Databricks notebook with a similar workflow:^[distributed-training-with-torchdistributor-databricks-on-aws.md]

1. Import the external repository as a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md).^[distributed-training-with-torchdistributor-databricks-on-aws.md]
2. Create a new notebook inside that folder.^[distributed-training-with-torchdistributor-databricks-on-aws.md]
3. Call `TorchDistributor.run()` with the path to the training file and any command-line arguments:^[distributed-training-with-torchdistributor-databricks-on-aws.md]

    ```python
    from pyspark.ml.torch.distributor import TorchDistributor
    
    train_file = "/path/to/train.py"
    args = ["--learning_rate=0.001", "--batch_size=16"]
    distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
    distributor.run(train_file, *args)
    ```
    
    ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Troubleshooting

#### Pickling errors

To avoid pickling errors when objects cannot be found on distributed executors, include all import statements (for example, `import torch`) **both** at the top of the training function passed to `run()` and inside any other user-defined functions that the training method calls.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

#### CUDA peer access errors on G5 GPUs

On AWS G5 GPU instances, you may encounter `peer access is not supported between these two devices`. Set the environment variable `NCCL_P2P_DISABLE = "1"` inside the training function to disable peer-to-peer access.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

#### NCCL internal error during multi-node training

A `ncclInternalError` during multi-node training usually indicates a network communication failure between GPUs. Set the environment variable `NCCL_SOCKET_IFNAME = "eth0"` to force NCCL to use the primary network interface.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

#### Gloo connection refused on CPU instances

When using Gloo for CPU-based distributed training, set `GLOO_SOCKET_IFNAME = "eth0"` to avoid a `Connection refused` error.^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Requirements

- Spark 3.4
- Databricks Runtime 13.0 ML or above

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The PySpark module that orchestrates the distributed training job.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – The standard PyTorch parallelism strategy used inside the training function.
- PySpark ML – The machine learning library that provides `TorchDistributor`.
- Hugging Face Transformers – A higher-level API that builds on PyTorch and is commonly fine-tuned with this workflow.

### Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
