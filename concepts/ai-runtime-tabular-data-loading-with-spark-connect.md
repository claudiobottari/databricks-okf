---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96a90d81a7d8d1e81f4aac82c28c570179ffae003cabcfa3bb79113be7b6cda7
  pageDirectory: concepts
  sources:
    - load-data-on-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-tabular-data-loading-with-spark-connect
    - ARTDLWSC
  citations:
    - file: load-data-on-ai-runtime-databricks-on-aws.md
title: AI Runtime Tabular Data Loading with Spark Connect
description: Loading tabular ML data from Delta tables using Spark Connect, with conversion to pandas/NumPy via toPandas() and to_numpy().
tags:
  - data-loading
  - spark
  - databricks
  - tabular-data
timestamp: "2026-06-19T19:14:15.814Z"
---

Here is the wiki page for "AI Runtime Tabular Data Loading with Spark Connect".

---

## AI Runtime Tabular Data Loading with Spark Connect

**AI Runtime Tabular Data Loading with Spark Connect** describes the recommended method for loading structured, tabular machine learning and deep learning data from [Delta Tables](/concepts/delta-lake-table.md) on Databricks AI Runtime. This approach uses [Spark Connect](/concepts/spark-connect.md) to query tables and then converts the resulting DataFrames into formats suitable for training.

### Overview

On AI Runtime, all data access goes through [Unity Catalog](/concepts/unity-catalog.md). Tables and volumes must be registered in Unity Catalog and accessible to the user or service principal. ^[load-data-on-ai-runtime-databricks-on-aws.md]

For tabular data, Spark Connect is used to load data from Delta tables. Spark Connect supports most PySpark APIs, including Spark SQL, Pandas API on Spark, Structured Streaming, and MLlib (DataFrame-based). ^[load-data-on-ai-runtime-databricks-on-aws.md]

### Basic Usage: Single-Node Training

For single-node training, after loading data via Spark Connect, you can convert a Spark DataFrame to a pandas DataFrame using the PySpark method `toPandas()`. Optionally, you can then convert to NumPy format using the `to_numpy()` method. ^[load-data-on-ai-runtime-databricks-on-aws.md]

```python
# Load data
spark_df = spark.table("catalog.schema.my_table")
# Convert to pandas
pandas_df = spark_df.toPandas()
# Optionally convert to NumPy
numpy_array = pandas_df.to_numpy()
```

### Large Delta Tables: Using Volumes

For large Delta tables that are too big to convert with `toPandas()`, the recommended approach is to export the data to a Unity Catalog volume and load it directly using PyTorch or Hugging Face Datasets:

1. **Export** the Delta table to Parquet files in a Unity Catalog volume:
   ```python
   output_path = "/Volumes/catalog/schema/my_volume/training_data"
   spark.table("catalog.schema.my_table").write.mode("overwrite").parquet(output_path)
   ```

2. **Load** the exported data directly using Hugging Face datasets:
   ```python
   from datasets import load_dataset
   dataset = load_dataset("parquet", data_files="/Volumes/catalog/schema/my_volume/training_data/*.parquet")
   ```

This approach avoids Spark overhead during training and works well for both single-GPU and distributed training workflows. ^[load-data-on-ai-runtime-databricks-on-aws.md]

### Distributed Training with the @distributed Decorator

When using the Serverless GPU API for distributed training, data loading code must be moved inside the `@distributed` decorator. This avoids pickling errors that occur when large datasets are passed across process boundaries. ^[load-data-on-ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def run_train():
    # Load data inside the decorator to avoid pickle serialization issues
    dataset = get_dataset(file_path)
    ...
```

### Performance Considerations

When loading data from Unity Catalog, data loading speed is limited by available network bandwidth to the remote storage. For multi-epoch training, the recommended approach is to use `UCVolumeDataset` from the `serverless_gpu.data` package, which caches files locally on first access and serves subsequent reads from the local copy. ^[load-data-on-ai-runtime-databricks-on-aws.md]

### Limitations

- For Spark Connect limitations, refer to [Serverless Compute Limitations](/concepts/serverless-compute-limitations-for-jar-tasks.md).
- The distributed training API for multi-GPU workloads remains in Beta. ^[load-data-on-ai-runtime-databricks-on-aws.md]

### Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [Spark Connect](/concepts/spark-connect.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Tables](/concepts/delta-lake-table.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- serverless_gpu.data.DataLoader|Serverless GPU Data Loading

### Sources

- load-data-on-ai-runtime-databricks-on-aws.md

# Citations

1. [load-data-on-ai-runtime-databricks-on-aws.md](/references/load-data-on-ai-runtime-databricks-on-aws-0b666631.md)
