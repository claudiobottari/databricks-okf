---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 261b3dac93a1d3b7b5cd9ff98c29df6902e7126655d3b91026ebf2d3e1fcdc0c
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-fine-tuning-retirement-policy
    - FMFRP
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Foundation Model Fine-tuning Retirement Policy
description: The specific model retirement timelines, migration windows, and replacement recommendations for Databricks' Foundation Model Fine-tuning offering.
tags:
  - databricks
  - fine-tuning
  - model-lifecycle
  - retirement-policy
timestamp: "2026-06-19T18:58:23.411Z"
---

# Foundation Model Fine-tuning Retirement Policy

The **Foundation Model Fine-tuning Retirement Policy** governs how Databricks handles the deprecation and retirement of models used through the [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) offering. This policy ensures customers have adequate transition time when a model is removed from service and provides guidance on migration to recommended replacement models.

## Policy Overview

Databricks may retire older models to continue supporting the most state-of-the-art models. The retirement policy applies to chat and completion models within the Foundation Model Fine-tuning offering and follows a structured timeline with defined phases. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Retirement Timeline

The model retirement policy for Foundation Model Fine-tuning follows a specific timeline with clear phases and milestones:

- **Announcement date**: The date when retirement is publicly announced
- **Transition period begins**: The start of the transition period, during which the model remains available
- **Retirement date**: The date when the model is fully retired and no longer available for use

During the transition period, customers can continue to use the model and should plan their migration to recommended replacement models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Retired Models

For Foundation Model Fine-tuning, the following model families have been retired or are scheduled for retirement:

| Model | Retirement Date | Recommended Replacement |
|-------|----------------|------------------------|
| `dolly-v2-12b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `falcon-7b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `falcon-40b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `MPT-7b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `MPT-30b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `Llama-2-7b` | May 1, 2025 | `meta-llama/Meta-Llama-3.1-8B` |
| `Llama-2-13b` | May 1, 2025 | `meta-llama/Meta-Llama-3.1-8B` |
| `Llama-2-70b` | September 30, 2025 | `meta-llama/Meta-Llama-3.1-70B` |

^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Updates

Databricks may ship incremental model updates for optimization purposes. When a model is updated:
- The endpoint URL remains the same
- The model ID in the response object changes to reflect the update date

For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, the model name updates to `meta-llama/Meta-Llama-3.3-70B-030424`. Databricks maintains a version history that customers can reference. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Partner Model Considerations

For partner models (from OpenAI, Anthropic, Google), Databricks generally follows the same retirement policies as described for other models. However, if partners provide shorter retirement timelines, Databricks may redirect the model to a similar version to maintain the full transition period. This redirection is only possible if the replacement model has the same price and is backwards compatible. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md)
- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md)
- Model Retirement
- Model Versioning

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

## Appendix: Full Retirement Details

The following table provides complete details for all Foundation Model Fine-tuning retirements:

| Model Family | Retirement Date | Recommended Replacement |
|-------------|----------------|------------------------|
| `dolly-v2-12b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `falcon-7b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `falcon-40b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `MPT-7b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `MPT-30b` | March 15, 2024 | `meta-llama/Meta-Llama-3.1-8B` |
| `Llama-2-7b` | May 1, 2025 | `meta-llama/Meta-Llama-3.1-8B` |
| `Llama-2-13b` | May 1, 2025 | `meta-llama/Meta-Llama-3.1-8B` |
| `Llama-2-70b` | September 30, 2025 | `meta-llama/Meta-Llama-3.1-70B` |

^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Finding Affected Workloads

To identify workloads using retired models, use the following query against the system catalog:

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

This query identifies usage patterns and helps determine migration needs. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Key Considerations

- The retirement policy only applies to supported chat and completion models
- Migration should be planned before the retirement date to avoid service disruption
- For long-term support of specific model versions, provisioned throughput is recommended
- The model ID in responses reflects the update date for version tracking

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
