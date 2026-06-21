---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 611f6313bc294ceee154dd7e08be63538616ba9873b449290b29a3a218adb99a
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incremental-model-updates-and-version-history
    - Version History and Incremental Model Updates
    - IMUAVH
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Incremental Model Updates and Version History
description: Databricks ships minor model updates with versioned model IDs appended with dates, while keeping endpoint URLs unchanged.
tags:
  - databricks
  - model-lifecycle
  - versioning
timestamp: "2026-06-18T12:28:43.434Z"
---

# Incremental Model Updates and Version History

**Incremental Model Updates and Version History** describes how Databricks ships minor improvements to supported generative AI models without breaking existing integrations. When an incremental update is released, the endpoint URL remains unchanged, but the model ID in the response object changes to reflect the date of the update. Databricks maintains a version history of these updates for reference. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## How Updates Work

Databricks can ship incremental model updates to deliver optimizations, such as performance improvements or bug fixes, while preserving backward compatibility. The update mechanism ensures that applications using the same endpoint URL continue to function without modification. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, the model name in the response object updates to `meta-llama/Meta-Llama-3.3-70B-030424`. This naming convention allows users to identify which version of the model handled a given request. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Version History

Databricks maintains a version history of the updates that users can refer to, enabling them to track which incremental versions have been deployed and when the changes occurred. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Role in Partner Model Retirements

During a partner model deprecation (for example, from OpenAI, Anthropic, or Google), Databricks may temporarily redirect traffic from the retiring model to a replacement model if that replacement has the same price and is backwards compatible. The replacement model is usually an incremental model version, such as version 3.0 versus 3.1. This redirection allows customers to receive the full transition period even when the partner’s retirement timeline is shorter than Databricks’ standard policy. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md) — The offering where incremental updates apply to supported chat and completion models.
- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md) — The offering for reserved throughput that may also receive incremental updates.
- [Model Retirement Policy](/concepts/model-retirement-policy-databricks.md) — The policy that governs model deprecation and includes transition periods.
- [Partner Model Retirement Policy](/concepts/partner-model-retirement-policy.md) — The specific rules for third-party models, which may involve incremental version redirects.
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) — The fine-tuning offering that also follows the model retirement and update policies.

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
