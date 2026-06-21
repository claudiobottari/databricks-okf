---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf5df98d97a08eeb776797e2f20c1094806abb831ace4defc10f639a95fed434
  pageDirectory: concepts
  sources:
    - migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-workload-type-selection-deprecation
    - GWTSD
  citations:
    - file: migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
title: GPU Workload Type Selection Deprecation
description: The move away from requiring customers to manually select GPU workload types for LLM serving endpoints, with legacy API-only support remaining for those who need to continue selecting GPU types.
tags:
  - gpu
  - deprecation
  - databricks
timestamp: "2026-06-19T19:34:05.285Z"
---

# GPU Workload Type Selection Deprecation

**GPU Workload Type Selection Deprecation** refers to the retirement of the manual GPU workload type selection for Databricks [LLM serving endpoints](/concepts/model-serving-endpoint.md). As part of a platform update, Databricks has shifted to a [Provisioned Throughput](/concepts/provisioned-throughput.md) experience for optimized LLM serving, which eliminates the need for customers to choose GPU workload types themselves. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

This documentation has been retired and might not be updated; the products, services, or technologies mentioned are no longer supported. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## What Changed

Provisioned throughput provides a simpler experience for launching optimized LLM serving endpoints. Databricks modified their LLM model serving system so that:

- Scale-out ranges can be configured in LLM-native terms, such as tokens per second instead of concurrency. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]
- Customers no longer need to select GPU workload types themselves. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

New LLM serving endpoints are created with provisioned throughput by default. If you want to continue selecting the GPU workload type, this experience is only supported using the API. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Migration Guidance

The simplest way to migrate an existing endpoint to provisioned throughput is to update the endpoint with a new model version. After selecting a new model version, the UI displays the experience for provisioned throughput, showing tokens-per-second ranges based on Databricks benchmarking for typical use cases. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

Performance with the updated offering is strictly better due to optimization improvements, and the price for the endpoint remains unchanged. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) — The new default serving experience for LLM endpoints.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The underlying API framework for deploying models with provisioned throughput.
- [LLM serving endpoints](/concepts/model-serving-endpoint.md) — The target of this migration; endpoints serving large language models.

## Sources

- migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md

# Citations

1. [migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md](/references/migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws-b1657ebd.md)
