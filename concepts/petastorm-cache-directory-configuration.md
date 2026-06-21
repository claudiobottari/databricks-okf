---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5efa7d981451a53e6e0047fc1ecea6d5d86318ba3f19069ade9eef1312b58748
  pageDirectory: concepts
  sources:
    - load-data-using-petastorm-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - petastorm-cache-directory-configuration
    - PCDC
  citations:
    - file: load-data-using-petastorm-databricks-on-aws.md
title: Petastorm Cache Directory Configuration
description: The mechanism to specify where Petastorm caches converted Spark DataFrames in Parquet format, configurable via Spark config or notebook, requiring a DBFS path starting with file:///dbfs/.
tags:
  - configuration
  - spark
  - storage
  - caching
timestamp: "2026-06-19T19:15:27.722Z"
---

# Petastorm Cache Directory Configuration

**Petastorm Cache Directory Configuration** refers to the setup of a storage location used by the Petastorm Spark converter to cache Spark DataFrames in Parquet format during conversion to TensorFlow or PyTorch datasets. Proper configuration of this cache directory is essential for efficient data loading in deep learning workflows.^[load-data-using-petastorm-databricks-on-aws.md]

## Overview

The Petastorm Spark converter caches the input [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) in Parquet format in a user-specified cache directory location. This cache directory must be a DBFS path starting with `file:///dbfs/`, for example, `file:///dbfs/tmp/foo/`, which refers to the same location as `dbfs:/tmp/foo/`.^[load-data-using-petastorm-databricks-on-aws.md]

## Configuration Methods

You can configure the cache directory in two ways:^[load-data-using-petastorm-databricks-on-aws.md]

### Spark Config

Add the following line to the cluster Spark configuration:

```
petastorm.spark.converter.parentCacheDirUrl file:///dbfs/...
```

### Notebook Configuration

In your notebook, call `spark.conf.set()`:

```python
from petastorm.spark import SparkDatasetConverter, make_spark_converter

spark.conf.set(SparkDatasetConverter.PARENT_CACHE_DIR_URL_CONF, 'file:///dbfs/...')
```

## Cache Management

After using the cache, you have two options for management:^[load-data-using-petastorm-databricks-on-aws.md]

- **Explicit deletion**: Call `converter.delete()` to remove the cache programmatically.
- **Implicit management**: Configure lifecycle rules in your object storage to automatically manage cache expiration.

## Related Concepts

- [Petastorm](/concepts/petastorm.md) — The open source data access library for deep learning frameworks
- [Spark Dataset Converter API](/concepts/spark-dataset-converter-api.md) — The Petastorm API for converting Spark DataFrames
- Parquet Format — The storage format used by the Petastorm converter
- [Mosaic Streaming](/concepts/mosaic-streaming.md) — The recommended replacement for loading large datasets from cloud storage
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Training scenarios that use Petastorm for data loading

## Sources

- load-data-using-petastorm-databricks-on-aws.md

# Citations

1. [load-data-using-petastorm-databricks-on-aws.md](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
