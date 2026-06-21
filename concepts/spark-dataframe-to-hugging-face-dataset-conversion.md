---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25ef3281a645d81a84310f2d6be43cc101d02a26e0dc673e636fee40ee6188b3
  pageDirectory: concepts
  sources:
    - prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-dataframe-to-hugging-face-dataset-conversion
    - SDTHFDC
    - Loading data for Hugging Face fine-tuning
  citations:
    - file: prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
title: Spark DataFrame to Hugging Face Dataset Conversion
description: Converting Apache Spark DataFrames to Hugging Face Dataset objects using the Dataset.from_spark method for model training
tags:
  - databricks
  - spark
  - hugging-face
  - data-conversion
timestamp: "2026-06-19T19:57:36.388Z"
---

# Spark DataFrame to Hugging Face Dataset Conversion

**Spark DataFrame to Hugging Face Dataset Conversion** refers to the process of converting a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) into a [Hugging Face Dataset](/concepts/hugging-face-datasets-on-databricks.md) using the `datasets.Dataset.from_spark()` method. This conversion enables users to leverage Hugging Face’s training utilities — such as Hugging Face Transformers fine‑tuning — while benefiting from Spark’s distributed data processing capabilities. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Overview

When preparing data for fine‑tuning open‑source large language models with Hugging Face Transformers and Hugging Face Datasets, data is first formatted into a Spark DataFrame. The Hugging Face `datasets` library provides the `Dataset.from_spark()` method to convert that DataFrame into a Hugging Face `Dataset` object, which can then be passed directly to the `Trainer` or `TrainerArguments` for fine‑tuning. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Conversion Process

The core method is `datasets.Dataset.from_spark()`. It accepts a Spark DataFrame and returns a Hugging Face `Dataset`. The method caches the dataset to disk during conversion; therefore, the `cache_dir` parameter is required and must point to a location accessible to all worker nodes. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

### Basic Usage

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

`Dataset.from_spark` caches the dataset. Because model training runs on the driver, the cached data must be available to it. Since cache materialization is parallelized using Spark, the provided `cache_dir` must be accessible to all workers. To satisfy these constraints, `cache_dir` should be a Unity Catalog volume path. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

### Accelerating Caching with a Working Directory

If the dataset is large, writing it directly to Unity Catalog can take a long time. To speed up the process, you can use the `working_dir` parameter to have Hugging Face `datasets` write the dataset to a temporary location on local disk (e.g., the cluster’s SSD) and then move it to Unity Catalog. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
dataset = datasets.Dataset.from_spark(
    train_df,
    cache_dir="/Volumes/main/default/my-volume/train",
    working_dir="/local_disk0/tmp/train",
)
```

## Caching for Datasets

The cache is one of the ways `datasets` improves efficiency. It stores all downloaded and processed datasets so that when the user needs to reuse the intermediate datasets, they are reloaded directly from the cache. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

The default cache directory of `datasets` is `~/.cache/huggingface/datasets`. When a cluster is terminated, the cache data is lost. To persist the cache file across cluster restarts, Databricks recommends changing the cache location to a Unity Catalog volume path by setting the environment variable `HF_DATASETS_CACHE`: ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
import os
os.environ["HF_DATASETS_CACHE"] = "/Volumes/main/default/my-volume/"
```

## Requirements

- **Databricks Runtime for Machine Learning** 13.0 or above. The Hugging Face `datasets` library is included in Databricks Runtime 13.0 ML and later. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]
- A workspace with [Unity Catalog](/concepts/unity-catalog.md) enabled.
- The following permissions on the Unity Catalog volume used for caching:
  - `WRITE VOLUME` privilege on the volume.
  - `USE SCHEMA` privilege on the parent schema.
  - `USE CATALOG` privilege on the parent catalog.
- Significant compute resources if downloading large datasets from the Hugging Face Hub before conversion. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Related Concepts

- Hugging Face Datasets – Library for accessing and sharing datasets.
- Hugging Face Transformers – Library for loading and fine‑tuning pre‑trained models.
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) – Distributed collection of data organized into named columns.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance solution for managing access to data assets.
- [Fine‑tuning Hugging Face Models](/concepts/single-gpu-fine-tuning-with-hugging-face-on-databricks.md) – The downstream training step that uses the converted dataset.

## Sources

- prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md

# Citations

1. [prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md](/references/prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws-b70184e4.md)
