---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 888208e3970983588c265e4cf9c3838f7a585fb1d1276bf79c8e3e1078dbcbdb
  pageDirectory: concepts
  sources:
    - reference-solution-for-image-applications-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - image-etl-pipeline-pattern
    - IEPP
  citations:
    - file: reference-solution-for-image-applications-databricks-on-aws.md
title: Image ETL Pipeline Pattern
description: "A two-stage reference pipeline for image applications: first ETL images into a Delta table using Auto Loader, then perform distributed inference using pandas UDFs with DL models."
tags:
  - pipeline
  - etl
  - machine-learning
  - architecture
timestamp: "2026-06-19T20:12:49.118Z"
---

# Image ETL Pipeline Pattern

The **Image ETL Pipeline Pattern** is a reference architecture for performing distributed image model inference on large-scale image datasets stored in an object store. It addresses the I/O‑heavy and compute‑heavy nature of loading many images and applying deep learning (DL) models by leveraging two core stages: extracting, transforming, and loading (ETL) images into a [Delta table](/concepts/delta-lake-table.md) using Auto Loader, and then running distributed inference via pandas UDFs. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Stage 1: ETL Images into a Delta Table Using Auto Loader

Databricks recommends using Auto Loader to ingest images from cloud object storage into a Delta table. Auto Loader incrementally processes new files as they arrive, handling continuous ingestion of newly uploaded images. This stage creates a managed Delta table that stores the raw image data or metadata, enabling subsequent processing steps to efficiently reference the images without repeatedly scanning object storage. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Stage 2: Distributed Inference Using pandas UDF

After the images are loaded into a Delta table, inference is performed in a distributed fashion using pandas UDFs. The reference solution provides notebooks that demonstrate this approach with two popular DL frameworks:

- **PyTorch** – Distributed inference via PyTorch and pandas UDF
- **TensorFlow (tf.Keras)** – Distributed inference via Keras and pandas UDF

Because the inference workload is embarrassingly parallel, distributing it across the workers of a Spark cluster achieves high throughput. The pandas UDF loads the model on each worker, processes batches of images, and returns predictions. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Limitations: Image File Sizes

For large image files—where the average image size exceeds 100 MB—Databricks recommends using the Delta table only to manage **metadata** (e.g., a list of file names). The images themselves should be loaded directly from the object store using their stored paths when needed, rather than being embedded in the Delta table. This avoids excessive I/O overhead and storage costs. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Related Concepts

- Auto Loader – Incremental ingestion engine for cloud object storage.
- [Delta table](/concepts/delta-lake-table.md) – Storage layer for managing image data and metadata.
- pandas UDF – Mechanism for distributed user‑defined functions on Spark.
- Distributed inference – Scaling model predictions across a cluster.
- Transfer learning with image models – Common downstream use case.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – Alternative deployment pattern for inference.

## Sources

- reference-solution-for-image-applications-databricks-on-aws.md

# Citations

1. [reference-solution-for-image-applications-databricks-on-aws.md](/references/reference-solution-for-image-applications-databricks-on-aws-890cf1b8.md)
