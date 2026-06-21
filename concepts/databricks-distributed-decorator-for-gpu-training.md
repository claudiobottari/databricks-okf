---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 050aee2093c7fbcf48cf5398e64447e9f2a73ed8c70019ce85a4ddb2ffc98764
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-distributed-decorator-for-gpu-training
    - D@DFGT
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
title: Databricks @distributed Decorator for GPU Training
description: A decorator from the serverless_gpu library that enables execution of GPU workloads on Databricks AI Runtime, automatically provisioning GPUs (e.g., 8xH100) and handling distributed training setup.
tags:
  - databricks
  - distributed-training
  - gpu
  - api
timestamp: "2026-06-19T18:50:45.657Z"
---

# Databricks `@distributed` Decorator for GPU Training

The **`@distributed` decorator** is a feature of the Databricks `serverless_gpu` Python library that enables running Python functions across multiple GPUs on a single node. It is designed for distributed GPU workloads such as large language model (LLM) training, and is a core component of the [AI Runtime](/concepts/ai-runtime.md) – Databricks’ managed GPU infrastructure. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

When applied to a function, the decorator provisions the specified number and type of GPUs, launches a separate process per GPU, and exposes local and global rank information via the `serverless_gpu.runtime` module. The decorated function is then called by invoking `.distributed()` on it. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Usage

To use the decorator, import `distributed` from `serverless_gpu` and apply it to a function with the required GPU configuration:

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = hello_world.distributed('SGC')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

In training workflows, the function typically loads a model and dataset, sets up a distributed trainer (e.g., [DeepSpeed](/concepts/deepspeed.md) ZeRO-3 or [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)), and performs training. The decorated function returns a dictionary of results, which the calling notebook can inspect. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Parameters

The `@distributed` decorator accepts the following parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `gpus` | Number of GPUs to use for the distributed function. Must match the available GPUs in the target configuration. | `gpus=8` |
| `gpu_type` | Type of GPU hardware. Supported values include `'h100'`, `'a10'`, and others. | `gpu_type='h100'` |

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Runtime Utilities

The `serverless_gpu.runtime` module provides two key functions:

- `rt.get_local_rank()` – Returns the rank of the current process **within the node** (0–based).
- `rt.get_global_rank()` – Returns the global rank across all processes on the node (0–based).

These ranks are typically used to coordinate distributed operations, such as assigning each GPU a partition of work or printing logs from only one process. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Integration with MLflow

The `@distributed` decorator works seamlessly with [MLflow](/concepts/mlflow.md) experiment tracking. In practice, the decorated function can start an [MLflow Run](/concepts/mlflow-run.md) (by calling `mlflow.start_run()` inside the function), set experiment tags, and log metrics. The [MLflow Run](/concepts/mlflow-run.md) ID can be obtained via `mlflow.last_active_run().info.run_id` and returned as part of the function’s output. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## Selecting GPU Resources

Before using the `@distributed` decorator, the notebook must be connected to a suitable serverless GPU compute. From the compute selector, choose **Serverless GPU**, then in the **Environment** tab select the desired accelerator (e.g., **8xH100**) and environment (e.g., **AI v5**). The training function will automatically provision the requested GPUs when `.distributed()` is called. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Limitations

The `@distributed` decorator is designed for **single-node, multi-GPU** execution. It does not automatically scale to multiple nodes; for multi-node training, other approaches such as [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) (e.g., using [DeepSpeed](/concepts/deepspeed.md) or [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)) are required. Additionally, the GPU type and count must match the capacity of the selected accelerator configuration. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – Managed GPU compute environment on Databricks.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On‑demand GPU provisioning for notebooks.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific GPU configuration used with this decorator.
- [DeepSpeed](/concepts/deepspeed.md) – A memory‑optimization library often used alongside `@distributed`.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Alternative distributed training strategy.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Basic data parallelism suitable for smaller models.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Tracking infrastructure integrated with training functions.

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
2. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
