---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d59bfb847f13e3ec3573510f2929ef47f2d9d9482af1321b35edd4180574393c
  pageDirectory: concepts
  sources:
    - distributed-data-parallel-ddp-training-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mosaic-streaming-mds-format
    - MS(F
    - Mosaic Streaming (MDS)
  citations:
    - file: distributed-data-parallel-ddp-training-databricks-on-aws.md
title: Mosaic Streaming (MDS) format
description: A data format used for preparing and streaming training data, demonstrated in the context of distributed training on Databricks.
tags:
  - data-format
  - distributed-training
  - databricks
timestamp: "2026-06-19T18:32:22.511Z"
---

```yaml
---
title: Mosaic Streaming (MDS) format
summary: A data preparation and streaming format used for efficient data loading in distributed training workflows, particularly on Databricks.
sources:
  - distributed-data-parallel-ddp-training-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:28:59.329Z"
updatedAt: "2026-06-18T15:28:59.329Z"
tags:
  - data-format
  - distributed-training
  - data-loading
aliases:
  - mosaic-streaming-mds-format
  - MDS format
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Mosaic Streaming (MDS) Format

**Mosaic Streaming (MDS) format** is a data preparation and streaming format used for efficient data loading in distributed training workflows. It is particularly useful for large-scale machine learning tasks where datasets must be efficiently partitioned and streamed across multiple GPUs during training. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Usage on Databricks

On Databricks, MDS format is used in notebook examples for training a [Two-Tower Recommender System](/concepts/two-tower-recommender-system.md) using [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md). The data preparation step involves converting raw datasets into MDS format before initiating distributed training across A10 or H100 GPU clusters. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

The complete notebooks are available on the [Deep learning recommendation examples](/concepts/deep-learning-based-recommender-systems.md) page, which includes:

- Data preparation and MDS format conversion
- Two-tower recommender training with PyTorch Lightning

## Benefits

MDS format enables efficient streaming of data during training, which is critical when working with large datasets that cannot fit entirely in GPU memory. It supports fast data loading and partitioning across distributed workers, reducing I/O bottlenecks in [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) training workflows. ^[distributed-data-parallel-ddp-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP) Training](/concepts/distributed-data-parallel-ddp-training.md) – Common parallelism technique that uses MDS for data loading.
- [Deep learning recommendation examples](/concepts/deep-learning-based-recommender-systems.md) – Databricks notebooks that demonstrate MDS format usage.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – High-level framework used with MDS streaming.
- A10 GPU Support on Databricks – GPU type used with MDS-prepared data.
- H100 GPU Support on Databricks – GPU type used with MDS-prepared data.
- [Data loading](/concepts/ai-runtime-data-loading.md) – General concept of efficiently loading data during training.

## Sources

- distributed-data-parallel-ddp-training-databricks-on-aws.md

# Citations

1. [distributed-data-parallel-ddp-training-databricks-on-aws.md](/references/distributed-data-parallel-ddp-training-databricks-on-aws-7c300c72.md)
