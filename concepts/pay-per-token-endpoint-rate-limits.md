---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9870abf766743ff1c4e6deb2594d2e992675b8c2dffaba51f06d0d993d9112a9
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-endpoint-rate-limits
    - PERL
    - Token limits
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Pay-per-token endpoint rate limits
description: Foundation Model APIs enforce token-based (ITPM, OTPM) and query-based (QPH) rate limits on pay-per-token endpoints, with the most restrictive limit applying at any time.
tags:
  - rate-limits
  - foundation-models
  - databricks
timestamp: "2026-06-19T18:54:38.966Z"
---

# Pay-per-token endpoint rate limits

Pay-per-token endpoints are a pricing model for [Foundation Model APIs](/concepts/foundation-model-apis.md) where you are charged per token processed, and they are governed by token-based and query-based rate limits to ensure reliable performance and fair resource allocation across users. These limits vary based on workspace platform tier, foundation model type, and deployment method. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Rate limit types

Pay-per-token endpoints enforce three primary rate limits: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Input tokens per minute (ITPM)**: The maximum number of input tokens (from your prompts) that can be processed within a 60‑second window. Controls input token throughput.
- **Output tokens per minute (OTPM)**: The maximum number of output tokens (from the model’s responses) that can be generated within a 60‑second window. Controls output token throughput.
- **Queries per hour (QPH)**: The maximum number of queries or requests that can be processed within a 60‑minute window. For sustained production usage, Databricks recommends [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) which offer guaranteed capacity.

## How limits are tracked and enforced

The most restrictive rate limit (ITPM, OTPM, or QPH) applies at any given time. Even if you haven’t reached your ITPM limit, you might be rate‑limited if you exceed the QPH or OTPM limit. When either ITPM or OTPM is reached, subsequent requests receive a `429 Too Many Requests` error until the rate limit window resets. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

Databricks uses a **pre‑admission checking** mechanism with **credit‑back** behavior. Before processing a request, the system reserves the maximum possible output tokens (based on `max_tokens`) against the OTPM limit and the actual input tokens against the ITPM limit. If the reservation would exceed either limit, the request is immediately rejected with a 429 error. After the response is generated, unused reserved tokens are credited back to the OTPM allowance and become available for other requests. The same applies for input tokens—the actual tokens consumed may be less than reserved, and the difference is credited back. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

```python
# Pre-admission checking example
request = {
    "prompt": "Write a story about...",  # 10 input tokens
    "max_tokens": 500  # System reserves 500 output tokens
}
# If admitted and actual response uses 350 tokens,
# 150 tokens are credited back to OTPM allowance.
```

## Rate limits by model

Specific ITPM, OTPM, and QPH limits vary by model and are documented in the Foundation Model APIs limits page. For **Enterprise tier workspaces**, the published tables list the exact limits for each supported model. Limits may change over time; always refer to the official documentation for the most current values. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Best practices for managing TPM rate limits

1. **Monitor token usage**: Track input and output tokens separately in your application. Compare against ITPM and OTPM limits to anticipate throttling. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
2. **Implement retry logic**: Use exponential backoff with jitter when encountering rate‑limit errors. A common pattern is to start with a 1‑second delay and double on each retry, up to 10 retries. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
3. **Optimize token usage**:
   - Minimize prompt length.
   - Control output length with the `max_tokens` parameter.
   - Always set `max_tokens` explicitly for Claude Sonnet 4 to avoid the default 1,000 token limit.
   - Batch related requests when possible, while staying within limits. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
4. **Consider model selection**: Use smaller models (e.g., Llama 3.1 8B) for high‑throughput tasks; reserve larger models (e.g., Llama 3.1 405B) for complex tasks that require maximum capability. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Monitoring and troubleshooting

Log token usage and set up warnings when approaching 80% of a limit: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

```python
import logging
logger = logging.getLogger(__name__)

def log_token_usage(response):
    usage = response.usage
    logger.info(f"Input tokens: {usage.prompt_tokens}")
    logger.info(f"Output tokens: {usage.completion_tokens}")
    if usage.prompt_tokens > ITPM_LIMIT * 0.8:
        logger.warning("Approaching ITPM limit")
    if usage.completion_tokens > OTPM_LIMIT * 0.8:
        logger.warning("Approaching OTPM limit")
```

When a rate limit is exceeded, the API returns a 429 error with details: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

```json
{
  "error": {
    "message": "Rate limit exceeded: ITPM limit of 200,000 tokens reached",
    "type": "rate_limit_exceeded",
    "code": 429,
    "limit_type": "input_tokens_per_minute",
    "limit": 200000,
    "current": 200150,
    "retry_after": 15
  }
}
```

The response includes `limit_type` (ITPM, OTPM, QPS, or QPH), the configured `limit`, current usage (`current`), and a suggested wait time in seconds (`retry_after`). Use this information to implement adaptive throttling. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Provisioned throughput as an alternative

For production workloads requiring higher throughput and predictable performance, Databricks offers provisioned throughput endpoints. These have no TPM restrictions—processing capacity is based on provisioned resources—and support up to 200 queries per second per workspace. They also eliminate token‑based rate limits, making them suitable for sustained, high‑volume usage. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Related concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of Databricks’ managed model serving.
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) – Alternative with no token rate limits.
- [Token-based rate limits](/concepts/token-based-rate-limiting-itpmotpm.md) – The ITPM/OTPM model.
- ITPM – Input tokens per minute limit.
- [OTPM](/concepts/online-table-permission-model.md) – Output tokens per minute limit.
- [QPH](/concepts/privilege-inheritance-hierarchy.md) – Queries per hour limit.
- Exponential backoff – Retry strategy for rate‑limited calls.
- 429 Too Many Requests – HTTP status for rate limit errors.

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
