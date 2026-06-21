---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 989330b14c5f5982af2fa159444949c0d0028032d51602e19d40145376812780
  pageDirectory: concepts
  sources:
    - load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-dataframe-to-ml-format-conversion
    - SDTMFC
  citations:
    - file: load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
title: Spark DataFrame to ML Format Conversion
description: Converting Apache Spark DataFrames into pandas DataFrames using toPandas() and optionally to NumPy format using to_numpy() for ML pipelines.
tags:
  - databricks
  - pyspark
  - data-conversion
  - pandas
timestamp: "2026-06-19T19:13:33.267Z"
---

# Spark DataFrame to ML Format Conversion

**Spark DataFrame to ML Format Conversion** refers to the process of transforming Apache Spark DataFrames into formats suitable for machine learning and deep learning workflows. This conversion is a critical step in ML pipeline development, bridging Spark's distributed data processing capabilities with popular ML frameworks such as PyTorch, TensorFlow, scikit-learn, and [Hugging Face](/concepts/hugging-face-trainer.md).

## Overview

Machine learning applications on [Databricks on AWS](/concepts/databricks-on-aws.md) often need to convert [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md) into formats compatible with ML libraries. While Spark DataFrames provide efficient distributed data handling, ML frameworks typically expect data in NumPy arrays, [pandas DataFrames](/concepts/pandas-dataframe-scoring-format.md), or framework-specific tensor objects. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Common Conversion Pathways

### Spark DataFrame to pandas DataFrame

The primary method for converting Spark DataFrames to ML-compatible formats is using the PySpark `toPandas()` method. This converts a Spark DataFrame into a pandas DataFrame, which can then be passed to ML libraries:

```python
pandas_df = spark_df.toPandas()
```

^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

### pandas DataFrame to NumPy Array

After conversion to pandas, you can further convert to NumPy format using the `to_numpy()` method. NumPy arrays are the standard input format for many ML libraries:

```python
numpy_array = pandas_df.to_numpy()
```

^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Supported ML Frameworks

### PyTorch

PyTorch integrates with [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md) through [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) and [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) training workflows. The PyTorch IterableDataset is recommended for large datasets that do not fit in memory. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

### Hugging Face

Hugging Face Transformers and Hugging Face Datasets support streaming for datasets hosted on the Hub or in [Unity Catalog](/concepts/unity-catalog.md) volumes. Use the Hugging Face Datasets streaming API for distributed data preparation. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

### Ray Data

Ray Data provides distributed batch data processing for converting Spark DataFrames into Ray datasets suitable for distributed training. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Storage and Checkpointing

Machine learning applications may need shared storage for data loading and [model checkpointing](/concepts/ai-runtime-model-checkpointing.md). Databricks provides [Unity Catalog](/concepts/unity-catalog.md) for accessing data using both Spark and local file APIs, supporting seamless conversion between formats. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Related Concepts

- [Apache Spark DataFrame](/concepts/apache-spark-dataframes-to-tfrecord-conversion.md)
- pandas DataFrame
- NumPy array
- PyTorch Tensor
- TensorFlow Dataset
- ML pipeline
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- [Data loading](/concepts/ai-runtime-data-loading.md)
- Model checkpointing

## Sources

- load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md

# Citations

1. [load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md](/references/load-data-for-machine-learning-and-deep-learning-databricks-on-aws-dfd2be96.md)
