---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ede7591bb1db78bc8ffc64f0d2a9814897e5408f7cc366a72d9c0b5451956c7d
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-handwritten-digit-classification
    - MHDC
    - handwritten digit recognition
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: MNIST handwritten digit classification
description: A classic benchmark dataset and problem for handwritten digit recognition using deep learning, used as a demonstration example for HorovodRunner with TensorFlow and Keras.
tags:
  - dataset
  - computer-vision
  - deep-learning
  - example
timestamp: "2026-06-19T14:58:23.575Z"
---

# MNIST Handwritten Digit Classification

**MNIST handwritten digit classification** is a classic deep learning benchmark used to demonstrate distributed training workflows on Databricks. The dataset consists of 28×28 grayscale images of handwritten digits (0–9) and is commonly trained with a TensorFlow/Keras model using [HorovodRunner](/concepts/horovodrunner.md) for multi-GPU scaling. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Databricks Example

Databricks provides a notebook that illustrates the recommended development workflow for distributed deep learning using HorovodRunner with TensorFlow and Keras on the MNIST dataset. The notebook covers data preparation, model definition, and distributed training. Before running the notebook, users must prepare the data for distributed training — typically by partitioning the dataset so each worker processes a distinct subset. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

The notebook is available in the Databricks documentation archive and can be opened in a new tab for direct use. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – The distributed training API used to parallelize the MNIST workload.
- TensorFlow – The deep learning framework used to build the classifier.
- Keras – The high‑level API for defining the model.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General approach for scaling across multiple GPUs.
- [MNIST Dataset](/concepts/mnist-dataset.md) – The standard handwritten digit benchmark.

## Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
