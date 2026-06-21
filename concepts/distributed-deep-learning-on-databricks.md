---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5cc3c816b9bc78ab2df5d5bf5b26628405c82e75d2cd63a2a57eccfd5fd38324
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
    - horovodrunner-examples-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-deep-learning-on-databricks
    - DDLOD
    - Distributed Deep Learning
  citations:
    - file: horovodrunner-examples-databricks-on-aws.md
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: Distributed deep learning on Databricks
description: The practice of scaling deep learning model training across multiple nodes using HorovodRunner within the Databricks platform.
tags:
  - distributed-training
  - deep-learning
  - databricks
timestamp: "2026-06-19T18:19:22.800Z"
---

# Distributed Deep Learning on Databricks

**Distributed Deep Learning on Databricks** refers to the tools and practices for scaling deep learning training across multiple GPUs and nodes within the Databricks platform. The platform has historically supported HorovodRunner for distributed training, but as of recent releases, Horovod and HorovodRunner are deprecated and alternative frameworks are recommended. ^[horovodrunner-examples-databricks-on-aws.md]

## Deprecated: HorovodRunner

Horovod and HorovodRunner are now **deprecated**. Releases after Databricks Runtime 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovodrunner-examples-databricks-on-aws.md]

Historical examples demonstrate HorovodRunner with a convolutional neural network on the MNIST dataset, but these should not be used for new projects. ^[horovodrunner-examples-databricks-on-aws.md] A development workflow for HorovodRunner, including data preparation for distributed training, is documented but no longer the recommended path. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Recommended Approaches

The recommended distributed training strategies for new projects on Databricks are:

- **[TorchDistributor](/concepts/torchdistributor.md)** – for distributed training with PyTorch.
- **`tf.distribute.Strategy` API** – for distributed training with TensorFlow.

These are the official replacements for HorovodRunner. ^[horovodrunner-examples-databricks-on-aws.md]

## Historical Example

The following notebook demonstrates the now‑deprecated development workflow for HorovodRunner with TensorFlow and Keras on the MNIST dataset: [HorovodRunner TensorFlow and Keras MNIST example notebook](https://assets.docs.databricks.com/_extras/notebooks/source/deep-learning/mnist-tensorflow-keras.html). ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md)
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [HorovodRunner](/concepts/horovodrunner.md) (deprecated)

## Sources

- horovodrunner-examples-databricks-on-aws.md
- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [horovodrunner-examples-databricks-on-aws.md](/references/horovodrunner-examples-databricks-on-aws-de1151e3.md)
2. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
