---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b273ecfb7bd94b94f8e2d1102928e44c5b81ae4861b47834c215bb3d5744ad5
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retired-model-discovery-query
    - RMDQ
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Retired Model Discovery Query
description: A SQL query against Databricks system tables (system.serving) to find workloads using deprecated models and identify the owners for migration planning.
tags:
  - databricks
  - monitoring
  - sql
timestamp: "2026-06-19T10:43:49.064Z"
---

# Retired Model Discovery Query

**Retired Model Discovery Query** is a SQL query that runs against Databricks system tables to identify workloads using deprecated or retired models in Foundation Model API serving endpoints. It enables teams to find affected endpoints, their users, and usage patterns to plan migrations before retirement dates. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Overview

When model retirement dates approach, administrators and platform teams need to identify all serving workloads that reference a soon-to-be-retired model. The Retired Model Discovery Query joins usage logs with served entity metadata to produce a comprehensive view of which users and endpoints are still invoking a deprecated model, how heavily it is being used, and when the last request occurred. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Query Definition

The query uses the `system.serving.endpoint_usage` and `system.serving.served_entities` tables, which are part of the Databricks system schema. It filters on a pattern match against the model name and aggregates usage statistics per requester and endpoint. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

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

Replace `<retired-model-name>` with the name of the retired model you are searching for (e.g., `llama-2-70b-chat`). ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Output Columns

| Column | Description |
|--------|-------------|
| `requester` | The user or service principal that made the requests |
| `endpoint_name` | The serving endpoint that hosts the retired model |
| `entity_name` | The specific model name as served by the endpoint |
| `request_count` | Total number of requests made by this requester to this endpoint |
| `total_input_tokens` | Sum of input tokens consumed by this requester |
| `total_output_tokens` | Sum of output tokens generated for this requester |
| `first_request` | Timestamp of the earliest request seen |
| `last_request` | Timestamp of the most recent request |

## Use Cases

### Migration Planning

The query identifies which endpoints and users are still relying on a retiring model. Teams can contact those users directly with migration instructions and recommended replacement models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Usage Prioritization

By sorting by `request_count` descending, teams can prioritize high-traffic endpoints for migration first, reducing the risk of production impact on the retirement date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Finding Dormant Workloads

The `last_request` timestamp helps distinguish between actively used endpoints and those that were created for testing or are no longer in use. Dormant endpoints connected to retired models can be cleaned up without migration. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Model Retirement Policy](/concepts/model-retirement-policy-databricks.md) — Timelines and notice periods for model deprecation
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Serving endpoints that host chat and completion models
- Serving Endpoint Monitoring — Observability for deployed models
- System Tables — The underlying schema that powers usage analytics
- [Provisioned Throughput Models](/concepts/provisioned-throughput-mode.md) — Alternative offering for long-term model version support
- [Partner Model Retirement Policy](/concepts/partner-model-retirement-policy.md) — Special rules for third-party models from OpenAI, Anthropic, and Google

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
