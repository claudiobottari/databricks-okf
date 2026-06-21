---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d0859085193a81821085d3e1cd3a5ff0830d173564d1f9f41eba6a22baabe9e
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-compute-databricks
    - SGC(
    - Serverless Compute Databricks
    - Serverless compute (Databricks)
    - serverless compute clusters
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: Serverless GPU Compute (Databricks)
description: Databricks managed compute that automatically provisions, scales, and orchestrates GPU resources (e.g., 8xH100) for distributed training without requiring users to manage infrastructure.
tags:
  - databricks
  - cloud-computing
  - distributed-training
timestamp: "2026-06-18T12:02:48.176Z"
---

# Serverless GPU Compute (Databricks)

**Serverless GPU Compute** is a Databricks-managed compute offering that automatically provisions and scales GPU resources for machine learning workloads without requiring users to configure or manage clusters. It provides on-demand access to GPU accelerators for distributed training, fine-tuning, and inference tasks. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Overview

Serverless GPU Compute eliminates the operational overhead of managing GPU infrastructure by handling resource provisioning, scaling, and lifecycle management automatically. Users connect to Serverless GPU Compute directly from notebooks, and the system dynamically allocates GPU resources based on the workload's requirements. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

The service supports a range of GPU accelerator types, including H100 GPUs, and offers different compute environments such as the AI v5 base environment, which includes pre-installed libraries for machine learning frameworks like `transformers`, `trl`, `peft`, `mlflow`, and `hf_transfer`. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Key Capabilities

### Distributed Training

Serverless GPU Compute supports multi-GPU distributed training through the `@distributed` decorator. This allows users to specify the number of GPUs and GPU type, and the system automatically handles GPU provisioning, data distribution, and synchronization across workers. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type="H100")
def run_train(use_lora=True):
    # Training code runs across 8 H100 GPUs
    pass
```

### Parameter-Efficient Fine-Tuning

Serverless GPU Compute is designed to work with parameter-efficient fine-tuning techniques like [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md), which reduces trainable parameters by approximately 99% while maintaining model quality. This dramatically reduces memory requirements and training time. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Memory Optimization

The platform supports [Liger Kernels](/concepts/liger-kernels.md), GPU-optimized Triton kernels that fuse multiple operations into single kernels, reducing memory usage by up to 80%. Additional optimizations include mixed-precision training (FP16), gradient checkpointing, and gradient accumulation for simulating larger batch sizes. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Connecting to Serverless GPU Compute

To use Serverless GPU Compute from a notebook: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

1. Click the notebook's compute selector in the top right and select **Serverless GPU**
2. On the right side, click the environment button
3. Select an accelerator type (e.g., **8xH100**)
4. Choose a base environment (e.g., **AI v5**)
5. Click **Apply**

The training function will automatically provision the specified GPU resources for distributed training.

## Integration with Unity Catalog

Models trained on Serverless GPU Compute can be registered directly in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment. The platform integrates with [MLflow](/concepts/mlflow.md) for tracking experiments, logging model artifacts and metadata, and managing model versioning. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Common Workloads

### Supervised Fine-Tuning

Serverless GPU Compute supports supervised fine-tuning of large language models using libraries like [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md). Users can fine-tune models such as Qwen2-0.5B on conversational datasets with automatic checkpointing and logging. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Model Registration

After training, models can be merged (e.g., LoRA adapters merged into the base model) and registered in Unity Catalog with full metadata for reproducibility and deployment. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Best Practices

- **Use parameter-efficient techniques like LoRA** to reduce memory requirements and training time while maintaining model quality ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Enable memory optimizations** such as Liger kernels, mixed precision (FP16), and gradient checkpointing to maximize GPU utilization ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]
- **Monitor compute usage** through Databricks observability tools to optimize resource allocation and costs ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Limitations

- Serverless GPU Compute is billed based on usage duration and GPU type selected
- Available GPU types and environments may vary by region

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU training across multiple workers
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) — Parameter-efficient fine-tuning technique
- [Liger Kernels](/concepts/liger-kernels.md) — Memory-optimized GPU kernels for transformer operations
- [TRL (Transformer Reinforcement Learning)](/concepts/trl-transformer-reinforcement-learning.md) — Library for training language models
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model management
- [Unity Catalog](/concepts/unity-catalog.md) — Model governance and deployment
- [Model Serving](/concepts/model-serving.md) — Deploying trained models for inference

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
