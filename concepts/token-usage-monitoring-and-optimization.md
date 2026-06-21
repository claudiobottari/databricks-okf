---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9654726717df8b3c48f57c199b95dab72245aab53eb490b34b18cc0675f6881d
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-usage-monitoring-and-optimization
    - optimization and Token usage monitoring
    - TUMAO
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Token usage monitoring and optimization
description: Best practices for tracking input/output tokens, minimizing prompt length, controlling output via max_tokens, and logging token usage to avoid rate limits.
tags:
  - monitoring
  - optimization
  - best-practices
timestamp: "2026-06-19T18:55:01.989Z"
---

Here is the wiki page for "Token usage monitoring and optimization", based solely on the provided source material.

---

## Token Usage Monitoring and Optimization

**Token usage monitoring and optimization** refers to the practice of tracking the number of input and output tokens consumed by [Foundation Model APIs](/concepts/foundation-model-apis.md) and implementing strategies to manage those counts to stay within rate limits and reduce costs. On Databricks, pay-per-token endpoints enforce separate rate limits for input and output tokens, making per-token monitoring essential for reliable application performance.

### Token-Based Rate Limits

Pay-per-token endpoints are governed by two token-based rate limits and one query-based limit: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Input tokens per minute (ITPM)**: The maximum number of input tokens (from prompts) that can be processed within a 60-second window.
- **Output tokens per minute (OTPM)**: The maximum number of output tokens (from model responses) that can be generated within a 60-second window.
- **Queries per hour (QPH)**: The maximum number of requests that can be processed within a 60-minute window.

The most restrictive limit (ITPM, OTPM, or QPH) applies at any given time. For example, even if you haven’t reached your ITPM limit, you might still be rate-limited if you exceed the QPH or OTPM limit. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### How Limits Are Tracked and Enforced

Databricks tracks and enforces TPM rate limits using a pre-admission checking system with a credit-back mechanism. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

When a request is submitted:
1. The system verifies the input token count against the ITPM limit.
2. It reserves the requested `max_tokens` count against the OTPM limit.
3. If either check would exceed the limits, it returns a `429 Too Many Requests` error immediately.

After the request is processed, if the actual response uses fewer tokens than were reserved, the system credits the unused tokens back to the OTPM allowance. Those credited tokens are immediately available for other requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Monitoring Token Usage

Track both input and output token counts separately in your applications using the token usage fields returned by the model response: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

```python
response = model.generate(prompt)
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

if input_tokens > ITPM_LIMIT or output_tokens > OTPM_LIMIT:
    # Implement backoff strategy
    pass
```

Log token usage for monitoring and set up alerts when usage approaches limits: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

```python
import logging
logger = logging.getLogger(__name__)

def log_token_usage(response):
    usage = response.usage
    logger.info(f"Input tokens: {usage.prompt_tokens}")
    logger.info(f"Output tokens: {usage.completion_tokens}")
    logger.info(f"Total tokens: {usage.total_tokens}")

    if usage.prompt_tokens > ITPM_LIMIT * 0.8:
        logger.warning("Approaching ITPM limit")
    if usage.completion_tokens > OTPM_LIMIT * 0.8:
        logger.warning("Approaching OTPM limit")
```

### Optimization Strategies

**Minimize prompt length**: Use concise, well-structured prompts to reduce input token consumption. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

**Control output length**: Use the `max_tokens` parameter to limit the size of model responses. For Claude Sonnet 4, always specify `max_tokens` explicitly to avoid the default 1,000 token limit. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

**Batch efficiently**: Group related requests when possible while staying within the applicable rate limits. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

**Consider model selection**: Use smaller models like Llama 3.1 8B for high-volume tasks that require higher throughput. Reserve larger models like Llama 3.1 405B for complex tasks that require maximum capability. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Handling Rate Limit Errors

When a rate limit is exceeded, the API returns a `429 Too Many Requests` error with a JSON body containing details about which limit was hit: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

The error response includes: `limit_type` (which specific limit was exceeded), `limit` (the configured limit value), `current` (current usage), and `retry_after` (suggested wait time in seconds). ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

Implement retry logic with exponential backoff and jitter when encountering these errors: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

### Provisioned Throughput as an Alternative

For production workloads that require higher or more predictable throughput, provisioned throughput endpoints offer no TPM restrictions, processing capacity based on provisioned resources, up to 200 queries per second per workspace, and dedicated resources that ensure consistent latency. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Rate limits](/concepts/rate-limits-and-timeouts-in-model-serving.md)
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md)
- [Pay-per-Token Pricing](/concepts/pay-per-token-pricing.md)
- Model selection for cost optimization

### Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
