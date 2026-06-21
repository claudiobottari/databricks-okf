---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 092b06c7ad590a8b6ccb2a13586e481da620871fd38add1c70e60a2025928c73
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
    - user-guides-for-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-training-with-distributed-decorator
    - DTW@D
  citations:
    - file: ai-runtime-databricks-on-aws.md
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - file: user-guides-for-ai-runtime-databricks-on-aws.md
title: Distributed Training with @distributed Decorator
description: A Python API (Beta) for multi-GPU distributed training on AI Runtime using PyTorch DDP, FSDP, or DeepSpeed via a @distributed decorator
tags:
  - distributed-training
  - pytorch
  - deep-learning
  - api
timestamp: "2026-06-19T17:31:25.906Z"
---

# Distributed Training with `@distributed` Decorator

The `@distributed` decorator, provided by the `serverless_gpu` Python API, is the primary mechanism for launching distributed training workloads on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) in Databricks. When applied to a Python function, it automatically orchestrates multi‑GPU training across the GPUs available on the single node the notebook is connected to, without requiring manual cluster setup or resource management. ^[ai-runtime-databricks-on-aws.md] ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## How It Works

The decorator takes the training logic defined inside the function and distributes it across the requested number of GPUs. It handles multi‑GPU orchestration, including data distribution, gradient synchronization, and process coordination. The function is executed on every GPU process, and the decorator automatically configures the distributed environment so that each process receives its own partition of the workload. Under the hood, it supports distributed strategies such as [PyTorch DDP](/concepts/pytorch-ddp-on-databricks.md), [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), and [DeepSpeed](/concepts/deepspeed.md). ^[ai-runtime-databricks-on-aws.md] ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Syntax and Parameters

Apply the `@distributed` decorator to any function that contains the training logic. The decorator accepts the following parameters:

- **`gpus`** (int): The number of GPUs to request for the training job.
- **`gpu_type`**: The GPU hardware type, typically specified using a string (e.g., `"H100"`) or the `GPUType` enum (e.g., `GPUType.H100`).

Inside the decorated function, you can use the `serverless_gpu.runtime` module to access local and global GPU ranks. The function is then invoked via its `.distributed()` method, which returns a list of results—one per GPU process. Conveniently, only the result from the primary process (rank 0) is typically used, for example to capture an [MLflow](/concepts/mlflow.md) run ID. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md] ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Basic Example

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type="H100")
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = hello_world.distributed('SGC')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Example: Fine-Tuning Olmo3 7B with Axolotl

The following code demonstrates the use of the `@distributed` decorator to fine‑tune an Olmo3 7B model using [Axolotl](/concepts/axolotl.md) and QLoRA across 8 H100 GPUs: ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

```python
from serverless_gpu.launcher import distributed
from serverless_gpu.compute import GPUType

@distributed(gpus=8, gpu_type=GPUType.H100)
def run_train(cfg):
    import os
    os.environ['HF_TOKEN'] = HF_TOKEN
    from axolotl.common.datasets import load_datasets
    from axolotl.cli.config import load_cfg

    cfg = load_cfg(cfg)
    dataset_meta = load_datasets(cfg=cfg)

    from axolotl.train import train
    cfg.max_steps = 16
    model, tokenizer, trainer = train(cfg=cfg, dataset_meta=dataset_meta)

    import mlflow
    mlflow_run_id = None
    if mlflow.last_active_run() is not None:
        mlflow_run_id = mlflow.last_active_run().info.run_id
    return mlflow_run_id

result = run_train.distributed(config)
run_id = result[0]
print(f"[[mlflow-run|MLflow Run]] ID: {run_id}")
```

In this example, the decorator automatically distributes the dataset, configures the distributed environment, and synchronizes training across all 8 GPUs. The function loads the dataset, validates the configuration, trains the model for 16 steps, and returns the [MLflow Run](/concepts/mlflow-run.md) ID for later model registration in [Unity Catalog](/concepts/unity-catalog.md). ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Best Practices

- **Capture the training result from rank 0**: The `.distributed()` method returns a list of results; use `result[0]` to obtain the output from the primary process (e.g., an [MLflow Run](/concepts/mlflow-run.md) ID). ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- **Log metrics to MLflow**: Inside the decorated function, use MLflow’s automatic logging (e.g., via Axolotl’s `use_mlflow=True` configuration) to track experiments across distributed runs. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- **Configure memory‑saving techniques**: When combined with [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md) and [gradient checkpointing](/concepts/activation-checkpointing.md), the decorator enables efficient training of large models on multi‑GPU serverless infrastructure. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- **Migrate from classic GPU clusters**: Replace Spark-based distributed training (e.g., `TorchDistributor`) with the `@distributed` decorator when moving to serverless compute. Also update data loading to use Unity Catalog volumes and install dependencies explicitly with `%pip install`. ^[user-guides-for-ai-runtime-databricks-on-aws.md]

## Limitations

- The `@distributed` decorator is designed specifically for GPU training workloads on serverless compute. It requires selecting the accelerator environment (e.g., 8xH100) in the notebook’s compute selector before execution. ^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- The number and type of GPUs must be specified at decoration time and cannot be changed dynamically.
- The distributed training API for multi‑GPU workloads remains in **Beta** as of the latest documentation. ^[ai-runtime-databricks-on-aws.md]
- The decorator operates only on a single node; multi‑node distributed training requires additional coordination beyond this API.

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The underlying compute platform that provisions GPU resources on demand.
- [Axolotl](/concepts/axolotl.md) – A high‑performance framework for LLM post‑training, often used with the decorator.
- [QLoRA (Quantized Low-Rank Adaptation)](/concepts/qlora-quantized-low-rank-adaptation.md) – Memory‑efficient fine‑tuning technique.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry integrated with the decorator.
- [Unity Catalog](/concepts/unity-catalog.md) – Destination for registering fine‑tuned models.
- [Distributed Data Parallelism (DDP)](/concepts/distributed-data-parallel-ddp.md) – One of the parallel strategies supported by the decorator.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Another supported strategy for very large models.
- [DeepSpeed](/concepts/deepspeed.md) – Another supported optimization library.

## Sources

- ai-runtime-databricks-on-aws.md
- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
- user-guides-for-ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
2. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
3. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
4. [user-guides-for-ai-runtime-databricks-on-aws.md](/references/user-guides-for-ai-runtime-databricks-on-aws-495c5d9c.md)
