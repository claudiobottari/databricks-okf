---
title: Prepare data for distributed training | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/load-data/ddl-data
ingestedAt: "2026-06-18T08:11:16.771Z"
---

This article describes methods for preparing data for distributed training.

For very large datasets that do not fit in memory, use streaming approaches:

*   [PyTorch IterableDataset](https://docs.pytorch.org/docs/stable/data.html#iterable-style-datasets) for custom streaming logic.
*   [Hugging Face datasets](https://huggingface.co/docs/datasets/stream) with streaming for datasets hosted on the Hub or in volumes.
*   [Ray Data](https://docs.ray.io/en/latest/data/data.html) for distributed batch data processing.

## TFRecord[​](#tfrecord "Direct link to TFRecord")

You can also use TFRecord format as the data source for distributed deep learning. TFRecord format is a simple record-oriented binary format that many TensorFlow applications use for training data.

[tf.data.TFRecordDataset](https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset) is the TensorFlow dataset, which is comprised of records from TFRecords files. For more details about how to consume TFRecord data, see the TensorFlow guide [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data).

The following articles describe and illustrate the recommended ways to save your data to TFRecord files and load TFRecord files:

*   [Save Apache Spark DataFrames as TFRecord files](https://docs.databricks.com/aws/en/machine-learning/load-data/tfrecords-save-load)
