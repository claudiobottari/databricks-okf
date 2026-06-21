---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83ed5f4adbbae0862887ff006dc917376085c7842efe4ebe4b01dcebc9cb4bd1
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-learning-data-loading-with-delta-lake
    - DLDLWDL
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Deep Learning Data Loading with Delta Lake
description: Best practices for using Delta Lake tables and streaming approaches (PyTorch IterableDataset, Hugging Face datasets, Ray Data) to optimize data throughput for deep learning workloads on Databricks.
tags:
  - deep-learning
  - data-loading
  - delta-lake
  - databricks
timestamp: "2026-06-18T10:53:05.079Z"
---

# Deep Learning Data Loading with Delta Lake

**Deep Learning Data Loading with Delta Lake** refers to the practice of using [Delta Lake](/concepts/delta-lake.md) tables as the primary storage format for deep learning datasets on Databricks. Delta Lake optimizes data throughput for deep learning applications, simplifies ETL, and provides efficient access to data for both training and inference.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Benefits

Cloud data storage is typically not optimized for I/O, which can be a challenge for deep learning models that require large datasets. Databricks Runtime ML includes Delta Lake to address this by providing a transactional storage layer that optimizes data throughput. Delta Lake simplifies ETL pipelines and enables efficient data access, especially for image datasets where it helps optimize ingestion for both training and inference.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices

### Use Delta Lake tables for data storage

Databricks recommends storing deep learning training and inference data in Delta Lake tables. This approach provides ACID transactions, scalable metadata handling, and unified batch and streaming capabilities. For image-based workloads, the reference solution for image ETL and inference demonstrates how to optimize data ingestion using Delta Lake.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Preprocess data into Delta Lake before inference

If you expect to access data for inference more than once, consider creating a preprocessing job to ETL the data into a [Delta Lake Table](/concepts/delta-lake-table.md) before running the inference job. This spreads the cost of ingesting and preparing the data across multiple reads. Separating preprocessing from inference also allows you to select different hardware for each job—for example, CPUs for ETL and GPUs for inference—to optimize cost and performance.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Use streaming for very large datasets

For datasets that are too large to fit in memory, combine Delta Lake with streaming approaches:

- **PyTorch `IterableDataset`** for custom streaming logic.
- **Hugging Face Datasets** with streaming for datasets hosted on the Hub or in volumes.
- **Ray Data** for distributed batch data processing.

These streaming methods can read from Delta Lake tables incrementally, avoiding the need to load the entire dataset into memory.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Integration with MLflow and Model Serving

Data loaded from Delta Lake can be used with MLflow-tracked training runs and later deployed for batch, streaming, or online inference via [Model Serving](/concepts/model-serving.md). When a model is logged from Databricks, MLflow automatically provides inference code to apply the model as a pandas UDF, which can read from Delta Lake tables for batch scoring.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format and transactional layer
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — Pre-configured runtime environment for deep learning
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking linked to data loading pipelines
- ETL — Extract, Transform, Load pipelines that populate Delta Lake tables
- Image ETL Reference Solution — Example of optimizing image ingestion with Delta Lake
- [Model Serving](/concepts/model-serving.md) — Deployment of models trained on data loaded from Delta Lake
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) — For scaling inference on Delta Lake data across a cluster

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
