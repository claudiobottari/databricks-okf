---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de3f94b92f6339a39b4b361315db626c41b65b414e4466cfbbc18766319c077f
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retired-model-discovery-via-system-tables
    - RMDVST
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Retired Model Discovery via System Tables
description: SQL query pattern for identifying workloads using retired models by querying Databricks system tables endpoint_usage and served_entities.
tags:
  - databricks
  - monitoring
  - system-tables
timestamp: "2026-06-18T12:28:51.380Z"
---

# Retired Model Discovery via System Tables

**Retired Model Discovery via System Tables** refers to the process of identifying workloads that use deprecated or retired models by querying Databricks system tables. This approach enables administrators and developers to find affected endpoints, understand usage patterns, and plan migrations before model retirement dates.

## Overview

When a model is scheduled for retirement, Databricks provides a query-based method to discover which serving endpoints are still using that model. By joining relevant system tables, you can identify the users, endpoints, and usage metrics associated with deprecated models.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Discovery Query

The following SQL query retrieves workload information for models matching a retired model name. Replace `<retired-model-name>` with the specific model name you want to investigate:

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
ORDER BY request_count DESC;
```

^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Query Output

The query returns the following information for each affected workload:

| Column | Description |
|--------|-------------|
| `requester` | The user or service principal that invoked the endpoint |
| `endpoint_name` | The name of the serving endpoint |
| `entity_name` | The name of the served model entity |
| `request_count` | Total number of requests made to the retired model |
| `total_input_tokens` | Total input tokens processed |
| `total_output_tokens` | Total output tokens generated |
| `first_request` | Timestamp of the first recorded request |
| `last_request` | Timestamp of the most recent request |

## Required Tables

The query uses the following system tables:

- **`system.serving.endpoint_usage`**: Contains usage metrics for model serving endpoints, including request counts, token counts, and timestamps.
- **`system.serving.served_entities`**: Contains information about the model entities served by each endpoint, including entity names.

Both tables are joined on the `served_entity_id` field.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Usage Scenarios

### Pre-Retirement Migration Planning

Before a model's retirement date, run the discovery query to identify all endpoints using the model. Contact the endpoint owners and the users listed in the `requester` column to coordinate migration to the recommended replacement model.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Post-Retirement Verification

After the retirement date has passed, re-run the query to confirm that no workloads are still sending requests to the retired model. A result set with zero rows indicates successful migration.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Usage Auditing

Use the query results to understand adoption patterns and usage volume for specific model versions across your organization. This information can inform decisions about provisioning [Provisioned Throughput](/concepts/provisioned-throughput.md) for long-term support of specific model versions.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Retirement Policy

Databricks maintains a formal retirement policy for [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md), [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md), and [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) offerings. The policy specifies notification timelines, transition periods, and recommended replacement models for each offering.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Partner Models

For models provided by third-party partners (OpenAI, Anthropic, and Google), Databricks generally follows the same deprecation policies. However, partners may provide shorter lead times. In such cases, Databricks may temporarily redirect models to a similar, backwards-compatible version to provide the full transition period. This redirection is possible only when the replacement model has the same price and is backwards compatible.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure for foundation models
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The deployment targets for models
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — A serving option for long-term model support
- [Model Maintenance Policy](/concepts/model-retirement-and-deprecation-policy.md) — The formal policy governing model retirements
- System Tables — The Databricks system tables used for monitoring and auditing
- Serving Endpoint Monitoring — Broader practices for endpoint observability

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
