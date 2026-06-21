---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca6150b1d064b49d7f08e28b2c000bd24ef9db868a3a57958f34bf33ac91e4ee
  pageDirectory: concepts
  sources:
    - load-data-using-mosaic-streaming-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-mosaic-streaming-integration
    - DRMMSI
  citations:
    - file: load-data-using-mosaic-streaming-databricks-on-aws.md
title: Databricks Runtime ML Mosaic Streaming Integration
description: Mosaic Streaming is pre-installed in Databricks Runtime 15.2 ML and higher; authentication for Unity Catalog volumes requires setting DATABRICKS_HOST and DATABRICKS_TOKEN environment variables, especially for distributed training with TorchDistributor.
tags:
  - databricks
  - configuration
  - authentication
timestamp: "2026-06-19T19:14:21.286Z"
---

# Databricks Runtime ML Mosaic Streaming Integration

**Databricks Runtime ML Mosaic Streaming Integration** refers to the built-in support and recommended workflow for using the [Mosaic Streaming](https://docs.mosaicml.com/projects/streaming/en/stable/index.html) open source data loading library within Databricks Runtime ML clusters. Mosaic Streaming converts data from Apache Spark DataFrames into the Mosaic Data Shard (MDS) format, which is optimized for single-node or distributed training and evaluation of deep learning models with PyTorch. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Overview

Mosaic Streaming is pre‑installed in all versions of **Databricks Runtime 15.2 ML** and higher. It integrates with Mosaic Composer, native PyTorch, PyTorch Lightning, and the TorchDistributor. The library provides several advantages over traditional PyTorch DataLoaders:

- Compatibility with any data type, including images, text, video, and multimodal data.
- Support for major cloud storage providers (AWS, OCI, GCS, Azure, Databricks UC Volume, and any S3‑compatible object store).
- Maximized correctness guarantees, performance, flexibility, and ease of use. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Workflow: Spark DataFrame to PyTorch

The recommended workflow consists of four steps:

1. **Load and preprocess data** using Apache Spark.
2. **Convert the DataFrame to MDS format** using `streaming.base.converters.dataframe_to_mds`. The resulting data can be saved to disk for transient storage or to a [Unity Catalog](/concepts/unity-catalog.md) volume for persistent storage. Advanced use cases can include preprocessing via UDFs. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]
3. **Load data into memory** with `streaming.StreamingDataset`. This is a version of PyTorch’s `IterableDataset` that features elastically deterministic shuffling, enabling fast mid‑epoch resumption. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]
4. **Load data for training/evaluation/testing** using `streaming.StreamingDataLoader`. This wrapper around PyTorch’s `DataLoader` adds a checkpoint/resumption interface that tracks the number of samples seen per rank. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

For an end‑to‑end example, the documentation references a notebook titled *Simplify data loading from Spark to PyTorch using Mosaic Streaming*. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Troubleshooting

### Authentication Error

When loading data from a Unity Catalog volume with `StreamingDataset`, you may encounter the following error:

```
ValueError: default auth: cannot configure default credentials, please check https://docs.databricks.com/en/dev-tools/auth.html#databricks-client-unified-authentication to configure credentials for your preferred authentication method.
```

To resolve this, set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` before calling `StreamingDataset`. In distributed training with `TorchDistributor`, these variables must be set on worker nodes as well. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

### Python 3.11 Shared Memory Issues

Due to issues with Python 3.11’s shared memory implementation, `StreamingDataset` can encounter transient problems on Databricks Runtime **15.4 LTS ML**. These issues are avoided by upgrading to **Databricks Runtime 16.4 LTS ML**, which uses Python 3.12. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Related Concepts

- Apache Spark – The data processing framework used in the first step of the workflow.
- PyTorch – The deep learning framework that consumes the MDS format via `StreamingDataset`.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) for persisting MDS‑formatted data.
- [TorchDistributor](/concepts/torchdistributor.md) – Databricks’ API for distributed PyTorch training.
- Mosaic Composer – The primary training library supported by Mosaic Streaming.

## Sources

- load-data-using-mosaic-streaming-databricks-on-aws.md

# Citations

1. [load-data-using-mosaic-streaming-databricks-on-aws.md](/references/load-data-using-mosaic-streaming-databricks-on-aws-4083e8c0.md)
