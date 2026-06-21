---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b98238062ff000065576555c27e9ce9f8056985ed7f97434deb31ac4e35b3fff
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-redirection-mechanism
    - MRM
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Model Redirection Mechanism
description: Databricks practice of temporarily redirecting requests from a retired partner model to a similar replacement model to ensure customers receive full transition time.
tags:
  - databricks
  - model-lifecycle
  - migration
timestamp: "2026-06-18T12:28:44.514Z"
---

# Model Redirection Mechanism

The **Model Redirection Mechanism** is a feature of Databricks' Foundation Model APIs that temporarily redirects queries from a retiring partner model to a similar, backwards-compatible replacement model when the partner's deprecation timeline is shorter than Databricks' standard transition period. This mechanism ensures customers receive the full transition window for migration even when third-party providers announce retirements with minimal notice.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Overview

When a partner model (provided by third-party partners such as OpenAI, Anthropic, or Google) is set for retirement, Databricks generally follows the same deprecation timelines and policies as described for provisioned throughput and pay-per-token models. However, retirement dates provided by partners might be shorter than the transition periods published by Databricks.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

In these cases, the Model Redirection Mechanism bridges the gap by temporarily redirecting queries from the retiring model to a similar version. This prevents immediate breakage and allows customers additional time to migrate their applications to an alternative model.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Conditions for Redirection

The model redirection mechanism can only occur under specific conditions:

- **Same pricing**: The replacement model must have the same price as the retiring model.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Backwards compatibility**: The replacement model must be backwards compatible with the retiring model.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Incremental version**: The replacement model is usually an incremental model version, such as version 3.0 replaced by version 3.1.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Duration and Behavior

If a pay-per-token model deprecation is announced with only one month's lead time instead of the standard three months, Databricks redirects the retiring model to a compatible replacement for an additional two months. This provides customers with the full three-month transition period.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

Queries continue to succeed during the redirection period. However, queries fail at the end of the full transition period if the customer has not migrated to a supported replacement model.^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service that hosts the models subject to the redirection mechanism
- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md) — Offering where the redirection mechanism applies
- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md) — Offering for which Databricks generally follows similar deprecation policies
- [Partner Model Retirement Policy](/concepts/partner-model-retirement-policy.md) — The broader policy for model retirements from third-party providers
- [Model Retirement Policy](/concepts/model-retirement-policy-databricks.md) — The overall policy governing model deprecations and transitions
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) — Another offering subject to model maintenance policies

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
