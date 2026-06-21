---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc90b2770ce39d73da5a95bdaacce680efb6bf4802c0b93afdf1f968c073d037
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compute-scale-out-configuration
    - CSC
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Compute Scale-out Configuration
description: Configuring concurrency and scaling for serving endpoints using Small (0-4), Medium (8-16), or Large (16-64) scale-out sizes, with optional scale-to-zero for non-production use.
tags:
  - model-serving
  - scaling
  - compute
timestamp: "2026-06-19T18:01:09.209Z"
---

# Compute Scale-out Configuration

**Compute Scale-out Configuration** refers to a setting within Databricks [Model Serving](/concepts/model-serving.md) that controls the number of simultaneous requests a served model can process. The configuration is selected when creating or updating a custom model serving endpoint and directly impacts the endpoint’s throughput and resource allocation.

## Overview

When creating a custom model serving endpoint through the Databricks Serving UI, you must choose a **Compute Scale-out** size. The selected size determines the concurrency level — the number of requests the served model can handle at the same time. The appropriate value should be roughly equal to the product of the expected queries per second (QPS) and the model’s runtime per request.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Available Sizes

Databricks provides three predefined compute scale-out sizes:^[create-custom-model-serving-endpoints-databricks-on-aws.md]

| Size   | Concurrent requests |
|--------|---------------------|
| Small  | 0–4                 |
| Medium | 8–16                |
| Large  | 16–64               |

These values are intended as a starting point. For workloads requiring custom concurrency settings outside these ranges, see the Model Serving Limits documentation.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Selection Guidance

To select the appropriate size, estimate the number of requests that need to run simultaneously. For example, if your model takes 200 ms to run and you expect 50 QPS, the required concurrency is roughly 10, which falls within the Medium range. The size should be chosen to match the throughput requirements without over‑ or under‑provisioning.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Relationship to GPU Replicas

For GPU workloads, the model serving endpoint provisions replicas based on the **concurrency** setting (a separate configuration from compute scale-out). The number of replicas equals the concurrency value divided by 4. Compute scale-out is distinct and controls the number of requests per replica, not the number of replicas.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The platform for deploying and serving custom models.
- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) – The full workflow for endpoint creation.
- [GPU workload types](/concepts/gpu-workload-types-for-model-serving.md) – GPU‑specific compute options for model serving.
- Model Serving Limits – Custom concurrency and resource constraints.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
