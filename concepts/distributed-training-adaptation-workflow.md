---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f20e162dd9c04b33b0944bb68a3e68fbde829f41bbfee4d2c3125b9677f52d28
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-adaptation-workflow
    - DTAW
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Distributed training adaptation workflow
description: The recommended development workflow of first training a model on a single node, then adapting it using HorovodRunner for distributed training.
tags:
  - workflow
  - distributed-training
  - best-practice
timestamp: "2026-06-19T17:26:05.770Z"
---

# Distributed training adaptation workflow

**Distributed training adaptation workflow** is the recommended development process for converting single‑node PyTorch training code to run on multiple GPUs or nodes using HorovodRunner on Databricks. The workflow proceeds in two stages: first, train and debug the model on a single node; second, adapt the code for distributed execution. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Development workflow

1. **Single‑node training** – Implement and validate the model and training loop on a single machine (or single GPU) using standard PyTorch. This step allows rapid iteration and debugging without the complexity of distributed communication.
2. **Distributed adaptation with HorovodRunner** – Modify the single‑node code to use [HorovodRunner](/concepts/horovodrunner.md), a Databricks library that wraps Horovod for distributed deep learning. The adaptation includes adding Horovod initialisation, distributing the data loader, broadcasting initial model parameters, and adjusting the learning rate schedule. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

HorovodRunner handles the coordination of multiple workers and the communication of gradients across GPUs, making the transition from single‑node to distributed training straightforward. The resulting distributed code runs on a cluster of GPU‑enabled instances. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related concepts

- [HorovodRunner](/concepts/horovodrunner.md) – The Databricks‑specific interface for running Horovod training jobs.
- [Horovod](/concepts/horovod.md) – An open‑source distributed training framework for TensorFlow, PyTorch, and MXNet.
- Distributed deep learning – Training models across multiple GPUs and machines.
- PyTorch distributed data parallel (DDP) – An alternative distributed strategy for PyTorch.
- [Single‑node training](/concepts/single-node-gpu-training-on-databricks.md) – The preliminary step before adapting to distributed execution.

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
