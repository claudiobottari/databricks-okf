---
title: Load data using Mosaic Streaming | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/load-data/streaming
ingestedAt: "2026-06-18T08:11:18.243Z"
---

This article describes how to use [Mosaic Streaming](https://docs.mosaicml.com/projects/streaming/en/stable/index.html) to convert data from Apache Spark to a format compatible with PyTorch.

Mosaic Streaming is an open source data loading library. It enables single-node or distributed training and evaluation of deep learning models from datasets that are already loaded as Apache Spark DataFrames. Mosaic Streaming primarily supports Mosaic Composer, but also integrates with native PyTorch, PyTorch Lightning, and the TorchDistributor. Mosaic Streaming provides a series of benefits over traditional PyTorch DataLoaders including:

*   Compatibility with any data type, including images, text, video, and multimodal data.
*   Support for major cloud storage providers (AWS, OCI, GCS, Azure, Databricks UC Volume, and any S3 compatible object store such as Cloudflare R2, Coreweave, Backblaze b2, etc.)
*   Maximizing correctness guarantees, performance, flexibility, and ease of use. For more information, view their [key features](https://docs.mosaicml.com/projects/streaming/en/stable/index.html#key-features) page.

For general information about Mosaic Streaming, view the [Streaming API documentation](https://docs.mosaicml.com/projects/streaming/en/stable/api_reference/streaming.html).

note

Mosaic Streaming has been pre-installed into all versions of the Databricks Runtime 15.2 ML and higher.

## Load data from Spark DataFrames using Mosaic Streaming[​](#load-data-from-spark-dataframes-using-mosaic-streaming "Direct link to Load data from Spark DataFrames using Mosaic Streaming")

Mosaic Streaming provides a straightforward workflow for converting from Apache Spark to the Mosaic Data Shard (MDS) format which can then be loaded for use in a distributed environment.

The recommended workflow is:

1.  Use Apache Spark to load and optionally preprocess data.
2.  Use `streaming.base.converters.dataframe_to_mds` to save the dataframe to disk for transient storage and/or to a Unity Catalog volume for persistent storage. This data will be stored in the MDS format and can be further optimized with support for compression and hashing. Advanced use cases can also include the preprocessing of data using UDFs. View the [Spark DataFrame to MDS tutorial](https://docs.mosaicml.com/projects/streaming/en/stable/preparing_datasets/spark_dataframe_to_mds.html) for more information.
3.  Use `streaming.StreamingDataset` to load the necessary data to memory. `StreamingDataset` is a version of PyTorch's IterableDataset that features elastically deterministic shuffling, which enables fast mid-epoch resumption. View the [StreamingDataset documentation](https://docs.mosaicml.com/projects/streaming/en/stable/api_reference/generated/streaming.StreamingDataset.html#streaming.StreamingDataset) for more information.
4.  Use `streaming.StreamingDataLoader` to load the necessary data for training/evaluation/testing. `StreamingDataLoader` is a version of PyTorch's DataLoader which provides an additional checkpoint/resumption interface, for which it tracks the number of samples seen by the model in this rank.

For an end-to-end example, see the following notebook:

#### Simplify data loading from Spark to PyTorch using Mosaic Streaming notebook

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Authentication error[​](#authentication-error "Direct link to Authentication error")

If you see the following error when loading data from a Unity Catalog volume using `StreamingDataset`, set up the environment variables as shown below.

sh

    ValueError: default auth: cannot configure default credentials, please check https://docs.databricks.com/en/dev-tools/auth.html#databricks-client-unified-authentication to configure credentials for your preferred authentication method.

note

If you see this error when running distributed training using `TorchDistributor`, you must also set the environment variables on the worker nodes.

Python

    db_host = "https://your-databricks-host.databricks.com"db_token = "YOUR API TOKEN" # Create a token with either method from https://docs.databricks.com/en/dev-tools/auth/index.html#databricks-authentication-methodsdef your_training_function():  import os  os.environ['DATABRICKS_HOST'] = db_host  os.environ['DATABRICKS_TOKEN'] = db_token# The above function can be distributed with TorchDistributor:# from pyspark.ml.torch.distributor import TorchDistributor# distributor = TorchDistributor(...)# distributor.run(your_training_function)

### Python 3.11 shared memory issues[​](#python-311-shared-memory-issues "Direct link to Python 3.11 shared memory issues")

Due to issues with Python 3.11's shared memory implementation, `StreamingDataset` can run into transient issues on Databricks Runtime 15.4 LTS for Machine Learning. You can avoid these issues by upgrading to Databricks Runtime 16.4 LTS for Machine Learning, as Python 3.12 addresses these issues.
