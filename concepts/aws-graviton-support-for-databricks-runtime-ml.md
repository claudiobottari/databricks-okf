---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b3016953f9db3d474a89fe314de818583b9ad9c17c8155fb0f5e187f521fb03
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aws-graviton-support-for-databricks-runtime-ml
    - AGSFDRM
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: AWS Graviton Support for Databricks Runtime ML
description: Support for Graviton instance types starting from Databricks Runtime 15.4 LTS ML, offering improved price-to-performance for Spark, Photon, and ML libraries
tags:
  - aws
  - graviton
  - databricks
  - infrastructure
timestamp: "2026-06-19T09:54:12.382Z"
---

Here is the wiki page for "AWS Graviton Support for Databricks Runtime ML".

---

# AWS Graviton Support for Databricks Runtime ML

**AWS Graviton Support for Databricks Runtime ML** refers to the ability to run [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (Databricks Runtime ML) on AWS Graviton instance types. This support is available starting from Databricks Runtime 15.4 LTS ML. Graviton instances, powered by AWS-designed Arm-based processors, offer performance improvements and a better price-to-performance ratio for specific machine learning workloads. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Supported Runtime Versions

AWS Graviton instance types are supported on Databricks Runtime **15.4 LTS ML and above**. Earlier versions of Databricks Runtime ML do not include Graviton support. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Performance Benefits

Using Graviton instance types with Databricks Runtime ML can improve performance for the following workloads: ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- **Spark** — General data processing workloads
- **Photon** — The accelerated query engine for SQL and DataFrames
- **Feature engineering** — Data transformation and feature computation
- **Machine learning libraries** — Including [XGBoost](/concepts/xgboostspark-module.md) and LightGBM
- **Spark MLlib algorithms for gradient boosting** — Distributed ML training algorithms

Graviton instances may also provide **better price-to-performance value** compared to other AWS EC2 instance types, making them a cost-effective option for ML infrastructure. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Creating a Compute Resource with Graviton

To use Graviton instance types with Databricks Runtime ML: ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

1. In the Databricks workspace, create a new compute resource.
2. Select the **Machine learning** checkbox to enable Databricks Runtime ML.
3. In the **Worker type** drop-down menu, select a supported Graviton instance type (such as `m7g`, `c7g`, or `r7g` families).
4. Ensure the Databricks Runtime version is set to **15.4 LTS ML or above**.

## Comparison with Other Instance Types

Graviton instances complement existing GPU-based compute options. While GPU instances remain necessary for deep learning workloads that require NVIDIA CUDA support, Graviton instances are well-suited for CPU-intensive ML tasks such as: ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- Feature engineering pipelines
- Gradient boosting model training (XGBoost, LightGBM)
- Spark MLlib algorithms
- Data preprocessing and transformation

For GPU-based ML workloads, see GPU compute on Databricks.

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The platform that includes Graviton support
- [AWS Graviton Instances](/concepts/aws-graviton-support-in-databricks-runtime-ml.md) — Arm-based processors from AWS
- Photon — Accelerated query engine compatible with Graviton
- GPU compute on Databricks — GPU options for deep learning
- [XGBoost](/concepts/xgboostspark-module.md) — Gradient boosting library benefiting from Graviton
- LightGBM — Gradient boosting framework with Graviton improvements
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — Workload type that performs well on Graviton

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
