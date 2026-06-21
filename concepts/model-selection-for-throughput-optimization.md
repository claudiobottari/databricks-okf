---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b4b0eefe4a9e981ebcf4821cdd5223db4c67c3929d65128bd28ecd72ec2cc89
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-selection-for-throughput-optimization
    - MSFTO
    - Model selection for cost optimization
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Model selection for throughput optimization
description: Choosing smaller models (e.g., Llama 3.1 8B) for high-volume throughput tasks and larger models (e.g., Llama 3.1 405B) for tasks requiring maximum capability.
tags:
  - model-selection
  - optimization
  - best-practices
timestamp: "2026-06-19T18:54:49.867Z"
---

# Model Selection for Throughput Optimization

**Model selection for throughput optimization** refers to the practice of choosing a foundation model size and deployment type to maximize request throughput while staying within the rate limits of [Foundation Model APIs](/concepts/foundation-model-apis.md). The goal is to balance model capability against the token and query limits imposed by pay-per-token endpoints, or to move to provisioned throughput when higher, predictable performance is required.

## Overview

Databricks Foundation Model APIs enforce three types of rate limits on pay-per-token endpoints: input tokens per minute (ITPM), output tokens per minute (OTPM), and queries per hour (QPH). The most restrictive limit applies at any time, meaning that even if ITPM is not exhausted, an application can be throttled by OTPM or QPH. To maintain high throughput, you must select a model whose typical token consumption stays well within these limits for your expected workload. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Key Trade-Off: Model Size vs. Throughput

Larger models (e.g., Llama 3.1 405B) offer greater capability but consume more tokens per request and often have lower rate limits, reducing achievable throughput. Smaller models (e.g., Llama 3.1 8B) process fewer tokens per request and generally have higher rate limits, making them suitable for high-volume tasks. The following table from the documentation outlines output token limits per model (partial excerpt): ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

| Model | Max output tokens |
|-------|-------------------|
| Llama 3.1 70B | 8,192 |
| Llama 3.1 405B | 8,192 |
| Mixtral 8x7B | 4,096 |
| (Full table in source) | |

Output token limits directly constrain throughput per request, especially for applications that generate long responses.

## Best Practices for Throughput-Optimized Selection

The Foundation Model API documentation recommends the following strategy: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Use smaller models for high-volume tasks.** For tasks that require higher throughput, choose models like Llama 3.1 8B instead of larger ones.
- **Reserve larger models for complex tasks.** Use models such as Llama 3.1 405B only when maximum capability is necessary, because their lower rate limits limit throughput.
- **Monitor token usage.** Track input and output token counts separately and compare them against ITPM and OTPM limits.
- **Implement retry logic.** Use exponential backoff when encountering 429 rate-limit errors.
- **Optimize prompts.** Keep prompts concise and use the `max_tokens` parameter to cap response length, especially for models like Claude Sonnet 4 where the default is 1,000 tokens.

## Considering Provisioned Throughput

For production workloads that cannot tolerate rate-limit throttling, [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) offer no TPM restrictions, higher rate limits (up to 200 queries per second per workspace), and consistent latency. Model selection for throughput becomes less constrained in this deployment model because throughput is determined by allocated resources rather than per-token limits. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Monitoring and Adjustment

After selecting a model, continuously monitor token usage and rate-limit errors. The API returns error details including which limit was exceeded (ITPM, OTPM, or QPH) and a suggested retry delay. If throughput is still insufficient, consider switching to a smaller model, further truncating prompt length, or migrating to provisioned throughput. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Pay-per-token endpoint rate limits](/concepts/pay-per-token-endpoint-rate-limits.md)
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md)
- [Token-based rate limits](/concepts/token-based-rate-limiting-itpmotpm.md)
- [Model Serving](/concepts/model-serving.md)
- [Retry with exponential backoff](/concepts/retry-logic-with-exponential-backoff.md)

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
