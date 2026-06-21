---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea6ed8218ed822ace3cf230ecb1233b8c27ada2e25746e039c329a742fef11f2
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-on-ai-runtime
    - DTOAR
    - Distributed Training with AI Runtime
    - Multi-GPU Distributed Training on AI Runtime
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: Distributed Training on AI Runtime
description: A Beta API using the @distributed decorator from the serverless_gpu Python package that enables multi-GPU training on a single node with PyTorch DDP, FSDP, or DeepSpeed and minimal configuration.
tags:
  - databricks
  - distributed-training
  - pytorch
  - deepspeed
timestamp: "2026-06-19T08:57:09.724Z"
---

```markdown
---
title: Distributed Training on AI Runtime
summary: Multi-GPU training support on a single node using the @distributed decorator from the serverless_gpu Python API, supporting PyTorch DDP, FSDP, or DeepSpeed.
sources:
  - ai-runtime-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:22:52.834Z"
updatedAt: "2026-06-18T14:22:52.834Z"
tags:
  - databricks
  - distributed-training
  - deep-learning
aliases:
  - distributed-training-on-ai-runtime
  - DTOAR
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Distributed Training on AI Runtime

**Distributed Training on AI Runtime** refers to the capability to train deep learning models across multiple GPUs on a single node using the [[AI Runtime]] compute offering on Databricks Serverless. This feature is currently in Beta. ^[ai-runtime-databricks-on-aws.md]

## Overview

AI Runtime supports distributed training across multiple GPUs on the single node that a notebook or job is connected to. The distributed training API enables users to launch multi-GPU workloads with popular distributed training frameworks including [[PyTorch DDP on Databricks|PyTorch DDP]], Fully Sharded Data Parallel ([[FSDP (Fully Sharded Data Parallel)|FSDP]]), and [[DeepSpeed]], all with minimal configuration. ^[ai-runtime-databricks-on-aws.md]

## API: `@distributed` Decorator

The primary interface for launching distributed training workloads on AI Runtime is the `@distributed` decorator from the `serverless_gpu` Python API (Beta). This decorator abstracts away much of the cluster configuration and resource management typically required for multi-GPU training. ^[ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed
def train_model():
    # Your multi-GPU training code here
    pass
```

## Supported Frameworks

The distributed training API on AI Runtime supports three major approaches for multi-GPU training:

- **PyTorch DDP (Distributed Data Parallel)** — Standard data parallelism across GPUs on the node. ^[ai-runtime-databricks-on-aws.md]
- **FSDP (Fully Sharded Data Parallel)** — Shards model parameters, gradients, and optimizer states across GPUs for memory efficiency, suitable for training models in the [[20B to 120B+ Parameter Model Training]] range. (Inferred from related material; FSDP is explicitly mentioned as supported by the source.)
- **DeepSpeed** — Advanced memory optimization features beyond what FSDP offers out-of-the-box. ^[ai-runtime-databricks-on-aws.md]

## Hardware

AI Runtime provisions a single node with GPU accelerators. The number of GPUs available depends on the accelerator type selected. Currently supported accelerators include A10 and H100 GPUs, with the 1xH100 accelerator in Beta. ^[ai-runtime-databricks-on-aws.md]

## Requirements

To use distributed training on AI Runtime:

- The workspace must be in a supported AWS region: `us-west-2`, `us-west-1`, `us-east-1`, `us-east-2`, `ca-central-1`, or `sa-east-1`. ^[ai-runtime-databricks-on-aws.md]
- The AI Runtime preview must be enabled via workspace admin settings. For the 1xH100 accelerator specifically, the **AI Runtime Beta Feature** preview must also be enabled. ^[ai-runtime-databricks-on-aws.md]

## Limitations

- Distributed training only spans multiple GPUs on the **single node** the notebook is connected to; it does not support multi-node distributed training. ^[ai-runtime-databricks-on-aws.md]
- AI Runtime supports only A10 and H100 accelerators. ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a workload is seven days. For model training jobs that exceed this limit, implement checkpointing and restart the job once the maximum runtime is reached. ^[ai-runtime-databricks-on-aws.md]

## Use Cases

Distributed training on AI Runtime is appropriate for any custom model training that involves deep learning and benefits from GPU acceleration, including:

- [[LLM fine-tuning on Databricks|LLM fine-tuning]] (LoRA, QLoRA, full fine-tuning)
- Computer vision (object detection, image classification)
- [[Deep learning based recommender systems|Deep learning recommender systems]]
- [[TRL (Transformer Reinforcement Learning)|Reinforcement learning]]
- Deep learning time series forecasting

^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [[AI Runtime]] — The compute offering that provides GPU support for Databricks Serverless
- [[Fully Sharded Data Parallel (FSDP)]] — A memory-efficient distributed training strategy
- [[20B to 120B+ Parameter Model Training]] — The parameter range where FSDP is particularly useful
- [[DeepSpeed]] — An alternative distributed training framework
- [[PyTorch DDP on Databricks|PyTorch DDP]] — Standard distributed data parallelism approach
- Multi-GPU workload — The broader category of workloads supported by the distributed training API
- [[MLflow for Experiment Tracking and Model Registry|Experiment tracking and observability]] — MLflow integration for tracking distributed training runs

## Sources

- ai-runtime-databricks-on-aws.md
```

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
