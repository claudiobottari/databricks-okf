---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48d284cb1799e83ef34f827d3e09b8d253915d8608ae98aff7711bbc1be20e94
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-runtime-data-access-and-integration
    - Integration and AI Runtime Data Access
    - ARDAAI
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Data Access and Integration
description: Data loading patterns and native integration points for AI Runtime including notebooks, jobs, Unity Catalog, MLflow experiment tracking, and Genie Code AI assistant for deep learning workloads.
tags:
  - databricks
  - data-access
  - mlflow
  - integration
timestamp: "2026-06-19T22:04:29.026Z"
---

# AI Runtime Data Access and Integration

**AI Runtime Data Access and Integration** refers to the mechanisms and best practices for reading, loading, and managing data within [AI Runtime](/concepts/ai-runtime.md) on Databricks. Understanding how data access works on AI Runtime is essential for a smooth experience when training and fine-tuning deep learning models. ^[ai-runtime-databricks-on-aws.md]

## Overview

AI Runtime is a compute offering at Databricks designed for deep learning workloads, providing GPU support for Databricks Serverless. It offers fully managed GPU infrastructure with no cluster configuration, driver selection, or autoscaling policies to manage. Users work within either a minimal default base environment for maximum flexibility or a full-featured AI environment pre-loaded with popular ML frameworks like PyTorch and Transformers. ^[ai-runtime-databricks-on-aws.md]

## Hardware and Environment Context

All AI Runtime accelerators provision a single node, with the number of GPUs depending on the accelerator type. Supported accelerators include A10 and H100 GPUs. When selecting an environment, users can choose between:

- **Minimal default base environment** — maximum flexibility over dependencies
- **Databricks AI environment** — pre-loaded with popular ML frameworks

^[ai-runtime-databricks-on-aws.md]

## Data Integration Methods

For detailed instructions on loading data on AI Runtime, users should refer to the [Load data on AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/dataloading) documentation. Key integration points include:

- **Notebooks** — Interactive data exploration and model development
- **Jobs** — Scheduled notebooks as recurring jobs
- **Jobs API and Databricks Asset Bundles** — Programmatic job creation

AI Runtime is natively integrated across notebooks, jobs, [Unity Catalog](/concepts/unity-catalog.md), and [MLflow](/concepts/mlflow.md) for seamless development, data access, and experiment tracking. ^[ai-runtime-databricks-on-aws.md]

## Use Cases Requiring Data Access

Databricks recommends AI Runtime for any custom model training use cases that involve deep learning, large-scale classic workloads, or GPUs. Common data-intensive workloads include:

- [LLM fine-tuning](/concepts/llm-fine-tuning-on-databricks.md) (LoRA, QLoRA, full fine-tuning)
- Computer vision (object detection, image classification)
- Deep-learning-based recommender systems
- [Reinforcement learning](/concepts/trl-transformer-reinforcement-learning.md)
- Deep-learning-based time series forecasting

^[ai-runtime-databricks-on-aws.md]

## Limitations and Considerations

When working with data on AI Runtime, users should be aware of several limitations:

- AI Runtime only supports A10 and H100 accelerators
- It is **not supported for compliance security profile workspaces** (like HIPAA or PCI); processing regulated data is not supported
- Adding dependencies using the **Environments** panel is not supported for scheduled jobs; install dependencies programmatically using `%pip install` instead
- The maximum runtime for a workload is seven days — for model training jobs exceeding this limit, implement checkpointing and restart the job
- AI Runtime provides on-demand access to GPU resources, but there may be periods where capacity is constrained or unavailable in your region
- AI Runtime leverages cross-region GPUs in certain cases during high demand, which may incur egress costs and potentially limited network connectivity

^[ai-runtime-databricks-on-aws.md]

## Requirements

To use AI Runtime for data access and integration, the following requirements must be met:

- A workspace in one of the supported AWS regions: `us-west-2`, `us-west-1`, `us-east-1`, `us-east-2`, `ca-central-1`, or `sa-east-1`
- The AI Runtime preview must be enabled via workspace admin settings

^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The core compute offering for deep learning workloads
- Databricks Serverless — The serverless compute infrastructure
- [Unity Catalog](/concepts/unity-catalog.md) — For managing and governing data assets
- [MLflow](/concepts/mlflow.md) — For experiment tracking and model management
- H100 GPU Support on Databricks — GPU hardware options for deep learning
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU workload support via the `@distributed` decorator
- Model Checkpointing — Important for long-running training jobs

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
