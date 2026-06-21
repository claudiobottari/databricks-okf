---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e46dcafe4c44793af0fa41c9cb18504e4fe2865067fe0b9c5cba1d5614f5f5ae
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limit-failure
    - RLF
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Rate Limit Failure
description: Request failures caused by exceeding the rate limits of a model serving endpoint, which can appear similar to timeouts.
tags:
  - databricks
  - model-serving
  - rate-limiting
  - throttling
timestamp: "2026-06-19T09:56:12.035Z"
---

# Rate Limit Failure

**Rate Limit Failure** occurs when the number of requests made to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) exceeds the allowed rate limit, causing subsequent requests to be rejected. This failure mode is relevant for both Databricks-hosted endpoints and third-party APIs used within model pipelines.

## Causes

Rate limit failures happen when clients send requests at a rate that exceeds the maximum allowed throughput for an endpoint. Multiple requests made over the rate limit of an endpoint might lead to failure for additional requests. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Identifying Rate Limit Failures

To determine if a failure is caused by rate limiting:

- Check the **Service Logs** for your endpoint for error messages related to rate limits.
- Examine **inference tables** if enabled, which may record rate limit errors.
- Review the error response from the endpoint, which typically indicates a rate limit has been exceeded. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Supported Rate Limits

Rate limits vary depending on the endpoint type. For specific rate limits based on endpoint types, consult the [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md) documentation for model serving endpoints. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Rate Limits for Third-Party Clients

When using third-party client APIs within model pipelines, such as those integrated through [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md), rate limits from those external services also apply. Databricks recommends reviewing the documentation of any third-party client used in your model pipeline to understand their rate limiting behavior. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Mitigation Strategies

- **Implement retry with backoff**: Configure your client to retry failed requests after a delay, reducing the effective request rate.
- **Throttle request rate**: Limit the number of requests your client sends per second to stay within the endpoint's rate limit.
- **Scale your endpoint**: For [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md), increasing the number of serving replicas can increase the effective rate limit.
- **Monitor usage**: Track request rates and rate limit errors using Model Serving Logs and inference tables to detect approaching limits before failures occur.

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md)
- [Server-Side Timeouts](/concepts/server-side-timeouts.md)
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md)
- [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md)
- Model Serving Logs

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
