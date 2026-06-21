---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: deb6afce1a3a8d60869a4ec8e8adfa6fdd6b4739e4501b045f31816a10c2c1e6
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limit-error-handling-429-errors
    - RLEH(E
    - Rate limit errors
    - rate-limit-error-handling-and-429-responses
    - 429 responses and Rate limit error handling
    - RLEHA4R
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Rate Limit Error Handling (429 Errors)
description: Error responses returned when rate limits are exceeded, including fields like limit_type, limit, current usage, and retry_after, along with strategies for handling them.
tags:
  - error-handling
  - rate-limiting
  - api
timestamp: "2026-06-19T10:38:59.772Z"
---

# Rate Limit Error Handling (429 Errors)

**Rate Limit Error Handling** refers to the strategies and best practices for managing HTTP 429 ("Too Many Requests") errors returned by [Foundation Model APIs](/concepts/foundation-model-apis.md) when a workload exceeds the platform's [token-based rate limits](/concepts/token-based-rate-limiting-itpmotpm.md) or query-based rate limits. Proper handling is essential for maintaining reliable application performance and fair resource allocation across all users. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Understanding 429 Errors

When a client exceeds any applicable rate limit—whether Input Tokens Per Minute (ITPM), Output Tokens Per Minute (OTPM), or Queries Per Hour (QPH)—the API returns a `429 Too Many Requests` error. The most restrictive limit at any given moment governs admission; for example, a request may be rejected due to OTPM limits even when ITPM usage is within bounds. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

The error response body includes fields that aid debugging and client-side recovery: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

| Field | Description |
|-------|-------------|
| `limit_type` | Which specific limit was exceeded (e.g., `input_tokens_per_minute`, `output_tokens_per_minute`, `queries_per_second`) |
| `limit` | The configured limit value for that resource |
| `current` | The client's current usage at the time of rejection |
| `retry_after` | Suggested wait time in seconds before the next retry |

## Best Practices for Handling

### Step 1: Monitor Token Usage

Track both input and output token counts separately in your application to detect approaching limits before they are hit: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

### Step 2: Implement Retry Logic with Exponential Backoff

Add [exponential backoff](/concepts/retry-with-exponential-backoff-for-rate-limits.md) with jitter when you encounter rate limit errors. The following function retries a call up to `max_retries` times, doubling the delay on each attempt and introducing random jitter to avoid thundering herd problems: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

### Step 3: Optimize Token Usage

Reduce the likelihood of hitting limits by: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Minimizing prompt length**: Use concise, well-structured prompts.
- **Controlling output length**: Use the `max_tokens` parameter to limit response size.
- **Setting max_tokens explicitly for Claude Sonnet 4**: Always specify `max_tokens` when using Claude Sonnet 4 to avoid the default 1,000-token limit.
- **Batching efficiently**: Group related requests when possible while staying within limits.

### Step 4: Consider Model Selection

Choose models appropriate for the throughput requirements of each task: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Smaller models for high-volume tasks**: Use models like Llama 3.1 8B for tasks that require higher throughput.
- **Large models for complex tasks**: Reserve Llama 3.1 405B for tasks that require maximum capability.

## Pre‑Admission Checking and Credit‑Back Behavior

The system uses **pre‑admission checking** to reserve output token capacity before a request executes. If a request specifies `max_tokens`, the system reserves that many output tokens against the OTPM limit before admitting the request. When the actual response uses fewer tokens, the unused capacity is **credited back** and becomes immediately available for other requests. This mechanism helps maximize throughput while preventing over‑commitment. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Monitoring and Logging

Log token usage to detect trends and alert on approaching limits: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

```python
import logging
logger = logging.getLogger(__name__)

def log_token_usage(response):
    usage = response.usage
    logger.info(f"Input tokens: {usage.prompt_tokens}")
    logger.info(f"Output tokens: {usage.completion_tokens}")
    logger.info(f"Total tokens: {usage.total_tokens}")

    # Alert if approaching limits
    if usage.prompt_tokens > ITPM_LIMIT * 0.8:
        logger.warning("Approaching ITPM limit")
    if usage.completion_tokens > OTPM_LIMIT * 0.8:
        logger.warning("Approaching OTPM limit")
```

## Related Concepts

- Token-Based Rate Limits — ITPM, OTPM, and QPH limits on pay‑per‑token endpoints.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Alternative endpoint type with no token‑based rate limits and higher query rates.
- Exponential Backoff — Retry strategy for distributed systems.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The broader API family that enforces these limits.
- Model Serving Limits and Regions — Regional resource constraints.

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
