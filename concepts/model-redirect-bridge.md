---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e0aabd496fbba0f582ccf1f61d0ba054306951c9694bfb7f3551c2826aa87a6
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-redirect-bridge
    - MRB
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Model Redirect Bridge
description: A Databricks technique where a retiring model is temporarily redirected to a compatible replacement (same price, backwards-compatible) to give customers the full transition period even when a partner's retirement timeline is shorter than Databricks' standard.
tags:
  - databricks
  - model-migration
  - backward-compatibility
timestamp: "2026-06-19T10:43:06.180Z"
---

---
title: Model Redirect Bridge
summary: A mechanism used by Databricks to temporarily redirect a deprecated partner model to a similar version, ensuring customers receive the full standard transition period even when the partner provides shorter deprecation notice.
sources:
  - generative-ai-models-maintenance-policy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:13:15.210Z"
updatedAt: "2026-06-18T08:13:15.210Z"
tags:
  - databricks
  - model-retirement
  - partner-models
  - migration
  - foundation-model-apis
aliases:
  - model-redirect-bridge
  - MRB
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Model Redirect Bridge

The **Model Redirect Bridge** is a mechanism employed by Databricks to mitigate the impact of short deprecation windows for partner models available through [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md) and [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md). When a partner — such as OpenAI, Anthropic, or Google — announces a model retirement with a transition period shorter than Databricks's standard policy (typically three months for pay-per-token and six months for provisioned throughput), Databricks attempts to "bridge the gap" by temporarily redirecting queries from the deprecated model to a similar, backwards-compatible version. This redirection allows customers to continue receiving service for the full standard transition period, preventing immediate breakage and providing time to migrate. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## How It Works

1. **Partner announces deprecation** – The third-party provider announces an end-of-life date for a specific model that is earlier than Databricks's normal transition timeline.
2. **Databricks identifies a replacement** – A replacement model, usually an incremental version (e.g., version 3.1 replacing version 3.0), is selected that has the same pricing and is backwards compatible.
3. **Traffic is redirected** – Instead of failing queries immediately, Databricks routes all requests for the deprecated model to the replacement model transparently. The endpoint URL remains unchanged, but the response object's model ID updates to reflect the new version.
4. **Full transition period delivered** – The redirect lasts until the end of Databricks's standard transition period (e.g., three months from the partner's announcement date). After that period, queries against the deprecated model fail, and customers must update their applications to use the replacement model. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Limitations

- **Redirection is only possible when** the replacement model has the same price and is backwards compatible with the deprecated model. If no suitable replacement exists, queries may fail earlier. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **The model ID in the response changes** to reflect the redirect, which may affect monitoring or logging systems that rely on the exact model name. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Not all retirements qualify** – The bridge is specifically for partner models where the partner's deprecation notice is shorter than Databricks's standard policy. For non-partner (Databricks-hosted) models, standard retirement timelines apply without the need for a redirect. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Model Retirement Policy](/concepts/model-retirement-policy-databricks.md) – The overall framework for model deprecation across Foundation Model APIs and fine-tuning.
- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md) – One of the offerings where the redirect bridge applies.
- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md) – The other offering where the redirect bridge applies.
- [Partner Model Retirement Policy](/concepts/partner-model-retirement-policy.md) – The specific policy for models provided by OpenAI, Anthropic, and Google.
- Model Updates – Databricks may also ship incremental model updates with the same endpoint URL but updated model IDs.
- [Find Workloads Using Retired Models](/concepts/workload-discovery-for-deprecated-models.md) – A query to discover endpoints still hitting deprecated models.

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
