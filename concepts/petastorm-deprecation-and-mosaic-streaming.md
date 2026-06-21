---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91d0e72fc6dda7aa82cb628ba7c0fc207d4e8dd83ab430bde73cfb542310ea16
  pageDirectory: concepts
  sources:
    - load-data-using-petastorm-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - petastorm-deprecation-and-mosaic-streaming
    - Mosaic Streaming and Petastorm Deprecation
    - PDAMS
  citations:
    - file: load-data-using-petastorm-databricks-on-aws.md
title: Petastorm Deprecation and Mosaic Streaming
description: The petastorm package is deprecated on Databricks, with Mosaic Streaming recommended as the replacement for loading large datasets from cloud storage.
tags:
  - deprecation
  - mosaic-streaming
  - databricks
  - migration
timestamp: "2026-06-19T19:14:57.071Z"
---

# Petastorm Deprecation and Mosaic Streaming

**Petastorm Deprecation and Mosaic Streaming** refers to the platform decision on Databricks to supersede the Petastorm data-access library with Mosaic Streaming as the recommended method for loading large datasets from cloud storage for deep learning training and inference.

## Overview

Petastorm is an open source data access library that enables single-node or distributed training and evaluation of deep learning models directly from datasets stored in Apache Parquet format or from Apache Spark DataFrames. It supported popular machine learning frameworks such as TensorFlow, PyTorch, and PySpark. The library provided a Spark converter API (`make_spark_converter`) to materialise a Spark DataFrame into Parquet and then create a `tf.data.Dataset` or `torch.utils.data.DataLoader`, as well as the ability to read Parquet files directly from DBFS paths. ^[load-data-using-petastorm-databricks-on-aws.md]

## Deprecation and Replacement

The `petastorm` package is now deprecated on the Databricks platform. Users are advised to adopt [Mosaic Streaming](/concepts/mosaic-streaming.md) as the replacement for loading large datasets from cloud storage. Mosaic Streaming is designed to handle large-scale data loading for deep learning workloads and is actively maintained by Databricks. ^[load-data-using-petastorm-databricks-on-aws.md]

## Migration Considerations

Users currently relying on Petastorm should plan to migrate their data-loading pipelines. The Petastorm documentation still exists for reference but will not receive feature updates. Key points for migration include:

- Petastorm cached Spark DataFrames to a Parquet cache directory (e.g., `file:///dbfs/...`), which could be managed via Spark config or lifecycle rules. ^[load-data-using-petastorm-databricks-on-aws.md]
- Petastorm’s Spark converter API and direct Parquet reader are no longer the recommended approach.
- Mosaic Streaming provides an alternative that integrates with the same deep learning frameworks and offers improved performance and scalability for cloud storage.

No specific migration guide is provided in the source material; refer to the [Mosaic Streaming](/concepts/mosaic-streaming.md) documentation for details.

## Related Concepts

- [Mosaic Streaming](/concepts/mosaic-streaming.md)
- [Petastorm](/concepts/petastorm.md)
- Apache Spark
- TensorFlow
- PyTorch
- Apache Parquet
- DBFS
- [Deep Learning Training](/concepts/deep-learning-on-databricks.md)

## Sources

- load-data-using-petastorm-databricks-on-aws.md

# Citations

1. [load-data-using-petastorm-databricks-on-aws.md](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
