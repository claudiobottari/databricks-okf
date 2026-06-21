---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba71dfaff5edd0d39462805bc2a1803fefe2f9211a18ad6d0f9f9cbb914b955e
  pageDirectory: concepts
  sources:
    - prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hugging-face-datasets-on-databricks
    - HFDOD
    - Hugging Face Dataset
    - Hugging Face Datasets Library
    - Hugging Face datasets
    - HuggingFace Datasets
  citations:
    - file: prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
title: Hugging Face Datasets on Databricks
description: Using the Hugging Face Datasets library within Databricks environments to load, prepare, and manage data for fine-tuning LLMs
tags:
  - machine-learning
  - databricks
  - hugging-face
  - data-preparation
timestamp: "2026-06-19T19:57:27.007Z"
---

# Hugging Face Datasets on Databricks

**Hugging Face Datasets on Databricks** refers to the integration of the Hugging Face Datasets library with Databricks for preparing and managing data used to fine-tune open source large language models (LLMs). The integration allows users to load datasets from the Hugging Face Hub, format them as [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md), and then convert them into Hugging Face `Dataset` objects for training with Hugging Face Transformers. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Requirements

To use Hugging Face Datasets on Databricks, the workspace must run **Databricks Runtime for Machine Learning 13.0 or above**, which includes the Hugging Face `datasets` library by default. Additionally, [Unity Catalog](/concepts/unity-catalog.md) must be enabled, and users need the `WRITE VOLUME` privilege on the target Unity Catalog volume, along with `USE SCHEMA` and `USE CATALOG` privileges. Downloading large datasets may require significant compute resources and time. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Loading Data from Hugging Face

The `datasets` library provides the `load_dataset` function to download datasets from the Hugging Face Hub. For example: ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
from datasets import load_dataset
dataset = load_dataset("imdb")
```

To inspect the dataset size before downloading, use `load_dataset_builder` to retrieve `download_size` and `dataset_size` from the dataset metadata. This helps decide whether the data fits within resource constraints. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Formatting Training and Evaluation Data

Before fine-tuning, raw data must be formatted into a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) with columns matching the expectations of the trainer. For text classification, a DataFrame requires a text column and a label column. Labels are often strings, but many Hugging Face `AutoModel` classes (e.g., `AutoModelForSequenceClassification`) expect integer IDs. A mapping between string labels and integer IDs must be created: ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
labels = df.select(df.label).groupBy(df.label).count().collect()
id2label = {index: row.label for (index, row) in enumerate(labels)}
label2id = {row.label: index for (index, row) in enumerate(labels)}
```

Then, a Pandas UDF can replace the string labels with integer IDs in the DataFrame. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Loading a Hugging Face Dataset from a Spark DataFrame

The `datasets.Dataset.from_spark` method converts a Spark DataFrame into a Hugging Face `Dataset`. This is essential because model training occurs on the driver and requires the data to be available in a format the trainer can iterate over. The method caches the dataset, and the `cache_dir` must be a Unity Catalog volume path accessible to all workers. Example: ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
import datasets
train_dataset = datasets.Dataset.from_spark(
    train_df,
    cache_dir="/Volumes/main/default/my-volume/train"
)
test_dataset = datasets.Dataset.from_spark(
    test_df,
    cache_dir="/Volumes/main/default/my-volume/test"
)
```

For large datasets, writing to Unity Catalog can be slow. The `working_dir` parameter allows caching to a temporary disk location (e.g., the local SSD at `/local_disk0/tmp/train`) before moving the final data to Unity Catalog, speeding up the process. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Caching for Datasets

The `datasets` library caches downloaded and processed datasets in `~/.cache/huggingface/datasets` by default. However, this cache is lost when the Databricks cluster terminates. To persist the cache across cluster restarts, Databricks recommends changing the cache location to a Unity Catalog volume by setting the environment variable `HF_DATASETS_CACHE`: ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
import os
os.environ["HF_DATASETS_CACHE"] = "/Volumes/main/default/my-volume/"
```

## Next Steps

Once the data is prepared, it can be used to [fine-tune a Hugging Face model](/concepts/single-gpu-fine-tuning-with-hugging-face-on-databricks.md) on Databricks. A best practices notebook is also provided in the documentation for downloading and preparing datasets of various sizes. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Related Concepts

- Hugging Face Transformers – Library for loading models and tokenizers
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) – Distributed data structure used for formatting training data
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for managing data access and volumes
- Pandas UDF – Used to transform label columns in Spark DataFrames
- Fine-tuning (NLP) – The process of adapting a pretrained model to a specific task
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Required runtime environment

## Sources

- prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md

# Citations

1. [prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md](/references/prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws-b70184e4.md)
