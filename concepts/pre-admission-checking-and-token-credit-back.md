---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed5c4d6ea86af71a976bdc8f02ff4d93ba0383d06b2af6316fdcbfac227df933
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-admission-checking-and-token-credit-back
    - token credit-back and Pre-admission checking
    - PCATC
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Pre-admission checking and token credit-back
description: Databricks pre-admits requests by verifying input tokens against ITPM and reserving max_tokens against OTPM; unused reserved tokens are credited back after the response.
tags:
  - rate-limits
  - token-management
  - databricks
timestamp: "2026-06-19T18:54:30.271Z"
---

# Pre-admission Checking and Token Credit-Back

**Pre-admission Checking** and **Token Credit-Back** are rate-limiting mechanisms used by [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) to manage token throughput and ensure fair resource allocation across all users. These features work together to reserve output tokens before processing and credit back any unused capacity to the user's allowance. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Pre-admission Checking

When a request is made to a pay-per-token endpoint, the system performs a pre-admission check before processing begins. The check verifies that the request can be admitted without exceeding the configured rate limits:

- **Input tokens per minute (ITPM)**: The system checks the prompt's input tokens against the ITPM limit.
- **Output tokens per minute (OTPM)**: The system reserves the number of output tokens specified in the `max_tokens` parameter against the OTPM limit.

If either check would cause the limit to be exceeded, the API immediately returns a `429 Too Many Requests` error. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Token Credit-Back

After a request is admitted and processed, the actual number of output tokens used is often less than the `max_tokens` value that was reserved during pre-admission. The system credits back the unused output tokens to the user's OTPM allowance. These credited tokens are immediately available for other requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Example

The following example illustrates how pre-admission checking and token credit-back work together: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

```python
# Request with max_tokens specified
request = {
    "prompt": "Write a story about...",  # 10 input tokens
    "max_tokens": 500                     # System reserves 500 output tokens
}

# Pre-admission check:
# - Verifies 10 tokens against ITPM limit
# - Reserves 500 tokens against OTPM limit
# - If either would exceed limits, returns 429 immediately
# If admitted, actual response uses only 350 tokens
# The system credits back 150 tokens (500 - 350) to your OTPM allowance
# These 150 tokens are immediately available for other requests
```

In this example, the `max_tokens` parameter specifies an upper bound of 500 output tokens. The system reserves 500 tokens against the OTPM limit during pre-admission. After processing, the actual response uses only 350 tokens. The remaining 150 tokens are credited back to the OTPM allowance and become immediately available for subsequent requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Rate Limit Enforcement

The most restrictive rate limit applies at any given time: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

| Limit Type | Description |
|------------|-------------|
| **Input tokens per minute (ITPM)** | Maximum input tokens processed within a 60-second window |
| **Output tokens per minute (OTPM)** | Maximum output tokens generated within a 60-second window |
| **Queries per hour (QPH)** | Maximum requests processed within a 60-minute window |

When any limit is reached, subsequent requests receive a `429` error until the rate limit window resets. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Best Practices

- **Set `max_tokens` explicitly**: Always specify a `max_tokens` value to control output length and provide a basis for token reservation and credit-back. This is especially important for models like Claude Sonnet 4, which defaults to a 1,000 token limit if not set. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Monitor token usage**: Track input and output token counts separately in applications. See monitoring and troubleshooting Foundation Model APIs. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Implement retry logic**: Use exponential backoff with jitter when encountering `429` rate limit errors. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Related Concepts

- Foundation Model APIs limits and quotas — Detailed rate limits by model
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Alternative for production workloads requiring higher limits
- [Rate limit errors](/concepts/rate-limit-error-handling-429-errors.md) — Handling `429` errors and error response structure
- [Pay-per-token endpoint rate limits](/concepts/pay-per-token-endpoint-rate-limits.md) — Token-based and query-based rate limits

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
