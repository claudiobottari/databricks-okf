---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aaf1b2b73412a2d58ca2a15680c21cafecb5b1f15f863976916647a0fb52a7e1
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-with-pytorch-on-databricks
    - MWPOD
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: MNIST with PyTorch on Databricks
description: Example of training an MNIST model using PyTorch on Databricks, serving as a reference for distributed deep learning
tags:
  - example
  - pytorch
  - mnist
  - databricks
timestamp: "2026-06-19T08:51:15.375Z"
---

# MNIST with PyTorch on Databricks

**MNIST with PyTorch on Databricks** is a reference example that demonstrates how to perform distributed training of a deep learning model using PyTorch on the Databricks platform. The example follows the recommended development workflow: it starts with training a model on a single node, then adapts the code for distributed training using HorovodRunner. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Overview

The example uses the classic MNIST dataset – a collection of handwritten digit images – and a PyTorch neural network to perform image classification. It is designed to illustrate the transition from single‑GPU or single‑node training to multi‑node distributed training, which is a common requirement for scaling deep learning workloads. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

The notebook is available in the Databricks documentation as the **HorovodRunner PyTorch MNIST example notebook**. It is part of the [Horovod](/concepts/horovod.md) documentation archive on Databricks. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Development Workflow

The recommended development workflow has two phases: ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

1. **Single‑node training** – Build and train the model on a single GPU (or CPU) to verify correctness and establish a baseline.
2. **Distributed training** – Adapt the single‑node code to run across multiple GPUs/nodes using [HorovodRunner](/concepts/horovodrunner.md), a Databricks‑integrated utility that wraps Horovod for easy distributed training.

This phased approach allows developers to debug locally before scaling, reducing iteration time. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## HorovodRunner

[HorovodRunner](/concepts/horovodrunner.md) is the key mechanism for adapting single‑node PyTorch code to distributed training on Databricks. It manages the communication between workers (using Horovod’s allreduce operations) and provides a simple API to launch training across the cluster. The MNIST example notebook shows how to modify a standard PyTorch training loop to work with HorovodRunner, including distributing the dataset, synchronizing gradients, and broadcasting initial model parameters. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [Horovod](/concepts/horovod.md) – The underlying distributed deep learning framework.
- [Distributed deep learning on Databricks](/concepts/distributed-deep-learning-on-databricks.md) – General guidance for multi‑GPU and multi‑node training.
- [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – An alternative distributed training approach.
- [MLflow](/concepts/mlflow.md) – For tracking experiments and models on Databricks.

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
