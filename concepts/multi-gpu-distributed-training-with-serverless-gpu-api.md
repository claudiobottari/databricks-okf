---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 49fdef70f1a85348326d1ee530c833bdb48e536d7dc62a36a4f7c442cade5b07
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-gpu-distributed-training-with-serverless-gpu-api
    - MDTWSGA
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Multi-GPU Distributed Training with Serverless GPU API
description: API for scaling deep learning training workloads across multiple GPUs and nodes on Databricks, currently in Beta.
tags:
  - distributed-training
  - gpu
  - databricks
timestamp: "2026-06-18T10:44:24.925Z"
---

# Multi-GPU Distributed Training with Serverless GPU API

**Multi-GPU Distributed Training with Serverless GPU API** is a capability within [AI Runtime](/concepts/ai-runtime.md) that enables scaling machine‑learning training workloads across multiple GPUs and multiple compute nodes. It uses the Serverless GPU API to dynamically provision GPU resources without the need to manually configure clusters or manage infrastructure.^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Status

The distributed training API for multi‑GPU workloads—including the Serverless GPU API integration—is currently in **Beta**. (AI Runtime for single‑node tasks is in Public Preview.)^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Examples

Databricks provides example notebooks that demonstrate how to use the Serverless GPU API for distributed training. These cover common patterns such as data‑parallel and model‑parallel training across multiple GPUs and nodes. The examples are part of the [AI Runtime example notebooks](/concepts/ai-runtime-example-notebooks.md) collection.^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related concepts

- [AI Runtime](/concepts/ai-runtime.md) — the runtime environment that provides GPU‑accelerated execution for ML workloads.
- [Serverless GPU API](/concepts/serverless-gpu-api.md) — the API that provisions on‑demand GPU clusters for training jobs.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — techniques (e.g., data parallelism, model parallelism) for scaling training across devices.
- [Multi-GPU Training](/concepts/multi-gpu-distributed-training-api.md) — training that uses more than one GPU, either on a single node or across nodes.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
