---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e56b6b251419a1d247d110b784428c21410c7e0c4148abe5450bed065b7deb7
  pageDirectory: concepts
  sources:
    - query-route-optimized-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - route-optimized-endpoint-url
    - REU
  citations:
    - file: query-route-optimized-serving-endpoints-databricks-on-aws.md
title: Route-optimized endpoint URL
description: The dedicated URL format for route-optimized endpoints — https://<unique-id>.serving.cloud.databricks.com/<workspace-id>/serving-endpoints/<endpoint-name>/invocations — which provides the benefits of route optimization.
tags:
  - networking
  - serving
  - URL structure
timestamp: "2026-06-19T20:04:18.729Z"
---

# Route-optimized Endpoint URL

A **route-optimized endpoint URL** is a specialized invocation endpoint for Databricks model serving and feature serving endpoints that provides optimized routing for inference requests. Unlike standard workspace URLs, these endpoints are designed to reduce latency and improve reliability by routing traffic through a dedicated serving infrastructure rather than the general workspace gateway.

## Overview

When route optimization is enabled on a serving endpoint, the system creates a dedicated URL with the following structure:

`https://<unique-id>.serving.cloud.databricks.com/<workspace-id>/serving-endpoints/<endpoint-name>/invocations`

This URL differs from the standard workspace URL (`https://<databricks-workspace>/serving-endpoints/<endpoint-name>/invocations`) in that it routes requests through a dedicated serving layer rather than the workspace's general API gateway, providing performance benefits for inference workloads.^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Key Features

- **Dedicated serving infrastructure**: Requests are routed through specialized serving endpoints rather than the workspace API gateway
- **OAuth-only authentication**: Route-optimized endpoints require OAuth tokens for authentication; personal access tokens (PATs) are not supported
- **Unique endpoint ID**: The URL contains a unique alpha-numeric identifier (the `unique-id` portion) that serves as the endpoint's identifier for authentication purposes

## When to Use

Route-optimized URLs are recommended for production inference workloads where:
- Low latency is critical
- High throughput is required
- Consistent routing behavior is needed across large-scale deployments

## Authentication Requirements

### OAuth Token Requirement

All route-optimized endpoints must be queried using OAuth tokens. Databricks recommends using service principals for production applications to fetch OAuth tokens programmatically.^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### Key Authentication Components

When authenticating, you need:
1. **Endpoint ID**: The alpha-numeric identifier found in the hostname portion of the URL (e.g., `abcdefg` in `https://abcdefg.serving.cloud.databricks.com`)
2. **Action permission**: Either `query_inference_endpoint` or `manage_inference_endpoint`

## Migration Considerations

### Post-September 2025 Endpoints

Starting **September 22, 2025**, all newly created route-optimized endpoints:
- Must be queried exclusively through the route-optimized URL
- Do not support querying through the standard workspace URL

### Pre-September 2025 Endpoints

Endpoints created before September 22, 2025:
- Continue to support both invocation methods
- Can be queried via either the route-optimized URL or standard workspace URL

## Usage Examples

### REST API Query

```bash
URL="<endpoint-url>"
OAUTH_TOKEN="<token>"
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OAUTH_TOKEN" \
  --data "@data.json" \
  "$URL"
```

### Python SDK Integration

```python
from databricks.sdk import WorkspaceClient
import databricks.sdk.core as client

endpoint_name = "<Serving-Endpoint-Name>"

c = client.Config(
    host="<Workspace-Host>",
    client_id="<Client-Id>",
    client_secret="<Secret>"
)

w = WorkspaceClient(config=c)
response = w.serving_endpoints_data_plane.query(
    endpoint_name, 
    dataframe_records=....
)
```

## Related Concepts

- [Model Serving](/concepts/model-serving.md) - The broader concept of serving machine learning models
- Feature Serving - Serving feature store values for inference
- OAuth Authentication - The required authentication method for route-optimized endpoints
- Service Principal - Recommended identity for production applications
- [Serving Endpoint Permissions](/concepts/serving-endpoint-acls.md) - Access control for serving endpoints

## Sources

- query-route-optimized-serving-endpoints-databricks-on-aws.md

# Citations

1. [query-route-optimized-serving-endpoints-databricks-on-aws.md](/references/query-route-optimized-serving-endpoints-databricks-on-aws-d31d8879.md)
