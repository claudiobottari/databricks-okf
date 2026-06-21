---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b62229af65ace43f5b4b12ee020c0e2eba6b13be8ac23f17da4a31af882b747
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-spark-estimator-api-with-keras
    - HSEAWK
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Horovod Spark Estimator API with Keras
description: Using the horovod.spark estimator API to run distributed deep learning training with Keras models on Databricks.
tags:
  - keras
  - horovod
  - spark
  - distributed-training
timestamp: "2026-06-19T19:07:06.731Z"
---

# Horovod Spark Estimator API with Keras

The **Horovod Spark Estimator API with Keras** is a distributed training API provided by the `horovod.spark` package that enables users to train Keras models at scale using Apache Spark clusters. It integrates Horovod's efficient allreduce operations with Spark's distributed computing framework, allowing for seamless scaling of deep learning workloads across multiple nodes and GPUs. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Overview

The `horovod.spark` package provides an estimator API that works directly within ML pipelines alongside Keras and PyTorch. This API allows data scientists to leverage Spark's data processing capabilities for data loading and preprocessing while using Horovod for distributed model training. The estimator pattern integrates naturally with Spark MLlib pipelines, enabling end-to-end workflows from data preparation to model training. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Requirements

To use the Horovod Spark Estimator API with Keras, you need Databricks Runtime ML 7.4 or above. The `horovod` package is pre-installed with its dependencies in Databricks Runtime ML. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Important Compatibility Note

`horovod.spark` does not support PyArrow versions 11.0 and above. Databricks Runtime 15.0 ML includes PyArrow version 14.0.1. To use `horovod.spark` with Databricks Runtime 15.0 ML or above, you must manually install PyArrow, specifying a version below 11.0. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Key Considerations for Keras

When using `horovod.spark` with custom callbacks in Keras, you must save models in the [TensorFlow SavedModel format](/concepts/tensorflow-savedmodel-format-requirement.md). With TensorFlow 2.x, use the `.tf` suffix in the file name. With TensorFlow 1.x, set the option `save_weights_only=True`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Usage Pattern

The basic workflow for using the Horovod Spark Estimator API involves defining a training function that initializes Horovod and performs distributed training, then executing it through the `horovod.spark.run()` method. A minimal example looks like: ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

```python
def train():
    import horovod.tensorflow as hvd
    hvd.init()

import horovod.spark
horovod.spark.run(train, num_proc=2)
```

This pattern can be extended to full Keras model definitions with distributed optimizers, callbacks, and data loading pipelines integrated with Spark DataFrames.

## Deprecation Notice

**Horovod and HorovodRunner are now deprecated.** Releases after Databricks Runtime 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [Horovod](/concepts/horovod.md) — The underlying distributed training framework
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) — General concepts for scaling model training
- [TensorFlow Keras](/concepts/mnist-tensorflow-keras-example.md) — The high-level neural networks API
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — Spark's machine learning library
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Alternative distributed training approach
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training for large models

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
