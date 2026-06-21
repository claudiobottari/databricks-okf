---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca546095e3516dba572e4c9b4ad98aa1e5acc8640391519c3865b33381528b6e
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - photon-on-databricks-runtime-ml
    - PODRM
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Photon on Databricks Runtime ML
description: A performance optimization engine for Spark SQL, DataFrames, and feature engineering workloads, available on Databricks Runtime 15.2 ML and above
tags:
  - performance
  - databricks
  - photon
  - optimization
timestamp: "2026-06-19T09:53:43.300Z"
---

# Photon on Databricks Runtime ML

**Photon on Databricks Runtime ML** refers to the optional enablement of the [Photon](https://docs.databricks.com/aws/en/compute/photon) engine when creating a compute resource that runs Databricks Runtime for Machine Learning (Databricks Runtime ML). Photon is a high-performance query engine that improves execution speed for specific workloads within the ML lifecycle.

## Availability

Photon can be enabled when you create a compute resource running **Databricks Runtime 15.2 ML** or above. When you select the **Machine learning** checkbox in the compute creation UI, you have the option to enable Photon alongside the pre-installed ML and DL libraries.^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Performance Benefits

Photon improves performance for applications that leverage the following technologies:^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- Spark SQL
- Spark DataFrames
- Feature engineering
- GraphFrames
- xgboost4j

These workloads benefit from Photon's optimized execution engine, making them faster than equivalent operations on standard runtimes.

## Limitations

Photon is **not expected to improve performance** on the following types of workloads:^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- **Spark RDD APIs** — Low-level distributed data abstractions.
- **Pandas UDFs** — User-defined functions written in Python using Pandas.
- **Non-JVM languages** such as Python.

As a result, common Python-based ML libraries — including XGBoost (Python package), [PyTorch](/wiki/pytorch), and [TensorFlow](/wiki/tensorflow) — will **not** see performance improvements with Photon enabled. These libraries operate primarily in Python and do not leverage the Photon engine.^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Compatibility Notes

Spark RDD APIs and [Spark MLlib](https://docs.databricks.com/aws/en/machine-learning/train-model/mllib) have **limited compatibility** with Photon. When processing large datasets using Spark RDD or Spark MLlib with Photon enabled, users may experience Spark memory issues. See the documentation on [Spark memory issues](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/spark-memory-issues) for troubleshooting guidance.^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## When to Enable Photon

Enable Photon on Databricks Runtime ML when your workload involves significant DataFrame operations, feature engineering pipelines, or Spark SQL queries as part of your ML training or inference pipeline. If your workload is predominantly Python-based (using PyTorch, TensorFlow, or pandas UDFs), Photon will not provide speed benefits and can remain disabled.^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime that provides pre-built ML and DL infrastructure.
- Photon — The high-performance query engine for Spark workloads.
- GPU Scheduling — Optimizing GPU utilization for deep learning on Databricks.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — GPU instance types available with Databricks Runtime ML.
- [AutoML on Databricks](/concepts/automl-on-databricks.md) — Automated model training using Databricks Runtime ML.

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
