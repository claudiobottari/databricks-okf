---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 638e1364aba67b0169f485de347ca2a5cb802aee9e609274e13f37d73b6dd9d1
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
    - deep-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-runtime-on-databricks
    - AROD
  citations:
    - file: deep-learning-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: AI Runtime on Databricks
description: A Databricks runtime optimized for AI and machine learning workloads, supporting single-node tasks (Public Preview) and multi-GPU distributed training (Beta).
tags:
  - databricks
  - machine-learning
  - runtime
timestamp: "2026-06-19T13:58:16.560Z"
---

# AI Runtime on Databricks

**AI Runtime** is a Databricks compute offering that provides serverless GPU infrastructure for single-node and multi-node deep learning workloads. It is designed to simplify deep learning development by eliminating the need to manually manage GPU clusters while providing access to powerful GPU hardware including NVIDIA H100 and A100 GPUs. ^[deep-learning-databricks-on-aws.md] ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Overview

AI Runtime integrates with [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) to provide GPU-accelerated environments for training and inference. The runtime supports popular deep learning frameworks including PyTorch and TensorFlow, which are pre-installed in Databricks Runtime ML. Distributed training is supported through integrations with Ray, [TorchDistributor](/concepts/torchdistributor.md), and [DeepSpeed](/concepts/deepspeed.md). ^[deep-learning-databricks-on-aws.md]

Experiment tracking and model management are handled natively via [MLflow](/concepts/mlflow.md), which is essential for the iterative development cycles common in deep learning. ^[deep-learning-databricks-on-aws.md]

## Key Features

### Serverless GPU Architecture

AI Runtime provides serverless GPU compute that automatically scales based on workload demands. This architecture supports both single-node training for smaller models and multi-node distributed training for larger, more complex models. ^[deep-learning-databricks-on-aws.md]

### GPU Configurations

AI Runtime supports multiple GPU configurations for different workload requirements:

- **8xH100 Single-Node Configuration** — Eight NVIDIA H100 80GB HBM3 GPUs on a single compute node, providing 640 GB of total GPU memory for large model training workloads. H100 GPUs offer larger FLOPS and HBM compared to A10 GPUs. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **A100 GPU Support** — NVIDIA A100 GPUs are supported across all cloud providers and are considered an efficient choice for many deep learning tasks, including LLM training, NLP, object detection, and recommendation engines. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Framework and Tool Support

The runtime environment includes:

- **PyTorch** – for GPU-accelerated tensor computation and deep learning network construction.
- **TensorFlow** with TensorBoard – for numerical computation and visual debugging.
- **Distributed training libraries** – Ray, TorchDistributor, and DeepSpeed for scaling across multiple GPUs.
- **MLflow** – for tracking training runs and model development.

These tools are part of the broader Databricks Runtime ML package, which AI Runtime uses as its underlying environment. ^[deep-learning-databricks-on-aws.md]

## Availability and Access

AI Runtime for single-node tasks is in **Public Preview**. The distributed training API for multi-GPU workloads remains in **Beta**. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

To use AI Runtime from a Databricks notebook:

1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab, select the desired accelerator (e.g., **8xH100**).
3. Choose the appropriate environment (e.g., **AI v5** for H100 configurations).
4. Click **Apply**.

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Distributed Programming with the `@distributed` Decorator

The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs on a single node. The `runtime` module provides access to local and global GPU ranks for coordinating work. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(
    gpus=8,
    gpu_type='h100',
)
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = hello_world.distributed('SGC')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

- `gpus=8` specifies that the function runs on 8 processes, one per GPU.
- `rt.get_local_rank()` returns the rank of the GPU within the node.
- `rt.get_global_rank()` returns the global rank across all processes.

## Use Cases

### Single-Node Training

For models that fit within a single GPU's memory, AI Runtime provides straightforward compute without requiring infrastructure configuration.

### Multi-Node Distributed Training

For large deep learning models that exceed the capacity of a single GPU, AI Runtime supports distributed training across multiple nodes. This is particularly relevant for:

- Large language models (LLMs)
- Generative AI models
- Foundation models
- Computer vision tasks including object detection and image classification
- Deep learning based recommender systems
- Classic ML tasks including XGBoost and time series forecasting

^[ai-runtime-example-notebooks-databricks-on-aws.md]

### Model Training in the 20B to 120B+ Parameter Range

For training models with 20 billion to over 120 billion parameters, [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is the recommended approach. FSDP shards model parameters, gradients, and optimizer states across multiple GPUs to reduce per-GPU memory footprint. For models requiring even more advanced memory optimization, [DeepSpeed](/concepts/deepspeed.md) provides additional strategies beyond what FSDP offers. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Best Practices

For general guidelines on optimizing deep learning workflows on Databricks, including resource allocation, data pipeline optimization, and performance tuning, see [Best Practices for Deep Learning on Databricks](/concepts/best-practices-for-deep-learning-on-databricks.md). ^[deep-learning-databricks-on-aws.md]

### Availability Considerations

A100 GPUs typically have limited capacity in cloud environments. Databricks recommends contacting your cloud provider for resource allocation or reserving capacity in advance to ensure availability for workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Example Notebooks

AI Runtime provides example notebooks for various tasks:

- **Large Language Models (LLMs)** — Examples for fine-tuning large language models including parameter-efficient methods.
- **Computer Vision** — Examples for object detection and image classification.
- **Deep Learning Based Recommender Systems** — Examples for building recommendation systems using modern approaches like two-tower models.
- **Classic ML** — Examples for XGBoost model training and time series forecasting.
- **Multi-GPU Distributed Training** — Examples for scaling training across multiple GPUs and nodes using the Serverless GPU API.

^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The ML-optimized runtime that underpins AI Runtime.
- [PyTorch on Databricks](/concepts/pytorch-on-databricks.md) – Using PyTorch with AI Runtime.
- [TensorFlow on Databricks](/concepts/tensorflow-on-databricks.md) – Using TensorFlow with AI Runtime.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Multi-node training approaches.
- [Serverless GPU](/concepts/serverless-gpu-compute.md) – The compute model powering AI Runtime.
- Deep Learning – Foundational deep learning concepts.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment tracking for deep learning.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient training for large models.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – Specific GPU configuration available on AI Runtime.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – A100 GPU availability on the platform.

## Sources

- deep-learning-databricks-on-aws.md
- ai-runtime-example-notebooks-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
4. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
5. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
