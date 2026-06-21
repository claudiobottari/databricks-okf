---
title: TensorFlow | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/tensorflow
ingestedAt: "2026-06-18T08:13:41.633Z"
---

note

The open-source version of [TensorFlow](https://github.com/tensorflow/tensorflow) is not compatible with the latest CUDA versions.

TensorFlow will be removed in the next major Databricks Runtime ML version. Databricks recommends you install your own versions as needed.

TensorFlow is an open-source framework for machine learning created by Google. It supports deep-learning and general numerical computations on CPUs, GPUs, and clusters of GPUs. It is subject to the terms and conditions of the [Apache License 2.0](https://github.com/tensorflow/tensorflow/blob/master/LICENSE).

Databricks Runtime ML includes TensorFlow and TensorBoard, so you can use these libraries without installing any packages. For the version of TensorFlow installed in the Databricks Runtime ML version that you are using, see the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/).

## Single node and distributed training[​](#single-node-and-distributed-training "Direct link to Single node and distributed training")

To test and migrate single-machine workflows, use a [Single Node cluster](https://docs.databricks.com/aws/en/compute/configure#single-node).

For distributed training options for deep learning, see [Distributed training](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/).

## Tensorflow example notebook[​](#tensorflow-example-notebook "Direct link to Tensorflow example notebook")

The following notebook shows how you can run TensorFlow (1.x and 2.x) with TensorBoard monitoring on a Single Node cluster.

#### TensorFlow 1.15/2.x notebook

## TensorFlow Keras example notebook[​](#tensorflow-keras-example-notebook "Direct link to TensorFlow Keras example notebook")

[TensorFlow Keras](https://keras.io/about/) is a deep learning API written in Python that runs on top of the machine learning platform TensorFlow. The 10-minute tutorial notebook shows an example of training machine learning models on tabular data with TensorFlow Keras, including using inline [TensorBoard](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorboard).

#### Get started with TensorFlow Keras notebook
