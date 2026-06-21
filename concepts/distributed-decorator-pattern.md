---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36368c9cf2e62c0604ec758f5ce65adb7991f7d25157d299cf8407c205d78efa
  pageDirectory: concepts
  sources:
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
    - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-decorator-pattern
    - "@DP"
  citations:
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
title: "@distributed Decorator Pattern"
description: A Python decorator from Databricks serverless_gpu library that provisions GPU resources and handles distributed training setup automatically
tags:
  - databricks
  - distributed-training
  - python
timestamp: "2026-06-19T10:34:34.984Z"
---

<!-- Existing page context:

title: "@distributed Decorator Pattern"
summary: A Python decorator from the Databricks serverless_gpu library that enables execution of GPU workloads on distributed hardware by automatically provisioning GPUs (e.g., 8xH100) and handling distributed training setup.
sources:
  - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
  - fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:21:24.345Z"
updatedAt: "2026-06-18T12:21:24.345Z"
tags:
  - databricks
  - gpu
  - python
  - distributed-computing
aliases:
  - distributed-decorator-pattern
  - "@DP"
confidence: 0.85
provenanceState: extracted
inferredParagraphs: 2
-->

# @distributed Decorator Pattern

The **`@distributed` decorator pattern** is a Python decorator from the `serverless_gpu` library that enables serverless GPU workloads to be executed on [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) with automatic provisioning of distributed GPU resources. The decorator handles the setup of distributed training environments, such as multi-GPU clusters, and executes the decorated function on the provisioned hardware. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Usage

### Import and Syntax

The decorator is imported from the `serverless_gpu` module and applied to any Python function that should run on a GPU cluster. The decorated function is executed by calling its `.distributed()` method rather than a regular call. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def run_training():
    # Training code here
    ...
    return results

results = run_training.distributed()
```

### Parameters

The `@distributed` decorator accepts two key parameters that control the GPU resources allocated for the workload: ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

| Parameter | Description | Example |
|-----------|-------------|---------|
| `gpus` | Number of GPUs to provision for the job. | `8` |
| `gpu_type` | GPU hardware type, such as `'H100'`. | `'H100'` |

The decorator may also accept other optional parameters (e.g., `remote` for multi-node training). When `remote=False` and more GPUs are specified, the training can be extended to multi-node distributed execution across multiple machines. ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## How It Works

When the `.distributed()` method is called, the `@distributed` decorator automatically provisions the specified number and type of GPUs on [Databricks AI Runtime](/concepts/databricks-ai-runtime.md). It sets up the distributed environment—including environment variables, network configuration, and process initialization—and then executes the decorated function across the provisioned resources. The function's return value is collected and returned to the caller after execution completes. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

The decorator is designed to work seamlessly with popular distributed training libraries. It can be used with [DeepSpeed ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md), as in the full fine-tuning of Llama 3.2 1B on 8 H100 GPUs. Alternatively, it can be used with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) and LoRA for parameter-efficient fine-tuning, as demonstrated in the supervised fine-tuning of the 120B parameter GPT‑OSS model on the same hardware. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

## Requirements

To use the `@distributed` decorator, the following prerequisites must be met: ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

- **Compute**: The notebook must be attached to a serverless GPU compute resource (for example, through the notebook's compute selector, choosing "Serverless GPU" and an appropriate accelerator like `8xH100`).
- **Runtime**: The environment must be a Databricks AI Runtime environment (e.g., AI v4 or v5) that includes the required libraries for distributed training. The `serverless_gpu` package is included in AI Runtime.
- **Authentication**: If the training function accesses external resources (e.g., HuggingFace Hub), tokens or secrets must be configured within the function body, as the decorator does not automatically propagate workspace secrets.

## Example: Full Fine-Tuning with DeepSpeed

The following pattern, extracted from a full fine-tuning notebook, demonstrates using the decorator with [DeepSpeed ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md) and the [TRL (Transformers Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) library: ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu import distributed
import mlflow

mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)

@distributed(gpus=8, gpu_type='H100')
def run_distributed_trl_sft():
    # Load model, tokenizer, dataset
    # Initialize SFTTrainer with DeepSpeed ZeRO-3 config
    # Train and save checkpoints
    return {"status": "success", "mlflow_run_id": mlflow_run_id}

results = run_distributed_trl_sft.distributed()
```

In this example, the decorator handles infrastructure provisioning; the function contains all training logic and returns an [MLflow](/concepts/mlflow.md) run ID for tracking.

## Example: PEFT with FSDP and LoRA

The decorator also works with [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) and LoRA for parameter-efficient fine-tuning of very large models. The following excerpt from a 120B parameter GPT-OSS notebook illustrates the pattern: ^[fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def train_gpt_oss_fsdp_120b():
    # Load model in bfloat16, apply LoRA adapters
    # Configure FSDP with full_shard and auto_wrap
    # Initialize SFTTrainer with FSDP settings
    trainer.train()
    return trainer.state.log_history

train_gpt_oss_fsdp_120b.distributed()
```

Here the decorator launches the training across 8 H100 GPUs, and FSDP shards model parameters, gradients, and optimizer states across those GPUs to accommodate the 120B parameter model. The function uses the `fsdp="full_shard auto_wrap"` configuration within SFTConfig.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The serverless GPU compute platform that hosts the `@distributed` decorator
- [DeepSpeed ZeRO Stage 3](/concepts/deepspeed-zero-stage-3.md) — A memory optimization technique often used with `@distributed`
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Another distributed training strategy supported by the decorator
- LoRA — Parameter-efficient fine-tuning method used in conjunction with FSDP
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Compute resources provisioned automatically for GPU workloads
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concept of training models across multiple GPUs or nodes
- [TRL (Transformers Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) — Library used in the example training functions
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking integrated with the distributed training function
- SFTConfig — Configuration class for supervised fine-tuning with the TRL library

## Sources

- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
- fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md

# Citations

1. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
2. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
