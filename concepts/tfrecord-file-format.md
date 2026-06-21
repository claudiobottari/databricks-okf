---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 804c24e386cff540aa370c6351d49e99ff66ef0fa478edb6b35e424758e27495
  pageDirectory: concepts
  sources:
    - save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tfrecord-file-format
    - TFF
    - Load TFRecord files
  citations:
    - file: save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
title: TFRecord File Format
description: A simple record-oriented binary file format for storing ML training data, commonly used with TensorFlow.
tags:
  - data-format
  - machine-learning
  - tensorflow
timestamp: "2026-06-19T20:18:19.524Z"
---

# TFRecord File Format

**TFRecord** is a simple, record-oriented binary file format designed for storing machine learning training data. It is part of the TensorFlow ecosystem and is commonly used to efficiently ingest large datasets into TensorFlow training pipelines. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Characteristics

TFRecord files store data as a sequence of binary records. Each record can hold a serialized example (e.g., a feature dictionary), making the format well-suited for large-scale ML workloads where compressed, high-throughput data loading is required. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Usage with TensorFlow

TensorFlow provides the `tf.data.TFRecordDataset` class to stream over the contents of one or more TFRecord files as part of an input pipeline. This enables efficient reading and preprocessing of large datasets without loading everything into memory at once. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Integration with Apache Spark via `spark-tensorflow-connector`

The [spark-tensorflow-connector](/concepts/spark-tensorflow-connector.md) is a library within the TensorFlow ecosystem that enables conversion between Apache Spark DataFrames and TFRecord files. Using this connector, you can use Spark DataFrame APIs to:

- **Read** TFRecord files into Spark DataFrames.
- **Write** Spark DataFrames to TFRecord files.

This integration allows data engineers to prepare and transform training data using Spark's distributed processing capabilities and then save it in TFRecord format for consumption by TensorFlow models. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Typical Workflow

A common pipeline involves:

1. Preparing and transforming data using Apache Spark DataFrames.
2. Saving the resulting DataFrame to TFRecord files using the `spark-tensorflow-connector`.
3. Loading the TFRecord files in a TensorFlow training script (e.g., with `tf.data.TFRecordDataset`) for model training. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Related Concepts

- TensorFlow
- [Apache Spark DataFrame](/concepts/apache-spark-dataframes-to-tfrecord-conversion.md)
- [spark-tensorflow-connector](/concepts/spark-tensorflow-connector.md)
- [tf.data.TFRecordDataset](/concepts/tfdatatfrecorddataset.md)
- ML training data
- Binary file formats

## Sources

- save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md

# Citations

1. [save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md](/references/save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws-fbcbc329.md)
