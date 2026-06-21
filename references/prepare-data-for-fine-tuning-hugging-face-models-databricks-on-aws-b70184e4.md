---
title: Prepare data for fine tuning Hugging Face models | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data
ingestedAt: "2026-06-18T08:13:30.401Z"
---

This article demonstrates how to prepare your data for fine-tuning open source large language models with [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) and [Hugging Face Datasets](https://huggingface.co/docs/datasets/index).

## Requirements[​](#requirements "Direct link to Requirements")

*   [Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/) 13.0 or above. The examples in this guide use Hugging Face [datasets](https://huggingface.co/docs/datasets/index) which is included in Databricks Runtime 13.0 ML and above.
*   A workspace with Unity Catalog enabled. You also need to have the following permissions in order to write data to a Unity Catalog volume:
    *   The WRITE VOLUME privilege on the volume you want to upload files to.
    *   The USE SCHEMA privilege on the parent schema.
    *   The USE CATALOG privilege on the parent catalog.
*   Significant compute resources for downloading large datasets. The large dataset used in the example notebook provided takes more than a day to download.

## Load data from Hugging Face[​](#load-data-from-hugging-face "Direct link to Load data from Hugging Face")

Hugging Face Datasets is a Hugging Face library for accessing and sharing datasets for audio, computer vision, and natural language processing (NLP) tasks. With Hugging Face `datasets` you can load data from various places. The `datasets` library has utilities for reading datasets from the Hugging Face Hub. There are many datasets downloadable and readable from the Hugging Face Hub by using the `load_dataset` function. Learn more about [loading data with Hugging Face Datasets](https://huggingface.co/docs/datasets/loading) in the Hugging Face documentation.

Python

    from datasets import load_datasetdataset = load_dataset("imdb")

Some datasets in the Hugging Face Hub provide the sizes of data that is downloaded and generated when `load_dataset` is called. You can use `load_dataset_builder` to know the sizes before downloading the dataset with `load_dataset`.

Python

    from datasets import load_dataset_builderfrom psutil._common import bytes2humandef print_dataset_size_if_provided(*args, **kwargs):  dataset_builder = load_dataset_builder(*args, **kwargs)  if dataset_builder.info.download_size and dataset_builder.info.dataset_size:    print(f'download_size={bytes2human(dataset_builder.info.download_size)}, dataset_size={bytes2human(dataset_builder.info.dataset_size)}')  else:    print('Dataset size is not provided by uploader')print_dataset_size_if_provided("imdb")

See the [Download datasets from Hugging Face best practices notebook](#notebook) for guidance on how to download and prepare datasets on Databricks for different sizes of data.

## Format your training and evaluation data[​](#format-your-training-and-evaluation-data "Direct link to Format your training and evaluation data")

To use your own data for model fine-tuning, you must first format your training and evaluation data into Spark DataFrames. Then, load the DataFrames using the Hugging Face `datasets` library.

Start by formatting your training data into a table meeting the expectations of the trainer. For text classification, this is a table with two columns: a text column and a column of labels.

To perform fine-tuning, you need to provide a model. The Hugging Face Transformer [AutoClasses](https://huggingface.co/docs/transformers/model_doc/auto) library makes it easy to load models and configuration settings, including a wide range of `Auto Models` for [natural language processing](https://huggingface.co/docs/transformers/model_doc/auto#natural-language-processing).

For example, Hugging Face `transformers` provides `AutoModelForSequenceClassification` as a model loader for text classification, which expects integer IDs as the category labels. However, if you have a DataFrame with string labels, you must also specify mappings between the integer labels and string labels when creating the model. You can collect this information as follows:

Python

    labels = df.select(df.label).groupBy(df.label).count().collect()id2label = {index: row.label for (index, row) in enumerate(labels)}label2id = {row.label: index for (index, row) in enumerate(labels)}

Then, create the integer IDs as a label column with a Pandas UDF:

Python

    from pyspark.sql.functions import pandas_udfimport pandas as pd@pandas_udf('integer')def replace_labels_with_ids(labels: pd.Series) -> pd.Series:  return labels.apply(lambda x: label2id[x])df_id_labels = df.select(replace_labels_with_ids(df.label).alias('label'), df.text)

## Load a Hugging Face dataset from a Spark DataFrame[​](#load-a-hugging-face-dataset-from-a-spark-dataframe "Direct link to Load a Hugging Face dataset from a Spark DataFrame")

Hugging Face `datasets` supports loading from Spark DataFrames using `datasets.Dataset.from_spark`. See the Hugging Face documentation to learn more about the [from\_spark()](https://huggingface.co/docs/datasets/use_with_spark) method.

For example, if you have `train_df` and `test_df` DataFrames, you can create datasets for each with the following code:

Python

    import datasetstrain_dataset = datasets.Dataset.from_spark(train_df, cache_dir="/Volumes/main/default/my-volume/train")test_dataset = datasets.Dataset.from_spark(test_df, cache_dir="/Volumes/main/default/my-volume/test")

`Dataset.from_spark` caches the dataset. This example describes model training on the driver, so data must be made available to it. Additionally, since cache materialization is parallelized using Spark, the provided `cache_dir` must be accessible to all workers. To satisfy these constraints, `cache_dir` should be a [Unity Catalog volume path](https://docs.databricks.com/aws/en/volumes/).

Access to the volume can be managed using [Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/).

If your dataset is large, writing it to Unity Catalog can take a long time. To speed up the process, you can use the `working_dir` parameter to have Hugging Face `datasets` write the dataset to a temporary location on disk, then move it to Unity Catalog. For example, to use the SSD as a temporary location:

Python

    import datasetsdataset = datasets.Dataset.from_spark(  train_df,  cache_dir="/Volumes/main/default/my-volume/train",  working_dir="/local_disk0/tmp/train",)

## Caching for datasets[​](#caching-for-datasets "Direct link to Caching for datasets")

The cache is one of the ways `datasets` improves efficiency. It stores all downloaded and processed datasets so when the user needs to use the intermediate datasets, they are reloaded directly from the cache.

The default cache directory of datasets is `~/.cache/huggingface/datasets`. When a cluster is terminated, the cache data is lost too. To persist the cache file on cluster termination, Databricks recommends changing the cache location to a Unity Catalog volume path by setting the environment variable `HF_DATASETS_CACHE`:

Python

    import osos.environ["HF_DATASETS_CACHE"] = "/Volumes/main/default/my-volume/"

## Fine-tune a model[​](#fine-tune-a-model "Direct link to Fine-tune a model")

When your data is ready, you can use it to [fine-tune a Hugging Face model](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/fine-tune-model).

## Notebook: Download datasets from Hugging Face[​](#notebook-download-datasets-from-hugging-face "Direct link to notebook-download-datasets-from-hugging-face")

This example notebook provides recommended best practices of using the Hugging Face `load_dataset` function to download and prepare datasets on Databricks for different sizes of data.

#### Download datasets from Hugging Face best practices notebook
