---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20dc88d491b7d00685cd9e1eb9a38571e8fab4cd62a09811081668092b87df79
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incremental-model-updates-databricks
    - IMU(
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Incremental Model Updates (Databricks)
description: Databricks practice of shipping minor model optimizations while keeping the endpoint URL unchanged, with the model ID in the response updated to reflect the date (e.g., 'model-name-030424').
tags:
  - databricks
  - model-versioning
  - api-design
timestamp: "2026-06-19T10:43:21.882Z"
---

# Incremental Model Updates (Databricks)

**Incremental Model Updates** refer to minor, non-breaking improvements shipped to supported models available through the [Foundation Model APIs](/concepts/foundation-model-apis.md). These updates deliver optimizations without changing the endpoint URL, ensuring minimal disruption to production workloads.

## Overview

Databricks periodically ships incremental model updates to improve performance, efficiency, or accuracy of supported generative AI models. When an update is applied, the serving endpoint continues to use the same URL, preserving existing integrations and application code. The only visible change is in the model ID returned in the API response object, which updates to include the date of the update.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Identifying Updated Models

The model ID in the response object follows a consistent naming convention that reflects the update date. For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, the model name in the response object updates to `meta-llama/Meta-Llama-3.3-70B-030424`.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

Databricks maintains a version history of all updates that users can reference to track changes over time.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Scope

Incremental model updates apply to the following offerings:

- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md)
- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md)
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md)

^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Behavior During Updates

The following characteristics define how incremental updates work:

| Aspect | Behavior |
|--------|----------|
| Endpoint URL | Remains unchanged |
| Response model ID | Updates to reflect the date of the change |
| Backward compatibility | Maintained — updates are non-breaking |
| User action required | None for the update itself |
| Version history | Available for reference |

^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Relationship to Model Retirement

Incremental model updates are distinct from [Model Retirement Policy](/concepts/model-retirement-policy-databricks.md). The retirement policy governs when models are fully deprecated and replaced, typically with longer notification periods. Incremental updates are smaller, more frequent improvements that do not trigger the retirement process. For models provided by third-party partners (OpenAI, Anthropic, Google), Databricks may temporarily redirect a retiring model to a similar, updated version to provide additional migration time — this redirection is possible only if the replacement model has the same price and is backward compatible, and is usually an incremental version (e.g., 3.0 versus 3.1).^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Model Retirement Policy](/concepts/model-retirement-policy-databricks.md) – The formal process for deprecating and replacing models
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The serving infrastructure for generative AI models
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) – Customization of base models
- Model Versioning – Tracking model iterations over time
- Backward Compatibility – Ensuring updates do not break existing integrations

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
