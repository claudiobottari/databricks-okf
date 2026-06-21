---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd141c1bdd95cc59f38978d7fe19e1d12f11166c7cc959dd78ead9cbc3fc4af7
  pageDirectory: concepts
  sources:
    - migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tokens-per-second-as-a-scaling-metric
    - TPSAASM
    - Tokens per Second
    - Tokens per second
  citations:
    - file: migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
title: Tokens Per Second as a Scaling Metric
description: Using tokens per second (instead of concurrency) as the unit for configuring scale-out ranges for LLM serving endpoints, providing LLM-native scaling semantics.
tags:
  - scaling
  - llm
  - performance
timestamp: "2026-06-19T19:34:07.032Z"
---

# Tokens Per Second as a Scaling Metric

**Tokens per second** is a scaling metric used to configure the scale-out range of optimized [LLM serving endpoint](/concepts/model-serving-endpoint.md)s on Databricks, replacing the previous concurrency-based model. It is part of the [Provisioned Throughput](/concepts/provisioned-throughput.md) experience provided by [Foundation Model APIs](/concepts/foundation-model-apis.md).

## Overview

When creating or updating an LLM serving endpoint, the scale-out range can now be specified in terms of tokens per second rather than concurrency. This metric is more natural for LLM workloads because it directly reflects the throughput of generated or processed tokens, which is the primary performance characteristic that matters to applications and users. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

The tokens per second metric is derived from Databricks benchmarking for typical use cases, so the UI shows recommended ranges based on the selected model version. This simplifies endpoint configuration: customers no longer need to choose GPU workload types or estimate concurrency levels. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Why Tokens Per Second?

Using tokens per second as the scaling metric aligns the infrastructure configuration with the business metric that matters most to LLM applications — the rate of token generation. Concurrency, while relevant to traditional request-based serving, is harder to translate into LLM performance because different prompts and generation settings produce widely varying token counts per request. Tokens per second provides a more direct and predictable scaling signal. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## How It Works

When you update an existing endpoint or create a new one, the UI presents a tokens‑per‑second range based on Databricks benchmarks for the selected model. You can set the minimum and maximum tokens per second that the endpoint should support, and Databricks automatically provisions the underlying GPU resources to meet that target. This replaces the previous workflow where users had to manually select GPU workload types and concurrency settings. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

For migration, updating an endpoint with a new model version automatically presents the provisioned throughput UI, making tokens per second the default scaling metric for all new LLM serving endpoints. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) – The overall mechanism for reserving compute capacity for LLM serving.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The API layer that exposes provisioned throughput endpoints.
- [LLM serving endpoint](/concepts/model-serving-endpoint.md) – The managed endpoint that hosts a large language model.
- Concurrency – The older scaling metric, now replaced by tokens per second.
- GPU workload type – The previous configuration option that is no longer needed.
- Tokens – The fundamental unit of input and output for large language models.
- [Serving optimization](/concepts/client-side-serving-optimization.md) – Techniques for improving LLM serving performance.

## Sources

- migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md

# Citations

1. [migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md](/references/migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws-b1657ebd.md)
