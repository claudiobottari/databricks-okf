---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c3c1a1a16cc38be5f44aafebc963a982d9afa2cadd7ae386c24b1d0aecb4f27
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-mnist-distributed-training-example
    - PMDTE
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: PyTorch MNIST Distributed Training Example
description: Reference notebook demonstrating how to train an MNIST model with PyTorch, first on a single node and then distributed with HorovodRunner on Databricks
tags:
  - example
  - pytorch
  - mnist
  - databricks
timestamp: "2026-06-18T10:38:48.862Z"
---

# PyTorch MNIST Distributed Training Example

This page describes how to adapt a single‑node PyTorch MNIST training script to run in a distributed fashion using **HorovodRunner** on Databricks. The example follows the recommended development workflow of first validating the model on a single node and then scaling it out for distributed training. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Overview

The notebook example demonstrates training a convolutional neural network on the MNIST dataset. The code is initially written for a single GPU or CPU, then refactored with Horovod primitives (such as `hvd.DistributedOptimizer`, `hvd.broadcast_parameters`, and `hvd.allreduce`) to enable synchronous data‑parallel training across multiple workers. The distributed version is executed via `HorovodRunner.run()` on a Databricks cluster. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Prerequisites

- A Databricks cluster with **Horovod** installed (available on Databricks Runtime for Machine Learning).
- PyTorch (included in the same runtime).
- Basic familiarity with PyTorch and the MNIST dataset.

## Step 1: Single‑Node Training

The notebook first implements a standard PyTorch training loop for MNIST:

- Loads the MNIST dataset using `torchvision.datasets.MNIST`.
- Defines a simple CNN (two convolutional layers followed by fully connected layers).
- Uses `torch.optim.SGD` as the optimizer and `torch.nn.CrossEntropyLoss`.
- Trains for a few epochs on a single GPU or CPU.

This baseline code runs entirely on one worker and serves as the starting point for distribution. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Step 2: Adapting for Distributed Training with HorovodRunner

The single‑node code is modified to use Horovod’s distributed primitives. The key changes are:

1. **Initialize Horovod**: `hvd.init()`.
2. **Pin GPU to local rank**: `torch.cuda.set_device(hvd.local_rank())`.
3. **Scale the learning rate**: Multiply the base learning rate by the number of workers to keep the effective batch size consistent.
4. **Wrap the optimizer**: `optimizer = hvd.DistributedOptimizer(optimizer)` so that gradients are averaged across workers.
5. **Broadcast initial parameters**: `hvd.broadcast_parameters(model.state_dict(), root_rank=0)` to ensure all workers start with the same weights.
6. **Partition the dataset**: Use `DistributedSampler` (or manual sharding) so each worker processes a different subset of the data.
7. **Wrap training logic in a function** that accepts a `rank` or uses the Horovod rank internally.

The adapted training function is then passed to `HorovodRunner.run(n_workers)`, where `n_workers` specifies the number of parallel processes. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

### Important Consideration

When using HorovodRunner, all worker processes execute the same Python function. The dataset must be sharded inside that function (e.g., using `DistributedSampler`) so that each worker trains on a unique subset of the data. Without proper sharding, every worker would train on the same data, defeating the purpose of distributed training. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Notebook

The full example is available as a Databricks notebook: **HorovodRunner PyTorch MNIST example notebook**. It includes both the single‑node and distributed code, with explanatory comments. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [Horovod Runner](/concepts/horovodrunner.md) — Databricks’ utility for distributed deep learning with Horovod
- [Horovod](/concepts/horovod.md) — The underlying distributed training framework
- PyTorch Distributed Training — General approach for scaling PyTorch models
- Distributed Sampler — How to shard data across workers
- [Synchronous Data Parallelism](/concepts/distributed-data-parallel-ddp.md) — The parallelism strategy used by Horovod

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
