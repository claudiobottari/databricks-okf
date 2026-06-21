---
title: Load data using Petastorm | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/machine-learning/petastorm
ingestedAt: "2026-06-18T08:02:54.776Z"
---

This article describes how to use [Petastorm](https://github.com/uber/petastorm) convert data from Apache Spark to TensorFlow or PyTorch. It also provides an example showing how to use Petastorm to prepare data for ML.

note

The `petastorm` package is deprecated. [Mosaic Streaming](https://docs.databricks.com/aws/en/machine-learning/load-data/streaming) is the recommended replacement for loading large datasets from cloud storage.

Petastorm is an open source data access library. It enables single-node or distributed training and evaluation of deep learning models directly from datasets in Apache Parquet format and datasets that are already loaded as Apache Spark DataFrames. Petastorm supports popular Python-based machine learning (ML) frameworks such as TensorFlow, PyTorch, and PySpark. For more information about Petastorm, see the [Petastorm API documentation](https://petastorm.readthedocs.io/en/latest).

## Load data from Spark DataFrames using Petastorm[​](#load-data-from-spark-dataframes-using-petastorm "Direct link to load-data-from-spark-dataframes-using-petastorm")

The Petastorm Spark converter API simplifies data conversion from Spark to TensorFlow or PyTorch. The input Spark DataFrame is first materialized in Parquet format and then loaded as a `tf.data.Dataset` or `torch.utils.data.DataLoader`. See the [Spark Dataset Converter API section](https://petastorm.readthedocs.io/en/latest/api.html#module-petastorm.spark.spark_dataset_converter) in the Petastorm API documentation.

The recommended workflow is:

1.  Use Apache Spark to load and optionally preprocess data.
2.  Use the Petastorm `spark_dataset_converter` method to convert data from a Spark DataFrame to a TensorFlow Dataset or a PyTorch DataLoader.
3.  Feed data into a DL framework for training or inference.

## Configure cache directory[​](#configure-cache-directory "Direct link to Configure cache directory")

The Petastorm Spark converter caches the input Spark DataFrame in Parquet format in a user-specified cache directory location. The cache directory must be a DBFS path starting with `file:///dbfs/`, for example, `file:///dbfs/tmp/foo/` which refers to the same location as `dbfs:/tmp/foo/`. You can configure the cache directory in two ways:

*   In the cluster [Spark config](https://docs.databricks.com/aws/en/compute/configure#spark-configuration) add the line: `petastorm.spark.converter.parentCacheDirUrl file:///dbfs/...`
    
*   In your notebook, call `spark.conf.set()`:
    
    Python
    
        from petastorm.spark import SparkDatasetConverter, make_spark_converterspark.conf.set(SparkDatasetConverter.PARENT_CACHE_DIR_URL_CONF, 'file:///dbfs/...')
    

You can either explicitly delete the cache after using it by calling `converter.delete()` or manage the cache implicitly by configuring the lifecycle rules in your object storage.

Databricks supports DL training in three scenarios:

*   Single-node training
*   Distributed hyperparameter tuning
*   Distributed training

For end-to-end examples, see the following notebooks:

*   [Simplify data conversion from Spark to TensorFlow](#petastorm-tensorflow)
*   [Simplify data conversion from Spark to PyTorch](#petastorm-pytorch)

## Load Parquet files directly using Petastorm[​](#load-parquet-files-directly-using-petastorm "Direct link to Load Parquet files directly using Petastorm")

This method is less preferred than the Petastorm Spark converter API.

The recommended workflow is:

1.  Use Apache Spark to load and optionally preprocess data.
2.  Save data in Parquet format into a DBFS path that has a companion DBFS mount.
3.  Load data in Petastorm format via the DBFS mount point.
4.  Use data in a DL framework for training or inference.

See [example notebook](#petastorm-example) for an end-to-end example.

## Examples: Preprocess data and train models with TensorFlow or PyTorch[​](#examples-preprocess-data-and-train-models-with-tensorflow-or-pytorch "Direct link to Examples: Preprocess data and train models with TensorFlow or PyTorch")

This example notebook demonstrates the following workflow on Databricks:

1.  Load data using Spark.
2.  Convert the Spark DataFrame to a TensorFlow Dataset using Petastorm.
3.  Feed the data into a single-node TensorFlow model for training.
4.  Feed the data into a distributed hyperparameter tuning function.
5.  Feed the data into a distributed TensorFlow model for training.

#### Simplify data conversion from Spark to TensorFlow notebook

This example notebook demonstrates the following workflow on Databricks:

1.  Load data using Spark.
2.  Convert the Spark DataFrame to a PyTorch DataLoader using Petastorm.
3.  Feed the data into a single-node PyTorch model for training.
4.  Feed the data into a distributed hyperparameter tuning function.
5.  Feed the data into a distributed PyTorch model for training.

#### Simplify data conversion from Spark to PyTorch notebook

## Example: Preprocess data and load Parquet files with Petastorm[​](#example-preprocess-data-and-load-parquet-files-with-petastorm "Direct link to Example: Preprocess data and load Parquet files with Petastorm")

This example notebook shows you the following workflow on Databricks:

1.  Use Spark to load and preprocess data.
2.  Save data using Parquet under `dbfs:/ml`.
3.  Load data using Petastorm via the optimized FUSE mount `file:/dbfs/ml`.
4.  Feed data into a deep learning framework for training or inference.

#### Use Spark and Petastorm to prepare data for deep learning notebook
