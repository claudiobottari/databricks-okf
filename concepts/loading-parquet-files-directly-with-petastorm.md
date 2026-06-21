---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb3052945472af160c1fa44bf750dc0c70fea20162d6d15c1eea7c462b226e99
  pageDirectory: concepts
  sources:
    - load-data-using-petastorm-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loading-parquet-files-directly-with-petastorm
    - LPFDWP
  citations:
    - file: load-data-using-petastorm-databricks-on-aws.md
    - file: load-data-using-petastorm-databricks-on-aws.md
      start: 7
      end: 9
    - file: load-data-using-petastorm-databricks-on-aws.md
      start: 11
      end: 14
    - file: 37-38
    - file: load-data-using-petastorm-databricks-on-aws.md
      start: 38
      end: 41
    - file: load-data-using-petastorm-databricks-on-aws.md
      start: 25
      end: 34
    - file: 38-41
    - file: load-data-using-petastorm-databricks-on-aws.md
      start: 45
      end: 51
title: Loading Parquet Files Directly with Petastorm
description: The alternative (less preferred) workflow for using Petastorm by saving data in Parquet format to DBFS and loading it via the DBFS mount point, bypassing the Spark Converter API.
tags:
  - data-loading
  - parquet
  - dbfs
  - deep-learning
timestamp: "2026-06-19T19:14:42.533Z"
---

# Loading Parquet Files Directly with Petastorm

**Loading Parquet Files Directly with Petastorm** is a method for feeding data from Apache Parquet files into deep learning frameworks such as TensorFlow or PyTorch using the Petastorm library. This approach bypasses the Spark DataFrame conversion pipeline by reading pre‑saved Parquet files directly through a DBFS mount point. ^[load-data-using-petastorm-databricks-on-aws.md]

> **Note:** The `petastorm` package is deprecated. [Mosaic Streaming](https://docs.databricks.com/aws/en/machine-learning/load-data/streaming) is the recommended replacement for loading large datasets from cloud storage. ^[load-data-using-petastorm-databricks-on-aws.md:7-9]

## Overview

Petastorm is an open‑source data access library that enables single‑node or distributed training and evaluation of deep learning models directly from datasets in Apache Parquet format or from datasets already loaded as [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md)s. It supports TensorFlow, PyTorch, and PySpark. The direct‑loading method described here is **less preferred** than the Petastorm Spark Dataset Converter API. ^[load-data-using-petastorm-databricks-on-aws.md:11-14, 37-38]

## Workflow

The recommended workflow for loading Parquet files directly with Petastorm consists of four steps:

1. **Use Apache Spark** to load and optionally preprocess the data.
2. **Save the data in Parquet format** into a DBFS path that has a companion DBFS mount (e.g., `dbfs:/ml`).
3. **Load the data in Petastorm format** via the DBFS mount point (e.g., `file:/dbfs/ml`).
4. **Feed the data into a deep learning framework** for training or inference. ^[load-data-using-petastorm-databricks-on-aws.md:38-41]

This method avoids the overhead of materializing a Spark DataFrame each time the data is needed, but it requires that the Parquet files are already saved and accessible via the FUSE mount. ^[load-data-using-petastorm-databricks-on-aws.md:38-41]

## Cache Directory Considerations

The Petastorm Spark converter (the preferred API) caches the input DataFrame in Parquet format. That cache directory can be configured as a DBFS path starting with `file:///dbfs/` (e.g., `file:///dbfs/tmp/foo/`). Configuration can be done in the Spark Config or by calling `spark.conf.set()`. After using the converter, the cache can be deleted explicitly with `converter.delete()`, or lifecycle rules can be set in object storage. ^[load-data-using-petastorm-databricks-on-aws.md:25-34]

This cache setup is **not required** for the direct Parquet loading method, because the data is already saved in Parquet format on DBFS. ^[load-data-using-petastorm-databricks-on-aws.md:25-34, 38-41]

## Example Notebook

Databricks provides an end‑to‑end example notebook titled **“Use Spark and Petastorm to prepare data for deep learning”** (referenced in the documentation). This notebook demonstrates the direct‑loading workflow:

- Load and preprocess data with Spark.
- Save data as Parquet under `dbfs:/ml`.
- Load data with Petastorm via the FUSE mount `file:/dbfs/ml`.
- Feed the data into a deep learning framework for training or inference. ^[load-data-using-petastorm-databricks-on-aws.md:45-51]

## Related Concepts

- [Petastorm](/concepts/petastorm.md) – The open‑source library used for direct Parquet loading.
- Apache Parquet – The columnar storage format that Petastorm reads natively.
- DBFS – The Databricks Filesystem where Parquet files are saved and mounted.
- [Mosaic Streaming](/concepts/mosaic-streaming.md) – The recommended replacement for Petastorm for large datasets.
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) – The source format in the recommended preprocessing step.
- TensorFlow and PyTorch – Deep learning frameworks that consume Petastorm datasets.
- Deep Learning – The training/inference use case for Petastorm.

## Sources

- load-data-using-petastorm-databricks-on-aws.md

# Citations

1. [load-data-using-petastorm-databricks-on-aws.md](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
2. [load-data-using-petastorm-databricks-on-aws.md:7-9](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
3. [load-data-using-petastorm-databricks-on-aws.md:11-14](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
4. 37-38
5. [load-data-using-petastorm-databricks-on-aws.md:38-41](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
6. [load-data-using-petastorm-databricks-on-aws.md:25-34](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
7. 38-41
8. [load-data-using-petastorm-databricks-on-aws.md:45-51](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
