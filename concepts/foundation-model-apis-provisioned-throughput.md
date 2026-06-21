---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8332473a4ae7912b0602df9f8c45772fcb0278d1ab76b04b464fdbcadb8e247f
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis-provisioned-throughput
    - FMAPT
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Foundation Model APIs Provisioned Throughput
description: A Databricks offering for dedicated model serving capacity with provisioned throughput, governed by a specific model retirement policy with defined transition periods.
tags:
  - databricks
  - foundation-model-apis
  - provisioned-throughput
timestamp: "2026-06-19T10:43:15.978Z"
---

# Foundation Model APIs Provisioned Throughput

**Foundation Model APIs Provisioned Throughput** is a Databricks offering that provides dedicated, reserved capacity for serving foundation models in production environments. Unlike pay-per-token serving, provisioned throughput guarantees consistent performance and availability for high-volume or latency-sensitive workloads.

## Overview

Provisioned throughput allocates dedicated compute resources to serve foundation models through Databricks [Foundation Model APIs](/wiki/foundation-model-apis). This offering is designed for production workloads that require predictable performance, low latency, and guaranteed capacity. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Key Features

### Guaranteed Capacity

Provisioned throughput reserves dedicated GPU resources for model serving, eliminating contention with other workloads. This ensures consistent response times and throughput regardless of overall system load. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Long-Term Model Support

For organizations that require stability beyond standard model retirement timelines, Databricks recommends using provisioned throughput. This offering provides extended support for specific model versions, allowing teams to maintain consistency in their production applications. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Predictable Performance

With dedicated infrastructure, provisioned throughput eliminates the variability associated with shared serving resources. This makes it suitable for applications with strict latency requirements or high-volume traffic patterns. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Retirement Policy

Databricks publishes specific retirement timelines for models available through provisioned throughput. The policy includes notification periods, transition windows, and recommended replacement models to facilitate migration planning. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Policy Overview

The model retirement policy for provisioned throughput follows a structured timeline:

| Phase | Duration | Description |
|-------|----------|-------------|
| Announcement | At retirement date announcement | Databricks notifies customers of upcoming model retirement |
| Transition Period | As specified in retirement schedule | Models remain operational during this window |
| Retirement Date | End of transition period | Model is no longer available through provisioned throughput |

### Partner Models

For partner models from OpenAI, Anthropic, and Google available through provisioned throughput, Databricks generally follows the same retirement timelines. However, when partners provide shorter deprecation notices than Databricks' standard transition periods, Databricks may temporarily redirect models to a similar, backwards-compatible version to maintain service continuity. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Retired Models and Migration

### Finding Affected Workloads

To identify workloads using models scheduled for retirement, Databricks provides system tables that track endpoint usage and served entities. The following query helps identify affected endpoints and their owners: ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

```sql
SELECT
  eu.requester,
  se.endpoint_name,
  se.entity_name,
  COUNT(*) AS request_count,
  SUM(eu.input_token_count) AS total_input_tokens,
  SUM(eu.output_token_count) AS total_output_tokens,
  MIN(eu.request_time) AS first_request,
  MAX(eu.request_time) AS last_request
FROM system.serving.endpoint_usage eu
JOIN system.serving.served_entities se
  ON eu.served_entity_id = se.served_entity_id
WHERE LOWER(se.entity_name) LIKE '%<retired-model-name>%'
GROUP BY eu.requester, se.endpoint_name, se.entity_name
ORDER BY request_count DESC
```

### Replacement Models

For each retired model, Databricks publishes a recommended replacement model. Teams should migrate their applications to the replacement model before the retirement date to avoid service disruption. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Updates

When Databricks ships incremental model updates to provisioned throughput endpoints, the endpoint URL remains unchanged. However, the model ID in the response object updates to include the date of the update. For example, an update to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, would result in the model ID changing to `meta-llama/Meta-Llama-3.3-70B-030424`. Databricks maintains a version history of all updates for reference. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Use Cases

- **Production workloads** requiring guaranteed availability and consistent response times
- **High-volume applications** with predictable traffic patterns that benefit from reserved capacity
- **Latency-sensitive services** where response time variability must be minimized
- **Compliance-focused deployments** requiring long-term support for specific model versions
- **Cost optimization** for workloads with sustained usage that benefit from reserved pricing over pay-per-token

## Comparison with Pay-Per-Token

| Feature | Provisioned Throughput | Pay-Per-Token |
|---------|----------------------|---------------|
| Capacity | Dedicated, reserved | Shared, on-demand |
| Performance | Consistent, predictable | Variable based on demand |
| Cost | Fixed reservation cost plus usage | Per-token pricing |
| Model Support | Extended lifecycle | Standard lifecycle |
| Use Case | Production, high-volume | Development, low-volume |

## Related Concepts

- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md) — On-demand model serving with per-token pricing
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) — Customizing models for specific use cases
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — Overview of serving infrastructure
- GPU Scheduling — Resource allocation for model serving
- Generative AI Models Maintenance Policy — Detailed retirement schedules and update notifications

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
