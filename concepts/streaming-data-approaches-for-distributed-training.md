---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a087039ad947140a3096d6f700552b139bfdb3f411fdb64e9e40167b901491d
  pageDirectory: concepts
  sources:
    - prepare-data-for-distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-data-approaches-for-distributed-training
    - SDAFDT
  citations:
    - file: prepare-data-for-distributed-training-databricks-on-aws.md
title: Streaming Data Approaches for Distributed Training
description: Methods for handling very large datasets that do not fit in memory when training distributed machine learning models, including PyTorch IterableDataset, Hugging Face datasets streaming, and Ray Data.
tags:
  - distributed-training
  - data-loading
  - machine-learning
timestamp: "2026-06-19T19:56:53.016Z"
---

# Streaming Data Approaches for Distributed Training

**Streaming data approaches** for distributed training are techniques used to handle very large datasets that do not fit into the memory of a single machine. Instead of loading the entire dataset at once, these approaches load and process data in a sequential, on‑demand fashion, enabling training on datasets that are larger than available RAM while maintaining compatibility with distributed training frameworks. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## PyTorch IterableDataset

[PyTorch](https://pytorch.org) provides the `IterableDataset` class for implementing custom streaming logic. Unlike a map‑style dataset that allows random access to individual samples, an `IterableDataset` yields data sequentially. This is ideal for large datasets where the entire set cannot be stored in memory and where samples are produced on the fly (for example, reading from a database or a remote file system). ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Hugging Face Datasets with Streaming

The [Hugging Face Datasets](https://huggingface.co/docs/datasets/stream) library supports streaming directly from the Hugging Face Hub or from datasets stored in Databricks [Volumes](/concepts/ucvolumedataset.md). When streaming is enabled, the library downloads and processes examples on demand rather than downloading the entire dataset ahead of time. This allows training on extremely large text corpora, such as those used in [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md), without exhausting local storage. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Ray Data

[Ray Data](https://docs.ray.io/en/latest/data/data.html) is a distributed batch data processing library built on top of Ray. It provides a streaming, distributed data pipeline that can read, transform, and batch data across a cluster of workers. Ray Data integrates natively with popular deep learning frameworks and is particularly well suited for workloads that require both data preprocessing and distributed training to be orchestrated together. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Alternative: TFRecord Format

In addition to the streaming approaches above, the TFRecord format—a record‑oriented binary format commonly used by TensorFlow—can serve as a data source for distributed deep learning. The `tf.data.TFRecordDataset` class in TensorFlow reads records from TFRecord files, enabling efficient data loading and preprocessing pipelines for very large datasets. ^[prepare-data-for-distributed-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- PyTorch
- [Hugging Face](/concepts/hugging-face-trainer.md)
- Ray
- TensorFlow
- [Volumes](/concepts/ucvolumedataset.md)
- Databricks Machine Learning

## Sources

- prepare-data-for-distributed-training-databricks-on-aws.md

# Citations

1. [prepare-data-for-distributed-training-databricks-on-aws.md](/references/prepare-data-for-distributed-training-databricks-on-aws-8445664b.md)
