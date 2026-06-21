---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d8d008f1e7c00c787c4f1248067eb8e08c3a88a33736d29b98ab9070cc8ed84
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workload-discovery-for-deprecated-models
    - WDFDM
    - Find Workloads Using Retired Models
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Workload Discovery for Deprecated Models
description: A SQL-based method to identify workloads, endpoints, and owners still using deprecated or retired models by querying Databricks system tables.
tags:
  - databricks
  - monitoring
  - sql
  - model-governance
timestamp: "2026-06-19T18:58:04.047Z"
---

# Workload Discovery for Deprecated Models

**Workload Discovery for Deprecated Models** refers to the process of identifying serving endpoints and fine-tuning jobs that use models scheduled for retirement or already retired. Databricks provides tools and queries to help administrators locate these workloads, understand their usage patterns, and plan migration to replacement models before the retirement date.

## Overview

When Databricks retires a model from the Foundation Model APIs (pay-per-token or provisioned throughput) or Foundation Model Fine-tuning, existing workloads that reference the retired model will eventually fail. To prevent disruption, administrators should proactively discover which endpoints and users depend on deprecated models and contact the workload owners to schedule migration. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Retirement Policy Context

Databricks publishes retirement dates and recommended replacement models for each offering:

- **Foundation Model APIs pay-per-token** – Models receive a notification period before retirement. Databricks recommends migrating to replacement models before the indicated date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Foundation Model APIs provisioned throughput** – Model families have specified retirement dates with recommended replacement families. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Foundation Model Fine-tuning** – Retired model families have published retirement dates and recommended replacement families. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

For partner models (OpenAI, Anthropic, Google), Databricks generally follows the same deprecation timelines but may redirect to a similar version to bridge shorter partner-provided notice periods. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Discovery Query

Use the following SQL query against the system.serving schema to find workloads that use a retired or deprecated model. Replace `<retired-model-name>` with the name of the model you are investigating (for example, `llama-2-70b-chat`). ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

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

The query returns:

- **requester** – The user or service principal that made requests to the endpoint.
- **endpoint_name** – The name of the serving endpoint.
- **entity_name** – The name of the model or served entity.
- **request_count** – Total number of requests using the retired model.
- **total_input_tokens / total_output_tokens** – Token consumption metrics.
- **first_request / last_request** – Time range of activity, useful for identifying active versus idle workloads.

## Migration Planning

After identifying workloads, Databricks recommends:

1. Contacting the workload owners listed as **requester** in the query results.
2. Reviewing the retired models table for the specific retirement date and recommended replacement model.
3. Migrating applications to the replacement model before the retirement date to avoid service disruption.

For workloads requiring long-term support for a specific model version, consider using [Provisioned Throughput](/concepts/provisioned-throughput.md) offerings instead of pay-per-token. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Pay-per-token and provisioned throughput model serving.
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) – Fine-tuning service for supported model families.
- [Model retirement policy](/concepts/model-retirement-policy-databricks.md) – Notification and transition periods for deprecated models.
- [Partner Model Retirement Policy](/concepts/partner-model-retirement-policy.md) – Deprecation handling for third-party models.
- System tables – System metadata tables including endpoint usage and serving entities.
- Model versioning and updates – How Databricks tracks incremental model updates.

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
