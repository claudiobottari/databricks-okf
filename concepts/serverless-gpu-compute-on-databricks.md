---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3574784a40324d4bda0711b81c2b557859fcd15e365dd8d58fbd9d770e80459
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
    - image-classification-using-convolutional-neural-networks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-compute-on-databricks
    - SGCOD
    - Serverless Compute in Databricks
    - Serverless Compute on Databricks
    - Serverless GPU on Databricks
    - Serverless compute in Databricks
    - Serverless compute on Databricks
  citations:
    - file: train-ai-and-ml-models-databricks-on-aws.md
    - file: connect-to-ai-runtime-databricks-on-aws.md
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - file: image-classification-using-convolutional-neural-networks-databricks-on-aws.md
title: Serverless GPU Compute on Databricks
description: On-demand GPU compute resource that auto-terminates after 60 minutes of inactivity, configurable via accelerator selection like 8xH100
tags:
  - databricks
  - compute
  - GPU
timestamp: "2026-06-19T17:52:48.294Z"
---

Here is the updated wiki page for "Serverless GPU Compute on Datatabricks".

---

# Serverless GPU Compute on Databricks

**Serverless GPU Compute** is a managed, on-demand GPU infrastructure offering within Databricks that eliminates the need to provision, configure, and manage GPU clusters. It provides instant access to GPU resources for deep learning, AI, and machine learning workloads without requiring users to manage underlying infrastructure.^[train-ai-and-ml-models-databricks-on-aws.md]

## Overview

Serverless GPU Compute is part of Databricks' [serverless compute](/concepts/serverless-gpu-compute.md) ecosystem. It automatically scales GPU resources based on workload demands, providing a simplified experience where users can connect notebooks directly to GPU resources without managing cluster infrastructure.^[train-ai-and-ml-models-databricks-on-aws.md]

## Architecture

The serverless GPU compute architecture operates within the Databricks serverless compute plane, removing the need for users to manage underlying cluster infrastructure. For a detailed overview of how serverless compute fits into the Databricks architecture, see Serverless workspace architecture.^[train-ai-and-ml-models-databricks-on-aws.md]

## Key Features

### Instant Availability

Serverless GPU Compute provides instant access to GPU resources without requiring users to manage underlying cluster infrastructure. Users can connect a notebook directly to serverless GPU resources by clicking the compute drop-down at the notebook's top and selecting **Serverless GPU**.^[connect-to-ai-runtime-databricks-on-aws.md]

### Hardware Options

The platform provides access to two primary GPU types:

- **A10 GPUs**: Cost-effective GPU option suitable for tasks like image classification, natural language processing, and recommendation engines
- **H100 GPUs**: High-performance GPU for large-scale AI workloads including LLM training, [distributed fine-tuning](/concepts/unsloth-distributed-finetuning-on-databricks.md), and multi-node deep learning tasks

For distributed training workloads, the recommended accelerator is **8xH100**.^[connect-to-ai-runtime-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Managed Environments

Serverless GPU Compute offers two base environment options:

- **Default environment** (set to **None**): Provides full customization for users who want complete control over their environment and dependencies
- **AI environment** (e.g., **AI v4** or **AI v5**): Pre-loaded with common ML packages like Transformers, Ray, and other deep learning libraries, reducing setup time

### Flexible Scaling

The platform supports both single-node and multi-node deep learning workloads, with automatic scaling across multiple GPUs and nodes. For distributed training, the `@distributed` decorator configures automatic GPU provisioning, data distribution, and synchronization across multiple H100 GPUs.^[connect-to-ai-runtime-databricks-on-aws.md, distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

## How to Connect

### Interactive Notebooks

To connect a notebook to serverless GPU compute:

1. From the notebook, click the compute drop-down menu at the top and select **Serverless GPU**
2. Click the **Environment** icon to open the side panel
3. Select an accelerator from the **Accelerator** field
4. Choose **None** for the default environment or **AI v4**/ **AI v5** for the AI environment
5. Click **Apply** and confirm the environment

### Scheduled Jobs

To schedule notebooks with serverless GPU as recurring jobs:

1. Open the notebook and select the **Schedule** button on the top right
2. Select **Add schedule**
3. Populate the form with job name, schedule, and compute settings
4. Select **Create**

Dependencies for scheduled jobs must be installed programmatically within the notebook (e.g., `%pip install`). The **Environments** panel for adding dependencies is not supported for serverless GPU scheduled jobs.^[connect-to-ai-runtime-databricks-on-aws.md]

### Jobs API and Databricks Asset Bundles

To programmatically create and manage serverless GPU jobs, configure the compute type as `serverless_gpu` in your job or bundle definition. For example, a Databricks Asset Bundle configuration uses the [`Databricks Jobs API`](https://docs.databricks.com/api/workspace/jobs) and specifies `hardware_accelerator: GPU_8xH100` for the compute type.^[connect-to-ai-runtime-databricks-on-aws.md]

## Usage Patterns

### Training and Fine-Tuning

Serverless GPU Compute is optimized for single-node and multi-node deep learning workloads, including:

- **Fine-tuning large language models**: Using LoRA (Low-Rank Adaptation) to reduce trainable parameters by ~99% while maintaining model quality
- **Training computer vision models**: Using convolutional neural networks (CNNs) for image classification tasks
- **Natural language processing**: NLP tasks like training and tuning [large language models](/concepts/large-language-models-llms-on-databricks.md)
- **Object detection and classification**: Deep learning tasks for identifying and classifying objects in images
- **Recommendation engines**: Building and training recommendation systems

### Distributed Training

For multi-GPU workloads, the `@distributed` decorator configures serverless GPU compute to:^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

- **8 GPUs**: Distributes training across 8 H100 GPUs for faster training
- **Automatic orchestration**: Handles GPU provisioning, data distribution, and synchronization
- **Gradient accumulation**: Simulates larger batch sizes for stable training
- **Mixed precision (FP16)**: Faster computation with lower memory footprint
- **Gradient checkpointing**: Trades computation for memory to fit larger batches

### Model Registration and Deployment

After training, models can be registered in [Unity Catalog](/concepts/unity-catalog.md) for governance and deployment. The registration process:^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

- **MLflow Tracking**: Logs model artifacts and metadata
- **Unity Catalog**: Registers models for governance and deployment
- **Model Versioning**: Automatic versioning for model lifecycle management
- **Metadata**: Complete model information for reproducibility

## Best Practices

### Resource Management

- **Disconnect after use**: To avoid unnecessary GPU usage, manually disconnect by selecting **Connected** at the top of the notebook, hovering over **Serverless**, and selecting **Terminate**. If you don't manually disconnect, your connection auto-terminates after 60 minutes of inactivity.^[image-classification-using-convolutional-neural-networks-databricks-on-aws.md]
- **Use CPU clusters for non-GPU tasks**: For operations that do not require GPUs (e.g., cloning a Git repository, converting data formats, or exploratory data analysis), attach your notebook to a CPU cluster to preserve GPU resources.^[connect-to-ai-runtime-databricks-on-aws.md]
- **Dependency management**: For scheduled jobs, dependencies must be installed programmatically within the notebook using `%pip install`. The **Environments** panel for adding dependencies is not supported for serverless GPU scheduled jobs.^[connect-to-ai-runtime-databricks-on-aws.md]

### Performance Optimization

- **Use [Liger Kernels](/concepts/liger-kernels.md)**: GPU-optimized operations that fuse multiple steps into single kernels, reducing memory overhead by up to 80%
- **Enable mixed precision (FP16)**: Faster computation with lower memory footprint for training
- **Configure [gradient checkpointing](/concepts/activation-checkpointing.md)**: Trades computation for memory to fit larger batches
- **Implement gradient accumulation**: Simulates larger batch sizes for stable training^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Model Checkpointing

For workloads that may exceed the 7-day maximum runtime, implement manual checkpointing to allow resumption. Use [Unity Catalog](/concepts/unity-catalog.md) volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data` for model checkpointing.^[connect-to-ai-runtime-databricks-on-aws.md]

## Limitations and Considerations

### Auto-Recovery

Auto-recovery is not supported for serverless GPU scheduled jobs. If a job fails due to incompatible packages, it must be manually fixed and re-run.^[connect-to-ai-runtime-databricks-on-aws.md]

### Maximum Runtime

Serverless GPU compute has a 7-day maximum runtime for workloads. For longer-running tasks, implement manual checkpointing to allow resumption.^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- Serverless Compute — The broader serverless compute infrastructure
- [AI Runtime](/concepts/ai-runtime.md) — Specialized deep learning runtime within serverless GPU
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built ML runtime
- GPU Scheduling — Optimizing GPU utilization
- [Unity Catalog](/concepts/unity-catalog.md) — Model governance and deployment
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registration
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU training techniques
- LoRA — Parameter-efficient fine-tuning
- [Liger Kernels](/concepts/liger-kernels.md) — Memory-efficient training optimizations
- Model Checkpointing — Resumable training for long-running jobs

## Sources

- connect-to-ai-runtime-databricks-on-aws.md
- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
- image-classification-using-convolutional-neural-networks-databricks-on-aws.md
- train-ai-and-ml-models-databricks-on-aws.md

# Citations

1. [train-ai-and-ml-models-databricks-on-aws.md](/references/train-ai-and-ml-models-databricks-on-aws-b6078c61.md)
2. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
3. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
4. [image-classification-using-convolutional-neural-networks-databricks-on-aws.md](/references/image-classification-using-convolutional-neural-networks-databricks-on-aws-0a8afbcf.md)
