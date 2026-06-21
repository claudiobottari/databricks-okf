---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bbd88ce2d1ad21c8fdcc2df7619002a6edefcac14b52667313210b0467639331
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - development-workflow-for-distributed-training
    - DWFDT
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Development Workflow for Distributed Training
description: Recommended workflow of first training a model on a single node, then adapting the code for distributed training using tools like HorovodRunner
tags:
  - workflow
  - best-practices
  - distributed-training
timestamp: "2026-06-19T08:51:06.503Z"
---

# Development Workflow for Distributed Training

**Development Workflow for Distributed Training** refers to the recommended iterative approach for scaling machine learning model training from a single node to multiple nodes using frameworks like [HorovodRunner](/concepts/horovodrunner.md). The workflow emphasizes starting with a working single‑node implementation before adding distributed logic, which simplifies debugging and validation. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Recommended Steps

1. **Train the model on a single node** – Develop and test the training logic, data pipeline, and model architecture on one machine. This step ensures the core code is correct before introducing distributed communication. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]
2. **Adapt the code for distributed training** – Once the single‑node version is verified, modify the code to use a distributed framework (e.g., HorovodRunner) to scale across multiple GPUs or nodes. The adaptation typically involves wrapping existing training loops and adding gradient synchronization. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Example

The official Databricks notebook “HorovodRunner PyTorch MNIST example” demonstrates this workflow. It first trains a PyTorch model on a single node using the MNIST dataset, then refactors the training loop to run with HorovodRunner for distributed training. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Benefits

- **Iterative development**: Issues in the model or data pipeline are caught early in the single‑node phase, reducing debugging complexity in a distributed setting. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]
- **Familiar tooling**: Developers can use standard PyTorch or PyTorch tools during the single‑node step before learning distributed primitives. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]
- **Clear separation of concerns**: The transition from single‑node to distributed code is made explicit, making it easier to maintain and port to other distributed frameworks. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – The Databricks utility for distributed deep learning using Horovod.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General techniques for scaling model training across multiple devices.
- PyTorch Distributed – Native PyTorch support for distributed training.
- [Single‑node Training](/concepts/single-node-gpu-training-on-databricks.md) – The starting point of the workflow.
- MNIST – Common benchmark dataset used in the example notebook.

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
