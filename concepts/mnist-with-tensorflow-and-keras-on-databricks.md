---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bec020eac21a08f6b1c33373a7a5e9cffb0df4831fea4e7520634ecbec176db6
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.7
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-with-tensorflow-and-keras-on-databricks
    - Keras on Databricks and MNIST with TensorFlow
    - MWTAKOD
    - MNIST with TensorFlow and Keras
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: MNIST with TensorFlow and Keras on Databricks
description: A reference pattern for training an MNIST digit classifier using TensorFlow and Keras, runnable with HorovodRunner for distributed execution
tags:
  - example
  - tensorflow
  - keras
  - computer-vision
timestamp: "2026-06-18T11:46:50.242Z"
---

# MNIST with TensorFlow and Keras on Databricks

**MNIST with TensorFlow and Keras on Databricks** demonstrates how to train a deep learning model on the MNIST digit classification dataset using TensorFlow and Keras with distributed training via [HorovodRunner](/concepts/horovodrunner.md). The notebook follows the recommended development workflow for distributed deep learning on Databricks.

## Overview

The notebook illustrates the complete pipeline: data preparation, model definition using the Keras API, and distributed training across multiple worker nodes by wrapping the training function with `HorovodRunner`. This approach allows scaling a standard TensorFlow/Keras model from a single GPU or CPU to a cluster of machines without modifying the model architecture. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Prerequisites

Before running the notebook, you must prepare the data for distributed training. The data preparation step ensures that each worker can read a partitioned copy of the [MNIST Dataset](/concepts/mnist-dataset.md) without contention. Details of the data preparation procedure are provided in the notebook’s prerequisites section. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Notebook Example

The example notebook is available for direct use:

- [HorovodRunner TensorFlow and Keras MNIST example notebook](https://assets.docs.databricks.com/_extras/notebooks/source/deep-learning/mnist-tensorflow-keras.html)

It can be opened in a new tab and imported into a Databricks workspace. The notebook walks through:

1. Loading and preprocessing the MNIST dataset.
2. Defining a Keras sequential model or functional model.
3. Wrapping the training loop with [HorovodRunner](/concepts/horovodrunner.md) to enable synchronous distributed training.
4. Running the training on multiple workers.

The notebook also covers metrics logging with [MLflow](/concepts/mlflow.md) for experiment tracking. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Related Concepts

- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) — Scaling training across multiple nodes
- [HorovodRunner](/concepts/horovodrunner.md) — Databricks’ API for Horovod-based distributed training
- TensorFlow and Keras — The deep learning framework used in the notebook
- [MNIST Dataset](/concepts/mnist-dataset.md) — Standard handwritten digit classification benchmark
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model logging

## Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
