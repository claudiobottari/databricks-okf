---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 77d86d636f2e23152d533cba5818c9906f76741051f3338e7cc5a227a677287d
  pageDirectory: concepts
  sources:
    - distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless_gpu-distributed-training
    - SDT
  citations:
    - file: distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md
title: serverless_gpu Distributed Training
description: A Databricks library that provides a @distributed decorator to run LLM training across multiple GPUs (e.g., 8xH100) with automatic rank management and device mapping.
tags:
  - distributed-computing
  - gpu
  - databricks
timestamp: "2026-06-18T12:05:43.491Z"
---

# serverless_gpu Distributed Training

**serverless_gpu Distributed Training** is a Databricks-native Python library that enables distributed model training across multiple GPUs using a simple decorator-based API. It abstracts the orchestration of multi-GPU compute so that data scientists can scale training across several accelerators without manually managing distributed process groups or communication backends.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Overview

The `@distributed` decorator, imported from `serverless_gpu`, wraps a user-defined training function and runs it in parallel across a specified number of GPUs. The decorator accepts parameters for the number of GPUs and the GPU type (e.g., H100). Inside the decorated function, each process can determine its rank using `serverless_gpu.runtime.get_global_rank()`, allowing rank-0 to handle saving or logging while other ranks perform only compute.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Usage

### Import and Decorate

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def run_train():
    # training code here
    ...
    if rt.get_global_rank() == 0:
        # save model, log metrics, etc.
    return some_value
```

The decorator supports the following parameters:

- `gpus` (int): Number of GPUs to allocate for the training job.
- `gpu_type` (str): The accelerator type, e.g., `'h100'`.

Inside the function, the environment variable `LOCAL_RANK` is available (set by the framework) and should be used to assign the CUDA device: `torch.cuda.set_device(local_rank)`.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Invoking the Distributed Run

The decorated function is called via `.distributed()` instead of a regular function call:

```python
run_id = run_train.distributed()
```

The method returns a list of results — one entry per GPU rank. In a typical pattern, only rank‑0 returns meaningful data (e.g., an [MLflow Run](/concepts/mlflow-run.md) ID), and the caller uses the first element of the list.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

### Rank-Aware Logic

The `serverless_gpu.runtime` module provides `get_global_rank()` to identify the current process’s rank. This is essential for operations that should happen only once (such as saving a checkpoint, logging to MLflow, or registering a model). A common pattern is to guard saving logic with `if rt.get_global_rank() == 0:`.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Environment and Compute Requirements

- **Databricks AI Runtime**: The library is available in **AI v5** (or later) environments. The AI v5 environment includes the full Unsloth stack (`unsloth`, `unsloth_zoo`, `trl`, `peft`, `bitsandbytes`, `xformers`, `einops`) as well as `serverless_gpu`, so no additional pip installations are needed.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]
- **Accelerator Selection**: In the Databricks notebook environment, the user selects the accelerator (e.g., **8xH100**) from the environment panel. The compute cluster startup can take up to 8 minutes.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Integration with MLflow

Inside the distributed function, MLflow tracking works normally. Each process can call `mlflow.last_active_run()` to obtain the current run. The run ID returned by rank‑0 can later be used to log the trained model to [Unity Catalog](/concepts/unity-catalog.md). This enables a seamless pipeline: training on multiple GPUs → logging metrics to a single [MLflow Run](/concepts/mlflow-run.md) → registering the model with a single version.^[distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md]

## Related Concepts

- [Unsloth](/concepts/unsloth.md) – The library used for efficient LoRA fine-tuning in the example notebook.
- LoRA – Low-Rank Adaptation technique applied via PEFT.
- [SFTTrainer](/concepts/sfttrainer.md) – The TRL trainer used for supervised fine-tuning.
- [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) – The environment that bundles distributed training libraries.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General concept of splitting training across multiple accelerators.
- [Serverless GPU](/concepts/serverless-gpu-compute.md) – The Databricks feature that provisions GPU compute on demand.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance and model registry where trained models are logged.

## Sources

- distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md

# Citations

1. [distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws.md](/references/distributed-finetune-llama-32-3b-with-unsloth-on-multiple-gpus-databricks-on-aws-5c6e3457.md)
