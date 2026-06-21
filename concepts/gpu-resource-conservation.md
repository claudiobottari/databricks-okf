---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47757a8742b235fdf8cb6bc2472b032bf6ae4f2a1c057638b4fded6e0c3edb72
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-resource-conservation
    - GRC
    - gRPC
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: GPU Resource Conservation
description: Best practice of attaching notebooks to CPU clusters for non-GPU operations (e.g., Git cloning, data conversion, EDA) to preserve GPU resources.
tags:
  - best-practices
  - resource-management
  - databricks
timestamp: "2026-06-19T14:25:00.143Z"
---

# GPU Resource Conservation

**GPU Resource Conservation** refers to the set of practices and platform features that minimize unnecessary GPU utilization on Databricks, helping teams manage costs, ensure availability, and avoid capacity contention. Effective conservation involves choosing the right compute type for each task, leveraging inactivity timeouts, and planning capacity for high-demand GPU instances.

## Overview

GPU instances are a finite and often contended resource in cloud environments. Databricks provides several mechanisms to conserve GPU capacity: attaching non-GPU workloads to CPU clusters, automatic timeout on idle sessions, and guidance on selecting appropriate hardware accelerators only when they are needed. ^[connect-to-ai-runtime-databricks-on-aws.md, best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices

### Use CPU Clusters for Non-GPU Operations

For operations that do not require GPUs — such as cloning a Git repository, converting data formats, or exploratory data analysis — attach the notebook to a CPU cluster instead of a GPU-enabled compute. This preserves GPU resources for the workloads that truly need them. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Select the Appropriate Accelerator

Choose the smallest GPU configuration that meets your workload’s requirements. For single-GPU tasks, a single H100 or A10 may suffice; for large model training requiring distributed parallelism, use the **8xH100** configuration. Oversizing wastes capacity and may reduce availability for other teams. ^[connect-to-ai-runtime-databricks-on-aws.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Leverage Auto-Termination

Serverless GPU compute sessions auto-terminate after 60 minutes of inactivity. This built-in timeout automatically releases GPU resources that are no longer in use, preventing idle GPUs from consuming capacity. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Plan Capacity for High-Demand Instances

A100 and H100 GPUs typically have limited capacity in cloud environments. Databricks recommends contacting your cloud provider for resource allocation or reserving capacity in advance to ensure availability for critical workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The on-demand infrastructure that provisions GPUs.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — A high-capacity configuration for distributed training.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) — Guidance on using A100 GPUs and their availability constraints.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-configured environments that include GPU libraries.
- Model Checkpointing — Persisting model state to allow resumption after job interruptions, reducing wasted compute on failed runs.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
3. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
