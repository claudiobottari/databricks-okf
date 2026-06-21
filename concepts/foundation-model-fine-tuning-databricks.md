---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c992b7dfa3788d3917310ff376aa5d5d2baa6ad1130dee18a9b50b5f54445bc6
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-fine-tuning-databricks
    - FMF(
    - Foundation Model Fine-tuning
    - Foundation Model Fine‑tuning
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Foundation Model Fine-tuning (Databricks)
description: A Databricks offering for fine-tuning foundation models, governed by a specific model retirement policy with defined transition periods and recommended replacement models.
tags:
  - databricks
  - fine-tuning
  - model-training
timestamp: "2026-06-19T10:43:32.838Z"
---

# Foundation Model Fine-tuning (Databricks)

**Foundation Model Fine-tuning** is a managed offering within the Databricks platform that allows users to fine-tune large language models on custom data. It is part of Databricks’ broader [Foundation Model APIs](/concepts/foundation-model-apis.md) suite, which also includes pay-per-token and provisioned throughput inference endpoints. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Retirement Policy

Databricks may retire older models from the Foundation Model Fine-tuning offering in order to support more state-of-the-art models. The retirement policy for fine-tuning follows the same structure as other offerings but has a specific transition timeline. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

The fine-tuning retirement policy applies only to supported chat and completion models. When a model is scheduled for retirement, Databricks notifies users and provides a transition period. After the retirement date, fine-tuning jobs using the retired model may fail. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

For partner models (from OpenAI, Anthropic, Google) available through Foundation Model APIs, Databricks generally follows the same deprecation policy as for other models. If a partner’s own retirement date is shorter than Databricks’ standard transition period, Databricks may temporarily redirect the model to a similar version to give customers the full transition time. This redirection is only possible if the replacement model has the same price and is backward compatible (typically an incremental version). ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Updates

Databricks may ship incremental model updates to deliver optimizations. When a fine-tuning model is updated, the endpoint URL remains the same, but the model ID in the response object changes to reflect the date of the update. For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, the model name becomes `meta-llama/Meta-Llama-3.3-70B-030424`. Databricks maintains a version history of these updates. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Retired Models for Fine-Tuning

Databricks publishes a table of retired model families and their retirement dates, along with recommended replacement model families. Users should migrate their fine-tuning workloads to the recommended replacement models before the indicated retirement date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Finding Workloads That Use Retired Models

To identify tasks that rely on a retired model, use the following SQL query against the system catalog. It retrieves endpoint usage records and matching served entity names for a given retired model name: ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

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

Replace `<retired-model-name>` with the name of the model you are checking (for example, `meta-llama`). ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md)
- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md)
- [Model retirement policy](/concepts/model-retirement-policy-databricks.md)
- [Partner Model Retirement Policy](/concepts/partner-model-retirement-policy.md)
- [System tables for serving monitoring](/concepts/databricks-model-serving-monitoring.md)

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
