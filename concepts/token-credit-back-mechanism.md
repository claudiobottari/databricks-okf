---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1203e90fc99b70a7d15750ed22672b9d06105a137c91e9871ce836a692b680a
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-credit-back-mechanism
    - TCM
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Token Credit-Back Mechanism
description: System that reserves output tokens against OTPM limits during pre-admission checking and credits back unused tokens from the actual response, making them immediately available for other requests.
tags:
  - rate-limiting
  - tokens
  - optimization
timestamp: "2026-06-19T10:38:30.345Z"
---

# Token Credit-Back Mechanism

The **Token Credit-Back Mechanism** is a rate-limit enforcement feature of the [Foundation Model APIs](/concepts/foundation-model-apis.md) that credits unused reserved tokens back to a user's available token allowance after a request completes. This mechanism improves throughput efficiency by ensuring that tokens reserved but not consumed by a request can be immediately used by other requests.

## Overview

When a request is made to a pay-per-token endpoint, the system performs a pre-admission check against the applicable rate limits. During this check, the system reserves a number of output tokens based on the `max_tokens` parameter specified in the request. If the actual response uses fewer tokens than reserved, the credit-back mechanism returns the unused tokens to the user's output tokens per minute (OTPM) allowance, making them immediately available for other requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## How It Works

The credit-back mechanism operates as part of the standard request lifecycle for pay-per-token endpoints:

1. **Pre-admission check**: The system verifies that the requested input tokens do not exceed the ITPM (Input Tokens Per Minute) limit and that the reserved output tokens (based on `max_tokens`) do not exceed the OTPM limit. If either would exceed the limit, a `429 Too Many Requests` error is returned immediately. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
2. **Token reservation**: Upon admission, the system reserves the full `max_tokens` count against the OTPM allowance, ensuring capacity for the expected response. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
3. **Credit-back**: After the response is generated, the system compares the actual output tokens used against the reserved amount and credits the difference back to the OTPM allowance. These credited tokens become immediately available for other requests. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Example

The following example illustrates the credit-back behavior for a request that reserves 500 output tokens but only uses 350: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

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

## Rate Limit Enforcement

The credit-back mechanism operates within the broader rate-limit framework. Pay-per-token endpoints are governed by three types of rate limits: ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

- **Input tokens per minute (ITPM)**: The maximum number of input tokens processed within a 60-second window.
- **Output tokens per minute (OTPM)**: The maximum number of output tokens generated within a 60-second window.
- **Queries per hour (QPH)**: The maximum number of requests processed within a 60-minute window.

The most restrictive rate limit applies at any given time. Even with the credit-back mechanism, a request may still be rate-limited if it exceeds the QPH or OTPM limit, or if the pre-admission check fails. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Best Practices

To maximize the benefit of the credit-back mechanism:

- **Set `max_tokens` explicitly**: Always specify the `max_tokens` parameter for models like Claude Sonnet 4 to avoid the default limit (e.g., 1,000 tokens for Claude Sonnet 4) and better manage token reservations. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Control output length**: Use `max_tokens` to limit response size, which reduces the gap between reserved and actual tokens and improves overall throughput. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Monitor token usage**: Track both input and output token counts to understand typical consumption patterns and set appropriate `max_tokens` values. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Related Concepts

- Foundation Model APIs Limits and Quotas – Complete documentation of rate limits and quotas.
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) – Alternative for production workloads without TPM restrictions.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of pay-per-token and provisioned throughput endpoints.
- Model Serving Limits – Additional limits for model serving workloads.

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
