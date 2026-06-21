---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fdfbdec16efcab123a10dff938b3c2420e3f9afc003ac37b260f473e7fb18e87
  pageDirectory: concepts
  sources:
    - save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - saving-spark-dataframes-to-tfrecords
    - SSDTT
    - Spark DataFrames
  citations:
    - file: save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
title: Saving Spark DataFrames to TFRecords
description: The process of writing Apache Spark DataFrames to the TFRecord binary format using the spark-tensorflow-connector library.
tags:
  - apache-spark
  - data-export
  - tensorflow
timestamp: "2026-06-19T20:18:51.743Z"
---

# Saving Spark DataFrames to TFRecords

**Saving Spark DataFrames to TFRecords** refers to the process of converting Apache Spark DataFrames into the TFRecord binary format using the `spark-tensorflow-connector` library. This enables seamless integration of Spark-based data preprocessing with TensorFlow training pipelines.

## Overview

The TFRecord file format is a simple record-oriented binary format commonly used for storing machine learning training data. TensorFlow provides the `tf.data.TFRecordDataset` class to stream over the contents of one or more TFRecord files as part of an input pipeline. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

The `spark-tensorflow-connector` is a library within the [TensorFlow ecosystem](https://github.com/tensorflow/ecosystem) that bridges Spark DataFrames and TFRecords. It allows you to use standard Spark DataFrame APIs to read TFRecords into DataFrames and write DataFrames out as TFRecords. This conversion is essential when preparing large-scale datasets on Apache Spark for later consumption by TensorFlow models. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Using `spark-tensorflow-connector`

To save a Spark DataFrame as TFRecord files, you attach the `spark-tensorflow-connector` library to your Spark session and use the DataFrame writer with the `"tfrecord"` format. Similarly, to load TFRecord files into a DataFrame, you use the reader with the same format. The connector handles the conversion between Spark data types and TensorFlow’s `Example` protocol buffer.

The exact API calls are not shown in the source, but the pattern follows the standard Spark DataFrame writer:

```python
df.write.format("tfrecord").save("path/to/tfrecords")
```

and reader:

```python
df = spark.read.format("tfrecord").load("path/to/tfrecords")
```

## Example: Loading TFRecord Files with TensorFlow

After saving DataFrames as TFRecords, you can load the files using TensorFlow’s `tf.data.TFRecordDataset` class for model training. The TensorFlow documentation provides detailed instructions on reading TFRecord files. A companion notebook (in the original documentation) demonstrates the end-to-end workflow of saving Spark DataFrames to TFRecord files and subsequently loading them for distributed deep learning. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Related Concepts

- [Apache Spark DataFrame](/concepts/apache-spark-dataframes-to-tfrecord-conversion.md) — The fundamental distributed data structure used in Spark.
- [TFRecord](/concepts/tfrecord-format.md) — The binary record-oriented format designed for TensorFlow.
- TensorFlow — The open-source machine learning framework consuming TFRecord files.
- [spark-tensorflow-connector](/concepts/spark-tensorflow-connector.md) — The library enabling the conversion.
- Machine Learning Training Pipeline — The workflow where TFRecords serve as an intermediate data format.
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) — Training paradigm often combining Spark preprocessing with TensorFlow training.

## Sources

- save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md

# Citations

1. [save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md](/references/save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws-fbcbc329.md)
