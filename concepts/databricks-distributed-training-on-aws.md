---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 11feedaa8a1a9a1a16d7fa48c47880448da7a786ff712c93a38abcdb2a14458c
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-distributed-training-on-aws
    - DDTOA
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: Databricks distributed training on AWS
description: Reference architecture for running distributed TensorFlow training on Databricks clusters in AWS
tags:
  - databricks
  - aws
  - distributed-training
timestamp: "2026-06-19T18:38:33.535Z"
---

##Databricks distributed training on AWS

**Databricks distributed training on AWS** enables you to scale TensorFlow model training across multiple workers on a Spark cluster using the open-source `spark-tensorflow-distributor` library. This library integrates natively with TensorFlow 2 and builds on top of `tensorflow.distribute.Strategy`, allowing data-parallel training to be launched directly from a Databricks notebook or job. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

The `spark-tensorflow-distributor` is part of the TensorFlow ecosystem and is available as a Python package. It wraps Spark tasks so that each worker executes a copy of the TensorFlow training script with the appropriate cluster configuration. TensorFlow’s built-in distribution strategies (such as `MirroredStrategy` or `MultiWorkerMirroredStrategy`) handle gradient synchronization and device placement. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

### Example notebook

Databricks provides an example notebook that demonstrates distributed training with TensorFlow 2 using `spark-tensorflow-distributor`. The notebook shows how to set up a `MirroredStrategyRunner`, define a model, and execute training across multiple Spark executors on AWS infrastructure. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

### Requirements

- A Databricks cluster on AWS with TensorFlow 2 installed.
- The `spark-tensorflow-distributor` package must be installed in the cluster library.
- Workers should have access to GPUs if using `MirroredStrategy` (each worker typically runs on a single GPU, with multi‑worker communication handled by TensorFlow).

For detailed API documentation, see the docstrings in the [spark-tensorflow-distributor repository](https://github.com/tensorflow/ecosystem/blob/master/spark/spark-tensorflow-distributor/spark_tensorflow_distributor/mirrored_strategy_runner.py). For general guidance on distributed TensorFlow, consult the [TensorFlow distributed training guide](https://www.tensorflow.org/guide/distributed_training).

### Limitations

The `spark-tensorflow-distributor` is designed for data‑parallel training where each worker holds a full copy of the model. For very large models (e.g., 20‑billion+ parameters) that cannot fit in a single GPU’s memory, alternative approaches such as [Fully Sharded Data Parallel (FSDP) training on Databricks](/concepts/fully-sharded-data-parallel-fsdp-on-databricks.md) or Serverless GPU Compute with H100s may be more appropriate.

### Related concepts

- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – parameter range where FSDP becomes necessary
- [Fully Sharded Data Parallel (FSDP) training on Databricks](/concepts/fully-sharded-data-parallel-fsdp-on-databricks.md) – sharded training for large models
- [Serverless GPU Compute on Databricks](/concepts/serverless-gpu-compute-on-databricks.md) – on‑demand GPU resources for distributed workloads
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – a specific high‑GPU configuration for intensive training
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – another parallelism strategy supported on Databricks
- [MLflow experiments](/concepts/mlflow-experiment.md) – tracking distributed training runs and evaluations

### Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
