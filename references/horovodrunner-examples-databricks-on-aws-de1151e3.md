---
title: HorovodRunner examples | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner-examples
ingestedAt: "2026-06-18T08:03:00.331Z"
---

important

Horovod and HorovodRunner are now deprecated. Releases after 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/#torch-distributor) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow.

The examples in this section demonstrate how to use HorovodRunner to perform distributed training using a convolutional neural network model on the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset, a large database of handwritten digits.
