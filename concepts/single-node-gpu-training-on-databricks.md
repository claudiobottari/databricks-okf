---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e5047208c6010341a301cd71a40f2a6cd0b0772ff7dbe3ae8fc4fc36f0e0cb39
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-gpu-training-on-databricks
    - SGTOD
    - Single Node Training
    - Single-Node GPU Training
    - Single-node training
    - Single‑Node Training
    - Single‑node Training
    - Single‑node training
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: computer-vision-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Single-node GPU Training on Databricks
description: AI Runtime supports single-node GPU tasks for model training and fine-tuning, currently in Public Preview.
tags:
  - databricks
  - gpu
  - training
  - single-node
timestamp: "2026-06-19T17:49:19.035Z"
---

# Single-node GPU Training on Databricks

**Single-node GPU Training on Databricks** refers to the practice of training deep learning models using one or more GPUs on a single compute node within the Databricks platform. This approach is suitable for models that can fit within the combined GPU memory of a single node and is supported through Databricks' AI Runtime and serverless GPU compute offerings.

## Overview

Single-node GPU training on Databricks involves using a single compute node equipped with one or more GPUs to train machine learning models. This configuration is simpler to set up than multi-node distributed training and is appropriate for many deep learning workloads, including computer vision tasks and models that fit within a single node's GPU memory. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Supported Configurations

Databricks offers several single-node GPU configurations for training workloads:

### 8xH100 Configuration

The [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) provides eight NVIDIA H100 80GB HBM3 GPUs on a single compute node. This configuration is available through Databricks Serverless GPU compute and is designed for large model training workloads requiring high FLOPS and HBM capabilities. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

To select this configuration from a Databricks notebook:

1. From the compute selector, choose **Serverless GPU**
2. In the **Environment** tab, select **8xH100** for your accelerator
3. Choose the **AI v5** environment
4. Click **Apply**

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Other GPU Options

Databricks supports various GPU types across all cloud providers. For the complete list of supported GPU instance types, refer to the Databricks documentation on supported instances. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Use Cases

### Computer Vision

Single-node GPU training is particularly well-suited for computer vision tasks. Databricks provides example notebooks for several computer vision applications:

| Tutorial | Description |
| --- | --- |
| Image classification using convolutional neural network | Training a 2-D convolution neural network on serverless GPUs for image classification |
| Object detection using RetinaNet | Training an object detection model using RetinaNet on serverless GPU |
| Object detection using YOLO11n | Training a YOLO11n object detection model on the COCO128 dataset |

^[computer-vision-databricks-on-aws.md]

These examples demonstrate how to train and fine-tune models for various computer vision applications using single-node GPU resources. ^[computer-vision-databricks-on-aws.md]

### Large Language Models

For Large Language Model (LLM) training, single-node configurations with multiple high-memory GPUs (such as 8xH100) can be effective for models that fit within the combined memory of eight H100 GPUs (640GB total). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Scaling Considerations

When a model exceeds the memory capacity of a single node, you should consider [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) approaches. For models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range, [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) becomes necessary, while [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is appropriate for models that fit within a single GPU's memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Parallelism Strategies

Single-node GPU training on Databricks supports various parallelism strategies:

- **DDP**: Best for models that fit within a single GPU's memory
- **FSDP**: Required for models that cannot fit in a single GPU
- **DeepSpeed**: An alternative when more advanced memory optimization features are needed

^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

For multi-GPU training on a single node, the `serverless_gpu` library provides a `@distributed` decorator for running functions across multiple GPUs: ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()
```

## Availability and Access

Single-node GPU compute is available through Databricks Serverless GPU compute. When using the 8xH100 configuration, use `nvidia-smi` to verify connection to eight H100 GPUs. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

For A100 GPUs, which offer high performance for large-scale models, Databricks recommends contacting your cloud provider for resource allocation or reserving capacity in advance, as these GPUs may have limited capacity. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Computer vision on Databricks](/concepts/computer-vision-on-databricks.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- computer-vision-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
3. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
4. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
