---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f93b3dad64221289517da06861bdda98802790b2c311a582fffff50b1f573d8
  pageDirectory: concepts
  sources:
    - horovodrunner-examples-databricks-on-aws.md
  confidence: 0.7
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mnist-dataset-for-distributed-training-examples
    - MDFDTE
  citations:
    - file: horovodrunner-examples-databricks-on-aws.md
title: MNIST dataset for distributed training examples
description: The MNIST handwritten digit database is used as the example dataset in Databricks' HorovodRunner distributed training demonstrations.
tags:
  - dataset
  - machine-learning
  - examples
  - computer-vision
timestamp: "2026-06-19T19:06:08.555Z"
---

# MNIST Dataset for Distributed Training Examples

The **MNIST dataset** (Modified National Institute of Standards and Technology database) is a large collection of handwritten digits widely used as a benchmark for image classification models. On Databricks, the MNIST dataset serves as the primary example dataset for demonstrating distributed training workflows, particularly with the now-deprecated [HorovodRunner](/concepts/horovodrunner.md) library. ^[horovodrunner-examples-databricks-on-aws.md]

## Role in Distributed Training Examples

Databricks documentation includes examples that show how to use HorovodRunner to perform distributed training using a convolutional neural network (CNN) model on the MNIST dataset. These examples illustrate how to scale model training across multiple GPUs or nodes using the Horovod framework. ^[horovodrunner-examples-databricks-on-aws.md]

## Deprecation and Current Recommendations

Horovod and HorovodRunner are now deprecated. As of Databricks Runtime releases after 15.4 LTS ML, these packages are not pre-installed. For distributed deep learning on Databricks, the recommended alternatives are:

- [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch.
- The `tf.distribute.Strategy` API for distributed training with TensorFlow.

These newer tools provide the same distributed training capabilities that were previously demonstrated with MNIST and HorovodRunner, but with ongoing support and integration. ^[horovodrunner-examples-databricks-on-aws.md]

## Related Concepts

- distributed training
- [handwritten digit recognition](/concepts/mnist-handwritten-digit-classification.md)
- convolutional neural network (CNN)
- [HorovodRunner](/concepts/horovodrunner.md) (deprecated)
- [TorchDistributor](/concepts/torchdistributor.md)
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md)

## Sources

- horovodrunner-examples-databricks-on-aws.md

# Citations

1. [horovodrunner-examples-databricks-on-aws.md](/references/horovodrunner-examples-databricks-on-aws-de1151e3.md)
