---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 379f9621e0d71ab9c87f070381e490df18c754dc543889b881fd9cef12677621
  pageDirectory: concepts
  sources:
    - applicable-model-terms-databricks-on-aws.md
  confidence: 0.5
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-on-aws
    - DOA
  citations:
    - file: applicable-model-terms-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Databricks on AWS
description: Databricks platform deployed on Amazon Web Services infrastructure for data analytics and machine learning
tags:
  - databricks
  - aws
  - platform
timestamp: "2026-06-19T09:00:58.566Z"
---

Here is the wiki page for "Databricks on AWS".

---

## Databricks on AWS

**Databricks on AWS** is the deployment of the Databricks Data Intelligence Platform on Amazon Web Services (AWS) cloud infrastructure. It provides a unified, open lakehouse architecture that combines data engineering, data science, machine learning, and analytics on top of cloud storage and compute resources managed by AWS.

### Overview

Databricks on AWS integrates deeply with native AWS services, including Amazon S3 for data lake storage, AWS IAM for identity and access management, and a wide range of EC2 instance types for compute. This integration allows organizations to leverage their existing AWS investments while gaining the benefits of Databricks' collaborative workspace, Delta Lake, and MLflow capabilities. ^[applicable-model-terms-databricks-on-aws.md]

### Key Features

- **Lakehouse Architecture**: Combines the flexibility of a data lake with the reliability and performance of a data warehouse, using Delta Lake as the foundation.
- **Unified Analytics**: Supports batch and streaming data processing, SQL analytics, and machine learning in a single platform.
- **Deep AWS Integration**: Native connectivity to Amazon S3, AWS Glue, Amazon EMR, and other AWS services.
- **Security and Governance**: Leverages AWS IAM for role-based access control, VPCs for network isolation, and Unity Catalog for fine-grained data governance.
- **Scalable Compute**: Supports a variety of EC2 instance types, including GPU instances for deep learning workloads.

### Supported GPU Instances

Databricks on AWS supports a range of GPU-enabled EC2 instances for deep learning and machine learning workloads. These include instances powered by NVIDIA A100, V100, T4, and L4 GPUs. For the complete list of supported GPU instance types, see the Databricks documentation on [supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Deep Learning Capabilities

Databricks on AWS provides a robust environment for deep learning, including:

- **Databricks Runtime for Machine Learning**: A pre-configured runtime that includes popular deep learning frameworks like TensorFlow, PyTorch, and Horovod.
- **GPU Scheduling**: Optimizes GPU utilization for distributed training and inference.
- **Distributed Training**: Supports [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) and [DeepSpeed](/concepts/deepspeed.md) for training large models with 20B to 120B+ parameters.
- **Model Serving**: Deploys models as endpoints for real-time inference, with support for GPU acceleration.

### Best Practices

- **Reserve GPU Capacity**: A100 and other high-demand GPU instances often have limited availability. Contact AWS to reserve capacity in advance for critical workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Use Spot Instances**: For non-critical or fault-tolerant workloads, consider using EC2 Spot Instances to reduce compute costs.
- **Optimize Storage**: Use Delta Lake with partitioning, Z-ordering, and liquid clustering to improve query performance on Amazon S3.
- **Implement Governance**: Use Unity Catalog with [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) and [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) to enforce fine-grained access control.

### Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [MLflow on Databricks](/concepts/mlflow-on-databricks.md)
- Lakehouse Architecture

### Sources

- applicable-model-terms-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [applicable-model-terms-databricks-on-aws.md](/references/applicable-model-terms-databricks-on-aws-2e13c689.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
