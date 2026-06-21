---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03001c9c2536fc9804a172d4fda9ac1875b14611295b37b21724cc4502fe7363
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-for-deep-learning-data-loading
    - DLFDLDL
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Delta Lake for Deep Learning Data Loading
description: Using Delta Lake tables to optimize data throughput for deep learning workloads, particularly for image ETL and large-scale training.
tags:
  - data-loading
  - delta-lake
  - deep-learning
timestamp: "2026-06-19T17:40:55.002Z"
---

# Delta Lake for Deep Learning Data Loading

**Delta Lake for Deep Learning Data Loading** refers to the practice of using [Delta Lake](/concepts/delta-lake.md) tables as the primary storage format for data used in deep learning workflows on [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). Cloud data storage is typically not optimized for I/O, which can be a challenge for deep learning models that require large datasets. Databricks Runtime ML includes Delta Lake to optimize data throughput for deep learning applications. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Benefits for Deep Learning

Databricks recommends using Delta Lake tables for data storage in deep learning applications. Delta Lake simplifies ETL and lets you access data efficiently. Especially for images, Delta Lake helps optimize ingestion for both training and inference. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## ETL Optimization

For image applications specifically, Databricks provides a reference solution for image ETL & inference that demonstrates how to optimize ETL using Delta Lake. This reference solution serves as a practical example of preparing image data efficiently for deep learning pipelines. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Streaming for Large Datasets

For very large datasets that do not fit in memory, Databricks recommends using streaming approaches rather than loading data entirely into memory: ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- PyTorch IterableDataset – for custom streaming logic that integrates directly with PyTorch data loading pipelines.
- Hugging Face Datasets with streaming – for datasets hosted on the Hugging Face Hub or stored in Databricks Volumes.
- Ray Data – for distributed batch data processing across multiple nodes.

## Relationship to Broader Best Practices

Delta Lake for data loading is one component of the [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) framework. Coupled with proper GPU scheduling and appropriate infrastructure choices like [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md), Delta Lake-based data loading helps create an end-to-end optimized deep learning pipeline. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying ACID-compliant storage layer used for data loading.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime environment that includes Delta Lake and deep learning libraries.
- GPU Scheduling – Techniques for maximizing GPU utilization during training and inference.
- Cluster policies – Configuration guidance for selecting appropriate compute resources.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Model tracking and experiment management for deep learning workflows.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
