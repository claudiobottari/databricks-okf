---
title: Foundation Model APIs limits and quotas | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/limits
ingestedAt: "2026-06-18T08:11:05.980Z"
---

This page describes the limits and quotas for Databricks Foundation Model APIs workloads.

Databricks Foundation Model APIs enforce rate limits to ensure reliable performance and fair resource allocation across all users. These limits vary based on the [workspace platform tier](https://www.databricks.com/product/pricing/platform-addons), foundation model type and how you deploy your foundation model.

## Pay-per-token endpoint rate limits[​](#pay-per-token-endpoint-rate-limits "Direct link to Pay-per-token endpoint rate limits")

Pay-per-token endpoints are governed by token-based and query-based rate limits. Token-based rate limits control the maximum number of tokens that can be processed per minute and are enforced separately for input and output tokens.

*   **Input tokens per minute (ITPM)**: The maximum number of input tokens (from your prompts) that can be processed within a 60-second window. An ITPM rate limit controls the input token throughput of an endpoint.
*   **Output tokens per minute (OTPM)**: The maximum number of output tokens (from the model's responses) that can be generated within a 60-second window. An OTPM rate limit controls the output token throughput of an endpoint.
*   **Queries per hour**: The maximum number of queries or requests that can be processed within a 60 minute window. For production applications with sustained usage patterns, Databricks recommends provisioned throughput endpoints, which provide guaranteed capacity.

### How limits are tracked and enforced[​](#how-limits-are-tracked-and-enforced "Direct link to How limits are tracked and enforced")

The most restrictive rate limit (ITPM, OTPM, QPH) applies at any given time. For example, even if you haven't reached your ITPM limit, you might still be rate-limited if you exceed the QPH or OTPM limit. When either ITPM or OTPM limit is reached, subsequent requests receive a 429 error that indicates too many requests were received. This message persists until the rate limit window resets.

Databricks tracks and enforces tokens per minute (TPM) rate limits using the following features:

The following is an example of how pre-admission checking and the credit-back behavior work.

Python

    # Request with max_tokens specifiedrequest = {    "prompt": "Write a story about...",  # 10 input tokens    "max_tokens": 500  # System reserves 500 output tokens}# Pre-admission check:# - Verifies 10 tokens against ITPM limit# - Reserves 500 tokens against OTPM limit# - If either would exceed limits, returns 429 immediately# If admitted, actual response uses only 350 tokens# The system credits back 150 tokens (500 - 350) to your OTPM allowance# These 150 tokens are immediately available for other requests

### Rate limits by model[​](#rate-limits-by-model "Direct link to Rate limits by model")

The following tables summarize the ITPM, OTPM, and QPH rate limits for pay-per-token Foundation Model API endpoints for _Enterprise tier workspaces_:

note

Starting February, 15 2026, Meta-Llama-3.1-405B-Instruct will be retired. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.

Starting March 26, 2026, Gemini 3 Pro Preview will be retired. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation. To allow more time for migration, between March 26, 2026 and June 7, 2026, API calls to Gemini 3 Pro will be temporarily redirected to Gemini 3.1 Pro. The pricing for both models is identical.

## Best practices for managing TPM rate limits[​](#best-practices-for-managing-tpm-rate-limits "Direct link to Best practices for managing TPM rate limits")

### Step 1. Monitor token usage[​](#step-1-monitor-token-usage "Direct link to Step 1. Monitor token usage")

Track both input and output token counts separately in your applications:

Python

    # Example: Track token usageresponse = model.generate(prompt)input_tokens = response.usage.prompt_tokensoutput_tokens = response.usage.completion_tokenstotal_tokens = response.usage.total_tokens# Check against limitsif input_tokens > ITPM_LIMIT or output_tokens > OTPM_LIMIT:    # Implement backoff strategy    pass

### Step 2. Implement retry logic[​](#step-2-implement-retry-logic "Direct link to Step 2. Implement retry logic")

Add exponential backoff when you encounter rate limit errors:

Python

    import timeimport randomdef retry_with_exponential_backoff(    func,    initial_delay: float = 1,    exponential_base: float = 2,    jitter: bool = True,    max_retries: int = 10,):    """Retry a function with exponential backoff."""    num_retries = 0    delay = initial_delay    while num_retries < max_retries:        try:            return func()        except Exception as e:            if "rate_limit" in str(e) or "429" in str(e):                num_retries += 1                if jitter:                    delay *= exponential_base * (1 + random.random())                else:                    delay *= exponential_base                time.sleep(delay)            else:                raise e    raise Exception(f"Maximum retries {max_retries} exceeded")

### Step 3. Optimize token usage[​](#step-3-optimize-token-usage "Direct link to Step 3. Optimize token usage")

*   **Minimize prompt length**: Use concise, well-structured prompts
*   **Control output length**: Use `max_tokens` parameter to limit response size
*   **Set max\_tokens explicitly for Claude Sonnet 4**: Always specify `max_tokens` when using Claude Sonnet 4 to avoid the default 1,000 token limit
*   **Batch efficiently**: Group related requests when possible while staying within limits

### Step 4. Consider model selection[​](#step-4-consider-model-selection "Direct link to Step 4. Consider model selection")

*   **Smaller models for high-volume tasks**: Use models like Llama 3.1 8B for tasks that require higher throughput
*   **Large models for complex tasks**: Reserve Llama 3.1 405B for tasks that require maximum capability

## Monitoring and troubleshooting[​](#monitoring-and-troubleshooting "Direct link to Monitoring and troubleshooting")

Monitor your token usage patterns to optimize performance:

Python

    # Example: Log token usage for monitoringimport logginglogger = logging.getLogger(__name__)def log_token_usage(response):    usage = response.usage    logger.info(f"Input tokens: {usage.prompt_tokens}")    logger.info(f"Output tokens: {usage.completion_tokens}")    logger.info(f"Total tokens: {usage.total_tokens}")    # Alert if approaching limits    if usage.prompt_tokens > ITPM_LIMIT * 0.8:        logger.warning("Approaching ITPM limit")    if usage.completion_tokens > OTPM_LIMIT * 0.8:        logger.warning("Approaching OTPM limit")

### Handle rate limit errors[​](#handle-rate-limit-errors "Direct link to Handle rate limit errors")

When you exceed rate limits, the API returns a `429 Too Many Requests` error:

JSON

    {  "error": {    "message": "Rate limit exceeded: ITPM limit of 200,000 tokens reached",    "type": "rate_limit_exceeded",    "code": 429,    "limit_type": "input_tokens_per_minute",    "limit": 200000,    "current": 200150,    "retry_after": 15  }}

The error response includes:

*   `limit_type`: Which specific limit was exceeded (ITPM, OTPM, QPS, or QPH)
*   `limit`: The configured limit value
*   `current`: Your current usage
*   `retry_after`: Suggested wait time in seconds

### Common issues and solutions[​](#common-issues-and-solutions "Direct link to Common issues and solutions")

## Provisioned throughput limits[​](#provisioned-throughput-limits "Direct link to Provisioned throughput limits")

For production workloads that require higher limits, provisioned throughput endpoints offer:

*   **No TPM restrictions**: Processing capacity based on provisioned resources
*   **Higher rate limits**: Up to 200 queries per second per workspace
*   **Predictable performance**: Dedicated resources ensure consistent latency

### Output token limits[​](#output-token-limits "Direct link to Output token limits")

note

Starting May 15, 2026, Meta-Llama-3.1-405B-Instruct will be retired. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.

The following table summarizes the output token limits for each supported model:

### Additional limits[​](#additional-limits "Direct link to Additional limits")

The following are limitations for provisioned throughput workloads:

*   For provisioned throughput workloads that use **Llama 4 Maverick**:
    *   Support for this model on provisioned throughput workloads is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types).
    *   Autoscaling is not supported.
    *   Metrics panels are not supported.
    *   Traffic splitting is not supported on an endpoint that serves Llama 4 Maverick. You cannot serve multiple models on an endpoint that serves Llama 4 Maverick.
*   To deploy a Meta Llama model from `system.ai` in Unity Catalog, you must choose the applicable **Instruct** version. Base versions of the Meta Llama models are not supported for deployment from Unity Catalog. See [Deploy provisioned throughput endpoints](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis#uc).

## Regional availability and data processing[​](#regional-availability-and-data-processing "Direct link to Regional availability and data processing")

For Databricks-hosted foundation model region availability, see [Foundation Model overview](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview).

For data processing and residency details, see [Data processing and residency](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/compliance#data-process).

## Resource and payload limits for Foundation models and external models[​](#resource-and-payload-limits-for-foundation-models-and-external-models "Direct link to Resource and payload limits for Foundation models and external models")

The following tables summarize resource and payload limits for endpoints serving [foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#use-foundation-apis) and [external models](https://docs.databricks.com/aws/en/generative-ai/external-models/#supported).

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Foundation Model APIs overview](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/)
*   [Deploy provisioned throughput endpoints](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)
*   [Model Serving limits and regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits)
*   [API reference](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference)
