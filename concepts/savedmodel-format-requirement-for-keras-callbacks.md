---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b8efc38f0b5f13465167c5f3171b78cfd7ac016681e69a1b55562318ebaaabb
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - savedmodel-format-requirement-for-keras-callbacks
    - SFRFKC
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: SavedModel Format Requirement for Keras Callbacks
description: When using horovod.spark with custom Keras callbacks, models must be saved in TensorFlow SavedModel format (.tf for TF 2.x, save_weights_only=True for TF 1.x).
tags:
  - keras
  - tensorflow
  - savedmodel
  - compatibility
timestamp: "2026-06-19T19:06:39.944Z"
---

# SavedModel Format Requirement for Keras Callbacks

The **SavedModel Format Requirement for Keras Callbacks** is a constraint that arises when using `horovod.spark` for distributed deep learning with custom Keras callbacks. In this context, models must be saved in the TensorFlow SavedModel format rather than using other Keras serialization methods. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Details

- **TensorFlow 2.x**: Use the `.tf` suffix in the file name when saving the model. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- **TensorFlow 1.x**: Set the option `save_weights_only=True` to save only the weights (the SavedModel format is not the default in TensorFlow 1.x). ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Context

This requirement is specific to the `horovod.spark` package, which provides an estimator API for distributed training with Keras and PyTorch on Apache Spark. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md] Note that `horovod.spark` (along with Horovod and HorovodRunner) is now deprecated; releases after Databricks Runtime 15.4 LTS ML will not include this package pre-installed. Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- Custom Keras Callbacks
- TensorFlow SavedModel
- [Horovod Spark](/concepts/horovod-on-spark.md)
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md)
- [horovod.spark](/concepts/horovodspark.md)
- [TorchDistributor](/concepts/torchdistributor.md)

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
