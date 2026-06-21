---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ecb616529f2e30654f0da9eedbffc157addd821bd5c2c717395c61c3191eb705
  pageDirectory: concepts
  sources:
    - migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migrating-llm-serving-endpoints
    - MLSE
    - Creating Serving Endpoints
  citations:
    - file: migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
title: Migrating LLM Serving Endpoints
description: The process of updating existing Databricks LLM serving endpoints to use provisioned throughput by selecting a new model version, which automatically switches the UI to the new experience.
tags:
  - migration
  - llm-serving
  - databricks
timestamp: "2026-06-19T19:34:08.881Z"
---

# Migrating LLM Serving Endpoints

**Migrating LLM Serving Endpoints** refers to the process of transitioning existing optimized large language model (LLM) serving endpoints from the legacy GPU workload type configuration to the [Provisioned Throughput](/concepts/provisioned-throughput.md) experience available through [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks. Provisioned throughput simplifies endpoint management by expressing scale-out in LLM-native terms (tokens per second) and removing the need for users to manually select GPU workload types. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## What’s changing

With the introduction of provisioned throughput, Databricks has modified the LLM model serving system in two key ways:

- **Scale-out ranges can now be configured in tokens per second** instead of concurrency, aligning with how LLM workloads are typically measured. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]
- **Customers no longer need to select GPU workload types** themselves; the system handles GPU selection automatically. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

New LLM serving endpoints are created with provisioned throughput by default. If a user still wants to manually select the GPU workload type, that experience is only supported via the API. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Migration steps

The simplest way to migrate an existing endpoint to provisioned throughput is to update the endpoint with a new model version. After selecting a new model version, the UI automatically displays the provisioned throughput experience, showing tokens per second ranges based on Databricks benchmarking for typical use cases. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

The UI presents a graph or slider (see documentation) that lets the user choose a tokens-per-second range. Performance with the updated offering is strictly better due to optimization improvements, and the price for the endpoint remains unchanged. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Results and support

After migration, the endpoint continues to serve requests with improved performance at the same cost. For product feedback or concerns, users can contact `model-serving-feedback@databricks.com`. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Related concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) – The new serving model discussed in this migration.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The underlying API layer for provisioned throughput endpoints.
- [LLM serving endpoints](/concepts/model-serving-endpoint.md) – The endpoints being migrated.
- [Tokens per second](/concepts/tokens-per-second-as-a-scaling-metric.md) – The LLM-native throughput metric used in the new configuration.
- GPU workload type – The legacy configuration option that is no longer required.

## Sources

- migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md

# Citations

1. [migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md](/references/migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws-b1657ebd.md)
