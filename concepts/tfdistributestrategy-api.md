---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d07aa3e241de4367f1869a9999595eb862b859508f662ad8785c4e404d5acace
  pageDirectory: concepts
  sources:
    - horovodrunner-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tfdistributestrategy-api
  citations:
    - file: horovodrunner-examples-databricks-on-aws.md
title: tf.distribute.Strategy API
description: TensorFlow's native API for distributed training, recommended by Databricks as the replacement for HorovodRunner when using TensorFlow.
tags:
  - machine-learning
  - distributed-training
  - tensorflow
  - databricks
timestamp: "2026-06-19T19:06:04.612Z"
---

---
title: tf.distribute.Strategy API
summary: The recommended API for distributed training with TensorFlow on Databricks, replacing the deprecated HorovodRunner.
sources:
  - horovodrunner-examples-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - distributed-training
  - tensorflow
  - databricks
  - api
aliases:
  - tf-distribute-strategy-api
  - tf.distribute.Strategy
  - TensorFlow Distribution Strategy API
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# tf.distribute.Strategy API

The **`tf.distribute.Strategy` API** is TensorFlow's built-in API for distributed training. Databricks recommends using this API for distributed training with TensorFlow, as an alternative to the deprecated [HorovodRunner](/concepts/horovodrunner.md). ^[horovodrunner-examples-databricks-on-aws.md]

This API is suitable for [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) workloads where model parallelism or data parallelism across multiple GPUs or nodes is required. ^[horovodrunner-examples-databricks-on-aws.md]

## Background

Horovod and HorovodRunner have been deprecated and will not be pre-installed in Databricks Runtime ML releases after 15.4 LTS. For distributed training with TensorFlow, Databricks recommends migrating to `tf.distribute.Strategy`. (For PyTorch, the recommended alternative is [TorchDistributor](/concepts/torchdistributor.md).) ^[horovodrunner-examples-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General strategies for training models across multiple devices.
- TensorFlow – The deep learning framework hosting this API.
- [HorovodRunner](/concepts/horovodrunner.md) – The deprecated distributed training tool for TensorFlow and PyTorch.
- [TorchDistributor](/concepts/torchdistributor.md) – The recommended distributed training API for PyTorch on Databricks.
- [Data Parallelism](/concepts/data-parallelism-spark.md) – A common paradigm supported by this API.
- Model Parallelism – Another paradigm supported for large models.

## Sources

- horovodrunner-examples-databricks-on-aws.md

# Citations

1. [horovodrunner-examples-databricks-on-aws.md](/references/horovodrunner-examples-databricks-on-aws-de1151e3.md)
