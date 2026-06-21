---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b962305991e1a7e77c381edcea08e91214a00e1d2c713b4bb674ab0850c0a4f9
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-distributed-training-api
    - SGDTA
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: Serverless GPU Distributed Training API
description: A Databricks API using the @distributed decorator that handles provisioning GPUs, setting up the distributed environment, and managing the lifecycle of remote compute resources for multi-GPU training.
tags:
  - databricks
  - api
  - distributed-training
timestamp: "2026-06-19T18:36:26.380Z"
---

---
title: Serverless GPU Distributed Training API
summary: Databricks’ `@distributed` decorator that handles provisioning GPUs, setting up the distributed training environment, and managing the lifecycle of remote compute resources for multi-GPU training.
sources:
  - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - databricks
  - distributed-training
  - api
  - serverless-gpu
aliases:
  - serverless-gpu-distributed-training-api
  - distributed decorator
  - distributed() method
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Serverless GPU Distributed Training API

The **Serverless GPU Distributed Training API** is a Databricks API that enables you to run multi‑GPU distributed training jobs on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) without manually managing cluster infrastructure. It is exposed through the `serverless_gpu` Python package and provides a `@distributed` decorator and a `.distributed()` method to orchestrate remote execution. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## How It Works

The API is designed to work with popular distributed training frameworks like [PyTorch FSDP](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md). A training function is decorated with `@distributed` to indicate that it should run on serverless GPU compute. The API handles:

- **GPU provisioning** – Allocates the requested number and type of GPUs (e.g., 8x H100).
- **Environment setup** – Initializes the distributed process group, sets environment variables (`RANK`, `WORLD_SIZE`, `LOCAL_RANK`), and configures the NCCL backend.
- **Lifecycle management** – Provisions compute resources, executes the training function, and tears down resources after completion. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

The training function is defined inside a decorated wrapper and can access the distributed environment as usual (e.g., via `os.environ` or `torch.distributed`). A companion `.distributed()` method on the wrapped function triggers remote execution. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Usage Example

The following example from the Databricks tutorial trains a Transformer model on 8 H100 GPUs using FSDP:

```python
from serverless_gpu import distributed
from serverless_gpu.compute import GPUType

NUM_WORKERS = 8

@distributed(gpus=NUM_WORKERS, gpu_type=GPUType.H100)
def run_fsdp_training(num_workers=NUM_WORKERS):
    # ... training code using FSDP, MLflow, etc. ...
    pass

# Trigger remote execution
result = run_fsdp_training.distributed()
```

The API also requires the notebook to be attached to a serverless GPU compute instance. Before calling the API, you must select the appropriate accelerator (e.g., **8xH100**) and environment (e.g., **AI v5**) through the notebook’s compute selector. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Key Features

- **No cluster management** – GPUs are provisioned automatically; no need to start or scale clusters manually.
- **Framework agnostic** – Works with any PyTorch distributed strategy (FSDP, DDP, etc.) and can be adapted to other frameworks.
- **MLflow integration** – Training metrics and artifacts can be logged to MLflow inside the distributed function and are automatically tracked.
- **Checkpoint support** – Models can save distributed checkpoints to Unity Catalog volumes during training. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Limitations and Considerations

- The API is designed for serverless GPU compute, which has specific availability and configuration constraints (e.g., GPU types may vary by cloud region).
- The training function must be self‑contained and importable; external data sources should be accessible from the serverless environment.
- Distributed process group initialization is handled by the API, but users are responsible for calling `torch.distributed.init_process_group` if needed (the example uses a conditional check). ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Multi-GPU and multi-node distributed training](/concepts/multi-gpu-distributed-training-api.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
