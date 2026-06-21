---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8218f3c46c257236db29399ced3ef8b952e07f46648b8fb08dce62038ded6801
  pageDirectory: concepts
  sources:
    - migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-for-llm-serving
    - PTFLS
  citations:
    - file: migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
title: Provisioned Throughput for LLM Serving
description: A Databricks offering that simplifies LLM serving endpoints by allowing scale-out configuration in tokens per second instead of concurrency, and removing the need for manual GPU workload type selection.
tags:
  - llm-serving
  - databricks
  - provisioned-throughput
timestamp: "2026-06-19T19:34:05.848Z"
---

# Provisioned Throughput for LLM Serving

**Provisioned Throughput for LLM Serving** is a Databricks offering that simplifies the deployment and management of optimized [LLM serving endpoints](/concepts/model-serving-endpoint.md). It provides a more intuitive experience for configuring [Foundation Model APIs](/concepts/foundation-model-apis.md) by replacing complex GPU workload selection with LLM-native throughput metrics. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Overview

Provisioned throughput modifies how LLM serving endpoints are configured and managed. Instead of requiring users to select GPU workload types directly, the system abstracts infrastructure details and allows configuration in terms relevant to LLM applications. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Key Features

### Simplified Scale-Out Configuration

With provisioned throughput, scale-out ranges can be configured in **LLM-native terms**, such as tokens per second, rather than abstract measures like concurrency. This makes capacity planning more intuitive for machine learning practitioners and application developers. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

### Automated GPU Workload Selection

Customers no longer need to manually select GPU workload types. The system handles this selection automatically, reducing the operational complexity of deploying LLM endpoints. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

### Improved Performance

Provisioned throughput offers strictly better performance compared to previous optimized LLM serving due to ongoing optimization improvements. The price for existing endpoints remains unchanged after migration. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Migration

### Default Experience

New LLM serving endpoints are created with provisioned throughput by default. The previous experience requiring manual GPU workload type selection is only supported through the API. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

### Migrating Existing Endpoints

To migrate an existing optimized LLM serving endpoint to provisioned throughput:

1. Update the endpoint with a new model version.
2. After selecting a new model version, the UI automatically displays the provisioned throughput experience.
3. The UI shows tokens per second ranges based on Databricks benchmarking for typical use cases.

^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

### Migration Benefits

- Simpler configuration workflow
- Performance improvements through ongoing optimization
- No price increase for existing endpoints

## Important Note

This documentation has been retired and might not be updated. The products, services, or technologies mentioned may no longer be supported. For product feedback or concerns, contact `model-serving-feedback@databricks.com`. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The API layer for deploying foundation models on Databricks
- [LLM serving endpoints](/concepts/model-serving-endpoint.md) — Endpoints used to serve large language models
- [Model Serving](/concepts/model-serving.md) — General concept for deploying ML models as APIs
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU infrastructure for model serving

## Sources

- migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md

# Citations

1. [migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md](/references/migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws-b1657ebd.md)
