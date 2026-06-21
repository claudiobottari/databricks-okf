---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: accf2641f28ccba7418a25b414805210ea148828c4cae0c54254109f9946667f
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - computer-vision-on-databricks
    - CVOD
    - Computer Vision
    - computer vision
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Computer vision on Databricks
description: Notebook examples for computer vision tasks on Databricks AI Runtime, including object detection and image classification.
tags:
  - databricks
  - computer-vision
  - object-detection
  - image-classification
timestamp: "2026-06-19T22:04:09.676Z"
---

# Computer Vision on Databricks

**Computer Vision on Databricks** refers to the use of Databricks' AI Runtime and GPU-optimized infrastructure to perform computer vision tasks such as object detection, image classification, and image segmentation at scale. Databricks provides pre-configured environments and example notebooks that simplify the development and deployment of computer vision models.

## Overview

Databricks supports computer vision workloads through its AI Runtime, which includes optimized deep learning libraries and GPU support. The platform enables data scientists and ML engineers to build, train, and deploy computer vision models using familiar frameworks like PyTorch and TensorFlow, leveraging distributed computing for processing large image datasets. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example Notebooks

Databricks provides dedicated example notebooks for computer vision tasks under the [AI Runtime examples](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/) documentation. The **Computer vision** section includes practical examples for common workloads:

- **Object detection**: Training and inference pipelines for identifying and localizing objects within images.
- **Image classification**: Models that assign category labels to images, suitable for use cases like product categorization or medical imaging.
- Additional vision tasks as covered in the example notebooks. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

These notebooks demonstrate end-to-end workflows from data loading and preprocessing to model training, evaluation, and deployment.

## Infrastructure and GPU Support

Computer vision workloads benefit significantly from GPU acceleration. Databricks supports:

- **A100 GPUs** across all cloud providers for high-performance training of vision models. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **H100 GPUs** for workloads requiring even higher FLOPS and memory bandwidth, available through the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **[Databricks Runtime for Machine Learning]**, which includes pre-installed deep learning frameworks and GPU libraries.
- **Distributed training** capabilities for multi-GPU setups, allowing scaling across multiple nodes using the Serverless GPU API. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

### AI Runtime Tiers

- **AI Runtime for single-node tasks**: Currently in Public Preview, suitable for smaller-scale computer vision experiments and single-GPU training.
- **Distributed training API for multi-GPU workloads**: Remains in Beta, designed for training large vision models that require multiple GPUs. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Distributed Training for Computer Vision

For large-scale computer vision training, Databricks supports distributed strategies that scale across multiple GPUs:

- **[Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)**: Suitable for models that fit within a single GPU's memory, replicating the model across GPUs and synchronizing gradients.
- **[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)**: Recommended for very large vision models (e.g., Vision Transformers with billions of parameters) that exceed single-GPU memory capacity. FSDP shards model parameters, gradients, and optimizer states across GPUs. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **Multi-node training**: Coordinating across multiple 8xH100 or 8xA100 nodes for training extremely large vision models.

The `@distributed` decorator from the `serverless_gpu` library enables running functions across multiple GPUs on a single node, with access to local and global GPU ranks for coordinating work. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The optimized runtime environment for machine learning on Databricks.
- GPU-Accelerated Training — Best practices for using GPUs effectively in deep learning.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — Details on GPU instance availability and capacity planning.
- H100 GPU Support on Databricks — Next-generation GPU capabilities for demanding vision workloads.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Specific configuration for high-performance vision model training.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling computer vision workloads across multiple GPUs and nodes.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training for large vision models.
- [Object Detection Models](/concepts/object-detection-with-yolo11n-on-databricks.md) — Specific model architectures commonly used in vision tasks.
- Image Classification — Foundational computer vision task supported by Databricks.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
3. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
4. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
