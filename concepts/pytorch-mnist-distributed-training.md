---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d043b82b5e20a7827c14d47815ca2ceb4a08033a5e2bd4d06c4a8bceb798e43c
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-mnist-distributed-training
    - PMDT
    - PyTorch Distributed Training
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: PyTorch MNIST distributed training
description: A reference notebook and example demonstrating how to train an MNIST model with PyTorch and scale it using HorovodRunner on Databricks.
tags:
  - pytorch
  - mnist
  - example
  - notebook
timestamp: "2026-06-19T17:26:18.621Z"
---

# PyTorch MNIST Distributed Training

**PyTorch MNIST Distributed Training** refers to the process of training a convolutional neural network on the MNIST dataset using PyTorch in a distributed manner, typically by leveraging multiple GPUs across one or more nodes. This approach accelerates training by parallelizing the workload and is a common starting point for learning distributed deep learning techniques. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Overview

The MNIST dataset is a classic benchmark for image classification, containing 28×28 grayscale images of handwritten digits. Distributed training of a PyTorch model on MNIST demonstrates how to scale a simple single‑GPU workflow to a multi‑GPU environment. On Databricks, this is accomplished using [HorovodRunner](/concepts/horovodrunner.md), a utility that wraps [Horovod](/concepts/horovod.md) to run distributed training jobs on a Spark cluster. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Development Workflow

The recommended workflow for distributed training with PyTorch on Databricks consists of two stages: ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

1. **Single‑node training** – First, implement and verify the model on a single GPU. This includes loading the MNIST data, defining the neural network, setting up the loss function and optimizer, and running a training loop. Once the model trains correctly on one node, the code can be adapted for distribution. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

2. **Adaptation with HorovodRunner** – After the single‑node version is working, modify the training script to use Horovod primitives such as `hvd.DistributedOptimizer` and `hvd.broadcast_parameters`. Then wrap the training function with `HorovodRunner` to execute it across multiple workers. HorovodRunner handles the MPI initialization, coordination between workers, and collection of results. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Example Notebook

The official Databricks notebook **"HorovodRunner PyTorch MNIST example"** provides a complete end‑to‑end demonstration. It follows the development workflow described above, showing both the single‑node code and the changes needed for distributed execution. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [Horovod](/concepts/horovod.md) – A distributed deep learning framework that provides communication primitives for all‑reduce and all‑gather operations.
- [HorovodRunner](/concepts/horovodrunner.md) – A Databricks utility that simplifies running Horovod jobs on a Spark cluster.
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) – General techniques for training models across multiple devices.
- PyTorch – The deep learning library used in the example.
- MNIST – The dataset used for the classification task.
- [Single‑Node Training](/concepts/single-node-gpu-training-on-databricks.md) – The baseline approach before distribution.

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
