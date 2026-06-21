---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 466c80a419786774426a8623f5137bfce6132a71e5637d6688dfeb89ac8bb418
  pageDirectory: concepts
  sources:
    - load-data-using-petastorm-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - petastorm
  citations:
    - file: load-data-using-petastorm-databricks-on-aws.md
title: Petastorm
description: An open source data access library for converting Apache Spark DataFrames to TensorFlow Datasets or PyTorch DataLoaders, enabling single-node and distributed deep learning training from Parquet data.
tags:
  - data-access
  - deep-learning
  - spark
  - open-source
timestamp: "2026-06-19T19:14:26.940Z"
---

# Petastorm

**Petastorm** is an open source data access library that enables single-node or distributed training and evaluation of deep learning models directly from datasets stored in Apache Parquet format or already loaded as [Apache Spark](/apache-spark) DataFrames. It supports popular Python-based machine learning (ML) frameworks such as TensorFlow, PyTorch, and PySpark. ^[load-data-using-petastorm-databricks-on-aws.md]

## Deprecation Notice

The `petastorm` package is deprecated. [Mosaic Streaming]() is the recommended replacement for loading large datasets from cloud storage. ^[load-data-using-petastorm-databricks-on-aws.md]

## Workflow Overview

Petastorm provides two primary workflows for converting data into a format consumable by deep learning frameworks:

1. **Spark DataFrame conversion (recommended)**: Use the Petastorm `spark_dataset_converter` method to convert a Spark DataFrame directly into a `tf.data.Dataset` or `torch.utils.data.DataLoader`. The recommended steps are:
   - Use Apache Spark to load and optionally preprocess data.
   - Use `spark_dataset_converter` to convert the Spark DataFrame to a TensorFlow Dataset or PyTorch DataLoader.
   - Feed the data into a deep learning framework for training or inference.

2. **Direct Parquet loading**: Save preprocessed data in Parquet format to a DBFS path that has a companion DBFS mount, then load it using Petastorm via the mount point. This method is less preferred than the Spark converter API. ^[load-data-using-petastorm-databricks-on-aws.md]

## Cache Directory Configuration

The Petastorm Spark converter caches the input Spark DataFrame in Parquet format in a user-specified cache directory. The cache directory must be a DBFS path starting with `file:///dbfs/`, for example `file:///dbfs/tmp/foo/` (equivalent to `dbfs:/tmp/foo/`). You can configure the cache directory in two ways:

- In the cluster Spark configuration, add the line: `petastorm.spark.converter.parentCacheDirUrl file:///dbfs/...`
- In a notebook, call `spark.conf.set()`:
  ```python
  from petastorm.spark import SparkDatasetConverter, make_spark_converter
  spark.conf.set(SparkDatasetConverter.PARENT_CACHE_DIR_URL_CONF, 'file:///dbfs/...')
  ```

Cache can be explicitly deleted after use by calling `converter.delete()`, or managed implicitly by configuring lifecycle rules in object storage. ^[load-data-using-petastorm-databricks-on-aws.md]

## Supported Training Scenarios

Databricks supports three DL training scenarios with Petastorm:

- Single-node training
- Distributed hyperparameter tuning
- Distributed training

End-to-end notebooks are available for Simplify data conversion from Spark to TensorFlow and Simplify data conversion from Spark to PyTorch. ^[load-data-using-petastorm-databricks-on-aws.md]

## Examples

Two example notebook workflows are documented:

1. **Spark to TensorFlow**: Load data using Spark, convert to a TensorFlow Dataset via Petastorm, then train a single-node model, perform distributed hyperparameter tuning, or train a distributed TensorFlow model.
2. **Spark to PyTorch**: Load data using Spark, convert to a PyTorch DataLoader via Petastorm, then train a single-node or distributed PyTorch model.
3. **Parquet direct loading**: Use Spark to load and preprocess data, save as Parquet under `dbfs:/ml`, load via Petastorm using the FUSE mount `file:/dbfs/ml`, then feed into a deep learning framework. ^[load-data-using-petastorm-databricks-on-aws.md]

## Related Concepts

- [Mosaic Streaming](/concepts/mosaic-streaming.md) — The recommended replacement for Petastorm.
- Apache Parquet — The storage format used by Petastorm.
- Apache Spark — Used for data preprocessing and loading.
- TensorFlow / PyTorch — Deep learning frameworks supported by Petastorm.
- DBFS — Databricks File System used for caching and Parquet storage.
- [Spark Dataset Converter API](/concepts/spark-dataset-converter-api.md) — The core API for converting Spark DataFrames.

## Sources

- load-data-using-petastorm-databricks-on-aws.md

# Citations

1. [load-data-using-petastorm-databricks-on-aws.md](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
