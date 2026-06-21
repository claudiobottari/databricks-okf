---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c113164590d1c5a2b16d9378a03ddb1eb3d9772e641635b8b96df468670f1dc
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-distributed-decorator-for-multi-gpu-training
    - D@DFMT
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: Databricks @distributed Decorator for Multi-GPU Training
description: A decorator-based API in Databricks Serverless GPU Compute that automatically orchestrates distributed training across multiple GPUs, handling provisioning, data distribution, and synchronization.
tags:
  - databricks
  - distributed-training
  - multi-gpu
  - orchestration
timestamp: "2026-06-19T15:14:07.812Z"
---

## Databricks `@distributed` Decorator for Multi-GPU Training

The **`@distributed` decorator** is a function-level annotation provided by the `serverless_gpu` Python library on Databricks. It allows a Python function to be executed across multiple GPUs on a single node, handling provisioning, data distribution, and result collection automatically.

### Overview

The decorator is imported from the `serverless_gpu` module and supports optional parameters to specify the number of GPUs and their type. When applied to a function, the function can then be called via a `.distributed()` method, which launches the function across the requested GPU resources.^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Usage

The following example (adapted from a fine-tuning notebook) shows the typical pattern: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type="H100")
def run_train(use_lora=True):
    # Training code
    # Can use rt.get_local_rank() and rt.get_global_rank()
    return mlflow_run_id

result = run_train.distributed(use_lora=True)[0]
```

### Parameters

- **`gpus`** – number of GPU processes to start (one per GPU). In the example, `8` GPUs are requested on a single node. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **`gpu_type`** – the type of GPU to use (e.g., `"H100"`). This determines which GPU hardware is provisioned. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Runtime Module

The `serverless_gpu.runtime` module provides utilities to coordinate work across the distributed processes: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

- **`rt.get_local_rank()`** – returns the rank of the GPU within the current node (0-indexed).
- **`rt.get_global_rank()`** – returns the global rank across all processes.

These are used for conditional logic, such as having only rank 0 save model artifacts or print messages.

### Return Value

When the decorated function is called via `.distributed()`, it returns a list of the return values from each process. In the example, the result is a list of [MLflow Run](/concepts/mlflow-run.md) IDs (one per GPU), and the first element is extracted. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Related Concepts

- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Multi-GPU Distributed Training](/concepts/multi-gpu-distributed-training-api.md)
- LoRA & Parameter-Efficient Fine-Tuning
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

### Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
