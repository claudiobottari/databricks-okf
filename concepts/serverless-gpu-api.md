---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9603ddd790081a82e3d96f27f88569415baf6b6b0e18cbf330c3642c52ffc0a0
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-api
    - SGA
    - Serverless GPU
    - serverless GPU
    - serverless_gpu
    - serverless_gpu API
    - serverless_gpu Python API
    - Serverless GPU API Documentation
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Serverless GPU API
description: Databricks API for scaling training across multiple GPUs and nodes without managing infrastructure.
tags:
  - serverless
  - gpu
  - api
timestamp: "2026-06-19T17:31:42.502Z"
---

# Serverless GPU API

The **Serverless GPU API** is a distributed training API on Databricks that enables scaling deep learning workloads across multiple GPUs and nodes. It is part of the [AI Runtime](/concepts/ai-runtime.md) offering and is used to run multi‑GPU training jobs without managing the underlying cluster infrastructure. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Status

The distributed training API for multi‑GPU workloads — which encompasses the Serverless GPU API — remains in **Beta**. In contrast, the AI Runtime for single‑node tasks is in **Public Preview**. Users should be aware that Beta features may have limited support and are not recommended for production use. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Usage

The Serverless GPU API is the mechanism by which users launch training scripts that span multiple GPUs, either on a single node or across multiple nodes. It abstracts away the provisioning and orchestration of GPU instances, allowing users to focus on the distributed training logic. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example Notebooks

Databricks provides example notebooks demonstrating how to use the Serverless GPU API for various tasks. These examples cover:

- [Large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) – fine‑tuning and parameter‑efficient methods.
- Computer vision – object detection and image classification.
- [Deep learning based recommender systems](/concepts/deep-learning-based-recommender-systems.md) – two‑tower models.
- Classic ML – XGBoost training and time series forecasting.
- [Multi‑GPU distributed training](/concepts/multi-gpu-distributed-training-databricks.md) – scaling across multiple GPUs and nodes using the Serverless GPU API.

All examples are part of the AI Runtime documentation. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- H100 GPU Support on Databricks
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
