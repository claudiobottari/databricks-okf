---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7046ff36b81c3a046337a9c24c491fc61ab1d7fb4ca3dbe353964cea452cee91
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
    - ai-runtime-example-notebooks-databricks-on-aws.md
    - large-language-models-llms-databricks-on-aws.md
    - set-up-your-environment-databricks-on-aws.md
    - train-ai-and-ml-models-databricks-on-aws.md
    - user-guides-for-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-runtime-databricks
    - AR(
  citations:
    - file: train-ai-and-ml-models-databricks-on-aws.md
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
    - file: set-up-your-environment-databricks-on-aws.md
    - file: user-guides-for-ai-runtime-databricks-on-aws.md
    - file: ai-runtime-cli-databricks-on-aws.md
    - file: large-language-models-llms-databricks-on-aws.md
title: AI Runtime (Databricks)
description: Databricks' on-demand serverless GPU compute platform designed for machine learning training workloads
tags:
  - databricks
  - gpu-computing
  - serverless
  - machine-learning
timestamp: "2026-06-19T22:02:29.692Z"
---

# AI Runtime (Databricks)

**AI Runtime** is a serverless GPU compute environment within the Databricks ecosystem, optimized for custom single-node and multi-node deep learning workloads such as fine-tuning large language models (LLMs), training computer vision models, and building recommendation systems.^[train-ai-and-ml-models-databricks-on-aws.md] It is a specialized offering within the Databricks serverless compute plane, removing the need to manage underlying cluster infrastructure.^[train-ai-and-ml-models-databricks-on-aws.md]

AI Runtime for single-node tasks is in **Public Preview**; the distributed training API for multi-GPU workloads remains in **Beta**.^[ai-runtime-example-notebooks-databricks-on-aws.md, set-up-your-environment-databricks-on-aws.md, user-guides-for-ai-runtime-databricks-on-aws.md]

## Key Features

- **Instant availability**: Connect a notebook directly to serverless GPU resources without provisioning or managing clusters.^[train-ai-and-ml-models-databricks-on-aws.md]
- **High-performance hardware**: Provides access to A10 GPUs ($2.50/GPU hour) for cost-effective tasks and H100 GPUs ($7.00/GPU hour) for large-scale AI workloads.^[train-ai-and-ml-models-databricks-on-aws.md, user-guides-for-ai-runtime-databricks-on-aws.md]
- **Managed environments**: Offers a default base environment (minimal, with `torch`, `cuda`, `torchvision`) or the Databricks AI environment (pre-loaded with Transformers, Ray, and other ML/DL packages).^[train-ai-and-ml-models-databricks-on-aws.md, set-up-your-environment-databricks-on-aws.md]
- **Flexible scaling**: Supports distributed training across multiple GPUs and nodes via the `@distributed` decorator from the `serverless_gpu` library.^[train-ai-and-ml-models-databricks-on-aws.md, user-guides-for-ai-runtime-databricks-on-aws.md]
- **AI Runtime CLI (Beta)**: A command-line interface (`air`) to submit and manage distributed training workloads using YAML-based job configuration, with MLflow integration and support for workspace-based or git-based code workflows.^[ai-runtime-cli-databricks-on-aws.md]

## Environments

AI Runtime provides two managed Python environments:^[set-up-your-environment-databricks-on-aws.md]

- **Default base environment**: A minimal, stable environment containing only required packages (`torch`, `cuda`, `torchvision`). Best for users who want full control over dependencies. This is the default when connecting to serverless GPU via AI Runtime.^[set-up-your-environment-databricks-on-aws.md]
- **Databricks AI environment** (available in environment v4+): Built on top of the base environment with pre-installed packages including PyTorch (with CUDA), Hugging Face Transformers, and additional ML/DL dependencies. Best for ML practitioners. To select, choose **AI v5** or **AI v4** from the Environment side panel.^[set-up-your-environment-databricks-on-aws.md]

Environments are cached across sessions to speed startup times, but cache behavior is not guaranteed; always include explicit `%pip install` commands for reproducibility.^[set-up-your-environment-databricks-on-aws.md]

Custom modules can be imported by placing them in `/Workspace/Shared` and appending the path to `sys.path`.^[set-up-your-environment-databricks-on-aws.md]

### Limitations

AI Runtime does not support: Spark functions (PySpark) – it is a Python-only environment (Spark Connect is available for data loading); Databricks Runtime ML pre-installed libraries – many are not available, so explicit `%pip install` is required; private artifacts in some cases.^[set-up-your-environment-databricks-on-aws.md]

## AI Runtime CLI

The `air` CLI (Beta) enables submitting GPU training workloads from the command line without opening a notebook. Jobs are defined declaratively in YAML and can be checked into source control. The CLI supports workspace-based and git-based code workflows and integrates with MLflow for run tracking.^[ai-runtime-cli-databricks-on-aws.md]

For the in-notebook Python API (`@distributed` and `@ray_launch`), see Multi-GPU Workload.

## Example Notebooks

Example notebooks are available for the following tasks:^[ai-runtime-example-notebooks-databricks-on-aws.md]

- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) – fine-tuning including parameter-efficient methods (e.g., LoRA) and full supervised fine-tuning.^[large-language-models-llms-databricks-on-aws.md]
- [Computer Vision](/concepts/computer-vision-on-databricks.md) – object detection and image classification.
- [Deep learning based recommender systems](/concepts/deep-learning-based-recommender-systems.md) – two-tower models and other modern approaches.
- Classic ML – XGBoost training and time series forecasting.
- [Multi-GPU Distributed Training](/concepts/multi-gpu-distributed-training-api.md) – scaling across multiple GPUs and nodes.

## Migrating from Classic GPU Workloads

When migrating a deep learning workload from Databricks Runtime ML (classic clusters) to AI Runtime (serverless), follow these steps:^[user-guides-for-ai-runtime-databricks-on-aws.md]

1. Replace Spark-based distributed training (e.g., `TorchDistributor`) with the `@distributed` decorator from `serverless_gpu`.
2. Update data loading: replace DBFS paths with Unity Catalog volumes paths (`/Volumes/...`) and use `UCVolumeDataset` from `serverless_gpu.data` for streaming file-based data.
3. Reinstall dependencies explicitly using `%pip install` – do not rely on Databricks Runtime ML pre-installed libraries.
4. Move checkpoints to Unity Catalog volumes; use `UCVolumeWriter` and `UCVolumeReader` for distributed checkpointing.
5. Update MLflow experiment names to absolute paths and configure run names for restartability.
6. Test interactively before scheduling as a job.

## Troubleshooting

Common issues include:^[user-guides-for-ai-runtime-databricks-on-aws.md]

- **NumPy ABI incompatibility**: Occurs when installed packages require a different NumPy version than the runtime environment. Check the runtime NumPy version via release notes and pin a compatible version.
- **PyTorch cannot find libcudnn**: When installing a different version of `torch`, you may see `ImportError: libcudnn.so.9`. Reinstall with `%pip install torch --force-reinstall`.

Genie Code can help diagnose library installation errors.^[user-guides-for-ai-runtime-databricks-on-aws.md]

## Pricing

AI Runtime charges per GPU hour under the Model Training SKU:^[user-guides-for-ai-runtime-databricks-on-aws.md]

- H100 on demand: $7.00/GPU hour (US East)
- A10 on demand: $2.50/GPU hour (US East)

Usage can be tracked via the `system.billing.usage` system table, filtering on `product_features.serverless_gpu IS NOT NULL`.

## Related Concepts

- Serverless Compute — Architectural overview of Databricks serverless compute plane.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Classic compute environment for ML workloads.
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and access control for volumes and checkpoints.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient distributed training strategy.
- [MLflow](/concepts/mlflow.md) — Run tracking and experiment management integrated with AI Runtime CLI.
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — Fine-tuning workloads supported by AI Runtime.

## Sources

- ai-runtime-cli-databricks-on-aws.md
- ai-runtime-example-notebooks-databricks-on-aws.md
- large-language-models-llms-databricks-on-aws.md
- set-up-your-environment-databricks-on-aws.md
- train-ai-and-ml-models-databricks-on-aws.md
- user-guides-for-ai-runtime-databricks-on-aws.md

# Citations

1. [train-ai-and-ml-models-databricks-on-aws.md](/references/train-ai-and-ml-models-databricks-on-aws-b6078c61.md)
2. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
3. [set-up-your-environment-databricks-on-aws.md](/references/set-up-your-environment-databricks-on-aws-10c7d209.md)
4. [user-guides-for-ai-runtime-databricks-on-aws.md](/references/user-guides-for-ai-runtime-databricks-on-aws-495c5d9c.md)
5. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
6. [large-language-models-llms-databricks-on-aws.md](/references/large-language-models-llms-databricks-on-aws-bfc38cd2.md)
