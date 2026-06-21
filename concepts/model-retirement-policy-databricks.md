---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 004d1437a3278c8c426be0fc920596657ee461a060711858ee1d054a37552b5b
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-retirement-policy-databricks
    - MRP(
    - Model Retirement Policy
    - Model retirement policy
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Model Retirement Policy (Databricks)
description: Databricks' official policy for notifying customers, managing transitions, and retiring deprecated generative AI models across Foundation Model API offerings.
tags:
  - databricks
  - model-lifecycle
  - retirement-policy
timestamp: "2026-06-19T10:42:53.765Z"
---

# Model Retirement Policy (Databricks)

**Model Retirement Policy (Databricks)** defines the process and timelines by which Databricks notifies customers when a supported generative AI model is scheduled for retirement, what happens during the transition period, and what to expect on the retirement date. The policy applies to Foundation Model APIs pay-per-token, Foundation Model APIs provisioned throughput, and Foundation Model Fine-tuning offerings. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Purpose

Databricks may update supported models or retire older models to continue supporting the most state-of-the-art models. The retirement policy ensures customers receive adequate notice and transition time before a model is removed from service. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Policy by Offering

The retirement policy timelines differ by offering and model category. The policies only impact supported chat and completion models for the Foundation Model APIs pay-per-token and Foundation Model Fine-tuning offerings. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Foundation Model APIs Pay-per-Token

The retirement policy for pay-per-token models follows specific notification and transition timelines, though the exact durations are referenced in the source table rather than enumerated in the narrative text. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Foundation Model APIs Provisioned Throughput

Provisioned throughput models have their own retirement policy timeline, summarized in the corresponding source table. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Foundation Model Fine-tuning

Foundation Model Fine-tuning has a separate retirement policy with its own notification and transition period, detailed in the source table. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Partner Model Retirement Policy

Partner models are models provided by third-party partners — specifically OpenAI, Anthropic, and Google — that are available through Foundation Model APIs. For these models, Databricks generally follows the same deprecation timelines and policies as described for provisioned throughput and pay-per-token models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

However, retirement dates provided by partners may be shorter than the transition periods published by Databricks. In these cases, Databricks attempts to bridge the gap by temporarily redirecting models to a similar version, so customers receive the full transition time. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

For example, if a pay-per-token model deprecation is announced with one month's lead time instead of three, Databricks redirects the model for an additional two months to prevent immediate breakage and allow time for migration. Queries fail at the end of the full three-month period. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

This redirection can only occur if the replacement model has the same price and is backwards compatible. The replacement model is usually an incremental model version, like 3.0 versus 3.1. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Updates

Databricks may ship incremental model updates to deliver optimizations. When a model is updated, the endpoint URL remains the same, but the model ID in the response object changes to reflect the date of the update. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on 3/4/2024, the model name in the response object updates to `meta-llama/Meta-Llama-3.3-70B-030424`. Databricks maintains a version history of the updates that customers can refer to. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Retired Models

Databricks publishes tables of current and upcoming model retirements for each offering, including retirement dates and recommended replacement models.

### Foundation Model APIs Pay-per-Token Retirements

The retirement table shows model retirements, their retirement dates, and recommended replacement models. Databricks recommends migrating applications to use replacement models before the indicated retirement date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

If you require long-term support for a specific model version, Databricks recommends using Foundation Model APIs provisioned throughput for serving workloads. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Foundation Model APIs Provisioned Throughput Retirements

The retirement table shows model family retirements, their retirement dates, and recommended replacement models. Databricks recommends migrating applications to use replacement models before the indicated retirement date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Foundation Model Fine-tuning Retirements

The retirement table shows retired model families, their retirement dates, and recommended replacement model families. Databricks recommends migrating applications to use replacement models before the indicated retirement date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Identifying Workloads Using Retired Models

Use the following query against system tables to find workloads that are using deprecated models and identify their owners: ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

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

## Related Concepts

- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md)
- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md)
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md)
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- System Tables for Model Monitoring
- GenAI Agent Migration Strategy

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
