---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 855d5f15eb00848b68e04d29b5f87af943b0214b54569d97c58fb1defd31486e
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retry-logic-with-exponential-backoff
    - RLWEB
    - Retry with exponential backoff
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Retry Logic with Exponential Backoff
description: Best practice for retrying requests after rate limit errors using exponential backoff with jitter to handle 429 errors gracefully.
tags:
  - retry-logic
  - best-practices
  - resilience
timestamp: "2026-06-19T10:38:23.250Z"
---

# Retry Logic with Exponential Backoff

**Retry Logic with Exponential Backoff** is a pattern for handling transient errors, especially rate‑limit errors (HTTP 429 “Too Many Requests”), by automatically retrying a failed operation after a delay that increases exponentially with each attempt. This approach reduces the load on the service during congestion and eventually succeeds when the rate limit window resets or the contention subsides. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Overview

When invoking APIs or services that enforce rate limits (such as [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md)), a request may be rejected because the consumer has exceeded a token‑based or query‑based quota. A naive immediate retry would likely fail again and could worsen the congestion. Exponential backoff spreads retries over time, giving the service breathing room while still attempting to complete the request. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Implementation

A typical retry‑with‑exponential‑backoff function accepts the original operation and parameters that control the delay schedule. Databricks recommends the following Python implementation for rate‑limited Foundation Model API endpoints: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

The function retries only when the exception message contains `"rate_limit"` or `"429"`; all other exceptions are re‑raised immediately. After each retry, the delay is multiplied by `exponential_base` (default 2), and optional random jitter is added to avoid thundering‑herd effects. The process repeats until the maximum number of retries (`max_retries`, default 10) is exhausted. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `initial_delay` | 1 | Starting delay in seconds before the first retry. |
| `exponential_base` | 2 | Factor by which the delay is multiplied after each retry. |
| `jitter` | True | When `True`, introduces a random variation to the delay to prevent synchronized retries. |
| `max_retries` | 10 | Maximum number of retry attempts before giving up. |

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## When to Use Exponential Backoff

- **Rate‑limited APIs** – Any API that returns a `429` status code when token or query quotas are exceeded. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Transient failures** – Temporary network outages, service throttling, or resource exhaustion that resolve within seconds to minutes.
- **Production workloads** – Systems that must stay resilient under load, such as batch inference pipelines or real‑time agent calls.

## Best Practices

- **Monitor token usage** – Track input and output token counts in your application to anticipate when limits might be hit. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Set appropriate `max_tokens`** – For models like Claude Sonnet 4, always specify `max_tokens` to avoid the default cap. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Use jitter** – Randomizing the delay prevents all clients from retrying at the same moment. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Consider provisioned throughput** – For sustained high‑volume usage, provisioned throughput endpoints eliminate token‑based rate limits and provide predictable performance. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Related Concepts

- Rate Limiting and Quotas – How token‑ and query‑based limits work.
- Foundation Model APIs limits and quotas – Specific ITPM, OTPM, and QPH limits for Databricks endpoints.
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) – Alternative for workloads requiring higher, predictable throughput.
- [Error Handling and Resilience Patterns](/concepts/error-handling-in-scorers.md) – Broader strategies for robust API clients.
- Model Serving Limits – Additional constraints on payload size and concurrency.

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
