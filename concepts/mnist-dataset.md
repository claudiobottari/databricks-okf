---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a449e3a07e83061e8d41e4a0d13f262dcf46ceb73bbe4c8de8a7798c93b36048
  pageDirectory: concepts
  sources:
    - horovodrunner-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-dataset
  citations:
    - file: horovodrunner-examples-databricks-on-aws.md
title: MNIST Dataset
description: A large database of handwritten digits used as the example dataset for HorovodRunner distributed training examples.
tags:
  - dataset
  - deep-learning
  - example
timestamp: "2026-06-19T10:48:19.130Z"
---

# MNIST Dataset

The **MNIST dataset** (Modified National Institute of Standards and Technology database) is a large database of handwritten digits used to train and evaluate image classification models. It is commonly employed as a benchmark for convolutional neural networks and other deep learning algorithms, particularly for [handwritten digit recognition](/concepts/mnist-handwritten-digit-classification.md) tasks.

## Overview

MNIST consists of grayscale images of handwritten digits (0 through 9). The dataset is widely used in machine learning education, research, and distributed training examples due to its manageable size and well‑defined task. ^[horovodrunner-examples-databricks-on-aws.md]

## Usage in Distributed Training on Databricks

On Databricks, the MNIST dataset has historically been used in examples demonstrating [HorovodRunner](/concepts/horovodrunner.md) for distributed training with a convolutional neural network (CNN). These examples show how to scale training of a digit‑recognition model across multiple GPUs or nodes using Horovod. ^[horovodrunner-examples-databricks-on-aws.md]

> **Note:** Horovod and HorovodRunner are now deprecated in Databricks. For distributed training, Databricks recommends using the [TorchDistributor](/concepts/torchdistributor.md) (for PyTorch) or the `tf.distribute.Strategy` API (for TensorFlow) instead. ^[horovodrunner-examples-databricks-on-aws.md]

## Related Concepts

- Convolutional Neural Network (CNN)
- Deep Learning 
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [HorovodRunner](/concepts/horovodrunner.md) (deprecated)
- [TorchDistributor](/concepts/torchdistributor.md)
- [TensorFlow distributed strategy](/concepts/tensorflowdistributestrategy.md)

## Sources

- horovodrunner-examples-databricks-on-aws.md

# Citations

1. [horovodrunner-examples-databricks-on-aws.md](/references/horovodrunner-examples-databricks-on-aws-de1151e3.md)
