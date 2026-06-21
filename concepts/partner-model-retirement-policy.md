---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b4799c042c147efc6830550ac30ae6b59e0c9022521a18ee8a27ba1428bc7cd1
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partner-model-retirement-policy
    - PMRP
    - Model Retirement Policy
    - Model retirement policy
    - Retired Models Policy
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Partner Model Retirement Policy
description: Special retirement policy for third-party models from OpenAI, Anthropic, and Google available through Databricks Foundation Model APIs, where Databricks may redirect models to bridge partner-led deprecation gaps.
tags:
  - databricks
  - partner-models
  - retirement-policy
timestamp: "2026-06-19T10:43:15.417Z"
---

# Partner Model Retirement Policy

**Partner Model Retirement Policy** describes how Databricks handles the retirement of third-party models provided by OpenAI, Anthropic, and Google that are available through Foundation Model APIs. Databricks generally follows the same deprecation timelines and policies for partner models as for provisioned throughput and pay-per-token models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Partner Model Retirement Timeline

Retirement dates provided by partners might be shorter than the transition periods published by Databricks. In these cases, Databricks attempts to bridge the gap by temporarily redirecting models to a similar version so customers receive the full transition time. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Example Scenario

If a pay-per-token model deprecation is announced with one month's lead time instead of three, Databricks redirects the model for an additional two months to prevent immediate breakage and allow time for migration. Queries fail at the end of the full three-month period. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Redirection Limitations

Redirection to a replacement model can only occur if the replacement model has the same price and is backwards compatible. The replacement model is usually an incremental model version, such as version 3.0 versus 3.1. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Migration Recommendations

Databricks recommends that you migrate your applications to use replacement models before the indicated retirement date. If you require long-term support for a specific model version, Databricks recommends using Foundation Model APIs provisioned throughput for your serving workloads. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Detecting Workloads Using Retired Models

Use the following query to find workloads that are using deprecated models and identify their owners: ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

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

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure that hosts partner models
- [Model Retirement Policy](/concepts/model-retirement-policy-databricks.md) — The broader policy applicable to all models
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Offering that provides long-term model support
- [Pay-per-Token](/concepts/pay-per-token-serving-mode.md) — Consumption-based model serving offering
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) — Model customization offering with its own retirement policy

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
