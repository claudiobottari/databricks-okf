---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9bf1be353c4998c4ea8d650d8252c5bf5f545f97aba8316d023d59c328c5a9e
  pageDirectory: concepts
  sources:
    - horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovodspark
    - Horovod Spark
    - horovodspark-estimator-api
    - HEA
  citations:
    - file: horovod-databricks-on-aws.md
title: horovod.spark
description: A Spark integration package for Horovod that provides an estimator API for Spark ML pipelines using Keras or PyTorch models.
tags:
  - spark
  - distributed-training
  - ml-pipelines
timestamp: "2026-06-19T10:47:46.866Z"
---

Here is the wiki page for "horovod.spark".

---

## horovod.spark

**horovod.spark** is a Python package that integrates [Horovod](/concepts/horovod.md) distributed training with Apache Spark ML pipelines. It provides an estimator API for training Keras and PyTorch models at scale across a Spark cluster, allowing users to leverage Horovod's efficient allreduce-based communication within a Spark workflow. ^[horovod-databricks-on-aws.md]

### Usage

The `horovod.spark` estimator API follows the Spark ML pipeline pattern (`Estimator`/`Transformer`). A user can wrap a Keras or PyTorch model in a `horovod.spark` estimator and call `.fit()` on a Spark DataFrame. Under the hood, Horovod distributes the training across Spark executors, each of which runs a Horovod training loop. This approach is particularly suited for users who already have a Spark ML pipeline and want to add deep learning without leaving the Spark ecosystem. ^[horovod-databricks-on-aws.md]

### Deprecation Note

Horovod and `horovod.spark` are deprecated on Databricks. Releases after Databricks Runtime 15.4 LTS ML will not have the package pre-installed. For new projects, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovod-databricks-on-aws.md]

### Related Concepts

- [Horovod](/concepts/horovod.md) — The underlying distributed deep learning framework.
- [HorovodRunner](/concepts/horovodrunner.md) — A complementary API for running single-node Horovod jobs on Databricks (also deprecated).
- [TorchDistributor](/concepts/torchdistributor.md) — Recommended alternative for PyTorch distributed training on Databricks.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — PyTorch's native distributed strategy.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient alternative for large models.
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) — The pipeline API that `horovod.spark` extends.

### Sources

- horovod-databricks-on-aws.md

# Citations

1. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
