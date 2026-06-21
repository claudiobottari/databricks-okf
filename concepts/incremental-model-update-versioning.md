---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b8dc89a364116a1dead6d77913f3cbcfc9d6cfcbfb14cf9637892a9adbc58de
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incremental-model-update-versioning
    - IMUV
    - incremental-model-updates-databricks
    - IMU(
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Incremental Model Update Versioning
description: Databricks' approach to shipping model optimizations where endpoint URLs remain stable but the model ID in responses includes a date stamp reflecting the update.
tags:
  - databricks
  - model-versioning
  - api-design
  - incremental-updates
timestamp: "2026-06-19T18:58:18.168Z"
---

Here is the wiki page for "Incremental Model Update Versioning".

---

## Incremental Model Update Versioning

**Incremental Model Update Versioning** describes the update policy for [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks, where the platform ships minor model improvements (such as performance optimizations or bug fixes) without changing the endpoint URL. Instead, the model identifier in the API response object is updated to reflect the date of the change. This enables backward-compatible updates while providing traceability for each version. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Versioning Format

When an incremental update is shipped, the model name in the response object changes to include a date suffix. The date suffix uses the format `MMDDYY` (month, day, two-digit year). For example, if an update is applied to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, the model name in the response becomes `meta-llama/Meta-Llama-3.3-70B-030424`. This ensures that each update is uniquely identifiable in API responses. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Scope

Incremental model updates apply to supported [Chat and Completion Models](/concepts/chat-completions-api.md) across the following offerings:

- [Foundation Model APIs](/concepts/foundation-model-apis.md) pay-per-token
- [Foundation Model APIs](/concepts/foundation-model-apis.md) provisioned throughput
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md)

For all three offerings, Databricks may ship incremental model updates to deliver optimizations. When a model is updated, the endpoint URL remains unchanged, but the model ID in the response object reflects the update date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Version History

Databricks maintains a version history of all incremental model updates. You can refer to this history to track which version of a model you are using and to verify when an update was applied. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Relationship to Model Retirement Policy

Incremental model updates are distinct from Model Retirement events. While incremental updates deliver minor improvements while keeping the same endpoint URL and pricing, retirement events indicate that a model family will be removed from service entirely, with a recommended replacement model. For Partner Models, Databricks may apply a redirection to a similar incremental version (e.g., 3.0 versus 3.1) to bridge shorter retirement timelines. Queries fail only at the end of the full transition period. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The serving infrastructure for chat, completion, and fine-tuning models.
- Model Retirement – The policy for removing entire model families from service.
- [Chat and Completion Models](/concepts/chat-completions-api.md) – The set of models to which the update policy applies.
- [Partner Model Retirement Policy](/concepts/partner-model-retirement-policy.md) – Special handling for partner model retirements with shorter lead times.

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
