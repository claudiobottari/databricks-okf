---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c83df7e1c6e22780551e6d0625909831b91420833182f7d05161b2a6348c401
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-tensorflow-keras-example-on-databricks
    - MTKEOD
    - HorovodRunner TensorFlow and Keras MNIST example
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: MNIST TensorFlow Keras example on Databricks
description: A reference notebook demonstrating deep learning with TensorFlow, Keras, and HorovodRunner for the MNIST dataset on Databricks.
tags:
  - tutorial
  - tensorflow
  - keras
  - mnist
timestamp: "2026-06-19T18:19:02.567Z"
---

## MNIST TensorFlow Keras example on Databricks

The **MNIST TensorFlow Keras example on Databricks** is a reference notebook that demonstrates distributed deep learning training on the MNIST dataset using TensorFlow with Keras and [HorovodRunner](/concepts/horovodrunner.md). The notebook follows the recommended [development workflow for HorovodRunner](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner#development-workflow) on Databricks. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Overview

The example trains a convolutional neural network (CNN) on the MNIST handwritten digit dataset using HorovodRunner to distribute the training across multiple GPU nodes. HorovodRunner wraps a standard TensorFlow/Keras training loop with Horovod callbacks, enabling scalable distributed training with minimal code changes. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Notebook

The notebook is published as a Databricks archive asset. It can be opened in a new tab from the documentation page. Before running, users must prepare the data for distributed training (e.g., by loading the MNIST dataset and distributing it across workers). ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Prerequisites

- A Databricks cluster configured with TensorFlow and [Horovod](/concepts/horovod.md) installed.
- Access to the MNIST dataset (typically loaded via `tensorflow.keras.datasets.mnist`).
- Understanding of the [HorovodRunner](/concepts/horovodrunner.md) development workflow, including converting a single-node training script to a distributed one.

### Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – Databricks API for running Horovod training.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – Overview of multi-GPU training strategies.
- [TensorFlow Keras](/concepts/mnist-tensorflow-keras-example.md) – High-level API for building neural networks.
- [Horovod](/concepts/horovod.md) – Open-source distributed training framework.
- MNIST – Classic dataset for handwritten digit recognition.
- [Deep Learning on Databricks](/concepts/deep-learning-on-databricks.md) – General documentation for GPU and distributed deep learning.

### Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
