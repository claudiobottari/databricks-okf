---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: efd8f9307e3f7d1a7e12d0c35d4267efefdde0c7fcf3d3d94c683e077f5bedc5
  pageDirectory: concepts
  sources:
    - horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovodspark-estimator-api
    - HEA
  citations:
    - file: horovod-databricks-on-aws.md
title: horovod.spark Estimator API
description: Spark ML pipeline estimator API for using Horovod with Keras and PyTorch models in Spark pipelines.
tags:
  - machine-learning
  - spark
  - pipeline
timestamp: "2026-06-19T19:05:09.620Z"
---

# horovod.spark Estimator API

The **horovod.spark Estimator API** is a distributed training interface within the Horovod framework that integrates with [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) for deep learning workloads using Keras or PyTorch. It provides an Estimator implementation that allows distributed training to be composed as a standard stage in a Spark ML pipeline. ^[horovod-databricks-on-aws.md]

## Overview

The `horovod.spark` package provides an estimator API that follows the Spark ML pipeline convention. This allows users to incorporate Horovod-based distributed deep learning training directly into Spark ML pipelines, enabling seamless integration with Spark's data processing and feature engineering stages. ^[horovod-databricks-on-aws.md]

## Requirements

The horovod.spark estimator API requires [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), which includes Horovod pre-installed along with the necessary deep learning frameworks. ^[horovod-databricks-on-aws.md]

## Deprecation Status

**Important**: Horovod and HorovodRunner are now deprecated. Releases after Databricks Runtime 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovod-databricks-on-aws.md]

## Use Case

The horovod.spark estimator API is specifically designed for Spark ML pipeline applications using Keras or PyTorch. It enables distributed training of deep learning models within the structured pipeline framework that Spark provides. ^[horovod-databricks-on-aws.md]

## Related Resources

The following articles provide additional information about using the horovod.spark package:

- [`horovod.spark`: distributed deep learning with Horovod](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-spark) — dedicated documentation for the estimator API
- [HorovodRunner](/concepts/horovodrunner.md) — alternative Horovod interface for distributed deep learning
- [Horovod](/concepts/horovod.md) — the underlying distributed training framework
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) — the pipeline framework that the estimator API integrates with

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Spark MLlib](/concepts/apache-spark-mllib.md)
- Deep Learning
- [DataParallel](/concepts/data-parallelism-spark.md)

## Sources

- horovod-databricks-on-aws.md

# Citations

1. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
