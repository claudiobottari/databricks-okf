---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c3ee5f107b7c1057c47ef2dc0869b7c85a8c9506f7ece6b58c02592f93b46d60
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorflow-savedmodel-format-requirement
    - TSFR
    - TensorFlow SavedModel format
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: TensorFlow SavedModel Format Requirement
description: When using horovod.spark with custom Keras callbacks, models must be saved in the TensorFlow SavedModel format using the .tf suffix (TF 2.x) or save_weights_only=True (TF 1.x).
tags:
  - tensorflow
  - keras
  - model-saving
  - horovod
timestamp: "2026-06-19T10:48:48.460Z"
---

# TensorFlow SavedModel Format Requirement

The **TensorFlow SavedModel Format Requirement** refers to a mandatory format constraint when using the deprecated `horovod.spark` package with custom callbacks in Keras. Specifically, when performing distributed training with `horovod.spark` and Keras, models must be saved using the TensorFlow SavedModel format. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Details

- **TensorFlow 2.x**: Use the `.tf` suffix in the file name when saving the model (e.g., `model.tf`). The SavedModel format is the default for TensorFlow 2.x, so the `.tf` suffix explicitly requests this format. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

- **TensorFlow 1.x**: Set the option `save_weights_only=True` when saving the model. This ensures the model is saved in the SavedModel format rather than as separate weight files. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Context

This requirement applies only when using `horovod.spark` with **custom callbacks** in Keras. Custom callbacks often rely on specific checkpointing behavior that must produce a SavedModel for downstream compatibility. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

The `horovod.spark` package is now **deprecated**. Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for PyTorch distributed training or the `tf.distribute.Strategy` API for TensorFlow distributed training instead. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [Horovod on Spark](/concepts/horovod-on-spark.md)
- Keras Callbacks
- TensorFlow SavedModel
- Distributed Deep Learning with Horovod
- [TorchDistributor](/concepts/torchdistributor.md)

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
