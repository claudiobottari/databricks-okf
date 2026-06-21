---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6908bd27c8977769625fcf62a5580134bb5bc70cb4c4e5a1674e21c11657ea47
  pageDirectory: concepts
  sources:
    - reference-solution-for-image-applications-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-loader-for-image-ingestion
    - ALFII
  citations:
    - file: reference-solution-for-image-applications-databricks-on-aws.md
title: Auto Loader for Image Ingestion
description: Using Databricks Auto Loader to incrementally ingest large volumes of images from cloud object storage into Delta tables, handling continuously arriving new files.
tags:
  - data-ingestion
  - databricks
  - automation
  - etl
timestamp: "2026-06-19T20:12:38.438Z"
---

## Auto Loader for Image Ingestion

**Auto Loader for Image Ingestion** refers to the use of Auto Loader, a Databricks incremental ingestion feature, to load image data from cloud object storage into a [Delta table](/concepts/delta-lake-table.md) as part of a machine learning pipeline. This approach is recommended for image applications that require both batch and continuously arriving new images. ^[reference-solution-for-image-applications-databricks-on-aws.md]

### Overview

In typical image-model inference workflows, images are stored in an object store and must be loaded efficiently for distributed processing. Databricks recommends using Auto Loader to perform the ETL (extract, transform, load) step that ingests images into a Delta table. This table then serves as the source for downstream tasks such as distributed inference using pandas UDFs. ^[reference-solution-for-image-applications-databricks-on-aws.md]

### Key Benefits

- **Data management**: Auto Loader automatically tracks which files have already been ingested, reducing manual bookkeeping and ensuring idempotent processing. ^[reference-solution-for-image-applications-databricks-on-aws.md]
- **Continuous ingestion**: New images that arrive in the object store are automatically detected and processed, enabling streaming or periodic refresh of the Delta table. ^[reference-solution-for-image-applications-databricks-on-aws.md]

### Workflow Role

The Auto Loader–based ingestion stage is the first of two major stages in the reference solution:

1. **ETL images into a Delta table using Auto Loader** – Ingests raw image files (e.g., from cloud storage) into a structured Delta table, preserving metadata such as file paths.
2. **Perform distributed inference using pandas UDF** – Applies trained deep‑learning models (e.g., PyTorch, TensorFlow) to the images loaded from the Delta table. ^[reference-solution-for-image-applications-databricks-on-aws.md]

### Limitations

For large image files (average file size greater than 100 MB), Databricks recommends not storing the image binary data directly in the Delta table. Instead, the Delta table should contain only metadata (such as a list of file names or paths), and the actual images should be loaded from the object store at inference time using their paths. ^[reference-solution-for-image-applications-databricks-on-aws.md]

### Related Concepts

- Auto Loader – The incremental ingestion engine on Databricks.
- [Delta table](/concepts/delta-lake-table.md) – The storage format used to manage ingested image data.
- Image ETL – The process of extracting, transforming, and loading image data.
- pandas UDF – Used in the second stage to perform distributed inference.
- Distributed Inference – Applying models at scale across a cluster.
- Object store – The source storage for image files (e.g., AWS S3).
- Reference solution for image applications – The broader architecture that includes Auto Loader and distributed inference.

### Sources

- reference-solution-for-image-applications-databricks-on-aws.md

# Citations

1. [reference-solution-for-image-applications-databricks-on-aws.md](/references/reference-solution-for-image-applications-databricks-on-aws-890cf1b8.md)
