---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6a2d55e652e60bb78cf6e52e356e3197027024875b6f802b2d686f8d7f59297
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-selection-strategy-for-throughput
    - MSSFT
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Model Selection Strategy for Throughput
description: Guidance on selecting smaller models (e.g., Llama 3.1 8B) for high-volume tasks and larger models (e.g., Llama 3.1 405B) for complex tasks to optimize within rate limits.
tags:
  - model-selection
  - optimization
  - best-practices
timestamp: "2026-06-19T10:38:55.038Z"
---

# Model Selection Strategy for Throughput

**Model Selection Strategy for Throughput** is a decision-making framework for choosing between smaller high-throughput models and larger high-capability models when deploying [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks. The strategy balances throughput requirements, rate limits, cost, and model capability to match the right model to each workload.

## Overview

Pay-per-token endpoints enforce three independent rate limits that constrain throughput: **Input Tokens Per Minute (ITPM)**, **Output Tokens Per Minute (OTPM)**, and **Queries Per Hour (QPH)**. These limits vary significantly by model size and workspace tier. The core trade-off is that smaller models typically offer higher rate limits and lower latency, while larger models provide superior reasoning capability but with stricter throughput constraints. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Selection Criteria

### Smaller Models for High-Volume Tasks

For workloads that require high throughput, such as real-time chat, content summarization, or batch processing of numerous independent queries, smaller models are recommended. Models like Llama 3.1 8B typically expose higher ITPM and OTPM quotas and have lower per-request latency, enabling sustained higher request rates without hitting rate limits. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Larger Models for Complex Tasks

For tasks demanding maximum reasoning capability—such as nuanced analysis, long-form generation, or multi-step reasoning—larger models like Llama 3.1 405B are appropriate. These models deliver superior output quality but come with lower rate limits. They are best reserved for infrequent, complex analyses where throughput is secondary to output quality. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Implementing the Strategy

### Step 1: Analyze Workload Requirements

Evaluate your application's expected volume, peak request patterns, and quality requirements. Consider:

- **Input volume**: Average and peak prompt sizes in tokens
- **Output requirements**: Expected response lengths
- **Request frequency**: Queries per hour/minute
- **Quality needs**: Level of reasoning or creativity required

### Step 2: Match Model to Limits

Select a model whose rate limits comfortably accommodate your expected peak load. The most restrictive limit at any moment governs whether a request is admitted. For example, even if ITPM limits are not reached, exceeding OTPM or QPH limits will still return `429` errors. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Step 3: Monitor and Adjust

Track token usage patterns to validate model selection:

```python
# Monitor token consumption against limits
response = model.generate(prompt)
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

# Alert if approaching limits
if input_tokens > ITPM_LIMIT * 0.8:
    logger.warning("Approaching ITPM limit")
if output_tokens > OTPM_LIMIT * 0.8:
    logger.warning("Approaching OTPM limit")
```

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Additional Considerations

### Provisioned Throughput as an Alternative

For production workloads with sustained high throughput requirements, [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) offer an alternative that eliminates per-token rate limits. These endpoints provide:

- **No TPM restrictions**: Processing capacity based on provisioned resources
- **Higher rate limits**: Up to 200 queries per second per workspace
- **Predictable performance**: Dedicated resources ensure consistent latency

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Implement Retry Logic

Even with careful model selection, rate limit errors can occur during traffic spikes. Implement exponential backoff with jitter to retry gracefully when encountering `429` errors:

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

### Optimize Token Usage

To maximize effective throughput within rate limits:

- **Minimize prompt length**: Use concise, well-structured prompts to reduce input token consumption
- **Control output length**: Use the `max_tokens` parameter to limit response size
- **Set max_tokens explicitly for Claude Sonnet 4**: Always specify `max_tokens` to avoid the default 1,000 token limit
- **Batch efficiently**: Group related requests when possible while staying within limits

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Decision Matrix

| Workload Pattern | Recommended Model | Rationale |
|-----------------|-------------------|-----------|
| High-volume, simple tasks (e.g., classification, short summaries) | Smaller models (e.g., Llama 3.1 8B) | Higher rate limits, lower latency, lower cost |
| Low-volume, complex tasks (e.g., long-form generation, reasoning) | Larger models (e.g., Llama 3.1 405B) | Superior output quality, acceptable throughput constraints |
| Sustained high-volume production | Provisioned throughput endpoints | No TPM restrictions, predictable performance |
| Mixed workloads | Hybrid approach with model routing | Route simple queries to small models, complex to large |

## Related Concepts

- Rate Limiting — Token-based and query-based limits enforced per endpoint
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Dedicated capacity for high-volume workloads
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Pay-per-token and provisioned throughput endpoints
- Throughput Optimization — Techniques to maximise requests within rate limits
- [Model Serving](/concepts/model-serving.md) — Serving infrastructure for foundation and custom models

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
