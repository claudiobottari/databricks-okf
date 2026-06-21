---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 128764cf8d9e00c06fc9d0f38fb5817db425fbb9d58ea9a7def2612969ee97f4
  pageDirectory: concepts
  sources:
    - route-optimization-on-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oauth-token-authentication-for-route-optimized-endpoints
    - OTAFRE
  citations:
    - file: route-optimization-on-serving-endpoints-databricks-on-aws.md
title: OAuth Token Authentication for Route-Optimized Endpoints
description: Route-optimized endpoints require Databricks in-house OAuth tokens instead of personal access tokens for authentication.
tags:
  - authentication
  - oauth
  - security
  - databricks
timestamp: "2026-06-19T20:15:42.987Z"
---

# OAuth Token Authentication for Route-Optimized Endpoints

**OAuth Token Authentication** is the required authentication mechanism for querying [Route-optimized serving endpoints](/concepts/route-optimized-serving-endpoints.md) on Databricks. When route optimization is enabled on a model serving or feature serving endpoint, the endpoint must be queried using a different URL and authentication method compared to non-optimized endpoints: only Databricks in-house OAuth tokens are supported. Personal access tokens (PATs) are not accepted for route-optimized endpoints.^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Requirements

To authenticate to a route-optimized endpoint, clients must obtain a valid Databricks in-house OAuth token. The token must be included in the request to the endpoint’s dedicated URL (which differs from the URL used for non-optimized endpoints). Detailed instructions for obtaining and using OAuth tokens are provided in the documentation for [Query route-optimized serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-route-optimization).^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Limitations

- **OAuth tokens only:** Databricks in-house OAuth tokens are the sole supported authentication method. Personal access tokens cannot be used.^[route-optimization-on-serving-endpoints-databricks-on-aws.md]
- Route-optimized endpoints are only available for custom model serving endpoints and feature serving endpoints; Foundation Model API and external model endpoints are not eligible for route optimization.^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Route Optimization on Serving Endpoints](/concepts/route-optimization-for-serving-endpoints.md)
- [Model Serving](/concepts/model-serving.md)
- Feature Serving
- OAuth Tokens (Databricks)
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md)
- Serving Endpoint Authentication

## Sources

- route-optimization-on-serving-endpoints-databricks-on-aws.md

# Citations

1. [route-optimization-on-serving-endpoints-databricks-on-aws.md](/references/route-optimization-on-serving-endpoints-databricks-on-aws-9093903f.md)
