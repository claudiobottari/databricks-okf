---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec885edf3848d5b7f30ec63235a2d2b40e23d87852424271f03bc80f56ccbf21
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-loading-with-delta-lake-for-deep-learning
    - DLWDLFDL
    - Data Loading for Deep Learning
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Data Loading with Delta Lake for Deep Learning
description: Using Delta Lake tables and streaming approaches (PyTorch IterableDataset, Hugging Face datasets, Ray Data) to optimize data throughput for large deep learning datasets.
tags:
  - data-loading
  - delta-lake
  - deep-learning
timestamp: "2026-06-19T09:09:41.135Z"
---

# Data Loading with Delta Lake for Deep Learning

**Data Loading with [Delta Lake](/concepts/delta-lake.md) for Deep Learning** refers to the use of [Delta Lake](/concepts/delta-lake.md) tables to efficiently store and load large-scale training and inference data within the [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) environment. Delta Lake overcomes the I/O limitations of typical cloud storage, making it suitable for deep learning workloads that require high data throughput. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Overview

Cloud data storage is often not optimized for the I/O demands of deep learning models, which require large datasets. Databricks Runtime ML includes Delta Lake as a built-in tool to optimize data throughput for these applications. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Databricks recommends using Delta Lake tables as the primary storage format for deep learning data. Delta Lake simplifies Extract, Transform, Load (ETL) and enables efficient data access for both training and inference. This is especially beneficial for image-based workloads, where Delta Lake helps optimize ingestion and preprocessing pipelines. A reference solution for image ETL and inference provides a concrete example of this approach. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Streaming Approaches for Large Datasets

When datasets are too large to fit into memory, Databricks advises using streaming-based data loading strategies rather than loading the entire dataset at once. The following streaming methods are supported and recommended:

- PyTorch IterableDataset for custom streaming logic in PyTorch workflows.
- [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming for datasets hosted on the Hugging Face Hub or stored in Databricks volumes.
- Ray Data for distributed batch data processing across a cluster.

^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices Summary

- Use Delta Lake tables to store training and inference data for better I/O performance.
- For image-heavy workloads, follow the reference solution for image ETL and inference to optimize ingestion.
- When data exceeds available memory, switch to one of the streaming approaches above instead of loading data eagerly. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- Model training best practices on Databricks
- Batch and streaming inference
- PyTorch data loading
- [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md)
- Ray Data

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
