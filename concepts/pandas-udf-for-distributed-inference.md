---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dfb6e429a95046382d03d0796a2780ab3e9236d2bc1ff6cee813c03728e698b4
  pageDirectory: concepts
  sources:
    - reference-solution-for-image-applications-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-udf-for-distributed-inference
    - PUFDI
  citations:
    - file: reference-solution-for-image-applications-databricks-on-aws.md
title: pandas UDF for Distributed Inference
description: Using pandas User-Defined Functions (UDFs) in PySpark to parallelize deep learning model inference across a Spark cluster, treating inference as an embarrassingly parallel workload.
tags:
  - pyspark
  - distributed-computing
  - machine-learning
  - udf
timestamp: "2026-06-19T20:12:50.991Z"
---

# pandas UDF for Distributed Inference

**pandas UDF for Distributed Inference** is a technique for applying trained deep learning models to large datasets in a distributed, embarrassingly parallel fashion on Databricks. By wrapping model inference logic inside a pandas UDF (also known as Vectorized UDF), users can scale inference workloads across cluster nodes without manual parallelism management. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Overview

Distributed inference using pandas UDFs is particularly suited for image classification and object detection applications. For example, you might apply a model like MobileNetV2 to detect human objects in user-uploaded photos for privacy protection. The inference workload is embarrassingly parallel, making it an ideal candidate for distribution across a Spark cluster. ^[reference-solution-for-image-applications-databricks-on-aws.md]

The typical workflow consists of two main stages:

1. ETL images into a Delta table using Auto Loader
2. Perform distributed inference using pandas UDF ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Workflow Stages

### Stage 1: ETL Images into Delta Table

For image applications, Databricks recommends extracting images from object storage and loading them into a [Delta table](/concepts/delta-lake-table.md) using Auto Loader. This approach simplifies data management and automatically handles continuously arriving new images. ^[reference-solution-for-image-applications-databricks-on-aws.md]

### Stage 2: Distributed Inference via pandas UDF

After images are stored in a Delta table, a pandas UDF wraps the model inference logic. This UDF can be applied to the DataFrame containing image paths or binary data, and Spark distributes the function execution across worker nodes. The technique is demonstrated in reference notebooks for both PyTorch and TensorFlow (tf.Keras) frameworks. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Limitations: Image File Sizes

For large image files (average file size greater than 100 MB), Databricks recommends using the Delta table only to manage metadata (the list of file names) rather than storing the binary image data directly. In this approach, images are loaded from the object store using their paths when needed. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Related Concepts

- Auto Loader — Incremental ingestion tool for continuously arriving data
- [Delta table](/concepts/delta-lake-table.md) — Storage layer for managing image metadata and paths
- Distributed Inference — General approach to scaling model predictions
- Vectorized UDF — Apache Spark's mechanism for applying Python functions to DataFrames
- Embarrassingly Parallel Workloads — Parallelism pattern where no communication is needed between tasks
- [Model Inference Pipeline](/concepts/batch-inference-pipelines.md) — End-to-end workflow for applying trained models to new data
- Image Classification — Common use case for distributed inference with pandas UDFs

## Sources

- reference-solution-for-image-applications-databricks-on-aws.md

# Citations

1. [reference-solution-for-image-applications-databricks-on-aws.md](/references/reference-solution-for-image-applications-databricks-on-aws-890cf1b8.md)
