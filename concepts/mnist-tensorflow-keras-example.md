---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2326cf68a464ed5acfbc0888e82704c64e1fa4a156a5bdd11b6471dc2132d27a
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-tensorflow-keras-example
    - MTKE
    - MNIST example
    - TensorFlow Keras
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: MNIST TensorFlow Keras Example
description: A reference notebook demonstrating distributed deep learning on the MNIST dataset using TensorFlow, Keras, and HorovodRunner on Databricks.
tags:
  - example
  - deep-learning
  - tensorflow
  - keras
  - mnist
timestamp: "2026-06-18T15:13:46.550Z"
---

# MNIST TensorFlow Keras Example

The **MNIST TensorFlow Keras Example** is a reference notebook demonstrating the recommended [development workflow] for distributed deep learning using TensorFlow with Keras and [HorovodRunner](/concepts/horovodrunner.md) on the [MNIST Dataset](/concepts/mnist-dataset.md).

## Overview

This notebook illustrates how to train a neural network on the MNIST handwritten digit dataset using the TensorFlow Keras API with HorovodRunner for distributed training. The example follows best practices for preparing data and scaling deep learning workloads across multiple GPUs.^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Key Components

- **[MNIST Dataset](/concepts/mnist-dataset.md)**: A collection of 70,000 grayscale images of handwritten digits (0-9) commonly used as a benchmark for image classification models.
- **[TensorFlow Keras](/concepts/mnist-tensorflow-keras-example.md)**: The high-level neural networks API within TensorFlow, providing a simplified interface for building and training deep learning models.
- **[HorovodRunner](/concepts/horovodrunner.md)**: A distributed training framework that enables scaling deep learning workloads across multiple GPUs and nodes using the Horovod library.

## Development Workflow

The notebook demonstrates the recommended development workflow for distributed training. Before running the training code, users should prepare the MNIST data for distributed training by ensuring it is accessible across all worker nodes.^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Related Concepts

- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md)
- [Data Parallelism](/concepts/data-parallelism-spark.md)
- GPU Training
- Model Parallelism

## Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
