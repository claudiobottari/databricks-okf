---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c7665bba9331b132c65afb16a731d23cbce30ac88a49dd9ba4df29f0fa8bbb3
  pageDirectory: concepts
  sources:
    - reference-solution-for-image-applications-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-image-inference-on-databricks
    - DIIOD
    - Image model inference on Databricks
  citations:
    - file: reference-solution-for-image-applications-databricks-on-aws.md
title: Distributed Image Inference on Databricks
description: Architecture and workflow for scaling deep learning model inference across large image collections using Spark, pandas UDFs, and DL frameworks like PyTorch and TensorFlow on Databricks.
tags:
  - machine-learning
  - distributed-computing
  - databricks
  - deep-learning
timestamp: "2026-06-19T20:12:44.224Z"
---

# Distributed Image Inference on Databricks

**Distributed Image Inference on Databricks** refers to the practice of applying pre-trained deep learning models—such as image classifiers and object detectors—to large collections of images stored in an object store, using the distributed computing capabilities of Databricks. The reference solution combines Auto Loader for ingestion with pandas UDF for parallel inference, and supports both PyTorch and TensorFlow frameworks. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Overview

Many real-world image applications require running trained Deep Learning models—for example, MobileNetV2 for detecting human objects in user-uploaded photos—against a large, continuously growing image dataset. The inference workload is embarrassingly parallel and can be distributed easily. However, loading many images and applying the models is both I/O-heavy and compute-heavy. The recommended solution on Databricks addresses these challenges through a two-stage pipeline. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Workflow

The pipeline consists of two major stages:

### 1. ETL Images into a Delta Table Using Auto Loader

Databricks recommends ingesting images into a [Delta table](/concepts/delta-lake-table.md) using Auto Loader. This approach helps with data management and automatically handles continuously arriving new images. A dedicated notebook demonstrates how to ETL image datasets into a Delta table. ^[reference-solution-for-image-applications-databricks-on-aws.md]

### 2. Perform Distributed Inference Using pandas UDF

Once images are stored in a Delta table, distributed inference is performed using pandas UDFs (user-defined functions) that apply the deep learning model to batches of images. The reference solution provides example notebooks for both PyTorch and TensorFlow/Keras. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Implementation

Two reference notebooks are available:
- **Distributed inference via PyTorch and pandas UDF** – uses PyTorch for model inference.
- **Distributed inference via Keras and pandas UDF** – uses TensorFlow tf.Keras for model inference.

These notebooks illustrate the common configuration used by many image applications: images stored in an object store, ingested via Auto Loader, and processed in parallel across a Databricks cluster. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Limitations: Image File Sizes

For large image files where the average file size exceeds 100 MB, Databricks recommends using the Delta table **only to manage metadata** (i.e., a list of file names and paths). The actual image data should be loaded directly from the object store using the file paths when needed. This avoids storing large binary data in Delta table columns, which can degrade performance. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Related Concepts

- Auto Loader – Ingestion tool for continuously arriving files.
- [Delta table](/concepts/delta-lake-table.md) – Apache Spark-based table format used for storing image metadata and inference results.
- pandas UDF – Distributed user-defined function for applying PyTorch/TensorFlow models.
- PyTorch / TensorFlow – Deep learning frameworks used in the reference notebooks.
- Object Store – Storage layer (e.g., AWS S3) where images reside.
- Image Classification / Object Detection – Typical inference tasks.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Complementary stage for retraining models.

## Sources

- reference-solution-for-image-applications-databricks-on-aws.md

# Citations

1. [reference-solution-for-image-applications-databricks-on-aws.md](/references/reference-solution-for-image-applications-databricks-on-aws-890cf1b8.md)
