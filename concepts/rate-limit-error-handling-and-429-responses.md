---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e78adc66f73ce948a6d6024826bb46f96441dc9e85fe323242222d0791fdd184
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limit-error-handling-and-429-responses
    - 429 responses and Rate limit error handling
    - RLEHA4R
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Rate limit error handling and 429 responses
description: When rate limits are exceeded, the API returns a 429 error with details including limit_type, limit value, current usage, and suggested retry_after time.
tags:
  - error-handling
  - rate-limits
  - api
timestamp: "2026-06-19T18:55:43.694Z"
---

# Rate limit error handling and 429 responses

**Rate limit error handling and 429 responses** are a critical aspect of working with [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md), which enforce rate limits to ensure reliable performance and fair resource allocation across all users. When a request exceeds an allowed rate, the API returns a `429 Too Many Requests` status code, and clients must implement proper error handling to maintain operational stability. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## How rate limits are enforced

For [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md), rate limits are controlled by three concurrent quotas: **input tokens per minute (ITPM)**, **output tokens per minute (OTPM)**, and **queries per hour (QPH)**. The most restrictive limit applies at any given time. For example, even if the ITPM limit has not been reached, a request may still be rejected if the QPH or OTPM limit has been exceeded. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

Databricks uses a **pre-admission checking** mechanism with a **credit-back** feature. Before processing a request, the system verifies the input tokens against the ITPM limit and reserves the requested output tokens (based on `max_tokens`) against the OTPM limit. If either check would exceed the limits, the request is immediately rejected with a 429 error. If the actual response uses fewer output tokens than reserved, the unused tokens are credited back and become immediately available for other requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## 429 error response format

When a rate limit is exceeded, the API returns a JSON error response that includes useful metadata for debugging and retry logic:

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

The response includes:
- `limit_type` – which specific limit was exceeded (e.g., `input_tokens_per_minute`, `output_tokens_per_minute`, `queries_per_hour`, `queries_per_second`).
- `limit` – the configured limit value.
- `current` – the current usage that triggered the limit.
- `retry_after` – a suggested wait time in seconds before retrying.

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Best practices for handling 429 errors

### 1. Monitor token usage

Track prompt and completion token counts separately in your application to anticipate when limits may be reached. Log token usage and set up alerts when approaching 80% of limits. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### 2. Implement exponential backoff with jitter

When a 429 error is received, retry the request using exponential backoff. The following example retries with an initial delay of 1 second, doubling each time, and adds random jitter to avoid thundering herd problems:

```python
import time
import random

def retry_with_exponential_backoff(
    func,
    initial_delay: float = 1,
    exponential_base: float = 2,
    jitter: bool = True,
    max_retries: int = 10,
):
    num_retries = 0
    delay = initial_delay
    while num_retries < max_retries:
        try:
            return func()
        except Exception as e:
            if "rate_limit" in str(e) or "429" in str(e):
                num_retries += 1
                if jitter:
                    delay *= exponential_base * (1 + random.random())
                else:
                    delay *= exponential_base
                time.sleep(delay)
            else:
                raise e
    raise Exception(f"Maximum retries {max_retries} exceeded")
```

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### 3. Optimize token usage

- Minimize prompt length by using concise, well-structured prompts.
- Control output length with the `max_tokens` parameter. When using Claude Sonnet 4, always specify `max_tokens` to avoid the default 1,000-token limit.
- Batch related requests where possible while staying within limits.

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### 4. Consider model selection

- Use smaller models (e.g., Llama 3.1 8B) for high‑volume tasks that require higher throughput.
- Reserve larger models (e.g., Llama 3.1 405B) for complex tasks that demand maximum capability.

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Provisioned throughput endpoints

For production workloads with predictable high throughput, [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) offer an alternative. These endpoints have **no TPM (tokens-per-minute) restrictions** and support higher rate limits (up to 200 queries per second per workspace). Because dedicated resources are allocated, rate limit errors are far less common. Use provisioned throughput when sustained usage patterns exceed the pay-per-token limits. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Related concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of API-based model serving on Databricks.
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) – On-demand endpoints governed by ITPM, OTPM, and QPH limits.
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) – Dedicated endpoints without TPM restrictions.
- Exponential backoff – Retry strategy for transient errors.
- [Token limits](/concepts/pay-per-token-endpoint-rate-limits.md) – General discussion of input/output token constraints.

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
