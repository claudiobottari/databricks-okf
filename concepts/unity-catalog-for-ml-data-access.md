---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e96a6d7b83be9e5f9a1ba903529e2174fa10c12e320a37fa1c45662274e4d59
  pageDirectory: concepts
  sources:
    - load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-ml-data-access
    - UCFMDA
  citations:
    - file: load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
title: Unity Catalog for ML Data Access
description: Using Unity Catalog as a unified governance solution to access data on clusters via both Spark and local file APIs for ML workloads.
tags:
  - databricks
  - unity-catalog
  - data-governance
timestamp: "2026-06-19T19:13:04.256Z"
---

# Unity Catalog for ML Data Access

**Unity Catalog for ML Data Access** refers to the use of [Unity Catalog](/concepts/unity-catalog.md) — Databricks’ unified governance solution for data and AI assets — to manage and load data for machine learning and deep learning workloads. Unity Catalog provides a single, governed layer that spans data lakes and AI assets, enabling consistent access control, lineage, and discovery across the ML lifecycle. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Key Capabilities

Unity Catalog supports two primary API paths for accessing data during ML training:

- **Spark APIs** – Data can be loaded as tables that are registered in Unity Catalog, then converted to ML-friendly formats such as pandas DataFrames or NumPy arrays. For example, you can read a Unity Catalog table into a Spark DataFrame and call `.toPandas()` for use with scikit-learn, PyTorch, or TensorFlow. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]
- **Local file APIs** – Unity Catalog also supports access via standard local file–system APIs (e.g., Python’s `open()` or `pathlib`), which is critical for distributed deep learning frameworks that expect file paths for data loading and model checkpointing. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Role in Shared Storage

Distributed deep learning (especially for [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)) requires shared storage so that all processes can read the same dataset and write checkpoints. Unity Catalog volumes or managed storage locations provide that shared namespace while enforcing governance policies. The source material notes that shared storage is “particularly important for distributed deep learning” and that Databricks provides Unity Catalog “for accessing data on a cluster using both Spark and local file APIs.” ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Common Workflows

1. **Load tabular data from a Unity Catalog table** – Use Spark SQL or DataFrame APIs to read a table, then convert to pandas for ML framework consumption.
2. **Prepare data for Hugging Face fine-tuning** – Load data from Unity Catalog tables and transform it using Hugging Face Transformers and Hugging Face Datasets.
3. **Distributed deep learning data loading** – Use PyTorch `IterableDataset`, streaming from Hugging Face Datasets, or Ray Data, all of which can read from Unity Catalog volumes via local file APIs.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The overarching data and AI governance platform.
- Data Governance – Access control, lineage, and discovery provided by Unity Catalog.
- [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md) – The primary API for reading Unity Catalog tables in Python.
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) – Workloads that depend on Unity Catalog’s shared storage and local file APIs.
- Model Checkpointing – Saving training state to Unity Catalog–managed storage.
- Hugging Face Datasets – A library that can stream data from Unity Catalog volumes.

## Sources

- load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md

# Citations

1. [load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md](/references/load-data-for-machine-learning-and-deep-learning-databricks-on-aws-dfd2be96.md)
