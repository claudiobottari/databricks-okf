---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6d2735ebcbbe0da2b55985ec98315150e7ba72bb2df16d901395e0fcb82dcc2
  pageDirectory: concepts
  sources:
    - load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-deep-learning-data-preparation-on-databricks
    - DDLDPOD
  citations:
    - file: load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
title: Distributed Deep Learning Data Preparation on Databricks
description: Strategies for preparing data specifically for distributed deep learning training workloads on Databricks clusters.
tags:
  - deep-learning
  - distributed-training
  - databricks
  - data-preparation
timestamp: "2026-06-19T19:13:21.951Z"
---

# Distributed Deep Learning Data Preparation on Databricks

**Distributed Deep Learning Data Preparation on Databricks** refers to the set of practices, tools, and storage configurations used to prepare and load data for training large-scale deep learning models across multiple GPUs or nodes. The approach emphasizes shared storage, efficient streaming for large datasets, and integration with popular deep learning frameworks.

## Overview

Machine learning applications on Databricks may require shared storage for data loading and model checkpointing, especially in distributed deep learning scenarios. Databricks provides [Unity Catalog](/concepts/unity-catalog.md) as a unified governance solution for data and AI assets, and you can use Unity Catalog to access data on a cluster using both Spark and local file APIs. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Loading Tabular Data

Tabular machine learning data can be loaded from tables or files (e.g., CSV). You can convert Apache Spark DataFrames into pandas DataFrames using the PySpark method `toPandas()`, and optionally convert to NumPy format using `to_numpy()`. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Preparing Data for Fine-Tuning Large Language Models

To fine‑tune open‑source [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md), you can use Hugging Face Transformers and Hugging Face Datasets. Databricks provides guidance on preparing data specifically for this workflow. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Preparing Data for Distributed Deep Learning Training

For very large datasets that do not fit in memory, streaming approaches are recommended. The following methods are supported:

- **PyTorch IterableDataset**: Use `torch.utils.data.IterableDataset` for custom streaming logic in PyTorch workflows.
- **Hugging Face datasets with streaming**: Use the streaming feature of Hugging Face Datasets to load datasets hosted on the Hub or in Databricks volumes without downloading them fully.
- **Ray Data**: Use Ray Data for distributed batch data processing across multiple workers or nodes.

These techniques allow training to begin without waiting for the entire dataset to be loaded, and they scale naturally with distributed training setups. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- Databricks Tables
- PyTorch
- [Hugging Face](/concepts/hugging-face-trainer.md)
- Ray
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- Model Checkpointing
- [Streaming Datasets](/concepts/streamingdataset.md)

## Sources

- load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md

# Citations

1. [load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md](/references/load-data-for-machine-learning-and-deep-learning-databricks-on-aws-dfd2be96.md)
