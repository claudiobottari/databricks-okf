---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32df64b714f1b49932c4aff7e28b024a8d01fbe270028c0053da44960bf82661
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-gpu-distributed-training-api
    - MDTA
    - Multi-GPU Distributed Training
    - Multi-GPU distributed training
    - Multi‑GPU distributed training
    - multi-GPU distributed training
    - Multi-GPU Training
    - Multi-GPU and multi-node distributed training
    - Multi-Node Distributed Training
    - Multi‑GPU Training
    - multi-GPU training
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Multi-GPU distributed training API
description: Beta-stage API on Databricks for scaling training workloads across multiple GPUs and nodes.
tags:
  - distributed-training
  - gpu
  - beta
timestamp: "2026-06-19T17:31:35.190Z"
---

# Multi-GPU distributed training API

The **Multi-GPU distributed training API** is a component of [AI Runtime](/concepts/ai-runtime.md) on Databricks that provides the ability to scale training workloads across multiple GPUs and nodes. The API uses the [Serverless GPU API](/concepts/serverless-gpu-api.md) to manage compute resources for distributed training tasks. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Availability

This API is currently in **Beta** status. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example Notebooks

Databricks offers example notebooks that demonstrate how to use the multi-GPU distributed training API for scaling training across multiple GPUs and nodes. These examples are part of the [AI Runtime example notebooks](/concepts/ai-runtime-example-notebooks.md) collection. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [Serverless GPU API](/concepts/serverless-gpu-api.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- Multi-Node Training
- [Single-Node GPU Training](/concepts/single-node-gpu-training-on-databricks.md)

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
