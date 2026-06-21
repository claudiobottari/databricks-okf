---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58c3282c40fa6db70348c5733f8c84d0d42f59625127eca20cd5ab53bc31aa7f
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-ml-distributed-training-with-pysparkmlconnect
    - SMDTWP
    - Train Spark ML models on Databricks Connect with pyspark.ml.connect
  citations:
    - file: distributed-training-databricks-on-aws.md
title: Spark ML Distributed Training with pyspark.ml.connect
description: A module in Databricks Runtime 17.0+ for distributed training and inference of Spark ML models, enabled by default in Standard compute resources.
tags:
  - spark-ml
  - pyspark
  - distributed-training
timestamp: "2026-06-18T12:04:22.451Z"
---

# Spark ML Distributed Training with `pyspark.ml.connect`

**Spark ML Distributed Training with `pyspark.ml.connect`** refers to the capability to train and run inference on Spark ML models across multiple machines in a Databricks cluster using the `pyspark.ml.connect` module. This approach is part of Databricks’ broader distributed training offering, which also includes [TorchDistributor](/concepts/torchdistributor.md), [DeepSpeed Distributor](/concepts/deepspeed-distributor.md), and Ray for deep learning workloads. ^[distributed-training-databricks-on-aws.md]

## When to use distributed training

Databricks generally recommends training neural networks on a single machine because distributed code is more complex and often slower due to communication overhead. However, distributed training should be considered when your model or your data are too large to fit in memory on a single machine. For Spark ML workflows specifically, `pyspark.ml.connect` provides a distributed path for training and inference. ^[distributed-training-databricks-on-aws.md]

## How `pyspark.ml.connect` works

The `pyspark.ml.connect` module lets you use Spark’s distributed machine learning capabilities through the [Spark Connect](/concepts/spark-connect.md) architecture. Starting in Databricks Runtime 17.0 and above, Spark ML is enabled by default in **Standard** compute resources, which means you can train Spark ML models without needing to manage a full cluster. This simplifies the setup for distributed training of traditional ML models like linear regression, random forests, or gradient-boosted trees. ^[distributed-training-databricks-on-aws.md]

For full details and code examples, see the official documentation: [Train Spark ML models on Databricks Connect with `pyspark.ml.connect`](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/distributed-ml-for-spark-connect).

## Related concepts

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The machine learning runtime that includes distributed training tools.
- [TorchDistributor](/concepts/torchdistributor.md) — Distributed training for PyTorch models.
- [DeepSpeed Distributor](/concepts/deepspeed-distributor.md) — Optimized memory and communication for large models.
- Ray — Parallel compute framework for ML workflows.
- [Spark Connect](/concepts/spark-connect.md) — The decoupled client-server architecture underlying `pyspark.ml.connect`.

## Sources

- distributed-training-databricks-on-aws.md

# Citations

1. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
