---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26b79e8c11eef1b3a3f13b34bc84e77178a015501ad67a77c67d282f3c6ee68b
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-pytorch-on-databricks
    - MPOD
    - mnist-with-pytorch-on-databricks
    - MWPOD
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: MNIST PyTorch on Databricks
description: A reference notebook example showing how to train an MNIST model using PyTorch on Databricks, first on a single node then distributed with HorovodRunner
tags:
  - example
  - pytorch
  - mnist
  - databricks
timestamp: "2026-06-19T13:53:01.446Z"
---

# MNIST PyTorch on Databricks

**MNIST PyTorch on Databricks** refers to a reference notebook that demonstrates how to train a PyTorch model on the MNIST dataset, first on a single GPU node and then adapt it for distributed training using [HorovodRunner](/concepts/horovodrunner.md). The notebook is part of the archived machine learning documentation for Databricks on AWS and follows the recommended development workflow for scaling deep learning workloads.

## Overview

The notebook illustrates the process of converting a single‑node PyTorch training script into a distributed one with minimal code changes. It uses the classic MNIST handwritten digit classification task and the PyTorch deep learning framework. The primary goal is to show how [HorovodRunner](/concepts/horovodrunner.md) can be used to parallelize training across multiple GPUs or nodes without requiring a complete rewrite of the model code. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Development Workflow

The notebook follows a two‑step workflow:

1. **Single‑node training** – The model is first trained on one GPU (or CPU) using standard PyTorch loops. This establishes a baseline implementation and verifies that the model and data pipeline work correctly. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

2. **Distributed training with HorovodRunner** – The single‑node code is adapted by integrating Horovod primitives (e.g., `hvd.init()`, `hvd.DistributedOptimizer`) and wrapping the training function with `HorovodRunner`. This enables scaling to multiple GPUs on a single node or across multiple nodes. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

The notebook is available as an interactive example that can be opened directly in Databricks. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – The Databricks API for running distributed training with Horovod.
- PyTorch – The deep learning framework used in the notebook.
- [MNIST Dataset](/concepts/mnist-dataset.md) – The benchmark dataset for handwritten digit recognition.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General approach for scaling model training across multiple accelerators.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The pre‑configured runtime that includes PyTorch and Horovod.

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
