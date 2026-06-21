---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 192918e535466b87577ad72cdbd215ad4d1200cbfe0e1478abad2955255b051a
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-fine-tuning-with-databricks-serverless-gpu
    - DFWDSG
  citations:
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
title: Distributed Fine-tuning with Databricks Serverless GPU
description: A training pattern that uses the @distributed decorator to automatically provision multiple H100 GPUs, handle data distribution, and orchestrate synchronized distributed training of LLMs.
tags:
  - distributed-training
  - databricks
  - fine-tuning
timestamp: "2026-06-18T15:29:42.401Z"
---

# Distributed Fine-tuning with Databricks Serverless GPU

**Distributed Fine-tuning with Databricks Serverless GPU** refers to the practice of using Databricks' managed, auto-scaling GPU infrastructure to fine-tune large language models (LLMs) across multiple GPUs in parallel. This approach combines parameter-efficient fine-tuning techniques with distributed training orchestration to reduce training time and memory requirements while simplifying infrastructure management.

## Overview

Databricks Serverless GPU Compute provides managed GPU resources that automatically scale to meet workload demands. When combined with distributed training techniques, it enables efficient fine-tuning of models that would otherwise exceed the memory capacity of a single GPU. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

The platform handles GPU provisioning, data distribution, and synchronization automatically, allowing practitioners to focus on model configuration rather than infrastructure management. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Key Techniques

### LoRA (Low-Rank Adaptation)

LoRA freezes the base model weights and trains only small adapter layers, reducing trainable parameters by approximately 99%. This dramatically reduces memory requirements and training time while maintaining model quality. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

Common LoRA configuration parameters include:
- **Rank (r)**: Typically set to 8 for a good balance of performance versus parameters
- **Alpha**: Scaling factor, usually 2-4x the rank (e.g., 32 for rank 8)
- **Dropout**: Regularization to prevent overfitting, commonly 0.1

Target modules for transformer models typically include attention layers (`q_proj`, `k_proj`, `v_proj`, `o_proj`) and MLP layers (`gate_proj`, `up_proj`, `down_proj`). ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Liger Kernels

[Liger Kernels](/concepts/liger-kernels.md) are GPU-optimized operations that fuse multiple computational steps into single kernels, reducing memory transfers and improving efficiency. Key benefits include: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

- **Fused operations**: Combines operations (e.g., linear + loss) to reduce memory overhead by up to 80%
- **Triton kernels**: Custom GPU kernels optimized for transformer operations (RMSNorm, RoPE, SwiGLU, CrossEntropy)
- **Memory efficiency**: Allows larger batch sizes or models that wouldn't otherwise fit in GPU memory
- **Single GPU optimization**: Particularly effective for A10/A100 single-GPU training scenarios

### TRL (Transformer Reinforcement Learning)

The TRL library simplifies training configuration and automatically applies optimizations for supervised fine-tuning and reinforcement learning-based training of language models. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Distributed Training Setup

### Connecting to Serverless GPU Compute

To use Serverless GPU Compute for distributed training: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

1. Select **Serverless GPU** as the compute type in the notebook's compute selector
2. Choose an accelerator type (e.g., **8xH100**)
3. Select the appropriate base environment (e.g., **AI v5**)

### The `@distributed` Decorator

The `@distributed` decorator from the `serverless_gpu` module configures distributed training across multiple GPUs: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type="H100")
def run_train(use_lora=True):
    # Training logic here
    pass
```

The decorator handles:
- GPU provisioning and allocation
- Data distribution across GPUs
- Synchronization between workers
- Collection of results from the distributed run

### Training Workflow

A typical distributed fine-tuning workflow includes: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

1. **Load dataset**: Download and prepare the training dataset
2. **Initialize model**: Load the base model and tokenizer with chat formatting
3. **Apply LoRA**: Attach adapter layers to reduce trainable parameters
4. **Configure training**: Set batch size, learning rate, and optimization settings
5. **Train model**: Run the training loop with automatic checkpointing and logging
6. **Save artifacts**: Store LoRA adapters and tokenizer to [Unity Catalog](/concepts/unity-catalog.md) volume
7. **Register model**: Log the model with MLflow and register in Unity Catalog

## Key Optimizations

### Mixed Precision Training

Using FP16 (half-precision) computation provides faster training with lower memory footprint. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Gradient Checkpointing

Trades computation for memory to fit larger batch sizes by recomputing intermediate activations during backpropagation rather than storing them. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Gradient Accumulation

Accumulates gradients over multiple batches before performing an optimizer step, simulating larger effective batch sizes for more stable training. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Learning Rate Adjustment

When using LoRA, learning rates are typically scaled 10x higher than for full fine-tuning to account for the smaller number of trainable parameters. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## Model Registration and Deployment

After distributed fine-tuning, models can be registered in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment: ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

```python
import mlflow

full_model_name = f"{catalog}.{schema}.{model_name}"

with mlflow.start_run(run_id=mlflow_run_id):
    model_info = mlflow.transformers.log_model(
        transformers_model=components,
        artifact_path="model",
        task="llm/v1/chat",
        registered_model_name=full_model_name,
        metadata={
            "task": task,
            "pretrained_model_name": MODEL_NAME,
            "databricks_model_family": "QwenForCausalLM",
        },
    )
```

The registered model can then be deployed using [Model Serving](/concepts/model-serving.md) for inference.

## Best Practices

- **Use LoRA for parameter efficiency**: Reduces trainable parameters by ~99% while maintaining quality
- **Enable Liger Kernels**: Fused GPU operations reduce memory usage by up to 80%
- **Configure gradient checkpointing**: Essential for fitting larger models on available GPU memory
- **Set appropriate batch sizes**: Balance memory constraints with training stability
- **Monitor with MLflow**: Track metrics, parameters, and artifacts for reproducibility
- **Save checkpoints regularly**: Use Unity Catalog volumes for persistent storage

## Related Concepts

- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- [Liger Kernels](/concepts/liger-kernels.md)
- TRL Library
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Model Serving](/concepts/model-serving.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Parameter-Efficient Fine-Tuning](/concepts/parameter-efficient-fine-tuning-peft.md)

## Sources

- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md

# Citations

1. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
