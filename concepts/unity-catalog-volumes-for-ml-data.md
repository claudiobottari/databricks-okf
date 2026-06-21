---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83347552c1a24d36c3e01132e87ca680198e33fdb2be82a02e5d99ad340054d1
  pageDirectory: concepts
  sources:
    - prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volumes-for-ml-data
    - UCVFMD
    - Unity Catalog Volumes|Unity Catalog volume
    - Unity Catalog Volumes|volume
  citations:
    - file: prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
title: Unity Catalog Volumes for ML Data
description: Using Unity Catalog volumes as persistent, cluster-independent storage for machine learning training data and Hugging Face dataset caches on Databricks
tags:
  - databricks
  - storage
  - unity-catalog
  - data-management
timestamp: "2026-06-19T19:57:35.264Z"
---

## Unity Catalog Volumes for ML Data

**Unity Catalog Volumes for ML Data** refers to the use of [Unity Catalog](/concepts/unity-catalog.md) volumes as a persistent, shared storage location for machine learning datasets loaded from [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md) via the Hugging Face `datasets` library. This pattern is particularly relevant when preparing data for fine-tuning models with Hugging Face Transformers on Databricks.

### Usage in Dataset Loading

When loading a Spark DataFrame into a Hugging Face dataset using `datasets.Dataset.from_spark`, the method requires a `cache_dir` parameter. This cache directory must be a Unity Catalog volume path (e.g., `/Volumes/main/default/my-volume/train`) because cache materialization is parallelized using Spark and the resulting files must be accessible to all worker nodes. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

For example:

```python
train_dataset = datasets.Dataset.from_spark(
    train_df,
    cache_dir="/Volumes/main/default/my-volume/train"
)
```

Access to the Unity Catalog volume is managed through [Unity Catalog](/concepts/unity-catalog.md) permissions. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

### Required Permissions

To write data to a Unity Catalog volume, the following permissions are required:

- **WRITE VOLUME** privilege on the target volume.
- **USE SCHEMA** privilege on the parent schema.
- **USE CATALOG** privilege on the parent catalog.

^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

### Optimizing for Large Datasets

For large datasets, writing directly to a Unity Catalog volume can be slow. To speed up the process, the `working_dir` parameter can be used. This instructs Hugging Face `datasets` to write the dataset to a temporary location on local disk (e.g., SSD) first, then move it to the Unity Catalog volume. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
dataset = datasets.Dataset.from_spark(
    train_df,
    cache_dir="/Volumes/main/default/my-volume/train",
    working_dir="/local_disk0/tmp/train"
)
```

### Persistent Cache for Hugging Face Datasets

By default, Hugging Face `datasets` caches downloaded and processed data in `~/.cache/huggingface/datasets`. This cache is lost when a cluster terminates. To persist the cache across cluster restarts, Databricks recommends setting the environment variable `HF_DATASETS_CACHE` to a Unity Catalog volume path. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
import os
os.environ["HF_DATASETS_CACHE"] = "/Volumes/main/default/my-volume/"
```

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Governance and storage management for data and AI assets.
- Hugging Face Transformers – Library for loading and fine-tuning transformer models.
- Fine-tuning – Process of adapting a pretrained model to a specific task.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The ML-specific runtime that includes Hugging Face libraries.
- [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md) – Distributed data structure used to prepare training data.
- Cache directory – Local or shared storage for intermediate dataset materialization.

### Sources

- prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md

# Citations

1. [prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md](/references/prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws-b70184e4.md)
