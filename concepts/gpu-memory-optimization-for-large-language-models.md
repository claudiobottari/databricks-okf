---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 977bb5f378378322c0702818c67071255ae31478b70dac7b274c9d0f9794e28b
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - gpu-memory-optimization-for-large-language-models
    - GMOFLLM
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: GPU Memory Optimization for Large Language Models
description: Techniques such as gradient accumulation fusion and CPU offloading used to reduce GPU memory footprint when training models ranging from 1B to 100B+ parameters.
tags:
  - machine-learning
  - memory-optimization
  - deep-learning
timestamp: "2026-06-18T15:33:55.452Z"
---

Here is the wiki page for "GPU Memory Optimization for Large Language Models", written based solely on the provided source material.

---

## GPU Memory Optimization for Large Language Models

**GPU Memory Optimization for Large Language Models** refers to the set of techniques and distributed training strategies used to reduce the per-GPU memory footprint of model parameters, gradients, and optimizer states. These optimizations are essential for training or serving large language models (LLMs) that would otherwise exceed the memory capacity of a single GPU.

### Overview

Training models in the 1B to 100B+ parameter range faces significant memory limitations because a single copy of the model parameters, gradients, and optimizer states often exceeds a GPU's available VRAM. Standard data parallelism (e.g., [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)) replicates these components across all GPUs, offering no memory efficiency improvement for the model itself. To overcome this, advanced memory optimization techniques shard or offload these components across devices or host memory. ^[distributed-training-using-deepspeed-databricks-on-aws.md, fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Key Optimization Strategies

#### Fully Sharded Data Parallel (FSDP)

[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is a PyTorch-native strategy that shards model parameters, gradients, and optimizer states across multiple GPUs. This sharding significantly reduces the per-GPU memory footprint, enabling the training of very large models that would otherwise be impossible. FSDP offers a better trade-off for memory efficiency compared to standard DDP and is the standard choice for models in the 20B to 120B+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

#### DeepSpeed ZeRO (Zero Redundancy Optimizer)

[DeepSpeed](/concepts/deepspeed.md) provides advanced memory optimization techniques through its ZeRO (Zero Redundancy Optimizer) stages, enabling efficient training of large models. DeepSpeed offers fine-grained control over optimizer state sharding through three stages: ^[distributed-training-using-deepspeed-databricks-on-aws.md]

- **ZeRO Stage 1**: Shards optimizer states across GPUs.
- **ZeRO Stage 2**: Shards optimizer states and gradients across GPUs.
- **ZeRO Stage 3**: Shards optimizer states, gradients, and parameters across GPUs.

For simpler use cases, practitioners may consider standard DDP, while for PyTorch-native large model training, FSDP is an alternative. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

#### CPU Offloading

Both DeepSpeed and FSDP can offload model states to CPU memory, further reducing GPU memory usage at the cost of increased communication overhead. This is particularly useful when working with very large models (e.g., 100B+ parameters) where even sharded GPU memory is insufficient. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

#### Gradient Accumulation Fusion

DeepSpeed includes a gradient accumulation fusion feature that combines multiple backward passes before performing optimizer updates, reducing memory spikes and smoothing the memory profile during training. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

### When to Use Each Strategy

| Strategy | When to Use | Memory Improvement |
|----------|-------------|--------------------|
| **DDP** | Models that fit within a single GPU's memory. | None (model replicated across GPUs) |
| **FSDP** | Training models in the 20B to 120B+ parameter range; PyTorch-native approach. | Significant per-GPU reduction |
| **DeepSpeed** | Advanced memory optimization beyond FSDP; fine-grained ZeRO control; 1B to 100B+ parameters. | Maximum per-GPU reduction |

^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md, distributed-training-using-deepspeed-databricks-on-aws.md]

### Use Cases

GPU memory optimization techniques are particularly valuable for:

- Training large language models (1B to 100B+ parameters)
- Fine-tuning very large models on limited hardware
- Running inference on large models with constrained VRAM
- Multi-node distributed training where per-GPU memory is a bottleneck

### A100 GPU Considerations

For high-performance GPU memory optimization, [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) is relevant. A100 GPUs are considered an efficient choice for many deep learning tasks, including training and tuning large language models. However, A100 GPUs typically have limited capacity in cloud environments, making advance capacity reservation important for consistent access. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Memory-Efficient Training](/concepts/gradient-checkpointing-for-memory-efficient-training.md)

### Sources

- distributed-training-using-deepspeed-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
