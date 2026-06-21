---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a34635107fe80d1664f1ce1d211c29a92c437fa358e65e4663d5c31a6cad6110
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-managed-environments
    - ARME
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Managed Environments
description: "Two Python environments offered by AI Runtime: a minimal default base environment and a full-featured Databricks AI environment pre-loaded with ML frameworks"
tags:
  - python
  - environment-management
  - ml-frameworks
timestamp: "2026-06-19T17:31:29.534Z"
---

# AI Runtime Managed Environments

**AI Runtime Managed Environments** are pre-configured Python environments provided by [AI Runtime](/concepts/ai-runtime.md) on Databricks Serverless. They offer two options: a minimal base environment for maximum dependency flexibility and a full-featured AI environment pre-loaded with popular deep learning frameworks like PyTorch and Transformers.^[ai-runtime-databricks-on-aws.md]

## Overview

When connecting to AI Runtime, users can select one of two managed Python environments. These environments eliminate the need to manually install common ML libraries and ensure compatibility with the underlying GPU infrastructure. The choice depends on whether you require a lightweight starting point or an out-of-the-box environment with widely used frameworks.^[ai-runtime-databricks-on-aws.md]

### Minimal Default Base Environment

The minimal base environment provides a clean Python installation with few pre-installed packages. It is intended for users who want full control over dependencies, such as specifying exact versions of PyTorch, TensorFlow, or other libraries. You can install additional packages at runtime using `%pip install` in a notebook or by including them in your job configuration.^[ai-runtime-databricks-on-aws.md]

### Full-Featured Databricks AI Environment

The full-featured AI environment comes pre-loaded with popular ML frameworks including PyTorch and Transformers, as well as other commonly used libraries for deep learning. It is optimized for AI Runtime's GPU accelerators and is the recommended choice for most training and fine-tuning workloads, such as [LLM Fine-tuning](/concepts/llm-fine-tuning-on-databricks.md), computer vision, and recommendation systems.^[ai-runtime-databricks-on-aws.md]

## Choosing an Environment

The Databricks AI environment is suitable for most users because it eliminates the setup overhead of common dependencies. Use the minimal environment if your workflow requires a specific library version not included in the full environment, or if you want to minimize the environment size for reproducibility.^[ai-runtime-databricks-on-aws.md]

## Environment Caching and Custom Modules

AI Runtime caches the environment for your session to reduce startup time across repeated uses. If you install custom modules or additional packages, those changes persist for the duration of the session but are not persisted across sessions unless you reinstall them. For details on caching behavior and known limitations, see the official documentation on setting up your environment.^[ai-runtime-databricks-on-aws.md]

## Limitations

- For scheduled jobs on AI Runtime, adding dependencies using the **Environments** panel is not supported. Install dependencies programmatically using `%pip install` in your notebook instead.^[ai-runtime-databricks-on-aws.md]
- Auto recovery behavior for incompatible package versions associated with your notebook is not supported in scheduled jobs.^[ai-runtime-databricks-on-aws.md]
- The environments are available only in supported AWS regions (us-west-2, us-west-1, us-east-1, us-east-2, ca-central-1, sa-east-1) and require the AI Runtime preview to be enabled by a workspace admin.^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The compute offering that provides these managed environments.
- GPU Scheduling – Optimizing GPU utilization for deep learning workloads.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime for classic ML workloads.
- [MLflow](/concepts/mlflow.md) – Used for experiment tracking during AI Runtime workloads.
- [Unity Catalog](/concepts/unity-catalog.md) – Natively integrated for data access and governance.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific GPU configuration available through AI Runtime.

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
