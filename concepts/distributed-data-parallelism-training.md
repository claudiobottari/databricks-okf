---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb9be1e8c7a2e4cfa06aff1b6dbeeba62b06375f5ceab5820d551c3b3ba969be
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-data-parallelism-training
    - DDPT
    - Distributed Data-Parallel Training
    - Distributed Data Processing
  citations:
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
title: Distributed Data Parallelism Training
description: Training technique that distributes model training across multiple GPUs using data parallelism, handling gradient synchronization and batching across devices
tags:
  - distributed-training
  - parallelism
  - deep-learning
timestamp: "2026-06-18T12:01:59.832Z"
---

# Distributed Data Parallelism Training

**Distributed Data Parallelism Training** is a technique where a model is replicated across multiple GPUs, each processing a different subset of the training data, and gradients are synchronized across replicas at each optimization step. This approach reduces training time by leveraging multiple accelerators in parallel while maintaining model accuracy. In Databricks, distributed data parallelism is implemented using the serverless GPU compute layer, which automatically provisions and orchestrates GPU resources. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## How Distributed Data Parallelism Works in Databricks

Databricks provides a `@distributed` decorator from the `serverless_gpu` library to run training functions on multiple GPUs. When applied, the decorator provisions the specified number of GPUs on-demand, sets up the distributed data parallelism (DDP) environment, and handles communication between processes automatically. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type="h100")
def run_train():
    # Training logic here
    pass
```

Inside the decorated function, environment variables such as `RANK`, `LOCAL_RANK`, and `WORLD_SIZE` are available for each process to control distributed execution. The device for each process is set using `torch.cuda.set_device(local_rank)`. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

The training function typically includes:

- Loading and tokenizing a dataset
- Initializing the model with quantization (e.g., [MXFP4 Quantization](/concepts/mxfp4-quantization.md)) to reduce memory usage
- Configuring LoRA adapters for parameter‑efficient fine‑tuning
- Training with gradient checkpointing, mixed precision (`bfloat16`), and gradient accumulation
- Saving the trained model to a Unity Catalog volume ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## GPUs and Accelerator Configuration

To use distributed data parallelism, a notebook must be connected to a serverless GPU compute resource. In the notebook environment, select **Serverless GPU**, choose an accelerator type (e.g., **8xH100**), and apply an AI environment (e.g., **AI v5**) that includes all required libraries. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Benefits of Distributed Data Parallelism

- **Reduced training time** by processing data across multiple GPUs in parallel.
- **Scalability** to train large models (e.g., 20B parameters) that would otherwise be too large for a single GPU.
- **Memory efficiency** when combined with techniques like MXFP4 quantization, gradient checkpointing, and LoRA adapters. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Monitoring GPU Memory

A utility function `log_gpu_memory` can be used during distributed training to log allocated and reserved memory for each GPU rank, helping to debug memory issues. ^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Related Concepts

- LoRA – Parameter‑efficient fine‑tuning that trains small adapter layers while freezing the base model.
- [MXFP4 Quantization](/concepts/mxfp4-quantization.md) – Microscaling 4‑bit floating point format that reduces memory usage.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Databricks managed compute that automatically provisions GPU resources.
- [AI Runtime](/concepts/ai-runtime.md) – Databricks environment with pre‑installed libraries for deep learning.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for model registration and checkpoint storage.
- [Gradient checkpointing](/concepts/activation-checkpointing.md) – Memory‑saving technique used during distributed training.
- [SFTTrainer](/concepts/sfttrainer.md) – The Trainer class from [TRL](/concepts/trl-transformer-reinforcement-learning.md) used for supervised fine‑tuning in the example.

## Sources

- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
