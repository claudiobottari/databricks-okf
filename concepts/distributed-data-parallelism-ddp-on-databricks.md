---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4793e2b88a0b664d4c3ace257be0bf821d03dc6605832f46b705225ccc62168
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-data-parallelism-ddp-on-databricks
    - DDP(OD
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Distributed data parallelism (DDP) on Databricks
description: Training approach that shards mini-batches across multiple GPUs with synchronized gradients, automated via Databricks' @distributed decorator
tags:
  - distributed-training
  - databricks
  - parallelism
timestamp: "2026-06-18T15:29:26.850Z"
---

# Distributed Data Parallelism (DDP) on Databricks

**Distributed Data Parallelism (DDP)** on Databricks is a method for training deep learning models across multiple GPUs by replicating the model on each device and synchronizing gradients at each training step. Databricks provides a serverless GPU compute environment that simplifies the setup and execution of DDP workloads, enabling efficient scaling for models that can fit within a single GPU's memory.

## How DDP Works on Databricks

Databricks offers the `@distributed` decorator from the `serverless_gpu` library to manage DDP training. This decorator automatically provisions the requested number of GPUs, handles data parallelism across devices, and sets up the distributed environment. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

A typical DDP training function on Databricks includes:

- **Rank and world size configuration**: The decorator sets environment variables `RANK`, `LOCAL_RANK`, and `WORLD_SIZE`, which the training function uses to assign each GPU a unique role. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **GPU device assignment**: The `local_rank` variable is used to set the current CUDA device for each process via `torch.cuda.set_device(local_rank)`. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **DDP-specific training arguments**: When using the Hugging Face `SFTTrainer`, the `ddp_find_unused_parameters` flag can be set to `False` for improved performance. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## When to Use DDP

DDP is the recommended approach for models that can fit entirely in the memory of a single GPU. It is simpler to implement compared to sharding strategies but offers no memory efficiency improvements for the model itself—each GPU still holds a full copy of model parameters, gradients, and optimizer states. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

For larger models that exceed single‑GPU memory capacity, [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or other sharding techniques should be used instead. DDP remains a strong choice for smaller models (e.g., up to a few billion parameters) where memory is not the primary constraint. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Best Practices for DDP on Databricks

- **Choose appropriate GPU types**: Databricks supports A100, H100, and other GPUs across clouds. For DDP training, select an accelerator that provides sufficient memory and compute for your model size. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Monitor GPU memory**: Use utilities like `log_gpu_memory()` to track allocated and reserved memory per rank during training, helping to detect memory issues early. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Disable unused parameter detection**: Setting `ddp_find_unused_parameters=False` can reduce overhead when you are certain all parameters are used in the forward pass. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]
- **Leverage serverless GPU compute**: The serverless GPU environment automatically scales resources and provisions the requested number of GPUs (e.g., 8× H100) without manual cluster management. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Alternative for models that do not fit in a single GPU.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Databricks’ on‑demand GPU provisioning for distributed training.
- LoRA – Parameter‑efficient fine‑tuning often combined with DDP.
- [Unity Catalog](/concepts/unity-catalog.md) – Model registry for storing and deploying trained models.
- GPU Scheduling – Optimizing GPU utilization in distributed workflows.

## Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
