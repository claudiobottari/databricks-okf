---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16d3af8a4f64a0ad7995e18ec9d1ad365fd4aa5655eda575423db281a4fa9fe9
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-use-cases
    - ARUC
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Use Cases
description: Recommended workloads for AI Runtime including LLM fine-tuning, computer vision, recommender systems, reinforcement learning, and time series forecasting
tags:
  - use-cases
  - deep-learning
  - llm
  - computer-vision
timestamp: "2026-06-19T17:31:25.873Z"
---

# AI Runtime Use Cases

**AI Runtime** is a compute offering on Databricks designed for deep learning workloads, providing serverless GPU infrastructure with no cluster configuration or autoscaling to manage. It is recommended for any custom model training that involves deep learning, large-scale classic workloads, or general GPU compute. ^[ai-runtime-databricks-on-aws.md]

AI Runtime runs on single‑node accelerators (A10 and H100 GPUs) and supports distributed training across multiple GPUs on that node via the `@distributed` decorator (Beta). The runtime is natively integrated with notebooks, jobs, [Unity Catalog](/concepts/unity-catalog.md), and [MLflow](/concepts/mlflow.md) for seamless experiment tracking and data access. ^[ai-runtime-databricks-on-aws.md]

The following sections describe the primary use cases for which Databricks recommends AI Runtime.

---

## LLM Fine-Tuning

AI Runtime is well suited for fine‑tuning large language models (LLMs) using techniques such as LoRA, [QLoRA](/concepts/qlora-quantized-low-rank-adaptation.md), and full fine‑tuning. These workloads benefit from the higher floating‑point operations (FLOPS) and larger memory of H100 GPUs, or from the cost efficiency of A10 GPUs for smaller models. ^[ai-runtime-databricks-on-aws.md]

## Computer Vision

Classic computer vision tasks — including object detection and image classification — can be trained on AI Runtime. The serverless GPU infrastructure simplifies provisioning for repeated experimentation, and the pre‑loaded AI environment includes popular frameworks like PyTorch and Transformers. ^[ai-runtime-databricks-on-aws.md]

## Deep-Learning-Based Recommender Systems

Recommendation engines that rely on deep neural networks (e.g., collaborative filtering with embeddings, sequence‑aware models) are a supported use case. AI Runtime provides single‑node multi‑GPU capacity for training these models efficiently. ^[ai-runtime-databricks-on-aws.md]

## Reinforcement Learning

Reinforcement learning (RL) workflows, which often require large batch simulations and frequent model updates, can run on AI Runtime. The serverless infrastructure allows on‑demand scaling of GPU resources for RL training loops. ^[ai-runtime-databricks-on-aws.md]

## Deep-Learning-Based Time Series Forecasting

Time series forecasting models built with deep learning (e.g., LSTMs, Transformers) are supported. AI Runtime can handle the GPU‑intensive training of these models for large‑scale prediction tasks. ^[ai-runtime-databricks-on-aws.md]

## Additional Capabilities

Beyond the listed use cases, AI Runtime can be applied to any custom deep learning training. The runtime also integrates with [Genie Code for Deep Learning](/concepts/genie-code-for-deep-learning.md), which helps generate training code, resolve library installation errors, suggest optimizations, and debug common issues. ^[ai-runtime-databricks-on-aws.md]

## Limitations Relevant to Use Cases

- AI Runtime is **not supported** for workspaces with a [compliance security profile](/concepts/compliance-security-profile-databricks-on-aws.md) (e.g., HIPAA, PCI). ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a workload is seven days. For longer training jobs, implement checkpointing and restart the job. ^[ai-runtime-databricks-on-aws.md]
- GPU capacity may be constrained at times; AI Runtime may use cross‑region GPUs during high demand, which can incur egress costs. ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- A10 GPU Support on Databricks
- H100 GPU Support on Databricks
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Distributed Training on AI Runtime](/concepts/distributed-training-on-ai-runtime.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
