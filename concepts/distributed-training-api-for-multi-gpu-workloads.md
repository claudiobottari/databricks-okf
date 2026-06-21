---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ba7f2d3331320bc4e3b566a3498792b3ee9317db8520543251ba51731aee086
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-api-for-multi-gpu-workloads
    - DTAFMW
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Distributed training API for multi-GPU workloads
description: Beta-stage API in Databricks AI Runtime that enables scaling training workloads across multiple GPUs and nodes using the Serverless GPU API.
tags:
  - databricks
  - distributed-training
  - multi-gpu
  - beta
timestamp: "2026-06-19T22:04:01.227Z"
---

# Distributed Training API for Multi-GPU Workloads

The **Distributed Training API for multi-GPU workloads** is a Databricks feature that enables training machine learning models across multiple Graphics Processing Units (GPUs) in a distributed fashion. This API is designed to address the memory and compute limitations of single-GPU training for large models such as recommendation systems and large language models (LLMs).

## Current Status

The distributed training API for multi-GPU workloads is currently in **Beta** status. This pre-release phase indicates that the API is available for testing and evaluation but may not yet be fully stable for production deployments. Users should be aware of potential changes and limitations while using this API. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

In contrast, the [AI Runtime](/concepts/ai-runtime.md) for single-node tasks is in **Public Preview**, representing a more mature stage of availability. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Purpose and Use Cases

The primary purpose of the distributed training API is to parallelize training workloads across multiple GPUs, enabling the training of models that would otherwise exceed the memory capacity of a single GPU. This is particularly important for:

- **Large-scale recommendation systems** — Such as the [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) shown in tutorials using PyTorch Lightning. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Large language model (LLM) training** — Including fine-tuning approaches like [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) and full supervised fine-tuning. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Computer vision tasks** — Including object detection and image classification. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Classic ML workloads** — Including XGBoost model training and time series forecasting. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Integration with AI Runtime

The distributed training API is part of the broader [AI Runtime](/concepts/ai-runtime.md) on Databricks, which provides pre-configured environments for running machine learning workloads. While AI Runtime supports both single-node and multi-node configurations, the distributed training API specifically handles the multi-GPU aspects of the runtime. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Available Tutorials and Examples

Several notebook examples demonstrate the use of the distributed training API across different domains:

- **[Large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)** — Examples for fine-tuning large language models including parameter-efficient methods. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Computer vision** — Examples for computer vision tasks including object detection and image classification. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **[Deep learning based recommender systems](/concepts/deep-learning-based-recommender-systems.md)** — Examples for building recommendation systems using modern deep learning approaches like two-tower models. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Classic ML** — Examples for traditional machine learning tasks including XGBoost model training and time series forecasting. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **[Multi-GPU distributed training](/concepts/multi-gpu-distributed-training-databricks.md)** — Examples for scaling training across multiple GPUs and nodes using the Serverless GPU API. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure that provisions GPU resources on demand.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — A serverless GPU setup with eight H100 GPUs on a single node.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Common parallelism strategy for multi-GPU training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training for very large models.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) — The parameter range where FSDP is particularly useful.
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Scaling beyond a single node by coordinating across multiple nodes.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
