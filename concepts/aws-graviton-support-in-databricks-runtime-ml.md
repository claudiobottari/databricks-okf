---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85a651776ccbb35e976d3fcba1a10dfe770c5b984ebd958e0505d0a5c2470f29
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aws-graviton-support-in-databricks-runtime-ml
    - AGSIDRM
    - AWS Graviton Instances
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: AWS Graviton Support in Databricks Runtime ML
description: Support for AWS Graviton (ARM-based) instance types in Databricks Runtime 15.4 LTS ML and above, offering improved performance for Spark, Photon, feature engineering, XGBoost, LightGBM, and Spark MLlib gradient boosting.
tags:
  - aws
  - performance
  - instance-types
timestamp: "2026-06-18T15:09:13.250Z"
---

# AWS Graviton Support in Databricks Runtime ML

**AWS Graviton Support in Databricks Runtime ML** refers to the ability to run Databricks Runtime for Machine Learning on AWS Graviton instance types, which are based on Arm-based AWS Graviton processors. This support enables improved price-to-performance value for many machine learning and data processing workloads.

## Overview

Databricks Runtime 15.4 LTS ML and above support Graviton instance types. Using Graviton instances can improve performance for several key workloads, including Spark, Photon, feature engineering, and machine learning libraries such as XGBoost and LightGBM. Additionally, Spark MLlib algorithms for gradient boosting benefit from Graviton instances. Graviton instances may also provide better price-to-performance value compared to other AWS EC2 instance types. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Supported Workloads

Graviton instances show performance improvements for the following:

- **Spark and Photon** — General data processing and SQL workloads
- **Feature engineering** — Feature transformation and preparation tasks
- **Machine learning libraries** — XGBoost and LightGBM training
- **Spark MLlib algorithms** — Particularly gradient boosting algorithms

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Availability

AWS Graviton support is available starting with Databricks Runtime 15.4 LTS ML. To use Graviton instances, select a Graviton-compatible instance type in the **Worker type** drop-down menu when creating a compute resource. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

For the complete list of supported GPU and CPU instance types, including Graviton, see the Databricks documentation on [supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list). ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Creating a Graviton Compute Resource

To create a compute resource using Graviton instances with Databricks Runtime ML:

1. Select the **Machine learning** checkbox in the create compute UI to use Databricks Runtime ML.
2. In the **Worker type** drop-down menu, select a Graviton instance type.
3. The access mode is automatically set to **Dedicated** for Databricks Runtime ML compute resources.

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime that includes Graviton support
- AWS Graviton — Arm-based processors designed by AWS
- [GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — GPU instance types for deep learning workloads
- Photon on Databricks — Performance-optimized engine that benefits from Graviton
- [Dedicated Access Mode](/concepts/dedicated-access-mode-for-ml-compute.md) — Required access mode for Databricks Runtime ML compute resources
- Supported Instance Types on Databricks — Complete list of available instance types

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
