---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6cc5ae092ac9fa968d4e6900a0fe39fc021bc47cf9ddaa71fdca0f348389da79
  pageDirectory: concepts
  sources:
    - reference-solution-for-image-applications-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - large-image-file-handling-strategy
    - LIFHS
  citations:
    - file: reference-solution-for-image-applications-databricks-on-aws.md
title: Large Image File Handling Strategy
description: Recommendation to store only metadata in Delta tables and load large images (>100 MB on average) directly from object store by path when needed, to avoid performance bottlenecks.
tags:
  - performance
  - optimization
  - data-engineering
  - best-practices
timestamp: "2026-06-19T20:12:54.760Z"
---

# Large Image File Handling Strategy

**Large Image File Handling Strategy** refers to the recommended approach for managing and processing image datasets where the average image size exceeds approximately 100 MB. On Databricks, the standard practice of storing image binaries directly in a Delta table becomes impractical at this scale, and a metadata-only management strategy is adopted instead. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Strategy Overview

For datasets with an average image file size greater than 100 MB, Databricks recommends **not** storing the actual image files inside a Delta table. Instead, the Delta table is used solely to manage metadata — specifically, a list of file names or paths pointing to the original images in the object store. When processing is required (for training or inference), the images are loaded directly from the object store using their stored paths rather than from the table. ^[reference-solution-for-image-applications-databricks-on-aws.md]

This approach avoids the excessive I/O and storage overhead that would result from reading and writing large binary objects (BLOBs) through the Delta table. It also keeps the table lightweight and queryable for metadata operations such as filtering, deduplication, and tracking newly arrived images. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Relationship to Standard Image ETL

The standard workflow for smaller images uses Auto Loader to ingest images into a Delta table, which simplifies data management and automatically handles continuously arriving new images. When the average image size is small, storing the full image binaries in the Delta table is acceptable. The large‑image strategy modifies this pipeline by retaining only file paths in the table and loading images on‑demand during Distributed inference using pandas UDF or other processing steps. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Applicability

This strategy is recommended when the average image size exceeds **100 MB**. It is especially relevant for workloads involving high‑resolution medical imagery, satellite imagery, or high‑frame‑rate video frames where individual file sizes are large. The metadata‑only approach keeps the Delta table performant and cost‑effective. ^[reference-solution-for-image-applications-databricks-on-aws.md]

## Related Concepts

- Auto Loader – Ingestion tool for continuously arriving files, used in the standard image pipeline.
- [Delta table](/concepts/delta-lake-table.md) – Storage format for tabular data; used here for metadata only when images are large.
- Distributed inference using pandas UDF – How models are applied to images after loading.
- [Image model inference on Databricks](/concepts/distributed-image-inference-on-databricks.md) – Broader workflow for applying deep learning models to images.
- Object store – Cloud storage (e.g., S3) where the actual image files reside.

## Sources

- reference-solution-for-image-applications-databricks-on-aws.md

# Citations

1. [reference-solution-for-image-applications-databricks-on-aws.md](/references/reference-solution-for-image-applications-databricks-on-aws-890cf1b8.md)
