---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d6fbaf560d85b470b22483c50e000a07ed471889e27489ff4561ac373db71f8
  pageDirectory: concepts
  sources:
    - prepare-data-for-distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tfrecord-format
    - TFRecord
  citations:
    - file: prepare-data-for-distributed-training-databricks-on-aws.md
title: TFRecord Format
description: A record-oriented binary format used by TensorFlow applications for training data, serving as a data source for distributed deep learning workflows.
tags:
  - tensorflow
  - data-format
  - distributed-training
timestamp: "2026-06-19T19:57:00.714Z"
---

# TFRecord Format

**TFRecord Format** is a simple record-oriented binary format commonly used by TensorFlow applications for storing and loading training data. It is designed for efficient reading and processing of large datasets in distributed deep learning workflows. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Overview

TFRecord files store data as a sequence of binary records, making them well-suited for large-scale machine learning pipelines. The format is particularly useful when working with datasets that are too large to fit in memory, as it supports streaming and efficient I/O operations. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Reading TFRecord Data

TensorFlow provides the `tf.data.TFRecordDataset` class for reading records from TFRecord files. This dataset type is part of the `tf.data` API and enables efficient streaming of data for training pipelines. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

```python
import tensorflow as tf

# Create a TFRecordDataset from one or more TFRecord files
dataset = tf.data.TFRecordDataset(['data.tfrecord'])
```

For detailed guidance on consuming TFRecord data, see the TensorFlow guide on [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data). ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Working with TFRecord Files

The recommended approaches for saving and loading TFRecord files include:

- **Saving Apache Spark DataFrames as TFRecord files** — Convert Spark DataFrames to TFRecord format for use in TensorFlow training pipelines.
- **Loading TFRecord files** — Read TFRecord data directly into TensorFlow datasets for training.

These operations are commonly performed in environments like Databricks where data processing and model training are integrated. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Use Cases

TFRecord format is particularly useful for:

- **Distributed training** — The binary format enables efficient data loading across multiple workers in [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) setups.
- **Large datasets** — When datasets do not fit in memory, TFRecord supports streaming approaches similar to PyTorch IterableDataset or [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming.
- **TensorFlow pipelines** — Native integration with TensorFlow's data API makes TFRecord the standard format for TensorFlow training workflows.

## Alternative Streaming Approaches

For very large datasets that do not fit in memory, several streaming approaches are available:

- **PyTorch IterableDataset** — Custom streaming logic for PyTorch workflows.
- **Hugging Face datasets** — Streaming support for datasets hosted on the Hub or in volumes.
- **Ray Data** — Distributed batch data processing for large-scale pipelines.

^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Training machine learning models across multiple GPUs or nodes.
- [Data Loading for Deep Learning](/concepts/data-loading-with-delta-lake-for-deep-learning.md) — Strategies for efficient data ingestion in training pipelines.
- TensorFlow Data API — The `tf.data` API for building input pipelines.
- Apache Spark DataFrames — Converting Spark DataFrames to TFRecord format.
- Binary Data Formats — Comparison of record-oriented binary formats for ML.

## Sources

- prepare-data-for-distributed-training-databricks-on-aws.md

# Citations

1. [prepare-data-for-distributed-training-databricks-on-aws.md](/references/prepare-data-for-distributed-training-databricks-on-aws-8445664b.md)
