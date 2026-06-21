---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f762bdc88f37cda39cf9a6cf9ed901b20a5c274b7b9e2f14f4f5fe78147b61a
  pageDirectory: concepts
  sources:
    - load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-data-for-distributed-deep-learning
    - SDFDDL
  citations:
    - file: load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
title: Streaming Data for Distributed Deep Learning
description: Streaming approaches for very large datasets that do not fit in memory, including PyTorch IterableDataset, Hugging Face Datasets streaming, and Ray Data.
tags:
  - deep-learning
  - streaming
  - distributed-training
  - pytorch
timestamp: "2026-06-19T19:13:23.524Z"
---

# Streaming Data for Distributed Deep Learning

**Streaming Data for Distributed Deep Learning** refers to techniques for loading and processing training data that does not fit into memory when training large-scale deep learning models across multiple GPUs or nodes. Streaming approaches are essential for [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) workflows where datasets are too large to hold in memory on any single worker.

## Overview

Distributed deep learning training on very large datasets requires data loading strategies that go beyond conventional in-memory approaches. When datasets exceed available memory, streaming techniques allow data to be loaded, processed, and fed to the training loop incrementally. This is particularly important for [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) and [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training at scale. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Streaming Approaches

Several libraries and frameworks provide streaming data capabilities for distributed deep learning:

- **PyTorch IterableDataset**: Provides custom streaming logic for iterable-style datasets. Unlike map-style datasets that require random access, `IterableDataset` loads data sequentially, making it suitable for streaming scenarios where data comes from files, databases, or network sources. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

- **Hugging Face Datasets streaming**: Enables loading datasets hosted on the Hugging Face Hub or stored in volumes without downloading the entire dataset to disk. Streaming mode iterates over data on-the-fly, supporting datasets that are much larger than available memory. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

- **Ray Data**: Provides distributed batch data processing capabilities designed for scalable machine learning workloads. Ray Data handles data loading and transformation across a cluster, making it suitable for streaming data into distributed training jobs. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Shared Storage for Distributed Data Loading

Machine learning applications may need to use shared storage for data loading and model checkpointing, particularly for distributed deep learning. [Unity Catalog](/concepts/unity-catalog.md) provides a unified governance solution for data and AI assets and can be used for accessing data on a cluster using both Spark and local file APIs, enabling consistent data access across distributed workers. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Tabular Data Loading

For tabular machine learning data, you can load from Tables or files (such as CSV). Apache Spark DataFrames can be converted into pandas DataFrames using the PySpark method `toPandas()`, and then optionally converted to NumPy format using `to_numpy()`. This allows tabular data to be processed through Spark's distributed engine before being converted to formats suitable for deep learning frameworks. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Relationship to Distributed Training Hardware

Streaming data becomes particularly important when training models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range. For example, with an [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) providing 640 GB of total GPU memory, datasets used for training large models frequently exceed this capacity, necessitating streaming approaches that feed data continuously during training iterations.

## Related Concepts

- Lazy evaluation
- Data pipeline optimization
- Model checkpointing
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- Iterable-style datasets
- Map-style datasets

## Sources

- load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md

# Citations

1. [load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md](/references/load-data-for-machine-learning-and-deep-learning-databricks-on-aws-dfd2be96.md)
