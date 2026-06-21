---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5cb47caf9f21245e0319645e358d0d678c5441b2dcf196f6b3322ea4ad5efcd2
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-retirement-policy
    - DMRP
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Databricks Model Retirement Policy
description: The overall policy governing how and when Databricks notifies customers about model retirements, covering transition periods, retirement dates, and migration recommendations.
tags:
  - databricks
  - machine-learning
  - model-lifecycle
  - retirement-policy
timestamp: "2026-06-19T18:57:45.005Z"
---

# Databricks Model Retirement Policy

The **Databricks Model Retirement Policy** defines how Databricks notifies customers when a supported model is set for retirement, what happens during the transition period, and what to expect on the retirement date. The policy applies to models offered through [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md), [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md), and [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md). In order to continue supporting the most state-of-the-art models, Databricks might update supported models or retire older models for these offerings. Timelines differ by offering and model category. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Foundation Model APIs Pay-Per-Token

The retirement policy for pay-per-token serving workloads follows timelines summarized in the official Databricks documentation. Customers are expected to migrate to recommended replacement models before the indicated retirement date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Foundation Model APIs Provisioned Throughput

The retirement policy for provisioned throughput models outlines transition periods for model family retirements and recommends replacement model families. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Partner Model Retirement Policy

Partner models are models provided by third-party partners—specifically OpenAI, Anthropic, and Google—that are available through Foundation Model APIs. For these models, Databricks generally follows the same deprecation timelines and policies as described for provisioned throughput and pay-per-token models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

However, retirement dates provided by partners might be shorter than the transition periods published by Databricks. In these cases, Databricks attempts to bridge the gap by temporarily redirecting models to a similar version so customers receive the full transition time. For example, if a pay-per-token model deprecation is announced with one month's lead time instead of three, Databricks redirects the model for an additional two months to prevent immediate breakage and allow time for migration. Queries fail at the end of the full three-month period. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

This redirection can only occur if the replacement model has the same price and is backwards compatible. The replacement model is usually an incremental model version, like 3.0 versus 3.1. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Foundation Model Fine-Tuning

The retirement policy for Foundation Model Fine-tuning follows timelines summarized in the official Databricks documentation. Customers should migrate workloads to recommended replacement model families before the indicated retirement date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Updates

Databricks might ship incremental model updates to deliver optimizations. When a model is updated, the endpoint URL remains the same, but the model ID in the response object changes to reflect the date of the update. For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, the model name in the response object updates to `meta-llama/Meta-Llama-3.3-70B-030424`. Databricks maintains a version history of these updates. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Retired Models

Databricks publishes tables showing current and upcoming model retirements for each offering:

- **Foundation Model APIs pay-per-token**: Lists retirement dates and recommended replacement models.
- **Foundation Model APIs provisioned throughput**: Shows model family retirements with replacement families.
- **Foundation Model Fine-tuning**: Shows retired model families and recommended replacements.

If you require long-term support for a specific model version, Databricks recommends using [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md) for serving workloads. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Finding Workloads That Use Retired Models

Databricks provides a SQL query to find workloads using deprecated models and identify their owners. Use the `system.serving.endpoint_usage` and `system.serving.served_entities` tables:

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

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Model Serving](/concepts/model-serving.md)
- [Model Fine-tuning](/concepts/multi-node-llm-fine-tuning-with-fsdp.md)
- [System Tables for ML](/concepts/mlflow-system-tables.md)

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
