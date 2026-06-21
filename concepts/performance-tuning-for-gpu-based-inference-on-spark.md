---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c9753968ef56bd501562177ff701f33152ac756c78f348f74a778efdedd8f16c
  pageDirectory: concepts
  sources:
    - model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - performance-tuning-for-gpu-based-inference-on-spark
    - PTFGIOS
  citations:
    - file: model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
title: Performance Tuning for GPU-based Inference on Spark
description: Strategies for optimizing Hugging Face inference performance on Spark clusters including batch size tuning, DataFrame repartitioning, and GPU utilization monitoring
tags:
  - performance
  - gpu
  - spark
  - optimization
timestamp: "2026-06-19T19:43:24.569Z"
---

# Performance Tuning for GPU-based Inference on Spark

**Performance Tuning for GPU-based Inference on Spark** refers to the set of techniques and best practices for optimizing the throughput and resource utilization of machine learning model inference workloads that run on GPU-equipped Spark clusters. When using frameworks like Hugging Face Transformers for NLP inference, careful tuning can significantly improve performance.

## Batch Size Optimization

Choosing the right batch size is one of the most important performance levers. While Pandas UDFs work out-of-the-box with a batch size of 1, this may not use GPU resources efficiently. Practitioners should tune the batch size to the specific model and hardware configuration. The goal is to find a batch size large enough to drive full GPU utilization without causing `CUDA out of memory` errors. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

When tuning, monitor GPU performance using live cluster metrics. Key metrics include `gpu0-util` for GPU processor utilization and `gpu0_mem_util` for GPU memory utilization. If `CUDA out of memory` errors occur during tuning, a new session must be started to release the memory used by the model and data in the GPU. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Stage-Level Scheduling for Parallelism

By default, Spark schedules one task per GPU on each machine. To increase parallelism within a GPU, use **stage-level scheduling** to specify how many tasks should run per GPU. For example, setting a GPU resource request of 0.5 tells Spark to run two tasks per GPU: ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

```python
from pyspark.resource import TaskResourceRequests, ResourceProfileBuilder

task_requests = TaskResourceRequests().resource("gpu", 0.5)
builder = ResourceProfileBuilder()
resource_profile = builder.require(task_requests).build
rdd = df.withColumn('predictions', loaded_model(struct(*map(col, df.columns)))).rdd.withResources(resource_profile)
```

## Data Partitioning

Making full use of all hardware requires well-partitioned DataFrames. Generally, a small multiple of the number of GPUs (for GPU clusters) or number of cores (for CPU clusters) works well. Check the current partition count with `df.rdd.getNumPartitions()` and repartition using `df.repartition(desired_partition_count)`. The input DataFrame may already have enough partitions to take advantage of the cluster's parallelism. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Model Caching

Frequent model loading from different or restarted clusters can be optimized by caching the Hugging Face model in the DBFS root volume or on a mount point. This decreases ingress costs and reduces model load time. Set the `TRANSFORMERS_CACHE` environment variable before loading the pipeline: ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

```python
import os
os.environ['TRANSFORMERS_CACHE'] = '/dbfs/hugging_face_transformers_cache/'
```

An alternative approach is to log the model to [MLflow](/concepts/mlflow.md) using the MLflow `transformers` flavor, which provides similar caching benefits. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Pandas UDFs for Distributed Inference

When using Hugging Face Transformers pipelines for inference, wrap the model in a Pandas UDF to distribute computation across worker nodes. Set the `device` parameter to ensure GPUs are used when available — `device=0` if `torch.cuda.is_available()`, otherwise `-1` for CPU. Spark automatically reassigns GPUs on worker nodes if the cluster has instances with multiple GPUs. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Hardware Considerations

Many popular NLP models work best on GPU hardware. For optimal performance, use recent GPU hardware unless the model is specifically optimized for CPU execution. The `transformers` library comes preinstalled on Databricks Runtime 10.4 LTS ML and above. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Related Concepts

- Hugging Face Transformers — The model library used for NLP inference pipelines.
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) — The mechanism for distributing model computation on a Spark cluster.
- Spark Cluster Metrics — Live monitoring of GPU utilization and memory during inference.
- [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md) — Model logging and serving for Hugging Face models.
- [Stage-Level Scheduling](/concepts/stage-level-scheduling-for-gpu-parallelism.md) — Fine-grained control over resource allocation per task.
- Batch Inference Optimization — General strategies for improving inference throughput.
- DBFS — Databricks File System used for model caching.

## Sources

- model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md

# Citations

1. [model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md](/references/model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws-b5ae44ca.md)
