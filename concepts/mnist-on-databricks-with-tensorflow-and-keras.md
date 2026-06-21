---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1efd23a8cb142d6ca3e6fd1b2733b97f9075a01ce7c4849303ca722b4c4cd42b
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-on-databricks-with-tensorflow-and-keras
    - Keras and MNIST on Databricks with TensorFlow
    - MODWTAK
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: MNIST on Databricks with TensorFlow and Keras
description: Reference example demonstrating distributed deep learning using TensorFlow, Keras, and HorovodRunner on Databricks for the MNIST digit classification task.
tags:
  - example
  - tensorflow
  - keras
  - MNIST
timestamp: "2026-06-19T09:58:13.890Z"
---

# MNIST on Databricks with TensorFlow and Keras

**MNIST on Databricks with TensorFlow and Keras** refers to the practice of training a convolutional neural network on the MNIST handwritten digit dataset using TensorFlow with Keras, distributed via HorovodRunner on Databricks. The approach follows the recommended development workflow for HorovodRunner on Databricks. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Overview

The standard example notebook demonstrates how to perform distributed training of an MNIST classifier using TensorFlow and Keras with [HorovodRunner](/concepts/horovodrunner.md) on Databricks. Before executing the notebook, users must prepare the data for distributed training — typically by partitioning the dataset so that each worker processes a subset during training. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Notebook

A complete example notebook is provided by Databricks: [HorovodRunner TensorFlow and Keras MNIST example notebook](https://assets.docs.databricks.com/_extras/notebooks/source/deep-learning/mnist-tensorflow-keras.html). It is part of the Databricks documentation archive under the HorovodRunner section. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — The Databricks API for distributing Horovod training jobs.
- [Distributed deep learning on Databricks](/concepts/distributed-deep-learning-on-databricks.md) — General guidance for multi-GPU and multi-node training.
- [Horovod](/concepts/horovod.md) — The distributed training framework used under the hood.
- [MNIST Dataset](/concepts/mnist-dataset.md) — The handwritten digit classification benchmark.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The pre-built runtime that includes TensorFlow and Horovod.

## Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
