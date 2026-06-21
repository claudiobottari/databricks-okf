---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8dfa1f59ae384e9b00517c66863f38e01b88397e39b476d592c254bd93cb13a5
  pageDirectory: concepts
  sources:
    - save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loading-tfrecords-into-spark-dataframes
    - LTISD
  citations:
    - file: save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
title: Loading TFRecords into Spark DataFrames
description: The process of reading TFRecord files into Apache Spark DataFrames using the spark-tensorflow-connector library.
tags:
  - apache-spark
  - data-ingestion
  - tensorflow
timestamp: "2026-06-19T20:18:32.913Z"
---

# Loading TFRecords into Spark DataFrames

Loading TFRecord files into Apache Spark DataFrames is a common task when preparing machine learning training data that originates in TensorFlow’s native binary format. The TFRecord format is a simple record-oriented binary format, and Spark can consume it directly using the `spark-tensorflow-connector` library. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## The `spark-tensorflow-connector` Library

The [spark-tensorflow-connector](https://github.com/tensorflow/ecosystem/tree/master/spark/spark-tensorflow-connector) is a library within the [TensorFlow ecosystem](https://github.com/tensorflow/ecosystem) that enables conversion between Spark DataFrames and [TFRecord](/concepts/tfrecord-format.md) files. With this library, you can use Spark DataFrame APIs to read TFRecord files into DataFrames and write DataFrames as TFRecords. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Loading TFRecord Files into DataFrames

To load TFRecord data into a Spark DataFrame, you use the DataFrame reader API with the `tfrecord` format. The library parses the binary records and presents them as a structured DataFrame, making the data immediately available for Spark transformations, analysis, or downstream ML pipelines. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

```python
df = spark.read.format("tfrecord").load("path/to/tfrecords")
```

After loading, you can process the DataFrame using standard Apache Spark operations or save it to other formats for training with TensorFlow.

## Example: Load and Use TFRecord Data with TensorFlow

The Databricks documentation provides a notebook example that demonstrates how to save data from Spark DataFrames to TFRecord files and then load those TFRecord files for ML training. You can load the TFRecord files using the `tf.data.TFRecordDataset` class from TensorFlow (see [Reading a TFRecord file](https://www.tensorflow.org/tutorials/load_data/tfrecord#reading_a_tfrecord_file) for details). ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

## Related Concepts

- [TFRecord](/concepts/tfrecord-format.md) – The binary file format used for TensorFlow training data.
- Apache Spark – The distributed computing engine that hosts DataFrames.
- TensorFlow – The ML framework that consumes TFRecord files.
- DataFrame Reader – The Spark API used to read structured data.
- Distributed DL Training – The broader workflow in which TFRecord loading occurs.

## Sources

- save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md

# Citations

1. [save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md](/references/save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws-fbcbc329.md)
