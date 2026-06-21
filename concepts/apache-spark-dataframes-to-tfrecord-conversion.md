---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2dee5d05fb313f9c72739dd73e1dbe88764feae47450450618d7f35c32bd2471
  pageDirectory: concepts
  sources:
    - prepare-data-for-distributed-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apache-spark-dataframes-to-tfrecord-conversion
    - ASDTTC
    - Apache Spark DataFrame
    - Save Apache Spark DataFrames as TFRecord files
  citations:
    - file: prepare-data-for-distributed-training-databricks-on-aws.md
title: Apache Spark DataFrames to TFRecord Conversion
description: The recommended approach for saving Apache Spark DataFrames as TFRecord files for use in distributed deep learning, as documented by Databricks.
tags:
  - spark
  - tensorflow
  - data-conversion
timestamp: "2026-06-19T19:57:26.229Z"
---

# Apache Spark DataFrames to TFRecord Conversion

**Apache Spark DataFrames to TFRecord Conversion** describes the process of saving a Spark DataFrame to the [TFRecord](/concepts/tfrecord-format.md) binary format for use in distributed deep learning training, particularly with TensorFlow. TFRecord is a simple, record-oriented binary format that many TensorFlow applications use as their primary training data source. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Overview

TFRecord files provide an efficient way to store and load large-scale training data. When working with Apache Spark in a Databricks environment, you can convert a Spark DataFrame to TFRecord files for consumption by TensorFlow's `tf.data.TFRecordDataset` API. This is especially useful when preparing data for distributed training workflows that use TensorFlow as the training framework. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Why Use TFRecord

For very large datasets that do not fit in memory, TFRecord format offers an efficient alternative to in-memory data loading. The recommended approaches for handling large datasets include:

- PyTorch IterableDataset for custom streaming logic
- [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming for datasets hosted on the Hub or in volumes
- Ray Data for distributed batch data processing

TFRecord format provides a TensorFlow-native binary format that is optimized for high-throughput data pipelines. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Saving Spark DataFrames as TFRecord Files

The recommended approach for saving Spark DataFrames as TFRecord files is described in the Databricks documentation. The process involves converting a Spark DataFrame's records into the TFRecord binary format and writing them to disk as a set of `.tfrecord` files. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Loading TFRecord Data

Once data is saved in TFRecord format, it can be loaded using TensorFlow's `tf.data.TFRecordDataset`, which creates a dataset comprised of records from TFRecord files. This dataset can then be used in training pipelines directly. For more details on consuming TFRecord data, see the TensorFlow guide on [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data). ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Related Resources

The following pages provide detailed instructions and examples for working with TFRecord in a Databricks environment:

- [Save Apache Spark DataFrames as TFRecord files](/concepts/apache-spark-dataframes-to-tfrecord-conversion.md) - Step-by-step guide for converting DataFrames to TFRecord format
- [Load TFRecord files](/concepts/tfrecord-file-format.md) - Instructions for reading TFRecord data into a TensorFlow pipeline

## Related Concepts

- [TFRecord](/concepts/tfrecord-format.md) - The binary record format used as a data source
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) - Training workflows that benefit from TFRecord format
- Data Pipeline Optimization - Techniques for efficient data loading
- tf.data API - TensorFlow's data loading API for consuming TFRecord files

## Sources

- prepare-data-for-distributed-training-databricks-on-aws.md

# Citations

1. [prepare-data-for-distributed-training-databricks-on-aws.md](/references/prepare-data-for-distributed-training-databricks-on-aws-8445664b.md)
