---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82a313e8666587a7c0a562982b18c71166309756230584c7f199564c385a45e0
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - photon-compatibility-with-ml-workloads
    - PCWMW
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Photon Compatibility with ML Workloads
description: Photon acceleration improves performance for Spark SQL, DataFrames, feature engineering, and xgboost4j but not for Spark RDDs, Pandas UDFs, Python packages like XGBoost/PyTorch/TensorFlow, and may cause memory issues with Spark MLlib.
tags:
  - photon
  - performance
  - spark
  - machine-learning
timestamp: "2026-06-19T14:53:18.430Z"
---

# Photon Compatibility with ML Workloads

**Photon Compatibility with ML Workloads** describes how the Photon engine—Databricks’ vectorized query engine—interacts with machine learning and deep learning libraries, highlighting which workloads benefit and which see limited or no improvement.

## Introduction

Photon is an optional acceleration engine available on compute resources that run Databricks Runtime 15.2 ML or above. When enabled, Photon optimizes specific workloads by vectorizing execution, but its benefits are not universal. Understanding the boundary between supported and unsupported operations is essential for planning ML training and feature engineering pipelines. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Supported Workloads

Photon improves performance for applications that use:

- **Spark SQL** queries and **Spark DataFrames**
- **Feature engineering** operations
- **GraphFrames** computations
- **xgboost4j** – the JVM-based XGBoost Spark integration

These workloads typically run on the JVM and benefit from Photon’s vectorized execution model. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Unsupported or Limited Workloads

Photon is **not expected** to improve performance on applications that rely on:

- **Spark RDD APIs**
- **Pandas UDFs**
- **Non-JVM languages such as Python**

Because Python-based ML libraries run outside the JVM, they do not gain acceleration from Photon. Specific examples include:

- **XGBoost** (Python package)
- **PyTorch**
- **TensorFlow**

These libraries will continue to use their native execution paths and will not see a performance improvement from enabling Photon. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

Additionally, **Spark MLlib** and the **Spark RDD APIs** have only limited compatibility with Photon. When processing large datasets using Spark RDD or Spark MLlib, users may encounter Spark memory issues. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Recommendations

Enable Photon only when your ML pipeline contains substantial Spark SQL, DataFrame, feature engineering, or GraphFrames work. For pipelines dominated by Python-based training loops (PyTorch, TensorFlow, or Python XGBoost), Photon provides no measurable benefit and can be left disabled.

If your workload mixes JVM-based feature engineering with Python training, Photon can accelerate the feature engineering stage while leaving the training stage unaffected. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- Photon – Databricks’ vectorized query engine
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime for ML and DL workloads
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – Process accelerated by Photon
- [Spark MLlib](/concepts/apache-spark-mllib.md) – Limited Photon compatibility
- [XGBoost](/concepts/xgboostspark-module.md) – Python package not accelerated; JVM binding (xgboost4j) is accelerated
- PyTorch – Not accelerated by Photon
- TensorFlow – Not accelerated by Photon
- Spark Memory Issues – Potential problem when using RDD/MLlib with Photon

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
