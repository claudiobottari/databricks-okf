---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c0605f7c3ad423043e3f4f8381c9c1baa0b57f94f08e56724b5848dc4a73ed6
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-environments
    - ARE
    - AI Runtime Environment
    - AI Runtime environment
    - AI Environment
    - AI Runtime (Preview)|AI Runtime
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Environments
description: "Two managed Python environments for AI Runtime: a minimal default base environment for maximum dependency flexibility, and a full-featured Databricks AI environment pre-loaded with popular ML frameworks like PyTorch and Transformers."
tags:
  - databricks
  - python
  - environment-management
  - deep-learning
timestamp: "2026-06-19T22:04:02.937Z"
---

# AI Runtime Environments

**AI Runtime Environments** are the pre-configured Python environments provided by [AI Runtime](/concepts/ai-runtime.md) on Databricks. AI Runtime is a compute offering for Deep Learning workloads that brings GPU support to Databricks Serverless, enabling training and fine-tuning of custom models. ^[ai-runtime-databricks-on-aws.md]

## Overview

AI Runtime offers two managed Python environments to suit different needs: a minimal **default base environment** for maximum flexibility over dependencies, and a full-featured **Databricks AI environment** that is pre-loaded with popular ML frameworks such as PyTorch and Transformers. ^[ai-runtime-databricks-on-aws.md]

These environments are selected when connecting to AI Runtime from notebooks, scheduled jobs, or programmatically through the Databricks Jobs API and Databricks Asset Bundles. ^[ai-runtime-databricks-on-aws.md]

## Default Base Environment

The default base environment is a minimal Python environment that provides only the essential system libraries. It gives you full control over which packages to install, making it suitable for users who want to manage their own dependency stack or use custom versions of frameworks. ^[ai-runtime-databricks-on-aws.md]

## AI Environment

The AI environment (referred to as the *Databricks AI environment*) is a pre-configured, full-featured environment that bundles popular machine learning and deep learning frameworks, including PyTorch and Transformers, among others. It is designed to accelerate development by eliminating the need to manually install common libraries for distributed GPU workloads. ^[ai-runtime-databricks-on-aws.md]

## Selecting an Environment

When connecting to AI Runtime, you choose the environment based on your workload:

- **Simplified selection**: In the notebook interface, the environment is selected as part of the compute setup. Users choose an accelerator (e.g., A10 or H100) and then pick either the default base environment or the AI environment.
- **Jobs API and Asset Bundles**: When defining jobs, the environment is specified in the YAML configuration using the `base_environment` field (e.g., `databricks_ai_v5` for the AI environment).

For detailed steps, see the guide on Connect to AI Runtime.

## Best Practices

- **Default environment** is recommended when you need to use specific package versions or minimize the environment footprint.
- **AI environment** is recommended for most deep learning tasks, as it comes with optimized versions of PyTorch and Transformers, reducing setup time.
- For scheduled jobs, dependencies must be installed programmatically (e.g., with `%pip install`) because the **Environments** panel is not supported for AI Runtime scheduled jobs. Auto-recovery for incompatible package versions is also not supported. ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a workload is seven days; implement checkpointing for longer training runs. ^[ai-runtime-databricks-on-aws.md]
- AI Runtime accelerators are provisioned on a single node. Multi-GPU workloads use the `@distributed` decorator from the `serverless_gpu` Python API. ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The full compute offering for deep learning.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The underlying serverless infrastructure.
- PyTorch — Framework included in the AI environment.
- Transformers — Library included in the AI environment.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU workload support via `@distributed`.
- [MLflow](/concepts/mlflow.md) — Experiment tracking integrated with AI Runtime.
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance integrated with AI Runtime.

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
