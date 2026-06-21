---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5864335e5734fc8e1523781468835be00160687c03961e39f910b86366e12c18
  pageDirectory: concepts
  sources:
    - prepare-data-for-distributed-training-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-data-preparation-for-distributed-ml
    - DDPFDM
  citations:
    - file: prepare-data-for-distributed-training-databricks-on-aws.md
title: Databricks Data Preparation for Distributed ML
description: The overall workflow and best practices for preparing data specifically on the Databricks platform to support distributed machine learning training.
tags:
  - databricks
  - machine-learning
  - data-preparation
timestamp: "2026-06-19T19:57:35.400Z"
---

# Databricks Data Preparation for Distributed ML

**Databricks Data Preparation for Distributed ML** covers the methods and best practices for loading and preparing large-scale datasets for distributed machine learning training on Databricks. When datasets are too large to fit into a single machine’s memory, streaming and specialised binary formats become essential to feed data efficiently to distributed training jobs. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Streaming Approaches for Very Large Datasets

For datasets that exceed available memory, you should use streaming approaches that load data on‑demand instead of loading the entire dataset into memory at once. Databricks recommends three primary streaming strategies: ^[prepare-data-for-distributed-training-databricks-on-aws.md]

### PyTorch IterableDataset

PyTorch’s `IterableDataset` provides a flexible interface for implementing custom streaming logic. It allows you to define how data is read from a source (such as a database, a set of files, or an API) and streamed to the training loop, making it ideal for datasets that are too large to materialise fully. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

### Hugging Face Datasets with Streaming

[Hugging Face](/concepts/hugging-face-trainer.md)’s `datasets` library supports streaming from datasets hosted on the Hugging Face Hub or from data stored in Databricks Volumes. When the `streaming=True` flag is set, the dataset loads samples on‑the‑fly without downloading the entire dataset, reducing memory pressure and enabling training on massive corpora. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

### Ray Data

Ray Data is a distributed batch data‑processing library designed to work natively with Ray cluster environments. It handles data loading, transformation, and shuffling at scale, and is well‑suited for distributed ML pipelines that require both data preprocessing and training orchestration. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## TFRecord Format

The **TFRecord** format is a simple, record‑oriented binary format commonly used by TensorFlow applications for training data. It provides efficient serialisation and is supported by TensorFlow’s `tf.data.TFRecordDataset`, which reads records from TFRecord files. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

On Databricks, you can save Apache Spark DataFrames as TFRecord files and later load them using TensorFlow’s dataset API. This workflow bridges the gap between Spark‑based data engineering and TensorFlow‑based model training. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

For more details on saving and loading TFRecord data, refer to the Databricks guides on [Save Apache Spark DataFrames as TFRecord files](/concepts/apache-spark-dataframes-to-tfrecord-conversion.md) and Consuming TFRecord data. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Summary

| Approach | Best suited for | Key component |
|----------|----------------|---------------|
| PyTorch IterableDataset | Custom streaming logic in PyTorch workflows | `torch.utils.data.IterableDataset` |
| Hugging Face datasets (streaming) | Datasets from the Hub or Volumes | `datasets.load_dataset(streaming=True)` |
| Ray Data | Distributed batch data processing | `ray.data` |
| TFRecord | TensorFlow‑centric pipelines | `tf.data.TFRecordDataset` |

Choose the method that aligns with your framework (PyTorch vs. TensorFlow) and your need for custom streaming or distributed preprocessing. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- PyTorch Data Loading
- TensorFlow Data API
- Databricks Volumes
- [Ray Cluster](/concepts/global-mode-ray-cluster.md)
- Hugging Face Datasets

## Sources

- prepare-data-for-distributed-training-databricks-on-aws.md

# Citations

1. [prepare-data-for-distributed-training-databricks-on-aws.md](/references/prepare-data-for-distributed-training-databricks-on-aws-8445664b.md)
