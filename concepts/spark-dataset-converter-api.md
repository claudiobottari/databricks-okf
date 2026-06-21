---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 39851eaa359ae4daad8a1a28deac0bec7c7103742094a8e7b317093911db078f
  pageDirectory: concepts
  sources:
    - load-data-using-petastorm-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-dataset-converter-api
    - SDCA
  citations:
    - file: load-data-using-petastorm-databricks-on-aws.md
title: Spark Dataset Converter API
description: The Petastorm API method that materializes a Spark DataFrame in Parquet format and loads it as a tf.data.Dataset or torch.utils.data.DataLoader for deep learning frameworks.
tags:
  - api
  - spark
  - deep-learning
  - data-conversion
timestamp: "2026-06-19T19:14:43.089Z"
---

# Spark Dataset Converter API

The **Spark Dataset Converter API** is a component of the open source [Petastorm](/concepts/petastorm.md) library that simplifies converting data from Apache Spark DataFrames into formats suitable for deep learning frameworks such as TensorFlow and PyTorch. The API first materializes the input Spark DataFrame in Parquet format and then loads it as a `tf.data.Dataset` or `torch.utils.data.DataLoader`.^[load-data-using-petastorm-databricks-on-aws.md]

## Overview

Petastorm is an open source data access library that enables single-node or distributed training and evaluation of deep learning models directly from datasets in Apache Parquet format or from datasets already loaded as Spark DataFrames. The Spark Dataset Converter API is the recommended way to bridge Spark and deep learning frameworks within the Petastorm ecosystem.^[load-data-using-petastorm-databricks-on-aws.md]

## Recommended Workflow

The recommended workflow using the Spark Dataset Converter API is:^[load-data-using-petastorm-databricks-on-aws.md]

1. Use Apache Spark to load and optionally preprocess data.
2. Use the Petastorm `spark_dataset_converter()` method to convert the Spark DataFrame to a TensorFlow Dataset or a PyTorch DataLoader.
3. Feed the converted data into a deep learning framework for training or inference.

## Cache Directory Configuration

The Spark Dataset Converter caches the input Spark DataFrame in Parquet format in a user‑specified cache directory. The cache directory must be a DBFS path starting with `file:///dbfs/` (for example, `file:///dbfs/tmp/foo/`, which refers to the same location as `dbfs:/tmp/foo/`).^[load-data-using-petastorm-databricks-on-aws.md]

The cache directory can be configured in two ways:^[load-data-using-petastorm-databricks-on-aws.md]

- In the cluster Spark config, add the line:  
  `petastorm.spark.converter.parentCacheDirUrl file:///dbfs/...`
- In the notebook, call:  
  `spark.conf.set(SparkDatasetConverter.PARENT_CACHE_DIR_URL_CONF, 'file:///dbfs/...')`

After use, the cache can be explicitly deleted by calling `converter.delete()`, or managed implicitly by configuring object storage lifecycle rules.^[load-data-using-petastorm-databricks-on-aws.md]

## Usage on Databricks

On Databricks, the Spark Dataset Converter API supports deep learning training in three scenarios:^[load-data-using-petastorm-databricks-on-aws.md]

- Single‑node training
- Distributed hyperparameter tuning
- Distributed training

End‑to‑end example notebooks are available for both TensorFlow and PyTorch workflows.^[load-data-using-petastorm-databricks-on-aws.md]

## Deprecation Notice

The `petastorm` package is deprecated. [Mosaic Streaming](/concepts/mosaic-streaming.md) is the recommended replacement for loading large datasets from cloud storage.^[load-data-using-petastorm-databricks-on-aws.md]

## Related Concepts

- [Petastorm](/concepts/petastorm.md) – The parent library that contains the Spark Dataset Converter API.
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) – The input data structure used by the API.
- TensorFlow – One of the supported deep learning frameworks.
- PyTorch – One of the supported deep learning frameworks.
- Parquet – The intermediate storage format used during conversion.
- Apache Spark – The distributed processing engine used for data loading and preprocessing.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – A supported training scenario on Databricks.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – Another supported scenario on Databricks.

## Sources

- load-data-using-petastorm-databricks-on-aws.md

# Citations

1. [load-data-using-petastorm-databricks-on-aws.md](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
