---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 522a1dac7b4a7bc75f545cef97160368553b39cc587cbe74f963492fbbb86416
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
    - train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - pysparkmlconnect
  citations:
    - file: distributed-training-databricks-on-aws.md
    - file: train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md
title: pyspark.ml.connect
description: A Spark ML module for distributed training and inference of Spark ML models, enabled by default in Databricks Runtime 17.0+ on Standard compute resources.
tags:
  - spark-ml
  - distributed-training
  - databricks
timestamp: "2026-06-19T18:34:48.912Z"
---

# pyspark.ml.connect

**pyspark.ml.connect** is a module in PySpark (introduced in Spark 3.5) that enables distributed training and inference of Spark ML models using the Spark Connect architecture. It is designed for client‑server environments such as [Databricks Connect](/concepts/databricks-connect.md), allowing workloads to train and run inference against a remote Spark cluster without requiring a full local cluster. ^[distributed-training-databricks-on-aws.md, train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]

## Overview

The module provides common machine learning algorithms and utilities, including classification, feature transformers, ML pipelines, and cross‑validation. Its API closely mirrors the legacy `pyspark.ml` module but currently contains only a subset of algorithms: ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]

- **Classification**: `pyspark.ml.connect.classification.LogisticRegression`
- **Feature transformers**: `pyspark.ml.connect.feature.MaxAbsScaler`, `pyspark.ml.connect.feature.StandardScaler`
- **Evaluators**: `pyspark.ml.connect.RegressionEvaluator`, `pyspark.ml.connect.BinaryClassificationEvaluator`, `pyspark.ml.connect.MulticlassClassificationEvaluator`
- **Pipeline**: `pyspark.ml.connect.pipeline.Pipeline`
- **Model tuning**: `pyspark.ml.connect.tuning.CrossValidator`

For full API reference details, Databricks recommends the [Apache Spark API reference](https://spark.apache.org/docs/latest/api/python/index.html). ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]

## Availability

`pyspark.ml.connect` is part of [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). Starting in **Databricks Runtime 17.0 and above**, Spark ML (including `pyspark.ml.connect`) is enabled by default on compute resources using **Standard** access mode. This eliminates the need to manage a full cluster for distributed machine learning workloads. ^[distributed-training-databricks-on-aws.md, train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]

For Databricks Runtime 14.0 ML and above (including Databricks Runtime 17.0 on compute resources with **Dedicated** access mode), additional requirements apply:
- Set up [Databricks Connect](/concepts/databricks-connect.md) on your clusters (see [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config)).
- Compute resource with **Dedicated** access mode.

Use Spark ML on Standard compute when data does not fit in memory on a single node and you need Spark‑level distribution, or when you need distributed hyperparameter tuning. ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]

## Limitations for Databricks Runtime 17.0 on Standard compute

When using Spark ML on Standard compute resources, the following limitations apply:

- **Python only**: Only Python is supported; R and Scala are not supported.
- **Library support**: Only the `pyspark.ml` package is supported. The `pyspark.mllib` package is not supported. ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]
- **Model size constraints**: The maximum model size is 1 GB. Tree model training stops early if the model size is about to exceed this limit. ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]
- **Memory constraints**: While data can be distributed across the cluster, the trained model is cached on the driver node, which is shared among other users. The maximum model cache size per session is 10 GB, and the maximum in‑memory model cache size per session is 25% of the Spark driver JVM memory. ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]
- **Session timeouts**: Cached models on Standard compute automatically time out after 15 minutes of inactivity. To avoid losing a model, save it to disk within 15 minutes after training completes, or keep the session active with frequent usage. ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]
- **Resource contention**: In Standard compute environments, resources are shared across users and jobs within the workspace. Running multiple large jobs concurrently may lead to slower performance or competition for executor slots. ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]
- **No GPU support**: Standard compute environments do not support GPU acceleration. For GPU‑accelerated workloads, dedicated GPU clusters are recommended. ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]
- **Limited SparkML models**: The following SparkML models are not supported:
  - `DistributedLDAModel`
  - `FPGrowthModel` ^[train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md]

## Use cases

Use `pyspark.ml.connect` for:
- Distributed training of Spark ML models (e.g., logistic regression, standard scaling, pipelines).
- Running model inference at scale with Spark Connect.
- Experiments and prototyping where you need Spark's distributed ML capabilities without the overhead of managing a dedicated cluster.

It is one of several distributed training offerings on Databricks, alongside [TorchDistributor](/concepts/torchdistributor.md), [DeepSpeed Distributor](/concepts/deepspeed-distributor.md), and Ray for deep learning workloads. ^[distributed-training-databricks-on-aws.md]

## Related concepts

- Spark ML – The core machine learning library for Apache Spark.
- [Databricks Connect](/concepts/databricks-connect.md) – The client‑server technology that `pyspark.ml.connect` relies on.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – Broader category of multi‑node model training on Databricks.
- [TorchDistributor](/concepts/torchdistributor.md) – Distributed training for PyTorch models.
- [DeepSpeed Distributor](/concepts/deepspeed-distributor.md) – Distributed training using Microsoft's DeepSpeed library.
- Ray – Parallel compute framework for ML workloads.

## Sources

- distributed-training-databricks-on-aws.md
- train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md

# Citations

1. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
2. [train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws.md](/references/train-spark-ml-models-on-databricks-connect-with-pysparkmlconnect-databricks-on-aws-c3691ddc.md)
