---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0869610c2cb069d8dae7e1fd6b594af0adf6c92719fcb49f113e8c2566196b7e
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limit-error-handling-best-practices
    - RLEHBP
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Rate Limit Error Handling Best Practices
description: Best practices for handling 429 rate limit errors including exponential backoff retry logic, token usage monitoring, and error response parsing.
tags:
  - error-handling
  - retry-logic
  - best-practices
timestamp: "2026-06-18T12:25:27.837Z"
---

# Rate Limit Error Handling Best Practices

Rate limit errors occur when an application exceeds the allowed number of requests or tokens within a given time window. Proper handling of these errors is critical for maintaining application reliability and ensuring fair resource allocation across users. Databricks Foundation Model APIs enforce rate limits that vary by model type, deployment method, and workspace platform tier. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Understanding Rate Limits

### Types of Rate Limits

Foundation Model APIs enforce three types of limits: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Input tokens per minute (ITPM)**: The maximum number of input tokens (from prompts) processed within a 60-second window.
- **Output tokens per minute (OTPM)**: The maximum number of output tokens (from model responses) generated within a 60-second window.
- **Queries per hour (QPH)**: The maximum number of requests processed within a 60-minute window.

### How Limits Are Tracked and Enforced

The most restrictive rate limit (ITPM, OTPM, or QPH) applies at any given time. For example, even if you haven't reached your ITPM limit, you might still be rate-limited if you exceed the QPH or OTPM limit. Databricks uses pre-admission checking and credit-back behavior: when a request is admitted, the system reserves tokens based on the `max_tokens` parameter. If the actual response uses fewer tokens, the unused tokens are credited back and become immediately available for other requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Error Response Format

When rate limits are exceeded, the API returns a `429 Too Many Requests` error with detailed information: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

- `limit_type`: Which specific limit was exceeded (ITPM, OTPM, or QPH)
- `limit`: The configured limit value
- `current`: Your current usage
- `retry_after`: Suggested wait time in seconds

## Monitoring Token Usage

Track both input and output token counts separately in your applications to stay within limits: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

Implement proactive logging to detect when usage approaches limits: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

## Implementing Retry Logic with Exponential Backoff

When rate limit errors occur, use exponential backoff with jitter to retry requests. This prevents thundering herd problems and ensures graceful recovery: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

## Optimizing Token Usage

### Minimize Prompt Length

Use concise, well-structured prompts to reduce input token consumption. Shorter prompts not only stay within ITPM limits but also reduce latency. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Control Output Length

Use the `max_tokens` parameter to limit response size. For Claude Sonnet 4, always specify `max_tokens` explicitly to avoid the default 1,000 token limit. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Batch Efficiently

Group related requests when possible while staying within limits. However, ensure that batched requests do not collectively exceed rate limits. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Model Selection Strategy

Choose models based on your workload requirements: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Smaller models for high-volume tasks**: Use models like Llama 3.1 8B for tasks that require higher throughput. These models typically have higher rate limits and lower cost per token.
- **Large models for complex tasks**: Reserve models like Llama 3.1 405B for tasks that require maximum capability, where rate limits may be more restrictive.

## Provisioned Throughput for Production Workloads

For production applications with sustained usage patterns, [Provisioned Throughput](/concepts/provisioned-throughput.md) endpoints offer significant advantages: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **No TPM restrictions**: Processing capacity based on provisioned resources
- **Higher rate limits**: Up to 200 queries per second per workspace
- **Predictable performance**: Dedicated resources ensure consistent latency

Consider migrating from pay-per-token to provisioned throughput endpoints if you consistently encounter rate limits or need guaranteed capacity. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Frequent 429 errors | Exceeding ITPM or OTPM limits | Implement exponential backoff; reduce prompt size or output length |
| Intermittent failures | Spikes in request volume | Add request queuing; use provisioned throughput |
| Slow response times | Approaching rate limits | Monitor token usage; consider smaller model |
| Rate limit errors during batch processing | Cumulative token usage exceeds limit | Reduce batch size; add delays between batches |

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Overview of Databricks hosted model endpoints
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Dedicated capacity for production workloads
- Model Serving Limits — Service-wide limits for model serving
- API Reference — Foundation Model API documentation
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Token-based pricing and rate limits

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
