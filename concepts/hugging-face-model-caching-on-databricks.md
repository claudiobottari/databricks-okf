---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6729ac825f387d10f9b7b42011012279b2e445f1ed53826b48bf8e8ac059fcf
  pageDirectory: concepts
  sources:
    - model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hugging-face-model-caching-on-databricks
    - HFMCOD
  citations:
    - file: model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
title: Hugging Face Model Caching on Databricks
description: Caching Hugging Face models in DBFS or mount points to reduce model load times and ingress costs across clusters by setting the TRANSFORMERS_CACHE environment variable
tags:
  - caching
  - hugging-face
  - dbfs
timestamp: "2026-06-19T19:43:19.101Z"
---

# Hugging Face Model Caching on Databricks

**Hugging Face Model Caching on Databricks** refers to strategies for storing pre-trained Hugging Face Transformer models in persistent storage locations (such as DBFS or mount points) to reduce load times and ingress costs when using them repeatedly across different or restarted clusters. Caching is particularly relevant for batch inference workflows using [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) on Databricks clusters.

## Overview

When running Hugging Face Transformers pipelines for tasks like translation, summarization, or named-entity recognition, the model is downloaded and loaded into memory each time a pipeline is created. On Databricks, this can lead to repeated download costs and longer startup times if the model is used frequently or across different clusters. The [TRANSFORMERS_CACHE](/concepts/mlflow-transformers-flavor.md) environment variable allows you to redirect where Hugging Face stores downloaded models, enabling persistent caching. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Caching Methods

### DBFS Root Volume Caching

The primary recommended caching method is to set the `TRANSFORMERS_CACHE` environment variable to a path within the [DBFS root volume](/concepts/dbfs-root-location.md) before loading the pipeline. This stores the model files in a cluster-agnostic location that persists across cluster restarts and can be shared by multiple clusters.

**Example:**

```python
import os
os.environ['TRANSFORMERS_CACHE'] = '/dbfs/hugging_face_transformers_cache/'
```

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Mount Point Caching

Alternatively, you can cache the model on a mount point in DBFS. Mount points provide access to external cloud storage (e.g., S3) or other persistent volumes, which can decrease ingress costs and reduce the time to load the model on a new or restarted cluster. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### MLflow Model Logging

You can achieve similar benefits by logging the model to MLflow using the [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md). MLflow captures the model artifacts and configuration, allowing you to load the model directly from an [MLflow Run](/concepts/mlflow-run.md) without re-downloading from Hugging Face. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Best Practices

- **Set the cache variable before loading the pipeline** – Ensure `TRANSFORMERS_CACHE` is set in the environment before instantiating any pipeline object.
- **Verify cache path** – Confirm that the cached directory is accessible from all worker nodes, especially when using [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) for distributed inference.
- **Combine with batch size tuning** – Caching reduces per-call overhead, but still tune batch sizes to avoid CUDA out-of-memory errors on GPU clusters.
- **Monitor GPU utilization** – Use Databricks cluster metrics (e.g., `gpu0-util`, `gpu0_mem_util`) to verify that caching does not interfere with GPU memory usage.

## Related Concepts

- TRANSFORMERS_CACHE environment variable
- [DBFS root volume](/concepts/dbfs-root-location.md)
- DBFS mounts
- [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md)
- [Pandas UDFs for model inference](/concepts/pandas-udfs-for-distributed-model-inference-on-spark.md)
- Hugging Face Transformers on Databricks
- Model caching strategies

## Sources

- model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md

# Citations

1. [model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md](/references/model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws-b5ae44ca.md)
