---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb42ac9e952fe0d552ee5c3a70d10e5ffa84b91a3a2e304d13b559a0fa29e733
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-based-rate-limiting-itpmotpm
    - TRL(
    - TRL
    - trl
    - Token-based rate limits
    - token-based rate limits
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Token-Based Rate Limiting (ITPM/OTPM)
description: Rate limits controlling the maximum number of input tokens per minute (ITPM) and output tokens per minute (OTPM) that can be processed within a 60-second window for pay-per-token endpoints.
tags:
  - rate-limiting
  - tokens
  - foundation-models
timestamp: "2026-06-19T10:38:34.398Z"
---

# Token-Based Rate Limiting (ITPM/OTPM)

**Token-Based Rate Limiting** is a throttling mechanism used by Databricks Foundation Model APIs to control the throughput of input and output tokens processed by pay-per-token endpoints. It ensures reliable performance and fair resource allocation across all users by enforcing separate limits for input tokens per minute (ITPM) and output tokens per minute (OTPM). ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Overview

Pay-per-token endpoints are governed by token-based and query-based rate limits. Token-based rate limits control the maximum number of tokens that can be processed per minute and are enforced separately for input and output tokens. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Input tokens per minute (ITPM)**: The maximum number of input tokens (from your prompts) that can be processed within a 60-second window. An ITPM rate limit controls the input token throughput of an endpoint. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Output tokens per minute (OTPM)**: The maximum number of output tokens (from the model's responses) that can be generated within a 60-second window. An OTPM rate limit controls the output token throughput of an endpoint. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Queries per hour (QPH)**: The maximum number of queries or requests that can be processed within a 60-minute window. For production applications with sustained usage patterns, Databricks recommends [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md), which provide guaranteed capacity. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## How Limits Are Tracked and Enforced

The most restrictive rate limit (ITPM, OTPM, or QPH) applies at any given time. For example, even if you haven't reached your ITPM limit, you might still be rate-limited if you exceed the QPH or OTPM limit. When either ITPM or OTPM limit is reached, subsequent requests receive a 429 error indicating too many requests were received. This message persists until the rate limit window resets. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

Databricks tracks and enforces token per minute (TPM) rate limits using pre-admission checking and a credit-back mechanism. When a request is submitted, the system checks whether the request's input tokens would exceed the ITPM limit and reserves the requested output tokens (based on `max_tokens`) against the OTPM limit. If either would exceed the limit, the system returns a 429 error immediately. If the request is admitted but the actual response uses fewer tokens than reserved, the system credits back the unused tokens to the OTPM allowance, making them immediately available for other requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Example of Pre-Admission Checking and Credit-Back

```python
# Request with max_tokens specified
request = {
    "prompt": "Write a story about...",  # 10 input tokens
    "max_tokens": 500  # System reserves 500 output tokens
}

# Pre-admission check:
# - Verifies 10 tokens against ITPM limit
# - Reserves 500 tokens against OTPM limit
# - If either would exceed limits, returns 429 immediately

# If admitted, actual response uses only 350 tokens
# The system credits back 150 tokens (500 - 350) to your OTPM allowance
# These 150 tokens are immediately available for other requests
```

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Rate Limits by Model

Rate limits vary based on the workspace platform tier, foundation model type, and how the model is deployed. The following tables summarize the ITPM, OTPM, and QPH rate limits for pay-per-token Foundation Model API endpoints for Enterprise tier workspaces. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

*Note: Specific rate limit values for each model are documented in the Databricks Foundation Model APIs limits and quotas page. Limits may change over time as Databricks updates its offerings.*

## Handling Rate Limit Errors

When you exceed rate limits, the API returns a `429 Too Many Requests` error: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

The error response includes: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- `limit_type`: Which specific limit was exceeded (ITPM, OTPM, QPS, or QPH)
- `limit`: The configured limit value
- `current`: Your current usage
- `retry_after`: Suggested wait time in seconds

## Best Practices for Managing TPM Rate Limits

### Monitor Token Usage

Track both input and output token counts separately in your applications: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

```python
# Example: Track token usage
response = model.generate(prompt)
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

# Check against limits
if input_tokens > ITPM_LIMIT or output_tokens > OTPM_LIMIT:
    # Implement backoff strategy
    pass
```

### Implement Retry Logic

Add exponential backoff when you encounter rate limit errors: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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
    """Retry a function with exponential backoff."""
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

### Optimize Token Usage

- **Minimize prompt length**: Use concise, well-structured prompts. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Control output length**: Use the `max_tokens` parameter to limit response size. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Set `max_tokens` explicitly for Claude Sonnet 4**: Always specify `max_tokens` when using Claude Sonnet 4 to avoid the default 1,000 token limit. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Batch efficiently**: Group related requests when possible while staying within limits. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Consider Model Selection

- **Smaller models for high-volume tasks**: Use models like Llama 3.1 8B for tasks that require higher throughput. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Large models for complex tasks**: Reserve Llama 3.1 405B for tasks that require maximum capability. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Provisioned Throughput Limits

For production workloads that require higher limits, provisioned throughput endpoints offer: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **No TPM restrictions**: Processing capacity based on provisioned resources
- **Higher rate limits**: Up to 200 queries per second per workspace
- **Predictable performance**: Dedicated resources ensure consistent latency

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service that enforces ITPM/OTPM rate limits
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Alternative deployment option without TPM restrictions
- Model Serving Limits and Regions — Additional limits for model serving workloads
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Endpoint type subject to token-based rate limiting
- Exponential Backoff — Retry strategy for handling rate limit errors

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
