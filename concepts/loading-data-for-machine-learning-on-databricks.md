---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4821e6e2d3254ffd8d46f517c3215206e01075a222991b290793d83020e0aab
  pageDirectory: concepts
  sources:
    - load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loading-data-for-machine-learning-on-databricks
    - LDFMLOD
    - Load Data for Machine Learning
  citations:
    - file: load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
title: Loading Data for Machine Learning on Databricks
description: Best practices and patterns for loading data specifically for ML and DL workloads on Databricks, as distinct from general data ingestion.
tags:
  - databricks
  - machine-learning
  - data-loading
timestamp: "2026-06-19T19:13:13.306Z"
---

# Loading Data for Machine Learning on Databricks

**Loading Data for Machine Learning on Databricks** covers the specific considerations, tools, and best practices for preparing and loading data used in machine learning (ML) and deep learning (DL) workloads on the Databricks platform. This is distinct from general data ingestion, as ML and DL applications have unique requirements for shared storage, distributed access, and efficient data streaming.

## Core Concepts

### Shared Storage for Distributed Workloads

Machine learning applications, particularly distributed deep learning training, often require **shared storage** for two critical purposes: **data loading** and **model checkpointing**. Shared storage ensures that all worker nodes in a distributed cluster can access the same training data and can save model checkpoints to a location visible to all nodes. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

Databricks provides **Unity Catalog** as a unified governance solution for data and AI assets. You can use Unity Catalog to access data on a cluster using both Spark and local file APIs. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

For more details on general data loading, see the Standard connectors in Lakeflow Connect.

### Tabular Data Loading

You can load tabular machine learning data from **tables** or files (for example, see Read and write CSV files). A common workflow is to convert Apache Spark DataFrames into pandas DataFrames using the PySpark method `toPandas()`, and then optionally convert to NumPy format using the `to_numpy()` method. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Data Preparation for Fine-Tuning Large Language Models

You can prepare your data for fine-tuning open source large language models with **Hugging Face Transformers** and **Hugging Face Datasets**. For specific guidance, see [Prepare data for fine tuning Hugging Face models](/concepts/data-preparation-for-llm-fine-tuning-with-hugging-face.md). ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Data Preparation for Distributed Deep Learning

For very large datasets that do not fit in memory, you should use streaming approaches. The following are key libraries and techniques for streaming data in distributed deep learning training:

- **PyTorch IterableDataset**: For custom streaming logic within PyTorch.
- **[Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md)**: For streaming datasets hosted on the Hub or in volumes.
- **Ray Data**: For distributed batch data processing.

Streaming is essential for handling large-scale training data without requiring it all to be loaded into RAM at once. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – A unified governance solution for data and AI assets.
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) – Training that requires shared storage for data and checkpoints.
- [Databricks on AWS](/concepts/databricks-on-aws.md) – The specific cloud platform for these features.
- Model Checkpointing – Saving model state to shared storage.
- Apache Spark DataFrames – The primary data structure for tabular data processing.
- [Hugging Face](/concepts/hugging-face-trainer.md) – Ecosystem for loading and processing pre-trained models.

## Sources

- load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md

# Citations

1. [load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md](/references/load-data-for-machine-learning-and-deep-learning-databricks-on-aws-dfd2be96.md)
