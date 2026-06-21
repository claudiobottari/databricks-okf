---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4cb28de38eaf90966f72439e9f25403e45c85ec5fbcc10ac4aa2802636c67f2c
  pageDirectory: concepts
  sources:
    - prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hugging-face-dataset-caching-on-databricks
    - HFDCOD
  citations:
    - file: prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
title: Hugging Face Dataset Caching on Databricks
description: Strategies for persisting Hugging Face dataset caches across cluster lifecycles using Unity Catalog volumes and HF_DATASETS_CACHE environment variable
tags:
  - databricks
  - hugging-face
  - caching
  - performance
timestamp: "2026-06-19T19:57:37.850Z"
---

Here is the wiki page for "Hugging Face Dataset Caching on Databricks", written based solely on the provided source material.

---

## Hugging Face Dataset Caching on Databricks

**Hugging Face Dataset Caching on Databricks** refers to the storage mechanism used by the Hugging Face `datasets` library to persist downloaded and processed datasets, and the recommended practices for managing this cache on the Databricks platform to ensure data persists across cluster lifecycles.

### Overview

The Hugging Face `datasets` library uses a cache to improve efficiency by storing all downloaded and processed datasets. When a user subsequently calls a function that requires a previously loaded dataset, the library reloads it directly from the cache instead of re-downloading or re-processing the data. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

### Default Cache Location and Risk

By default, the cache directory for Hugging Face `datasets` is `~/.cache/huggingface/datasets`. On Databricks, when a cluster is terminated, any data stored in this default local cache location is lost, including cached datasets. This means that any previously downloaded or processed datasets would need to be obtained again after the cluster is restarted. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

### Recommended Configuration for Persistence

To persist the cache file across cluster terminations, Databricks recommends changing the cache location to a Unity Catalog volume path. This can be done by setting the environment variable `HF_DATASETS_CACHE` to a Unity Catalog volume path. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

Python example:

```python
import os
os.environ["HF_DATASETS_CACHE"] = "/Volumes/main/default/my-volume/"
```

### Caching During Dataset Loading from Spark DataFrames

When loading data using `datasets.Dataset.from_spark`, the dataset is cached to the directory specified by the `cache_dir` parameter. Since this cache materialization is parallelized using Spark, the provided `cache_dir` must be accessible to all worker nodes. To satisfy this constraint, Databricks recommends using a Unity Catalog volume path as the `cache_dir`. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

Python example:

```python
import datasets
train_dataset = datasets.Dataset.from_spark(train_df, cache_dir="/Volumes/main/default/my-volume/train")
test_dataset = datasets.Dataset.from_spark(test_df, cache_dir="/Volumes/main/default/my-volume/test")
```

For large datasets, writing directly to Unity Catalog can take a long time. To speed up the process, you can use the `working_dir` parameter to have the `datasets` library write the dataset to a temporary local location first (such as the SSD on the worker nodes), and then move it to Unity Catalog. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
import datasets
dataset = datasets.Dataset.from_spark(
  train_df,
  cache_dir="/Volumes/main/default/my-volume/train",
  working_dir="/local_disk0/tmp/train",
)
```

### Related Concepts

- [Hugging Face Datasets Library](/concepts/hugging-face-datasets-on-databricks.md) — The library that provides caching.
- Unity Catalog Volumes — A storage location recommended for persisting cache data on Databricks.
- Fine-Tuning Hugging Face Models on Databricks — The broader workflow of which data preparation is a part.
- [Prepare Data for Fine-Tuning Hugging Face Models](/concepts/data-preparation-for-llm-fine-tuning-with-hugging-face.md) — The guide covering data loading and formatting.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime that includes the Hugging Face `datasets` library.

### Sources

- prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md

# Citations

1. [prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md](/references/prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws-b70184e4.md)
