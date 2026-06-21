---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43ee7cacc8502af5c6e70cb26fac992607a1383f41f4bd29c1eac68f9ba11a25
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
    - computer-vision-databricks-on-aws.md
    - distributed-fine-tuning-of-openai-gpt-oss-20b-databricks-on-aws.md
    - distributed-training-using-deepspeed-databricks-on-aws.md
    - fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
    - multi-gpu-distributed-training-databricks-on-aws.md
    - yolo11n-object-detection-on-databricks-ai-runtime-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime
    - DAR
    - Data loading on AI Runtime
  citations:
    - file: ai-runtime-databricks-on-aws.md
    - file: computer-vision-databricks-on-aws.md
    - file: fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
    - file: yolo11n-object-detection-on-databricks-ai-runtime-databricks-on-aws.md
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
title: Databricks AI Runtime
description: A serverless GPU compute offering on Databricks for deep learning workloads, providing fully managed GPU infrastructure with native integration across notebooks, jobs, Unity Catalog, and MLflow.
tags:
  - databricks
  - machine-learning
  - compute
  - deep-learning
timestamp: "2026-06-19T22:03:46.537Z"
---

# Databricks AI Runtime

**Databricks AI Runtime** is a serverless compute offering on Databricks designed for deep learning workloads, bringing GPU support to Databricks Serverless. It enables training and fine‑tuning of custom models using frameworks like PyTorch and Transformers without requiring users to manage cluster infrastructure. ^[ai-runtime-databricks-on-aws.md]

## Key features

- **Fully managed GPU infrastructure** — Serverless, flexible access to GPUs with no cluster configuration, driver selection, or autoscaling policies to manage. ^[ai-runtime-databricks-on-aws.md]
- **Two managed Python environments** — A minimal default base environment for maximum flexibility over dependencies, or a full‑featured **Databricks AI** environment pre‑loaded with popular ML frameworks such as PyTorch and Transformers. ^[ai-runtime-databricks-on-aws.md]
- **Natively integrated** across notebooks, jobs, [Unity Catalog](/concepts/unity-catalog.md), and [MLflow](/concepts/mlflow.md) for seamless development, data access, and experiment tracking. ^[ai-runtime-databricks-on-aws.md]
- **Distributed training** — Multi‑GPU workloads on a single node using the `@distributed` decorator (Beta) from the `serverless_gpu` Python API. ^[ai-runtime-databricks-on-aws.md]

## Hardware options

All AI Runtime accelerators provision a single node. The number of GPUs depends on the accelerator type. Supported GPUs are:

- **A10** — Available for general GPU workloads.
- **H100** — Available in configurations such as 8xH100. The 1xH100 accelerator is in Beta and requires workspace admin preview enablement. ^[ai-runtime-databricks-on-aws.md]

For a full description of the 8‑GPU configuration, see [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md).

## Recommended use cases

AI Runtime is recommended for any custom model training that involves deep learning, large‑scale classic workloads, or GPUs. Examples include: ^[ai-runtime-databricks-on-aws.md]

- LLM fine‑tuning (LoRA, QLoRA, full fine‑tuning)
- Computer vision (object detection, image classification)
- Deep‑learning‑based recommender systems
- Reinforcement learning
- Deep‑learning‑based time series forecasting

Concrete tutorial notebooks are available for image classification, object detection with RetinaNet, and object detection with YOLO11n. ^[computer-vision-databricks-on-aws.md]

## Requirements and limitations

### Requirements

- Workspace in a supported AWS region: `us-west-2`, `us-west-1`, `us-east-1`, `us-east-2`, `ca-central-1`, or `sa-east-1`.
- The AI Runtime preview must be enabled via workspace admin settings. ^[ai-runtime-databricks-on-aws.md]

### Limitations

- AI Runtime only supports A10 and H100 accelerators.
- Not supported for compliance security profile workspaces (HIPAA or PCI). Processing regulated data is not supported.
- Adding dependencies using the **Environments** panel is not supported for scheduled jobs; use `%pip install` in your notebook instead.
- The maximum runtime for a single workload is seven days. For longer training, implement checkpointing and restart.
- On‑demand GPU capacity may be constrained or unavailable during periods of high demand. AI Runtime may leverage cross‑region GPUs, incurring egress costs and potential network limitations. ^[ai-runtime-databricks-on-aws.md]

## Connecting to AI Runtime

You can connect to AI Runtime interactively from notebooks, schedule notebooks as recurring jobs, or programmatically create jobs using the Jobs API and Databricks Asset Bundles. ^[ai-runtime-databricks-on-aws.md]

To connect from a notebook:
1. Click the compute selector and choose **Serverless GPU**.
2. Select an **Accelerator** (e.g., 8xH100).
3. Choose an **Environment** (e.g., **AI v5** for the full‑featured AI environment).
4. Click **Apply**. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

Additional Python packages can be installed with `%pip install` in the notebook. The environment caches installed packages for subsequent sessions. ^[ai-runtime-databricks-on-aws.md]

## Environment setup

The Databricks AI environment (AI v5) pre‑bundles core libraries including `mlflow>=3` (skinny), `torch`, and `nvidia-ml-py`. Only additional libraries such as `ultralytics` or `deepspeed` need separate installation. ^[yolo11n-object-detection-on-databricks-ai-runtime-databricks-on-aws.md] ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

For fine‑tuning with Unsloth on A10 GPUs, the AI v5 environment includes `unsloth`, `unsloth_zoo`, `bitsandbytes`, `trl`, `xformers`, and `mlflow`, so no additional installation is needed. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Distributed training

AI Runtime supports distributed training across multiple GPUs on a single node using the `@distributed` decorator from the `serverless_gpu` library (Beta). The decorator provisions the requested GPUs, sets up the distributed environment, and executes the training function with frameworks such as PyTorch DDP, FSDP, or DeepSpeed with minimal configuration. ^[ai-runtime-databricks-on-aws.md]

Example notebook demonstrations include:
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training for models that fit in single‑GPU memory.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) for models that exceed single‑GPU memory.
- [DeepSpeed](/concepts/deepspeed.md) ZeRO Stage 3 optimization for memory‑efficient training of models such as Llama 3.2‑1B on 8 H100 GPUs. ^[ai-runtime-databricks-on-aws.md] ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md]

For training models with 20B to 120B+ parameters, see [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md).

## Experiment tracking and model management

Training metrics are automatically logged to [MLflow](/concepts/mlflow.md) when using `@distributed`. Model checkpoints can be saved to a [Unity Catalog](/concepts/unity-catalog.md) volume. After training, models can be logged to MLflow and registered in Unity Catalog for deployment to Model Serving endpoints. ^[fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md] ^[yolo11n-object-detection-on-databricks-ai-runtime-databricks-on-aws.md]

For detailed guidance on experiment tracking, log viewing, and checkpoint management, see the official documentation on experiment tracking and observability. ^[ai-runtime-databricks-on-aws.md]

## Genie Code support

Genie Code supports deep learning workloads on AI Runtime. It can help generate training code, resolve library installation errors, suggest optimizations, and debug common issues. ^[ai-runtime-databricks-on-aws.md]

## Related concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The underlying infrastructure for AI Runtime.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Classic GPU runtime for clusters.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – Details on the 8‑GPU H100 setup.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Parallelism technique for multi‑GPU training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Advanced sharding for large models.
- [DeepSpeed](/concepts/deepspeed.md) – Memory optimization for large model training.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – Parameter range where FSDP is essential.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance for ML assets.
- [Model Serving](/concepts/model-serving.md) – Deploying registered models to endpoints.

## Sources

- ai-runtime-databricks-on-aws.md
- computer-vision-databricks-on-aws.md
- fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md
- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
- yolo11n-object-detection-on-databricks-ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
2. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
3. [fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws.md](/references/fine-tune-llama-32-1b-using-ai-runtime-databricks-on-aws-4a3f88ec.md)
4. [yolo11n-object-detection-on-databricks-ai-runtime-databricks-on-aws.md](/references/yolo11n-object-detection-on-databricks-ai-runtime-databricks-on-aws-d5edeb53.md)
5. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
