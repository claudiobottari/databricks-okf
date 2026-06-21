---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c8976406c1f8996536cb3b74061db64b8209a5735c0e8b407a2620946c27dc0c
  pageDirectory: concepts
  sources:
    - prepare-data-for-distributed-training-databricks-on-aws.md
    - save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - tfdatatfrecorddataset
  citations:
    - file: prepare-data-for-distributed-training-databricks-on-aws.md
    - file: save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md
title: tf.data.TFRecordDataset
description: A TensorFlow dataset class that reads records from TFRecord files, enabling efficient consumption of TFRecord data for training.
tags:
  - tensorflow
  - dataset-api
  - data-loading
timestamp: "2026-06-19T19:57:29.422Z"
---

## `tf.data.TFRecordDataset`

**`tf.data.TFRecordDataset`** is a TensorFlow dataset class that streams records from one or more [TFRecord](/concepts/tfrecord-format.md) files. It is designed to form the input pipeline for machine learning training, especially when working with large datasets that cannot be loaded entirely into memory. ^[prepare-data-for-distributed-training-databricks-on-aws.md, save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

### Overview

The TFRecord file format is a simple, record-oriented binary format commonly used by TensorFlow applications for training data. `tf.data.TFRecordDataset` enables efficient reading of these files by iterating over records sequentially, making it suitable for distributed training scenarios where data is stored in many shards. ^[prepare-data-for-distributed-training-databricks-on-aws.md, save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

Because the dataset streams data record-by-record, it avoids loading the entire dataset into memory at once. This characteristic is important for very large datasets that do not fit in memory. Alternative streaming approaches include PyTorch IterableDataset, [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming, and Ray Data. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

### Usage with TFRecord Files

To consume TFRecord data, instantiate `tf.data.TFRecordDataset` with the file path(s) of one or more TFRecord files. For example:

```python
import tensorflow as tf

dataset = tf.data.TFRecordDataset(["file1.tfrecord", "file2.tfrecord"])
```

The resulting dataset yields raw bytes for each record; these bytes must be parsed using `tf.io.parse_single_example` or similar functions to reconstruct the original features. The TensorFlow guide on [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data) provides detailed instructions. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

### Relationship with Apache Spark

The `spark-tensorflow-connector` library (part of the TensorFlow ecosystem) allows conversion between Apache Spark DataFrames and TFRecord files. After saving a Spark DataFrame as TFRecords using the connector, you can load the files with `tf.data.TFRecordDataset` and feed them into a TensorFlow training pipeline. This integration bridges data processing in Spark and model training in TensorFlow. ^[save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md]

### Related Concepts

- [TFRecord](/concepts/tfrecord-format.md) – The binary file format read by this dataset.
- tf.data – The TensorFlow input pipeline API of which `TFRecordDataset` is a part.
- [spark-tensorflow-connector](/concepts/spark-tensorflow-connector.md) – Library for reading/writing TFRecords from Apache Spark.
- Apache Spark – A distributed data processing engine that can produce TFRecord files.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Training workloads that benefit from sharded TFRecord datasets.
- Data Streaming – Techniques for handling datasets that exceed memory capacity.

### Sources

- prepare-data-for-distributed-training-databricks-on-aws.md
- save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md

# Citations

1. [prepare-data-for-distributed-training-databricks-on-aws.md](/references/prepare-data-for-distributed-training-databricks-on-aws-8445664b.md)
2. [save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws.md](/references/save-apache-spark-dataframes-as-tfrecord-files-databricks-on-aws-fbcbc329.md)
