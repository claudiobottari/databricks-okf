---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18bd1e49b5ff5bf1ecc923461e0d5d3bfbd7d52300ad2dbdfc91564f4699cf25
  pageDirectory: concepts
  sources:
    - load-data-on-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - volume-export-for-large-delta-tables
    - VEFLDT
  citations:
    - file: load-data-on-ai-runtime-databricks-on-aws.md
title: Volume Export for Large Delta Tables
description: Technique to export oversized Delta tables to Parquet files in Unity Catalog volumes for direct loading via PyTorch or Hugging Face datasets, avoiding Spark overhead.
tags:
  - data-loading
  - delta
  - databricks
  - volumes
timestamp: "2026-06-19T19:13:45.857Z"
---

# Volume Export for Large Delta Tables

**Volume Export for Large Delta Tables** is a technique for exporting large Delta tables that are too big to convert in memory using `toPandas()`. Instead of loading the entire table into a pandas DataFrame, the data is written to Parquet files in a Unity Catalog volume, enabling direct loading by ML frameworks like PyTorch or [Hugging Face](/concepts/hugging-face-trainer.md) without Spark overhead. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Overview

When working with [AI Runtime](/concepts/ai-runtime.md) for machine learning and deep learning applications on Databricks, tabular data is typically loaded from [Delta tables](/concepts/delta-lake-table.md). For single-node training, the recommended approach is to convert a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) to a pandas DataFrame using `toPandas()`, then optionally convert to NumPy format. However, for large Delta tables that exceed available memory, this conversion becomes impractical. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Export Process

The solution is to export the Delta table to Parquet files in a Unity Catalog volume:

```python
# Step 1: Export the Delta table to Parquet files in a UC volume
output_path = "/Volumes/catalog/schema/my_volume/training_data"
spark.table("catalog.schema.my_table").write.mode("overwrite").parquet(output_path)
```

```python
# Step 2: Load the exported data directly using Hugging Face datasets
from datasets import load_dataset
dataset = load_dataset("parquet", data_files="/Volumes/catalog/schema/my_volume/training_data/*.parquet")
```

This two-step approach writes the Delta table in parallel to Parquet files using Spark's distributed write, then loads those files directly with [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) — avoiding Spark overhead during training while remaining compatible with both [single-GPU](/concepts/single-gpu-fine-tuning.md) and distributed training workflows. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Benefits

- **Avoids memory limits**: The table is never fully materialized in a single Python process; Spark writes in parallel and the ML framework reads only what it needs.
- **Works with large tables**: Tables too large for `toPandas()` can be exported and consumed by any Parquet-compatible reader.
- **Compatible with distributed training**: The exported Parquet files can be sharded across ranks when used inside the [@distributed Decorator](/concepts/distributed-decorator.md).

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Required for all data access on AI Runtime
- Unity Catalog volumes – Storage location for exported data
- [Data loading on AI Runtime](/concepts/databricks-ai-runtime.md) – Full guide for data loading patterns
- [AI Runtime](/concepts/ai-runtime.md) – The runtime environment supporting these workflows
- [UCVolumeDataset](/concepts/ucvolumedataset.md) – For loading unstructured data from volumes with local caching

## Sources

- load-data-on-ai-runtime-databricks-on-aws.md

# Citations

1. [load-data-on-ai-runtime-databricks-on-aws.md](/references/load-data-on-ai-runtime-databricks-on-aws-0b666631.md)
