---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 082bf18030b8669e3b78b7adca1d282b460f6a9271fa170984e62ee1012c2a92
  pageDirectory: concepts
  sources:
    - route-optimization-on-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - query-route-optimized-serving-endpoints
    - QRSE
    - Query Route‑Optimized Serving Endpoints
  citations:
    - file: route-optimization-on-serving-endpoints-databricks-on-aws.md
title: Query Route-Optimized Serving Endpoints
description: Route-optimized endpoints require a different URL and OAuth-based query pattern compared to non-optimized endpoints.
tags:
  - model-serving
  - api
  - networking
  - databricks
timestamp: "2026-06-19T20:15:42.725Z"
---

# Query Route-Optimized Serving Endpoints

**Query Route-Optimized Serving Endpoints** refers to the method of sending inference requests to Databricks model or feature serving endpoints that have route optimization enabled. These endpoints use a different URL and authentication mechanism compared to non-optimized endpoints. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Key Differences

- **URL**: Route-optimized endpoints are queried using a different URL than non-optimized endpoints. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]
- **Authentication**: Only Databricks in-house OAuth tokens are supported for authentication. Personal access tokens (PATs) are **not** supported. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Getting Started

When you create a route-optimized endpoint, Databricks sends a notification with the specific details required to query it. This includes the correct endpoint URL and instructions for obtaining and using OAuth tokens. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Authentication

Use Databricks in-house OAuth tokens to authenticate requests to route-optimized endpoints. Personal access tokens will be rejected. The authentication flow follows Databricks OAuth standards and must be configured accordingly in your client application. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Scope

Route-optimized querying is available for:
- Custom [model serving endpoints](/concepts/model-serving-endpoint.md).
- [Feature serving endpoints](/concepts/feature-serving-endpoint.md).

It is **not** available for endpoints using Foundation Model APIs or external models. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Additional Resources

For full query instructions, including example code and detailed steps, refer to the dedicated [Query route-optimized serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-route-optimization) article. ^[route-optimization-on-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- Feature Serving
- [Serving Endpoints](/concepts/serving-endpoint-acls.md)
- OAuth Token
- Route Optimization

## Sources

- route-optimization-on-serving-endpoints-databricks-on-aws.md

# Citations

1. [route-optimization-on-serving-endpoints-databricks-on-aws.md](/references/route-optimization-on-serving-endpoints-databricks-on-aws-9093903f.md)
