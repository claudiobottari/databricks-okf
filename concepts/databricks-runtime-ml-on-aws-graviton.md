---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df31f9ea8e92b798ffa1cefe66bb38e5c4d0494513cbcd1cdba8ca87c6c36ad3
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-on-aws-graviton
    - DRMOAG
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Databricks Runtime ML on AWS Graviton
description: Support for Graviton instance types starting from Databricks Runtime 15.4 LTS ML, offering improved performance for Spark, Photon, feature engineering, and ML libraries like XGBoost and LightGBM with better price-to-performance.
tags:
  - databricks
  - aws
  - graviton
  - performance
timestamp: "2026-06-19T18:14:52.170Z"
---

# Databricks Runtime ML on AWS Graviton

**Databricks Runtime ML on AWS Graviton** refers to the support for AWS Graviton instance types within Databricks Runtime for Machine Learning, starting from Databricks Runtime 15.4 LTS ML and above. This configuration leverages Arm-based AWS Graviton processors to deliver improved performance and cost efficiency for machine learning workloads. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Overview

Graviton instances are AWS EC2 instance types powered by Arm-based AWS Graviton processors. When used with Databricks Runtime ML, these instances can improve performance for several key workloads including Spark, Photon, feature engineering, machine learning libraries such as XGBoost and LightGBM, and Spark MLlib algorithms for gradient boosting. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

A primary advantage of using Graviton instances is their potential to provide better price-to-performance value compared to other AWS EC2 instance types, making them an attractive option for cost-conscious ML workloads. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Supported Runtime Versions

Support for Graviton instance types begins with **Databricks Runtime 15.4 LTS ML** and continues in subsequent releases. Earlier runtime versions do not support Graviton instances. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Performance Improvements

Graviton instances offer performance improvements for the following components and libraries when used with Databricks Runtime ML:

- **Apache Spark** — General Spark processing benefits from Graviton's architecture.
- **Photon** — Databricks' vectorized query engine sees performance gains on Graviton instances.
- **[Feature Engineering](/concepts/featureengineeringclient-api.md)** — Feature transformation and preparation tasks run more efficiently.
- **[XGBoost](/concepts/xgboostspark-module.md)** and **LightGBM** — Popular gradient boosting libraries see improved performance.
- **[Spark MLlib](/concepts/apache-spark-mllib.md)** — Gradient boosting algorithms specifically benefit from Graviton instances.

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Creating a Compute Resource with Graviton Instances

To use Databricks Runtime ML on AWS Graviton instances:

1. When creating a compute resource, select **Databricks Runtime 15.4 LTS ML** or above as the runtime version.
2. Select the **Machine learning** checkbox to enable Databricks Runtime ML.
3. In the **Worker type** drop-down menu, select a Graviton instance type.

For GPU-based workloads, select a GPU-enabled instance type in the worker type menu instead of Graviton, as Graviton instances are CPU-based. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Considerations

Graviton instances are CPU-based and are not suitable for GPU-accelerated deep learning workloads. For such workloads, you should select appropriate GPU-enabled instance types. The performance benefits of Graviton instances are most pronounced for CPU-bound ML tasks such as gradient boosting, feature engineering, and Spark-based data processing. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The ML-optimized runtime that supports Graviton instances
- AWS Graviton — The Arm-based processor architecture powering these instances
- Photon — Databricks' high-performance query engine that benefits from Graviton
- [XGBoost](/concepts/xgboostspark-module.md) and LightGBM — Gradient boosting libraries with improved performance on Graviton
- [Spark MLlib](/concepts/apache-spark-mllib.md) — Spark's machine learning library, optimized for gradient boosting on Graviton
- Cost Optimization on Databricks — Strategies for reducing compute costs, including Graviton usage

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
