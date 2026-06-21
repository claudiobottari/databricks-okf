---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a96afe0f1adb1606ecc30e7375696eb2f851be83f753cb5cf6dc76a22343f1e8
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retry-with-exponential-backoff-for-rate-limits
    - RWEBFRL
    - exponential backoff
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Retry with exponential backoff for rate limits
description: Best practice pattern for handling 429 rate limit errors by retrying with exponential backoff, optionally adding jitter to avoid thundering herd problems.
tags:
  - best-practices
  - resilience
  - rate-limits
timestamp: "2026-06-19T18:54:59.651Z"
---

# Retry with Exponential Backoff for Rate Limits

**Retry with exponential backoff** is a strategy for handling [rate limiting](/concepts/rate-limiting-in-evaluation.md) errors from [Foundation Model APIs](/concepts/foundation-model-apis.md) and other API services. When a request is rejected because a rate limit has been exceeded (typically returning an HTTP `429 Too Many Requests` status), the client waits an increasing amount of time between each retry attempt before resubmitting the request. This approach reduces server load and improves the likelihood of successful retries. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## How Exponential Backoff Works

Exponential backoff increases the delay between retries by multiplying the previous delay by a constant factor (the exponential base) after each failed attempt. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

The basic algorithm is:

1. Attempt the request.
2. If the request succeeds, return the result.
3. If the request fails with a rate limit error (`429` or `rate_limit` in the error message), wait for a delay period, then retry.
4. After each failed retry, multiply the delay by the exponential base (commonly 2).
5. Stop retrying after reaching a maximum number of retries.

## Implementation Example

The following Python function implements retry with exponential backoff, including optional jitter (randomization) to prevent multiple clients from retrying simultaneously: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

## Key Parameters

- **`initial_delay`**: The starting wait time before the first retry (default: 1 second). ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **`exponential_base`**: The multiplier applied to the delay after each retry (default: 2). A base of 2 doubles the wait time after each attempt. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **`jitter`**: When enabled, randomizes the delay to prevent thundering herd problem|thundering herd problems where many clients retry simultaneously (default: True). ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **`max_retries`**: The maximum number of retry attempts before giving up (default: 10). ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Rate Limit Error Response

When a rate limit is exceeded, Databricks Foundation Model APIs return a `429 Too Many Requests` error with detailed information: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

The `retry_after` field in the error response provides a suggested wait time in seconds, which can be used as the initial delay. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Related Concepts

- Foundation Model APIs limits and quotas — Details on rate limits for pay-per-token endpoints
- [Token-based rate limits](/concepts/token-based-rate-limiting-itpmotpm.md) — ITPM (input tokens per minute) and OTPM (output tokens per minute) limits
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Alternative deployment with no TPM restrictions
- Rate limit monitoring — Tracking token usage to anticipate limits
- [Model Serving](/concepts/model-serving.md) — Infrastructure for deploying and serving models

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
