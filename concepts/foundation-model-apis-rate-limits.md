---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c28a9525ea701ca832d4074a9d18fb9dab801e870e34c5e0d548a455f865697
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis-rate-limits
    - FMARL
    - Foundation Model APIs Rate Limits and Quotas
    - Foundation Model APIs limits
    - Foundation Model APIs rate limits and quotas
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Foundation Model APIs Rate Limits
description: Rate limits enforced on Databricks Foundation Model APIs to ensure reliable performance and fair resource allocation, varying by workspace tier, model type, and deployment method.
tags:
  - rate-limiting
  - foundation-models
  - databricks
timestamp: "2026-06-19T10:39:30.813Z"
---

# Foundation Model APIs Rate Limits

Databricks Foundation Model APIs enforce **rate limits** to ensure reliable performance and fair resource allocation across all users. These limits vary based on the workspace platform tier, foundation model type, and deployment method (pay-per-token vs. provisioned throughput). ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Pay-per-token Endpoint Rate Limits

Pay-per-token endpoints are governed by three types of rate limits: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

* **Input tokens per minute (ITPM)** – Maximum number of input tokens (from prompts) that can be processed within a 60-second window.
* **Output tokens per minute (OTPM)** – Maximum number of output tokens (from model responses) that can be generated within a 60-second window.
* **Queries per hour (QPH)** – Maximum number of queries or requests that can be processed within a 60-minute window.

For production applications with sustained usage patterns, Databricks recommends [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md), which provide guaranteed capacity. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### How Limits Are Tracked and Enforced

The most restrictive rate limit among ITPM, OTPM, and QPH applies at any given time. Even if you have not reached your ITPM limit, you may still be rate-limited if you exceed the QPH or OTPM limit. When either limit is reached, subsequent requests receive a **429 Too Many Requests** error until the rate limit window resets. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

Databricks uses **pre-admission checking** with **credit-back** behavior. Before executing a request, the system checks the prompt's input tokens against the ITPM limit and reserves the `max_tokens` value against the OTPM limit. If either check would exceed limits, a 429 is returned immediately. If the actual response uses fewer output tokens than reserved, the unused tokens are credited back to the OTPM allowance and become immediately available for other requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Rate Limits by Model

Rate limits for pay-per-token endpoints vary by model. For Enterprise tier workspaces, specific ITPM, OTPM, and QPH values are documented in the official Databricks documentation. Some models have planned retirements — for example, starting February 15, 2026, Meta-Llama-3.1-405B-Instruct will be retired, and starting March 26, 2026, Gemini 3 Pro Preview will be retired. Between March 26, 2026 and June 7, 2026, API calls to Gemini 3 Pro will be temporarily redirected to Gemini 3.1 Pro with identical pricing. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Best Practices for Managing Rate Limits

### Step 1. Monitor Token Usage

Track both input and output token counts separately in your applications. Compare usage against known limits and implement logic to handle approaching thresholds. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

### Step 2. Implement Retry Logic

Add exponential backoff when encountering rate limit errors: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

### Step 3. Optimize Token Usage

- **Minimize prompt length**: Use concise, well-structured prompts.
- **Control output length**: Use the `max_tokens` parameter to limit response size.
- **Set `max_tokens` explicitly for Claude Sonnet 4**: Always specify `max_tokens` when using Claude Sonnet 4 to avoid the default 1,000 token limit.
- **Batch efficiently**: Group related requests when possible while staying within limits.

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Step 4. Consider Model Selection

- **Smaller models for high-volume tasks**: Use models like Llama 3.1 8B for tasks requiring higher throughput.
- **Large models for complex tasks**: Reserve Llama 3.1 405B for tasks requiring maximum capability.

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Provisioned Throughput Limits

For production workloads requiring higher limits, provisioned throughput endpoints offer: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **No TPM restrictions** – Processing capacity is based on provisioned resources.
- **Higher rate limits** – Up to 200 queries per second per workspace.
- **Predictable performance** – Dedicated resources ensure consistent latency.

### Output Token Limits

Each supported model has a maximum output token limit (the maximum number of tokens the model can generate in a single response). Specific values are documented in the official Databricks documentation. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Additional Limits for Provisioned Throughput

- **Llama 4 Maverick** is in Public Preview; autoscaling and metrics panels are not supported; traffic splitting is not supported on endpoints serving this model.
- When deploying a Meta Llama model from `system.ai` in Unity Catalog, you must choose the **Instruct** version; base versions are not supported for deployment from Unity Catalog.

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Resource and Payload Limits

Endpoints serving foundation models and external models are subject to resource and payload limits, including maximum request size, maximum context length, and maximum output tokens. Exact values are documented in the official Databricks documentation. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Monitoring and Troubleshooting

Monitor token usage patterns to optimize performance: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

When a rate limit is exceeded, the API returns a 429 error with a JSON body containing: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

- `limit_type` – Which specific limit was exceeded (ITPM, OTPM, QPS, or QPH).
- `limit` – The configured limit value.
- `current` – Your current usage.
- `retry_after` – Suggested wait time in seconds.

Common issues include rate limits for high-frequency requests and hitting output token limits. Solutions include upgrading to provisioned throughput and reducing `max_tokens` values. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Regional Availability and Data Processing

For supported regions, see the [Foundation Model APIs](/concepts/foundation-model-apis.md) overview. For data processing and residency details, see the compliance documentation. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md)
- [Model Serving](/concepts/model-serving.md)
- [Retired Models Policy](/concepts/partner-model-retirement-policy.md)
- [External Models](/concepts/external-models.md)

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
