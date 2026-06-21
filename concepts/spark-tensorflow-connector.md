---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d8a0f7e478eb8d360abd044083b46fe6a83e30fb7eb68cfa878d8e87f6d4563
  pageDirectory: concepts
  sources:
    - save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  citations:
    - file: save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
title: spark-tensorflow-connector
description: A TensorFlow ecosystem library that enables conversion between Apache Spark DataFrames and TFRecord files.
tags:
  - apache-spark
  - tensorflow
  - data-conversion
timestamp: "2026-06-19T20:18:32.625Z"
---

Here is the wiki page for "spark-tensorflow-connector".

## spark-tensorflow-connector

The **spark-tensorflow-connector** is a library within the TensorFlow ecosystem that enables conversion between Apache Spark DataFrames and TFRecord files. TFRecord is a simple, record-oriented binary format commonly used for machine learning training data in TensorFlow. Using the connector, you can read TFRecord files into Spark DataFrames and write Spark DataFrames as TFRecords using standard Spark DataFrame APIs. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Purpose and Benefits

The primary purpose of the spark-tensorflow-connector is to bridge the gap between Apache Spark data processing pipelines and TensorFlow training workflows. Data scientists and engineers can prepare and transform data at scale using Spark, then save the processed data in TFRecord format for consumption by TensorFlow's input pipeline, particularly the `tf.data.TFRecordDataset` class. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

Key benefits include:
- Leverage Spark’s distributed processing capabilities for large-scale data transformation.
- Store preprocessed data in a format optimized for TensorFlow’s input pipeline.
- Stream over one or more TFRecord files as part of a TensorFlow input pipeline using `tf.data.TFRecordDataset`. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Usage

The spark-tensorflow-connector allows you to use Spark DataFrame APIs to:
- **Write** a DataFrame to TFRecord files.
- **Read** TFRecord files into a DataFrame for further processing.

After saving data to TFRecord files, you can load them using the `tf.data.TFRecordDataset` class in TensorFlow, a standard approach for building ML training pipelines. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Related Concepts

- [TFRecord File Format](/concepts/tfrecord-file-format.md) – The binary record format used by TensorFlow.
- [tf.data.TFRecordDataset](/concepts/tfdatatfrecorddataset.md) – TensorFlow API for streaming data from TFRecord files.
- Apache Spark DataFrames – The primary data structure used by Spark.
- [TensorFlow Ecosystem](/concepts/tensorflow-ecosystem.md) – The broader collection of libraries and tools around TensorFlow.
- [Distributed ML Training](/concepts/workload-yaml-for-distributed-training.md) – Workflow where spark-tensorflow-connector plays a role in data preparation.

## Sources

- save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md

# Citations

1. [save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md](/references/save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws-fbcbc329.md)
