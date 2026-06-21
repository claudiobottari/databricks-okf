---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4fd0e8c479f181dd32831dac54a2bc31e792750b1e47ce336c4de10e84a4d28b
  pageDirectory: concepts
  sources:
    - load-data-using-mosaic-streaming-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-dataframe-to-mds-conversion-workflow
    - SDTMCW
  citations:
    - file: load-data-using-mosaic-streaming-databricks-on-aws.md
title: Spark DataFrame to MDS Conversion Workflow
description: "A recommended four-step workflow: load/preprocess data with Spark, convert to MDS format via dataframe_to_mds, load with StreamingDataset, and serve with StreamingDataLoader."
tags:
  - workflow
  - spark
  - data-pipeline
  - deep-learning
timestamp: "2026-06-19T19:14:54.226Z"
---

# Spark DataFrame to MDS Conversion Workflow

The **Spark DataFrame to MDS Conversion Workflow** is a process for converting data from Apache Spark DataFrames into the Mosaic Data Shard (MDS) format using the open source [Mosaic Streaming](/concepts/mosaic-streaming.md) library. This workflow enables the use of Spark for data loading and preprocessing, then moves the data into a format optimized for PyTorch-based deep learning training and evaluation. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Overview

Mosaic Streaming is an open source data loading library that supports single-node or distributed training and evaluation of deep learning models. It integrates with Mosaic Composer, native PyTorch, [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), and the [TorchDistributor](/concepts/torchdistributor.md). The library provides advantages over traditional PyTorch DataLoaders, including compatibility with any data type (images, text, video, multimodal data), support for major cloud storage providers, and maximized correctness guarantees, performance, flexibility, and ease of use. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

Mosaic Streaming is pre-installed in all versions of Databricks Runtime 15.2 ML and higher. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Workflow Steps

The recommended workflow for converting Spark DataFrames to the MDS format consists of four steps:

### 1. Load and Preprocess Data with Apache Spark

Use Apache Spark to load raw data and perform any necessary preprocessing operations. This step leverages Spark's distributed processing capabilities for large-scale data transformation. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

### 2. Convert to MDS Format

Use the function `streaming.base.converters.dataframe_to_mds` to save the DataFrame to disk in MDS format. The data can be stored in transient storage or persisted to a Unity Catalog Volume for long-term use. The MDS format supports compression and optional hashing for optimization. Advanced use cases can also include data preprocessing using user-defined functions (UDFs). ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

### 3. Load Data with StreamingDataset

Use `streaming.StreamingDataset` to load the MDS-formatted data into memory. `StreamingDataset` is a version of PyTorch's `IterableDataset` that features elastically deterministic shuffling, enabling fast mid-epoch resumption during training. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

### 4. Create DataLoader

Use `streaming.StreamingDataLoader` to load data for training, evaluation, or testing. `StreamingDataLoader` is a version of PyTorch's `DataLoader` that provides an additional checkpoint and resumption interface, tracking the number of samples seen by the model on each rank. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Benefits

The Spark DataFrame to MDS workflow enables seamless transition from Apache Spark's data processing capabilities to PyTorch's deep learning training loop. This eliminates the need for custom data format converters and provides a standardized pipeline for preparing large-scale training datasets. The MDS format's support for cloud storage providers makes the workflow suitable for cloud-native ML pipelines. ^[load-data-using-mosaic-streaming-databricks-on-aws.md]

## Related Concepts

- [Mosaic Streaming](/concepts/mosaic-streaming.md)
- Mosaic Composer
- PyTorch DataLoader
- [TorchDistributor](/concepts/torchdistributor.md)
- Unity Catalog Volume
- Apache Spark DataFrames

## Sources

- load-data-using-mosaic-streaming-databricks-on-aws.md

# Citations

1. [load-data-using-mosaic-streaming-databricks-on-aws.md](/references/load-data-using-mosaic-streaming-databricks-on-aws-4083e8c0.md)
