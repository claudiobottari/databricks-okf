---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97c9fc241737523612ac94782c7c9efbd7865019333702cd89dada4e80cdd494
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - photon-compatibility-with-databricks-runtime-ml
    - PCWDRM
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Photon Compatibility with Databricks Runtime ML
description: Photon can be enabled on Databricks Runtime 15.2 ML+ to improve Spark SQL, DataFrames, feature engineering, and xgboost4j performance, but does not benefit Python-based ML packages like PyTorch and TensorFlow.
tags:
  - databricks
  - photon
  - performance
timestamp: "2026-06-19T18:14:55.528Z"
---

```yaml
---
title: Photon Compatibility with Databricks Runtime ML
summary: Photon acceleration support in Databricks Runtime 15.2 ML and above for Spark SQL, DataFrames, feature engineering, GraphFrames, and xgboost4j, with limitations for RDDs, Pandas UDFs, and Python-only libraries.
sources:
  - databricks-runtime-for-machine-learning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:41:23.068Z"
updatedAt: "2026-06-18T15:09:17.223Z"
tags:
  - performance
  - databricks
  - spark
aliases:
  - photon-compatibility-with-databricks-runtime-ml
  - PCWDRM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Photon Compatibility with Databricks Runtime ML

**Photon Compatibility with Databricks Runtime ML** describes which workloads are accelerated by the Photon native vectorized query engine when running on [[Databricks Runtime for Machine Learning]] compute resources. Photon is available as an optional feature starting from Databricks Runtime 15.2 ML and above. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Workloads That Benefit

Photon improves performance for the following types of applications:

- Spark SQL queries and transformations
- Spark DataFrame operations
- Feature engineering tasks using Spark DataFrames or SQL
- GraphFrames graph processing
- xgboost4j (the JVM-based XGBoost interface)

When a machine-learning pipeline is dominated by these workloads, enabling Photon typically yields significant speed improvements without code changes. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Workloads That Do Not Benefit

Photon is **not expected** to improve performance on:

- Applications using Spark RDD APIs
- Pandas UDFs (user-defined functions operating on Pandas DataFrames)
- Code written in non‑JVM languages such as Python, R, or Scala UDFs executed outside the JVM

Because Photon’s optimizations target JVM execution paths, Python‑native libraries — including XGBoost (the Python package), PyTorch, and TensorFlow — do not see acceleration. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Spark MLlib Compatibility

[[Apache Spark MLlib|Spark MLlib]] has **limited compatibility** with Photon. When processing large datasets using Spark RDD APIs or Spark MLlib, you may encounter Spark memory issues. Databricks recommends testing MLlib workflows separately when Photon is enabled and monitoring memory consumption. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Availability

Photon can be enabled on compute resources that run Databricks Runtime 15.2 ML or above. In the create‑compute UI or API, select the **Machine learning** checkbox to set the runtime version, then enable Photon as an additional configuration. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- Photon — The native vectorized query engine
- [[Databricks Runtime for Machine Learning]] — Pre‑built runtime with ML libraries
- Spark Memory Issues — Troubleshooting memory problems when using Photon and Spark MLlib
- GPU Scheduling — Optimizing GPU resources for ML workloads

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md
```

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
