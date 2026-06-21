---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aae9e8a27a0581b216962da62b50fe773da287ffa48f90f072ab6ed72d4c028b
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-infrastructure
    - SGI
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: Serverless GPU Infrastructure
description: Fully managed, flexible access to GPUs on Databricks without cluster configuration, driver selection, or autoscaling policies.
tags:
  - databricks
  - infrastructure
  - gpu
timestamp: "2026-06-18T14:22:43.495Z"
---

# Serverless GPU Infrastructure

**Serverless GPU Infrastructure** refers to fully managed, on-demand GPU compute resources that require no cluster configuration, driver selection, or autoscaling policy management. In the Databricks ecosystem, this capability is delivered through [AI Runtime](/concepts/ai-runtime.md), a compute offering designed for deep learning workloads that brings GPU support to Databricks Serverless.^[ai-runtime-databricks-on-aws.md]

## Overview

Serverless GPU infrastructure eliminates the operational overhead traditionally associated with GPU computing. Users can access GPU resources interactively from notebooks, schedule notebooks as recurring jobs, or programmatically create jobs using the Jobs API and Databricks Asset Bundles — all without provisioning or managing underlying infrastructure.^[ai-runtime-databricks-on-aws.md]

This model is particularly suited for custom model training use cases involving deep learning, including [LLM fine-tuning](/concepts/llm-fine-tuning-on-databricks.md) (LoRA, QLoRA, full fine-tuning), computer vision (object detection, image classification), deep-learning-based recommender systems, reinforcement learning, and deep-learning-based time series forecasting.^[ai-runtime-databricks-on-aws.md]

## Key Features

- **Fully managed GPU infrastructure** — Serverless, flexible access to GPUs with no cluster configuration, driver selection, or autoscaling policies to manage.^[ai-runtime-databricks-on-aws.md]
- **A runtime dedicated for deep learning** — Choose either a minimal default base environment for maximum flexibility over dependencies or a full-featured AI environment pre-loaded with popular ML frameworks like PyTorch and Transformers.^[ai-runtime-databricks-on-aws.md]
- **Natively integrated** across notebooks, jobs, [Unity Catalog](/concepts/unity-catalog.md), and [MLflow](/concepts/mlflow.md) for seamless development, data access, and experiment tracking.^[ai-runtime-databricks-on-aws.md]

## Hardware Options

All AI Runtime accelerators provision a single node. The number of GPUs on that node depends on the accelerator type. AI Runtime supports A10 and H100 accelerators. The 1xH100 accelerator is in Beta and requires workspace admin enablement.^[ai-runtime-databricks-on-aws.md]

## Distributed Training

AI Runtime supports distributed training across multiple GPUs on the single node the notebook is connected to. Using the `@distributed` decorator from the `serverless_gpu` Python API (Beta), users can launch multi-GPU workloads with [PyTorch DDP](/concepts/pytorch-ddp-on-databricks.md), [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md), or [DeepSpeed](/concepts/deepspeed.md) with minimal configuration.^[ai-runtime-databricks-on-aws.md]

## Requirements

- A workspace in one of the supported AWS regions: `us-west-2`, `us-west-1`, `us-east-1`, `us-east-2`, `ca-central-1`, or `sa-east-1`.^[ai-runtime-databricks-on-aws.md]
- The AI Runtime preview must be enabled via workspace admin settings.^[ai-runtime-databricks-on-aws.md]

## Limitations

- AI Runtime only supports A10 and H100 accelerators.^[ai-runtime-databricks-on-aws.md]
- AI Runtime is **not supported for compliance security profile workspaces** (such as HIPAA or PCI). Processing regulated data is not supported.^[ai-runtime-databricks-on-aws.md]
- Adding dependencies using the **Environments** panel is not supported for AI Runtime scheduled jobs. Install dependencies programmatically using `%pip install` in the notebook instead.^[ai-runtime-databricks-on-aws.md]
- For scheduled jobs on AI Runtime, auto recovery behavior for incompatible package versions associated with the notebook is not supported.^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a workload is seven days. For model training jobs that exceed this limit, implement checkpointing and restart the job once the maximum runtime is reached.^[ai-runtime-databricks-on-aws.md]
- AI Runtime provides on-demand access to GPU resources, which may lead to periods where capacity is constrained or unavailable in the region.^[ai-runtime-databricks-on-aws.md]
- AI Runtime leverages cross-region GPUs in certain cases during moments of high demand. There may be egress costs associated with such usage, and cross-region network connectivity might be limited at certain times.^[ai-runtime-databricks-on-aws.md]

## Environment Setup

AI Runtime offers two managed Python environments: a minimal default base environment for maximum dependency flexibility, and a full-featured Databricks AI environment pre-loaded with popular ML frameworks. Users should understand data access patterns on AI Runtime for a smooth experience.^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The compute offering that delivers serverless GPU infrastructure
- Databricks Serverless — The serverless compute architecture underlying AI Runtime
- LLM Fine-Tuning — A primary use case for serverless GPU infrastructure
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU workload support via the `@distributed` decorator
- [MLflow](/concepts/mlflow.md) — Experiment tracking and observability integration
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance integration for model management

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
