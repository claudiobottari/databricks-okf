---
title: Load data for machine learning and deep learning | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/load-data/
ingestedAt: "2026-06-18T08:11:15.337Z"
---

This section covers information about loading data specifically for ML and DL applications. For general information about loading data, see [Standard connectors in Lakeflow Connect](https://docs.databricks.com/aws/en/ingestion/).

## Store files for data loading and model checkpointing[​](#store-files-for-data-loading-and-model-checkpointing "Direct link to Store files for data loading and model checkpointing")

Machine learning applications may need to use shared storage for data loading and model checkpointing. This is particularly important for distributed deep learning.

Databricks provides [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/), a unified governance solution for data and AI assets. You can use Unity Catalog for accessing data on a cluster using both Spark and local file APIs.

## Load tabular data[​](#load-tabular-data "Direct link to Load tabular data")

You can load tabular machine learning data from [tables](https://docs.databricks.com/aws/en/tables/) or files (for example, see [Read and write CSV files](https://docs.databricks.com/aws/en/query/formats/csv)). You can convert Apache Spark DataFrames into pandas DataFrames using the [PySpark method](https://docs.databricks.com/aws/en/pyspark/reference/classes/dataframe/toPandas) `toPandas()`, and then optionally convert to NumPy format using the [PySpark method](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.to_numpy.html) `to_numpy()`.

## Prepare data to fine tune large language models[​](#prepare-data-to-fine-tune-large-language-models "Direct link to Prepare data to fine tune large language models")

You can prepare your data for fine-tuning open source large language models with [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) and [Hugging Face Datasets](https://huggingface.co/docs/datasets/index).

[Prepare data for fine tuning Hugging Face models](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data)

## Prepare data for distributed deep learning training[​](#prepare-data-for-distributed-deep-learning-training "Direct link to Prepare data for distributed deep learning training")

This section covers preparing data for [distributed deep learning training](https://docs.databricks.com/aws/en/machine-learning/load-data/ddl-data).

For very large datasets that do not fit in memory, use streaming approaches:

*   [PyTorch IterableDataset](https://docs.pytorch.org/docs/stable/data.html#iterable-style-datasets) for custom streaming logic.
*   [Hugging Face datasets](https://huggingface.co/docs/datasets/stream) with streaming for datasets hosted on the Hub or in volumes.
*   [Ray Data](https://docs.ray.io/en/latest/data/data.html) for distributed batch data processing.
