---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16e6a47ab290f0a5f81108bfd0ef2101dcab624964299f2c18268da66a138041
  pageDirectory: concepts
  sources:
    - distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
    - fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - train-a-retinanet-image-detection-model-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-compute
    - DSGC
    - Databricks Serverless Compute
    - Databricks serverless compute
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
    - file: train-a-retinanet-image-detection-model-databricks-on-aws.md
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
    - file: fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md
    - file: fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
    - file: fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: Databricks Serverless GPU Compute
description: Databricks managed compute service that automatically scales GPU resources and handles provisioning, data distribution, and synchronization for distributed training workloads.
tags:
  - infrastructure
  - cloud-computing
  - gpu
timestamp: "2026-06-19T18:33:34.591Z"
---

# Databricks Serverless GPU Compute

**Databricks Serverless GPU Compute** is a managed compute offering on Databricks that automatically provisions and scales GPU resources for machine learning workloads, including training, fine-tuning, and inference. It eliminates the need to manually configure and manage GPU clusters, providing on-demand access to GPU accelerators directly from notebooks.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

Serverless GPU Compute uses the **AI Runtime**, a managed environment that automatically scales GPU resources and includes pre-installed deep learning libraries. Key capabilities include on-demand GPU provisioning, distributed training support, integrated MLflow logging, and [Unity Catalog](/concepts/unity-catalog.md) model registration.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

## GPU Accelerator Options

Serverless GPU Compute offers multiple GPU accelerator configurations depending on workload requirements:^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, train-a-retinanet-image-detection-model-databricks-on-aws.md]

| Accelerator | Use Case |
|-------------|----------|
| **1xA10** | Single-GPU training, small to medium models, inference |
| **8xH100** | Large model training, distributed training, models requiring high throughput and large GPU memory |

H100 GPUs offer larger floating-point operations per second (FLOPS) and high-bandwidth memory (HBM) compared to A10 GPUs. Use H100s for large model training where high throughput or large GPU memory is needed.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Connecting to Serverless GPU Compute

To connect a notebook to serverless GPU compute:^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

1. Click the notebook's compute selector in the top right and select **Serverless GPU**.
2. On the right side, click the environment button.
3. Select an **Accelerator** (e.g., **8xH100**).
4. Choose an **Environment** (e.g., **AI v5**) that contains the required libraries.
5. Click **Apply**.

## The `serverless_gpu` Library

The `serverless_gpu` Python library is the primary interface for running distributed GPU workloads directly from Databricks notebooks. It provides decorators and runtime utilities for distributed GPU computing.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### The `@distributed` Decorator

The `@distributed` decorator enables multi-GPU distributed execution by annotating a Python function. It handles provisioning GPUs, setting up the distributed environment, and managing the lifecycle of remote compute resources.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='h100')
def train_model():
    # Training logic here
    pass

# Execute distributed training
train_model.distributed()
```

The decorator accepts parameters including `gpus` (number of GPUs) and `gpu_type` (accelerator type). Functions annotated with this decorator use the `runtime` module to access local and global GPU ranks via `rt.get_local_rank()` and `rt.get_global_rank()`.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### The `distributed()` Method

After defining a function with the `@distributed` decorator, calling `.distributed()` triggers remote execution on serverless GPU compute. The method handles all distributed coordination across GPUs.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Workloads and Use Cases

### Large Language Model Fine-Tuning

Fine-tune models such as OpenAI's gpt-oss-20b (20 billion parameters) and gpt-oss-120b using parameter-efficient techniques like LoRA, QLoRA, and MXFP4 quantization. Distributed training across 8 H100 GPUs is typical for these workloads.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md]

### Distributed Training with PyTorch FSDP

Use PyTorch's Fully Sharded Data Parallel (FSDP) to shard model parameters, gradients, and optimizer states across multiple GPUs. This enables training of large models that do not fit on a single GPU. The example notebook demonstrates training a 10M parameter Transformer model using FSDP on 8 H100 GPUs with synthetic data.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

### Fine-Tuning with Axolotl

Leverage the Axolotl framework for efficient LLM fine-tuning with QLoRA on multi-GPU infrastructure. Axolotl provides high-performance configurations for fine-tuning models like Olmo3 7B Instruct with Flash Attention and Cut Cross Entropy optimization, with MLflow integration for experiment tracking and Unity Catalog model registration.^[fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

### Fine-Tuning with Mosaic LLM Foundry

Use Mosaic LLM Foundry for training, fine-tuning, and evaluating large language models with built-in support for FSDP, efficient data loading, and MLflow integration. This framework is demonstrated for fine-tuning Llama 3.1 8B on 8 H100 GPUs.^[fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md]

### Supervised Fine-Tuning with TRL and DeepSpeed

Use the Transformers Reinforcement Learning (TRL) library with DeepSpeed ZeRO Stage 3 optimization to efficiently train models like Llama 3.2 1B on 8 H100 GPUs. DeepSpeed partitions model parameters, gradients, and optimizer states across GPUs to reduce memory consumption.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

### Image Detection Model Training

Train computer vision models such as RetinaNet from scratch using PyTorch and torchvision with a ResNet-50 backbone. Scale from single-GPU (1xA10) to multi-GPU (8xH100) training using Distributed Data Parallel (DDP) with COCO dataset support.^[train-a-retinanet-image-detection-model-databricks-on-aws.md]

### Time Series Forecasting

Train probabilistic forecasting models like DeepAR using GluonTS. Serverless GPU compute accelerates model training for time series prediction tasks.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Distributed Training Strategies

- **Data Parallelism (DDP)**: Distribute training data across multiple GPUs, each holding a copy of the model. Gradients are synchronized after each batch. Suitable for models that fit within a single GPU's memory.^[train-a-retinanet-image-detection-model-databricks-on-aws.md]
- **Fully Sharded Data Parallel (FSDP)**: Shard model parameters, gradients, and optimizer states across GPUs to reduce per-GPU memory requirements and enable training of larger models.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **DeepSpeed ZeRO Stage 3**: Partition all model states across GPUs with bfloat16 precision optimization. Commonly used with TRL's SFTTrainer for supervised fine-tuning.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **LoRA and QLoRA**: Reduce trainable parameters by adding small adapter layers (LoRA) or combining with 4-bit quantization (QLoRA) to further reduce memory requirements.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]

## Unity Catalog Integration

Serverless GPU compute integrates with Unity Catalog for model and artifact storage:^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

- **Checkpoints** are saved to Unity Catalog volumes (e.g., `/Volumes/<catalog>/<schema>/<volume>/<model_name>`).
- **Models** can be registered in Unity Catalog via MLflow after training for deployment.
- **Datasets** stored in Unity Catalog volumes are accessible during training.

## MLflow Integration

Training runs on serverless GPU compute automatically integrate with [MLflow](/concepts/mlflow.md) for experiment tracking. Metrics such as loss, average loss, and training time are logged during training. After training, models can be registered to the MLflow registry with Unity Catalog registration for deployment to [Model Serving](/concepts/model-serving.md).^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md, distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

## Best Practices

- **Select the right accelerator**: Use A10 GPUs for single-GPU workloads and H100 GPUs for large model training or distributed training requiring high throughput.^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Tune batch size per GPU**: Adjust batch size based on GPU type (e.g., batch size 8 for H100 in RetinaNet training, batch size 2 for H100 in RetinaNet DDP training).^[train-a-retinanet-image-detection-model-databricks-on-aws.md]
- **Set prefetch factor**: Use prefetch_factor=4 with H100 GPUs for optimal data loading performance.^[train-a-retinanet-image-detection-model-databricks-on-aws.md]
- **Use gradient checkpointing**: Enable gradient checkpointing to reduce memory usage during training of large models.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md, fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md]
- **Use bfloat16 precision**: Enable bfloat16 for faster training and reduced memory usage on H100 hardware.^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]
- **Save checkpoints regularly**: Save to Unity Catalog volumes to enable recovery and continued training.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- **Use MLflow for tracking**: Log metrics, parameters, and model artifacts for reproducibility and comparison.

## Troubleshooting

Common issues and solutions for serverless GPU compute workloads are documented in the Troubleshoot Issues on Serverless GPU Compute guide.^[distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md]

For more information, see:
- [Serverless GPU API documentation](https://api-docs.databricks.com/python/serverless_gpu/index.html)
- [Best practices for Serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
- [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The managed runtime that automatically scales GPU resources
- [Serverless GPU API Documentation](/concepts/serverless-gpu-api.md) — The Python API reference for the `serverless_gpu` library
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Distributed training strategy for large models
- [DeepSpeed](/concepts/deepspeed.md) — Memory optimization for distributed training
- LoRA — Parameter-efficient fine-tuning technique
- [Model Serving](/concepts/model-serving.md) — Deploying fine-tuned models for inference
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for storing models, datasets, and artifacts
- [Multi-GPU Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Different distributed training strategies available
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — Another GPU option for deep learning workloads
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Specific H100 configuration for distributed workloads

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
- fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md
- fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md
- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
- train-a-retinanet-image-detection-model-databricks-on-aws.md
- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
2. [distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md](/references/distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws-7ee24e1a.md)
3. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
4. [train-a-retinanet-image-detection-model-databricks-on-aws.md](/references/train-a-retinanet-image-detection-model-databricks-on-aws-f9a3d9a2.md)
5. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
6. [fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws.md](/references/fine-tune-openais-gpt-oss-120b-model-using-distributed-training-databricks-on-aws-9fff83fc.md)
7. [fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws.md](/references/fine-tune-olmo3-7b-with-axolotl-on-multi-gpu-serverless-compute-databricks-on-aws-c7178be1.md)
8. [fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws.md](/references/fine-tune-llama-31-8b-using-mosaic-llm-foundry-on-databricks-serverless-gpu-databricks-on-aws-d6760424.md)
9. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
