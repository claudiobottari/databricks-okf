---
title: Save Apache Spark DataFrames as TFRecord files | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/load-data/tfrecords-save-load
ingestedAt: "2026-06-18T08:11:20.014Z"
---

This article shows you how to use spark-tensorflow-connector to save Apache Spark DataFrames to TFRecord files and load TFRecord with TensorFlow.

The TFRecord file format is a simple record-oriented binary format for ML training data. The [tf.data.TFRecordDataset](https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset) class enables you to stream over the contents of one or more TFRecord files as part of an input pipeline.

## Use `spark-tensorflow-connector` library[​](#use-spark-tensorflow-connector-library "Direct link to use-spark-tensorflow-connector-library")

You can use [spark-tensorflow-connector](https://github.com/tensorflow/ecosystem/tree/master/spark/spark-tensorflow-connector) to save Apache Spark DataFrames to TFRecord files.

`spark-tensorflow-connector` is a library within the [TensorFlow ecosystem](https://github.com/tensorflow/ecosystem) that enables conversion between Spark DataFrames and [TFRecords](https://www.tensorflow.org/tutorials/load_data/tfrecord#tfrecord_files_in_python) (a popular format for storing data for TensorFlow). With spark-tensorflow-connector, you can use Spark DataFrame APIs to read TFRecords files into DataFrames and write DataFrames as TFRecords.

## Example: Load data from TFRecord files with TensorFlow[​](#example-load-data-from-tfrecord-files-with-tensorflow "Direct link to Example: Load data from TFRecord files with TensorFlow")

The example notebook demonstrates how to save data from Apache Spark DataFrames to TFRecord files and load TFRecord files for ML training.

You can load the TFRecord files using the `tf.data.TFRecordDataset` class. See [Reading a TFRecord file](https://www.tensorflow.org/tutorials/load_data/tfrecord#reading_a_tfrecord_file) from TensorFlow for details.

#### Prepare image data for Distributed DL notebook
