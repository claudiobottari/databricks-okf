---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: deeb68b71f3afed5472106064151a2a3548dbae4a3692152d43fb1734304ba24
  pageDirectory: concepts
  sources:
    - load-data-using-mosaic-streaming-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mds-mosaic-data-shard-format
    - M(DSF
    - Mosaic Data Shard (MDS) format
    - Mosaic Data Shard (MDS)
  citations:
    - file: load-data-using-mosaic-streaming-databricks-on-aws.md
title: MDS (Mosaic Data Shard) Format
description: A storage format produced by converting Apache Spark DataFrames using Mosaic Streaming, optimized for distributed deep learning training with support for compression and hashing.
tags:
  - data-format
  - deep-learning
  - spark
timestamp: "2026-06-19T19:14:03.837Z"
---

# MDS (Mosaic Data Shard) Format

The **MDS (Mosaic Data Shard) Format** is a data storage format developed for the [Mosaic Streaming](/concepts/mosaic-streaming.md) library that converts data from Apache Spark DataFrames into a format compatible with PyTorch for deep learning training and evaluation. It serves as an intermediate format that bridges the gap between large-scale data processing with Spark and high-performance model training with PyTorch. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Overview

MDS files are created by converting Spark DataFrames using the `streaming.base.converters.dataframe_to_mds` function. This format is designed for efficient storage and retrieval in distributed training environments. Data can be saved to disk for transient storage or to a Unity Catalog volume for persistent storage. The MDS format supports optional optimizations including compression and hashing. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

The MDS format is compatible with any data type, including images, text, video, and multimodal data. It also supports major cloud storage providers such as AWS, OCI, GCS, Azure, Databricks UC Volume, and any S3-compatible object store. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Workflow

The recommended workflow for using the MDS format involves four steps:

1. **Load and preprocess data** using Apache Spark.
2. **Convert to MDS format** using `streaming.base.converters.dataframe_to_mds` to save data to disk or a Unity Catalog volume. For advanced use cases, data can be preprocessed using UDFs before conversion.
3. **Load data into memory** using `streaming.StreamingDataset`, a version of PyTorch's IterableDataset that features elastically deterministic shuffling for fast mid-epoch resumption.
4. **Prepare for training** using `streaming.StreamingDataLoader`, which extends PyTorch's DataLoader with additional checkpoint and resumption interfaces that track the number of samples seen by each rank.

^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Integration with Training Frameworks

Mosaic Streaming and the MDS format primarily support Mosaic Composer, but also integrate with native PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), and the [TorchDistributor](/concepts/torchdistributor.md). The format enables both single-node and distributed training of deep learning models. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Availability

Mosaic Streaming (and by extension the MDS format) is pre-installed in all versions of Databricks Runtime 15.2 ML and higher. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Benefits

The MDS format and Mosaic Streaming provide several advantages over traditional PyTorch DataLoaders:
- Compatibility with any data type (images, text, video, multimodal)
- Support for major cloud storage providers
- Maximized correctness guarantees, performance, flexibility, and ease of use

^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Related Concepts

- [Mosaic Streaming](/concepts/mosaic-streaming.md) — The open-source data loading library that uses the MDS format
- Mosaic Composer — Primary training framework supported by Mosaic Streaming
- [TorchDistributor](/concepts/torchdistributor.md) — Distributed training utility compatible with MDS format
- [Unity Catalog](/concepts/unity-catalog.md) — Persistent storage option for MDS files
- Apache Spark — The data processing framework used before conversion to MDS

## Sources

- load-data-using-mosaic-streaming-databricks-on-aws.md

# Citations

1. [load-data-using-mosaic-streaming-databricks-on-aws.md](/references/load-data-using-mosaic-streaming-databricks-on-aws-4083e8c0.md)
